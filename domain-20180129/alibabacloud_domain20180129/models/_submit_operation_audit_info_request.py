# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitOperationAuditInfoRequest(DaraModel):
    def __init__(
        self,
        audit_info: str = None,
        audit_type: int = None,
        domain_name: str = None,
        id: int = None,
        lang: str = None,
    ):
        self.audit_info = audit_info
        # This parameter is required.
        self.audit_type = audit_type
        # This parameter is required.
        self.domain_name = domain_name
        self.id = id
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_info is not None:
            result['AuditInfo'] = self.audit_info

        if self.audit_type is not None:
            result['AuditType'] = self.audit_type

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.id is not None:
            result['Id'] = self.id

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditInfo') is not None:
            self.audit_info = m.get('AuditInfo')

        if m.get('AuditType') is not None:
            self.audit_type = m.get('AuditType')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

