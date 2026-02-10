# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAssetImportantRequest(DaraModel):
    def __init__(
        self,
        important_code: int = None,
        uuid_list: str = None,
    ):
        # The importance of the asset. Valid values:
        # 
        # *   **0**: test
        # *   **1**: normal
        # *   **2**: important
        self.important_code = important_code
        # The UUIDs of servers. Separate multiple UUIDs with commas (,).
        # 
        # >  You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to query the UUIDs of servers.
        self.uuid_list = uuid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.important_code is not None:
            result['ImportantCode'] = self.important_code

        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportantCode') is not None:
            self.important_code = m.get('ImportantCode')

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        return self

