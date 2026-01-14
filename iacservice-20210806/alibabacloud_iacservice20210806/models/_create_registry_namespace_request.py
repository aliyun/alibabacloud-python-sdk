# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRegistryNamespaceRequest(DaraModel):
    def __init__(
        self,
        acl: str = None,
        client_token: str = None,
        description: str = None,
        maintainer: str = None,
        namespace_name: str = None,
    ):
        self.acl = acl
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        self.maintainer = maintainer
        # This parameter is required.
        self.namespace_name = namespace_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl is not None:
            result['acl'] = self.acl

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.description is not None:
            result['description'] = self.description

        if self.maintainer is not None:
            result['maintainer'] = self.maintainer

        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('maintainer') is not None:
            self.maintainer = m.get('maintainer')

        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')

        return self

