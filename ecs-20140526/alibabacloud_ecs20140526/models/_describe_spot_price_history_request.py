# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSpotPriceHistoryRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        instance_type: str = None,
        io_optimized: str = None,
        network_type: str = None,
        ostype: str = None,
        offset: int = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        spot_duration: int = None,
        start_time: str = None,
        zone_id: str = None,
    ):
        # The end time to query the historical prices of spot instances. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        # 
        # Default value: empty. An empty value indicates the current time.
        self.end_time = end_time
        # The instance type.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # Specifies whether the spot instance is an I/O optimized instance. Valid values:
        # 
        # - optimized: The spot instance is an I/O optimized instance.
        # 
        # - none: The spot instance is a non-I/O optimized instance.
        # 
        # Default value for Generation I instances: none.
        # 
        # Default value for other instance family types: optimized.
        self.io_optimized = io_optimized
        # The network type of the spot instance. Valid values:
        # 
        # - vpc: VPC.
        # - classic: classic network. This feature is retired. For more information, see [Retirement notice](https://help.aliyun.com/document_detail/2833134.html).
        # 
        # This parameter is required.
        self.network_type = network_type
        # The operating system platform of the instance. Valid values:
        # 
        # - linux
        # - windows
        self.ostype = ostype
        # The starting row for the query.
        # 
        # Default value: 0.
        self.offset = offset
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the instance. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The protection period of the spot instance. Unit: hours. Default value: 1. Valid values:
        # - 1: Alibaba Cloud guarantees that the instance is not automatically released within 1 hour after it is created. After 1 hour, the system automatically compares your bid with the market price and checks resource inventory to determine whether to retain or revoke the instance.
        # - 0: Alibaba Cloud does not guarantee that the instance runs for 1 hour after it is created. The system automatically compares your bid with the market price and checks resource inventory to determine whether to retain or revoke the instance.
        # 
        # Alibaba Cloud sends you a notification through an ECS system event 5 minutes before the instance is revoked. Spot instances are billed by the second. Select an appropriate protection period based on the execution duration of specific tasks.
        # 
        # > This parameter takes effect only when SpotStrategy is set to SpotWithPriceLimit or SpotAsPriceGo.
        self.spot_duration = spot_duration
        # The start time to query the historical prices of spot instances. The time span between the start time and the specified end time cannot exceed 30 days. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        # 
        # Default value: empty. An empty value indicates 3 hours before the end time.
        self.start_time = start_time
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.ostype is not None:
            result['OSType'] = self.ostype

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

