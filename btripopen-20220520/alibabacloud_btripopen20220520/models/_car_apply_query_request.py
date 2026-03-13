# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CarApplyQueryRequest(DaraModel):
    def __init__(
        self,
        created_end_at: str = None,
        created_start_at: str = None,
        page_number: int = None,
        page_size: int = None,
        third_part_apply_id: str = None,
        user_id: str = None,
    ):
        self.created_end_at = created_end_at
        self.created_start_at = created_start_at
        self.page_number = page_number
        self.page_size = page_size
        self.third_part_apply_id = third_part_apply_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_end_at is not None:
            result['created_end_at'] = self.created_end_at

        if self.created_start_at is not None:
            result['created_start_at'] = self.created_start_at

        if self.page_number is not None:
            result['page_number'] = self.page_number

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.third_part_apply_id is not None:
            result['third_part_apply_id'] = self.third_part_apply_id

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_end_at') is not None:
            self.created_end_at = m.get('created_end_at')

        if m.get('created_start_at') is not None:
            self.created_start_at = m.get('created_start_at')

        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('third_part_apply_id') is not None:
            self.third_part_apply_id = m.get('third_part_apply_id')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

