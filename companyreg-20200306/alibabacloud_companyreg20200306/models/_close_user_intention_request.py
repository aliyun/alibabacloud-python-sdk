# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloseUserIntentionRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        intention_biz_id: str = None,
        note: str = None,
    ):
        self.biz_type = biz_type
        # This parameter is required.
        self.intention_biz_id = intention_biz_id
        # This parameter is required.
        self.note = note

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.intention_biz_id is not None:
            result['IntentionBizId'] = self.intention_biz_id

        if self.note is not None:
            result['Note'] = self.note

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('IntentionBizId') is not None:
            self.intention_biz_id = m.get('IntentionBizId')

        if m.get('Note') is not None:
            self.note = m.get('Note')

        return self

