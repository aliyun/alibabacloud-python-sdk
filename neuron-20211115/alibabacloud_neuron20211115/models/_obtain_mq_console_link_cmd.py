# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ObtainMqConsoleLinkCmd(DaraModel):
    def __init__(
        self,
        env: str = None,
        group_type: str = None,
        mq_group_id: str = None,
        pbc_id: int = None,
        service_name: str = None,
        topic_name: str = None,
    ):
        self.env = env
        self.group_type = group_type
        self.mq_group_id = mq_group_id
        self.pbc_id = pbc_id
        self.service_name = service_name
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env is not None:
            result['env'] = self.env

        if self.group_type is not None:
            result['groupType'] = self.group_type

        if self.mq_group_id is not None:
            result['mqGroupId'] = self.mq_group_id

        if self.pbc_id is not None:
            result['pbcId'] = self.pbc_id

        if self.service_name is not None:
            result['serviceName'] = self.service_name

        if self.topic_name is not None:
            result['topicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('groupType') is not None:
            self.group_type = m.get('groupType')

        if m.get('mqGroupId') is not None:
            self.mq_group_id = m.get('mqGroupId')

        if m.get('pbcId') is not None:
            self.pbc_id = m.get('pbcId')

        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')

        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')

        return self

