# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeResourceLogResponseBody(DaraModel):
    def __init__(
        self,
        log_store: str = None,
        message: str = None,
        project_name: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The Logstore of Log Service.
        self.log_store = log_store
        # The returned message.
        self.message = message
        # The Log Service project that is associated with the resource group.
        self.project_name = project_name
        # The request ID.
        self.request_id = request_id
        # The state of the resource group.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_store is not None:
            result['LogStore'] = self.log_store

        if self.message is not None:
            result['Message'] = self.message

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

