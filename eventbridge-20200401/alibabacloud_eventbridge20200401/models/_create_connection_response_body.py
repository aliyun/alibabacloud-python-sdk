# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class CreateConnectionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CreateConnectionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The returned response code. The value Success indicates that the request is successful.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message. If the request is successful, success is returned. If the request failed, an error code is returned.
        self.message = message
        # The request ID.
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
            temp_model = main_models.CreateConnectionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateConnectionResponseBodyData(DaraModel):
    def __init__(
        self,
        connection_name: str = None,
    ):
        # The connection name.
        self.connection_name = connection_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')

        return self

