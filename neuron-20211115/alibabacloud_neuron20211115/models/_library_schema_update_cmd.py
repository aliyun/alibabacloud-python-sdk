# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LibrarySchemaUpdateCmd(DaraModel):
    def __init__(
        self,
        artifact_id: str = None,
        description: str = None,
        git_group: str = None,
        group_id: str = None,
        id: int = None,
        library_id: int = None,
    ):
        self.artifact_id = artifact_id
        self.description = description
        self.git_group = git_group
        self.group_id = group_id
        self.id = id
        self.library_id = library_id

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

        if self.git_group is not None:
            result['gitGroup'] = self.git_group

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.id is not None:
            result['id'] = self.id

        if self.library_id is not None:
            result['libraryId'] = self.library_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('artifactId') is not None:
            self.artifact_id = m.get('artifactId')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('gitGroup') is not None:
            self.git_group = m.get('gitGroup')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')

        return self

