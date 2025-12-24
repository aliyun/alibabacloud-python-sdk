# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class MiguLivePullToPushStatusResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.MiguLivePullToPushStatusResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        timestamp: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.timestamp = timestamp

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.MiguLivePullToPushStatusResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        return self

class MiguLivePullToPushStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        message: str = None,
        status: str = None,
    ):
        self.message = message
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['message'] = self.message

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

