# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetFolderRequest(DaraModel):
    def __init__(
        self,
        folder_id: str = None,
        folder_path: str = None,
        project_id: int = None,
        project_identifier: str = None,
    ):
        # The folder ID. Either this parameter or FolderPath must be specified. You can call the [ListFolders](https://help.aliyun.com/document_detail/173955.html) operation to obtain the folder ID.
        self.folder_id = folder_id
        # The folder path. Either this parameter or FolderId must be specified. You can call the [ListFolders](https://help.aliyun.com/document_detail/173955.html) operation to obtain the folder path.
        self.folder_path = folder_path
        # The ID of the DataWorks workspace. You can obtain the workspace ID from the workspace configuration page in the DataWorks console. Either this parameter or ProjectIdentifier must be specified to determine which DataWorks workspace this API call operates on.
        self.project_id = project_id
        # The name of the DataWorks workspace. You can obtain the workspace name from the workspace configuration page in the DataWorks console. Either this parameter or ProjectId must be specified to determine which DataWorks workspace this API call operates on.
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

        if self.folder_path is not None:
            result['FolderPath'] = self.folder_path

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_identifier is not None:
            result['ProjectIdentifier'] = self.project_identifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('FolderPath') is not None:
            self.folder_path = m.get('FolderPath')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectIdentifier') is not None:
            self.project_identifier = m.get('ProjectIdentifier')

        return self

