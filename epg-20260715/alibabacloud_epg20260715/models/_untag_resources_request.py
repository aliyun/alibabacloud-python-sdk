# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UntagResourcesRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        client_token: str = None,
        dry_run: bool = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to remove all tags from the resources. Valid values:
        # 
        # - **true**: Removes all tags from the resources.
        # - **false** (default): Does not remove all tags from the resources.
        self.all = all
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate the client token on the client side. Make sure that the client token is unique across different requests. The client token can only contain ASCII characters.
        # 
        # > Note: If you do not specify this parameter, the system automatically uses the RequestId of the API request as the client token. The RequestId of each API request is different.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: Performs a dry run. The system checks the request without removing the resource tags. Check items include whether required parameters are specified, the request format, and service limits. If the check fails, the corresponding error is returned. If the check succeeds, the DryRunOperation error code is returned.
        # 
        # - **false** (default): Performs a normal request. If the check succeeds, an HTTP 2xx status code is returned and the operation is directly executed.
        self.dry_run = dry_run
        # The list of resource IDs. You can specify up to 50 resource IDs in a single call.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type. Valid values:
        # 
        # - **EgressProxyGateway**: egress proxy gateway instance
        # - **EgressProxyIpPool**: egress proxy IP address pool
        # - **EgressProxyConfiguration**: egress proxy configuration
        # - **EgressProxyRuleGroup**: egress proxy rule group
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The list of tag keys to remove. You can remove up to 20 tags in a single call.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all is not None:
            result['All'] = self.all

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        return self

