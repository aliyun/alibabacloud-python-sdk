# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class FetchLosslessRuleListResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.FetchLosslessRuleListResponseBodyData = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code returned.
        self.code = code
        # The returned result.
        self.data = data
        self.error_code = error_code
        self.http_status_code = http_status_code
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

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
            temp_model = main_models.FetchLosslessRuleListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class FetchLosslessRuleListResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        results: List[main_models.FetchLosslessRuleListResponseBodyDataResults] = None,
        total_size: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The returned data.
        self.results = results
        # The total number of entries returned.
        self.total_size = total_size

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.FetchLosslessRuleListResponseBodyDataResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class FetchLosslessRuleListResponseBodyDataResults(DaraModel):
    def __init__(
        self,
        aligned: bool = None,
        app_id: str = None,
        app_name: str = None,
        count: int = None,
        delay_time: int = None,
        enable: bool = None,
        func_type: int = None,
        loss_less_detail: bool = None,
        notice: bool = None,
        related: bool = None,
        warmup_time: int = None,
    ):
        # Indicates whether service registration is complete before readiness probe.
        self.aligned = aligned
        # The ID of the application.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name
        # The number of instances.
        self.count = count
        # The registration latency. Unit: seconds.
        self.delay_time = delay_time
        # Indicates whether graceful start is enabled. Valid values:
        # 
        # *   `true`: enabled
        # *   `false`: disabled
        self.enable = enable
        # The slope of the prefetching curve.
        self.func_type = func_type
        # Indicates whether online and offline processing details are displayed.
        self.loss_less_detail = loss_less_detail
        # Indicates whether notification is enabled.
        self.notice = notice
        # Indicates whether service prefetching is complete before readiness probe.
        self.related = related
        # The prefetching duration. Unit: seconds.
        self.warmup_time = warmup_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aligned is not None:
            result['Aligned'] = self.aligned

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.count is not None:
            result['Count'] = self.count

        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.func_type is not None:
            result['FuncType'] = self.func_type

        if self.loss_less_detail is not None:
            result['LossLessDetail'] = self.loss_less_detail

        if self.notice is not None:
            result['Notice'] = self.notice

        if self.related is not None:
            result['Related'] = self.related

        if self.warmup_time is not None:
            result['WarmupTime'] = self.warmup_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Aligned') is not None:
            self.aligned = m.get('Aligned')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('FuncType') is not None:
            self.func_type = m.get('FuncType')

        if m.get('LossLessDetail') is not None:
            self.loss_less_detail = m.get('LossLessDetail')

        if m.get('Notice') is not None:
            self.notice = m.get('Notice')

        if m.get('Related') is not None:
            self.related = m.get('Related')

        if m.get('WarmupTime') is not None:
            self.warmup_time = m.get('WarmupTime')

        return self

