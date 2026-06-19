# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeAccessPointsResponseBody(DaraModel):
    def __init__(
        self,
        access_point_set: main_models.DescribeAccessPointsResponseBodyAccessPointSet = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.access_point_set = access_point_set
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.access_point_set:
            self.access_point_set.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point_set is not None:
            result['AccessPointSet'] = self.access_point_set.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointSet') is not None:
            temp_model = main_models.DescribeAccessPointsResponseBodyAccessPointSet()
            self.access_point_set = temp_model.from_map(m.get('AccessPointSet'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAccessPointsResponseBodyAccessPointSet(DaraModel):
    def __init__(
        self,
        access_point_type: List[main_models.DescribeAccessPointsResponseBodyAccessPointSetAccessPointType] = None,
    ):
        self.access_point_type = access_point_type

    def validate(self):
        if self.access_point_type:
            for v1 in self.access_point_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccessPointType'] = []
        if self.access_point_type is not None:
            for k1 in self.access_point_type:
                result['AccessPointType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_point_type = []
        if m.get('AccessPointType') is not None:
            for k1 in m.get('AccessPointType'):
                temp_model = main_models.DescribeAccessPointsResponseBodyAccessPointSetAccessPointType()
                self.access_point_type.append(temp_model.from_map(k1))

        return self

class DescribeAccessPointsResponseBodyAccessPointSetAccessPointType(DaraModel):
    def __init__(
        self,
        access_point_id: str = None,
        attached_region_no: str = None,
        description: str = None,
        host_operator: str = None,
        location: str = None,
        name: str = None,
        status: str = None,
        type: str = None,
    ):
        self.access_point_id = access_point_id
        self.attached_region_no = attached_region_no
        self.description = description
        self.host_operator = host_operator
        self.location = location
        self.name = name
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

        if self.attached_region_no is not None:
            result['AttachedRegionNo'] = self.attached_region_no

        if self.description is not None:
            result['Description'] = self.description

        if self.host_operator is not None:
            result['HostOperator'] = self.host_operator

        if self.location is not None:
            result['Location'] = self.location

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

        if m.get('AttachedRegionNo') is not None:
            self.attached_region_no = m.get('AttachedRegionNo')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HostOperator') is not None:
            self.host_operator = m.get('HostOperator')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

