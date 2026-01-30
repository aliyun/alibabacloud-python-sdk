# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RefreshRenderingInstanceStreamingShrinkRequest(DaraModel):
    def __init__(
        self,
        client_info_shrink: str = None,
        rendering_instance_id: str = None,
    ):
        self.client_info_shrink = client_info_shrink
        # This parameter is required.
        self.rendering_instance_id = rendering_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_info_shrink is not None:
            result['ClientInfo'] = self.client_info_shrink

        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientInfo') is not None:
            self.client_info_shrink = m.get('ClientInfo')

        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        return self

