# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class MLDataParam(DaraModel):
    def __init__(
        self,
        annotationdata_id: str = None,
        annotations: Dict[str, main_models.MLDataParamAnnotationsValue] = None,
        config: Dict[str, str] = None,
        create_time: int = None,
        data_hash: str = None,
        dataset_id: str = None,
        last_modify_time: int = None,
        predictions: Dict[str, main_models.MLDataParamPredictionsValue] = None,
        value: str = None,
        value_type: str = None,
    ):
        self.annotationdata_id = annotationdata_id
        self.annotations = annotations
        self.config = config
        self.create_time = create_time
        self.data_hash = data_hash
        self.dataset_id = dataset_id
        self.last_modify_time = last_modify_time
        self.predictions = predictions
        self.value = value
        self.value_type = value_type

    def validate(self):
        if self.annotations:
            for v1 in self.annotations.values():
                 if v1:
                    v1.validate()
        if self.predictions:
            for v1 in self.predictions.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotationdata_id is not None:
            result['annotationdataId'] = self.annotationdata_id

        result['annotations'] = {}
        if self.annotations is not None:
            for k1, v1 in self.annotations.items():
                result['annotations'][k1] = v1.to_map() if v1 else None

        if self.config is not None:
            result['config'] = self.config

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.data_hash is not None:
            result['dataHash'] = self.data_hash

        if self.dataset_id is not None:
            result['datasetId'] = self.dataset_id

        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time

        result['predictions'] = {}
        if self.predictions is not None:
            for k1, v1 in self.predictions.items():
                result['predictions'][k1] = v1.to_map() if v1 else None

        if self.value is not None:
            result['value'] = self.value

        if self.value_type is not None:
            result['valueType'] = self.value_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotationdataId') is not None:
            self.annotationdata_id = m.get('annotationdataId')

        self.annotations = {}
        if m.get('annotations') is not None:
            for k1, v1 in m.get('annotations').items():
                temp_model = main_models.MLDataParamAnnotationsValue()
                self.annotations[k1] = temp_model.from_map(v1)

        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('dataHash') is not None:
            self.data_hash = m.get('dataHash')

        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')

        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')

        self.predictions = {}
        if m.get('predictions') is not None:
            for k1, v1 in m.get('predictions').items():
                temp_model = main_models.MLDataParamPredictionsValue()
                self.predictions[k1] = temp_model.from_map(v1)

        if m.get('value') is not None:
            self.value = m.get('value')

        if m.get('valueType') is not None:
            self.value_type = m.get('valueType')

        return self

