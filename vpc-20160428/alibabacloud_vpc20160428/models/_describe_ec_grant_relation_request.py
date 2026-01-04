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
        # The ID of the instance.
        # 
        # *   If you set **InstanceType** to **VBR**, specify a VBR ID.
        # *   If you set **InstanceType** to **VPC**, specify a VPC ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The type of instance. Valid values:
        # 
        # *   **VBR**: queries the permissions that are granted to a VBR.
        # *   **VPC**: queries the permissions that are granted from a VPC.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Maximum value: **50**. Default value: **10**.
        self.page_size = page_size
        # The ID of the region where the instance is deployed.
        # 
        # *   If **InstanceType** is set to **VBR**, this parameter is required.
        # *   If **InstanceType** is set to **VPC**, you can ignore this parameter.
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

