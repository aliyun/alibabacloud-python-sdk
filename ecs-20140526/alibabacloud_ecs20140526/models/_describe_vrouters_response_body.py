# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeVRoutersResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vrouters: main_models.DescribeVRoutersResponseBodyVRouters = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.vrouters = vrouters

    def validate(self):
        if self.vrouters:
            self.vrouters.validate()

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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.vrouters is not None:
            result['VRouters'] = self.vrouters.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('VRouters') is not None:
            temp_model = main_models.DescribeVRoutersResponseBodyVRouters()
            self.vrouters = temp_model.from_map(m.get('VRouters'))

        return self

class DescribeVRoutersResponseBodyVRouters(DaraModel):
    def __init__(
        self,
        vrouter: List[main_models.DescribeVRoutersResponseBodyVRoutersVRouter] = None,
    ):
        self.vrouter = vrouter

    def validate(self):
        if self.vrouter:
            for v1 in self.vrouter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VRouter'] = []
        if self.vrouter is not None:
            for k1 in self.vrouter:
                result['VRouter'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vrouter = []
        if m.get('VRouter') is not None:
            for k1 in m.get('VRouter'):
                temp_model = main_models.DescribeVRoutersResponseBodyVRoutersVRouter()
                self.vrouter.append(temp_model.from_map(k1))

        return self

class DescribeVRoutersResponseBodyVRoutersVRouter(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        region_id: str = None,
        route_table_ids: main_models.DescribeVRoutersResponseBodyVRoutersVRouterRouteTableIds = None,
        vrouter_id: str = None,
        vrouter_name: str = None,
        vpc_id: str = None,
    ):
        self.creation_time = creation_time
        self.description = description
        self.region_id = region_id
        self.route_table_ids = route_table_ids
        self.vrouter_id = vrouter_id
        self.vrouter_name = vrouter_name
        self.vpc_id = vpc_id

    def validate(self):
        if self.route_table_ids:
            self.route_table_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.route_table_ids is not None:
            result['RouteTableIds'] = self.route_table_ids.to_map()

        if self.vrouter_id is not None:
            result['VRouterId'] = self.vrouter_id

        if self.vrouter_name is not None:
            result['VRouterName'] = self.vrouter_name

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RouteTableIds') is not None:
            temp_model = main_models.DescribeVRoutersResponseBodyVRoutersVRouterRouteTableIds()
            self.route_table_ids = temp_model.from_map(m.get('RouteTableIds'))

        if m.get('VRouterId') is not None:
            self.vrouter_id = m.get('VRouterId')

        if m.get('VRouterName') is not None:
            self.vrouter_name = m.get('VRouterName')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeVRoutersResponseBodyVRoutersVRouterRouteTableIds(DaraModel):
    def __init__(
        self,
        route_table_id: List[str] = None,
    ):
        self.route_table_id = route_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        return self

