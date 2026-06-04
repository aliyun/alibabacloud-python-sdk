# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveAppRequirementRequest(DaraModel):
    def __init__(
        self,
        conversation_id: str = None,
        prd: str = None,
    ):
        self.conversation_id = conversation_id
        self.prd = prd

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.prd is not None:
            result['Prd'] = self.prd

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('Prd') is not None:
            self.prd = m.get('Prd')

        return self

