# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAggregateResourceComplianceByConfigRuleRequest(DaraModel):
    def __init__(
        self,
        aggregator_id: str = None,
        compliance_type: str = None,
        config_rule_id: str = None,
        resource_account_id: int = None,
        resource_owner_id: int = None,
    ):
        # The ID of the account group.
        # 
        # For more information about how to obtain the ID of the account group, see [ListAggregators](https://help.aliyun.com/document_detail/255797.html).
        # 
        # This parameter is required.
        self.aggregator_id = aggregator_id
        # The compliance evaluation result of the resources. Valid values:
        # 
        # *   COMPLIANT: The resource is evaluated as compliant.
        # *   NON_COMPLIANT: The resource is evaluated as incompliant.
        # *   NOT_APPLICABLE: The rule does not apply to your resources.
        # *   INSUFFICIENT_DATA: No resource data is available.
        self.compliance_type = compliance_type
        # The ID of the rule.
        # 
        # For more information about how to obtain the ID of a rule, see [ListAggregateConfigRules](https://help.aliyun.com/document_detail/264148.html).
        # 
        # This parameter is required.
        self.config_rule_id = config_rule_id
        # The ID of the Alibaba Cloud account to which the resources in the account group belong.
        # 
        # > You can use either the ResourceAccountId or ResourceOwnerId parameter. We recommend that you use the ResourceAccountId parameter.
        self.resource_account_id = resource_account_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type

        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id

        if self.resource_account_id is not None:
            result['ResourceAccountId'] = self.resource_account_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')

        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')

        if m.get('ResourceAccountId') is not None:
            self.resource_account_id = m.get('ResourceAccountId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

