# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteRemindRequest(DaraModel):
    def __init__(
        self,
        remind_id: int = None,
    ):
        # The ID of the custom alert rule.
        # 
        # This parameter is required.
        self.remind_id = remind_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remind_id is not None:
            result['RemindId'] = self.remind_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemindId') is not None:
            self.remind_id = m.get('RemindId')

        return self

