# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceInspectionsRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        engine: str = None,
        instance_area: str = None,
        page_no: str = None,
        page_size: str = None,
        resource_group_id: str = None,
        search_map: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # >  The end time must be later than the start time.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The database engine. Valid values:
        # 
        # *   **MySQL**
        # *   **Redis**
        # *   **PolarDBMySQL**
        # 
        # This parameter is required.
        self.engine = engine
        # The type of the instance on which the database is deployed. Valid values:
        # 
        # *   **RDS**: an Alibaba Cloud database instance.
        # *   **ECS**: an ECS instance on which a self-managed database is deployed.
        # *   **IDC**: a self-managed database instance that is not deployed on Alibaba Cloud.
        # 
        # >  The value IDC specifies that the instance is deployed in a data center.
        # 
        # This parameter is required.
        self.instance_area = instance_area
        # The page number. The value must be a positive integer. Default value: 1.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of entries per page. Default value: 10.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The filter condition, which can be specified in one of the following formats:
        # 
        # *   Specify the ID of a single instance in the {"InstanceId":"Instance ID"} format.
        # *   Specify the IDs of multiple instances in the {"InstanceIds":["Instance ID1","Instance ID2"]} format. Separate the instance IDs with commas (,).
        # *   Specify the region in which the instance resides in the {"region":"Region of the instance"} format.
        self.search_map = search_map
        # The beginning of the time range to query. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
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

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.instance_area is not None:
            result['InstanceArea'] = self.instance_area

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.search_map is not None:
            result['SearchMap'] = self.search_map

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('InstanceArea') is not None:
            self.instance_area = m.get('InstanceArea')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SearchMap') is not None:
            self.search_map = m.get('SearchMap')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

