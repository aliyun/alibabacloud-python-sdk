# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class ModelSpecification(DaraModel):
    def __init__(
        self,
        meta_data: main_models.MetaData = None,
        spec: main_models.Spec = None,
    ):
        # The basic model information.
        # 
        # This parameter is required.
        self.meta_data = meta_data
        # The model specification information.
        # 
        # This parameter is required.
        self.spec = spec

    def validate(self):
        if self.meta_data:
            self.meta_data.validate()
        if self.spec:
            self.spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.meta_data is not None:
            result['MetaData'] = self.meta_data.to_map()

        if self.spec is not None:
            result['Spec'] = self.spec.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetaData') is not None:
            temp_model = main_models.MetaData()
            self.meta_data = temp_model.from_map(m.get('MetaData'))

        if m.get('Spec') is not None:
            temp_model = main_models.Spec()
            self.spec = temp_model.from_map(m.get('Spec'))

        return self

