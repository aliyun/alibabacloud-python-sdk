# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class GetEpdSummaryResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetEpdSummaryResponseBodyData] = None,
        request_id: str = None,
    ):
        # Response parameters
        self.data = data
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.GetEpdSummaryResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetEpdSummaryResponseBodyData(DaraModel):
    def __init__(
        self,
        carbon_emission: float = None,
        indicator: str = None,
        key: str = None,
        method: str = None,
        name: str = None,
        num: int = None,
        pre_unit: str = None,
        state: int = None,
    ):
        # Emissions. The result is maintained up to 31 decimal places for precise intermediate calculation and subsequently truncated for display. It is advised to pair the emissions figure with the unit of the environmental impact result for a comprehensive understanding.
        self.carbon_emission = carbon_emission
        # The evaluation index adopted for the environmental impact
        self.indicator = indicator
        # The category key. The environmental impact category. Currently, a maximum of 19 categories are supported. Enumeration refers to [Carbon Footprint Appendices](https://carbon-doc.oss-cn-hangzhou.aliyuncs.com/CarbonFootprintAppendices-en.pdf).
        self.key = key
        # Calculation method standard
        self.method = method
        # The name of the category.
        self.name = name
        # Category num: the unique serial number of the environmental impact category. A maximum of 19 categories are supported. Enumeration refers to [Carbon Footprint Appendices](https://carbon-doc.oss-cn-hangzhou.aliyuncs.com/CarbonFootprintAppendices-en.pdf).
        self.num = num
        # Environmental impact result Value Unit.
        self.pre_unit = pre_unit
        # The data status. 1 indicates that the calculation is accurate, 2 indicates that the default data is used, and 3 indicates that the missing factor uses the value of 0.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.carbon_emission is not None:
            result['carbonEmission'] = self.carbon_emission

        if self.indicator is not None:
            result['indicator'] = self.indicator

        if self.key is not None:
            result['key'] = self.key

        if self.method is not None:
            result['method'] = self.method

        if self.name is not None:
            result['name'] = self.name

        if self.num is not None:
            result['num'] = self.num

        if self.pre_unit is not None:
            result['preUnit'] = self.pre_unit

        if self.state is not None:
            result['state'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmission') is not None:
            self.carbon_emission = m.get('carbonEmission')

        if m.get('indicator') is not None:
            self.indicator = m.get('indicator')

        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('method') is not None:
            self.method = m.get('method')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('num') is not None:
            self.num = m.get('num')

        if m.get('preUnit') is not None:
            self.pre_unit = m.get('preUnit')

        if m.get('state') is not None:
            self.state = m.get('state')

        return self

