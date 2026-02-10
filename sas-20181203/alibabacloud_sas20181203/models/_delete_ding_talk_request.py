# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDingTalkRequest(DaraModel):
    def __init__(
        self,
        ids: str = None,
    ):
        # The ID of the notification from the DingTalk chatbot. Separate multiple IDs with commas (,).
        # 
        # >  You can call the [DescribeDingTalk](~~DescribeDingTalk~~) operation to query the ID.
        # 
        # This parameter is required.
        self.ids = ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ids is not None:
            result['Ids'] = self.ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        return self

