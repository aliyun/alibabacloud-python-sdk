# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TranslateChannelDraftRequest(DaraModel):
    def __init__(
        self,
        draft_id: str = None,
    ):
        # The ID of the channel draft.
        # 
        # This parameter is required.
        self.draft_id = draft_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.draft_id is not None:
            result['DraftId'] = self.draft_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DraftId') is not None:
            self.draft_id = m.get('DraftId')

        return self

