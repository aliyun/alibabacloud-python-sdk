# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RewriteChannelTitleRequest(DaraModel):
    def __init__(
        self,
        draft_id: str = None,
        user_requirement: str = None,
    ):
        # The channel draft ID.
        # 
        # This parameter is required.
        self.draft_id = draft_id
        # The user personalization requirement in free text format. This parameter is optional.
        self.user_requirement = user_requirement

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.draft_id is not None:
            result['DraftId'] = self.draft_id

        if self.user_requirement is not None:
            result['UserRequirement'] = self.user_requirement

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DraftId') is not None:
            self.draft_id = m.get('DraftId')

        if m.get('UserRequirement') is not None:
            self.user_requirement = m.get('UserRequirement')

        return self

