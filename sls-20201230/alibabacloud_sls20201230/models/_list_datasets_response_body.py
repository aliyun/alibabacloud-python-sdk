# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class ListDatasetsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        datasets: List[main_models.ListDatasetsResponseBodyDatasets] = None,
        total: int = None,
    ):
        self.count = count
        self.datasets = datasets
        self.total = total

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
        if self.count is not None:
            result['count'] = self.count

        result['datasets'] = []
        if self.datasets is not None:
            for k1 in self.datasets:
                result['datasets'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        self.datasets = []
        if m.get('datasets') is not None:
            for k1 in m.get('datasets'):
                temp_model = main_models.ListDatasetsResponseBodyDatasets()
                self.datasets.append(temp_model.from_map(k1))

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListDatasetsResponseBodyDatasets(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        name: str = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.description = description
        self.name = name
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

