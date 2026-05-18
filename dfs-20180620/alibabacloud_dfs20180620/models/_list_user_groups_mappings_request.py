# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUserGroupsMappingsRequest(DaraModel):
    def __init__(
        self,
        filesystem_id: str = None,
        input_region_id: str = None,
        limit: int = None,
        next_token: str = None,
    ):
        # This parameter is required.
        self.filesystem_id = filesystem_id
        # This parameter is required.
        self.input_region_id = input_region_id
        self.limit = limit
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filesystem_id is not None:
            result['FilesystemId'] = self.filesystem_id

        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilesystemId') is not None:
            self.filesystem_id = m.get('FilesystemId')

        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

