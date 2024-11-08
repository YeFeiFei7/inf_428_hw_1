import unittest
import pandas as pd

from task_2 import calculate_aggregated_threat

class TestAggregatedThreatFunction(unittest.TestCase):

    def setUp(self):
        data = {
            'Department': ['HR', 'HR', 'IT', 'IT', 'Finance', 'Finance'],
            'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
            'Threat_Score': [30, 40, 50, 60, 70, 80],
            'Department_Importance': [1, 1, 2, 2, 3, 3]
        }
        self.df = pd.DataFrame(data)

    def test_calculate_aggregated_threat(self):
        # test correctness of result
        result = calculate_aggregated_threat(self.df)
        # expected result: HR-35，IT-55，Finance-75
        expected_result = (35 * 1 + 55 * 2 + 75 * 3) / (1 + 2 + 3)
        self.assertEqual(result, round(expected_result, 2))

    def test_edge_case_identical_threat_scores(self):
        # test if all emp scores are same
        data = {
            'Department': ['HR', 'HR', 'IT', 'IT', 'Finance', 'Finance'],
            'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
            'Threat_Score': [50, 50, 50, 50, 50, 50],
            'Department_Importance': [1, 1, 2, 2, 3, 3]
        }
        df = pd.DataFrame(data)
        result = calculate_aggregated_threat(df)
        expected_result = (50 * 1 + 50 * 2 + 50 * 3) / (1 + 2 + 3)
        self.assertEqual(result, expected_result)  # all threat scores are same

    def test_edge_case_zero_importance(self):
        # test if all  importances are o
        data = {
            'Department': ['HR', 'HR', 'IT', 'IT', 'Finance', 'Finance'],
            'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
            'Threat_Score': [30, 40, 50, 60, 70, 80],
            'Department_Importance': [0, 0, 0, 0, 0, 0]
        }
        df = pd.DataFrame(data)
        result = calculate_aggregated_threat(df)
        self.assertEqual(result, 0)  # threat scores should be 0
