# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class ListTrainingJobOutputModelsResponseBody(DaraModel):
    def __init__(
        self,
        output_models: List[main_models.ListTrainingJobOutputModelsResponseBodyOutputModels] = None,
    ):
        self.output_models = output_models

    def validate(self):
        if self.output_models:
            for v1 in self.output_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OutputModels'] = []
        if self.output_models is not None:
            for k1 in self.output_models:
                result['OutputModels'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.output_models = []
        if m.get('OutputModels') is not None:
            for k1 in m.get('OutputModels'):
                temp_model = main_models.ListTrainingJobOutputModelsResponseBodyOutputModels()
                self.output_models.append(temp_model.from_map(k1))

        return self

class ListTrainingJobOutputModelsResponseBodyOutputModels(DaraModel):
    def __init__(
        self,
        compression_spec: Dict[str, Any] = None,
        evaluation_spec: Dict[str, Any] = None,
        inference_spec: Dict[str, Any] = None,
        labels: List[main_models.ListTrainingJobOutputModelsResponseBodyOutputModelsLabels] = None,
        metrics: Dict[str, Any] = None,
        output_channel_name: str = None,
        source_id: str = None,
        source_type: str = None,
        training_spec: Dict[str, Any] = None,
        uri: str = None,
    ):
        self.compression_spec = compression_spec
        self.evaluation_spec = evaluation_spec
        self.inference_spec = inference_spec
        self.labels = labels
        self.metrics = metrics
        self.output_channel_name = output_channel_name
        self.source_id = source_id
        self.source_type = source_type
        self.training_spec = training_spec
        self.uri = uri

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compression_spec is not None:
            result['CompressionSpec'] = self.compression_spec

        if self.evaluation_spec is not None:
            result['EvaluationSpec'] = self.evaluation_spec

        if self.inference_spec is not None:
            result['InferenceSpec'] = self.inference_spec

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.metrics is not None:
            result['Metrics'] = self.metrics

        if self.output_channel_name is not None:
            result['OutputChannelName'] = self.output_channel_name

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.training_spec is not None:
            result['TrainingSpec'] = self.training_spec

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompressionSpec') is not None:
            self.compression_spec = m.get('CompressionSpec')

        if m.get('EvaluationSpec') is not None:
            self.evaluation_spec = m.get('EvaluationSpec')

        if m.get('InferenceSpec') is not None:
            self.inference_spec = m.get('InferenceSpec')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.ListTrainingJobOutputModelsResponseBodyOutputModelsLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')

        if m.get('OutputChannelName') is not None:
            self.output_channel_name = m.get('OutputChannelName')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('TrainingSpec') is not None:
            self.training_spec = m.get('TrainingSpec')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

class ListTrainingJobOutputModelsResponseBodyOutputModelsLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

