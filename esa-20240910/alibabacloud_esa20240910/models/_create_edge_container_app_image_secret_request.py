# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEdgeContainerAppImageSecretRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        password: str = None,
        registry: str = None,
        username: str = None,
    ):
        # Application ID, which can be obtained using the [ListEdgeContainerApps](~~ListEdgeContainerApps~~) interface.
        # 
        # This parameter is required.
        self.app_id = app_id
        # Image repository password.
        # 
        # This parameter is required.
        self.password = password
        # Image repository address.
        # 
        # This parameter is required.
        self.registry = registry
        # Image repository username.
        # 
        # This parameter is required.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.password is not None:
            result['Password'] = self.password

        if self.registry is not None:
            result['Registry'] = self.registry

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Registry') is not None:
            self.registry = m.get('Registry')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

