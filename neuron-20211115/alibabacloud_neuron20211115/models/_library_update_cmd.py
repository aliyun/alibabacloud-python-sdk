# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LibraryUpdateCmd(DaraModel):
    def __init__(
        self,
        artifact_id: str = None,
        description: str = None,
        group_id: str = None,
        id: int = None,
        name: str = None,
        repo_url: str = None,
    ):
        self.artifact_id = artifact_id
        self.description = description
        self.group_id = group_id
        self.id = id
        self.name = name
        self.repo_url = repo_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_id is not None:
            result['artifactId'] = self.artifact_id

        if self.description is not None:
            result['description'] = self.description

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.repo_url is not None:
            result['repoUrl'] = self.repo_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('artifactId') is not None:
            self.artifact_id = m.get('artifactId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('repoUrl') is not None:
            self.repo_url = m.get('repoUrl')

        return self

