# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTopicRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        enable_schema_registry: bool = None,
        expand_mode: bool = None,
        lifecycle: int = None,
        project_name: str = None,
        record_schema: str = None,
        record_type: str = None,
        shard_count: int = None,
        topic_name: str = None,
    ):
        # The description of the topic.
        # 
        # This parameter is required.
        self.comment = comment
        # Specifies whether to enable multi-version schema. After this feature is enabled, a topic can have multiple schemas. You can select one of the schemas for writing. The consumer automatically parses each record based on the version tag. If the schema for the corresponding version has been deleted, parsing fails.
        # 
        # > Enabling multi-version schema has the following impacts:
        # 1. You can no longer use the appendFields operation.
        #  2. You can create, delete, modify, and query schemas.
        #  3. Connectors are created by using the schema of the latest version.
        self.enable_schema_registry = enable_schema_registry
        # The expansion mode of the topic. After the expansion mode is enabled, shards support horizontal scaling and no longer support merge or split operations. The number of shards can only increase and cannot decrease. After this mode is enabled, you can consume the current topic by using Kafka.
        self.expand_mode = expand_mode
        # The lifecycle of the topic. Unit: days.
        # 
        # This parameter is required.
        self.lifecycle = lifecycle
        # The project name.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The schema table structure.
        self.record_schema = record_schema
        # The topic type. Valid values:
        # 
        # 1. Blob: supports writing a block of binary data as a single record.
        # 
        # 1. Tuple: supports database-like records where each record contains multiple columns. You must specify RecordSchema because data is transmitted over the network as strings and requires a schema to convert the data into the corresponding types.
        # 
        # This parameter is required.
        self.record_type = record_type
        # The number of shards.
        # 
        # This parameter is required.
        self.shard_count = shard_count
        # The topic name.
        # 
        # This parameter is required.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

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

        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

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

        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        return self

