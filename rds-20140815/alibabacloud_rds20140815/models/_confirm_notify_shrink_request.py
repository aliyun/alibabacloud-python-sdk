# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfirmNotifyShrinkRequest(DaraModel):
    def __init__(
        self,
        confirmor: int = None,
        notify_id_list_shrink: str = None,
    ):
        # The ID of the Alibaba Cloud account that is used to confirm the notification. You can set this parameter to **0**, which indicates that the notification is confirmed by the system.
        # 
        # This parameter is required.
        self.confirmor = confirmor
        # The notification IDs.
        # 
        # This parameter is required.
        self.notify_id_list_shrink = notify_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confirmor is not None:
            result['Confirmor'] = self.confirmor

        if self.notify_id_list_shrink is not None:
            result['NotifyIdList'] = self.notify_id_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confirmor') is not None:
            self.confirmor = m.get('Confirmor')

        if m.get('NotifyIdList') is not None:
            self.notify_id_list_shrink = m.get('NotifyIdList')

        return self

