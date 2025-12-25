# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEdgeContainerAppStatusRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        publish_env: str = None,
    ):
        # The application ID, which can be obtained by calling the [ListEdgeContainerApps](~~ListEdgeContainerApps~~) operation.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The release environment. Valid values: prod and staging.
        self.publish_env = publish_env

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.publish_env is not None:
            result['PublishEnv'] = self.publish_env

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('PublishEnv') is not None:
            self.publish_env = m.get('PublishEnv')

        return self

