# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class QuerySavingsPlansDiscountResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QuerySavingsPlansDiscountResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned.
        self.code = code
        # data
        self.data = data
        # The error message returned.
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
            temp_model = main_models.QuerySavingsPlansDiscountResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QuerySavingsPlansDiscountResponseBodyData(DaraModel):
    def __init__(
        self,
        host_id: str = None,
        items: List[main_models.QuerySavingsPlansDiscountResponseBodyDataItems] = None,
    ):
        # The IP address of the request.
        self.host_id = host_id
        # The information about the discounts on saving plans.
        self.items = items

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_id is not None:
            result['HostId'] = self.host_id

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.QuerySavingsPlansDiscountResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        return self

class QuerySavingsPlansDiscountResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        commodity_name: str = None,
        contract_discount_rate: str = None,
        cycle: str = None,
        discount_rate: str = None,
        module_name: str = None,
        pay_mode: str = None,
        region: str = None,
        region_code: str = None,
        spec: str = None,
        spn_type: str = None,
    ):
        # The details of the service.
        self.commodity_name = commodity_name
        # The contracted discount.
        self.contract_discount_rate = contract_discount_rate
        # The cycle based on which queries were performed.
        self.cycle = cycle
        # The discount provided by the official website.
        self.discount_rate = discount_rate
        # The name of the pricing module.
        self.module_name = module_name
        # The payment mode. Valid values:
        # 
        # *   total: all upfront
        # *   half: half upfront
        # *   zero: no upfront
        self.pay_mode = pay_mode
        # The ID of the region.
        self.region = region
        # The region ID of the instance. You can call the [DescribeDBInstanceAttribute](https://help.aliyun.com/document_detail/26231.html) operation to query the region ID of the instance.
        self.region_code = region_code
        # The type of the resource.
        self.spec = spec
        # The type of the savings plan.
        self.spn_type = spn_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_name is not None:
            result['CommodityName'] = self.commodity_name

        if self.contract_discount_rate is not None:
            result['ContractDiscountRate'] = self.contract_discount_rate

        if self.cycle is not None:
            result['Cycle'] = self.cycle

        if self.discount_rate is not None:
            result['DiscountRate'] = self.discount_rate

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        if self.pay_mode is not None:
            result['PayMode'] = self.pay_mode

        if self.region is not None:
            result['Region'] = self.region

        if self.region_code is not None:
            result['RegionCode'] = self.region_code

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.spn_type is not None:
            result['SpnType'] = self.spn_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityName') is not None:
            self.commodity_name = m.get('CommodityName')

        if m.get('ContractDiscountRate') is not None:
            self.contract_discount_rate = m.get('ContractDiscountRate')

        if m.get('Cycle') is not None:
            self.cycle = m.get('Cycle')

        if m.get('DiscountRate') is not None:
            self.discount_rate = m.get('DiscountRate')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        if m.get('PayMode') is not None:
            self.pay_mode = m.get('PayMode')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('SpnType') is not None:
            self.spn_type = m.get('SpnType')

        return self

