# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateStackRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        name: str = None,
        ram_role: str = None,
        source_path: str = None,
        working_directory: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.name = name
        self.ram_role = ram_role
        self.source_path = source_path
        self.working_directory = working_directory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.ram_role is not None:
            result['ramRole'] = self.ram_role

        if self.source_path is not None:
            result['sourcePath'] = self.source_path

        if self.working_directory is not None:
            result['workingDirectory'] = self.working_directory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')

        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')

        if m.get('workingDirectory') is not None:
            self.working_directory = m.get('workingDirectory')

        return self

