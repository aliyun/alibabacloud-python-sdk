# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InvoiceSearchRequest(DaraModel):
    def __init__(
        self,
        third_part_id: str = None,
        title: str = None,
        user_id: str = None,
    ):
        self.third_part_id = third_part_id
        self.title = title
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.third_part_id is not None:
            result['third_part_id'] = self.third_part_id

        if self.title is not None:
            result['title'] = self.title

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('third_part_id') is not None:
            self.third_part_id = m.get('third_part_id')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

