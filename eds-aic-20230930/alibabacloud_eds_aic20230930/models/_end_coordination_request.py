# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EndCoordinationRequest(DaraModel):
    def __init__(
        self,
        coordinator_user_id: str = None,
        instance_id: str = None,
        owner_user_id: str = None,
    ):
        self.coordinator_user_id = coordinator_user_id
        self.instance_id = instance_id
        self.owner_user_id = owner_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.coordinator_user_id is not None:
            result['CoordinatorUserId'] = self.coordinator_user_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoordinatorUserId') is not None:
            self.coordinator_user_id = m.get('CoordinatorUserId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        return self

