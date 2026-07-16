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
        # The list of return fields for workspace details. This parameter limits the workspace properties returned in the result.
        # Separate multiple properties with commas (,). Currently, only Id is supported, which represents the workspace ID.
        self.fields = fields
        # The comma-separated list of modules. Default value: PAI.
        self.module_list = module_list
        # The query option. Valid values:
        # * GetWorkspaces (default): retrieves the workspace list. The Workspaces parameter is returned.
        # * GetResourceLimits: retrieves resource limits. The ResourceLimits parameter is returned.
        self.option = option
        # The sort order for the specified sort field in a paged query. Valid values:
        # * ASC (default): ascending order.
        # * DESC: descending order.
        self.order = order
        # The page number of the workspace list. Minimum value: 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page in a paged query. Default value: 20.
        self.page_size = page_size
        # The resource group ID. For information about how to view the resource group ID, see [View basic information of a resource group](https://help.aliyun.com/document_detail/151181.html).
        self.resource_group_id = resource_group_id
        # The field used for sorting in a paged query. Default value: GmtCreateTime. Valid values:
        # * GmtCreateTime (default): sorts by creation time.
        # * GmtModifiedTime: sorts by modification time.
        self.sort_by = sort_by
        # The workspace status. Valid values:
        # 
        # - ENABLED: Normal.
        # - INITIALIZING: Being initialized.
        # - FAILURE: Failed.
        # - DISABLED: Manually disabled.
        # - FROZEN: Frozen due to overdue payment.
        # - UPDATING: Being updated.
        self.status = status
        self.user_id = user_id
        # Specifies whether to display detailed workspace information. Valid values:
        # - false (default): does not display detailed information.
        # - true: displays detailed information.
        self.verbose = verbose
        # The list of workspace IDs. Separate multiple workspace IDs with commas (,).
        self.workspace_ids = workspace_ids
        # The workspace name.
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

