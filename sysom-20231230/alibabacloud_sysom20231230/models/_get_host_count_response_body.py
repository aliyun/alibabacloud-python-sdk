# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class GetHostCountResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetHostCountResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        total: int = None,
    ):
        # The status code.
        # - `code == Success` indicates that the authorization is successful.
        # - Other status codes indicate that the authorization failed. Check the `message` field for the detailed fault information.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        # - If `code == Success`, this field is empty.
        # - Otherwise, this field contains the request error information.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total = total

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
            result['code'] = self.code

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['request_id'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.GetHostCountResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class GetHostCountResponseBodyData(DaraModel):
    def __init__(
        self,
        time: int = None,
        value: int = None,
    ):
        # The point in time.
        self.time = time
        # The count.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.time is not None:
            result['time'] = self.time

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

