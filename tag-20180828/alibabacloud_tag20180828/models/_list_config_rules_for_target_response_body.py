# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_tag20180828 import models as main_models
from darabonba.model import DaraModel

class ListConfigRulesForTargetResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListConfigRulesForTargetResponseBodyData] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The tag detection tasks.
        self.data = data
        # Indicates whether the next query is required.
        # 
        # - If the value of this parameter is empty (`"NextToken": ""`), all results are returned, and the next query is not required.
        # 
        # - If the value of this parameter is not empty, the next query is required, and the value is the token used to start the next query.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListConfigRulesForTargetResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListConfigRulesForTargetResponseBodyData(DaraModel):
    def __init__(
        self,
        aggregator_id: str = None,
        config_rule_id: str = None,
        policy_type: str = None,
        remediation: bool = None,
        tag_key: str = None,
        tag_value: str = None,
        target_id: str = None,
        target_type: str = None,
    ):
        # The ID of the account group.
        # 
        # You can use the ID to query the content of the related resource non-compliance report in Cloud Config.
        # 
        # > This parameter is returned only if you use the Tag Policy feature in multi-account mode.
        self.aggregator_id = aggregator_id
        # The ID of the rule.
        self.config_rule_id = config_rule_id
        # The use scenario of the tag policy. Valid values:
        # 
        # - tags: enables tags with specified tag values to be added to resources.
        # 
        # - rg_inherit: enables resources in a resource group to automatically inherit tags from the resource group.
        self.policy_type = policy_type
        # Indicates whether automatic remediation is enabled. Valid values:
        # 
        # - true
        # 
        # - false
        self.remediation = remediation
        # The tag key.
        self.tag_key = tag_key
        # The tag value for automatic remediation.
        self.tag_value = tag_value
        # The ID of the object.
        self.target_id = target_id
        # The type of the object. Valid values:
        # 
        # - USER: the current logon account. This value is available if you use the Tag Policy feature in single-account mode.
        # 
        # - ROOT: the Root folder in the resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # 
        # - FOLDER: a folder other than the Root folder in the resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        # 
        # - ACCOUNT: a member in the resource directory. This value is available if you use the Tag Policy feature in multi-account mode.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.remediation is not None:
            result['Remediation'] = self.remediation

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('Remediation') is not None:
            self.remediation = m.get('Remediation')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

