# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateYikeUserRequest(DaraModel):
    def __init__(
        self,
        nickname: str = None,
        password: str = None,
        production_ids: str = None,
        user_name_prefix: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.nickname = nickname
        # This parameter is required.
        self.password = password
        # This parameter is required.
        self.production_ids = production_ids
        # This parameter is required.
        self.user_name_prefix = user_name_prefix
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nickname is not None:
            result['Nickname'] = self.nickname

        if self.password is not None:
            result['Password'] = self.password

        if self.production_ids is not None:
            result['ProductionIds'] = self.production_ids

        if self.user_name_prefix is not None:
            result['UserNamePrefix'] = self.user_name_prefix

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Nickname') is not None:
            self.nickname = m.get('Nickname')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('ProductionIds') is not None:
            self.production_ids = m.get('ProductionIds')

        if m.get('UserNamePrefix') is not None:
            self.user_name_prefix = m.get('UserNamePrefix')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

