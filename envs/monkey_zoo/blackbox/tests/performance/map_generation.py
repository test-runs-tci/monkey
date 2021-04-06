from datetime import timedelta

from envs.monkey_zoo.blackbox.tests.exploitation import ExploitationTest
from envs.monkey_zoo.blackbox.tests.performance.performance_test import PerformanceTest
from envs.monkey_zoo.blackbox.tests.performance.performance_test_config import PerformanceTestConfig
from envs.monkey_zoo.blackbox.tests.performance.performance_test_workflow import (
    PerformanceTestWorkflow,
)

MAX_ALLOWED_SINGLE_PAGE_TIME = timedelta(seconds=2)
MAX_ALLOWED_TOTAL_TIME = timedelta(seconds=5)

MAP_RESOURCES = [
    "api/netmap",
]


class MapGenerationTest(PerformanceTest):

    TEST_NAME = "Map generation performance test"

    def __init__(
        self, island_client, raw_config, analyzers, timeout, log_handler, break_on_timeout
    ):
        self.island_client = island_client
        exploitation_test = ExploitationTest(
            MapGenerationTest.TEST_NAME, island_client, raw_config, analyzers, timeout, log_handler
        )
        performance_config = PerformanceTestConfig(
            max_allowed_single_page_time=MAX_ALLOWED_SINGLE_PAGE_TIME,
            max_allowed_total_time=MAX_ALLOWED_TOTAL_TIME,
            endpoints_to_test=MAP_RESOURCES,
            break_on_timeout=break_on_timeout,
        )
        self.performance_test_workflow = PerformanceTestWorkflow(
            MapGenerationTest.TEST_NAME, exploitation_test, performance_config
        )

    def run(self):
        self.performance_test_workflow.run()
