# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_epg20260715 import models as main_models
from darabonba.model import DaraModel

class AttachEgressProxyRuleGroupsToConfigurationRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        egress_proxy_configuration_id: str = None,
        egress_proxy_rule_groups: List[main_models.AttachEgressProxyRuleGroupsToConfigurationRequestEgressProxyRuleGroups] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > Note If you do not specify this parameter, the system automatically uses the RequestId of the API request as the client token. The RequestId of each API request is different.
        self.client_token = client_token
        # Specifies whether to perform only a dry run. Valid values:
        # 
        # - **true**: performs a dry run and does not attach the egress proxy rule groups. The system checks whether required parameters are specified, the request format is valid, and the service limits are met. If the request fails the dry run, an error message is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # 
        # - **false** (default): sends a normal request. If the request passes the check, the system returns an HTTP 2xx status code and performs the operation.
        self.dry_run = dry_run
        # The ID of the egress proxy configuration.
        # 
        # This parameter is required.
        self.egress_proxy_configuration_id = egress_proxy_configuration_id
        # The list of egress proxy rule group references to be attached to the egress proxy configuration.
        # 
        # This parameter is required.
        self.egress_proxy_rule_groups = egress_proxy_rule_groups

    def validate(self):
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

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.egress_proxy_configuration_id is not None:
            result['EgressProxyConfigurationId'] = self.egress_proxy_configuration_id

        result['EgressProxyRuleGroups'] = []
        if self.egress_proxy_rule_groups is not None:
            for k1 in self.egress_proxy_rule_groups:
                result['EgressProxyRuleGroups'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EgressProxyConfigurationId') is not None:
            self.egress_proxy_configuration_id = m.get('EgressProxyConfigurationId')

        self.egress_proxy_rule_groups = []
        if m.get('EgressProxyRuleGroups') is not None:
            for k1 in m.get('EgressProxyRuleGroups'):
                temp_model = main_models.AttachEgressProxyRuleGroupsToConfigurationRequestEgressProxyRuleGroups()
                self.egress_proxy_rule_groups.append(temp_model.from_map(k1))

        return self

class AttachEgressProxyRuleGroupsToConfigurationRequestEgressProxyRuleGroups(DaraModel):
    def __init__(
        self,
        egress_proxy_rule_group_id: str = None,
        priority: int = None,
    ):
        # The ID of the egress proxy rule group.
        # 
        # This parameter is required.
        self.egress_proxy_rule_group_id = egress_proxy_rule_group_id
        # The priority of the egress proxy rule group in the egress proxy configuration. Valid values: 1 to 1000. A smaller value indicates a higher priority.
        # 
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

