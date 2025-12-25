# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_push20160801 import models as main_models
from darabonba.model import DaraModel

class QueryDevicesByAliasResponseBody(DaraModel):
    def __init__(
        self,
        device_ids: main_models.QueryDevicesByAliasResponseBodyDeviceIds = None,
        request_id: str = None,
    ):
        self.device_ids = device_ids
        self.request_id = request_id

    def validate(self):
        if self.device_ids:
            self.device_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_ids is not None:
            result['DeviceIds'] = self.device_ids.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceIds') is not None:
            temp_model = main_models.QueryDevicesByAliasResponseBodyDeviceIds()
            self.device_ids = temp_model.from_map(m.get('DeviceIds'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryDevicesByAliasResponseBodyDeviceIds(DaraModel):
    def __init__(
        self,
        device_id: List[str] = None,
    ):
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        return self

