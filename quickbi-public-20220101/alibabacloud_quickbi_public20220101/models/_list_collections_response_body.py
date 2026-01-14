# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class ListCollectionsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListCollectionsResponseBodyResult] = None,
        success: bool = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Details of the list of reports favored by the user.
        self.result = result
        # The primary key ID of the favorite record.
        self.success = success

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListCollectionsResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListCollectionsResponseBodyResult(DaraModel):
    def __init__(
        self,
        favorite_id: int = None,
        owner_id: str = None,
        works_id: str = None,
        works_name: str = None,
        works_type: str = None,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        # The primary key ID of the favorite record.
        self.favorite_id = favorite_id
        # The user ID of the work owner. This refers to the UserID in Quick BI, not the Alibaba Cloud UID.
        self.owner_id = owner_id
        # The ID of the work.
        self.works_id = works_id
        # The name of the work.
        self.works_name = works_name
        # The type of the work. Possible values:
        # 
        # - DATAPRODUCT: Data Portal
        # - PAGE: Dashboard
        # - REPORT: Spreadsheet
        # - dataForm: Data Entry Form
        # - dashboardOfflineQuery: Self-service Data Extraction
        self.works_type = works_type
        # Workspace ID.
        self.workspace_id = workspace_id
        # Workspace Name.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.favorite_id is not None:
            result['FavoriteId'] = self.favorite_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.works_id is not None:
            result['WorksId'] = self.works_id

        if self.works_name is not None:
            result['WorksName'] = self.works_name

        if self.works_type is not None:
            result['WorksType'] = self.works_type

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.workspace_name is not None:
            result['WorkspaceName'] = self.workspace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FavoriteId') is not None:
            self.favorite_id = m.get('FavoriteId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('WorksId') is not None:
            self.works_id = m.get('WorksId')

        if m.get('WorksName') is not None:
            self.works_name = m.get('WorksName')

        if m.get('WorksType') is not None:
            self.works_type = m.get('WorksType')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WorkspaceName') is not None:
            self.workspace_name = m.get('WorkspaceName')

        return self

