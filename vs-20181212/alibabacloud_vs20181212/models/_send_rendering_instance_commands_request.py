# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendRenderingInstanceCommandsRequest(DaraModel):
    def __init__(
        self,
        commands: str = None,
        mode: str = None,
        rendering_instance_id: str = None,
        timeout: int = None,
    ):
        # This parameter is required.
        self.commands = commands
        self.mode = mode
        # This parameter is required.
        self.rendering_instance_id = rendering_instance_id
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commands is not None:
            result['Commands'] = self.commands

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commands') is not None:
            self.commands = m.get('Commands')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

