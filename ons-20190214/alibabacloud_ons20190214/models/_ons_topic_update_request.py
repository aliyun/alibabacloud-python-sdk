# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OnsTopicUpdateRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        perm: int = None,
        topic: str = None,
    ):
        # The ID of the instance to which the topic belongs.
        self.instance_id = instance_id
        # The read/write mode that you want to configure for the topic. Valid values:
        # 
        # *   **6**: Both read and write operations are allowed.
        # *   **4**: Write operations are forbidden.
        # *   **2**: Read operations are forbidden.
        # 
        # This parameter is required.
        self.perm = perm
        # The name of the topic that you want to manage.
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

        if self.perm is not None:
            result['Perm'] = self.perm

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Perm') is not None:
            self.perm = m.get('Perm')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

