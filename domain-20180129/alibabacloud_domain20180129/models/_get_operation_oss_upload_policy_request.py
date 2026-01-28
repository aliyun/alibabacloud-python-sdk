# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOperationOssUploadPolicyRequest(DaraModel):
    def __init__(
        self,
        audit_type: int = None,
        lang: str = None,
    ):
        # This parameter is required.
        self.audit_type = audit_type
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_type is not None:
            result['AuditType'] = self.audit_type

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditType') is not None:
            self.audit_type = m.get('AuditType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

