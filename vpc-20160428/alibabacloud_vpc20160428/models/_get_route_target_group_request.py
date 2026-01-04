# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class GetRouteTargetGroupRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        route_target_group_id: str = None,
        tag: List[main_models.GetRouteTargetGroupRequestTag] = None,
    ):
        # Client token, used to ensure idempotence of the request.
        # 
        # Generate a parameter value from your client and ensure that it is unique across different requests. ClientToken only supports ASCII characters.
        # 
        # > If you do not specify this, the system automatically uses the **RequestId** of the API request as the **ClientToken** identifier. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # ID of the region to which the route target group belongs. You can obtain the region ID by calling the DescribeRegions interface.
        # 
        # This parameter is required.
        self.region_id = region_id
        # ID of the route target group member instance.
        # 
        # This parameter is required.
        self.route_target_group_id = route_target_group_id
        # Tag information.
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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.route_target_group_id is not None:
            result['RouteTargetGroupId'] = self.route_target_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RouteTargetGroupId') is not None:
            self.route_target_group_id = m.get('RouteTargetGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.GetRouteTargetGroupRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class GetRouteTargetGroupRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Resource tag key. Up to 20 tag keys are supported. If you need to pass this value, you cannot input an empty string.
        # 
        # A tag key can have up to 128 characters and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # Resource tag value. Up to 20 tag values are supported. If you need to pass this value, you can input an empty string.
        # 
        # A tag value can have up to 128 characters and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
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

