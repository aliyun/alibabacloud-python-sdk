# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeAgenticDBBranchLineageResponseBody(DaraModel):
    def __init__(
        self,
        anchor_branch_id: str = None,
        items: List[main_models.DescribeAgenticDBBranchLineageResponseBodyItems] = None,
        node_count: int = None,
        project_id: str = None,
        project_name: str = None,
        request_id: str = None,
        root_branch_id: str = None,
        tenant_id: str = None,
    ):
        # The anchor branch ID.
        self.anchor_branch_id = anchor_branch_id
        # The list of lineage nodes.
        self.items = items
        # The total number of returned nodes.
        self.node_count = node_count
        # The project ID.
        self.project_id = project_id
        # The project name.
        self.project_name = project_name
        # The request ID.
        self.request_id = request_id
        # The primary branch ID.
        self.root_branch_id = root_branch_id
        # The tenant ID.
        self.tenant_id = tenant_id

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
        if self.anchor_branch_id is not None:
            result['AnchorBranchId'] = self.anchor_branch_id

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root_branch_id is not None:
            result['RootBranchId'] = self.root_branch_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnchorBranchId') is not None:
            self.anchor_branch_id = m.get('AnchorBranchId')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeAgenticDBBranchLineageResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RootBranchId') is not None:
            self.root_branch_id = m.get('RootBranchId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

class DescribeAgenticDBBranchLineageResponseBodyItems(DaraModel):
    def __init__(
        self,
        branch_compute_cluster_id: str = None,
        branch_description: str = None,
        branch_id: str = None,
        branch_name: str = None,
        create_time: str = None,
        depth: int = None,
        direct_child_count: int = None,
        has_more_ancestors: bool = None,
        has_more_children: bool = None,
        is_anchor: bool = None,
        is_default_branch: bool = None,
        is_root: bool = None,
        parent_branch_id: str = None,
        parent_branch_name: str = None,
        status: str = None,
    ):
        # The compute cluster ID of the branch.
        self.branch_compute_cluster_id = branch_compute_cluster_id
        # The branch description.
        self.branch_description = branch_description
        # The branch ID.
        self.branch_id = branch_id
        # The branch name.
        self.branch_name = branch_name
        # The time when the branch was created.
        self.create_time = create_time
        # The depth relative to the anchor branch. The anchor branch has a depth of 0. Ancestor branches have negative values. Descendant branches have positive values.
        self.depth = depth
        # The total number of direct child branches.
        self.direct_child_count = direct_child_count
        # Indicates whether more ancestor nodes exist but are not returned.
        self.has_more_ancestors = has_more_ancestors
        # Indicates whether more child nodes exist but are not returned.
        self.has_more_children = has_more_children
        # Indicates whether the branch is the anchor branch.
        self.is_anchor = is_anchor
        self.is_default_branch = is_default_branch
        # Indicates whether the branch is the primary branch.
        self.is_root = is_root
        # The parent branch ID.
        self.parent_branch_id = parent_branch_id
        # The parent branch name.
        self.parent_branch_name = parent_branch_name
        # The branch status. Valid values:
        # - Active
        # - Destroying
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

        if self.branch_description is not None:
            result['BranchDescription'] = self.branch_description

        if self.branch_id is not None:
            result['BranchId'] = self.branch_id

        if self.branch_name is not None:
            result['BranchName'] = self.branch_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.depth is not None:
            result['Depth'] = self.depth

        if self.direct_child_count is not None:
            result['DirectChildCount'] = self.direct_child_count

        if self.has_more_ancestors is not None:
            result['HasMoreAncestors'] = self.has_more_ancestors

        if self.has_more_children is not None:
            result['HasMoreChildren'] = self.has_more_children

        if self.is_anchor is not None:
            result['IsAnchor'] = self.is_anchor

        if self.is_default_branch is not None:
            result['IsDefaultBranch'] = self.is_default_branch

        if self.is_root is not None:
            result['IsRoot'] = self.is_root

        if self.parent_branch_id is not None:
            result['ParentBranchId'] = self.parent_branch_id

        if self.parent_branch_name is not None:
            result['ParentBranchName'] = self.parent_branch_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchComputeClusterId') is not None:
            self.branch_compute_cluster_id = m.get('BranchComputeClusterId')

        if m.get('BranchDescription') is not None:
            self.branch_description = m.get('BranchDescription')

        if m.get('BranchId') is not None:
            self.branch_id = m.get('BranchId')

        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Depth') is not None:
            self.depth = m.get('Depth')

        if m.get('DirectChildCount') is not None:
            self.direct_child_count = m.get('DirectChildCount')

        if m.get('HasMoreAncestors') is not None:
            self.has_more_ancestors = m.get('HasMoreAncestors')

        if m.get('HasMoreChildren') is not None:
            self.has_more_children = m.get('HasMoreChildren')

        if m.get('IsAnchor') is not None:
            self.is_anchor = m.get('IsAnchor')

        if m.get('IsDefaultBranch') is not None:
            self.is_default_branch = m.get('IsDefaultBranch')

        if m.get('IsRoot') is not None:
            self.is_root = m.get('IsRoot')

        if m.get('ParentBranchId') is not None:
            self.parent_branch_id = m.get('ParentBranchId')

        if m.get('ParentBranchName') is not None:
            self.parent_branch_name = m.get('ParentBranchName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

