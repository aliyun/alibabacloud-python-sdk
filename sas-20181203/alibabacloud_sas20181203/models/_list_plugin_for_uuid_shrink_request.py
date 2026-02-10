# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPluginForUuidShrinkRequest(DaraModel):
    def __init__(
        self,
        types_shrink: str = None,
        uuid: str = None,
    ):
        # The plug-in types.
        self.types_shrink = types_shrink
        # The UUID of the server.
        # 
        # >  You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to query the UUIDs of servers.
        # 
        # This parameter is required.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.types_shrink is not None:
            result['Types'] = self.types_shrink

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Types') is not None:
            self.types_shrink = m.get('Types')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

