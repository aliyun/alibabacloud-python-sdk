# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryOperationAuditInfoDetailRequest(DaraModel):
    def __init__(
        self,
        audit_record_id: int = None,
        lang: str = None,
    ):
        # This parameter is required.
        self.audit_record_id = audit_record_id
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_record_id is not None:
            result['AuditRecordId'] = self.audit_record_id

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditRecordId') is not None:
            self.audit_record_id = m.get('AuditRecordId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

