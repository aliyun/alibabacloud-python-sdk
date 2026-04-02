# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class CreateDatasetRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        description: str = None,
        schema: Dict[str, main_models.IndexKey] = None,
    ):
        # This parameter is required.
        self.dataset_name = dataset_name
        self.description = description
        # This parameter is required.
        self.schema = schema

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
        if self.dataset_name is not None:
            result['datasetName'] = self.dataset_name

        if self.description is not None:
            result['description'] = self.description

        result['schema'] = {}
        if self.schema is not None:
            for k1, v1 in self.schema.items():
                result['schema'][k1] = v1.to_map() if v1 else None

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('datasetName') is not None:
            self.dataset_name = m.get('datasetName')

        if m.get('description') is not None:
            self.description = m.get('description')

        self.schema = {}
        if m.get('schema') is not None:
            for k1, v1 in m.get('schema').items():
                temp_model = main_models.IndexKey()
                self.schema[k1] = temp_model.from_map(v1)

        return self

