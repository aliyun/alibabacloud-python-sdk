# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitVideoCharacterReplaceJobRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_params: str = None,
        folder_id: str = None,
        project_id: str = None,
    ):
        # The ID of the video character replacement application. Use a configured application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The input parameters of the application, serialized as a JSON string. The field names and material requirements are subject to the input definition of the corresponding AppId.
        self.app_params = app_params
        # The folder ID.
        self.folder_id = folder_id
        # The project ID.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_params is not None:
            result['AppParams'] = self.app_params

        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppParams') is not None:
            self.app_params = m.get('AppParams')

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

