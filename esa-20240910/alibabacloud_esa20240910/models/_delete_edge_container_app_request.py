# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteEdgeContainerAppRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        # The application ID. You can call the [ListEdgeContainerApps](~~ListEdgeContainerApps~~) operation to obtain the application ID. 
        # <notice>AppId is required. If this parameter is not specified, the API returns InvalidParameter.appid (400). You can obtain the value by calling ListEdgeContainerApps.
        # The AppId value is in the format of the app- prefix followed by 18 or more digits (at least 20 characters in total). You can obtain the actual value from the AppId field in the ListEdgeContainerApps response.</notice>.
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

