# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai20240521 import models as main_models
from darabonba.model import DaraModel

class ListDataCacheServicesResponseBody(DaraModel):
    def __init__(
        self,
        cache_services: List[main_models.CacheService] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.cache_services = cache_services
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.cache_services:
            for v1 in self.cache_services:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CacheServices'] = []
        if self.cache_services is not None:
            for k1 in self.cache_services:
                result['CacheServices'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cache_services = []
        if m.get('CacheServices') is not None:
            for k1 in m.get('CacheServices'):
                temp_model = main_models.CacheService()
                self.cache_services.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

