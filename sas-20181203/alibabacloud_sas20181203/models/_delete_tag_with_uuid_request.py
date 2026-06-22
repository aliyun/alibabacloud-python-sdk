# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteTagWithUuidRequest(DaraModel):
    def __init__(
        self,
        tag_name: str = None,
        uuid_list: str = None,
    ):
        # The label name.
        # 
        # This parameter is required.
        self.tag_name = tag_name
        # The list of server UUIDs.
        # > If UuidList is specified, Security Center deletes the label only from the servers included in UuidList. If UuidList is empty, Security Center deletes the label from all servers.
        self.uuid_list = uuid_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        if self.uuid_list is not None:
            result['UuidList'] = self.uuid_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        if m.get('UuidList') is not None:
            self.uuid_list = m.get('UuidList')

        return self

