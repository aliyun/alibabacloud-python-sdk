# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListProjectRolesRequest(DaraModel):
    def __init__(
        self,
        codes: List[str] = None,
        names: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        project_id: int = None,
        type: str = None,
    ):
        # An array of workspace role codes.
        self.codes = codes
        # An array of workspace role names.
        self.names = names
        # The page number to return.
        self.page_number = page_number
        # The number of entries to return per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The ID of the DataWorks workspace. You can find the ID on the Workspace Management page in the [DataWorks console](https://workbench.data.aliyun.com/console).
        # 
        # This parameter specifies the DataWorks workspace for which you want to list roles.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The type of the workspace role.
        # 
        # - `UserCustom`: Custom Role
        # 
        # - `System`: System Role
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.codes is not None:
            result['Codes'] = self.codes

        if self.names is not None:
            result['Names'] = self.names

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
            self.codes = m.get('Codes')

        if m.get('Names') is not None:
            self.names = m.get('Names')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

