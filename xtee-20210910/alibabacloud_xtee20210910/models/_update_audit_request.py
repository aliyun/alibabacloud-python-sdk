# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAuditRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        audit_msg: str = None,
        audit_relation_type: str = None,
        audit_status: str = None,
        id: int = None,
        reg_id: str = None,
    ):
        # Sets the language type for requests and received messages, default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Approval comments
        self.audit_msg = audit_msg
        # Associated type
        self.audit_relation_type = audit_relation_type
        # Status
        self.audit_status = audit_status
        # The ID of the approval to be updated.
        self.id = id
        # Region code
        self.reg_id = reg_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.audit_msg is not None:
            result['auditMsg'] = self.audit_msg

        if self.audit_relation_type is not None:
            result['auditRelationType'] = self.audit_relation_type

        if self.audit_status is not None:
            result['auditStatus'] = self.audit_status

        if self.id is not None:
            result['id'] = self.id

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('auditMsg') is not None:
            self.audit_msg = m.get('auditMsg')

        if m.get('auditRelationType') is not None:
            self.audit_relation_type = m.get('auditRelationType')

        if m.get('auditStatus') is not None:
            self.audit_status = m.get('auditStatus')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        return self

