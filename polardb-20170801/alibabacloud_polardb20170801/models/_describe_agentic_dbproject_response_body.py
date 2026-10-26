# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAgenticDBProjectResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        default_branch_id: str = None,
        default_branch_name: str = None,
        description: str = None,
        history_retention_seconds: int = None,
        project_id: str = None,
        project_name: str = None,
        request_id: str = None,
        status: str = None,
        tenant_id: str = None,
    ):
        # The creation time.
        # 
        # The time is displayed in ISO 8601 format in the UTC time zone (YYYY-MM-DDTHH:mm:ssZ).
        self.create_time = create_time
        # The default branch ID.
        self.default_branch_id = default_branch_id
        # The default branch name.
        self.default_branch_name = default_branch_name
        # The description.
        self.description = description
        # The retention period for recent records of the project. This parameter may be empty for older projects. To query the current effective value, call DescribeAgenticDBProjectHistoryRetention.
        self.history_retention_seconds = history_retention_seconds
        # Project ID
        self.project_id = project_id
        # The project name.
        self.project_name = project_name
        # The request ID.
        self.request_id = request_id
        # The project status. Valid values: Active (Normal), Destroying (Destroying), and Destroyed (Destroyed).
        self.status = status
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.default_branch_id is not None:
            result['DefaultBranchId'] = self.default_branch_id

        if self.default_branch_name is not None:
            result['DefaultBranchName'] = self.default_branch_name

        if self.description is not None:
            result['Description'] = self.description

        if self.history_retention_seconds is not None:
            result['HistoryRetentionSeconds'] = self.history_retention_seconds

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DefaultBranchId') is not None:
            self.default_branch_id = m.get('DefaultBranchId')

        if m.get('DefaultBranchName') is not None:
            self.default_branch_name = m.get('DefaultBranchName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HistoryRetentionSeconds') is not None:
            self.history_retention_seconds = m.get('HistoryRetentionSeconds')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

