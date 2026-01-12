# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryCallbackRequest(DaraModel):
    def __init__(
        self,
        check_for_oss: bool = None,
        id: int = None,
        region_id: str = None,
    ):
        # Query data under the OSS detection task.
        self.check_for_oss = check_for_oss
        # Primary key ID.
        # 
        # This parameter is required.
        self.id = id
        # Region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_for_oss is not None:
            result['CheckForOss'] = self.check_for_oss

        if self.id is not None:
            result['Id'] = self.id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckForOss') is not None:
            self.check_for_oss = m.get('CheckForOss')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

