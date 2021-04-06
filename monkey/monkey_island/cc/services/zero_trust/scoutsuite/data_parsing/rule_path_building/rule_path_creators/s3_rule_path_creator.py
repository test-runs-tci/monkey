from monkey_island.cc.services.zero_trust.scoutsuite.consts.rule_names.s3_rules import S3Rules
from monkey_island.cc.services.zero_trust.scoutsuite.consts.service_consts import SERVICE_TYPES
from monkey_island.cc.services.zero_trust.scoutsuite.data_parsing.rule_path_building.abstract_rule_path_creator import (
    AbstractRulePathCreator,
)


class S3RulePathCreator(AbstractRulePathCreator):

    service_type = SERVICE_TYPES.S3
    supported_rules = S3Rules
