# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateRenderingInstanceResponseBody(DaraModel):
    def __init__(
        self,
        rendering_instance_id: str = None,
        rendering_instance_ids: List[str] = None,
        request_id: str = None,
    ):
        # The instance ID of the cloud application service.
        self.rendering_instance_id = rendering_instance_id
        # The instance ID list of the cloud application service.
        self.rendering_instance_ids = rendering_instance_ids
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rendering_instance_id is not None:
            result['RenderingInstanceId'] = self.rendering_instance_id

        if self.rendering_instance_ids is not None:
            result['RenderingInstanceIds'] = self.rendering_instance_ids

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RenderingInstanceId') is not None:
            self.rendering_instance_id = m.get('RenderingInstanceId')

        if m.get('RenderingInstanceIds') is not None:
            self.rendering_instance_ids = m.get('RenderingInstanceIds')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

