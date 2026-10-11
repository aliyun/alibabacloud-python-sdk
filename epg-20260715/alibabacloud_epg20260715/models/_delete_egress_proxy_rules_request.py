# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteEgressProxyRulesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        egress_proxy_rule_group_id: str = None,
        egress_proxy_rule_ids: List[str] = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > Note: If you do not specify this parameter, the system automatically uses the request ID of the API request as the client token. The request ID of each API request is unique.
        self.client_token = client_token
        # Specifies whether to perform only a dry run on the request. Valid values:
        # 
        # - **true**: performs only a dry run and does not delete the rules. The system checks whether required parameters are specified, the request format is valid, and the service limits are met. If the request fails the dry run, an error message is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # 
        # - **false** (default): performs a dry run and sends the actual request. If the request passes the dry run, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the egress proxy rule group.
        # 
        # This parameter is required.
        self.egress_proxy_rule_group_id = egress_proxy_rule_group_id
        # The IDs of the egress proxy rules.
        # 
        # This parameter is required.
        self.egress_proxy_rule_ids = egress_proxy_rule_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.egress_proxy_rule_group_id is not None:
            result['EgressProxyRuleGroupId'] = self.egress_proxy_rule_group_id

        if self.egress_proxy_rule_ids is not None:
            result['EgressProxyRuleIds'] = self.egress_proxy_rule_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EgressProxyRuleGroupId') is not None:
            self.egress_proxy_rule_group_id = m.get('EgressProxyRuleGroupId')

        if m.get('EgressProxyRuleIds') is not None:
            self.egress_proxy_rule_ids = m.get('EgressProxyRuleIds')

        return self

