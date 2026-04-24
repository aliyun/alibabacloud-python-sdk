# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteApiKeyRequest(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        instance_id: str = None,
    ):
        # Api Key
        # 
        # This parameter is required.
        self.api_key = api_key
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

