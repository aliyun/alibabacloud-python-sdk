# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProjectRolesShrinkRequest(DaraModel):
    def __init__(
        self,
        codes_shrink: str = None,
        names_shrink: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        type: str = None,
    ):
        # The list of workspace role codes.
        self.codes_shrink = codes_shrink
        # The list of workspace role names.
        self.names_shrink = names_shrink
        # The page number. Used for paging.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the workspace management page to obtain the ID.
        # 
        # This parameter specifies the DataWorks workspace for this API invoke operation.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The type of the workspace role. Valid values:
        # - UserCustom: user-defined role.
        # - System: system role.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.codes_shrink is not None:
            result['Codes'] = self.codes_shrink

        if self.names_shrink is not None:
            result['Names'] = self.names_shrink

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Codes') is not None:
            self.codes_shrink = m.get('Codes')

        if m.get('Names') is not None:
            self.names_shrink = m.get('Names')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

