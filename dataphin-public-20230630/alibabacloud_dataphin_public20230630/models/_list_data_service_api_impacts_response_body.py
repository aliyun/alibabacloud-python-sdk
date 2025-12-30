# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListDataServiceApiImpactsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListDataServiceApiImpactsResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_result = page_result
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageResult') is not None:
            temp_model = main_models.ListDataServiceApiImpactsResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDataServiceApiImpactsResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        impact_list: List[main_models.ListDataServiceApiImpactsResponseBodyPageResultImpactList] = None,
        total_count: int = None,
    ):
        self.impact_list = impact_list
        self.total_count = total_count

    def validate(self):
        if self.impact_list:
            for v1 in self.impact_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImpactList'] = []
        if self.impact_list is not None:
            for k1 in self.impact_list:
                result['ImpactList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.impact_list = []
        if m.get('ImpactList') is not None:
            for k1 in m.get('ImpactList'):
                temp_model = main_models.ListDataServiceApiImpactsResponseBodyPageResultImpactList()
                self.impact_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataServiceApiImpactsResponseBodyPageResultImpactList(DaraModel):
    def __init__(
        self,
        api_id: int = None,
        app_key: int = None,
        app_name: str = None,
        call_count: int = None,
        client_fail_count: int = None,
        client_ip: str = None,
        error_api_count: int = None,
        error_count: int = None,
        error_rate: str = None,
        last_call_time: str = None,
        minute: str = None,
        offline_count: int = None,
        success_time_cost: str = None,
        total_count: int = None,
        total_time_cost: str = None,
    ):
        # apiNo
        self.api_id = api_id
        # appKey
        self.app_key = app_key
        self.app_name = app_name
        self.call_count = call_count
        self.client_fail_count = client_fail_count
        self.client_ip = client_ip
        self.error_api_count = error_api_count
        self.error_count = error_count
        self.error_rate = error_rate
        self.last_call_time = last_call_time
        self.minute = minute
        self.offline_count = offline_count
        self.success_time_cost = success_time_cost
        self.total_count = total_count
        self.total_time_cost = total_time_cost

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.call_count is not None:
            result['CallCount'] = self.call_count

        if self.client_fail_count is not None:
            result['ClientFailCount'] = self.client_fail_count

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.error_api_count is not None:
            result['ErrorApiCount'] = self.error_api_count

        if self.error_count is not None:
            result['ErrorCount'] = self.error_count

        if self.error_rate is not None:
            result['ErrorRate'] = self.error_rate

        if self.last_call_time is not None:
            result['LastCallTime'] = self.last_call_time

        if self.minute is not None:
            result['Minute'] = self.minute

        if self.offline_count is not None:
            result['OfflineCount'] = self.offline_count

        if self.success_time_cost is not None:
            result['SuccessTimeCost'] = self.success_time_cost

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_time_cost is not None:
            result['TotalTimeCost'] = self.total_time_cost

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('CallCount') is not None:
            self.call_count = m.get('CallCount')

        if m.get('ClientFailCount') is not None:
            self.client_fail_count = m.get('ClientFailCount')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('ErrorApiCount') is not None:
            self.error_api_count = m.get('ErrorApiCount')

        if m.get('ErrorCount') is not None:
            self.error_count = m.get('ErrorCount')

        if m.get('ErrorRate') is not None:
            self.error_rate = m.get('ErrorRate')

        if m.get('LastCallTime') is not None:
            self.last_call_time = m.get('LastCallTime')

        if m.get('Minute') is not None:
            self.minute = m.get('Minute')

        if m.get('OfflineCount') is not None:
            self.offline_count = m.get('OfflineCount')

        if m.get('SuccessTimeCost') is not None:
            self.success_time_cost = m.get('SuccessTimeCost')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalTimeCost') is not None:
            self.total_time_cost = m.get('TotalTimeCost')

        return self

