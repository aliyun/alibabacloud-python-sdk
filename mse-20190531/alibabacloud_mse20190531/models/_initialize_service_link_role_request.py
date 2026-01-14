# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InitializeServiceLinkRoleRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        role_name: str = None,
        token: str = None,
    ):
        self.accept_language = accept_language
        self.role_name = role_name
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        if self.token is not None:
            result['Token'] = self.token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        return self

