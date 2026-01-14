# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateChatSessionRequest(DaraModel):
    def __init__(
        self,
        folder_id: str = None,
        name: str = None,
        user_id: str = None,
    ):
        # Folder ID, to search for Q&A content within the current folder and its subfolders.
        # 
        # This parameter is required.
        self.folder_id = folder_id
        # Name of the current session.
        # 
        # This parameter is required.
        self.name = name
        # The unique identifier of the user. If not provided, the SDK calling account will be used as the user ID by default.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.folder_id is not None:
            result['folderId'] = self.folder_id

        if self.name is not None:
            result['name'] = self.name

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

