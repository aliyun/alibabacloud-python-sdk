# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCommonCateSecondFloorRequest(DaraModel):
    def __init__(
        self,
        parent_cate_id: int = None,
    ):
        # Parent category ID
        self.parent_cate_id = parent_cate_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parent_cate_id is not None:
            result['ParentCateId'] = self.parent_cate_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParentCateId') is not None:
            self.parent_cate_id = m.get('ParentCateId')

        return self

