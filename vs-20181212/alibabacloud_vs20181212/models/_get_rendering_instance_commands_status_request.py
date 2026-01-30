# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRenderingInstanceCommandsStatusRequest(DaraModel):
    def __init__(
        self,
        cmd_id: str = None,
        rendering_instance_id: str = None,
    ):
        # This parameter is required.
        self.cmd_id = cmd_id
        # This parameter is required.
        self.rendering_instance_id = rendering_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cmd_id is not None:
            result['CmdId'] = self.cmd_id

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CmdId') is not None:
            self.cmd_id = m.get('CmdId')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        return self

