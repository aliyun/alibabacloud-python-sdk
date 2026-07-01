# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAgenticDBProjectResponseBody(DaraModel):
    def __init__(
        self,
        branch_compute_cluster_id: str = None,
        create_time: str = None,
        default_branch_id: str = None,
        default_branch_name: str = None,
        project_id: str = None,
        project_name: str = None,
        request_id: str = None,
        tenant_id: str = None,
    ):
        # The ID of the compute instance associated with the default branch.
        self.branch_compute_cluster_id = branch_compute_cluster_id
        # The time when the project was created.
        self.create_time = create_time
        # The default branch ID.
        self.default_branch_id = default_branch_id
        # The default branch name.
        self.default_branch_name = default_branch_name
        # The ID of the new project.
        self.project_id = project_id
        # The project name.
        self.project_name = project_name
        # The request ID.
        self.request_id = request_id
        # The tenant ID.
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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.default_branch_id is not None:
            result['DefaultBranchId'] = self.default_branch_id

        if self.default_branch_name is not None:
            result['DefaultBranchName'] = self.default_branch_name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchComputeClusterId') is not None:
            self.branch_compute_cluster_id = m.get('BranchComputeClusterId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DefaultBranchId') is not None:
            self.default_branch_id = m.get('DefaultBranchId')

        if m.get('DefaultBranchName') is not None:
            self.default_branch_name = m.get('DefaultBranchName')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

