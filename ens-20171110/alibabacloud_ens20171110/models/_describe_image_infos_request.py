# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeImageInfosRequest(DaraModel):
    def __init__(
        self,
        os_type: str = None,
    ):
        # The operating system type. Only a single type can be specified. If this parameter is not specified, all types are queried.
        # 
        # Valid values:
        # 
        # - Linux
        # 
        # - windows
        # 
        # In practice, passing linux or Linux may return an empty list, whereas omitting this parameter can return images with an OSType of linux. Verify the actual results before relying on this filter.
        self.os_type = os_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.os_type is not None:
            result['OsType'] = self.os_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        return self

