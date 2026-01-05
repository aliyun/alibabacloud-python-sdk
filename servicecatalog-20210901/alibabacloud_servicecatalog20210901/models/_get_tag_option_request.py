# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTagOptionRequest(DaraModel):
    def __init__(
        self,
        tag_option_id: str = None,
    ):
        # The ID of the tag option.
        # 
        # This parameter is required.
        self.tag_option_id = tag_option_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_option_id is not None:
            result['TagOptionId'] = self.tag_option_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagOptionId') is not None:
            self.tag_option_id = m.get('TagOptionId')

        return self

