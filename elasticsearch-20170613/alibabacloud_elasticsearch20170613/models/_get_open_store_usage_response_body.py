# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class GetOpenStoreUsageResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.GetOpenStoreUsageResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The current request result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetOpenStoreUsageResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class GetOpenStoreUsageResponseBodyResult(DaraModel):
    def __init__(
        self,
        current_usage: int = None,
        last_day_usage: int = None,
    ):
        # The current OpenStore storage capacity (estimated value based on actual indexes). Unit: Byte.
        self.current_usage = current_usage
        # The storage capacity of OpenStore yesterday. Unit: bytes.
        self.last_day_usage = last_day_usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_usage is not None:
            result['currentUsage'] = self.current_usage

        if self.last_day_usage is not None:
            result['lastDayUsage'] = self.last_day_usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentUsage') is not None:
            self.current_usage = m.get('currentUsage')

        if m.get('lastDayUsage') is not None:
            self.last_day_usage = m.get('lastDayUsage')

        return self

