# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeEssdCacheConfigResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeEssdCacheConfigResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeEssdCacheConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEssdCacheConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        enable_essd_cache: bool = None,
        essd_cache_size: int = None,
    ):
        # Specifies whether to enable the disk cache feature.
        # 
        # Valid values:
        # 
        # *   true
        # *   false
        self.enable_essd_cache = enable_essd_cache
        # The disk cache size. Unit: GB.
        self.essd_cache_size = essd_cache_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_essd_cache is not None:
            result['EnableEssdCache'] = self.enable_essd_cache

        if self.essd_cache_size is not None:
            result['EssdCacheSize'] = self.essd_cache_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableEssdCache') is not None:
            self.enable_essd_cache = m.get('EnableEssdCache')

        if m.get('EssdCacheSize') is not None:
            self.essd_cache_size = m.get('EssdCacheSize')

        return self

