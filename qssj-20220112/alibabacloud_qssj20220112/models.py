# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class GetAgeDistributionRequest(TeaModel):
    def __init__(
        self,
        cate_ids: str = None,
    ):
        self.cate_ids = cate_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_ids is not None:
            result['CateIds'] = self.cate_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateIds') is not None:
            self.cate_ids = m.get('CateIds')
        return self


class GetAgeDistributionResponseBodyData(TeaModel):
    def __init__(
        self,
        age_range: str = None,
        sale_numbers: int = None,
        search_numbers: int = None,
    ):
        self.age_range = age_range
        self.sale_numbers = sale_numbers
        self.search_numbers = search_numbers

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.age_range is not None:
            result['AgeRange'] = self.age_range
        if self.sale_numbers is not None:
            result['SaleNumbers'] = self.sale_numbers
        if self.search_numbers is not None:
            result['SearchNumbers'] = self.search_numbers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgeRange') is not None:
            self.age_range = m.get('AgeRange')
        if m.get('SaleNumbers') is not None:
            self.sale_numbers = m.get('SaleNumbers')
        if m.get('SearchNumbers') is not None:
            self.search_numbers = m.get('SearchNumbers')
        return self


class GetAgeDistributionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetAgeDistributionResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success_response: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success_response = success_response

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_response is not None:
            result['SuccessResponse'] = self.success_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetAgeDistributionResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessResponse') is not None:
            self.success_response = m.get('SuccessResponse')
        return self


class GetAgeDistributionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAgeDistributionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAgeDistributionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAllTrendCategoryResponseBodyData(TeaModel):
    def __init__(
        self,
        category_id: int = None,
        category_level: int = None,
        category_name: str = None,
        child_category: List[Any] = None,
        super_category_name: str = None,
    ):
        self.category_id = category_id
        self.category_level = category_level
        self.category_name = category_name
        self.child_category = child_category
        self.super_category_name = super_category_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_level is not None:
            result['CategoryLevel'] = self.category_level
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.child_category is not None:
            result['ChildCategory'] = self.child_category
        if self.super_category_name is not None:
            result['SuperCategoryName'] = self.super_category_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryLevel') is not None:
            self.category_level = m.get('CategoryLevel')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('ChildCategory') is not None:
            self.child_category = m.get('ChildCategory')
        if m.get('SuperCategoryName') is not None:
            self.super_category_name = m.get('SuperCategoryName')
        return self


class GetAllTrendCategoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetAllTrendCategoryResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success_response: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success_response = success_response

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_response is not None:
            result['SuccessResponse'] = self.success_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetAllTrendCategoryResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessResponse') is not None:
            self.success_response = m.get('SuccessResponse')
        return self


class GetAllTrendCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAllTrendCategoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAllTrendCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCrowdLabelRequest(TeaModel):
    def __init__(
        self,
        cate_ids: str = None,
    ):
        self.cate_ids = cate_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_ids is not None:
            result['CateIds'] = self.cate_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateIds') is not None:
            self.cate_ids = m.get('CateIds')
        return self


class GetCrowdLabelResponseBodyData(TeaModel):
    def __init__(
        self,
        closing_date: str = None,
        label_name: str = None,
        order_amount: float = None,
        purchase_amount: float = None,
        search_volume: float = None,
    ):
        self.closing_date = closing_date
        self.label_name = label_name
        self.order_amount = order_amount
        self.purchase_amount = purchase_amount
        self.search_volume = search_volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.closing_date is not None:
            result['ClosingDate'] = self.closing_date
        if self.label_name is not None:
            result['LabelName'] = self.label_name
        if self.order_amount is not None:
            result['OrderAmount'] = self.order_amount
        if self.purchase_amount is not None:
            result['PurchaseAmount'] = self.purchase_amount
        if self.search_volume is not None:
            result['SearchVolume'] = self.search_volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClosingDate') is not None:
            self.closing_date = m.get('ClosingDate')
        if m.get('LabelName') is not None:
            self.label_name = m.get('LabelName')
        if m.get('OrderAmount') is not None:
            self.order_amount = m.get('OrderAmount')
        if m.get('PurchaseAmount') is not None:
            self.purchase_amount = m.get('PurchaseAmount')
        if m.get('SearchVolume') is not None:
            self.search_volume = m.get('SearchVolume')
        return self


class GetCrowdLabelResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetCrowdLabelResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success_response: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success_response = success_response

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_response is not None:
            result['SuccessResponse'] = self.success_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetCrowdLabelResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessResponse') is not None:
            self.success_response = m.get('SuccessResponse')
        return self


class GetCrowdLabelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCrowdLabelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCrowdLabelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCrowdReginRequest(TeaModel):
    def __init__(
        self,
        cate_ids: str = None,
    ):
        self.cate_ids = cate_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_ids is not None:
            result['CateIds'] = self.cate_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateIds') is not None:
            self.cate_ids = m.get('CateIds')
        return self


class GetCrowdReginResponseBodyDataSaleNumbers(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: int = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetCrowdReginResponseBodyDataSearchNumbers(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: int = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetCrowdReginResponseBodyData(TeaModel):
    def __init__(
        self,
        sale_numbers: List[GetCrowdReginResponseBodyDataSaleNumbers] = None,
        search_numbers: List[GetCrowdReginResponseBodyDataSearchNumbers] = None,
    ):
        self.sale_numbers = sale_numbers
        self.search_numbers = search_numbers

    def validate(self):
        if self.sale_numbers:
            for k in self.sale_numbers:
                if k:
                    k.validate()
        if self.search_numbers:
            for k in self.search_numbers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SaleNumbers'] = []
        if self.sale_numbers is not None:
            for k in self.sale_numbers:
                result['SaleNumbers'].append(k.to_map() if k else None)
        result['SearchNumbers'] = []
        if self.search_numbers is not None:
            for k in self.search_numbers:
                result['SearchNumbers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sale_numbers = []
        if m.get('SaleNumbers') is not None:
            for k in m.get('SaleNumbers'):
                temp_model = GetCrowdReginResponseBodyDataSaleNumbers()
                self.sale_numbers.append(temp_model.from_map(k))
        self.search_numbers = []
        if m.get('SearchNumbers') is not None:
            for k in m.get('SearchNumbers'):
                temp_model = GetCrowdReginResponseBodyDataSearchNumbers()
                self.search_numbers.append(temp_model.from_map(k))
        return self


class GetCrowdReginResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetCrowdReginResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success_response: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success_response = success_response

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_response is not None:
            result['SuccessResponse'] = self.success_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetCrowdReginResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessResponse') is not None:
            self.success_response = m.get('SuccessResponse')
        return self


class GetCrowdReginResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCrowdReginResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCrowdReginResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOpportunityMarketRequest(TeaModel):
    def __init__(
        self,
        cate_ids: str = None,
        time_display: int = None,
    ):
        self.cate_ids = cate_ids
        self.time_display = time_display

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_ids is not None:
            result['CateIds'] = self.cate_ids
        if self.time_display is not None:
            result['TimeDisplay'] = self.time_display
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateIds') is not None:
            self.cate_ids = m.get('CateIds')
        if m.get('TimeDisplay') is not None:
            self.time_display = m.get('TimeDisplay')
        return self


class GetOpportunityMarketResponseBodyData(TeaModel):
    def __init__(
        self,
        cate_name: str = None,
        opportunity_index: float = None,
        relative_commodity: float = None,
        relative_discharge: float = None,
        time_unit: str = None,
    ):
        self.cate_name = cate_name
        self.opportunity_index = opportunity_index
        self.relative_commodity = relative_commodity
        self.relative_discharge = relative_discharge
        self.time_unit = time_unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.opportunity_index is not None:
            result['OpportunityIndex'] = self.opportunity_index
        if self.relative_commodity is not None:
            result['RelativeCommodity'] = self.relative_commodity
        if self.relative_discharge is not None:
            result['RelativeDischarge'] = self.relative_discharge
        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('OpportunityIndex') is not None:
            self.opportunity_index = m.get('OpportunityIndex')
        if m.get('RelativeCommodity') is not None:
            self.relative_commodity = m.get('RelativeCommodity')
        if m.get('RelativeDischarge') is not None:
            self.relative_discharge = m.get('RelativeDischarge')
        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')
        return self


class GetOpportunityMarketResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetOpportunityMarketResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success_response: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success_response = success_response

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_response is not None:
            result['SuccessResponse'] = self.success_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetOpportunityMarketResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessResponse') is not None:
            self.success_response = m.get('SuccessResponse')
        return self


class GetOpportunityMarketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOpportunityMarketResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetOpportunityMarketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPriceRangeRequest(TeaModel):
    def __init__(
        self,
        cate_ids: str = None,
    ):
        self.cate_ids = cate_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_ids is not None:
            result['CateIds'] = self.cate_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateIds') is not None:
            self.cate_ids = m.get('CateIds')
        return self


class GetPriceRangeResponseBodyData(TeaModel):
    def __init__(
        self,
        closing_date: str = None,
        goods_sales: int = None,
        price_range: str = None,
        sales_volume: float = None,
    ):
        self.closing_date = closing_date
        self.goods_sales = goods_sales
        self.price_range = price_range
        self.sales_volume = sales_volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.closing_date is not None:
            result['ClosingDate'] = self.closing_date
        if self.goods_sales is not None:
            result['GoodsSales'] = self.goods_sales
        if self.price_range is not None:
            result['PriceRange'] = self.price_range
        if self.sales_volume is not None:
            result['SalesVolume'] = self.sales_volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClosingDate') is not None:
            self.closing_date = m.get('ClosingDate')
        if m.get('GoodsSales') is not None:
            self.goods_sales = m.get('GoodsSales')
        if m.get('PriceRange') is not None:
            self.price_range = m.get('PriceRange')
        if m.get('SalesVolume') is not None:
            self.sales_volume = m.get('SalesVolume')
        return self


class GetPriceRangeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetPriceRangeResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success_response: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success_response = success_response

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_response is not None:
            result['SuccessResponse'] = self.success_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetPriceRangeResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessResponse') is not None:
            self.success_response = m.get('SuccessResponse')
        return self


class GetPriceRangeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPriceRangeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPriceRangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSexRatioRequest(TeaModel):
    def __init__(
        self,
        cate_ids: str = None,
    ):
        self.cate_ids = cate_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_ids is not None:
            result['CateIds'] = self.cate_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateIds') is not None:
            self.cate_ids = m.get('CateIds')
        return self


class GetSexRatioResponseBodyDataSaleNumbers(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: int = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetSexRatioResponseBodyDataSearchNumbers(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: int = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetSexRatioResponseBodyData(TeaModel):
    def __init__(
        self,
        sale_numbers: List[GetSexRatioResponseBodyDataSaleNumbers] = None,
        search_numbers: List[GetSexRatioResponseBodyDataSearchNumbers] = None,
    ):
        self.sale_numbers = sale_numbers
        self.search_numbers = search_numbers

    def validate(self):
        if self.sale_numbers:
            for k in self.sale_numbers:
                if k:
                    k.validate()
        if self.search_numbers:
            for k in self.search_numbers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SaleNumbers'] = []
        if self.sale_numbers is not None:
            for k in self.sale_numbers:
                result['SaleNumbers'].append(k.to_map() if k else None)
        result['SearchNumbers'] = []
        if self.search_numbers is not None:
            for k in self.search_numbers:
                result['SearchNumbers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sale_numbers = []
        if m.get('SaleNumbers') is not None:
            for k in m.get('SaleNumbers'):
                temp_model = GetSexRatioResponseBodyDataSaleNumbers()
                self.sale_numbers.append(temp_model.from_map(k))
        self.search_numbers = []
        if m.get('SearchNumbers') is not None:
            for k in m.get('SearchNumbers'):
                temp_model = GetSexRatioResponseBodyDataSearchNumbers()
                self.search_numbers.append(temp_model.from_map(k))
        return self


class GetSexRatioResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetSexRatioResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success_response: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success_response = success_response

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_response is not None:
            result['SuccessResponse'] = self.success_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetSexRatioResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessResponse') is not None:
            self.success_response = m.get('SuccessResponse')
        return self


class GetSexRatioResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSexRatioResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSexRatioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStoreSalesVolumeTopRequest(TeaModel):
    def __init__(
        self,
        cate_ids: str = None,
    ):
        self.cate_ids = cate_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_ids is not None:
            result['CateIds'] = self.cate_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateIds') is not None:
            self.cate_ids = m.get('CateIds')
        return self


class GetStoreSalesVolumeTopResponseBodyData(TeaModel):
    def __init__(
        self,
        shop_name: str = None,
    ):
        self.shop_name = shop_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.shop_name is not None:
            result['ShopName'] = self.shop_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShopName') is not None:
            self.shop_name = m.get('ShopName')
        return self


class GetStoreSalesVolumeTopResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetStoreSalesVolumeTopResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success_response: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success_response = success_response

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_response is not None:
            result['SuccessResponse'] = self.success_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetStoreSalesVolumeTopResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessResponse') is not None:
            self.success_response = m.get('SuccessResponse')
        return self


class GetStoreSalesVolumeTopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStoreSalesVolumeTopResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetStoreSalesVolumeTopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStoreSearchTopRequest(TeaModel):
    def __init__(
        self,
        cate_ids: str = None,
    ):
        self.cate_ids = cate_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_ids is not None:
            result['CateIds'] = self.cate_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateIds') is not None:
            self.cate_ids = m.get('CateIds')
        return self


class GetStoreSearchTopResponseBodyData(TeaModel):
    def __init__(
        self,
        shop_name: str = None,
    ):
        self.shop_name = shop_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.shop_name is not None:
            result['ShopName'] = self.shop_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShopName') is not None:
            self.shop_name = m.get('ShopName')
        return self


class GetStoreSearchTopResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetStoreSearchTopResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success_response: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success_response = success_response

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_response is not None:
            result['SuccessResponse'] = self.success_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetStoreSearchTopResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessResponse') is not None:
            self.success_response = m.get('SuccessResponse')
        return self


class GetStoreSearchTopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStoreSearchTopResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetStoreSearchTopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStyleTopRequest(TeaModel):
    def __init__(
        self,
        cate_ids: str = None,
        page_index: int = None,
        sort_order: int = None,
        time_display: int = None,
    ):
        self.cate_ids = cate_ids
        self.page_index = page_index
        self.sort_order = sort_order
        self.time_display = time_display

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_ids is not None:
            result['CateIds'] = self.cate_ids
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.time_display is not None:
            result['TimeDisplay'] = self.time_display
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateIds') is not None:
            self.cate_ids = m.get('CateIds')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('TimeDisplay') is not None:
            self.time_display = m.get('TimeDisplay')
        return self


class GetStyleTopResponseBodyData(TeaModel):
    def __init__(
        self,
        attribute_content: str = None,
        brand_name: str = None,
        buyer_tags: str = None,
        cate_name: str = None,
        color: str = None,
        images: List[str] = None,
        material: str = None,
        price: float = None,
        product_link: str = None,
        sales_volume: float = None,
        search_volume: float = None,
        shop_name: str = None,
        style: str = None,
        title: str = None,
    ):
        self.attribute_content = attribute_content
        self.brand_name = brand_name
        self.buyer_tags = buyer_tags
        self.cate_name = cate_name
        self.color = color
        self.images = images
        self.material = material
        self.price = price
        self.product_link = product_link
        self.sales_volume = sales_volume
        self.search_volume = search_volume
        self.shop_name = shop_name
        self.style = style
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_content is not None:
            result['AttributeContent'] = self.attribute_content
        if self.brand_name is not None:
            result['BrandName'] = self.brand_name
        if self.buyer_tags is not None:
            result['BuyerTags'] = self.buyer_tags
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.color is not None:
            result['Color'] = self.color
        if self.images is not None:
            result['Images'] = self.images
        if self.material is not None:
            result['Material'] = self.material
        if self.price is not None:
            result['Price'] = self.price
        if self.product_link is not None:
            result['ProductLink'] = self.product_link
        if self.sales_volume is not None:
            result['SalesVolume'] = self.sales_volume
        if self.search_volume is not None:
            result['SearchVolume'] = self.search_volume
        if self.shop_name is not None:
            result['ShopName'] = self.shop_name
        if self.style is not None:
            result['Style'] = self.style
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeContent') is not None:
            self.attribute_content = m.get('AttributeContent')
        if m.get('BrandName') is not None:
            self.brand_name = m.get('BrandName')
        if m.get('BuyerTags') is not None:
            self.buyer_tags = m.get('BuyerTags')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('Color') is not None:
            self.color = m.get('Color')
        if m.get('Images') is not None:
            self.images = m.get('Images')
        if m.get('Material') is not None:
            self.material = m.get('Material')
        if m.get('Price') is not None:
            self.price = m.get('Price')
        if m.get('ProductLink') is not None:
            self.product_link = m.get('ProductLink')
        if m.get('SalesVolume') is not None:
            self.sales_volume = m.get('SalesVolume')
        if m.get('SearchVolume') is not None:
            self.search_volume = m.get('SearchVolume')
        if m.get('ShopName') is not None:
            self.shop_name = m.get('ShopName')
        if m.get('Style') is not None:
            self.style = m.get('Style')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetStyleTopResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetStyleTopResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success_response: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success_response = success_response

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_response is not None:
            result['SuccessResponse'] = self.success_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetStyleTopResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessResponse') is not None:
            self.success_response = m.get('SuccessResponse')
        return self


class GetStyleTopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetStyleTopResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetStyleTopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrendImageDetailRequest(TeaModel):
    def __init__(
        self,
        ai_img_id: str = None,
    ):
        self.ai_img_id = ai_img_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ai_img_id is not None:
            result['AiImgId'] = self.ai_img_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiImgId') is not None:
            self.ai_img_id = m.get('AiImgId')
        return self


class GetTrendImageDetailResponseBodyDataSimilarGoods(TeaModel):
    def __init__(
        self,
        ai_img_url: str = None,
        goods_sales: int = None,
        search_volume: int = None,
    ):
        self.ai_img_url = ai_img_url
        self.goods_sales = goods_sales
        self.search_volume = search_volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ai_img_url is not None:
            result['AiImgUrl'] = self.ai_img_url
        if self.goods_sales is not None:
            result['GoodsSales'] = self.goods_sales
        if self.search_volume is not None:
            result['SearchVolume'] = self.search_volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiImgUrl') is not None:
            self.ai_img_url = m.get('AiImgUrl')
        if m.get('GoodsSales') is not None:
            self.goods_sales = m.get('GoodsSales')
        if m.get('SearchVolume') is not None:
            self.search_volume = m.get('SearchVolume')
        return self


class GetTrendImageDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        ai_img_id: str = None,
        ai_img_url: str = None,
        multi_pict_url: str = None,
        population: str = None,
        price_max: int = None,
        price_min: int = None,
        similar_goods: List[GetTrendImageDetailResponseBodyDataSimilarGoods] = None,
        tags: str = None,
    ):
        self.ai_img_id = ai_img_id
        self.ai_img_url = ai_img_url
        self.multi_pict_url = multi_pict_url
        self.population = population
        self.price_max = price_max
        self.price_min = price_min
        self.similar_goods = similar_goods
        self.tags = tags

    def validate(self):
        if self.similar_goods:
            for k in self.similar_goods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ai_img_id is not None:
            result['AiImgId'] = self.ai_img_id
        if self.ai_img_url is not None:
            result['AiImgUrl'] = self.ai_img_url
        if self.multi_pict_url is not None:
            result['MultiPictUrl'] = self.multi_pict_url
        if self.population is not None:
            result['Population'] = self.population
        if self.price_max is not None:
            result['PriceMax'] = self.price_max
        if self.price_min is not None:
            result['PriceMin'] = self.price_min
        result['SimilarGoods'] = []
        if self.similar_goods is not None:
            for k in self.similar_goods:
                result['SimilarGoods'].append(k.to_map() if k else None)
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiImgId') is not None:
            self.ai_img_id = m.get('AiImgId')
        if m.get('AiImgUrl') is not None:
            self.ai_img_url = m.get('AiImgUrl')
        if m.get('MultiPictUrl') is not None:
            self.multi_pict_url = m.get('MultiPictUrl')
        if m.get('Population') is not None:
            self.population = m.get('Population')
        if m.get('PriceMax') is not None:
            self.price_max = m.get('PriceMax')
        if m.get('PriceMin') is not None:
            self.price_min = m.get('PriceMin')
        self.similar_goods = []
        if m.get('SimilarGoods') is not None:
            for k in m.get('SimilarGoods'):
                temp_model = GetTrendImageDetailResponseBodyDataSimilarGoods()
                self.similar_goods.append(temp_model.from_map(k))
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class GetTrendImageDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetTrendImageDetailResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success_response: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success_response = success_response

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_response is not None:
            result['SuccessResponse'] = self.success_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetTrendImageDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessResponse') is not None:
            self.success_response = m.get('SuccessResponse')
        return self


class GetTrendImageDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTrendImageDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTrendImageDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrendImageListRequest(TeaModel):
    def __init__(
        self,
        cate_ids: str = None,
        query: str = None,
    ):
        self.cate_ids = cate_ids
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_ids is not None:
            result['CateIds'] = self.cate_ids
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateIds') is not None:
            self.cate_ids = m.get('CateIds')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class GetTrendImageListResponseBodyData(TeaModel):
    def __init__(
        self,
        ai_img_id: str = None,
        ai_img_url: str = None,
        population: str = None,
        price_max: int = None,
        price_min: int = None,
    ):
        self.ai_img_id = ai_img_id
        self.ai_img_url = ai_img_url
        self.population = population
        self.price_max = price_max
        self.price_min = price_min

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ai_img_id is not None:
            result['AiImgId'] = self.ai_img_id
        if self.ai_img_url is not None:
            result['AiImgUrl'] = self.ai_img_url
        if self.population is not None:
            result['Population'] = self.population
        if self.price_max is not None:
            result['PriceMax'] = self.price_max
        if self.price_min is not None:
            result['PriceMin'] = self.price_min
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiImgId') is not None:
            self.ai_img_id = m.get('AiImgId')
        if m.get('AiImgUrl') is not None:
            self.ai_img_url = m.get('AiImgUrl')
        if m.get('Population') is not None:
            self.population = m.get('Population')
        if m.get('PriceMax') is not None:
            self.price_max = m.get('PriceMax')
        if m.get('PriceMin') is not None:
            self.price_min = m.get('PriceMin')
        return self


class GetTrendImageListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetTrendImageListResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success_response: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success_response = success_response

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_response is not None:
            result['SuccessResponse'] = self.success_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetTrendImageListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessResponse') is not None:
            self.success_response = m.get('SuccessResponse')
        return self


class GetTrendImageListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTrendImageListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTrendImageListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrendIndexRequest(TeaModel):
    def __init__(
        self,
        cate_ids: str = None,
        month_num: int = None,
    ):
        self.cate_ids = cate_ids
        self.month_num = month_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_ids is not None:
            result['CateIds'] = self.cate_ids
        if self.month_num is not None:
            result['MonthNum'] = self.month_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateIds') is not None:
            self.cate_ids = m.get('CateIds')
        if m.get('MonthNum') is not None:
            self.month_num = m.get('MonthNum')
        return self


class GetTrendIndexResponseBodyData(TeaModel):
    def __init__(
        self,
        brand_index: float = None,
        ecommerce_index: float = None,
        institutional_index: float = None,
        media_index: float = None,
        social_index: float = None,
        trend_index: float = None,
        year_month: str = None,
    ):
        self.brand_index = brand_index
        self.ecommerce_index = ecommerce_index
        self.institutional_index = institutional_index
        self.media_index = media_index
        self.social_index = social_index
        self.trend_index = trend_index
        self.year_month = year_month

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.brand_index is not None:
            result['BrandIndex'] = self.brand_index
        if self.ecommerce_index is not None:
            result['ECommerceIndex'] = self.ecommerce_index
        if self.institutional_index is not None:
            result['InstitutionalIndex'] = self.institutional_index
        if self.media_index is not None:
            result['MediaIndex'] = self.media_index
        if self.social_index is not None:
            result['SocialIndex'] = self.social_index
        if self.trend_index is not None:
            result['TrendIndex'] = self.trend_index
        if self.year_month is not None:
            result['YearMonth'] = self.year_month
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BrandIndex') is not None:
            self.brand_index = m.get('BrandIndex')
        if m.get('ECommerceIndex') is not None:
            self.ecommerce_index = m.get('ECommerceIndex')
        if m.get('InstitutionalIndex') is not None:
            self.institutional_index = m.get('InstitutionalIndex')
        if m.get('MediaIndex') is not None:
            self.media_index = m.get('MediaIndex')
        if m.get('SocialIndex') is not None:
            self.social_index = m.get('SocialIndex')
        if m.get('TrendIndex') is not None:
            self.trend_index = m.get('TrendIndex')
        if m.get('YearMonth') is not None:
            self.year_month = m.get('YearMonth')
        return self


class GetTrendIndexResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetTrendIndexResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success_response: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success_response = success_response

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_response is not None:
            result['SuccessResponse'] = self.success_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetTrendIndexResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessResponse') is not None:
            self.success_response = m.get('SuccessResponse')
        return self


class GetTrendIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTrendIndexResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTrendIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrendSearchRecordRequest(TeaModel):
    def __init__(
        self,
        key: str = None,
    ):
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class GetTrendSearchRecordResponseBodyData(TeaModel):
    def __init__(
        self,
        id: int = None,
        query_key: str = None,
    ):
        self.id = id
        self.query_key = query_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.query_key is not None:
            result['QueryKey'] = self.query_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('QueryKey') is not None:
            self.query_key = m.get('QueryKey')
        return self


class GetTrendSearchRecordResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetTrendSearchRecordResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success_response: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success_response = success_response

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_response is not None:
            result['SuccessResponse'] = self.success_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetTrendSearchRecordResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessResponse') is not None:
            self.success_response = m.get('SuccessResponse')
        return self


class GetTrendSearchRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTrendSearchRecordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTrendSearchRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrendStatisticRequest(TeaModel):
    def __init__(
        self,
        cate_ids: str = None,
    ):
        self.cate_ids = cate_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_ids is not None:
            result['CateIds'] = self.cate_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateIds') is not None:
            self.cate_ids = m.get('CateIds')
        return self


class GetTrendStatisticResponseBodyData(TeaModel):
    def __init__(
        self,
        commodity_count: int = None,
        sales: float = None,
        shop_count: int = None,
    ):
        self.commodity_count = commodity_count
        self.sales = sales
        self.shop_count = shop_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_count is not None:
            result['CommodityCount'] = self.commodity_count
        if self.sales is not None:
            result['Sales'] = self.sales
        if self.shop_count is not None:
            result['ShopCount'] = self.shop_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCount') is not None:
            self.commodity_count = m.get('CommodityCount')
        if m.get('Sales') is not None:
            self.sales = m.get('Sales')
        if m.get('ShopCount') is not None:
            self.shop_count = m.get('ShopCount')
        return self


class GetTrendStatisticResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetTrendStatisticResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success_response: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success_response = success_response

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_response is not None:
            result['SuccessResponse'] = self.success_response
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetTrendStatisticResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessResponse') is not None:
            self.success_response = m.get('SuccessResponse')
        return self


class GetTrendStatisticResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTrendStatisticResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTrendStatisticResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


