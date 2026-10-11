# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DetachEgressProxyRuleGroupsFromConfigurationRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        egress_proxy_configuration_id: str = None,
        egress_proxy_rule_group_ids: List[str] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > Note If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId of each API request is unique.
        self.client_token = client_token
        # Specifies whether to perform only a dry run on the request. Valid values:
        # 
        # - **true**: Sends a check request and does not disassociate the egress proxy rule groups. The check items include whether the required parameters are specified, the request format, and service limits. If the check fails, the corresponding error is returned. If the check succeeds, the DryRunOperation error code is returned.
        # 
        # - **false** (default): Sends a normal request. After the check succeeds, an HTTP 2xx status code is returned and the operation is directly executed.
        self.dry_run = dry_run
        # The ID of the egress proxy configuration.
        # 
        # This parameter is required.
        self.egress_proxy_configuration_id = egress_proxy_configuration_id
        # The IDs of the egress proxy rule groups to be disassociated from the egress proxy configuration.
        # 
        # This parameter is required.
        self.egress_proxy_rule_group_ids = egress_proxy_rule_group_ids

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

        if self.egress_proxy_configuration_id is not None:
            result['EgressProxyConfigurationId'] = self.egress_proxy_configuration_id

        if self.egress_proxy_rule_group_ids is not None:
            result['EgressProxyRuleGroupIds'] = self.egress_proxy_rule_group_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EgressProxyConfigurationId') is not None:
            self.egress_proxy_configuration_id = m.get('EgressProxyConfigurationId')

        if m.get('EgressProxyRuleGroupIds') is not None:
            self.egress_proxy_rule_group_ids = m.get('EgressProxyRuleGroupIds')

        return self

