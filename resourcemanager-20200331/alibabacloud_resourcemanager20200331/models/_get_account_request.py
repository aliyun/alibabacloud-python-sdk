# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAccountRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        include_tags: bool = None,
    ):
        # The member account ID.
        # 
        # This parameter is required.
        self.account_id = account_id
        # Specifies whether to return tag information. Valid values:
        # 
        # - false (default): Does not return tag information.
        # - true: Returns tag information.
        self.include_tags = include_tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.include_tags is not None:
            result['IncludeTags'] = self.include_tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('IncludeTags') is not None:
            self.include_tags = m.get('IncludeTags')

        return self

