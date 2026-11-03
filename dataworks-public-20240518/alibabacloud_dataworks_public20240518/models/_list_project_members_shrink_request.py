# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProjectMembersShrinkRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        role_codes_shrink: str = None,
        user_ids_shrink: str = None,
    ):
        # The page number of the requested data.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the workspace management page to obtain the ID.
        # 
        # This parameter specifies the DataWorks workspace used when you invoke this API operation.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The list of workspace role codes. You can call the [ListProjectRoles](https://help.aliyun.com/document_detail/2853930.html) operation to obtain the role codes.
        self.role_codes_shrink = role_codes_shrink
        # The list of DataWorks account IDs. You can log on to the [DataWorks console - Administration](https://dataworks.console.aliyun.com/product/ms_menu), select the workspace that you want to manage, go to the Administration page, and then go to the Tenant Members and Roles page to view the account IDs.
        self.user_ids_shrink = user_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.role_codes_shrink is not None:
            result['RoleCodes'] = self.role_codes_shrink

        if self.user_ids_shrink is not None:
            result['UserIds'] = self.user_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RoleCodes') is not None:
            self.role_codes_shrink = m.get('RoleCodes')

        if m.get('UserIds') is not None:
            self.user_ids_shrink = m.get('UserIds')

        return self

