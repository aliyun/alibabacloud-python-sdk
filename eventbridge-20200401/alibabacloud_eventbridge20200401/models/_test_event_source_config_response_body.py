# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class TestEventSourceConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.TestEventSourceConfigResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. Valid values:
        # 
        # *   Success: The request was successful.
        # *   Other codes indicate that the request failed. For information about error codes, see Error codes.
        self.code = code
        # The update result.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation was successful. If the operation was successful, the value true is returned.
        self.success = success

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

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.TestEventSourceConfigResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class TestEventSourceConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        check_item: str = None,
        error_msg: str = None,
        is_succeed: str = None,
    ):
        # The name of the check item.
        self.check_item = check_item
        # The error message.
        self.error_msg = error_msg
        # Indicates whether the check item is executed.
        self.is_succeed = is_succeed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_item is not None:
            result['CheckItem'] = self.check_item

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.is_succeed is not None:
            result['IsSucceed'] = self.is_succeed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckItem') is not None:
            self.check_item = m.get('CheckItem')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('IsSucceed') is not None:
            self.is_succeed = m.get('IsSucceed')

        return self

