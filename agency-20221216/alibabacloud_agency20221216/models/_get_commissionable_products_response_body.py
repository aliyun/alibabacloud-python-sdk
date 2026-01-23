# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agency20221216 import models as main_models
from darabonba.model import DaraModel

class GetCommissionableProductsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetCommissionableProductsResponseBodyData] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.code = code
        self.data = data
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total = total

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
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetCommissionableProductsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetCommissionableProductsResponseBodyData(DaraModel):
    def __init__(
        self,
        actual_start_month: str = None,
        commodity_code: str = None,
        commodity_name: str = None,
        eligible_for_commission: str = None,
        eligible_for_discount: str = None,
        end_month: str = None,
        product_campaign: str = None,
        product_code: str = None,
        product_name: str = None,
        seven_core_products: str = None,
        status: str = None,
    ):
        self.actual_start_month = actual_start_month
        self.commodity_code = commodity_code
        self.commodity_name = commodity_name
        self.eligible_for_commission = eligible_for_commission
        self.eligible_for_discount = eligible_for_discount
        self.end_month = end_month
        self.product_campaign = product_campaign
        self.product_code = product_code
        self.product_name = product_name
        self.seven_core_products = seven_core_products
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_start_month is not None:
            result['ActualStartMonth'] = self.actual_start_month

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.commodity_name is not None:
            result['CommodityName'] = self.commodity_name

        if self.eligible_for_commission is not None:
            result['EligibleForCommission'] = self.eligible_for_commission

        if self.eligible_for_discount is not None:
            result['EligibleForDiscount'] = self.eligible_for_discount

        if self.end_month is not None:
            result['EndMonth'] = self.end_month

        if self.product_campaign is not None:
            result['ProductCampaign'] = self.product_campaign

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_name is not None:
            result['ProductName'] = self.product_name

        if self.seven_core_products is not None:
            result['SevenCoreProducts'] = self.seven_core_products

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualStartMonth') is not None:
            self.actual_start_month = m.get('ActualStartMonth')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CommodityName') is not None:
            self.commodity_name = m.get('CommodityName')

        if m.get('EligibleForCommission') is not None:
            self.eligible_for_commission = m.get('EligibleForCommission')

        if m.get('EligibleForDiscount') is not None:
            self.eligible_for_discount = m.get('EligibleForDiscount')

        if m.get('EndMonth') is not None:
            self.end_month = m.get('EndMonth')

        if m.get('ProductCampaign') is not None:
            self.product_campaign = m.get('ProductCampaign')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')

        if m.get('SevenCoreProducts') is not None:
            self.seven_core_products = m.get('SevenCoreProducts')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

