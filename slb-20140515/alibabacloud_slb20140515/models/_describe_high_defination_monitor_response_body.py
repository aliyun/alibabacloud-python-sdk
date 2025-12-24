# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHighDefinationMonitorResponseBody(DaraModel):
    def __init__(
        self,
        log_project: str = None,
        log_store: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The name of the Log Service project.
        self.log_project = log_project
        # The name of the Logstore.
        self.log_store = log_store
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_project is not None:
            result['LogProject'] = self.log_project

        if self.log_store is not None:
            result['LogStore'] = self.log_store

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogProject') is not None:
            self.log_project = m.get('LogProject')

        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

