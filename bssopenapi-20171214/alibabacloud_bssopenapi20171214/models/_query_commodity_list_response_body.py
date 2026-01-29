# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QueryCommodityListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryCommodityListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the information about the service was queried.
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
            temp_model = main_models.QueryCommodityListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryCommodityListResponseBodyData(DaraModel):
    def __init__(
        self,
        commodity_list: List[main_models.QueryCommodityListResponseBodyDataCommodityList] = None,
    ):
        # The information about the service.
        self.commodity_list = commodity_list

    def validate(self):
        if self.commodity_list:
            for v1 in self.commodity_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CommodityList'] = []
        if self.commodity_list is not None:
            for k1 in self.commodity_list:
                result['CommodityList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.commodity_list = []
        if m.get('CommodityList') is not None:
            for k1 in m.get('CommodityList'):
                temp_model = main_models.QueryCommodityListResponseBodyDataCommodityList()
                self.commodity_list.append(temp_model.from_map(k1))

        return self

class QueryCommodityListResponseBodyDataCommodityList(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        commodity_code: str = None,
        commodity_name: str = None,
    ):
        # The payment type. Valid values: POSTPAY (pay-as-you-go) and PREPAY (subscription).
        self.charge_type = charge_type
        # The code of the service, which is the same as that on the Billing Management page.
        self.commodity_code = commodity_code
        # The name of the service.
        self.commodity_name = commodity_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.commodity_name is not None:
            result['CommodityName'] = self.commodity_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CommodityName') is not None:
            self.commodity_name = m.get('CommodityName')

        return self

