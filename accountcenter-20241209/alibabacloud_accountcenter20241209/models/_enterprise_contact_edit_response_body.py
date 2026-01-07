# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_accountcenter20241209 import models as main_models
from darabonba.model import DaraModel

class EnterpriseContactEditResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.EnterpriseContactEditResponseBodyData = None,
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
            temp_model = main_models.EnterpriseContactEditResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class EnterpriseContactEditResponseBodyData(DaraModel):
    def __init__(
        self,
        contact_id: int = None,
        error_list: List[main_models.EnterpriseContactEditResponseBodyDataErrorList] = None,
        result: bool = None,
    ):
        self.contact_id = contact_id
        self.error_list = error_list
        self.result = result

    def validate(self):
        if self.error_list:
            for v1 in self.error_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        result['ErrorList'] = []
        if self.error_list is not None:
            for k1 in self.error_list:
                result['ErrorList'].append(k1.to_map() if k1 else None)

        if self.result is not None:
            result['Result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        self.error_list = []
        if m.get('ErrorList') is not None:
            for k1 in m.get('ErrorList'):
                temp_model = main_models.EnterpriseContactEditResponseBodyDataErrorList()
                self.error_list.append(temp_model.from_map(k1))

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

class EnterpriseContactEditResponseBodyDataErrorList(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_desc: str = None,
        item: str = None,
    ):
        self.error_code = error_code
        self.error_desc = error_desc
        self.item = item

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_desc is not None:
            result['ErrorDesc'] = self.error_desc

        if self.item is not None:
            result['Item'] = self.item

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorDesc') is not None:
            self.error_desc = m.get('ErrorDesc')

        if m.get('Item') is not None:
            self.item = m.get('Item')

        return self

