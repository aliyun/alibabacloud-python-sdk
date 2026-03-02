# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class NeuronDraftRecord(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        content: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        name: str = None,
        type: str = None,
    ):
        self.biz_id = biz_id
        # This parameter is required.
        self.content = content
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.name = name
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['bizId'] = self.biz_id

        if self.content is not None:
            result['content'] = self.content

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

