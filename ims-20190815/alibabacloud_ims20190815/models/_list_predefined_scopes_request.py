# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPredefinedScopesRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
    ):
        # The type of the application. Valid values:
        # 
        # - WebApp
        # 
        # - NativeApp
        # 
        # - ServerApp
        # 
        # If this parameter is empty, the permissions on all types of applications are queried.
        self.app_type = app_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        return self

