# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchEventRedeployInstanceShrinkRequest(DaraModel):
    def __init__(
        self,
        event_infos_shrink: str = None,
    ):
        # List of events.
        self.event_infos_shrink = event_infos_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_infos_shrink is not None:
            result['EventInfos'] = self.event_infos_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventInfos') is not None:
            self.event_infos_shrink = m.get('EventInfos')

        return self

