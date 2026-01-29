# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bssopenapi20171214 import models as main_models
from darabonba.model import DaraModel

class GetPayAsYouGoPriceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetPayAsYouGoPriceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The data returned.
        self.data = data
        # The message returned.
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
            temp_model = main_models.GetPayAsYouGoPriceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetPayAsYouGoPriceResponseBodyData(DaraModel):
    def __init__(
        self,
        currency: str = None,
        module_details: main_models.GetPayAsYouGoPriceResponseBodyDataModuleDetails = None,
        promotion_details: main_models.GetPayAsYouGoPriceResponseBodyDataPromotionDetails = None,
    ):
        # The type of the currency. Valid values:
        # 
        # *   CNY: Chinese Yuan
        # *   USD: US dollar
        # *   JPY: Japanese Yen
        self.currency = currency
        # The price details of the pricing module.
        self.module_details = module_details
        # The details of the discount.
        self.promotion_details = promotion_details

    def validate(self):
        if self.module_details:
            self.module_details.validate()
        if self.promotion_details:
            self.promotion_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.currency is not None:
            result['Currency'] = self.currency

        if self.module_details is not None:
            result['ModuleDetails'] = self.module_details.to_map()

        if self.promotion_details is not None:
            result['PromotionDetails'] = self.promotion_details.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')

        if m.get('ModuleDetails') is not None:
            temp_model = main_models.GetPayAsYouGoPriceResponseBodyDataModuleDetails()
            self.module_details = temp_model.from_map(m.get('ModuleDetails'))

        if m.get('PromotionDetails') is not None:
            temp_model = main_models.GetPayAsYouGoPriceResponseBodyDataPromotionDetails()
            self.promotion_details = temp_model.from_map(m.get('PromotionDetails'))

        return self

class GetPayAsYouGoPriceResponseBodyDataPromotionDetails(DaraModel):
    def __init__(
        self,
        promotion_detail: List[main_models.GetPayAsYouGoPriceResponseBodyDataPromotionDetailsPromotionDetail] = None,
    ):
        self.promotion_detail = promotion_detail

    def validate(self):
        if self.promotion_detail:
            for v1 in self.promotion_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PromotionDetail'] = []
        if self.promotion_detail is not None:
            for k1 in self.promotion_detail:
                result['PromotionDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.promotion_detail = []
        if m.get('PromotionDetail') is not None:
            for k1 in m.get('PromotionDetail'):
                temp_model = main_models.GetPayAsYouGoPriceResponseBodyDataPromotionDetailsPromotionDetail()
                self.promotion_detail.append(temp_model.from_map(k1))

        return self

class GetPayAsYouGoPriceResponseBodyDataPromotionDetailsPromotionDetail(DaraModel):
    def __init__(
        self,
        promotion_desc: str = None,
        promotion_id: int = None,
        promotion_name: str = None,
    ):
        # The description of the discount.
        self.promotion_desc = promotion_desc
        # The ID of the discount.
        self.promotion_id = promotion_id
        # The name of the discount.
        self.promotion_name = promotion_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc

        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id

        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')

        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')

        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')

        return self

class GetPayAsYouGoPriceResponseBodyDataModuleDetails(DaraModel):
    def __init__(
        self,
        module_detail: List[main_models.GetPayAsYouGoPriceResponseBodyDataModuleDetailsModuleDetail] = None,
    ):
        self.module_detail = module_detail

    def validate(self):
        if self.module_detail:
            for v1 in self.module_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ModuleDetail'] = []
        if self.module_detail is not None:
            for k1 in self.module_detail:
                result['ModuleDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.module_detail = []
        if m.get('ModuleDetail') is not None:
            for k1 in m.get('ModuleDetail'):
                temp_model = main_models.GetPayAsYouGoPriceResponseBodyDataModuleDetailsModuleDetail()
                self.module_detail.append(temp_model.from_map(k1))

        return self

class GetPayAsYouGoPriceResponseBodyDataModuleDetailsModuleDetail(DaraModel):
    def __init__(
        self,
        cost_after_discount: float = None,
        invoice_discount: float = None,
        module_code: str = None,
        original_cost: float = None,
        unit_price: float = None,
    ):
        # The discount price.
        self.cost_after_discount = cost_after_discount
        # The discount that was applied.
        self.invoice_discount = invoice_discount
        # The code of the pricing module.
        self.module_code = module_code
        # The original price.
        self.original_cost = original_cost
        # The unit price.
        self.unit_price = unit_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost_after_discount is not None:
            result['CostAfterDiscount'] = self.cost_after_discount

        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount

        if self.module_code is not None:
            result['ModuleCode'] = self.module_code

        if self.original_cost is not None:
            result['OriginalCost'] = self.original_cost

        if self.unit_price is not None:
            result['UnitPrice'] = self.unit_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostAfterDiscount') is not None:
            self.cost_after_discount = m.get('CostAfterDiscount')

        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')

        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')

        if m.get('OriginalCost') is not None:
            self.original_cost = m.get('OriginalCost')

        if m.get('UnitPrice') is not None:
            self.unit_price = m.get('UnitPrice')

        return self

