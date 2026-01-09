# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_umeng_finplus20220913 import models as main_models
from darabonba.model import DaraModel

class SaveCrowdDatasetAndBindingDatasetRequest(DaraModel):
    def __init__(
        self,
        body: main_models.SaveCrowdDatasetAndBindingDatasetRequestBody = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.SaveCrowdDatasetAndBindingDatasetRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class SaveCrowdDatasetAndBindingDatasetRequestBody(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        dataset_ids: List[str] = None,
        description: str = None,
        name: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        # This parameter is required.
        self.dataset_ids = dataset_ids
        self.description = description
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.dataset_ids is not None:
            result['datasetIds'] = self.dataset_ids

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('datasetIds') is not None:
            self.dataset_ids = m.get('datasetIds')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

