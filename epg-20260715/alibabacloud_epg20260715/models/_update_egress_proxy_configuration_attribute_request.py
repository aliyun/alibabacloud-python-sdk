# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_epg20260715 import models as main_models
from darabonba.model import DaraModel

class UpdateEgressProxyConfigurationAttributeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        default_rule_phase_actions: main_models.UpdateEgressProxyConfigurationAttributeRequestDefaultRulePhaseActions = None,
        description: str = None,
        dry_run: bool = None,
        egress_proxy_configuration_id: str = None,
        egress_proxy_configuration_name: str = None,
        egress_proxy_rule_groups: List[main_models.UpdateEgressProxyConfigurationAttributeRequestEgressProxyRuleGroups] = None,
    ):
        self.client_token = client_token
        self.default_rule_phase_actions = default_rule_phase_actions
        self.description = description
        self.dry_run = dry_run
        # This parameter is required.
        self.egress_proxy_configuration_id = egress_proxy_configuration_id
        self.egress_proxy_configuration_name = egress_proxy_configuration_name
        self.egress_proxy_rule_groups = egress_proxy_rule_groups

    def validate(self):
        if self.default_rule_phase_actions:
            self.default_rule_phase_actions.validate()
        if self.egress_proxy_rule_groups:
            for v1 in self.egress_proxy_rule_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.default_rule_phase_actions is not None:
            result['DefaultRulePhaseActions'] = self.default_rule_phase_actions.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.egress_proxy_configuration_id is not None:
            result['EgressProxyConfigurationId'] = self.egress_proxy_configuration_id

        if self.egress_proxy_configuration_name is not None:
            result['EgressProxyConfigurationName'] = self.egress_proxy_configuration_name

        result['EgressProxyRuleGroups'] = []
        if self.egress_proxy_rule_groups is not None:
            for k1 in self.egress_proxy_rule_groups:
                result['EgressProxyRuleGroups'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DefaultRulePhaseActions') is not None:
            temp_model = main_models.UpdateEgressProxyConfigurationAttributeRequestDefaultRulePhaseActions()
            self.default_rule_phase_actions = temp_model.from_map(m.get('DefaultRulePhaseActions'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EgressProxyConfigurationId') is not None:
            self.egress_proxy_configuration_id = m.get('EgressProxyConfigurationId')

        if m.get('EgressProxyConfigurationName') is not None:
            self.egress_proxy_configuration_name = m.get('EgressProxyConfigurationName')

        self.egress_proxy_rule_groups = []
        if m.get('EgressProxyRuleGroups') is not None:
            for k1 in m.get('EgressProxyRuleGroups'):
                temp_model = main_models.UpdateEgressProxyConfigurationAttributeRequestEgressProxyRuleGroups()
                self.egress_proxy_rule_groups.append(temp_model.from_map(k1))

        return self

class UpdateEgressProxyConfigurationAttributeRequestEgressProxyRuleGroups(DaraModel):
    def __init__(
        self,
        egress_proxy_rule_group_id: str = None,
        priority: int = None,
    ):
        # This parameter is required.
        self.egress_proxy_rule_group_id = egress_proxy_rule_group_id
        # This parameter is required.
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

class UpdateEgressProxyConfigurationAttributeRequestDefaultRulePhaseActions(DaraModel):
    def __init__(
        self,
        post_response: str = None,
        pre_dns: str = None,
        pre_request: str = None,
    ):
        # This parameter is required.
        self.post_response = post_response
        # This parameter is required.
        self.pre_dns = pre_dns
        # This parameter is required.
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

