# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListAssetInfoPublishRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        uuid_list: List[str] = None,
    ):
        # An extended parameter. This parameter is temporarily unavailable.
        self.name = name
        # The UUIDs of the servers that you want to query.
        # 
        # This parameter is required.
        self.uuid_list = uuid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        return self

