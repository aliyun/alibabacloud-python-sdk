# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class CostModelDetailRespDTO(DaraModel):
    def __init__(
        self,
        columns: List[main_models.MetricDefRespDTO] = None,
        granularity: str = None,
        model_id: int = None,
        model_name: str = None,
        page: int = None,
        page_size: int = None,
        rows: List[main_models.CostModelDetailRowDTO] = None,
        total: int = None,
    ):
        self.columns = columns
        self.granularity = granularity
        self.model_id = model_id
        self.model_name = model_name
        self.page = page
        self.page_size = page_size
        self.rows = rows
        self.total = total

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

        if self.granularity is not None:
            result['granularity'] = self.granularity

        if self.model_id is not None:
            result['modelId'] = self.model_id

        if self.model_name is not None:
            result['modelName'] = self.model_name

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        result['rows'] = []
        if self.rows is not None:
            for k1 in self.rows:
                result['rows'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.columns = []
        if m.get('columns') is not None:
            for k1 in m.get('columns'):
                temp_model = main_models.MetricDefRespDTO()
                self.columns.append(temp_model.from_map(k1))

        if m.get('granularity') is not None:
            self.granularity = m.get('granularity')

        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')

        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        self.rows = []
        if m.get('rows') is not None:
            for k1 in m.get('rows'):
                temp_model = main_models.CostModelDetailRowDTO()
                self.rows.append(temp_model.from_map(k1))

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

