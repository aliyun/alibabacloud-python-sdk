# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RenameApiKeyRequest(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        instance_id: str = None,
        key_name: str = None,
    ):
        # API KEY
        # 
        # This parameter is required.
        self.api_key = api_key
        self.instance_id = instance_id
        # This parameter is required.
        self.key_name = key_name

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

        if self.key_name is not None:
            result['KeyName'] = self.key_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')

        return self

