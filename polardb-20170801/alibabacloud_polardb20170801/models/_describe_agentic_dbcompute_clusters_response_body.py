# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeAgenticDBComputeClustersResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeAgenticDBComputeClustersResponseBodyItems] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of compute instances.
        self.items = items
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
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
                temp_model = main_models.DescribeAgenticDBComputeClustersResponseBodyItems()
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

class DescribeAgenticDBComputeClustersResponseBodyItems(DaraModel):
    def __init__(
        self,
        branch_id: str = None,
        branch_name: str = None,
        compute_cluster_id: str = None,
        compute_node_count: int = None,
        create_time: str = None,
        description: str = None,
        is_default_branch: bool = None,
        last_activated_at: str = None,
        max_cu: str = None,
        min_cu: str = None,
        operator_type: str = None,
        parent_branch_id: str = None,
        parent_branch_name: str = None,
        project_id: str = None,
        project_name: str = None,
        status: str = None,
        storage_size: int = None,
        tenant_id: str = None,
        tenant_name: str = None,
    ):
        # The ID of the associated branch.
        self.branch_id = branch_id
        # The name of the associated branch.
        self.branch_name = branch_name
        # The compute instance ID.
        self.compute_cluster_id = compute_cluster_id
        # The number of compute nodes. The value is fixed to 1 in the first phase.
        self.compute_node_count = compute_node_count
        # The time when the compute instance was created.
        self.create_time = create_time
        # The description of the compute instance.
        self.description = description
        self.is_default_branch = is_default_branch
        # The time when the compute instance was last activated.
        self.last_activated_at = last_activated_at
        # The maximum compute unit.
        self.max_cu = max_cu
        # The minimum compute unit.
        self.min_cu = min_cu
        # The operator type.
        self.operator_type = operator_type
        self.parent_branch_id = parent_branch_id
        self.parent_branch_name = parent_branch_name
        # The ID of the associated project.
        self.project_id = project_id
        # The name of the associated project.
        self.project_name = project_name
        # The status of the compute instance.
        self.status = status
        # The amount of used data, in bytes.
        self.storage_size = storage_size
        # The ID of the associated tenant.
        self.tenant_id = tenant_id
        # The name of the associated tenant.
        self.tenant_name = tenant_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch_id is not None:
            result['BranchId'] = self.branch_id

        if self.branch_name is not None:
            result['BranchName'] = self.branch_name

        if self.compute_cluster_id is not None:
            result['ComputeClusterId'] = self.compute_cluster_id

        if self.compute_node_count is not None:
            result['ComputeNodeCount'] = self.compute_node_count

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

        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type

        if self.parent_branch_id is not None:
            result['ParentBranchId'] = self.parent_branch_id

        if self.parent_branch_name is not None:
            result['ParentBranchName'] = self.parent_branch_name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchId') is not None:
            self.branch_id = m.get('BranchId')

        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')

        if m.get('ComputeClusterId') is not None:
            self.compute_cluster_id = m.get('ComputeClusterId')

        if m.get('ComputeNodeCount') is not None:
            self.compute_node_count = m.get('ComputeNodeCount')

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

        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')

        if m.get('ParentBranchId') is not None:
            self.parent_branch_id = m.get('ParentBranchId')

        if m.get('ParentBranchName') is not None:
            self.parent_branch_name = m.get('ParentBranchName')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')

        return self

