# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTrafficMirrorSessionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resource_group_id: str = None,
        traffic_mirror_session_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group to which the mirrored traffic belongs.
        self.resource_group_id = resource_group_id
        # The ID of the traffic mirror session.
        self.traffic_mirror_session_id = traffic_mirror_session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.traffic_mirror_session_id is not None:
            result['TrafficMirrorSessionId'] = self.traffic_mirror_session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('TrafficMirrorSessionId') is not None:
            self.traffic_mirror_session_id = m.get('TrafficMirrorSessionId')

        return self

