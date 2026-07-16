# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateEdgeContainerAppLogRiverRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        path: str = None,
        stdout: bool = None,
    ):
        # The application ID. You can call the [ListEdgeContainerApps](https://help.aliyun.com/document_detail/2852396.html) operation to obtain the application ID.
        # >Notice: The AppId is in the format of the app- prefix followed by a numeric suffix, with a total length of 20 to 64 characters (example: app-8806886***83794688). Call ListEdgeContainerApps to obtain an existing AppId, or call CreateEdgeContainerApp to create an application first.</notice>.
        self.app_id = app_id
        # The log file of the container.
        self.path = path
        # Specifies whether to enable standard output collection for the container.
        self.stdout = stdout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.path is not None:
            result['Path'] = self.path

        if self.stdout is not None:
            result['Stdout'] = self.stdout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Stdout') is not None:
            self.stdout = m.get('Stdout')

        return self

