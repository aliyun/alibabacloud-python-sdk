# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CostCenterQueryRequest(DaraModel):
    def __init__(
        self,
        disable: int = None,
        need_org_entity: bool = None,
        thirdpart_id: str = None,
        title: str = None,
        user_id: str = None,
    ):
        self.disable = disable
        self.need_org_entity = need_org_entity
        self.thirdpart_id = thirdpart_id
        self.title = title
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disable is not None:
            result['disable'] = self.disable

        if self.need_org_entity is not None:
            result['need_org_entity'] = self.need_org_entity

        if self.thirdpart_id is not None:
            result['thirdpart_id'] = self.thirdpart_id

        if self.title is not None:
            result['title'] = self.title

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disable') is not None:
            self.disable = m.get('disable')

        if m.get('need_org_entity') is not None:
            self.need_org_entity = m.get('need_org_entity')

        if m.get('thirdpart_id') is not None:
            self.thirdpart_id = m.get('thirdpart_id')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

