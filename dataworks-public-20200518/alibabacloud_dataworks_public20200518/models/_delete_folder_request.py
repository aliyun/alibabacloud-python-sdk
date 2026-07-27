# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteFolderRequest(DaraModel):
    def __init__(
        self,
        folder_id: str = None,
        project_id: int = None,
        project_identifier: str = None,
    ):
        # The ID of the folder. For more information about how to obtain the folder ID, see [ListFolders](https://help.aliyun.com/document_detail/173955.html).
        # 
        # This parameter is required.
        self.folder_id = folder_id
        # The ID of the DataWorks workspace. To obtain the workspace ID, log on to the DataWorks console and go to the Workspace Management page. You must set this parameter or ProjectIdentifier to specify the DataWorks workspace for the API call.
        self.project_id = project_id
        # The name of the DataWorks workspace. To obtain the workspace name, log on to the DataWorks console and go to the Workspace Management page. You must set this parameter or ProjectId to specify the DataWorks workspace for the API call.
        self.project_identifier = project_identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_identifier is not None:
            result['ProjectIdentifier'] = self.project_identifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectIdentifier') is not None:
            self.project_identifier = m.get('ProjectIdentifier')

        return self

