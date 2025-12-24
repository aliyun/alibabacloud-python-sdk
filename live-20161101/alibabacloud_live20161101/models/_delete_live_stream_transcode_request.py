# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLiveStreamTranscodeRequest(DaraModel):
    def __init__(
        self,
        app: str = None,
        domain: str = None,
        owner_id: int = None,
        security_token: str = None,
        template: str = None,
    ):
        # The name of the application to which the live stream belongs.
        # 
        # This parameter is required.
        self.app = app
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain = domain
        self.owner_id = owner_id
        self.security_token = security_token
        # The transcoding template ID. Valid values:
        # 
        # *   Standard transcoding:
        # 
        #     *   lld: low definition
        #     *   lsd: standard definition
        #     *   lhd: high definition
        #     *   lud : ultra-high definition
        # 
        # *   Narrowband HD™ transcoding:
        # 
        #     *   ld: low definition
        #     *   sd: standard definition
        #     *   hd: high definition
        #     *   ud: ultra-high definition
        # 
        # *   Custom transcoding: a custom ID
        # 
        # This parameter is required.
        self.template = template

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

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.template is not None:
            result['Template'] = self.template

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        return self

