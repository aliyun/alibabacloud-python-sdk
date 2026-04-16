# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class CostQueryModelsDTO(DaraModel):
    def __init__(
        self,
        columns: List[main_models.MetricDefRespDTO] = None,
        id_field: str = None,
        name_field: str = None,
        rows: List[main_models.ModelRowDTO] = None,
    ):
        self.columns = columns
        self.id_field = id_field
        self.name_field = name_field
        self.rows = rows

    def validate(self):
        if self.columns:
            for v1 in self.columns:
                 if v1:
                    v1.validate()
        if self.rows:
            for v1 in self.rows:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['columns'] = []
        if self.columns is not None:
            for k1 in self.columns:
                result['columns'].append(k1.to_map() if k1 else None)

        if self.id_field is not None:
            result['idField'] = self.id_field

        if self.name_field is not None:
            result['nameField'] = self.name_field

        result['rows'] = []
        if self.rows is not None:
            for k1 in self.rows:
                result['rows'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.columns = []
        if m.get('columns') is not None:
            for k1 in m.get('columns'):
                temp_model = main_models.MetricDefRespDTO()
                self.columns.append(temp_model.from_map(k1))

        if m.get('idField') is not None:
            self.id_field = m.get('idField')

        if m.get('nameField') is not None:
            self.name_field = m.get('nameField')

        self.rows = []
        if m.get('rows') is not None:
            for k1 in m.get('rows'):
                temp_model = main_models.ModelRowDTO()
                self.rows.append(temp_model.from_map(k1))

        return self

