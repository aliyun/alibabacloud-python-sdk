# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_notifications20241225 import models as main_models
from darabonba.model import DaraModel

class ReadNumGroupByClassResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ReadNumGroupByClassResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned when the call fails. For more information, see error codes.
        self.code = code
        # The execution result.
        self.data = data
        # The message returned when the call fails.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # - true: The call was successful.
        # - false: The call failed.
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
                temp_model = main_models.ReadNumGroupByClassResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ReadNumGroupByClassResponseBodyData(DaraModel):
    def __init__(
        self,
        class_id: int = None,
        msg_count: int = None,
    ):
        # The message category ID.
        self.class_id = class_id
        # The number of unread messages in the category.
        self.msg_count = msg_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_id is not None:
            result['ClassId'] = self.class_id

        if self.msg_count is not None:
            result['MsgCount'] = self.msg_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')

        if m.get('MsgCount') is not None:
            self.msg_count = m.get('MsgCount')

        return self

