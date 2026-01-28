# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitOperationCredentialsRequest(DaraModel):
    def __init__(
        self,
        audit_record_id: int = None,
        audit_type: int = None,
        credentials: str = None,
        lang: str = None,
        reg_type: int = None,
    ):
        self.audit_record_id = audit_record_id
        self.audit_type = audit_type
        self.credentials = credentials
        self.lang = lang
        self.reg_type = reg_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_record_id is not None:
            result['AuditRecordId'] = self.audit_record_id

        if self.audit_type is not None:
            result['AuditType'] = self.audit_type

        if self.credentials is not None:
            result['Credentials'] = self.credentials

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.reg_type is not None:
            result['RegType'] = self.reg_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditRecordId') is not None:
            self.audit_record_id = m.get('AuditRecordId')

        if m.get('AuditType') is not None:
            self.audit_type = m.get('AuditType')

        if m.get('Credentials') is not None:
            self.credentials = m.get('Credentials')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RegType') is not None:
            self.reg_type = m.get('RegType')

        return self

