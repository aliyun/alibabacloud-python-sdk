# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEdgeContainerAppLogRiverResponseBody(DaraModel):
    def __init__(
        self,
        path: str = None,
        request_id: str = None,
        stdout: bool = None,
    ):
        # The log path of the container. It must be an absolute path that starts with a forward slash (/). You can use asterisks (\\*) and question marks (?) as wildcards.
        self.path = path
        # The request ID.
        self.request_id = request_id
        # Indicates whether the standard output of the container is collected.
        self.stdout = stdout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.path is not None:
            result['Path'] = self.path

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.stdout is not None:
            result['Stdout'] = self.stdout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Stdout') is not None:
            self.stdout = m.get('Stdout')

        return self

