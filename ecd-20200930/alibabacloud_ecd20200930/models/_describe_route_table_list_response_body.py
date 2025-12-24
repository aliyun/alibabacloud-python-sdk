# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeRouteTableListResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        route_table_list: List[main_models.DescribeRouteTableListResponseBodyRouteTableList] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.route_table_list = route_table_list

    def validate(self):
        if self.route_table_list:
            for v1 in self.route_table_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RouteTableList'] = []
        if self.route_table_list is not None:
            for k1 in self.route_table_list:
                result['RouteTableList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.route_table_list = []
        if m.get('RouteTableList') is not None:
            for k1 in m.get('RouteTableList'):
                temp_model = main_models.DescribeRouteTableListResponseBodyRouteTableList()
                self.route_table_list.append(temp_model.from_map(k1))

        return self

class DescribeRouteTableListResponseBodyRouteTableList(DaraModel):
    def __init__(
        self,
        associate_type: str = None,
        route_table_id: str = None,
        route_table_type: str = None,
        router_type: str = None,
        status: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        self.associate_type = associate_type
        self.route_table_id = route_table_id
        self.route_table_type = route_table_type
        self.router_type = router_type
        self.status = status
        self.v_switch_ids = v_switch_ids
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.associate_type is not None:
            result['AssociateType'] = self.associate_type

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        if self.route_table_type is not None:
            result['RouteTableType'] = self.route_table_type

        if self.router_type is not None:
            result['RouterType'] = self.router_type

        if self.status is not None:
            result['Status'] = self.status

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssociateType') is not None:
            self.associate_type = m.get('AssociateType')

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        if m.get('RouteTableType') is not None:
            self.route_table_type = m.get('RouteTableType')

        if m.get('RouterType') is not None:
            self.router_type = m.get('RouterType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

