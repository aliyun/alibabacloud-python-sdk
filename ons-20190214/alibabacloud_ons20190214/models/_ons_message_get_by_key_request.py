# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OnsMessageGetByKeyRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        key: str = None,
        topic: str = None,
    ):
        # The ID of the instance to which the messages that you want to query belong.
        self.instance_id = instance_id
        # The key of the messages that you want to query.
        # 
        # This parameter is required.
        self.key = key
        # The topic that contains the messages that you want to query.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.key is not None:
            result['Key'] = self.key

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

