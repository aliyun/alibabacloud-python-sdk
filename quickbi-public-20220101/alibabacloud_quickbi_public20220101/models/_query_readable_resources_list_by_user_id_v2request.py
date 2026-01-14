# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryReadableResourcesListByUserIdV2Request(DaraModel):
    def __init__(
        self,
        user_id: str = None,
        work_type: str = None,
        workspace_id: str = None,
    ):
        # User ID.
        # 
        # This parameter is required.
        self.user_id = user_id
        # Work type. Possible values:
        # - DATAPRODUCT: Data Portal
        # - PAGE: Dashboard
        # - REPORT: Spreadsheet
        # - dashboardOfflineQuery: Self-service Data Extraction
        # - SCREEN: Data Wall
        # - DATAFORM: Data Entry
        # - ANALYSIS: Ad-hoc Analysis
        self.work_type = work_type
        # Workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.work_type is not None:
            result['WorkType'] = self.work_type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorkType') is not None:
            self.work_type = m.get('WorkType')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

