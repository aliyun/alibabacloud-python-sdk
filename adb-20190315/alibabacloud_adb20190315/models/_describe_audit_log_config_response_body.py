# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAuditLogConfigResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        audit_log_status: str = None,
        dbcluster_id: str = None,
        request_id: str = None,
    ):
        # The details about the access denial. This parameter is returned only if Resource Access Management (RAM) permission verification failed.
        self.access_denied_detail = access_denied_detail
        # The status of SQL audit. Valid values:
        # 
        # *   **on**: SQL audit is enabled.
        # *   **off**: SQL audit is disabled.
        self.audit_log_status = audit_log_status
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.audit_log_status is not None:
            result['AuditLogStatus'] = self.audit_log_status

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('AuditLogStatus') is not None:
            self.audit_log_status = m.get('AuditLogStatus')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

