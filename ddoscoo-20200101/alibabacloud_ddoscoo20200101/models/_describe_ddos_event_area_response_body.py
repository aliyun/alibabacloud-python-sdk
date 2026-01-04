# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDDosEventAreaResponseBody(DaraModel):
    def __init__(
        self,
        areas: List[main_models.DescribeDDosEventAreaResponseBodyAreas] = None,
        request_id: str = None,
    ):
        # The information about the source region from which the volumetric attack was initiated.
        self.areas = areas
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.areas:
            for v1 in self.areas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Areas'] = []
        if self.areas is not None:
            for k1 in self.areas:
                result['Areas'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.areas = []
        if m.get('Areas') is not None:
            for k1 in m.get('Areas'):
                temp_model = main_models.DescribeDDosEventAreaResponseBodyAreas()
                self.areas.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDDosEventAreaResponseBodyAreas(DaraModel):
    def __init__(
        self,
        area: str = None,
        in_pkts: int = None,
    ):
        # The code or ID of the source region. For more information, see [Codes of administrative regions in China and codes of countries and areas](https://help.aliyun.com/document_detail/167926.html). For example, **110000** indicates Beijing, China, and **us** indicates the United States.
        self.area = area
        # The number of request packets that were sent from the source region.
        self.in_pkts = in_pkts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['Area'] = self.area

        if self.in_pkts is not None:
            result['InPkts'] = self.in_pkts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')

        if m.get('InPkts') is not None:
            self.in_pkts = m.get('InPkts')

        return self

