# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSchemaResponseBody(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        creator: str = None,
        project_name: str = None,
        record_schema: str = None,
        request_id: str = None,
        success: bool = None,
        topic_name: str = None,
        version_id: int = None,
    ):
        self.create_time = create_time
        self.creator = creator
        self.project_name = project_name
        self.record_schema = record_schema
        self.request_id = request_id
        self.success = success
        self.topic_name = topic_name
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.record_schema is not None:
            result['RecordSchema'] = self.record_schema

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RecordSchema') is not None:
            self.record_schema = m.get('RecordSchema')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

