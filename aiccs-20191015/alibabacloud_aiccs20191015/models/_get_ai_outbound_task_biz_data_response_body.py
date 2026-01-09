# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class GetAiOutboundTaskBizDataResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAiOutboundTaskBizDataResponseBodyData = None,
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
            temp_model = main_models.GetAiOutboundTaskBizDataResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAiOutboundTaskBizDataResponseBodyData(DaraModel):
    def __init__(
        self,
        biz_data: str = None,
        case_id: int = None,
        phone_num: str = None,
        task_id: int = None,
    ):
        self.biz_data = biz_data
        self.case_id = case_id
        self.phone_num = phone_num
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_data is not None:
            result['BizData'] = self.biz_data

        if self.case_id is not None:
            result['CaseId'] = self.case_id

        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizData') is not None:
            self.biz_data = m.get('BizData')

        if m.get('CaseId') is not None:
            self.case_id = m.get('CaseId')

        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

