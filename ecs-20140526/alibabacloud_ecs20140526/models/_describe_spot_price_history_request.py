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
        # The end of the time range to query the historical prices of spot instances. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        # 
        # Default value: null, which indicates the current time.
        self.end_time = end_time
        # The instance type.
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # Specifies whether the spot instance is I/O optimized. Valid values:
        # 
        # - optimized: The spot instance is an I/O optimization instance.
        # 
        # - none: The spot instance is not an I/O optimization instance.
        # 
        # Default value for Generation I instance families: none.
        # 
        # Default value for other instance families: optimized.
        self.io_optimized = io_optimized
        # The network type of the spot instance. Valid values:
        # 
        # - vpc: virtual private cloud (VPC).
        # - classic: classic network. This feature has been retired. For more information, see [Retirement notice](https://help.aliyun.com/document_detail/2833134.html).
        # 
        # This parameter is required.
        self.network_type = network_type
        # The type of the operating system platform. Valid values:
        # 
        # - linux.
        # - windows.
        self.ostype = ostype
        # The row from which the query starts.
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
        # - 1: After a spot instance is created, Alibaba Cloud ensures that the instance is not automatically released within 1 hour. After 1 hour, the system compares the bid price with the market price and checks the resource inventory to determine whether to retain automatic release the instance.
        # - 0: After a spot instance is created, Alibaba Cloud does not ensure that the instance runs for 1 hour. The system compares the bid price with the market price and checks the resource inventory to determine whether to retain automatic release the instance.
        # 
        # Alibaba Cloud sends an ECS system event notification 5 minutes before the instance is released. Spot instances are billed by second. Specify an appropriate protection period based on the expected task execution duration.
        # 
        # > This parameter takes effect only when SpotStrategy is set to SpotWithPriceLimit or SpotAsPriceGo.
        self.spot_duration = spot_duration
        # The beginning of the time range to query the historical prices of spot instances. The maximum time range between the start time and end time is 30 days. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        # 
        # Default value: null, which indicates 3 hours before the end time.
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

