# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisableCenVbrHealthCheckRequest(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        vbr_instance_id: str = None,
        vbr_instance_owner_id: int = None,
        vbr_instance_region_id: str = None,
    ):
        # The ID of the Cloud Enterprise Network (CEN) instance.
        # 
        # This parameter is required.
        self.cen_id = cen_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the VBR.
        # 
        # This parameter is required.
        self.vbr_instance_id = vbr_instance_id
        # The ID of the Alibaba Cloud account to which the VBR belongs.
        # 
        # > This parameter is required if the VBR and the CEN instance belong to different Alibaba Cloud accounts.
        self.vbr_instance_owner_id = vbr_instance_owner_id
        # The ID of the region where the VBR is deployed.
        # 
        # You can call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.vbr_instance_region_id = vbr_instance_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.vbr_instance_id is not None:
            result['VbrInstanceId'] = self.vbr_instance_id

        if self.vbr_instance_owner_id is not None:
            result['VbrInstanceOwnerId'] = self.vbr_instance_owner_id

        if self.vbr_instance_region_id is not None:
            result['VbrInstanceRegionId'] = self.vbr_instance_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('VbrInstanceId') is not None:
            self.vbr_instance_id = m.get('VbrInstanceId')

        if m.get('VbrInstanceOwnerId') is not None:
            self.vbr_instance_owner_id = m.get('VbrInstanceOwnerId')

        if m.get('VbrInstanceRegionId') is not None:
            self.vbr_instance_region_id = m.get('VbrInstanceRegionId')

        return self

