# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateEventsAttentionRequest(DaraModel):
    def __init__(
        self,
        x_debug_id: str = None,
        mode: int = None,
        range: str = None,
        uuid: str = None,
        x_sysom_invoke_source: str = None,
    ):
        self.x_debug_id = x_debug_id
        # The sensitivity of the anomaly event. Valid values: -1 to 3. A value of -1 indicates that the sensitivity is decreased by 1. A value of 0 indicates that the sensitivity is increased by 1.
        self.mode = mode
        # The scope in which the update takes effect. Valid values: cluster and node.
        self.range = range
        # The UUID of the anomaly event.
        # 
        # This parameter is required.
        self.uuid = uuid
        self.x_sysom_invoke_source = x_sysom_invoke_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_debug_id is not None:
            result['X-Debug-Id'] = self.x_debug_id

        if self.mode is not None:
            result['mode'] = self.mode

        if self.range is not None:
            result['range'] = self.range

        if self.uuid is not None:
            result['uuid'] = self.uuid

        if self.x_sysom_invoke_source is not None:
            result['x-sysom-invoke-source'] = self.x_sysom_invoke_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Debug-Id') is not None:
            self.x_debug_id = m.get('X-Debug-Id')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('range') is not None:
            self.range = m.get('range')

        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')

        if m.get('x-sysom-invoke-source') is not None:
            self.x_sysom_invoke_source = m.get('x-sysom-invoke-source')

        return self

