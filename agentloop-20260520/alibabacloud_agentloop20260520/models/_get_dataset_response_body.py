# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class GetDatasetResponseBody(DaraModel):
    def __init__(
        self,
        agent_space: str = None,
        create_time: str = None,
        dataset_name: str = None,
        description: str = None,
        is_favorite: bool = None,
        labels: Dict[str, List[str]] = None,
        region_id: str = None,
        request_id: str = None,
        schema: Dict[str, main_models.IndexKey] = None,
        update_time: str = None,
    ):
        # The agent space name.
        self.agent_space = agent_space
        # The creation time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        # The dataset name.
        self.dataset_name = dataset_name
        # The dataset description.
        self.description = description
        self.is_favorite = is_favorite
        self.labels = labels
        # The region ID.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The table schema of the dataset.
        self.schema = schema
        # The update time.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.update_time = update_time

    def validate(self):
        if self.schema:
            for v1 in self.schema.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_space is not None:
            result['agentSpace'] = self.agent_space

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.dataset_name is not None:
            result['datasetName'] = self.dataset_name

        if self.description is not None:
            result['description'] = self.description

        if self.is_favorite is not None:
            result['isFavorite'] = self.is_favorite

        if self.labels is not None:
            result['labels'] = self.labels

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['schema'] = {}
        if self.schema is not None:
            for k1, v1 in self.schema.items():
                result['schema'][k1] = v1.to_map() if v1 else None

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentSpace') is not None:
            self.agent_space = m.get('agentSpace')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('datasetName') is not None:
            self.dataset_name = m.get('datasetName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('isFavorite') is not None:
            self.is_favorite = m.get('isFavorite')

        if m.get('labels') is not None:
            self.labels = m.get('labels')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.schema = {}
        if m.get('schema') is not None:
            for k1, v1 in m.get('schema').items():
                temp_model = main_models.IndexKey()
                self.schema[k1] = temp_model.from_map(v1)

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

