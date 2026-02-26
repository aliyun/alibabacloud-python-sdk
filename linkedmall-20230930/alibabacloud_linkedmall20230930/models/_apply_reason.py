# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ApplyReason(DaraModel):
    def __init__(
        self,
        reason_text_id: int = None,
        reason_tips: str = None,
    ):
        self.reason_text_id = reason_text_id
        self.reason_tips = reason_tips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reason_text_id is not None:
            result['reasonTextId'] = self.reason_text_id

        if self.reason_tips is not None:
            result['reasonTips'] = self.reason_tips

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('reasonTextId') is not None:
            self.reason_text_id = m.get('reasonTextId')

        if m.get('reasonTips') is not None:
            self.reason_tips = m.get('reasonTips')

        return self

