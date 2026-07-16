# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAgenticDBBranchResponseBody(DaraModel):
    def __init__(
        self,
        branch_compute_cluster_id: str = None,
        branch_compute_node_count: int = None,
        branch_id: str = None,
        branch_name: str = None,
        create_time: str = None,
        description: str = None,
        is_default_branch: bool = None,
        last_activated_at: str = None,
        max_cu: str = None,
        min_cu: str = None,
        parent_branch_id: str = None,
        parent_branch_name: str = None,
        project_id: str = None,
        project_name: str = None,
        request_id: str = None,
        status: str = None,
        tenant_id: str = None,
    ):
        self.branch_compute_cluster_id = branch_compute_cluster_id
        self.branch_compute_node_count = branch_compute_node_count
        self.branch_id = branch_id
        self.branch_name = branch_name
        self.create_time = create_time
        self.description = description
        self.is_default_branch = is_default_branch
        self.last_activated_at = last_activated_at
        self.max_cu = max_cu
        self.min_cu = min_cu
        self.parent_branch_id = parent_branch_id
        self.parent_branch_name = parent_branch_name
        self.project_id = project_id
        self.project_name = project_name
        self.request_id = request_id
        self.status = status
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch_compute_cluster_id is not None:
            result['BranchComputeClusterId'] = self.branch_compute_cluster_id

        if self.branch_compute_node_count is not None:
            result['BranchComputeNodeCount'] = self.branch_compute_node_count

        if self.branch_id is not None:
            result['BranchId'] = self.branch_id

        if self.branch_name is not None:
            result['BranchName'] = self.branch_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.is_default_branch is not None:
            result['IsDefaultBranch'] = self.is_default_branch

        if self.last_activated_at is not None:
            result['LastActivatedAt'] = self.last_activated_at

        if self.max_cu is not None:
            result['MaxCU'] = self.max_cu

        if self.min_cu is not None:
            result['MinCU'] = self.min_cu

        if self.parent_branch_id is not None:
            result['ParentBranchId'] = self.parent_branch_id

        if self.parent_branch_name is not None:
            result['ParentBranchName'] = self.parent_branch_name

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
        if m.get('BranchComputeClusterId') is not None:
            self.branch_compute_cluster_id = m.get('BranchComputeClusterId')

        if m.get('BranchComputeNodeCount') is not None:
            self.branch_compute_node_count = m.get('BranchComputeNodeCount')

        if m.get('BranchId') is not None:
            self.branch_id = m.get('BranchId')

        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IsDefaultBranch') is not None:
            self.is_default_branch = m.get('IsDefaultBranch')

        if m.get('LastActivatedAt') is not None:
            self.last_activated_at = m.get('LastActivatedAt')

        if m.get('MaxCU') is not None:
            self.max_cu = m.get('MaxCU')

        if m.get('MinCU') is not None:
            self.min_cu = m.get('MinCU')

        if m.get('ParentBranchId') is not None:
            self.parent_branch_id = m.get('ParentBranchId')

        if m.get('ParentBranchName') is not None:
            self.parent_branch_name = m.get('ParentBranchName')

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

