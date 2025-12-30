# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetDataServiceApiCallSummaryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetDataServiceApiCallSummaryResponseBodyData = None,
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
            temp_model = main_models.GetDataServiceApiCallSummaryResponseBodyData()
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

class GetDataServiceApiCallSummaryResponseBodyData(DaraModel):
    def __init__(
        self,
        call_count: int = None,
        error_api_count: int = None,
        error_app_count: int = None,
        error_count: int = None,
        error_rate: float = None,
        offline_rate: float = None,
    ):
        self.call_count = call_count
        self.error_api_count = error_api_count
        self.error_app_count = error_app_count
        self.error_count = error_count
        self.error_rate = error_rate
        self.offline_rate = offline_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_count is not None:
            result['CallCount'] = self.call_count

        if self.error_api_count is not None:
            result['ErrorApiCount'] = self.error_api_count

        if self.error_app_count is not None:
            result['ErrorAppCount'] = self.error_app_count

        if self.error_count is not None:
            result['ErrorCount'] = self.error_count

        if self.error_rate is not None:
            result['ErrorRate'] = self.error_rate

        if self.offline_rate is not None:
            result['OfflineRate'] = self.offline_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallCount') is not None:
            self.call_count = m.get('CallCount')

        if m.get('ErrorApiCount') is not None:
            self.error_api_count = m.get('ErrorApiCount')

        if m.get('ErrorAppCount') is not None:
            self.error_app_count = m.get('ErrorAppCount')

        if m.get('ErrorCount') is not None:
            self.error_count = m.get('ErrorCount')

        if m.get('ErrorRate') is not None:
            self.error_rate = m.get('ErrorRate')

        if m.get('OfflineRate') is not None:
            self.offline_rate = m.get('OfflineRate')

        return self

