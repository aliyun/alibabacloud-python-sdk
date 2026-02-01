# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateFuncSwitchRecordShrinkRequest(DaraModel):
    def __init__(
        self,
        channel: str = None,
        params_shrink: str = None,
        service_name: str = None,
    ):
        # This parameter is required.
        self.channel = channel
        # This parameter is required.
        self.params_shrink = params_shrink
        # This parameter is required.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.channel is not None:
            result['channel'] = self.channel

        if self.params_shrink is not None:
            result['params'] = self.params_shrink

        if self.service_name is not None:
            result['service_name'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')

        if m.get('params') is not None:
            self.params_shrink = m.get('params')

        if m.get('service_name') is not None:
            self.service_name = m.get('service_name')

        return self

