# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyClientConfStrategyRequest(DaraModel):
    def __init__(
        self,
        tag: str = None,
        tag_ext: str = None,
        tag_value: str = None,
        uuid: str = None,
        uuids: List[str] = None,
    ):
        # The key of the tag that is added to the agent configuration policy.
        # 
        # This parameter is required.
        self.tag = tag
        # The extended tag of the agent configuration policy.
        self.tag_ext = tag_ext
        # The value of the tag that is added to the agent configuration policy.
        # 
        # *   major
        # *   advanced
        # *   basic
        # 
        # This parameter is required.
        self.tag_value = tag_value
        # The UUID of the server that you want to query.
        self.uuid = uuid
        # The UUID of the asset. You can specify a maximum of 500 UUIDs at a time.
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag is not None:
            result['Tag'] = self.tag

        if self.tag_ext is not None:
            result['TagExt'] = self.tag_ext

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('TagExt') is not None:
            self.tag_ext = m.get('TagExt')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

