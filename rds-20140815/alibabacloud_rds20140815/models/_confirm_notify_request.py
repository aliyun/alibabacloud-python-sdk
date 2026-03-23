# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ConfirmNotifyRequest(DaraModel):
    def __init__(
        self,
        confirmor: int = None,
        notify_id_list: List[int] = None,
    ):
        # This parameter is required.
        self.confirmor = confirmor
        # This parameter is required.
        self.notify_id_list = notify_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confirmor is not None:
            result['Confirmor'] = self.confirmor

        if self.notify_id_list is not None:
            result['NotifyIdList'] = self.notify_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confirmor') is not None:
            self.confirmor = m.get('Confirmor')

        if m.get('NotifyIdList') is not None:
            self.notify_id_list = m.get('NotifyIdList')

        return self

