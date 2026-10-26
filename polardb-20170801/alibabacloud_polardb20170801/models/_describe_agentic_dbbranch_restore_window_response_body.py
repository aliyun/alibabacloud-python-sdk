# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAgenticDBBranchRestoreWindowResponseBody(DaraModel):
    def __init__(
        self,
        branch_id: str = None,
        dbcluster_id: str = None,
        earliest_restorable_time: str = None,
        project_id: str = None,
        queried_at: str = None,
        request_id: str = None,
        tenant_id: str = None,
    ):
        # The ID of the source branch.
        self.branch_id = branch_id
        # DBClusterId
        self.dbcluster_id = dbcluster_id
        # The earliest time available for creating a historical branch, in UTC RFC3339 format. This time point can be selected. The available range changes over time and is revalidated during creation.
        self.earliest_restorable_time = earliest_restorable_time
        # ProjectId
        self.project_id = project_id
        # The time when the query was completed, in UTC RFC3339 format. This does not represent the latest restorable time.
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
        if self.branch_id is not None:
            result['BranchId'] = self.branch_id

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.earliest_restorable_time is not None:
            result['EarliestRestorableTime'] = self.earliest_restorable_time

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
        if m.get('BranchId') is not None:
            self.branch_id = m.get('BranchId')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('EarliestRestorableTime') is not None:
            self.earliest_restorable_time = m.get('EarliestRestorableTime')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('QueriedAt') is not None:
            self.queried_at = m.get('QueriedAt')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

