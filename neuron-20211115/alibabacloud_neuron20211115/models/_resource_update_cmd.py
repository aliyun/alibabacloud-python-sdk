# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResourceUpdateCmd(DaraModel):
    def __init__(
        self,
        address: str = None,
        configuration: str = None,
        credentials: str = None,
        description: str = None,
        id: int = None,
        namespace: str = None,
        use_scope: str = None,
        use_type: str = None,
    ):
        self.address = address
        self.configuration = configuration
        self.credentials = credentials
        self.description = description
        self.id = id
        self.namespace = namespace
        self.use_scope = use_scope
        self.use_type = use_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address

        if self.configuration is not None:
            result['configuration'] = self.configuration

        if self.credentials is not None:
            result['credentials'] = self.credentials

        if self.description is not None:
            result['description'] = self.description

        if self.id is not None:
            result['id'] = self.id

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.use_scope is not None:
            result['useScope'] = self.use_scope

        if self.use_type is not None:
            result['useType'] = self.use_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('configuration') is not None:
            self.configuration = m.get('configuration')

        if m.get('credentials') is not None:
            self.credentials = m.get('credentials')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('useScope') is not None:
            self.use_scope = m.get('useScope')

        if m.get('useType') is not None:
            self.use_type = m.get('useType')

        return self

