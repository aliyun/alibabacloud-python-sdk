# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OnsConsumerAccumulateRequest(DaraModel):
    def __init__(
        self,
        detail: bool = None,
        group_id: str = None,
        instance_id: str = None,
    ):
        # Specifies whether to query the details of each topic to which the consumer group subscribes. Valid values:
        # 
        # *   **true**: The details of each topic are queried. You can obtain the details from the **DetailInTopicList** response parameter.
        # *   **false**: The details of each topic are not queried. This is the default value. If you use this value, the value of the **DetailInTopicList** response parameter is empty.
        self.detail = detail
        # The ID of the consumer group.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the instance.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail is not None:
            result['Detail'] = self.detail

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

