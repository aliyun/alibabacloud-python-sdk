# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSlsLogstoreInfoResponseBody(DaraModel):
    def __init__(
        self,
        log_store: str = None,
        project: str = None,
        quota: int = None,
        request_id: str = None,
        ttl: int = None,
        used: int = None,
    ):
        # The Logstore of the Anti-DDoS Pro or Anti-DDoS Premium instance.
        self.log_store = log_store
        # The Logstore project of the Anti-DDoS Pro or Anti-DDoS Premium instance.
        self.project = project
        # The available log storage capacity. Unit: bytes.
        self.quota = quota
        # The ID of the request.
        self.request_id = request_id
        # The log storage duration. Unit: days.
        self.ttl = ttl
        # The used log storage capacity. Unit: bytes.
        # 
        # > The statistics on Log Service are delayed for about two hours.
        self.used = used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_store is not None:
            result['LogStore'] = self.log_store

        if self.project is not None:
            result['Project'] = self.project

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
        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('Quota') is not None:
            self.quota = m.get('Quota')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('Used') is not None:
            self.used = m.get('Used')

        return self

