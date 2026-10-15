import unittest

from ab_test import compare_conversion_rates


class CompareConversionRatesTests(unittest.TestCase):
    def test_equal_rates_have_no_evidence_of_a_difference(self):
        control_rate, variant_rate, p_value = compare_conversion_rates(100, 10, 200, 20)

        self.assertEqual(control_rate, variant_rate)
        self.assertAlmostEqual(p_value, 1.0)

    def test_larger_samples_can_detect_a_clear_difference(self):
        _, _, p_value = compare_conversion_rates(10_000, 1_000, 10_000, 1_500)

        self.assertLess(p_value, 0.05)

    def test_rejects_impossible_conversion_counts(self):
        with self.assertRaises(ValueError):
            compare_conversion_rates(100, 101, 100, 10)


if __name__ == "__main__":
    unittest.main()
