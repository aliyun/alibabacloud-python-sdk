# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGroupRequest(DaraModel):
    def __init__(
        self,
        app: str = None,
        callback: str = None,
        description: str = None,
        in_protocol: str = None,
        lazy_pull: bool = None,
        name: str = None,
        out_protocol: str = None,
        owner_id: int = None,
        play_domain: str = None,
        push_domain: str = None,
        region: str = None,
    ):
        self.app = app
        self.callback = callback
        self.description = description
        # This parameter is required.
        self.in_protocol = in_protocol
        self.lazy_pull = lazy_pull
        # This parameter is required.
        self.name = name
        self.out_protocol = out_protocol
        self.owner_id = owner_id
        self.play_domain = play_domain
        self.push_domain = push_domain
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app is not None:
            result['App'] = self.app

        if self.callback is not None:
            result['Callback'] = self.callback

        if self.description is not None:
            result['Description'] = self.description

        if self.in_protocol is not None:
            result['InProtocol'] = self.in_protocol

        if self.lazy_pull is not None:
            result['LazyPull'] = self.lazy_pull

        if self.name is not None:
            result['Name'] = self.name

        if self.out_protocol is not None:
            result['OutProtocol'] = self.out_protocol

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.play_domain is not None:
            result['PlayDomain'] = self.play_domain

        if self.push_domain is not None:
            result['PushDomain'] = self.push_domain

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')

        if m.get('Callback') is not None:
            self.callback = m.get('Callback')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InProtocol') is not None:
            self.in_protocol = m.get('InProtocol')

        if m.get('LazyPull') is not None:
            self.lazy_pull = m.get('LazyPull')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OutProtocol') is not None:
            self.out_protocol = m.get('OutProtocol')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PlayDomain') is not None:
            self.play_domain = m.get('PlayDomain')

        if m.get('PushDomain') is not None:
            self.push_domain = m.get('PushDomain')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

