# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainViewSourceProvincesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        source_provinces: List[main_models.DescribeDomainViewSourceProvincesResponseBodySourceProvinces] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # An array consisting of the details of the administrative region in China from which the requests are sent.
        self.source_provinces = source_provinces

    def validate(self):
        if self.source_provinces:
            for v1 in self.source_provinces:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SourceProvinces'] = []
        if self.source_provinces is not None:
            for k1 in self.source_provinces:
                result['SourceProvinces'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.source_provinces = []
        if m.get('SourceProvinces') is not None:
            for k1 in m.get('SourceProvinces'):
                temp_model = main_models.DescribeDomainViewSourceProvincesResponseBodySourceProvinces()
                self.source_provinces.append(temp_model.from_map(k1))

        return self

class DescribeDomainViewSourceProvincesResponseBodySourceProvinces(DaraModel):
    def __init__(
        self,
        count: int = None,
        province_id: str = None,
    ):
        # The total number of requests.
        self.count = count
        # The ID of the region inside China. For more information, see the **Codes of administrative regions in China** section of the [Codes of administrative regions in China and codes of countries and areas](https://help.aliyun.com/document_detail/167926.html) topic. For example, **110000** indicates Beijing, and **120000** indicates Tianjin.
        self.province_id = province_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.province_id is not None:
            result['ProvinceId'] = self.province_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('ProvinceId') is not None:
            self.province_id = m.get('ProvinceId')

        return self

