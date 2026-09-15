# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class E2BTemplateTag(DaraModel):
    def __init__(
        self,
        build_id: str = None,
        created_at: str = None,
        tag: str = None,
    ):
        self.build_id = build_id
        self.created_at = created_at
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_id is not None:
            result['buildID'] = self.build_id

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.tag is not None:
            result['tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('buildID') is not None:
            self.build_id = m.get('buildID')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('tag') is not None:
            self.tag = m.get('tag')

        return self

