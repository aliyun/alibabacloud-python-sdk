# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeCallbacksResponseBody(DaraModel):
    def __init__(
        self,
        callbacks: List[main_models.DescribeCallbacksResponseBodyCallbacks] = None,
        request_id: str = None,
    ):
        self.callbacks = callbacks
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.callbacks:
            for v1 in self.callbacks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Callbacks'] = []
        if self.callbacks is not None:
            for k1 in self.callbacks:
                result['Callbacks'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.callbacks = []
        if m.get('Callbacks') is not None:
            for k1 in m.get('Callbacks'):
                temp_model = main_models.DescribeCallbacksResponseBodyCallbacks()
                self.callbacks.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCallbacksResponseBodyCallbacks(DaraModel):
    def __init__(
        self,
        category: str = None,
        check_status: str = None,
        code: str = None,
        conf: str = None,
        msg: str = None,
        status: int = None,
        sub_event: List[int] = None,
    ):
        self.category = category
        self.check_status = check_status
        self.code = code
        self.conf = conf
        self.msg = msg
        self.status = status
        self.sub_event = sub_event

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.check_status is not None:
            result['CheckStatus'] = self.check_status

        if self.code is not None:
            result['Code'] = self.code

        if self.conf is not None:
            result['Conf'] = self.conf

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_event is not None:
            result['SubEvent'] = self.sub_event

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Conf') is not None:
            self.conf = m.get('Conf')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubEvent') is not None:
            self.sub_event = m.get('SubEvent')

        return self

