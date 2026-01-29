# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QueryPriceEntityListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryPriceEntityListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The data that is returned.
        self.data = data
        # The message that is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryPriceEntityListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryPriceEntityListResponseBodyData(DaraModel):
    def __init__(
        self,
        price_entity_info_list: List[main_models.QueryPriceEntityListResponseBodyDataPriceEntityInfoList] = None,
    ):
        # The information about the billable items.
        self.price_entity_info_list = price_entity_info_list

    def validate(self):
        if self.price_entity_info_list:
            for v1 in self.price_entity_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PriceEntityInfoList'] = []
        if self.price_entity_info_list is not None:
            for k1 in self.price_entity_info_list:
                result['PriceEntityInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.price_entity_info_list = []
        if m.get('PriceEntityInfoList') is not None:
            for k1 in m.get('PriceEntityInfoList'):
                temp_model = main_models.QueryPriceEntityListResponseBodyDataPriceEntityInfoList()
                self.price_entity_info_list.append(temp_model.from_map(k1))

        return self

class QueryPriceEntityListResponseBodyDataPriceEntityInfoList(DaraModel):
    def __init__(
        self,
        price_entity_code: str = None,
        price_entity_name: str = None,
        price_factor_list: List[main_models.QueryPriceEntityListResponseBodyDataPriceEntityInfoListPriceFactorList] = None,
    ):
        # The code of the billable item.
        self.price_entity_code = price_entity_code
        # The name of the billable item.
        self.price_entity_name = price_entity_name
        # The factors of the billable item.
        self.price_factor_list = price_factor_list

    def validate(self):
        if self.price_factor_list:
            for v1 in self.price_factor_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.price_entity_code is not None:
            result['PriceEntityCode'] = self.price_entity_code

        if self.price_entity_name is not None:
            result['PriceEntityName'] = self.price_entity_name

        result['PriceFactorList'] = []
        if self.price_factor_list is not None:
            for k1 in self.price_factor_list:
                result['PriceFactorList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PriceEntityCode') is not None:
            self.price_entity_code = m.get('PriceEntityCode')

        if m.get('PriceEntityName') is not None:
            self.price_entity_name = m.get('PriceEntityName')

        self.price_factor_list = []
        if m.get('PriceFactorList') is not None:
            for k1 in m.get('PriceFactorList'):
                temp_model = main_models.QueryPriceEntityListResponseBodyDataPriceEntityInfoListPriceFactorList()
                self.price_factor_list.append(temp_model.from_map(k1))

        return self

class QueryPriceEntityListResponseBodyDataPriceEntityInfoListPriceFactorList(DaraModel):
    def __init__(
        self,
        price_factor_code: str = None,
        price_factor_name: str = None,
        price_factor_value_list: List[str] = None,
    ):
        # The code of the factor.
        self.price_factor_code = price_factor_code
        # The name of the factor.
        self.price_factor_name = price_factor_name
        # The values of the factor.
        self.price_factor_value_list = price_factor_value_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.price_factor_code is not None:
            result['PriceFactorCode'] = self.price_factor_code

        if self.price_factor_name is not None:
            result['PriceFactorName'] = self.price_factor_name

        if self.price_factor_value_list is not None:
            result['PriceFactorValueList'] = self.price_factor_value_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PriceFactorCode') is not None:
            self.price_factor_code = m.get('PriceFactorCode')

        if m.get('PriceFactorName') is not None:
            self.price_factor_name = m.get('PriceFactorName')

        if m.get('PriceFactorValueList') is not None:
            self.price_factor_value_list = m.get('PriceFactorValueList')

        return self

