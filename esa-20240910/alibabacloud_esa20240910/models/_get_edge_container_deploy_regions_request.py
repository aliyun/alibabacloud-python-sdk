# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEdgeContainerDeployRegionsRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        # The application ID. You can call the [ListEdgeContainerApps](~~ListEdgeContainerApps~~) operation to obtain the application ID.>Notice: This parameter is required. If this parameter is not specified, the service returns InvalidParameter.appid (400). The valid format is app-{18-digit number}. You can call the ListEdgeContainerApps operation to obtain the application ID. Example: app-880****75783794688. If you have not activated the Edge Container service, activate it first and then call the CreateEdgeContainerApp operation to create an application and obtain the AppId.</notice>.
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

