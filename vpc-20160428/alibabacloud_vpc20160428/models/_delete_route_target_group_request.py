# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DeleteRouteTargetGroupRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        force_delete: bool = None,
        region_id: str = None,
        route_target_group_id: str = None,
        tag: List[main_models.DeleteRouteTargetGroupRequestTag] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may differ for each API request.
        self.client_token = client_token
        self.force_delete = force_delete
        # The ID of the region where the resource group resides.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The routing target group instance ID.
        # 
        # This parameter is required.
        self.route_target_group_id = route_target_group_id
        # The tags of the resource.
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

        if self.force_delete is not None:
            result['ForceDelete'] = self.force_delete

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

        if m.get('ForceDelete') is not None:
            self.force_delete = m.get('ForceDelete')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RouteTargetGroupId') is not None:
            self.route_target_group_id = m.get('RouteTargetGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DeleteRouteTargetGroupRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DeleteRouteTargetGroupRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 128 characters in length. It cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the resource. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length. It cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
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

