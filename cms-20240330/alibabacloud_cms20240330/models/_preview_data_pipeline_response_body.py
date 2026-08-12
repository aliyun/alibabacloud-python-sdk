# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class PreviewDataPipelineResponseBody(DaraModel):
    def __init__(
        self,
        datasets: List[main_models.PreviewDataPipelineResponseBodyDatasets] = None,
        effective_script: str = None,
        request_id: str = None,
    ):
        # The dataset preview results.
        self.datasets = datasets
        # The effective SPL.
        self.effective_script = effective_script
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.datasets:
            for v1 in self.datasets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['datasets'] = []
        if self.datasets is not None:
            for k1 in self.datasets:
                result['datasets'].append(k1.to_map() if k1 else None)

        if self.effective_script is not None:
            result['effectiveScript'] = self.effective_script

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.datasets = []
        if m.get('datasets') is not None:
            for k1 in m.get('datasets'):
                temp_model = main_models.PreviewDataPipelineResponseBodyDatasets()
                self.datasets.append(temp_model.from_map(k1))

        if m.get('effectiveScript') is not None:
            self.effective_script = m.get('effectiveScript')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class PreviewDataPipelineResponseBodyDatasets(DaraModel):
    def __init__(
        self,
        data: List[Dict[str, Any]] = None,
        meta: List[main_models.PreviewDataPipelineResponseBodyDatasetsMeta] = None,
        name: str = None,
        sample_count: int = None,
    ):
        # The preview data.
        self.data = data
        # The field metadata.
        self.meta = meta
        # The dataset name.
        self.name = name
        # The number of samples.
        self.sample_count = sample_count

    def validate(self):
        if self.meta:
            for v1 in self.meta:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data

        result['meta'] = []
        if self.meta is not None:
            for k1 in self.meta:
                result['meta'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.sample_count is not None:
            result['sampleCount'] = self.sample_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')

        self.meta = []
        if m.get('meta') is not None:
            for k1 in m.get('meta'):
                temp_model = main_models.PreviewDataPipelineResponseBodyDatasetsMeta()
                self.meta.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('sampleCount') is not None:
            self.sample_count = m.get('sampleCount')

        return self

class PreviewDataPipelineResponseBodyDatasetsMeta(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The field name.
        self.name = name
        # The field type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

