# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_datahub20240620 import models as main_models
from darabonba.model import DaraModel

class PutRecordsRequest(DaraModel):
    def __init__(
        self,
        project_name: str = None,
        records: List[main_models.PutRecordsRequestRecords] = None,
        shard_id: str = None,
        topic_name: str = None,
    ):
        # This parameter is required.
        self.project_name = project_name
        # This parameter is required.
        self.records = records
        self.shard_id = shard_id
        # This parameter is required.
        self.topic_name = topic_name

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.shard_id is not None:
            result['ShardId'] = self.shard_id

        if self.topic_name is not None:
            result['TopicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.PutRecordsRequestRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('ShardId') is not None:
            self.shard_id = m.get('ShardId')

        if m.get('TopicName') is not None:
            self.topic_name = m.get('TopicName')

        return self

class PutRecordsRequestRecords(DaraModel):
    def __init__(
        self,
        attributes: Dict[str, str] = None,
        data: List[str] = None,
    ):
        self.attributes = attributes
        # This parameter is required.
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.data is not None:
            result['Data'] = self.data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        return self

