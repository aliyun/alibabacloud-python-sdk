# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteEdgeContainerAppImageSecretRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        name: str = None,
    ):
        # Application ID, which can be obtained using the [ListEdgeContainerApps](~~ListEdgeContainerApps~~) API.
        # 
        # This parameter is required.
        self.app_id = app_id
        # Name of the image secret.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

