# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGroupFileRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        directory_id: str = None,
        file_record_id: str = None,
        group_id: str = None,
        name: str = None,
        source_tags: str = None,
        tenant_id: str = None,
    ):
        # The description of the AI assistant.
        self.description = description
        # The folder ID.
        self.directory_id = directory_id
        # The file record ID. This parameter is optional and corresponds to settings.file_record_id.
        # 
        # This parameter is required.
        self.file_record_id = file_record_id
        # The project group ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The name.
        # 
        # This parameter is required.
        self.name = name
        # The source tags.
        self.source_tags = source_tags
        # The tenant ID.
        self.tenant_id = tenant_id

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

        if self.file_record_id is not None:
            result['fileRecordId'] = self.file_record_id

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.name is not None:
            result['name'] = self.name

        if self.source_tags is not None:
            result['sourceTags'] = self.source_tags

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')

        if m.get('fileRecordId') is not None:
            self.file_record_id = m.get('fileRecordId')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('sourceTags') is not None:
            self.source_tags = m.get('sourceTags')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

