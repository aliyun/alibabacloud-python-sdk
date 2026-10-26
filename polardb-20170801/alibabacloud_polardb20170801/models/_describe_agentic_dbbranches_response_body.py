# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeAgenticDBBranchesResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeAgenticDBBranchesResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of branches.
        self.items = items
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeAgenticDBBranchesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAgenticDBBranchesResponseBodyItems(DaraModel):
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
        parent_timestamp: str = None,
        project_id: str = None,
        project_name: str = None,
        status: str = None,
        tenant_id: str = None,
    ):
        # The ID of the compute cluster for the branch.
        self.branch_compute_cluster_id = branch_compute_cluster_id
        # The number of compute nodes. The value is fixed to 1 in the first phase.
        self.branch_compute_node_count = branch_compute_node_count
        # The ID of the branch.
        self.branch_id = branch_id
        # The name of the branch.
        self.branch_name = branch_name
        # The time when the branch was created. The time is displayed in ISO 8601 format in UTC (YYYY-MM-DDTHH:mm:ssZ).
        self.create_time = create_time
        # The description of the branch.
        self.description = description
        # Indicates whether the branch is the default branch.
        self.is_default_branch = is_default_branch
        # The time when the branch was last activated.
        self.last_activated_at = last_activated_at
        # The maximum number of compute units (CUs).
        self.max_cu = max_cu
        # The minimum number of compute units (CUs).
        self.min_cu = min_cu
        # The ID of the parent branch.
        self.parent_branch_id = parent_branch_id
        # The name of the parent branch.
        self.parent_branch_name = parent_branch_name
        # The historical time of the parent branch specified when the branch was created. The time is displayed in RFC 3339 format in UTC. This parameter may be empty if no historical time is specified or for legacy records.
        self.parent_timestamp = parent_timestamp
        # The project ID.
        self.project_id = project_id
        # The name of the project to which the branch belongs.
        self.project_name = project_name
        # The status of the branch. Valid values: Running, Pending, and Paused.
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

        if self.parent_timestamp is not None:
            result['ParentTimestamp'] = self.parent_timestamp

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

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

        if m.get('ParentTimestamp') is not None:
            self.parent_timestamp = m.get('ParentTimestamp')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

