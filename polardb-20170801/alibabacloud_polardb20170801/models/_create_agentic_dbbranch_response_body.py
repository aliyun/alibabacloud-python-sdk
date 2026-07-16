# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAgenticDBBranchResponseBody(DaraModel):
    def __init__(
        self,
        branch_compute_cluster_id: str = None,
        branch_id: str = None,
        branch_name: str = None,
        dbcluster_id: str = None,
        parent_branch_id: str = None,
        parent_branch_name: str = None,
        project_id: str = None,
        project_name: str = None,
        request_id: str = None,
        status: str = None,
    ):
        # The ID of the compute cluster associated with the branch.
        self.branch_compute_cluster_id = branch_compute_cluster_id
        # The branch ID.
        self.branch_id = branch_id
        # The name of the branch.
        self.branch_name = branch_name
        # The AgenticDB cluster ID.
        self.dbcluster_id = dbcluster_id
        # The ID of the parent branch.
        self.parent_branch_id = parent_branch_id
        # The name of the parent branch.
        self.parent_branch_name = parent_branch_name
        # The ID of the project to which the branch belongs.
        self.project_id = project_id
        # The name of the project to which the branch belongs.
        self.project_name = project_name
        # The request ID.
        self.request_id = request_id
        # The status of the branch.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch_compute_cluster_id is not None:
            result['BranchComputeClusterId'] = self.branch_compute_cluster_id

        if self.branch_id is not None:
            result['BranchId'] = self.branch_id

        if self.branch_name is not None:
            result['BranchName'] = self.branch_name

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchComputeClusterId') is not None:
            self.branch_compute_cluster_id = m.get('BranchComputeClusterId')

        if m.get('BranchId') is not None:
            self.branch_id = m.get('BranchId')

        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

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

        return self

