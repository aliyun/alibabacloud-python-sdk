# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dm20151123 import models as main_models
from darabonba.model import DaraModel

class GetUserResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetUserResponseBodyData = None,
        request_id: str = None,
    ):
        # Returned Content
        self.data = data
        # Request ID
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetUserResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetUserResponseBodyData(DaraModel):
    def __init__(
        self,
        enable_eventbridge: bool = None,
    ):
        # Whether EventBridge is enabled
        self.enable_eventbridge = enable_eventbridge

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_eventbridge is not None:
            result['EnableEventbridge'] = self.enable_eventbridge

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableEventbridge') is not None:
            self.enable_eventbridge = m.get('EnableEventbridge')

        return self

