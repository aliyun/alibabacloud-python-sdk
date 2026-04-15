# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLlmAccessProfileShrinkRequest(DaraModel):
    def __init__(
        self,
        access_profile_id: str = None,
        instance_id: str = None,
        profile_shrink: str = None,
    ):
        self.access_profile_id = access_profile_id
        self.instance_id = instance_id
        self.profile_shrink = profile_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_profile_id is not None:
            result['AccessProfileId'] = self.access_profile_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.profile_shrink is not None:
            result['Profile'] = self.profile_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessProfileId') is not None:
            self.access_profile_id = m.get('AccessProfileId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Profile') is not None:
            self.profile_shrink = m.get('Profile')

        return self

