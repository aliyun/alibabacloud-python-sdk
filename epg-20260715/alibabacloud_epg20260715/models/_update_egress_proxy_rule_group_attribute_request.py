# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateEgressProxyRuleGroupAttributeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        egress_proxy_ip_pool_id: str = None,
        egress_proxy_rule_group_id: str = None,
        egress_proxy_rule_group_name: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.dry_run = dry_run
        self.egress_proxy_ip_pool_id = egress_proxy_ip_pool_id
        # This parameter is required.
        self.egress_proxy_rule_group_id = egress_proxy_rule_group_id
        self.egress_proxy_rule_group_name = egress_proxy_rule_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.egress_proxy_ip_pool_id is not None:
            result['EgressProxyIpPoolId'] = self.egress_proxy_ip_pool_id

        if self.egress_proxy_rule_group_id is not None:
            result['EgressProxyRuleGroupId'] = self.egress_proxy_rule_group_id

        if self.egress_proxy_rule_group_name is not None:
            result['EgressProxyRuleGroupName'] = self.egress_proxy_rule_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EgressProxyIpPoolId') is not None:
            self.egress_proxy_ip_pool_id = m.get('EgressProxyIpPoolId')

        if m.get('EgressProxyRuleGroupId') is not None:
            self.egress_proxy_rule_group_id = m.get('EgressProxyRuleGroupId')

        if m.get('EgressProxyRuleGroupName') is not None:
            self.egress_proxy_rule_group_name = m.get('EgressProxyRuleGroupName')

        return self

