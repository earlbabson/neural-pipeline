import unittest

from neural_pipeline.train_config.train_config import MetricsGroup

__all__ = ['NeuralPipelineTest']


class NeuralPipelineTest(unittest.TestCase):
    def test_metrics(self):
        metrics_group_lv1 = MetricsGroup('lvl')
        metrics_group_lv2 = MetricsGroup('lv2')
        metrics_group_lv1.add(metrics_group_lv2)
        self.assertRaises(MetricsGroup.MetricsGroupException, lambda: metrics_group_lv2.add(MetricsGroup('lv3')))

        metrics_group_lv1 = MetricsGroup('lvl')
        metrics_group_lv2 = MetricsGroup('lv2')
        metrics_group_lv3 = MetricsGroup('lv2')
        metrics_group_lv2.add(metrics_group_lv3)
        self.assertRaises(MetricsGroup.MetricsGroupException, lambda: metrics_group_lv1.add(metrics_group_lv2))


if __name__ == '__main__':
    unittest.main()