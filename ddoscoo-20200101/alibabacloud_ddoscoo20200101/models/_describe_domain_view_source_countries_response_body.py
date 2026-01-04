# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDomainViewSourceCountriesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        source_countrys: List[main_models.DescribeDomainViewSourceCountriesResponseBodySourceCountrys] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # An array consisting of the country or area from which the requests are sent.
        self.source_countrys = source_countrys

    def validate(self):
        if self.source_countrys:
            for v1 in self.source_countrys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SourceCountrys'] = []
        if self.source_countrys is not None:
            for k1 in self.source_countrys:
                result['SourceCountrys'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.source_countrys = []
        if m.get('SourceCountrys') is not None:
            for k1 in m.get('SourceCountrys'):
                temp_model = main_models.DescribeDomainViewSourceCountriesResponseBodySourceCountrys()
                self.source_countrys.append(temp_model.from_map(k1))

        return self

class DescribeDomainViewSourceCountriesResponseBodySourceCountrys(DaraModel):
    def __init__(
        self,
        count: int = None,
        country_id: str = None,
    ):
        # The total number of requests.
        self.count = count
        # The abbreviation of the country or area. For more information, see the **Codes of countries and areas** section of the [Codes of administrative regions in China and codes of countries and areas](https://help.aliyun.com/document_detail/167926.html) topic. For example, **cn** indicates China, and **us** indicates the United States.
        self.country_id = country_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.country_id is not None:
            result['CountryId'] = self.country_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')

        return self

