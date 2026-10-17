from pathlib import Path
import unittest
from analyze import abbott, analyze, read_observations, two_point_crossing


class AnalysisTests(unittest.TestCase):
    def test_control_adjustment(self):
        self.assertAlmostEqual(abbott(0.5, 0.1), 4 / 9)

    def test_invalid_control(self):
        with self.assertRaises(ValueError):
            abbott(0.5, 1)

    def test_report_values_and_endpoint_sensitivity(self):
        rows = read_observations(Path(__file__).parents[1] / "data/observations.csv")
        summary = analyze(rows)
        self.assertAlmostEqual(summary["primary"]["descriptive_50_percent_crossing_nominal_ppm"], 42.51, places=2)
        self.assertAlmostEqual(summary["endpoint_sensitivity"]["descriptive_50_percent_crossing_nominal_ppm"], 42.97, places=2)

    def test_wrong_group_count(self):
        with self.assertRaises(ValueError):
            two_point_crossing([40], [0.5])

    def test_nonincreasing_response(self):
        with self.assertRaises(ValueError):
            two_point_crossing([40, 100], [0.8, 0.4])


if __name__ == "__main__":
    unittest.main()
