# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcecenter20221201 import models as main_models
from darabonba.model import DaraModel

class ListFiltersResponseBody(DaraModel):
    def __init__(
        self,
        default_filter_name: str = None,
        filters: List[main_models.ListFiltersResponseBodyFilters] = None,
        request_id: str = None,
    ):
        self.default_filter_name = default_filter_name
        self.filters = filters
        self.request_id = request_id

    def validate(self):
        if self.filters:
            for v1 in self.filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_filter_name is not None:
            result['DefaultFilterName'] = self.default_filter_name

        result['Filters'] = []
        if self.filters is not None:
            for k1 in self.filters:
                result['Filters'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultFilterName') is not None:
            self.default_filter_name = m.get('DefaultFilterName')

        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.ListFiltersResponseBodyFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListFiltersResponseBodyFilters(DaraModel):
    def __init__(
        self,
        filter_configuration: str = None,
        filter_name: str = None,
    ):
        # This parameter is required.
        self.filter_configuration = filter_configuration
        self.filter_name = filter_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_configuration is not None:
            result['FilterConfiguration'] = self.filter_configuration

        if self.filter_name is not None:
            result['FilterName'] = self.filter_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterConfiguration') is not None:
            self.filter_configuration = m.get('FilterConfiguration')

        if m.get('FilterName') is not None:
            self.filter_name = m.get('FilterName')

        return self

