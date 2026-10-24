# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSimilarEventScenariosRequest(DaraModel):
    def __init__(
        self,
        security_event_id: int = None,
    ):
        # The ID of the alert event.
        # > You can call the [DescribeSuspEvents](~~DescribeSuspEvents~~) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.security_event_id = security_event_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_event_id is not None:
            result['SecurityEventId'] = self.security_event_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityEventId') is not None:
            self.security_event_id = m.get('SecurityEventId')

        return self

