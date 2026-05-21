# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hologram20220601 import models as main_models
from darabonba.model import DaraModel

class GetLastUpgradeRecordResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetLastUpgradeRecordResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
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
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetLastUpgradeRecordResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetLastUpgradeRecordResponseBodyData(DaraModel):
    def __init__(
        self,
        from_version: str = None,
        start_readonly_time: str = None,
        stop_readonly_time: str = None,
        to_version: str = None,
    ):
        self.from_version = from_version
        self.start_readonly_time = start_readonly_time
        self.stop_readonly_time = stop_readonly_time
        self.to_version = to_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_version is not None:
            result['fromVersion'] = self.from_version

        if self.start_readonly_time is not None:
            result['startReadonlyTime'] = self.start_readonly_time

        if self.stop_readonly_time is not None:
            result['stopReadonlyTime'] = self.stop_readonly_time

        if self.to_version is not None:
            result['toVersion'] = self.to_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fromVersion') is not None:
            self.from_version = m.get('fromVersion')

        if m.get('startReadonlyTime') is not None:
            self.start_readonly_time = m.get('startReadonlyTime')

        if m.get('stopReadonlyTime') is not None:
            self.stop_readonly_time = m.get('stopReadonlyTime')

        if m.get('toVersion') is not None:
            self.to_version = m.get('toVersion')

        return self

