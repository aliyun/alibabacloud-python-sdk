# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEcGrantRelationRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
        page_number: int = None,
        page_size: int = None,
        vbr_region_no: str = None,
    ):
        # The instance ID of the instance for which you want to query the authorization relationship.
        # 
        # - If **InstanceType** is set to **VBR**, set this parameter to the instance ID of the VBR instance.
        # 
        # - If **InstanceType** is set to **VPC**, set this parameter to the instance ID of the VPC-connected instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The type of the instance for which you want to query the authorization relationship. Valid values:
        # 
        # - **VBR**: Virtual Border vRouter (VBR) instance used for routing. Queries the VPC-connected instances that have authorized the VBR instance.
        # - **VPC**: Virtual Private Cloud (VPC) instance. Queries the VBR instances that the VPC-connected instance has authorized.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page for paging in a paged query. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size
        # The region ID of the VBR instance for which you want to query the authorization relationship.
        # 
        # - If **InstanceType** is set to **VBR**, this parameter is required.
        # 
        # - If **InstanceType** is set to **VPC**, this parameter is not required.
        self.vbr_region_no = vbr_region_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.vbr_region_no is not None:
            result['VbrRegionNo'] = self.vbr_region_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('VbrRegionNo') is not None:
            self.vbr_region_no = m.get('VbrRegionNo')

        return self

