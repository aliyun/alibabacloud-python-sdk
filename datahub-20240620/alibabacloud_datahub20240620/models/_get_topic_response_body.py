# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTopicResponseBody(DaraModel):
    def __init__(
        self,
        comment: str = None,
        create_time: str = None,
        creator: str = None,
        enable_schema_registry: bool = None,
        expand_mode: bool = None,
        lifecycle: int = None,
        project_name: str = None,
        record_schema: str = None,
        record_type: str = None,
        request_id: str = None,
        shard_count: int = None,
        storage: int = None,
        success: bool = None,
        topic_name: str = None,
        update_time: str = None,
    ):
        self.comment = comment
        self.create_time = create_time
        self.creator = creator
        self.enable_schema_registry = enable_schema_registry
        self.expand_mode = expand_mode
        self.lifecycle = lifecycle
        self.project_name = project_name
        self.record_schema = record_schema
        self.record_type = record_type
        self.request_id = request_id
        self.shard_count = shard_count
        self.storage = storage
        self.success = success
        self.topic_name = topic_name
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.enable_schema_registry is not None:
            result['EnableSchemaRegistry'] = self.enable_schema_registry

        if self.expand_mode is not None:
            result['ExpandMode'] = self.expand_mode

        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.record_schema is not None:
            result['RecordSchema'] = self.record_schema

        if self.record_type is not None:
            result['RecordType'] = self.record_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count

        if self.storage is not None:
            result['Storage'] = self.storage

        if self.success is not None:
            result['Success'] = self.success

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('EnableSchemaRegistry') is not None:
            self.enable_schema_registry = m.get('EnableSchemaRegistry')

        if m.get('ExpandMode') is not None:
            self.expand_mode = m.get('ExpandMode')

        if m.get('Lifecycle') is not None:
            self.lifecycle = m.get('Lifecycle')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RecordSchema') is not None:
            self.record_schema = m.get('RecordSchema')

        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')

        if m.get('Storage') is not None:
            self.storage = m.get('Storage')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

