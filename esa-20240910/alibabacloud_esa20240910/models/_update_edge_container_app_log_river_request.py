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
        # The application ID, which can be obtained by calling the [ListEdgeContainerApps](https://help.aliyun.com/document_detail/2852396.html) operation.
        self.app_id = app_id
        # The log path of the container.
        self.path = path
        # Specifies whether to collect the standard output of the container.
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

