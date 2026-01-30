# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartPublishStreamRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_id: int = None,
        publish_url: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_id = owner_id
        # This parameter is required.
        self.publish_url = publish_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.publish_url is not None:
            result['PublishUrl'] = self.publish_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PublishUrl') is not None:
            self.publish_url = m.get('PublishUrl')

        return self

