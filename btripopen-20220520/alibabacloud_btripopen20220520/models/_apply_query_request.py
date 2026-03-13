# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplyQueryRequest(DaraModel):
    def __init__(
        self,
        apply_id: int = None,
        apply_show_id: str = None,
        sub_corp_id: str = None,
        thirdpart_apply_id: str = None,
        type: int = None,
    ):
        self.apply_id = apply_id
        self.apply_show_id = apply_show_id
        self.sub_corp_id = sub_corp_id
        self.thirdpart_apply_id = thirdpart_apply_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_id is not None:
            result['apply_id'] = self.apply_id

        if self.apply_show_id is not None:
            result['apply_show_id'] = self.apply_show_id

        if self.sub_corp_id is not None:
            result['sub_corp_id'] = self.sub_corp_id

        if self.thirdpart_apply_id is not None:
            result['thirdpart_apply_id'] = self.thirdpart_apply_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apply_id') is not None:
            self.apply_id = m.get('apply_id')

        if m.get('apply_show_id') is not None:
            self.apply_show_id = m.get('apply_show_id')

        if m.get('sub_corp_id') is not None:
            self.sub_corp_id = m.get('sub_corp_id')

        if m.get('thirdpart_apply_id') is not None:
            self.thirdpart_apply_id = m.get('thirdpart_apply_id')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

