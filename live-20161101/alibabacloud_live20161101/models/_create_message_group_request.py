# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class CreateMessageGroupRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        creator_id: str = None,
        extension: Dict[str, str] = None,
    ):
        # The ID of the interactive messaging application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the creator. The ID can be up to 36 characters in length and can contain only letters and digits.
        # 
        # This parameter is required.
        self.creator_id = creator_id
        # The extended field.
        self.extension = extension

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.extension is not None:
            result['Extension'] = self.extension

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('Extension') is not None:
            self.extension = m.get('Extension')

        return self

