# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_epg20260715 import models as main_models
from darabonba.model import DaraModel

class TagResourcesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[main_models.TagResourcesRequestTag] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > Note If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId of each API request is unique.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run and does not attach tags to resources. The system checks whether required parameters are specified, the request format is valid, and service limits are met. If the request fails the dry run, an error is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # 
        # - **false** (default): does not perform a dry run. The system sends a normal request. If the request passes the check, an HTTP 2xx status code is returned and the operation is performed.
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
        # The list of tags. You can specify up to 20 tags in a single call.
        # 
        # This parameter is required.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
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

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class TagResourcesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The key can be up to 128 characters in length, cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        # 
        # This parameter is required.
        self.key = key
        # The tag value. The value can be up to 256 characters in length and cannot contain `http://` or `https://`.
        # 
        # This parameter is required.
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

