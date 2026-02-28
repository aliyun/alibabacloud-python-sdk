# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateChatRoutingProfileRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        routing_profiles: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.routing_profiles = routing_profiles

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.routing_profiles is not None:
            result['RoutingProfiles'] = self.routing_profiles

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RoutingProfiles') is not None:
            self.routing_profiles = m.get('RoutingProfiles')

        return self

