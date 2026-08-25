# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class GetLogSyncToSLSResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetLogSyncToSLSResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
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
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetLogSyncToSLSResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetLogSyncToSLSResponseBodyData(DaraModel):
    def __init__(
        self,
        status: str = None,
        target_log_store: str = None,
        target_project: str = None,
    ):
        # The log synchronization status. Valid values:
        # - on: Synchronization is enabled.
        # - off: Synchronization is disabled.
        self.status = status
        # The Simple Log Service Logstore.
        self.target_log_store = target_log_store
        # The Simple Log Service project.
        self.target_project = target_project

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.target_log_store is not None:
            result['TargetLogStore'] = self.target_log_store

        if self.target_project is not None:
            result['TargetProject'] = self.target_project

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetLogStore') is not None:
            self.target_log_store = m.get('TargetLogStore')

        if m.get('TargetProject') is not None:
            self.target_project = m.get('TargetProject')

        return self

