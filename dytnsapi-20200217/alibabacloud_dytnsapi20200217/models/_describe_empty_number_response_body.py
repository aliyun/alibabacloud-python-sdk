# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dytnsapi20200217 import models as main_models
from darabonba.model import DaraModel

class DescribeEmptyNumberResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeEmptyNumberResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # 返回状态码。取值：
        # 
        # - **OK**：成功。
        # 
        # - **InvalidPhoneNumber.Check**：手机号非法。
        self.code = code
        # 返回结果。
        self.data = data
        # 状态码的描述。
        self.message = message
        # 公共参数，每个请求返回的ID都是唯一的，可用于排查和定位问题。
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeEmptyNumberResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEmptyNumberResponseBodyData(DaraModel):
    def __init__(
        self,
        number: str = None,
        status: str = None,
    ):
        # 传入的手机号。
        self.number = number
        # 检测手机号返回状态。取值：
        # 
        # - **EMPTY**：空号。
        # 
        # - **NORMAL**：正常。
        # 
        # - **SUSPECT_EMPTY**：疑似空号。
        # 
        # - **UNKNOWN**：未知。
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.number is not None:
            result['Number'] = self.number

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

