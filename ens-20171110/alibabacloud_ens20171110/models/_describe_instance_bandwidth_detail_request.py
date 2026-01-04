# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstanceBandwidthDetailRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        ens_region_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
        page_number: int = None,
        page_size: int = None,
        service_type: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query. The maximum interval between the beginning time and the end time is 86400 seconds. The interval is left-closed and right-open. Specify the time in the yyyy-MM-dd HH:mm:ss format.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the ENS node.
        self.ens_region_id = ens_region_id
        # The plan ID.
        self.instance_id = instance_id
        # The type of the instance, such as vm, eip, single_tenant, and nc. You can leave this parameter empty. The type of the instance, such as vm, eip, single_tenant, and nc.
        self.instance_type = instance_type
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 200.
        self.page_size = page_size
        # The type of the service, such as vm, eip, esk, and meta.
        self.service_type = service_type
        # The beginning of the time range to query. Specify the time in the yyyy-MM-dd HH:mm:ss format.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

