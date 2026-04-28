# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class JWTPayload(DaraModel):
    def __init__(
        self,
        aud: str = None,
        auto_create: bool = None,
        exp: int = None,
        iat: int = None,
        iss: str = None,
        jti: str = None,
        nbf: int = None,
        sub: str = None,
        sub_type: str = None,
    ):
        self.aud = aud
        self.auto_create = auto_create
        self.exp = exp
        self.iat = iat
        self.iss = iss
        self.jti = jti
        self.nbf = nbf
        self.sub = sub
        self.sub_type = sub_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aud is not None:
            result['aud'] = self.aud

        if self.auto_create is not None:
            result['auto_create'] = self.auto_create

        if self.exp is not None:
            result['exp'] = self.exp

        if self.iat is not None:
            result['iat'] = self.iat

        if self.iss is not None:
            result['iss'] = self.iss

        if self.jti is not None:
            result['jti'] = self.jti

        if self.nbf is not None:
            result['nbf'] = self.nbf

        if self.sub is not None:
            result['sub'] = self.sub

        if self.sub_type is not None:
            result['sub_type'] = self.sub_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aud') is not None:
            self.aud = m.get('aud')

        if m.get('auto_create') is not None:
            self.auto_create = m.get('auto_create')

        if m.get('exp') is not None:
            self.exp = m.get('exp')

        if m.get('iat') is not None:
            self.iat = m.get('iat')

        if m.get('iss') is not None:
            self.iss = m.get('iss')

        if m.get('jti') is not None:
            self.jti = m.get('jti')

        if m.get('nbf') is not None:
            self.nbf = m.get('nbf')

        if m.get('sub') is not None:
            self.sub = m.get('sub')

        if m.get('sub_type') is not None:
            self.sub_type = m.get('sub_type')

        return self

