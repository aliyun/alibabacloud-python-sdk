# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateChatSessionRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        license: str = None,
        platform: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.license = license
        self.platform = platform

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.license is not None:
            result['license'] = self.license

        if self.platform is not None:
            result['platform'] = self.platform

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('license') is not None:
            self.license = m.get('license')

        if m.get('platform') is not None:
            self.platform = m.get('platform')

        return self

