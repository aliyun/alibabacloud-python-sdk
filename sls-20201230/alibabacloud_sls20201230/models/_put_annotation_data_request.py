# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class PutAnnotationDataRequest(DaraModel):
    def __init__(
        self,
        annotationdata_id: str = None,
        ml_data_param: main_models.MLDataParam = None,
        raw_log: List[Dict[str, str]] = None,
    ):
        # The unique identifier of the data.
        self.annotationdata_id = annotationdata_id
        # The data structure of the request.
        self.ml_data_param = ml_data_param
        # The raw log data.
        self.raw_log = raw_log

    def validate(self):
        if self.ml_data_param:
            self.ml_data_param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotationdata_id is not None:
            result['annotationdataId'] = self.annotationdata_id

        if self.ml_data_param is not None:
            result['mlDataParam'] = self.ml_data_param.to_map()

        if self.raw_log is not None:
            result['rawLog'] = self.raw_log

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotationdataId') is not None:
            self.annotationdata_id = m.get('annotationdataId')

        if m.get('mlDataParam') is not None:
            temp_model = main_models.MLDataParam()
            self.ml_data_param = temp_model.from_map(m.get('mlDataParam'))

        if m.get('rawLog') is not None:
            self.raw_log = m.get('rawLog')

        return self

