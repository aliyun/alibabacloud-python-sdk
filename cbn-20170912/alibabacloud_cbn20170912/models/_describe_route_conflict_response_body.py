# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribeRouteConflictResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        route_conflicts: main_models.DescribeRouteConflictResponseBodyRouteConflicts = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # A list of overlapping routes.
        self.route_conflicts = route_conflicts
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.route_conflicts:
            self.route_conflicts.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.route_conflicts is not None:
            result['RouteConflicts'] = self.route_conflicts.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RouteConflicts') is not None:
            temp_model = main_models.DescribeRouteConflictResponseBodyRouteConflicts()
            self.route_conflicts = temp_model.from_map(m.get('RouteConflicts'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeRouteConflictResponseBodyRouteConflicts(DaraModel):
    def __init__(
        self,
        route_conflict: List[main_models.DescribeRouteConflictResponseBodyRouteConflictsRouteConflict] = None,
    ):
        self.route_conflict = route_conflict

    def validate(self):
        if self.route_conflict:
            for v1 in self.route_conflict:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RouteConflict'] = []
        if self.route_conflict is not None:
            for k1 in self.route_conflict:
                result['RouteConflict'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.route_conflict = []
        if m.get('RouteConflict') is not None:
            for k1 in m.get('RouteConflict'):
                temp_model = main_models.DescribeRouteConflictResponseBodyRouteConflictsRouteConflict()
                self.route_conflict.append(temp_model.from_map(k1))

        return self

class DescribeRouteConflictResponseBodyRouteConflictsRouteConflict(DaraModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        instance_id: str = None,
        instance_type: str = None,
        region_id: str = None,
        status: str = None,
    ):
        # The destination CIDR block of the overlapping route.
        self.destination_cidr_block = destination_cidr_block
        # The ID of the peer network instance on which the overlapping routes are found.
        self.instance_id = instance_id
        # The type of the peer network instance on which the overlapping routes are found.
        # 
        # *   **VPC**: VPC
        # *   **VBR**: VBR
        # *   **CCN**: CCN instance
        self.instance_type = instance_type
        # The region ID of the peer network instance on which the overlapping routes are found is deployed.
        self.region_id = region_id
        # The cause of the route error. Valid values:
        # 
        # *   **conflict**: The routes have the same destination CIDR block.
        # *   **overflow**: The number of routes in the route table configured on another network instance has reached the upper limit.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

