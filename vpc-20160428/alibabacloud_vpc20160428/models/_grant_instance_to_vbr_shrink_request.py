# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrantInstanceToVbrShrinkRequest(DaraModel):
    def __init__(
        self,
        grant_type: str = None,
        instance_id: str = None,
        region_id: str = None,
        vbr_instance_ids_shrink: str = None,
        vbr_owner_uid: int = None,
        vbr_region_no: str = None,
    ):
        # The scope of VBR instances that accept the authorization. Valid values:
        # 
        # - **All**: Grants authorization of the VPC instance to all VBR instances in the specified region under the specified Alibaba Cloud account. In this case, the **VbrInstanceIds** parameter can be left empty.
        # - **Specify**: Grants authorization of the VPC instance to the specified VBR instances. In this case, the **VbrInstanceIds** parameter is required.
        # 
        # This parameter is required.
        self.grant_type = grant_type
        # The ID of the VPC instance for which authorization is to be granted.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the VPC instance for which authorization is to be granted.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The list of VBR instances to be granted authorization.
        self.vbr_instance_ids_shrink = vbr_instance_ids_shrink
        # The Alibaba Cloud account ID that owns the VBR instance to be granted authorization.
        # 
        # This parameter is required.
        self.vbr_owner_uid = vbr_owner_uid
        # The region ID of the VBR instance to be granted authorization.
        # 
        # This parameter is required.
        self.vbr_region_no = vbr_region_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.grant_type is not None:
            result['GrantType'] = self.grant_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vbr_instance_ids_shrink is not None:
            result['VbrInstanceIds'] = self.vbr_instance_ids_shrink

        if self.vbr_owner_uid is not None:
            result['VbrOwnerUid'] = self.vbr_owner_uid

        if self.vbr_region_no is not None:
            result['VbrRegionNo'] = self.vbr_region_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GrantType') is not None:
            self.grant_type = m.get('GrantType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VbrInstanceIds') is not None:
            self.vbr_instance_ids_shrink = m.get('VbrInstanceIds')

        if m.get('VbrOwnerUid') is not None:
            self.vbr_owner_uid = m.get('VbrOwnerUid')

        if m.get('VbrRegionNo') is not None:
            self.vbr_region_no = m.get('VbrRegionNo')

        return self

