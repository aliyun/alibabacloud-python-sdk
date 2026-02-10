# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class JoinWebLockProcessWhiteListRequest(DaraModel):
    def __init__(
        self,
        process_paths: List[str] = None,
        uuids: str = None,
    ):
        # The paths of the processes.
        self.process_paths = process_paths
        # The UUIDs of the servers on which the processes run. Separate multiple UUIDs with commas (,).
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.process_paths is not None:
            result['ProcessPaths'] = self.process_paths

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProcessPaths') is not None:
            self.process_paths = m.get('ProcessPaths')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

