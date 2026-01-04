# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeEnsCommodityCodeResponseBody(DaraModel):
    def __init__(
        self,
        commodity_code_info: List[main_models.DescribeEnsCommodityCodeResponseBodyCommodityCodeInfo] = None,
        request_id: str = None,
    ):
        self.commodity_code_info = commodity_code_info
        self.request_id = request_id

    def validate(self):
        if self.commodity_code_info:
            for v1 in self.commodity_code_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CommodityCodeInfo'] = []
        if self.commodity_code_info is not None:
            for k1 in self.commodity_code_info:
                result['CommodityCodeInfo'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.commodity_code_info = []
        if m.get('CommodityCodeInfo') is not None:
            for k1 in m.get('CommodityCodeInfo'):
                temp_model = main_models.DescribeEnsCommodityCodeResponseBodyCommodityCodeInfo()
                self.commodity_code_info.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEnsCommodityCodeResponseBodyCommodityCodeInfo(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        commodity_name: str = None,
    ):
        self.commodity_code = commodity_code
        self.commodity_name = commodity_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.commodity_name is not None:
            result['CommodityName'] = self.commodity_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CommodityName') is not None:
            self.commodity_name = m.get('CommodityName')

        return self

