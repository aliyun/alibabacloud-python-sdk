# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RevokeDatabasePermissionRequest(DaraModel):
    def __init__(
        self,
        database_name: str = None,
        privileges: List[str] = None,
        user_name: str = None,
    ):
        self.database_name = database_name
        self.privileges = privileges
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_name is not None:
            result['databaseName'] = self.database_name

        if self.privileges is not None:
            result['privileges'] = self.privileges

        if self.user_name is not None:
            result['userName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('databaseName') is not None:
            self.database_name = m.get('databaseName')

        if m.get('privileges') is not None:
            self.privileges = m.get('privileges')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        return self

