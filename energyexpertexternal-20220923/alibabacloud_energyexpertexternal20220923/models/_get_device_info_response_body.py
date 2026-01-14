# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class GetDeviceInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetDeviceInfoResponseBodyData = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The code returned for the request. A value of Success indicates that the request was successful. Other values indicate that the request failed. You can troubleshoot the error by viewing the error message returned.
        self.code = code
        # The data returned.
        self.data = data
        # The HTTP status code.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetDeviceInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetDeviceInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        device_id: str = None,
        device_name: str = None,
        first_type_name: str = None,
        record_list: List[main_models.GetDeviceInfoResponseBodyDataRecordList] = None,
        second_type_name: str = None,
    ):
        # The ID of the device.
        self.device_id = device_id
        # The name of the device.
        self.device_name = device_name
        # The level 1 meter type.
        self.first_type_name = first_type_name
        # The device parameters.
        self.record_list = record_list
        # The level 2 meter type.
        self.second_type_name = second_type_name

    def validate(self):
        if self.record_list:
            for v1 in self.record_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_id is not None:
            result['deviceId'] = self.device_id

        if self.device_name is not None:
            result['deviceName'] = self.device_name

        if self.first_type_name is not None:
            result['firstTypeName'] = self.first_type_name

        result['recordList'] = []
        if self.record_list is not None:
            for k1 in self.record_list:
                result['recordList'].append(k1.to_map() if k1 else None)

        if self.second_type_name is not None:
            result['secondTypeName'] = self.second_type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')

        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')

        if m.get('firstTypeName') is not None:
            self.first_type_name = m.get('firstTypeName')

        self.record_list = []
        if m.get('recordList') is not None:
            for k1 in m.get('recordList'):
                temp_model = main_models.GetDeviceInfoResponseBodyDataRecordList()
                self.record_list.append(temp_model.from_map(k1))

        if m.get('secondTypeName') is not None:
            self.second_type_name = m.get('secondTypeName')

        return self

class GetDeviceInfoResponseBodyDataRecordList(DaraModel):
    def __init__(
        self,
        identifier: str = None,
        param_name: str = None,
        statistics_date: str = None,
        type: str = None,
        unit: str = None,
        value: float = None,
    ):
        # The device identifier.
        self.identifier = identifier
        # The parameter name.
        self.param_name = param_name
        # The date on which the statistics were collected.
        self.statistics_date = statistics_date
        # The type of the measuring point.
        self.type = type
        # The unit of the parameter value.
        self.unit = unit
        # The value of the measuring point.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identifier is not None:
            result['identifier'] = self.identifier

        if self.param_name is not None:
            result['paramName'] = self.param_name

        if self.statistics_date is not None:
            result['statisticsDate'] = self.statistics_date

        if self.type is not None:
            result['type'] = self.type

        if self.unit is not None:
            result['unit'] = self.unit

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')

        if m.get('paramName') is not None:
            self.param_name = m.get('paramName')

        if m.get('statisticsDate') is not None:
            self.statistics_date = m.get('statisticsDate')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

