# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class GetStoreViewResponseBody(DaraModel):
    def __init__(
        self,
        store_type: str = None,
        stores: List[main_models.StoreViewStore] = None,
    ):
        # The type of the dataset.
        # 
        # Valid values:
        # 
        # *   metricstore
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   logstore
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.store_type = store_type
        # The Logstores or Metricstores.
        self.stores = stores

    def validate(self):
        if self.stores:
            for v1 in self.stores:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.store_type is not None:
            result['storeType'] = self.store_type

        result['stores'] = []
        if self.stores is not None:
            for k1 in self.stores:
                result['stores'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')

        self.stores = []
        if m.get('stores') is not None:
            for k1 in m.get('stores'):
                temp_model = main_models.StoreViewStore()
                self.stores.append(temp_model.from_map(k1))

        return self

