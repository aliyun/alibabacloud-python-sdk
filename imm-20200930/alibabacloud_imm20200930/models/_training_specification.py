# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class TrainingSpecification(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        endpoint: str = None,
        model_specification: main_models.ModelSpecification = None,
        runtime: main_models.Runtime = None,
        source_uri: str = None,
        target_uri: str = None,
        transforms: List[main_models.CustomParams] = None,
        validation_source_uri: str = None,
        validation_split: float = None,
    ):
        # Name of the dataset
        self.dataset_name = dataset_name
        # The endpoint of the storage where the dataset is stored.
        # 
        # This parameter is required.
        self.endpoint = endpoint
        # The model specification details.
        # 
        # This parameter is required.
        self.model_specification = model_specification
        # The information about the runtime for model training.
        # 
        # This parameter is required.
        self.runtime = runtime
        # URI of the dataset
        # 
        # This parameter is required.
        self.source_uri = source_uri
        # The storage path to the model data. Only an Object Storage Service (OSS) path is supported.
        # 
        # This parameter is required.
        self.target_uri = target_uri
        # Local preprocessing parameters for the dataset.
        self.transforms = transforms
        # The URI of the evaluation dataset. You must specify this parameter or the ValidationSplit parameter.
        self.validation_source_uri = validation_source_uri
        # The ratio for splitting the training dataset into the evaluation dataset. You must specify this parameter or the ValidationSourceURI parameter.
        self.validation_split = validation_split

    def validate(self):
        if self.model_specification:
            self.model_specification.validate()
        if self.runtime:
            self.runtime.validate()
        if self.transforms:
            for v1 in self.transforms:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.model_specification is not None:
            result['ModelSpecification'] = self.model_specification.to_map()

        if self.runtime is not None:
            result['Runtime'] = self.runtime.to_map()

        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri

        if self.target_uri is not None:
            result['TargetURI'] = self.target_uri

        result['Transforms'] = []
        if self.transforms is not None:
            for k1 in self.transforms:
                result['Transforms'].append(k1.to_map() if k1 else None)

        if self.validation_source_uri is not None:
            result['ValidationSourceURI'] = self.validation_source_uri

        if self.validation_split is not None:
            result['ValidationSplit'] = self.validation_split

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('ModelSpecification') is not None:
            temp_model = main_models.ModelSpecification()
            self.model_specification = temp_model.from_map(m.get('ModelSpecification'))

        if m.get('Runtime') is not None:
            temp_model = main_models.Runtime()
            self.runtime = temp_model.from_map(m.get('Runtime'))

        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')

        if m.get('TargetURI') is not None:
            self.target_uri = m.get('TargetURI')

        self.transforms = []
        if m.get('Transforms') is not None:
            for k1 in m.get('Transforms'):
                temp_model = main_models.CustomParams()
                self.transforms.append(temp_model.from_map(k1))

        if m.get('ValidationSourceURI') is not None:
            self.validation_source_uri = m.get('ValidationSourceURI')

        if m.get('ValidationSplit') is not None:
            self.validation_split = m.get('ValidationSplit')

        return self

