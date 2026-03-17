# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSmartAGByAccessPointRequest(DaraModel):
    def __init__(
        self,
        access_point_id: int = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        smart_agstatus: str = None,
    ):
        # The ID of the access point.
        # 
        # This parameter is required.
        self.access_point_id = access_point_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. Pages start from page 1. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: **10**. Maximum value: **50** .
        self.page_size = page_size
        # The ID of the region where the SAG instance is deployed.
        # 
        # A region contains one or more access points. You can call the [ListAccessPoints](https://help.aliyun.com/document_detail/183876.html) operation to query access points in a specific region.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The status of the SAG instance. Valid values:
        # 
        # *   **Active**: The SAG device is connected to Alibaba Cloud.
        # *   **offline**: The SAG device is disconnected from Alibaba Cloud.
        self.smart_agstatus = smart_agstatus

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.smart_agstatus is not None:
            result['SmartAGStatus'] = self.smart_agstatus

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SmartAGStatus') is not None:
            self.smart_agstatus = m.get('SmartAGStatus')

        return self

