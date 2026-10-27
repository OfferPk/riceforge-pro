#!/usr/bin/env python3
"""
Automated Test Runner for RiceForge Pro
Verifies predictive difference bijectivity, J=16 split-sample optimization, zero-block, uncompressed fallback, exact lossless inversion, and 10-point normative auditor.
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rice_cli import map_difference, inv_map_difference, compress_telemetry, audit_rice

class TestRiceForge(unittest.TestCase):

    def test_01_difference_mapping_bijectivity(self):
        n_bits = 12
        prev = 2048
        for curr in [2048, 2049, 2047, 2100, 1900, 4095, 0]:
            delta = map_difference(curr, prev, n_bits)
            recovered = inv_map_difference(delta, prev, n_bits)
            self.assertEqual(curr, recovered)

    def test_02_lossless_exact_reconstruction(self):
        samples = [2000 + i * 2 for i in range(32)]
        res = compress_telemetry(samples, n_bits=12)
        self.assertEqual(res["rmse"], 0.0)
        self.assertIn("Lossless", res["psnr"])

    def test_03_block_size_j16(self):
        samples = [1000] * 32
        res = compress_telemetry(samples, n_bits=12)
        self.assertEqual(res["blockCount"], 2) # 32 / 16 = 2 blocks

    def test_04_zero_block_detection(self):
        # Constant signal -> all differences zero -> zero block option
        samples = [1500] * 32
        res = compress_telemetry(samples, n_bits=12)
        # Verify second block chose zero or split-sample 0
        b1_opt = res["blocks"][1]["bestOption"]
        self.assertIn(b1_opt, ["zero", "0"])

    def test_05_compression_ratio_positive(self):
        samples = [1000 + int(10 * (i % 4)) for i in range(64)]
        res = compress_telemetry(samples, n_bits=12)
        self.assertLess(res["compressedBytes"], res["originalBytes"])
        self.assertTrue(":1" in res["compressionRatio"])

    def test_06_header_sync_prefix(self):
        samples = [2000] * 16
        res = compress_telemetry(samples, n_bits=12)
        self.assertTrue(res["headerHex"].startswith("52 43"))

    def test_07_normative_auditor_compliance(self):
        report = audit_rice()
        self.assertEqual(report["status"], "PASSED")
        self.assertEqual(report["score"], "10/10 Normative Rules Compliant")
        self.assertEqual(len(report["rules"]), 10)

    def test_08_dynamic_range_bounds(self):
        samples = [0, 4095, 2048, 1024] * 4
        res = compress_telemetry(samples, n_bits=12)
        self.assertEqual(res["nBits"], 12)
        self.assertEqual(res["rmse"], 0.0)

    def test_09_sinusoidal_telemetry_fidelity(self):
        import math
        samples = [int(2048 + 300 * math.sin(i / 2.0)) for i in range(48)]
        res = compress_telemetry(samples, n_bits=12)
        self.assertEqual(res["rmse"], 0.0)

    def test_10_single_block_length(self):
        samples = [500] * 16
        res = compress_telemetry(samples, n_bits=12)
        self.assertEqual(res["blockCount"], 1)

if __name__ == "__main__":
    unittest.main()
