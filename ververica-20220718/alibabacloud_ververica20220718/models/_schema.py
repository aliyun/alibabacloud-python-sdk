# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class Schema(DaraModel):
    def __init__(
        self,
        columns: List[main_models.TableColumn] = None,
        primary_key: main_models.PrimaryKey = None,
        watermark_specs: List[main_models.WatermarkSpec] = None,
    ):
        # The information about columns.
        self.columns = columns
        # The information about the primary key.
        self.primary_key = primary_key
        # The watermark information.
        self.watermark_specs = watermark_specs

    def validate(self):
        if self.columns:
            for v1 in self.columns:
                 if v1:
                    v1.validate()
        if self.primary_key:
            self.primary_key.validate()
        if self.watermark_specs:
            for v1 in self.watermark_specs:
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

        if self.primary_key is not None:
            result['primaryKey'] = self.primary_key.to_map()

        result['watermarkSpecs'] = []
        if self.watermark_specs is not None:
            for k1 in self.watermark_specs:
                result['watermarkSpecs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.columns = []
        if m.get('columns') is not None:
            for k1 in m.get('columns'):
                temp_model = main_models.TableColumn()
                self.columns.append(temp_model.from_map(k1))

        if m.get('primaryKey') is not None:
            temp_model = main_models.PrimaryKey()
            self.primary_key = temp_model.from_map(m.get('primaryKey'))

        self.watermark_specs = []
        if m.get('watermarkSpecs') is not None:
            for k1 in m.get('watermarkSpecs'):
                temp_model = main_models.WatermarkSpec()
                self.watermark_specs.append(temp_model.from_map(k1))

        return self

