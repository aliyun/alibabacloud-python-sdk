# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteWildcardByTopicRequest(DaraModel):
    def __init__(
        self,
        first_topic: str = None,
        instance_id: str = None,
        wildcards: str = None,
    ):
        # The first-level topic.
        # 
        # This parameter is required.
        self.first_topic = first_topic
        # The ID of the instance to which the group ID that you want to delete belongs.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The wildcard subscriptions to delete.
        # 
        # This parameter is required.
        self.wildcards = wildcards

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.first_topic is not None:
            result['FirstTopic'] = self.first_topic

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.wildcards is not None:
            result['Wildcards'] = self.wildcards

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirstTopic') is not None:
            self.first_topic = m.get('FirstTopic')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Wildcards') is not None:
            self.wildcards = m.get('Wildcards')

        return self

