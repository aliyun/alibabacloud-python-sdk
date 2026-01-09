# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class GetHotlineMessageLogResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetHotlineMessageLogResponseBodyData] = None,
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
                temp_model = main_models.GetHotlineMessageLogResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetHotlineMessageLogResponseBodyData(DaraModel):
    def __init__(
        self,
        acid: str = None,
        content: str = None,
        end_time: int = None,
        mid: str = None,
        sender_type: int = None,
        start_time: int = None,
    ):
        self.acid = acid
        self.content = content
        self.end_time = end_time
        self.mid = mid
        self.sender_type = sender_type
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acid is not None:
            result['Acid'] = self.acid

        if self.content is not None:
            result['Content'] = self.content

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.mid is not None:
            result['Mid'] = self.mid

        if self.sender_type is not None:
            result['SenderType'] = self.sender_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Mid') is not None:
            self.mid = m.get('Mid')

        if m.get('SenderType') is not None:
            self.sender_type = m.get('SenderType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

