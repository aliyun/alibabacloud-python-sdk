# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSlsLogStoreResponseBody(DaraModel):
    def __init__(
        self,
        log_store_name: str = None,
        project_name: str = None,
        quota: int = None,
        request_id: str = None,
        ttl: int = None,
        used: int = None,
    ):
        # The name of the Logstore.
        self.log_store_name = log_store_name
        # The name of the Simple Log Service project.
        self.project_name = project_name
        # The capacity of the Logstore. Unit: bytes.
        self.quota = quota
        # The request ID.
        self.request_id = request_id
        # The storage duration of the Logstore. Unit: days.
        self.ttl = ttl
        # The used capacity of the Logstore. Unit: bytes.
        self.used = used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.quota is not None:
            result['Quota'] = self.quota

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.used is not None:
            result['Used'] = self.used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Quota') is not None:
            self.quota = m.get('Quota')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('Used') is not None:
            self.used = m.get('Used')

        return self

