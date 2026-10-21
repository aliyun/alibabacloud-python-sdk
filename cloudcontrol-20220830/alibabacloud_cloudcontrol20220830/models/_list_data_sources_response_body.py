# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudcontrol20220830 import models as main_models
from darabonba.model import DaraModel

class ListDataSourcesResponseBody(DaraModel):
    def __init__(
        self,
        data_sources: List[main_models.ListDataSourcesResponseBodyDataSources] = None,
        request_id: str = None,
    ):
        # The list of data.
        self.data_sources = data_sources
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data_sources:
            for v1 in self.data_sources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['dataSources'] = []
        if self.data_sources is not None:
            for k1 in self.data_sources:
                result['dataSources'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_sources = []
        if m.get('dataSources') is not None:
            for k1 in m.get('dataSources'):
                temp_model = main_models.ListDataSourcesResponseBodyDataSources()
                self.data_sources.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListDataSourcesResponseBodyDataSources(DaraModel):
    def __init__(
        self,
        id: str = None,
    ):
        # The data ID.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        return self

