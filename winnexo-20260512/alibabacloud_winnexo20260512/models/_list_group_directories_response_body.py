# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListGroupDirectoriesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        directories: List[main_models.ListGroupDirectoriesResponseBodyDirectories] = None,
        message: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The business status code. A value of 200 indicates success.
        self.code = code
        # The query root itself and all its descendant directories, including visible referenced directories in the space. The results are not paginated.
        self.directories = directories
        # The error description.
        self.message = message
        # The request trace ID.
        self.request_id = request_id
        # The number of returned directories, which equals the length of the directories array.
        self.total_count = total_count

    def validate(self):
        if self.directories:
            for v1 in self.directories:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['directories'] = []
        if self.directories is not None:
            for k1 in self.directories:
                result['directories'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.directories = []
        if m.get('directories') is not None:
            for k1 in m.get('directories'):
                temp_model = main_models.ListGroupDirectoriesResponseBodyDirectories()
                self.directories.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListGroupDirectoriesResponseBodyDirectories(DaraModel):
    def __init__(
        self,
        description: str = None,
        directory_id: str = None,
        directory_type: str = None,
        name: str = None,
        parent_directory_id: str = None,
        read_only: bool = None,
    ):
        # The directory description.
        self.description = description
        # The directory ID, including the query root itself and its descendants.
        self.directory_id = directory_id
        # The original directory type. The value is GROUP for physical directories in the space. Referenced directories retain their original type.
        self.directory_type = directory_type
        # The directory name.
        self.name = name
        # The parent directory ID. This value is empty for the internal root of the space.
        self.parent_directory_id = parent_directory_id
        # Indicates whether the directory is a read-only referenced directory. A value of false still requires creator or administrator permissions to modify the directory. The internal root is always unmodifiable.
        self.read_only = read_only

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.directory_type is not None:
            result['directoryType'] = self.directory_type

        if self.name is not None:
            result['name'] = self.name

        if self.parent_directory_id is not None:
            result['parentDirectoryId'] = self.parent_directory_id

        if self.read_only is not None:
            result['readOnly'] = self.read_only

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('directoryType') is not None:
            self.directory_type = m.get('directoryType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('parentDirectoryId') is not None:
            self.parent_directory_id = m.get('parentDirectoryId')

        if m.get('readOnly') is not None:
            self.read_only = m.get('readOnly')

        return self

