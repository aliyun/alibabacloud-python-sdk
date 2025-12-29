# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetApplicationRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        namespace_id: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The application name.
        self.app_name = app_name
        # The ID of the namespace.
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        return self

