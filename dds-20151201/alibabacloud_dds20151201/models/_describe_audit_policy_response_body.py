# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAuditPolicyResponseBody(DaraModel):
    def __init__(
        self,
        log_audit_status: str = None,
        request_id: str = None,
    ):
        # Indicates whether the log audit feature is enabled. Valid values:
        # 
        # *   Enable
        # *   Disabled
        # 
        # Default value: Disabled.
        self.log_audit_status = log_audit_status
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_audit_status is not None:
            result['LogAuditStatus'] = self.log_audit_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogAuditStatus') is not None:
            self.log_audit_status = m.get('LogAuditStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

