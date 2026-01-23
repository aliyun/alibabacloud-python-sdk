# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetStandardStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetStandardStatisticsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetStandardStatisticsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetStandardStatisticsResponseBodyData(DaraModel):
    def __init__(
        self,
        standard_type_count_list: List[main_models.GetStandardStatisticsResponseBodyDataStandardTypeCountList] = None,
        total_count: int = None,
    ):
        self.standard_type_count_list = standard_type_count_list
        self.total_count = total_count

    def validate(self):
        if self.standard_type_count_list:
            for v1 in self.standard_type_count_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['StandardTypeCountList'] = []
        if self.standard_type_count_list is not None:
            for k1 in self.standard_type_count_list:
                result['StandardTypeCountList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.standard_type_count_list = []
        if m.get('StandardTypeCountList') is not None:
            for k1 in m.get('StandardTypeCountList'):
                temp_model = main_models.GetStandardStatisticsResponseBodyDataStandardTypeCountList()
                self.standard_type_count_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class GetStandardStatisticsResponseBodyDataStandardTypeCountList(DaraModel):
    def __init__(
        self,
        count: int = None,
        standard_type: str = None,
    ):
        self.count = count
        self.standard_type = standard_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.standard_type is not None:
            result['StandardType'] = self.standard_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('StandardType') is not None:
            self.standard_type = m.get('StandardType')

        return self

