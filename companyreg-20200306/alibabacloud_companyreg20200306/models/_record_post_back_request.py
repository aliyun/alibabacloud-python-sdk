# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RecordPostBackRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: str = None,
        contactor: str = None,
        content: str = None,
        entity_key: str = None,
    ):
        # This parameter is required.
        self.biz_id = biz_id
        # This parameter is required.
        self.biz_type = biz_type
        # This parameter is required.
        self.contactor = contactor
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.entity_key = entity_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['bizId'] = self.biz_id

        if self.biz_type is not None:
            result['bizType'] = self.biz_type

        if self.contactor is not None:
            result['contactor'] = self.contactor

        if self.content is not None:
            result['content'] = self.content

        if self.entity_key is not None:
            result['entityKey'] = self.entity_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')

        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')

        if m.get('contactor') is not None:
            self.contactor = m.get('contactor')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('entityKey') is not None:
            self.entity_key = m.get('entityKey')

        return self

