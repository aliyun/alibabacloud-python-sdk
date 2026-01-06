# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWorkspacesRequest(DaraModel):
    def __init__(
        self,
        fields: str = None,
        module_list: str = None,
        option: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        sort_by: str = None,
        status: str = None,
        user_id: str = None,
        verbose: bool = None,
        workspace_ids: str = None,
        workspace_name: str = None,
    ):
        # The list of returned fields of workspace details. Used to limit the fields in the returned results. Separate multiple fields with commas (,). Currently, only Id is supported, which is the workspace ID.
        self.fields = fields
        # The modules, separated by commas (,). Default value: PAI.
        self.module_list = module_list
        # The query options. Valid values:
        # 
        # *   GetWorkspaces (default): Obtains a list of Workspaces.
        # *   GetResourceLimits: Obtains a list of ResourceLimits.
        self.option = option
        # The order of results (ascending or descending). Valid values:
        # 
        # *   ASC: ascending order. This is the default value.
        # *   DESC: descending order.
        self.order = order
        # The page number of the workspace list. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 20.
        self.page_size = page_size
        # The resource group ID. To obtain the ID of a resource group, see [View basic information of a resource group](https://help.aliyun.com/document_detail/151181.html).
        self.resource_group_id = resource_group_id
        # Specifies how to sort the results. Default value: GmtCreateTime. Valid values:
        # 
        # *   GmtCreateTime: Sort by the time when created.
        # *   GmtModifiedTime: Sort by the time when modified.
        self.sort_by = sort_by
        # The workspace status. Valid values:
        # 
        # *   ENABLED
        # *   INITIALIZING
        # *   FAILURE
        # *   DISABLED
        # *   FROZEN
        # *   UPDATING
        self.status = status
        self.user_id = user_id
        # Specifies whether to display workspace details. Valid values:
        # 
        # *   false (default)
        # *   true
        self.verbose = verbose
        # The workspace IDs. Separate multiple IDs by commas (,).
        self.workspace_ids = workspace_ids
        # The name of the workspace.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fields is not None:
            result['Fields'] = self.fields

        if self.module_list is not None:
            result['ModuleList'] = self.module_list

        if self.option is not None:
            result['Option'] = self.option

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.verbose is not None:
            result['Verbose'] = self.verbose

        if self.workspace_ids is not None:
            result['WorkspaceIds'] = self.workspace_ids

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')

        if m.get('ModuleList') is not None:
            self.module_list = m.get('ModuleList')

        if m.get('Option') is not None:
            self.option = m.get('Option')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Verbose') is not None:
            self.verbose = m.get('Verbose')

        if m.get('WorkspaceIds') is not None:
            self.workspace_ids = m.get('WorkspaceIds')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

