# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryWorksByWorkspaceRequest(DaraModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        status: int = None,
        third_part_auth_flag: int = None,
        works_type: str = None,
        workspace_id: str = None,
    ):
        # The page number of the returned page.
        # 
        # *   Default value: 1.
        self.page_num = page_num
        # The number of entries returned per page.
        # 
        # *   Default value: 10.
        self.page_size = page_size
        # The status of the work. Valid values:
        # 
        # *   0: unpublished
        # *   1: published
        # *   2: modified but not published
        # *   3: unpublished
        self.status = status
        # Third-party embedding status. Valid values:
        # 
        # *   0: The embed service is not enabled.
        # *   1: Embed is enabled.
        self.third_part_auth_flag = third_part_auth_flag
        # The type of the work. Valid values:
        # 
        # *   DATAPRODUCT: BI portal
        # *   PAGE: Dashboard
        # *   FULLPAGE: full-screen dashboards
        # *   REPORT: workbook
        self.works_type = works_type
        # The ID of the workspace.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        if self.third_part_auth_flag is not None:
            result['ThirdPartAuthFlag'] = self.third_part_auth_flag

        if self.works_type is not None:
            result['WorksType'] = self.works_type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ThirdPartAuthFlag') is not None:
            self.third_part_auth_flag = m.get('ThirdPartAuthFlag')

        if m.get('WorksType') is not None:
            self.works_type = m.get('WorksType')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

