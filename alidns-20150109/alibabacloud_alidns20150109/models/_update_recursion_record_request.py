# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRecursionRecordRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        priority: int = None,
        record_id: str = None,
        request_source: str = None,
        rr: str = None,
        ttl: int = None,
        type: str = None,
        value: str = None,
        weight: int = None,
    ):
        self.client_token = client_token
        self.priority = priority
        self.record_id = record_id
        self.request_source = request_source
        self.rr = rr
        self.ttl = ttl
        self.type = type
        self.value = value
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.request_source is not None:
            result['RequestSource'] = self.request_source

        if self.rr is not None:
            result['Rr'] = self.rr

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('RequestSource') is not None:
            self.request_source = m.get('RequestSource')

        if m.get('Rr') is not None:
            self.rr = m.get('Rr')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

