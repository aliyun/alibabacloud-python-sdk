# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEdgeContainerTerminalRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        # The application ID. You can call the [ListEdgeContainerApps](~~ListEdgeContainerApps~~) operation to obtain the application ID.
        # <notice>This parameter is required. If this parameter is not specified, the API returns InvalidParameter.appid(400).
        # Full dependency chain: CreateEdgeContainerApp → CreateEdgeContainerAppVersion → PublishEdgeContainerAppVersion → Wait for the container status to become Running → Call this API.</notice>.
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

