# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitYikeProjectExportJobRequest(DaraModel):
    def __init__(
        self,
        export_type: str = None,
        project_id: str = None,
        user_data: str = None,
    ):
        # The export type of the editing project. Valid values:
        # - PureAudio: pure audio (the export result returns a pure audio file and a subtitle file).
        self.export_type = export_type
        # The ID of the online editing project.
        self.project_id = project_id
        # The custom parameter in JSON string format. The callback result carries this parameter as-is (for example, newsKey).
        # The system reserved field NotifyAddress specifies the callback URL. After the task is complete, a callback is sent to this URL. Example: {"NotifyAddress": "http://xxx.callback.url"}
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.export_type is not None:
            result['ExportType'] = self.export_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

