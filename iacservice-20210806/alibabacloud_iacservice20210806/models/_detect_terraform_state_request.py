# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DetectTerraformStateRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        identifier: str = None,
        type: str = None,
    ):
        # The idempotence token. Format: [0-9a-zA-Z-]{1,64}. Use a UUID.
        # 
        # This parameter is required.
        self.client_token = client_token
        # The task identifier. For a Stack task, the format is <$stackId>:<$deploymentName>. For a Task task, the format is <$TaskId>.
        # 
        # This parameter is required.
        self.identifier = identifier
        # The task type. Valid values:
        # - Stack
        # - Task.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.identifier is not None:
            result['identifier'] = self.identifier

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

