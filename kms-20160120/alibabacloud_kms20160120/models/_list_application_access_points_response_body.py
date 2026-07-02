# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_kms20160120 import models as main_models
from darabonba.model import DaraModel

class ListApplicationAccessPointsResponseBody(DaraModel):
    def __init__(
        self,
        application_access_points: main_models.ListApplicationAccessPointsResponseBodyApplicationAccessPoints = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.application_access_points = application_access_points
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.application_access_points:
            self.application_access_points.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_access_points is not None:
            result['ApplicationAccessPoints'] = self.application_access_points.to_map()

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
        if m.get('ApplicationAccessPoints') is not None:
            temp_model = main_models.ListApplicationAccessPointsResponseBodyApplicationAccessPoints()
            self.application_access_points = temp_model.from_map(m.get('ApplicationAccessPoints'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListApplicationAccessPointsResponseBodyApplicationAccessPoints(DaraModel):
    def __init__(
        self,
        application_access_point: List[main_models.ListApplicationAccessPointsResponseBodyApplicationAccessPointsApplicationAccessPoint] = None,
    ):
        self.application_access_point = application_access_point

    def validate(self):
        if self.application_access_point:
            for v1 in self.application_access_point:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplicationAccessPoint'] = []
        if self.application_access_point is not None:
            for k1 in self.application_access_point:
                result['ApplicationAccessPoint'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.application_access_point = []
        if m.get('ApplicationAccessPoint') is not None:
            for k1 in m.get('ApplicationAccessPoint'):
                temp_model = main_models.ListApplicationAccessPointsResponseBodyApplicationAccessPointsApplicationAccessPoint()
                self.application_access_point.append(temp_model.from_map(k1))

        return self

class ListApplicationAccessPointsResponseBodyApplicationAccessPointsApplicationAccessPoint(DaraModel):
    def __init__(
        self,
        authentication_method: str = None,
        name: str = None,
    ):
        self.authentication_method = authentication_method
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authentication_method is not None:
            result['AuthenticationMethod'] = self.authentication_method

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthenticationMethod') is not None:
            self.authentication_method = m.get('AuthenticationMethod')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

