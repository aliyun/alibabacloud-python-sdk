# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_epg20260715 import models as main_models
from darabonba.model import DaraModel

class GetEgressProxyConfigurationAttributeResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        default_rule_phase_actions: main_models.GetEgressProxyConfigurationAttributeResponseBodyDefaultRulePhaseActions = None,
        description: str = None,
        egress_proxy_configuration_id: str = None,
        egress_proxy_configuration_name: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        rule_groups: List[main_models.GetEgressProxyConfigurationAttributeResponseBodyRuleGroups] = None,
        status: str = None,
        tags: List[main_models.GetEgressProxyConfigurationAttributeResponseBodyTags] = None,
    ):
        # The creation time of the egress proxy configuration. The time is displayed in UTC in the yyyy-MM-ddTHH:mm:ssZ format.
        self.create_time = create_time
        # The default actions executed in each effective phase (PreDns, PreRequest, and PostResponse) when traffic does not match any rules.
        self.default_rule_phase_actions = default_rule_phase_actions
        # The description of the egress proxy configuration. The description must be 2 to 256 characters in length and can contain Chinese characters, letters, digits, hyphens (-), forward slashes (/), periods (.), and underscores (_).
        self.description = description
        # The ID of the egress proxy configuration.
        self.egress_proxy_configuration_id = egress_proxy_configuration_id
        # The name of the egress proxy configuration. The name must be 2 to 128 characters in length and must start with a letter or a Chinese character. It can contain digits, periods (.), underscores (_), and hyphens (-).
        self.egress_proxy_configuration_name = egress_proxy_configuration_name
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The list of egress rule group references associated with the egress proxy configuration.
        self.rule_groups = rule_groups
        # The status of the egress proxy configuration. Valid values:
        # 
        # - **Provisioning**: The configuration is being created.
        # 
        # - **Available**: The configuration is available.
        # 
        # - **Configuring**: The configuration is being modified.
        self.status = status
        # The list of tags.
        self.tags = tags

    def validate(self):
        if self.default_rule_phase_actions:
            self.default_rule_phase_actions.validate()
        if self.rule_groups:
            for v1 in self.rule_groups:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.default_rule_phase_actions is not None:
            result['DefaultRulePhaseActions'] = self.default_rule_phase_actions.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.egress_proxy_configuration_id is not None:
            result['EgressProxyConfigurationId'] = self.egress_proxy_configuration_id

        if self.egress_proxy_configuration_name is not None:
            result['EgressProxyConfigurationName'] = self.egress_proxy_configuration_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['RuleGroups'] = []
        if self.rule_groups is not None:
            for k1 in self.rule_groups:
                result['RuleGroups'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DefaultRulePhaseActions') is not None:
            temp_model = main_models.GetEgressProxyConfigurationAttributeResponseBodyDefaultRulePhaseActions()
            self.default_rule_phase_actions = temp_model.from_map(m.get('DefaultRulePhaseActions'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EgressProxyConfigurationId') is not None:
            self.egress_proxy_configuration_id = m.get('EgressProxyConfigurationId')

        if m.get('EgressProxyConfigurationName') is not None:
            self.egress_proxy_configuration_name = m.get('EgressProxyConfigurationName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.rule_groups = []
        if m.get('RuleGroups') is not None:
            for k1 in m.get('RuleGroups'):
                temp_model = main_models.GetEgressProxyConfigurationAttributeResponseBodyRuleGroups()
                self.rule_groups.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetEgressProxyConfigurationAttributeResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class GetEgressProxyConfigurationAttributeResponseBodyTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The key can be up to 128 characters in length. It cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. The value can be up to 256 characters in length and cannot contain `http://` or `https://`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetEgressProxyConfigurationAttributeResponseBodyRuleGroups(DaraModel):
    def __init__(
        self,
        egress_proxy_rule_group_id: str = None,
        priority: int = None,
    ):
        # The ID of the egress rule group.
        self.egress_proxy_rule_group_id = egress_proxy_rule_group_id
        # The priority of the egress rule group in the egress proxy configuration. Valid values: 1 to 1000. A smaller value indicates a higher priority.
        self.priority = priority

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.egress_proxy_rule_group_id is not None:
            result['EgressProxyRuleGroupId'] = self.egress_proxy_rule_group_id

        if self.priority is not None:
            result['Priority'] = self.priority

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EgressProxyRuleGroupId') is not None:
            self.egress_proxy_rule_group_id = m.get('EgressProxyRuleGroupId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        return self

class GetEgressProxyConfigurationAttributeResponseBodyDefaultRulePhaseActions(DaraModel):
    def __init__(
        self,
        post_response: str = None,
        pre_dns: str = None,
        pre_request: str = None,
    ):
        # The default action executed in the PostResponse phase (after a response is returned) when traffic does not match any rules. This phase only supports the value **Allow** (default), which indicates that the traffic is allowed.
        self.post_response = post_response
        # The default action executed in the PreDns phase (before DNS resolution) when traffic does not match any rules. Valid values:
        # 
        # - **Allow** (default): allows the traffic.
        # 
        # - **Deny**: denies the traffic.
        self.pre_dns = pre_dns
        # The default action executed in the PreRequest phase (before a request is forwarded) when traffic does not match any rules. Valid values:
        # 
        # - **Allow** (default): allows the traffic.
        # 
        # - **Deny**: denies the traffic.
        self.pre_request = pre_request

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.post_response is not None:
            result['PostResponse'] = self.post_response

        if self.pre_dns is not None:
            result['PreDns'] = self.pre_dns

        if self.pre_request is not None:
            result['PreRequest'] = self.pre_request

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PostResponse') is not None:
            self.post_response = m.get('PostResponse')

        if m.get('PreDns') is not None:
            self.pre_dns = m.get('PreDns')

        if m.get('PreRequest') is not None:
            self.pre_request = m.get('PreRequest')

        return self

