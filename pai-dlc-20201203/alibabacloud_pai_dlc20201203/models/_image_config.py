# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImageConfig(DaraModel):
    def __init__(
        self,
        auth: str = None,
        docker_registry: str = None,
        password: str = None,
        username: str = None,
    ):
        self.auth = auth
        self.docker_registry = docker_registry
        self.password = password
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth is not None:
            result['Auth'] = self.auth

        if self.docker_registry is not None:
            result['DockerRegistry'] = self.docker_registry

        if self.password is not None:
            result['Password'] = self.password

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auth') is not None:
            self.auth = m.get('Auth')

        if m.get('DockerRegistry') is not None:
            self.docker_registry = m.get('DockerRegistry')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

