# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLiveDelayConfigRequest(DaraModel):
    def __init__(
        self,
        app: str = None,
        domain: str = None,
        owner_id: int = None,
        region_id: str = None,
        stream: str = None,
    ):
        # The name of the application to which the live stream belongs. You can specify an asterisk (\\*) as the value to match all applications that belong to the domain name.
        # 
        # This parameter is required.
        self.app = app
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain = domain
        self.owner_id = owner_id
        self.region_id = region_id
        # The name of the live stream. You can use the wildcard (\\*) to specify all streams of the application.
        # 
        # This parameter is required.
        self.stream = stream

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app is not None:
            result['App'] = self.app

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stream is not None:
            result['Stream'] = self.stream

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        return self

