# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChatBIFileUploadCallbackRequest(DaraModel):
    def __init__(
        self,
        character_set_name: str = None,
        db_name: str = None,
        file_name: str = None,
        instance_name: str = None,
        table_name: str = None,
        table_type: str = None,
    ):
        self.character_set_name = character_set_name
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.file_name = file_name
        # This parameter is required.
        self.instance_name = instance_name
        # This parameter is required.
        self.table_name = table_name
        # This parameter is required.
        self.table_type = table_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.character_set_name is not None:
            result['CharacterSetName'] = self.character_set_name

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.table_type is not None:
            result['TableType'] = self.table_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CharacterSetName') is not None:
            self.character_set_name = m.get('CharacterSetName')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')

        return self

