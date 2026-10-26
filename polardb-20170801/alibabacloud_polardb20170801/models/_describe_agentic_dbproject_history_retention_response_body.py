# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAgenticDBProjectHistoryRetentionResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        history_retention_seconds: int = None,
        project_id: str = None,
        queried_at: str = None,
        request_id: str = None,
        tenant_id: str = None,
    ):
        # DBClusterId
        self.dbcluster_id = dbcluster_id
        # The effective history data retention period for the project. For the actual recoverable range, query the branch recovery window.
        self.history_retention_seconds = history_retention_seconds
        # ProjectId
        self.project_id = project_id
        # The time when the query was completed, in UTC RFC3339 format. This does not represent the latest recoverable time.
        self.queried_at = queried_at
        # The request ID.
        self.request_id = request_id
        # TenantId
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.history_retention_seconds is not None:
            result['HistoryRetentionSeconds'] = self.history_retention_seconds

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.queried_at is not None:
            result['QueriedAt'] = self.queried_at

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('HistoryRetentionSeconds') is not None:
            self.history_retention_seconds = m.get('HistoryRetentionSeconds')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('QueriedAt') is not None:
            self.queried_at = m.get('QueriedAt')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

