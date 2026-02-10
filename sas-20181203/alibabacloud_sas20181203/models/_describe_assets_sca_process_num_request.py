# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeAssetsScaProcessNumRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        uuid_list: List[str] = None,
    ):
        # The type of the application process. Default value: java. Valid values:
        # 
        # *   **java**
        # *   **php**
        self.biz_type = biz_type
        # The UUIDs of the servers.
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
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        return self

