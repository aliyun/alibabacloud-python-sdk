# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDingTalkStatusRequest(DaraModel):
    def __init__(
        self,
        ids: str = None,
        status: int = None,
    ):
        # The notification IDs of DingTalk chatbots. Separate multiple IDs with commas (,).
        # 
        # >  You can call the [DescribeDingTalk](~~DescribeDingTalk~~) operation to query the notification IDs.
        # 
        # This parameter is required.
        self.ids = ids
        # The notification status of a DingTalk chatbot. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ids is not None:
            result['Ids'] = self.ids

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

