# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEdgeContainerAppResourceReserveRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        # The application ID. You can call the [ListEdgeContainerApps](~~ListEdgeContainerApps~~) operation to obtain the application ID.
        # >Notice: This parameter is required. If this parameter is not specified, the service returns InvalidParameter.Appid (400).
        # If no applications exist under your account, call CreateEdgeContainerApp to create an application first, and then call ListEdgeContainerApps to obtain the AppId.
        # </notice>.
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        return self

