# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListMeasureDataResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        measure_datas: List[main_models.ListMeasureDataResponseBodyMeasureDatas] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The metering results.
        self.measure_datas = measure_datas
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.measure_datas:
            for v1 in self.measure_datas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['MeasureDatas'] = []
        if self.measure_datas is not None:
            for k1 in self.measure_datas:
                result['MeasureDatas'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.measure_datas = []
        if m.get('MeasureDatas') is not None:
            for k1 in m.get('MeasureDatas'):
                temp_model = main_models.ListMeasureDataResponseBodyMeasureDatas()
                self.measure_datas.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListMeasureDataResponseBodyMeasureDatas(DaraModel):
    def __init__(
        self,
        component_code: str = None,
        domain_code: str = None,
        end_time: int = None,
        start_time: int = None,
        usage: int = None,
    ):
        # The measurement component.
        self.component_code = component_code
        # The item that is measured.
        self.domain_code = domain_code
        # The end timestamp of the metering cycle, in milliseconds.
        self.end_time = end_time
        # The start timestamp of the metering cycle, in milliseconds.
        self.start_time = start_time
        # The total quantity used within the measurement period.
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_code is not None:
            result['ComponentCode'] = self.component_code

        if self.domain_code is not None:
            result['DomainCode'] = self.domain_code

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.usage is not None:
            result['Usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentCode') is not None:
            self.component_code = m.get('ComponentCode')

        if m.get('DomainCode') is not None:
            self.domain_code = m.get('DomainCode')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        return self

