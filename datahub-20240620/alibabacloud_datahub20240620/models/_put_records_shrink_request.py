# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PutRecordsShrinkRequest(DaraModel):
    def __init__(
        self,
        project_name: str = None,
        records_shrink: str = None,
        shard_id: str = None,
        topic_name: str = None,
    ):
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.records_shrink = records_shrink
        self.shard_id = shard_id
        # This parameter is required.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.records_shrink is not None:
            result['Records'] = self.records_shrink

        if self.shard_id is not None:
            result['ShardId'] = self.shard_id

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Records') is not None:
            self.records_shrink = m.get('Records')

        if m.get('ShardId') is not None:
            self.shard_id = m.get('ShardId')

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        return self

