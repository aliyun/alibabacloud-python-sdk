# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateKnowledgeBaseDirectoryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        directory_id: str = None,
        directory_kind: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        message: str = None,
        name: str = None,
        parent_directory_id: str = None,
        path: str = None,
        request_id: str = None,
    ):
        # The status code.
        self.code = code
        # The description of the to-do card type.
        self.description = description
        # The directory ID.
        self.directory_id = directory_id
        # The directory type.
        self.directory_kind = directory_kind
        # The creation time.
        self.gmt_create = gmt_create
        # The last modification time.
        self.gmt_modified = gmt_modified
        # The description of the status code.
        self.message = message
        # The name.
        self.name = name
        # The directory ID.
        self.parent_directory_id = parent_directory_id
        # The path of the node.
        self.path = path
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.description is not None:
            result['description'] = self.description

        if self.directory_id is not None:
            result['directoryId'] = self.directory_id

        if self.directory_kind is not None:
            result['directoryKind'] = self.directory_kind

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.message is not None:
            result['message'] = self.message

        if self.name is not None:
            result['name'] = self.name

        if self.parent_directory_id is not None:
            result['parentDirectoryId'] = self.parent_directory_id

        if self.path is not None:
            result['path'] = self.path

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('directoryKind') is not None:
            self.directory_kind = m.get('directoryKind')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('parentDirectoryId') is not None:
            self.parent_directory_id = m.get('parentDirectoryId')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

