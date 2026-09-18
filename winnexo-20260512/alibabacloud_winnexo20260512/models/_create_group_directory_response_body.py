# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGroupDirectoryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        directory_id: str = None,
        directory_type: str = None,
        group_id: str = None,
        kb_root_directory_id: str = None,
        message: str = None,
        name: str = None,
        parent_directory_id: str = None,
        request_id: str = None,
    ):
        # SUCCESS indicates success. In failure cases, the corresponding error type is returned, such as ERR_BAD_REQUEST, ERR_VALIDATION_FAILED, or ERR_INTERNAL_SERVER_ERROR.
        self.code = code
        # The description of the AI assistant.
        self.description = description
        # The folder ID.
        self.directory_id = directory_id
        # The folder type.
        self.directory_type = directory_type
        # The project group ID.
        self.group_id = group_id
        # The root folder ID of the knowledge base.
        self.kb_root_directory_id = kb_root_directory_id
        # The response message.
        self.message = message
        # The name of the worksheet.
        self.name = name
        # The folder ID.
        self.parent_directory_id = parent_directory_id
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

        if self.directory_type is not None:
            result['directoryType'] = self.directory_type

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.kb_root_directory_id is not None:
            result['kbRootDirectoryId'] = self.kb_root_directory_id

        if self.message is not None:
            result['message'] = self.message

        if self.name is not None:
            result['name'] = self.name

        if self.parent_directory_id is not None:
            result['parentDirectoryId'] = self.parent_directory_id

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

        if m.get('directoryType') is not None:
            self.directory_type = m.get('directoryType')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('kbRootDirectoryId') is not None:
            self.kb_root_directory_id = m.get('kbRootDirectoryId')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('parentDirectoryId') is not None:
            self.parent_directory_id = m.get('parentDirectoryId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

