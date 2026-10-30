# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class CreateRouteMapRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        direction: str = None,
        dry_run: bool = None,
        name: str = None,
        priority: int = None,
        resource_group_id: str = None,
        tag: List[main_models.CreateRouteMapRequestTag] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate a parameter value on your client to ensure that the value is unique across different requests. The client token only supports ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request may be different.
        self.client_token = client_token
        # The description of the route map.
        # 
        # The description can be empty or 1 to 256 characters in length. It cannot start with `http://` or `https://`.
        self.description = description
        # The direction of the route map. Valid values:
        # 
        # - **Inbound**: inbound. The direction in which the instance route table receives routes from the associated network instance. This affects the routes that the current instance can learn from the associated network instance.
        # - **Outbound**: outbound. The direction in which the instance route table sends routes to the associated network instance. This affects the routes that the current instance advertises to the associated network instance.
        # 
        # This parameter is required.
        self.direction = direction
        # Specifies whether to perform a dry run on the request, including permission and instance status checks. Valid values:
        # 
        # - **false** (default): sends a normal request. After the check is passed, the route map is directly created.
        # - **true**: sends a dry run request. Only the check is performed, and the route map is not created. Check items include whether required parameters are specified and the request format. If the check fails, the corresponding error is returned. If the check is passed, the error code `DryRunOperation` is returned.
        self.dry_run = dry_run
        # The name of the route map.
        # 
        # The name can be empty or 1 to 128 characters in length. It cannot start with `http://` or `https://`.
        self.name = name
        # Policy priority of the route map. Valid values: **1** to **100**. A smaller value indicates a higher priority.
        # 
        # > Policy priority of a route map must be unique within an Alibaba Cloud account. When a route map is executed, the system matches route map rules starting from the route map with the smallest priority value based on policy priority of the route map rules. Therefore, when you specify policy priority of a route map, make sure that policy priority meets your expected matching order.
        # 
        # This parameter is required.
        self.priority = priority
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tag information.
        # 
        # You can specify up to 20 tags at a time.
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

        if self.description is not None:
            result['Description'] = self.description

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.name is not None:
            result['Name'] = self.name

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateRouteMapRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateRouteMapRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource.
        # 
        # If you specify this parameter, it cannot be an empty string. The tag key can be up to 64 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        # 
        # You can specify up to 20 tag keys at a time.
        self.key = key
        # The tag value of the resource.
        # 
        # If you specify this parameter, it cannot be empty. The tag value can be up to 128 characters in length. It cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        # 
        # Each tag key corresponds to a tag value. You can specify up to 20 tag values at a time.
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

