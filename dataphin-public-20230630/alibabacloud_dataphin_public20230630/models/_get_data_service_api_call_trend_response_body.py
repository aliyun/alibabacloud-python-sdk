# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetDataServiceApiCallTrendResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetDataServiceApiCallTrendResponseBodyData = None,
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
            temp_model = main_models.GetDataServiceApiCallTrendResponseBodyData()
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

class GetDataServiceApiCallTrendResponseBodyData(DaraModel):
    def __init__(
        self,
        call_error_impact_trend_list: List[main_models.GetDataServiceApiCallTrendResponseBodyDataCallErrorImpactTrendList] = None,
        call_error_trend_list: List[main_models.GetDataServiceApiCallTrendResponseBodyDataCallErrorTrendList] = None,
    ):
        self.call_error_impact_trend_list = call_error_impact_trend_list
        self.call_error_trend_list = call_error_trend_list

    def validate(self):
        if self.call_error_impact_trend_list:
            for v1 in self.call_error_impact_trend_list:
                 if v1:
                    v1.validate()
        if self.call_error_trend_list:
            for v1 in self.call_error_trend_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CallErrorImpactTrendList'] = []
        if self.call_error_impact_trend_list is not None:
            for k1 in self.call_error_impact_trend_list:
                result['CallErrorImpactTrendList'].append(k1.to_map() if k1 else None)

        result['CallErrorTrendList'] = []
        if self.call_error_trend_list is not None:
            for k1 in self.call_error_trend_list:
                result['CallErrorTrendList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.call_error_impact_trend_list = []
        if m.get('CallErrorImpactTrendList') is not None:
            for k1 in m.get('CallErrorImpactTrendList'):
                temp_model = main_models.GetDataServiceApiCallTrendResponseBodyDataCallErrorImpactTrendList()
                self.call_error_impact_trend_list.append(temp_model.from_map(k1))

        self.call_error_trend_list = []
        if m.get('CallErrorTrendList') is not None:
            for k1 in m.get('CallErrorTrendList'):
                temp_model = main_models.GetDataServiceApiCallTrendResponseBodyDataCallErrorTrendList()
                self.call_error_trend_list.append(temp_model.from_map(k1))

        return self

class GetDataServiceApiCallTrendResponseBodyDataCallErrorTrendList(DaraModel):
    def __init__(
        self,
        call_count: int = None,
        error_count: int = None,
        minute: str = None,
    ):
        self.call_count = call_count
        self.error_count = error_count
        self.minute = minute

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_count is not None:
            result['CallCount'] = self.call_count

        if self.error_count is not None:
            result['ErrorCount'] = self.error_count

        if self.minute is not None:
            result['Minute'] = self.minute

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallCount') is not None:
            self.call_count = m.get('CallCount')

        if m.get('ErrorCount') is not None:
            self.error_count = m.get('ErrorCount')

        if m.get('Minute') is not None:
            self.minute = m.get('Minute')

        return self

class GetDataServiceApiCallTrendResponseBodyDataCallErrorImpactTrendList(DaraModel):
    def __init__(
        self,
        api_id_list: List[int] = None,
        error_api_count: int = None,
        error_app_count: int = None,
        minute: str = None,
    ):
        self.api_id_list = api_id_list
        self.error_api_count = error_api_count
        self.error_app_count = error_app_count
        self.minute = minute

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id_list is not None:
            result['ApiIdList'] = self.api_id_list

        if self.error_api_count is not None:
            result['ErrorApiCount'] = self.error_api_count

        if self.error_app_count is not None:
            result['ErrorAppCount'] = self.error_app_count

        if self.minute is not None:
            result['Minute'] = self.minute

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiIdList') is not None:
            self.api_id_list = m.get('ApiIdList')

        if m.get('ErrorApiCount') is not None:
            self.error_api_count = m.get('ErrorApiCount')

        if m.get('ErrorAppCount') is not None:
            self.error_app_count = m.get('ErrorAppCount')

        if m.get('Minute') is not None:
            self.minute = m.get('Minute')

        return self

