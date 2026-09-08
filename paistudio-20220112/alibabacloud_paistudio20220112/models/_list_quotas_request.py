# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListQuotasRequest(DaraModel):
    def __init__(
        self,
        cluster_type: str = None,
        gputype: str = None,
        has_resource: str = None,
        labels: str = None,
        layout_mode: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        parent_quota_id: str = None,
        quota_ids: str = None,
        quota_name: str = None,
        resource_type: str = None,
        sort_by: str = None,
        statuses: str = None,
        verbose: bool = None,
        versions: str = None,
        workspace_ids: str = None,
        workspace_name: str = None,
    ):
        # The cluster type.
        self.cluster_type = cluster_type
        self.gputype = gputype
        self.has_resource = has_resource
        # Filters by label key and value. Separate multiple labels with commas (,).
        self.labels = labels
        # The display mode. Valid values: tree or list.
        self.layout_mode = layout_mode
        # The sort order. Valid values: desc or asc.
        self.order = order
        # The page number to query. Minimum value: 1.
        self.page_number = page_number
        # The number of entries per page. Minimum value: 1.
        self.page_size = page_size
        # Filters by ParentQuotaId:
        # 
        # - Not specified: lists all quotas under the tenant, including root quotas and child quotas.
        # 
        # - Empty string: lists all root quotas.
        # 
        # - Non-empty string: lists all child quotas of the specified ParentQuotaId.
        self.parent_quota_id = parent_quota_id
        # Comma-separated QuotaIds for filtering. Only exact match is supported. A maximum of 100 IDs can be specified at a time.
        self.quota_ids = quota_ids
        # Filters by QuotaName. Fuzzy match is supported.
        self.quota_name = quota_name
        # The resource type of the quota (Lingjun/ECS/ACS). Default value: ECS.
        self.resource_type = resource_type
        # The field by which to sort the results. Valid values:
        # 
        # - QuotaName
        # 
        # - Status
        # 
        # - CPU
        # 
        # - Memory
        # 
        # - GPU
        # 
        # - GmtCreatedTime
        # 
        # - GmtModifiedTime
        self.sort_by = sort_by
        # Comma-separated quota statuses for filtering. Only exact match is supported.
        self.statuses = statuses
        # Specifies whether to display details. Valid values:
        # - true: Displays details.
        # - false: Does not display details.
        self.verbose = verbose
        # Filters by version information.
        self.versions = versions
        # Comma-separated WorkspaceIds for filtering. Only exact match is supported. A maximum of 10 IDs can be specified at a time.
        self.workspace_ids = workspace_ids
        # The name of the associated workspace.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.gputype is not None:
            result['GPUType'] = self.gputype

        if self.has_resource is not None:
            result['HasResource'] = self.has_resource

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.layout_mode is not None:
            result['LayoutMode'] = self.layout_mode

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.parent_quota_id is not None:
            result['ParentQuotaId'] = self.parent_quota_id

        if self.quota_ids is not None:
            result['QuotaIds'] = self.quota_ids

        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.statuses is not None:
            result['Statuses'] = self.statuses

        if self.verbose is not None:
            result['Verbose'] = self.verbose

        if self.versions is not None:
            result['Versions'] = self.versions

        if self.workspace_ids is not None:
            result['WorkspaceIds'] = self.workspace_ids

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')

        if m.get('HasResource') is not None:
            self.has_resource = m.get('HasResource')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('LayoutMode') is not None:
            self.layout_mode = m.get('LayoutMode')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ParentQuotaId') is not None:
            self.parent_quota_id = m.get('ParentQuotaId')

        if m.get('QuotaIds') is not None:
            self.quota_ids = m.get('QuotaIds')

        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')

        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')

        if m.get('Versions') is not None:
            self.versions = m.get('Versions')

        if m.get('WorkspaceIds') is not None:
            self.workspace_ids = m.get('WorkspaceIds')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

