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
        # A shell command string. Enter multiple commands separated by semicolons (;) or line feeds.
        # 
        # - Dangerous commands such as rm and reboot are disabled.
        # 
        # This parameter is required.
        self.commands = commands
        # The response pattern for the command. Valid values:
        # 
        # 1. Sync: The response is returned synchronously. This is the default value.
        # 
        # 2. Async: The response is returned asynchronously.
        self.mode = mode
        # The ID of the cloud application service instance.
        # 
        # This parameter is required.
        self.rendering_instance_id = rendering_instance_id
        # The timeout period for command execution, in seconds. The value range depends on the Mode parameter:
        # 
        # 1. If Mode is set to Sync, the value range is 0 to 30. The default value is 30.
        # 
        # 2. If Mode is set to Async, the value range is 0 to 3600. The default value is 300.
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

