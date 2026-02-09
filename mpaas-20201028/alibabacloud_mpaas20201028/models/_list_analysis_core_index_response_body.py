# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class ListAnalysisCoreIndexResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_content: main_models.ListAnalysisCoreIndexResponseBodyResultContent = None,
        result_message: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.result_content = result_content
        self.result_message = result_message
        self.success = success

    def validate(self):
        if self.result_content:
            self.result_content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_content is not None:
            result['ResultContent'] = self.result_content.to_map()

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultContent') is not None:
            temp_model = main_models.ListAnalysisCoreIndexResponseBodyResultContent()
            self.result_content = temp_model.from_map(m.get('ResultContent'))

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAnalysisCoreIndexResponseBodyResultContent(DaraModel):
    def __init__(
        self,
        data: main_models.ListAnalysisCoreIndexResponseBodyResultContentData = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListAnalysisCoreIndexResponseBodyResultContentData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAnalysisCoreIndexResponseBodyResultContentData(DaraModel):
    def __init__(
        self,
        arrival_num: str = None,
        arrival_rate: str = None,
        ignore_num: str = None,
        ignore_rate: str = None,
        open_num: str = None,
        open_rate: str = None,
        push_num: str = None,
        push_total_num: str = None,
    ):
        # 0
        self.arrival_num = arrival_num
        # 0
        self.arrival_rate = arrival_rate
        # 0
        self.ignore_num = ignore_num
        # 0
        self.ignore_rate = ignore_rate
        # 0
        self.open_num = open_num
        # 0
        self.open_rate = open_rate
        # 0
        self.push_num = push_num
        # 0
        self.push_total_num = push_total_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arrival_num is not None:
            result['ArrivalNum'] = self.arrival_num

        if self.arrival_rate is not None:
            result['ArrivalRate'] = self.arrival_rate

        if self.ignore_num is not None:
            result['IgnoreNum'] = self.ignore_num

        if self.ignore_rate is not None:
            result['IgnoreRate'] = self.ignore_rate

        if self.open_num is not None:
            result['OpenNum'] = self.open_num

        if self.open_rate is not None:
            result['OpenRate'] = self.open_rate

        if self.push_num is not None:
            result['PushNum'] = self.push_num

        if self.push_total_num is not None:
            result['PushTotalNum'] = self.push_total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArrivalNum') is not None:
            self.arrival_num = m.get('ArrivalNum')

        if m.get('ArrivalRate') is not None:
            self.arrival_rate = m.get('ArrivalRate')

        if m.get('IgnoreNum') is not None:
            self.ignore_num = m.get('IgnoreNum')

        if m.get('IgnoreRate') is not None:
            self.ignore_rate = m.get('IgnoreRate')

        if m.get('OpenNum') is not None:
            self.open_num = m.get('OpenNum')

        if m.get('OpenRate') is not None:
            self.open_rate = m.get('OpenRate')

        if m.get('PushNum') is not None:
            self.push_num = m.get('PushNum')

        if m.get('PushTotalNum') is not None:
            self.push_total_num = m.get('PushTotalNum')

        return self

