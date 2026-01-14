# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DataValue(DaraModel):
    def __init__(
        self,
        user_id: str = None,
        region_id: str = None,
        namespace: str = None,
        app_name: str = None,
        app_id: str = None,
    ):
        # The ID of the user to which the application belongs.
        self.user_id = user_id
        # The region where the application resides.
        self.region_id = region_id
        # The microservice namespace where the application resides.
        self.namespace = namespace
        # The application name.
        self.app_name = app_name
        # The application ID.
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_id is not None:
            result['AppId'] = self.app_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        return self

