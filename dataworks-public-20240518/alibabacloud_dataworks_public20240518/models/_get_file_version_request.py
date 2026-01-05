# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetFileVersionRequest(DaraModel):
    def __init__(
        self,
        file_id: int = None,
        file_version: int = None,
        project_id: int = None,
        project_identifier: str = None,
    ):
        # The file ID. You can call the [ListFiles](https://help.aliyun.com/document_detail/173942.html) operation to query the ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The file version whose information you want to query.
        # 
        # This parameter is required.
        self.file_version = file_version
        # The DataWorks workspace ID. You can click the Workspace Manage icon in the upper-right corner of the DataStudio page to go to the Workspace page and query the workspace ID.
        self.project_id = project_id
        # The unique identifier of the DataWorks workspace. You can view the identifier in the upper part of the DataStudio page. You can also select another identifier to switch to another workspace.
        # 
        # You must configure either this parameter or the ProjectId parameter to determine the DataWorks workspace to which the operation is applied.
        self.project_identifier = project_identifier

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_version is not None:
            result['FileVersion'] = self.file_version

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_identifier is not None:
            result['ProjectIdentifier'] = self.project_identifier

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileVersion') is not None:
            self.file_version = m.get('FileVersion')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectIdentifier') is not None:
            self.project_identifier = m.get('ProjectIdentifier')

        return self

