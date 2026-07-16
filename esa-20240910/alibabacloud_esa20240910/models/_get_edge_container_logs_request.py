# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEdgeContainerLogsRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        lines: int = None,
    ):
        # The application ID. You can call the [ListEdgeContainerApps](~~ListEdgeContainerApps~~) operation to obtain the application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The number of log lines to output.>Notice: Valid values: 1 to 5000. If the value exceeds the upper limit, an error is returned.</notice>.
        # 
        # This parameter is required.
        self.lines = lines

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.lines is not None:
            result['Lines'] = self.lines

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Lines') is not None:
            self.lines = m.get('Lines')

        return self

