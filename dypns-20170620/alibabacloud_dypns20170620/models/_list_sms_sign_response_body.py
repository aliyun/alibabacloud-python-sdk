# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dypns20170620 import models as main_models
from darabonba.model import DaraModel

class ListSmsSignResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListSmsSignResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListSmsSignResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListSmsSignResponseBodyData(DaraModel):
    def __init__(
        self,
        audit_result: str = None,
        create_date: int = None,
        default_flag: bool = None,
        sms_sign_name: str = None,
        status: str = None,
        test_flag: bool = None,
    ):
        self.audit_result = audit_result
        self.create_date = create_date
        self.default_flag = default_flag
        self.sms_sign_name = sms_sign_name
        self.status = status
        self.test_flag = test_flag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_result is not None:
            result['AuditResult'] = self.audit_result

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.default_flag is not None:
            result['DefaultFlag'] = self.default_flag

        if self.sms_sign_name is not None:
            result['SmsSignName'] = self.sms_sign_name

        if self.status is not None:
            result['Status'] = self.status

        if self.test_flag is not None:
            result['TestFlag'] = self.test_flag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditResult') is not None:
            self.audit_result = m.get('AuditResult')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('DefaultFlag') is not None:
            self.default_flag = m.get('DefaultFlag')

        if m.get('SmsSignName') is not None:
            self.sms_sign_name = m.get('SmsSignName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TestFlag') is not None:
            self.test_flag = m.get('TestFlag')

        return self

