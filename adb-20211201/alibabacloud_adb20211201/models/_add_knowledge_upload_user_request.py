# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddKnowledgeUploadUserRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        file_location: str = None,
        users: str = None,
    ):
        # The ID of the ADB instance.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The location of the knowledge base document.
        # 
        # This parameter is required.
        self.file_location = file_location
        # The JSON string of the authorized user array.
        # 
        # This parameter is required.
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.file_location is not None:
            result['FileLocation'] = self.file_location

        if self.users is not None:
            result['Users'] = self.users

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('FileLocation') is not None:
            self.file_location = m.get('FileLocation')

        if m.get('Users') is not None:
            self.users = m.get('Users')

        return self

