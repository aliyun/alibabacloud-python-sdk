# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAuditLogConfigResponseBody(DaraModel):
    def __init__(
        self,
        db_audit: str = None,
        request_id: str = None,
        retention: str = None,
    ):
        # Indicates whether the audit log feature is enabled. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        # 
        # > You can call the [ModifyAuditLogConfig](https://help.aliyun.com/document_detail/473829.html) operation to enable or disable the audit log feature for a Tair (Redis OSS-compatible) instance.
        self.db_audit = db_audit
        # The ID of the request.
        self.request_id = request_id
        # The retention period of audit logs. Unit: days.
        self.retention = retention

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_audit is not None:
            result['DbAudit'] = self.db_audit

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.retention is not None:
            result['Retention'] = self.retention

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbAudit') is not None:
            self.db_audit = m.get('DbAudit')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Retention') is not None:
            self.retention = m.get('Retention')

        return self

