from common.configuration import AgentConfiguration, PluginConfiguration

from .noop_test_configuration import noop_test_configuration
from .utils import add_exploiters, add_subnets, add_tcp_ports, replace_agent_configuration


def _add_exploiters(agent_configuration: AgentConfiguration) -> AgentConfiguration:
    brute_force = [PluginConfiguration(name="SmbExploiter", options={})]
    vulnerability = [PluginConfiguration(name="ZerologonExploiter", options={})]

    return add_exploiters(agent_configuration, brute_force=brute_force, vulnerability=vulnerability)


def _add_tcp_ports(agent_configuration: AgentConfiguration) -> AgentConfiguration:
    tcp_ports = [135, 445]
    return add_tcp_ports(agent_configuration, tcp_ports)


def _add_subnets(agent_configuration: AgentConfiguration) -> AgentConfiguration:
    subnets = ["10.2.2.25"]
    return add_subnets(agent_configuration, subnets)


agent_configuration = _add_exploiters(
    _add_tcp_ports(_add_subnets(noop_test_configuration.agent_configuration))
)
zerologon_test_configuration = replace_agent_configuration(
    noop_test_configuration, agent_configuration
)
