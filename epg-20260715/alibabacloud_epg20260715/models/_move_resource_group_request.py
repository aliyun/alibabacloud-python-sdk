# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MoveResourceGroupRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        new_resource_group_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > Note: If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId of each API request is different.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run. The system checks the request for potential issues, including missing required parameters, incorrect request format, and service limits. The resource group is not modified. If the request fails the dry run, an error message is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # 
        # - **false** (default): sends a normal request. If the request passes the check, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The ID of the destination resource group.
        # 
        # This parameter is required.
        self.new_resource_group_id = new_resource_group_id
        # The resource ID.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type. Valid values:
        # 
        # - **EgressProxyGateway**: egress proxy gateway instance.
        # - **EgressProxyConfiguration**: egress configuration.
        # - **EgressProxyRuleGroup**: egress rule group.
        # 
        # This parameter is required.
        self.resource_type = resource_type

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

        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

