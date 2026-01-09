# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class InsertAiOutboundPhoneNumsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.InsertAiOutboundPhoneNumsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
            temp_model = main_models.InsertAiOutboundPhoneNumsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class InsertAiOutboundPhoneNumsResponseBodyData(DaraModel):
    def __init__(
        self,
        fail_info: List[main_models.InsertAiOutboundPhoneNumsResponseBodyDataFailInfo] = None,
        success_count: int = None,
        total_count: int = None,
    ):
        self.fail_info = fail_info
        self.success_count = success_count
        self.total_count = total_count

    def validate(self):
        if self.fail_info:
            for v1 in self.fail_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FailInfo'] = []
        if self.fail_info is not None:
            for k1 in self.fail_info:
                result['FailInfo'].append(k1.to_map() if k1 else None)

        if self.success_count is not None:
            result['SuccessCount'] = self.success_count

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fail_info = []
        if m.get('FailInfo') is not None:
            for k1 in m.get('FailInfo'):
                temp_model = main_models.InsertAiOutboundPhoneNumsResponseBodyDataFailInfo()
                self.fail_info.append(temp_model.from_map(k1))

        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class InsertAiOutboundPhoneNumsResponseBodyDataFailInfo(DaraModel):
    def __init__(
        self,
        biz_data: str = None,
        msg: str = None,
        phone_num: str = None,
    ):
        self.biz_data = biz_data
        self.msg = msg
        self.phone_num = phone_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_data is not None:
            result['BizData'] = self.biz_data

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizData') is not None:
            self.biz_data = m.get('BizData')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')

        return self

