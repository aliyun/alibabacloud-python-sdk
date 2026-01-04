# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeGlobalAccelerationInstancesRequest(DaraModel):
    def __init__(
        self,
        bandwidth_type: str = None,
        global_acceleration_instance_id: str = None,
        include_reservation_data: bool = None,
        ip_address: str = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        server_id: str = None,
        service_location: str = None,
        status: str = None,
    ):
        # The bandwidth type of the GA instance. Valid values:
        # 
        # *   **Sharing**
        # *   **Exclusive** (default)
        self.bandwidth_type = bandwidth_type
        # The ID of the GA instance.
        self.global_acceleration_instance_id = global_acceleration_instance_id
        # Specifies whether to return information about pending orders. Valid values:
        # 
        # *   **false** (default)
        # *   **true**
        self.include_reservation_data = include_reservation_data
        # The public IP address of the GA instance.
        self.ip_address = ip_address
        # The name of the GA instance.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: **100**. Default value: **10**.
        self.page_size = page_size
        # The region ID of the GA instance. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the backend service instance.
        self.server_id = server_id
        # The region of the backend service. Valid values:
        # 
        # *   **china-mainland**
        # *   **north-america**
        # *   **asia-pacific**
        # *   **europe**
        self.service_location = service_location
        # The status of the GA instance. Valid values:
        # 
        # *   **Available**
        # *   **Inuse**
        # *   **Associating**
        # *   **Unassociating**
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_type is not None:
            result['BandwidthType'] = self.bandwidth_type

        if self.global_acceleration_instance_id is not None:
            result['GlobalAccelerationInstanceId'] = self.global_acceleration_instance_id

        if self.include_reservation_data is not None:
            result['IncludeReservationData'] = self.include_reservation_data

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.name is not None:
            result['Name'] = self.name

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

        if self.server_id is not None:
            result['ServerId'] = self.server_id

        if self.service_location is not None:
            result['ServiceLocation'] = self.service_location

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthType') is not None:
            self.bandwidth_type = m.get('BandwidthType')

        if m.get('GlobalAccelerationInstanceId') is not None:
            self.global_acceleration_instance_id = m.get('GlobalAccelerationInstanceId')

        if m.get('IncludeReservationData') is not None:
            self.include_reservation_data = m.get('IncludeReservationData')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('Name') is not None:
            self.name = m.get('Name')

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

        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')

        if m.get('ServiceLocation') is not None:
            self.service_location = m.get('ServiceLocation')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

