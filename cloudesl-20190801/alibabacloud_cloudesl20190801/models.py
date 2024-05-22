# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ActivateApDeviceRequest(TeaModel):
    def __init__(
        self,
        ap_mac: str = None,
        store_id: str = None,
    ):
        # This parameter is required.
        self.ap_mac = ap_mac
        # This parameter is required.
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class ActivateApDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ActivateApDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ActivateApDeviceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ActivateApDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddApDeviceRequest(TeaModel):
    def __init__(
        self,
        ap_mac: str = None,
        store_id: str = None,
    ):
        # This parameter is required.
        self.ap_mac = ap_mac
        # This parameter is required.
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class AddApDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddApDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddApDeviceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AddApDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddEslDeviceRequest(TeaModel):
    def __init__(
        self,
        esl_bar_code: str = None,
        store_id: str = None,
    ):
        # This parameter is required.
        self.esl_bar_code = esl_bar_code
        # This parameter is required.
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class AddEslDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddEslDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddEslDeviceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AddEslDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUserRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AddUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AddUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssignUserRequest(TeaModel):
    def __init__(
        self,
        stores: str = None,
        user_id: str = None,
        user_type: str = None,
    ):
        self.stores = stores
        # This parameter is required.
        self.user_id = user_id
        # This parameter is required.
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stores is not None:
            result['Stores'] = self.stores
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Stores') is not None:
            self.stores = m.get('Stores')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class AssignUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AssignUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssignUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AssignUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchInsertItemsRequestItemInfo(TeaModel):
    def __init__(
        self,
        action_price: int = None,
        be_promotion: bool = None,
        be_source_code: bool = None,
        brand_name: str = None,
        category_name: str = None,
        company_id: str = None,
        customize_feature_a: str = None,
        customize_feature_b: str = None,
        customize_feature_c: str = None,
        customize_feature_d: str = None,
        customize_feature_e: str = None,
        customize_feature_f: str = None,
        customize_feature_g: str = None,
        customize_feature_h: str = None,
        customize_feature_i: str = None,
        customize_feature_j: str = None,
        energy_efficiency: str = None,
        extra_attribute: str = None,
        forest_first_id: str = None,
        forest_second_id: str = None,
        item_bar_code: str = None,
        item_id: int = None,
        item_info_index: int = None,
        item_qr_code: str = None,
        item_short_title: str = None,
        item_title: str = None,
        member_price: int = None,
        model_number: str = None,
        option_groups: str = None,
        original_price: int = None,
        price_unit: str = None,
        production_place: str = None,
        promotion_end: str = None,
        promotion_reason: str = None,
        promotion_start: str = None,
        promotion_text: str = None,
        rank: str = None,
        sale_spec: str = None,
        sku_id: str = None,
        source_code: str = None,
        store_id: str = None,
        suggest_price: int = None,
    ):
        self.action_price = action_price
        self.be_promotion = be_promotion
        self.be_source_code = be_source_code
        self.brand_name = brand_name
        self.category_name = category_name
        self.company_id = company_id
        self.customize_feature_a = customize_feature_a
        self.customize_feature_b = customize_feature_b
        self.customize_feature_c = customize_feature_c
        self.customize_feature_d = customize_feature_d
        self.customize_feature_e = customize_feature_e
        self.customize_feature_f = customize_feature_f
        self.customize_feature_g = customize_feature_g
        self.customize_feature_h = customize_feature_h
        self.customize_feature_i = customize_feature_i
        self.customize_feature_j = customize_feature_j
        self.energy_efficiency = energy_efficiency
        self.extra_attribute = extra_attribute
        self.forest_first_id = forest_first_id
        self.forest_second_id = forest_second_id
        self.item_bar_code = item_bar_code
        self.item_id = item_id
        self.item_info_index = item_info_index
        self.item_qr_code = item_qr_code
        self.item_short_title = item_short_title
        self.item_title = item_title
        self.member_price = member_price
        self.model_number = model_number
        self.option_groups = option_groups
        self.original_price = original_price
        self.price_unit = price_unit
        self.production_place = production_place
        self.promotion_end = promotion_end
        self.promotion_reason = promotion_reason
        self.promotion_start = promotion_start
        self.promotion_text = promotion_text
        self.rank = rank
        self.sale_spec = sale_spec
        self.sku_id = sku_id
        self.source_code = source_code
        self.store_id = store_id
        self.suggest_price = suggest_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_price is not None:
            result['ActionPrice'] = self.action_price
        if self.be_promotion is not None:
            result['BePromotion'] = self.be_promotion
        if self.be_source_code is not None:
            result['BeSourceCode'] = self.be_source_code
        if self.brand_name is not None:
            result['BrandName'] = self.brand_name
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.company_id is not None:
            result['CompanyId'] = self.company_id
        if self.customize_feature_a is not None:
            result['CustomizeFeatureA'] = self.customize_feature_a
        if self.customize_feature_b is not None:
            result['CustomizeFeatureB'] = self.customize_feature_b
        if self.customize_feature_c is not None:
            result['CustomizeFeatureC'] = self.customize_feature_c
        if self.customize_feature_d is not None:
            result['CustomizeFeatureD'] = self.customize_feature_d
        if self.customize_feature_e is not None:
            result['CustomizeFeatureE'] = self.customize_feature_e
        if self.customize_feature_f is not None:
            result['CustomizeFeatureF'] = self.customize_feature_f
        if self.customize_feature_g is not None:
            result['CustomizeFeatureG'] = self.customize_feature_g
        if self.customize_feature_h is not None:
            result['CustomizeFeatureH'] = self.customize_feature_h
        if self.customize_feature_i is not None:
            result['CustomizeFeatureI'] = self.customize_feature_i
        if self.customize_feature_j is not None:
            result['CustomizeFeatureJ'] = self.customize_feature_j
        if self.energy_efficiency is not None:
            result['EnergyEfficiency'] = self.energy_efficiency
        if self.extra_attribute is not None:
            result['ExtraAttribute'] = self.extra_attribute
        if self.forest_first_id is not None:
            result['ForestFirstId'] = self.forest_first_id
        if self.forest_second_id is not None:
            result['ForestSecondId'] = self.forest_second_id
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_info_index is not None:
            result['ItemInfoIndex'] = self.item_info_index
        if self.item_qr_code is not None:
            result['ItemQrCode'] = self.item_qr_code
        if self.item_short_title is not None:
            result['ItemShortTitle'] = self.item_short_title
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.member_price is not None:
            result['MemberPrice'] = self.member_price
        if self.model_number is not None:
            result['ModelNumber'] = self.model_number
        if self.option_groups is not None:
            result['OptionGroups'] = self.option_groups
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit
        if self.production_place is not None:
            result['ProductionPlace'] = self.production_place
        if self.promotion_end is not None:
            result['PromotionEnd'] = self.promotion_end
        if self.promotion_reason is not None:
            result['PromotionReason'] = self.promotion_reason
        if self.promotion_start is not None:
            result['PromotionStart'] = self.promotion_start
        if self.promotion_text is not None:
            result['PromotionText'] = self.promotion_text
        if self.rank is not None:
            result['Rank'] = self.rank
        if self.sale_spec is not None:
            result['SaleSpec'] = self.sale_spec
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.suggest_price is not None:
            result['SuggestPrice'] = self.suggest_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionPrice') is not None:
            self.action_price = m.get('ActionPrice')
        if m.get('BePromotion') is not None:
            self.be_promotion = m.get('BePromotion')
        if m.get('BeSourceCode') is not None:
            self.be_source_code = m.get('BeSourceCode')
        if m.get('BrandName') is not None:
            self.brand_name = m.get('BrandName')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('CompanyId') is not None:
            self.company_id = m.get('CompanyId')
        if m.get('CustomizeFeatureA') is not None:
            self.customize_feature_a = m.get('CustomizeFeatureA')
        if m.get('CustomizeFeatureB') is not None:
            self.customize_feature_b = m.get('CustomizeFeatureB')
        if m.get('CustomizeFeatureC') is not None:
            self.customize_feature_c = m.get('CustomizeFeatureC')
        if m.get('CustomizeFeatureD') is not None:
            self.customize_feature_d = m.get('CustomizeFeatureD')
        if m.get('CustomizeFeatureE') is not None:
            self.customize_feature_e = m.get('CustomizeFeatureE')
        if m.get('CustomizeFeatureF') is not None:
            self.customize_feature_f = m.get('CustomizeFeatureF')
        if m.get('CustomizeFeatureG') is not None:
            self.customize_feature_g = m.get('CustomizeFeatureG')
        if m.get('CustomizeFeatureH') is not None:
            self.customize_feature_h = m.get('CustomizeFeatureH')
        if m.get('CustomizeFeatureI') is not None:
            self.customize_feature_i = m.get('CustomizeFeatureI')
        if m.get('CustomizeFeatureJ') is not None:
            self.customize_feature_j = m.get('CustomizeFeatureJ')
        if m.get('EnergyEfficiency') is not None:
            self.energy_efficiency = m.get('EnergyEfficiency')
        if m.get('ExtraAttribute') is not None:
            self.extra_attribute = m.get('ExtraAttribute')
        if m.get('ForestFirstId') is not None:
            self.forest_first_id = m.get('ForestFirstId')
        if m.get('ForestSecondId') is not None:
            self.forest_second_id = m.get('ForestSecondId')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemInfoIndex') is not None:
            self.item_info_index = m.get('ItemInfoIndex')
        if m.get('ItemQrCode') is not None:
            self.item_qr_code = m.get('ItemQrCode')
        if m.get('ItemShortTitle') is not None:
            self.item_short_title = m.get('ItemShortTitle')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('MemberPrice') is not None:
            self.member_price = m.get('MemberPrice')
        if m.get('ModelNumber') is not None:
            self.model_number = m.get('ModelNumber')
        if m.get('OptionGroups') is not None:
            self.option_groups = m.get('OptionGroups')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')
        if m.get('ProductionPlace') is not None:
            self.production_place = m.get('ProductionPlace')
        if m.get('PromotionEnd') is not None:
            self.promotion_end = m.get('PromotionEnd')
        if m.get('PromotionReason') is not None:
            self.promotion_reason = m.get('PromotionReason')
        if m.get('PromotionStart') is not None:
            self.promotion_start = m.get('PromotionStart')
        if m.get('PromotionText') is not None:
            self.promotion_text = m.get('PromotionText')
        if m.get('Rank') is not None:
            self.rank = m.get('Rank')
        if m.get('SaleSpec') is not None:
            self.sale_spec = m.get('SaleSpec')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('SuggestPrice') is not None:
            self.suggest_price = m.get('SuggestPrice')
        return self


class BatchInsertItemsRequest(TeaModel):
    def __init__(
        self,
        item_info: List[BatchInsertItemsRequestItemInfo] = None,
        store_id: str = None,
    ):
        # This parameter is required.
        self.item_info = item_info
        # This parameter is required.
        self.store_id = store_id

    def validate(self):
        if self.item_info:
            for k in self.item_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ItemInfo'] = []
        if self.item_info is not None:
            for k in self.item_info:
                result['ItemInfo'].append(k.to_map() if k else None)
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item_info = []
        if m.get('ItemInfo') is not None:
            for k in m.get('ItemInfo'):
                temp_model = BatchInsertItemsRequestItemInfo()
                self.item_info.append(temp_model.from_map(k))
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class BatchInsertItemsResponseBodyBatchResultsBatchResult(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        index: int = None,
        message: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.index = index
        self.message = message
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.index is not None:
            result['Index'] = self.index
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchInsertItemsResponseBodyBatchResults(TeaModel):
    def __init__(
        self,
        batch_result: List[BatchInsertItemsResponseBodyBatchResultsBatchResult] = None,
    ):
        self.batch_result = batch_result

    def validate(self):
        if self.batch_result:
            for k in self.batch_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BatchResult'] = []
        if self.batch_result is not None:
            for k in self.batch_result:
                result['BatchResult'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.batch_result = []
        if m.get('BatchResult') is not None:
            for k in m.get('BatchResult'):
                temp_model = BatchInsertItemsResponseBodyBatchResultsBatchResult()
                self.batch_result.append(temp_model.from_map(k))
        return self


class BatchInsertItemsResponseBody(TeaModel):
    def __init__(
        self,
        batch_results: BatchInsertItemsResponseBodyBatchResults = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.batch_results = batch_results
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.batch_results:
            self.batch_results.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_results is not None:
            result['BatchResults'] = self.batch_results.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchResults') is not None:
            temp_model = BatchInsertItemsResponseBodyBatchResults()
            self.batch_results = temp_model.from_map(m['BatchResults'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchInsertItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchInsertItemsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = BatchInsertItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindEslDeviceRequest(TeaModel):
    def __init__(
        self,
        esl_bar_code: str = None,
        item_bar_code: str = None,
        store_id: str = None,
    ):
        # This parameter is required.
        self.esl_bar_code = esl_bar_code
        # This parameter is required.
        self.item_bar_code = item_bar_code
        # This parameter is required.
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class BindEslDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BindEslDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindEslDeviceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = BindEslDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindEslDeviceShelfRequest(TeaModel):
    def __init__(
        self,
        esl_bar_code: str = None,
        shelf_code: str = None,
        store_id: str = None,
    ):
        # This parameter is required.
        self.esl_bar_code = esl_bar_code
        # This parameter is required.
        self.shelf_code = shelf_code
        # This parameter is required.
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.shelf_code is not None:
            result['ShelfCode'] = self.shelf_code
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('ShelfCode') is not None:
            self.shelf_code = m.get('ShelfCode')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class BindEslDeviceShelfResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BindEslDeviceShelfResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindEslDeviceShelfResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = BindEslDeviceShelfResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmLogisticsRequest(TeaModel):
    def __init__(
        self,
        logistics_documents: str = None,
        po_number: str = None,
        pr_number: str = None,
        status: str = None,
    ):
        self.logistics_documents = logistics_documents
        # This parameter is required.
        self.po_number = po_number
        # This parameter is required.
        self.pr_number = pr_number
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logistics_documents is not None:
            result['LogisticsDocuments'] = self.logistics_documents
        if self.po_number is not None:
            result['PoNumber'] = self.po_number
        if self.pr_number is not None:
            result['PrNumber'] = self.pr_number
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogisticsDocuments') is not None:
            self.logistics_documents = m.get('LogisticsDocuments')
        if m.get('PoNumber') is not None:
            self.po_number = m.get('PoNumber')
        if m.get('PrNumber') is not None:
            self.pr_number = m.get('PrNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ConfirmLogisticsResponseBody(TeaModel):
    def __init__(
        self,
        acceptance: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.acceptance = acceptance
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acceptance is not None:
            result['Acceptance'] = self.acceptance
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acceptance') is not None:
            self.acceptance = m.get('Acceptance')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConfirmLogisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfirmLogisticsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ConfirmLogisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStoreRequest(TeaModel):
    def __init__(
        self,
        brand: str = None,
        comments: str = None,
        company_id: str = None,
        groups: str = None,
        out_id: str = None,
        parent_id: str = None,
        phone: str = None,
        store_name: str = None,
    ):
        self.brand = brand
        self.comments = comments
        # This parameter is required.
        self.company_id = company_id
        self.groups = groups
        self.out_id = out_id
        self.parent_id = parent_id
        # This parameter is required.
        self.phone = phone
        # This parameter is required.
        self.store_name = store_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.brand is not None:
            result['Brand'] = self.brand
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.company_id is not None:
            result['CompanyId'] = self.company_id
        if self.groups is not None:
            result['Groups'] = self.groups
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Brand') is not None:
            self.brand = m.get('Brand')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CompanyId') is not None:
            self.company_id = m.get('CompanyId')
        if m.get('Groups') is not None:
            self.groups = m.get('Groups')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        return self


class CreateStoreResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        store_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.store_id = store_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateStoreResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CreateStoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApDeviceRequest(TeaModel):
    def __init__(
        self,
        ap_mac: str = None,
        store_id: str = None,
    ):
        # This parameter is required.
        self.ap_mac = ap_mac
        # This parameter is required.
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class DeleteApDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteApDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteApDeviceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteApDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEslDeviceRequest(TeaModel):
    def __init__(
        self,
        esl_bar_code: str = None,
        store_id: str = None,
    ):
        # This parameter is required.
        self.esl_bar_code = esl_bar_code
        # This parameter is required.
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class DeleteEslDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteEslDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEslDeviceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteEslDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteItemRequest(TeaModel):
    def __init__(
        self,
        item_bar_code: str = None,
        store_id: str = None,
    ):
        # This parameter is required.
        self.item_bar_code = item_bar_code
        # This parameter is required.
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class DeleteItemResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteItemResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteItemBySkuIdRequest(TeaModel):
    def __init__(
        self,
        sku_id: str = None,
        store_id: str = None,
    ):
        # This parameter is required.
        self.sku_id = sku_id
        # This parameter is required.
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class DeleteItemBySkuIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteItemBySkuIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteItemBySkuIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteItemBySkuIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteStoreRequest(TeaModel):
    def __init__(
        self,
        store_id: str = None,
    ):
        # This parameter is required.
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class DeleteStoreResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteStoreResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteStoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAlarmsRequest(TeaModel):
    def __init__(
        self,
        alarm_id: str = None,
        alarm_status: str = None,
        alarm_type: str = None,
        error_type: str = None,
        from_alarm_time: str = None,
        page_number: int = None,
        page_size: int = None,
        store_id: str = None,
        to_alarm_time: str = None,
    ):
        self.alarm_id = alarm_id
        self.alarm_status = alarm_status
        self.alarm_type = alarm_type
        self.error_type = error_type
        self.from_alarm_time = from_alarm_time
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.store_id = store_id
        self.to_alarm_time = to_alarm_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.alarm_status is not None:
            result['AlarmStatus'] = self.alarm_status
        if self.alarm_type is not None:
            result['AlarmType'] = self.alarm_type
        if self.error_type is not None:
            result['ErrorType'] = self.error_type
        if self.from_alarm_time is not None:
            result['FromAlarmTime'] = self.from_alarm_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.to_alarm_time is not None:
            result['ToAlarmTime'] = self.to_alarm_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('AlarmStatus') is not None:
            self.alarm_status = m.get('AlarmStatus')
        if m.get('AlarmType') is not None:
            self.alarm_type = m.get('AlarmType')
        if m.get('ErrorType') is not None:
            self.error_type = m.get('ErrorType')
        if m.get('FromAlarmTime') is not None:
            self.from_alarm_time = m.get('FromAlarmTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('ToAlarmTime') is not None:
            self.to_alarm_time = m.get('ToAlarmTime')
        return self


class DescribeAlarmsResponseBodyAlarmsAlarmInfo(TeaModel):
    def __init__(
        self,
        alarm_id: str = None,
        alarm_status: str = None,
        alarm_time: str = None,
        alarm_type: str = None,
        company_id: str = None,
        deal_time: str = None,
        deal_user_id: int = None,
        device_bar_code: str = None,
        device_mac: str = None,
        device_type: str = None,
        error_type: str = None,
        item_bar_code: str = None,
        item_title: str = None,
        model: str = None,
        store_id: str = None,
        vendor: str = None,
    ):
        self.alarm_id = alarm_id
        self.alarm_status = alarm_status
        self.alarm_time = alarm_time
        self.alarm_type = alarm_type
        self.company_id = company_id
        self.deal_time = deal_time
        self.deal_user_id = deal_user_id
        self.device_bar_code = device_bar_code
        self.device_mac = device_mac
        self.device_type = device_type
        self.error_type = error_type
        self.item_bar_code = item_bar_code
        self.item_title = item_title
        self.model = model
        self.store_id = store_id
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.alarm_status is not None:
            result['AlarmStatus'] = self.alarm_status
        if self.alarm_time is not None:
            result['AlarmTime'] = self.alarm_time
        if self.alarm_type is not None:
            result['AlarmType'] = self.alarm_type
        if self.company_id is not None:
            result['CompanyId'] = self.company_id
        if self.deal_time is not None:
            result['DealTime'] = self.deal_time
        if self.deal_user_id is not None:
            result['DealUserId'] = self.deal_user_id
        if self.device_bar_code is not None:
            result['DeviceBarCode'] = self.device_bar_code
        if self.device_mac is not None:
            result['DeviceMac'] = self.device_mac
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.error_type is not None:
            result['ErrorType'] = self.error_type
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.model is not None:
            result['Model'] = self.model
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('AlarmStatus') is not None:
            self.alarm_status = m.get('AlarmStatus')
        if m.get('AlarmTime') is not None:
            self.alarm_time = m.get('AlarmTime')
        if m.get('AlarmType') is not None:
            self.alarm_type = m.get('AlarmType')
        if m.get('CompanyId') is not None:
            self.company_id = m.get('CompanyId')
        if m.get('DealTime') is not None:
            self.deal_time = m.get('DealTime')
        if m.get('DealUserId') is not None:
            self.deal_user_id = m.get('DealUserId')
        if m.get('DeviceBarCode') is not None:
            self.device_bar_code = m.get('DeviceBarCode')
        if m.get('DeviceMac') is not None:
            self.device_mac = m.get('DeviceMac')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('ErrorType') is not None:
            self.error_type = m.get('ErrorType')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class DescribeAlarmsResponseBodyAlarms(TeaModel):
    def __init__(
        self,
        alarm_info: List[DescribeAlarmsResponseBodyAlarmsAlarmInfo] = None,
    ):
        self.alarm_info = alarm_info

    def validate(self):
        if self.alarm_info:
            for k in self.alarm_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlarmInfo'] = []
        if self.alarm_info is not None:
            for k in self.alarm_info:
                result['AlarmInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarm_info = []
        if m.get('AlarmInfo') is not None:
            for k in m.get('AlarmInfo'):
                temp_model = DescribeAlarmsResponseBodyAlarmsAlarmInfo()
                self.alarm_info.append(temp_model.from_map(k))
        return self


class DescribeAlarmsResponseBody(TeaModel):
    def __init__(
        self,
        alarms: DescribeAlarmsResponseBodyAlarms = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.alarms = alarms
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.alarms:
            self.alarms.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarms is not None:
            result['Alarms'] = self.alarms.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alarms') is not None:
            temp_model = DescribeAlarmsResponseBodyAlarms()
            self.alarms = temp_model.from_map(m['Alarms'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAlarmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAlarmsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeAlarmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApDevicesRequest(TeaModel):
    def __init__(
        self,
        activated: bool = None,
        ap_mac: str = None,
        page_number: int = None,
        page_size: int = None,
        store_id: str = None,
    ):
        self.activated = activated
        self.ap_mac = ap_mac
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activated is not None:
            result['Activated'] = self.activated
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Activated') is not None:
            self.activated = m.get('Activated')
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class DescribeApDevicesResponseBodyApDevicesApInfo(TeaModel):
    def __init__(
        self,
        is_activate: bool = None,
        mac: str = None,
        model: str = None,
        status: bool = None,
    ):
        self.is_activate = is_activate
        self.mac = mac
        self.model = model
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_activate is not None:
            result['IsActivate'] = self.is_activate
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.model is not None:
            result['Model'] = self.model
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsActivate') is not None:
            self.is_activate = m.get('IsActivate')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeApDevicesResponseBodyApDevices(TeaModel):
    def __init__(
        self,
        ap_info: List[DescribeApDevicesResponseBodyApDevicesApInfo] = None,
    ):
        self.ap_info = ap_info

    def validate(self):
        if self.ap_info:
            for k in self.ap_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApInfo'] = []
        if self.ap_info is not None:
            for k in self.ap_info:
                result['ApInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ap_info = []
        if m.get('ApInfo') is not None:
            for k in m.get('ApInfo'):
                temp_model = DescribeApDevicesResponseBodyApDevicesApInfo()
                self.ap_info.append(temp_model.from_map(k))
        return self


class DescribeApDevicesResponseBody(TeaModel):
    def __init__(
        self,
        ap_devices: DescribeApDevicesResponseBodyApDevices = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.ap_devices = ap_devices
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.ap_devices:
            self.ap_devices.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_devices is not None:
            result['ApDevices'] = self.ap_devices.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApDevices') is not None:
            temp_model = DescribeApDevicesResponseBodyApDevices()
            self.ap_devices = temp_model.from_map(m['ApDevices'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeApDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeApDevicesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeApDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEslDevicesRequest(TeaModel):
    def __init__(
        self,
        be_bind: bool = None,
        esl_bar_code: str = None,
        esl_status: str = None,
        from_battery_level: int = None,
        item_bar_code: str = None,
        mac: str = None,
        page_number: int = None,
        page_size: int = None,
        shelf_code: str = None,
        store_id: str = None,
        to_battery_level: int = None,
        type: str = None,
        vendor: str = None,
    ):
        self.be_bind = be_bind
        self.esl_bar_code = esl_bar_code
        self.esl_status = esl_status
        self.from_battery_level = from_battery_level
        self.item_bar_code = item_bar_code
        self.mac = mac
        self.page_number = page_number
        self.page_size = page_size
        self.shelf_code = shelf_code
        # This parameter is required.
        self.store_id = store_id
        self.to_battery_level = to_battery_level
        self.type = type
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.be_bind is not None:
            result['BeBind'] = self.be_bind
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.esl_status is not None:
            result['EslStatus'] = self.esl_status
        if self.from_battery_level is not None:
            result['FromBatteryLevel'] = self.from_battery_level
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.shelf_code is not None:
            result['ShelfCode'] = self.shelf_code
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.to_battery_level is not None:
            result['ToBatteryLevel'] = self.to_battery_level
        if self.type is not None:
            result['Type'] = self.type
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeBind') is not None:
            self.be_bind = m.get('BeBind')
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('EslStatus') is not None:
            self.esl_status = m.get('EslStatus')
        if m.get('FromBatteryLevel') is not None:
            self.from_battery_level = m.get('FromBatteryLevel')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ShelfCode') is not None:
            self.shelf_code = m.get('ShelfCode')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('ToBatteryLevel') is not None:
            self.to_battery_level = m.get('ToBatteryLevel')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class DescribeEslDevicesResponseBodyEslDevicesEslDeviceInfo(TeaModel):
    def __init__(
        self,
        battery_level: int = None,
        be_bind: bool = None,
        company_id: str = None,
        connect_ap: str = None,
        esl_bar_code: str = None,
        esl_status: str = None,
        item_action_price: int = None,
        item_bar_code: str = None,
        item_id: int = None,
        item_price_unit: str = None,
        item_title: str = None,
        last_communicate_time: str = None,
        mac: str = None,
        model: str = None,
        position_code: str = None,
        screen_height: int = None,
        screen_width: int = None,
        shelf_code: str = None,
        store_id: str = None,
        type: str = None,
        vendor: str = None,
    ):
        self.battery_level = battery_level
        self.be_bind = be_bind
        self.company_id = company_id
        self.connect_ap = connect_ap
        self.esl_bar_code = esl_bar_code
        self.esl_status = esl_status
        self.item_action_price = item_action_price
        self.item_bar_code = item_bar_code
        self.item_id = item_id
        self.item_price_unit = item_price_unit
        self.item_title = item_title
        self.last_communicate_time = last_communicate_time
        self.mac = mac
        self.model = model
        self.position_code = position_code
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.shelf_code = shelf_code
        self.store_id = store_id
        self.type = type
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.battery_level is not None:
            result['BatteryLevel'] = self.battery_level
        if self.be_bind is not None:
            result['BeBind'] = self.be_bind
        if self.company_id is not None:
            result['CompanyId'] = self.company_id
        if self.connect_ap is not None:
            result['ConnectAp'] = self.connect_ap
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.esl_status is not None:
            result['EslStatus'] = self.esl_status
        if self.item_action_price is not None:
            result['ItemActionPrice'] = self.item_action_price
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_price_unit is not None:
            result['ItemPriceUnit'] = self.item_price_unit
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.last_communicate_time is not None:
            result['LastCommunicateTime'] = self.last_communicate_time
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.model is not None:
            result['Model'] = self.model
        if self.position_code is not None:
            result['PositionCode'] = self.position_code
        if self.screen_height is not None:
            result['ScreenHeight'] = self.screen_height
        if self.screen_width is not None:
            result['ScreenWidth'] = self.screen_width
        if self.shelf_code is not None:
            result['ShelfCode'] = self.shelf_code
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.type is not None:
            result['Type'] = self.type
        if self.vendor is not None:
            result['Vendor'] = self.vendor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatteryLevel') is not None:
            self.battery_level = m.get('BatteryLevel')
        if m.get('BeBind') is not None:
            self.be_bind = m.get('BeBind')
        if m.get('CompanyId') is not None:
            self.company_id = m.get('CompanyId')
        if m.get('ConnectAp') is not None:
            self.connect_ap = m.get('ConnectAp')
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('EslStatus') is not None:
            self.esl_status = m.get('EslStatus')
        if m.get('ItemActionPrice') is not None:
            self.item_action_price = m.get('ItemActionPrice')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemPriceUnit') is not None:
            self.item_price_unit = m.get('ItemPriceUnit')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('LastCommunicateTime') is not None:
            self.last_communicate_time = m.get('LastCommunicateTime')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('PositionCode') is not None:
            self.position_code = m.get('PositionCode')
        if m.get('ScreenHeight') is not None:
            self.screen_height = m.get('ScreenHeight')
        if m.get('ScreenWidth') is not None:
            self.screen_width = m.get('ScreenWidth')
        if m.get('ShelfCode') is not None:
            self.shelf_code = m.get('ShelfCode')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')
        return self


class DescribeEslDevicesResponseBodyEslDevices(TeaModel):
    def __init__(
        self,
        esl_device_info: List[DescribeEslDevicesResponseBodyEslDevicesEslDeviceInfo] = None,
    ):
        self.esl_device_info = esl_device_info

    def validate(self):
        if self.esl_device_info:
            for k in self.esl_device_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EslDeviceInfo'] = []
        if self.esl_device_info is not None:
            for k in self.esl_device_info:
                result['EslDeviceInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.esl_device_info = []
        if m.get('EslDeviceInfo') is not None:
            for k in m.get('EslDeviceInfo'):
                temp_model = DescribeEslDevicesResponseBodyEslDevicesEslDeviceInfo()
                self.esl_device_info.append(temp_model.from_map(k))
        return self


class DescribeEslDevicesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        esl_devices: DescribeEslDevicesResponseBodyEslDevices = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.esl_devices = esl_devices
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.esl_devices:
            self.esl_devices.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.esl_devices is not None:
            result['EslDevices'] = self.esl_devices.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('EslDevices') is not None:
            temp_model = DescribeEslDevicesResponseBodyEslDevices()
            self.esl_devices = temp_model.from_map(m['EslDevices'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeEslDevicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEslDevicesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeEslDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeItemsRequest(TeaModel):
    def __init__(
        self,
        be_promotion: bool = None,
        item_bar_code: str = None,
        item_id: int = None,
        item_title: str = None,
        page_number: int = None,
        page_size: int = None,
        sku_id: str = None,
        store_id: str = None,
    ):
        self.be_promotion = be_promotion
        self.item_bar_code = item_bar_code
        self.item_id = item_id
        self.item_title = item_title
        self.page_number = page_number
        self.page_size = page_size
        self.sku_id = sku_id
        # This parameter is required.
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.be_promotion is not None:
            result['BePromotion'] = self.be_promotion
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BePromotion') is not None:
            self.be_promotion = m.get('BePromotion')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class DescribeItemsResponseBodyItemsItemInfo(TeaModel):
    def __init__(
        self,
        action_price: int = None,
        be_promotion: bool = None,
        be_source_code: bool = None,
        brand_name: str = None,
        category_name: str = None,
        company_id: str = None,
        customize_feature_a: str = None,
        customize_feature_b: str = None,
        customize_feature_c: str = None,
        customize_feature_d: str = None,
        customize_feature_e: str = None,
        customize_feature_f: str = None,
        customize_feature_g: str = None,
        customize_feature_h: str = None,
        customize_feature_i: str = None,
        customize_feature_j: str = None,
        energy_efficiency: str = None,
        extra_attribute: str = None,
        forest_first_id: str = None,
        forest_second_id: str = None,
        item_bar_code: str = None,
        item_id: int = None,
        item_info_index: int = None,
        item_qr_code: str = None,
        item_short_title: str = None,
        item_title: str = None,
        member_price: int = None,
        model_number: str = None,
        option_groups: str = None,
        original_price: int = None,
        price_unit: str = None,
        production_place: str = None,
        promotion_end: str = None,
        promotion_reason: str = None,
        promotion_start: str = None,
        promotion_text: str = None,
        rank: str = None,
        sale_spec: str = None,
        sku_id: str = None,
        source_code: str = None,
        store_id: str = None,
        suggest_price: int = None,
    ):
        self.action_price = action_price
        self.be_promotion = be_promotion
        self.be_source_code = be_source_code
        self.brand_name = brand_name
        self.category_name = category_name
        self.company_id = company_id
        self.customize_feature_a = customize_feature_a
        self.customize_feature_b = customize_feature_b
        self.customize_feature_c = customize_feature_c
        self.customize_feature_d = customize_feature_d
        self.customize_feature_e = customize_feature_e
        self.customize_feature_f = customize_feature_f
        self.customize_feature_g = customize_feature_g
        self.customize_feature_h = customize_feature_h
        self.customize_feature_i = customize_feature_i
        self.customize_feature_j = customize_feature_j
        self.energy_efficiency = energy_efficiency
        self.extra_attribute = extra_attribute
        self.forest_first_id = forest_first_id
        self.forest_second_id = forest_second_id
        self.item_bar_code = item_bar_code
        self.item_id = item_id
        self.item_info_index = item_info_index
        self.item_qr_code = item_qr_code
        self.item_short_title = item_short_title
        self.item_title = item_title
        self.member_price = member_price
        self.model_number = model_number
        self.option_groups = option_groups
        self.original_price = original_price
        self.price_unit = price_unit
        self.production_place = production_place
        self.promotion_end = promotion_end
        self.promotion_reason = promotion_reason
        self.promotion_start = promotion_start
        self.promotion_text = promotion_text
        self.rank = rank
        self.sale_spec = sale_spec
        self.sku_id = sku_id
        self.source_code = source_code
        self.store_id = store_id
        self.suggest_price = suggest_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_price is not None:
            result['ActionPrice'] = self.action_price
        if self.be_promotion is not None:
            result['BePromotion'] = self.be_promotion
        if self.be_source_code is not None:
            result['BeSourceCode'] = self.be_source_code
        if self.brand_name is not None:
            result['BrandName'] = self.brand_name
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        if self.company_id is not None:
            result['CompanyId'] = self.company_id
        if self.customize_feature_a is not None:
            result['CustomizeFeatureA'] = self.customize_feature_a
        if self.customize_feature_b is not None:
            result['CustomizeFeatureB'] = self.customize_feature_b
        if self.customize_feature_c is not None:
            result['CustomizeFeatureC'] = self.customize_feature_c
        if self.customize_feature_d is not None:
            result['CustomizeFeatureD'] = self.customize_feature_d
        if self.customize_feature_e is not None:
            result['CustomizeFeatureE'] = self.customize_feature_e
        if self.customize_feature_f is not None:
            result['CustomizeFeatureF'] = self.customize_feature_f
        if self.customize_feature_g is not None:
            result['CustomizeFeatureG'] = self.customize_feature_g
        if self.customize_feature_h is not None:
            result['CustomizeFeatureH'] = self.customize_feature_h
        if self.customize_feature_i is not None:
            result['CustomizeFeatureI'] = self.customize_feature_i
        if self.customize_feature_j is not None:
            result['CustomizeFeatureJ'] = self.customize_feature_j
        if self.energy_efficiency is not None:
            result['EnergyEfficiency'] = self.energy_efficiency
        if self.extra_attribute is not None:
            result['ExtraAttribute'] = self.extra_attribute
        if self.forest_first_id is not None:
            result['ForestFirstId'] = self.forest_first_id
        if self.forest_second_id is not None:
            result['ForestSecondId'] = self.forest_second_id
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_info_index is not None:
            result['ItemInfoIndex'] = self.item_info_index
        if self.item_qr_code is not None:
            result['ItemQrCode'] = self.item_qr_code
        if self.item_short_title is not None:
            result['ItemShortTitle'] = self.item_short_title
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.member_price is not None:
            result['MemberPrice'] = self.member_price
        if self.model_number is not None:
            result['ModelNumber'] = self.model_number
        if self.option_groups is not None:
            result['OptionGroups'] = self.option_groups
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.price_unit is not None:
            result['PriceUnit'] = self.price_unit
        if self.production_place is not None:
            result['ProductionPlace'] = self.production_place
        if self.promotion_end is not None:
            result['PromotionEnd'] = self.promotion_end
        if self.promotion_reason is not None:
            result['PromotionReason'] = self.promotion_reason
        if self.promotion_start is not None:
            result['PromotionStart'] = self.promotion_start
        if self.promotion_text is not None:
            result['PromotionText'] = self.promotion_text
        if self.rank is not None:
            result['Rank'] = self.rank
        if self.sale_spec is not None:
            result['SaleSpec'] = self.sale_spec
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.source_code is not None:
            result['SourceCode'] = self.source_code
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.suggest_price is not None:
            result['SuggestPrice'] = self.suggest_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionPrice') is not None:
            self.action_price = m.get('ActionPrice')
        if m.get('BePromotion') is not None:
            self.be_promotion = m.get('BePromotion')
        if m.get('BeSourceCode') is not None:
            self.be_source_code = m.get('BeSourceCode')
        if m.get('BrandName') is not None:
            self.brand_name = m.get('BrandName')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        if m.get('CompanyId') is not None:
            self.company_id = m.get('CompanyId')
        if m.get('CustomizeFeatureA') is not None:
            self.customize_feature_a = m.get('CustomizeFeatureA')
        if m.get('CustomizeFeatureB') is not None:
            self.customize_feature_b = m.get('CustomizeFeatureB')
        if m.get('CustomizeFeatureC') is not None:
            self.customize_feature_c = m.get('CustomizeFeatureC')
        if m.get('CustomizeFeatureD') is not None:
            self.customize_feature_d = m.get('CustomizeFeatureD')
        if m.get('CustomizeFeatureE') is not None:
            self.customize_feature_e = m.get('CustomizeFeatureE')
        if m.get('CustomizeFeatureF') is not None:
            self.customize_feature_f = m.get('CustomizeFeatureF')
        if m.get('CustomizeFeatureG') is not None:
            self.customize_feature_g = m.get('CustomizeFeatureG')
        if m.get('CustomizeFeatureH') is not None:
            self.customize_feature_h = m.get('CustomizeFeatureH')
        if m.get('CustomizeFeatureI') is not None:
            self.customize_feature_i = m.get('CustomizeFeatureI')
        if m.get('CustomizeFeatureJ') is not None:
            self.customize_feature_j = m.get('CustomizeFeatureJ')
        if m.get('EnergyEfficiency') is not None:
            self.energy_efficiency = m.get('EnergyEfficiency')
        if m.get('ExtraAttribute') is not None:
            self.extra_attribute = m.get('ExtraAttribute')
        if m.get('ForestFirstId') is not None:
            self.forest_first_id = m.get('ForestFirstId')
        if m.get('ForestSecondId') is not None:
            self.forest_second_id = m.get('ForestSecondId')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemInfoIndex') is not None:
            self.item_info_index = m.get('ItemInfoIndex')
        if m.get('ItemQrCode') is not None:
            self.item_qr_code = m.get('ItemQrCode')
        if m.get('ItemShortTitle') is not None:
            self.item_short_title = m.get('ItemShortTitle')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('MemberPrice') is not None:
            self.member_price = m.get('MemberPrice')
        if m.get('ModelNumber') is not None:
            self.model_number = m.get('ModelNumber')
        if m.get('OptionGroups') is not None:
            self.option_groups = m.get('OptionGroups')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('PriceUnit') is not None:
            self.price_unit = m.get('PriceUnit')
        if m.get('ProductionPlace') is not None:
            self.production_place = m.get('ProductionPlace')
        if m.get('PromotionEnd') is not None:
            self.promotion_end = m.get('PromotionEnd')
        if m.get('PromotionReason') is not None:
            self.promotion_reason = m.get('PromotionReason')
        if m.get('PromotionStart') is not None:
            self.promotion_start = m.get('PromotionStart')
        if m.get('PromotionText') is not None:
            self.promotion_text = m.get('PromotionText')
        if m.get('Rank') is not None:
            self.rank = m.get('Rank')
        if m.get('SaleSpec') is not None:
            self.sale_spec = m.get('SaleSpec')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('SuggestPrice') is not None:
            self.suggest_price = m.get('SuggestPrice')
        return self


class DescribeItemsResponseBodyItems(TeaModel):
    def __init__(
        self,
        item_info: List[DescribeItemsResponseBodyItemsItemInfo] = None,
    ):
        self.item_info = item_info

    def validate(self):
        if self.item_info:
            for k in self.item_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ItemInfo'] = []
        if self.item_info is not None:
            for k in self.item_info:
                result['ItemInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item_info = []
        if m.get('ItemInfo') is not None:
            for k in m.get('ItemInfo'):
                temp_model = DescribeItemsResponseBodyItemsItemInfo()
                self.item_info.append(temp_model.from_map(k))
        return self


class DescribeItemsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        items: DescribeItemsResponseBodyItems = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.items = items
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Items') is not None:
            temp_model = DescribeItemsResponseBodyItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeItemsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLogisticsRequest(TeaModel):
    def __init__(
        self,
        order_id: str = None,
    ):
        # This parameter is required.
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class DescribeLogisticsResponseBodyLogisticsLogisticsInfo(TeaModel):
    def __init__(
        self,
        accept_status: bool = None,
        ap_mac_list: str = None,
        description: str = None,
        esl_mac_list: str = None,
        has_send: str = None,
        logistics_documents: str = None,
        order_id: str = None,
        po_number: str = None,
        pr_number: str = None,
    ):
        self.accept_status = accept_status
        self.ap_mac_list = ap_mac_list
        self.description = description
        self.esl_mac_list = esl_mac_list
        self.has_send = has_send
        self.logistics_documents = logistics_documents
        self.order_id = order_id
        self.po_number = po_number
        self.pr_number = pr_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_status is not None:
            result['AcceptStatus'] = self.accept_status
        if self.ap_mac_list is not None:
            result['ApMacList'] = self.ap_mac_list
        if self.description is not None:
            result['Description'] = self.description
        if self.esl_mac_list is not None:
            result['EslMacList'] = self.esl_mac_list
        if self.has_send is not None:
            result['HasSend'] = self.has_send
        if self.logistics_documents is not None:
            result['LogisticsDocuments'] = self.logistics_documents
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.po_number is not None:
            result['PoNumber'] = self.po_number
        if self.pr_number is not None:
            result['PrNumber'] = self.pr_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptStatus') is not None:
            self.accept_status = m.get('AcceptStatus')
        if m.get('ApMacList') is not None:
            self.ap_mac_list = m.get('ApMacList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EslMacList') is not None:
            self.esl_mac_list = m.get('EslMacList')
        if m.get('HasSend') is not None:
            self.has_send = m.get('HasSend')
        if m.get('LogisticsDocuments') is not None:
            self.logistics_documents = m.get('LogisticsDocuments')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PoNumber') is not None:
            self.po_number = m.get('PoNumber')
        if m.get('PrNumber') is not None:
            self.pr_number = m.get('PrNumber')
        return self


class DescribeLogisticsResponseBodyLogistics(TeaModel):
    def __init__(
        self,
        logistics_info: List[DescribeLogisticsResponseBodyLogisticsLogisticsInfo] = None,
    ):
        self.logistics_info = logistics_info

    def validate(self):
        if self.logistics_info:
            for k in self.logistics_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LogisticsInfo'] = []
        if self.logistics_info is not None:
            for k in self.logistics_info:
                result['LogisticsInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.logistics_info = []
        if m.get('LogisticsInfo') is not None:
            for k in m.get('LogisticsInfo'):
                temp_model = DescribeLogisticsResponseBodyLogisticsLogisticsInfo()
                self.logistics_info.append(temp_model.from_map(k))
        return self


class DescribeLogisticsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        logistics: DescribeLogisticsResponseBodyLogistics = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.logistics = logistics
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.logistics:
            self.logistics.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.logistics is not None:
            result['Logistics'] = self.logistics.to_map()
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Logistics') is not None:
            temp_model = DescribeLogisticsResponseBodyLogistics()
            self.logistics = temp_model.from_map(m['Logistics'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeLogisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeLogisticsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeLogisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePayOrdersRequest(TeaModel):
    def __init__(
        self,
        from_date: str = None,
        order_id: str = None,
        page_number: int = None,
        page_size: int = None,
        to_date: str = None,
    ):
        self.from_date = from_date
        self.order_id = order_id
        self.page_number = page_number
        self.page_size = page_size
        self.to_date = to_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_date is not None:
            result['FromDate'] = self.from_date
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.to_date is not None:
            result['ToDate'] = self.to_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromDate') is not None:
            self.from_date = m.get('FromDate')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ToDate') is not None:
            self.to_date = m.get('ToDate')
        return self


class DescribePayOrdersResponseBodyPayOrdersPayOrderInfo(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        commodity_name: str = None,
        detail_name: str = None,
        gmt_create: str = None,
        gmt_pay: str = None,
        is_accepted: bool = None,
        order_id: str = None,
        order_status: str = None,
        order_type: str = None,
        original_amount: float = None,
        pay_amount: float = None,
        quantity: int = None,
    ):
        self.commodity_code = commodity_code
        self.commodity_name = commodity_name
        self.detail_name = detail_name
        self.gmt_create = gmt_create
        self.gmt_pay = gmt_pay
        self.is_accepted = is_accepted
        self.order_id = order_id
        self.order_status = order_status
        self.order_type = order_type
        self.original_amount = original_amount
        self.pay_amount = pay_amount
        self.quantity = quantity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.commodity_name is not None:
            result['CommodityName'] = self.commodity_name
        if self.detail_name is not None:
            result['DetailName'] = self.detail_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_pay is not None:
            result['GmtPay'] = self.gmt_pay
        if self.is_accepted is not None:
            result['IsAccepted'] = self.is_accepted
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        if self.pay_amount is not None:
            result['PayAmount'] = self.pay_amount
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CommodityName') is not None:
            self.commodity_name = m.get('CommodityName')
        if m.get('DetailName') is not None:
            self.detail_name = m.get('DetailName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtPay') is not None:
            self.gmt_pay = m.get('GmtPay')
        if m.get('IsAccepted') is not None:
            self.is_accepted = m.get('IsAccepted')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        if m.get('PayAmount') is not None:
            self.pay_amount = m.get('PayAmount')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        return self


class DescribePayOrdersResponseBodyPayOrders(TeaModel):
    def __init__(
        self,
        pay_order_info: List[DescribePayOrdersResponseBodyPayOrdersPayOrderInfo] = None,
    ):
        self.pay_order_info = pay_order_info

    def validate(self):
        if self.pay_order_info:
            for k in self.pay_order_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PayOrderInfo'] = []
        if self.pay_order_info is not None:
            for k in self.pay_order_info:
                result['PayOrderInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pay_order_info = []
        if m.get('PayOrderInfo') is not None:
            for k in m.get('PayOrderInfo'):
                temp_model = DescribePayOrdersResponseBodyPayOrdersPayOrderInfo()
                self.pay_order_info.append(temp_model.from_map(k))
        return self


class DescribePayOrdersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        pay_orders: DescribePayOrdersResponseBodyPayOrders = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.pay_orders = pay_orders
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.pay_orders:
            self.pay_orders.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pay_orders is not None:
            result['PayOrders'] = self.pay_orders.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PayOrders') is not None:
            temp_model = DescribePayOrdersResponseBodyPayOrders()
            self.pay_orders = temp_model.from_map(m['PayOrders'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePayOrdersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePayOrdersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribePayOrdersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePlanogramRailsRequest(TeaModel):
    def __init__(
        self,
        layer: str = None,
        page_number: int = None,
        page_size: int = None,
        rail_code: str = None,
        shelf: str = None,
        store_id: str = None,
    ):
        self.layer = layer
        self.page_number = page_number
        self.page_size = page_size
        self.rail_code = rail_code
        self.shelf = shelf
        # This parameter is required.
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.layer is not None:
            result['Layer'] = self.layer
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.rail_code is not None:
            result['RailCode'] = self.rail_code
        if self.shelf is not None:
            result['Shelf'] = self.shelf
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RailCode') is not None:
            self.rail_code = m.get('RailCode')
        if m.get('Shelf') is not None:
            self.shelf = m.get('Shelf')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class DescribePlanogramRailsResponseBodyPlanogramRailInfos(TeaModel):
    def __init__(
        self,
        gap_unit: int = None,
        layer: str = None,
        rail_code: str = None,
        shelf: str = None,
    ):
        self.gap_unit = gap_unit
        self.layer = layer
        self.rail_code = rail_code
        self.shelf = shelf

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gap_unit is not None:
            result['GapUnit'] = self.gap_unit
        if self.layer is not None:
            result['Layer'] = self.layer
        if self.rail_code is not None:
            result['RailCode'] = self.rail_code
        if self.shelf is not None:
            result['Shelf'] = self.shelf
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GapUnit') is not None:
            self.gap_unit = m.get('GapUnit')
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        if m.get('RailCode') is not None:
            self.rail_code = m.get('RailCode')
        if m.get('Shelf') is not None:
            self.shelf = m.get('Shelf')
        return self


class DescribePlanogramRailsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        planogram_rail_infos: List[DescribePlanogramRailsResponseBodyPlanogramRailInfos] = None,
        request_id: str = None,
        store_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.planogram_rail_infos = planogram_rail_infos
        self.request_id = request_id
        self.store_id = store_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.planogram_rail_infos:
            for k in self.planogram_rail_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['PlanogramRailInfos'] = []
        if self.planogram_rail_infos is not None:
            for k in self.planogram_rail_infos:
                result['PlanogramRailInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.planogram_rail_infos = []
        if m.get('PlanogramRailInfos') is not None:
            for k in m.get('PlanogramRailInfos'):
                temp_model = DescribePlanogramRailsResponseBodyPlanogramRailInfos()
                self.planogram_rail_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePlanogramRailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePlanogramRailsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribePlanogramRailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeStoresRequest(TeaModel):
    def __init__(
        self,
        brand: str = None,
        company_id: str = None,
        from_date: str = None,
        page_number: int = None,
        page_size: int = None,
        store_id: str = None,
        store_name: str = None,
        to_date: str = None,
    ):
        self.brand = brand
        self.company_id = company_id
        self.from_date = from_date
        self.page_number = page_number
        self.page_size = page_size
        self.store_id = store_id
        self.store_name = store_name
        self.to_date = to_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.brand is not None:
            result['Brand'] = self.brand
        if self.company_id is not None:
            result['CompanyId'] = self.company_id
        if self.from_date is not None:
            result['FromDate'] = self.from_date
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        if self.to_date is not None:
            result['ToDate'] = self.to_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Brand') is not None:
            self.brand = m.get('Brand')
        if m.get('CompanyId') is not None:
            self.company_id = m.get('CompanyId')
        if m.get('FromDate') is not None:
            self.from_date = m.get('FromDate')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        if m.get('ToDate') is not None:
            self.to_date = m.get('ToDate')
        return self


class DescribeStoresResponseBodyStoresStoreInfo(TeaModel):
    def __init__(
        self,
        brand: str = None,
        comments: str = None,
        company_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        groups: str = None,
        level: str = None,
        out_id: str = None,
        parent_id: str = None,
        phone: str = None,
        store_id: str = None,
        store_name: str = None,
    ):
        self.brand = brand
        self.comments = comments
        self.company_id = company_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.groups = groups
        self.level = level
        self.out_id = out_id
        self.parent_id = parent_id
        self.phone = phone
        self.store_id = store_id
        self.store_name = store_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.brand is not None:
            result['Brand'] = self.brand
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.company_id is not None:
            result['CompanyId'] = self.company_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.groups is not None:
            result['Groups'] = self.groups
        if self.level is not None:
            result['Level'] = self.level
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Brand') is not None:
            self.brand = m.get('Brand')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('CompanyId') is not None:
            self.company_id = m.get('CompanyId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Groups') is not None:
            self.groups = m.get('Groups')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        return self


class DescribeStoresResponseBodyStores(TeaModel):
    def __init__(
        self,
        store_info: List[DescribeStoresResponseBodyStoresStoreInfo] = None,
    ):
        self.store_info = store_info

    def validate(self):
        if self.store_info:
            for k in self.store_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['StoreInfo'] = []
        if self.store_info is not None:
            for k in self.store_info:
                result['StoreInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.store_info = []
        if m.get('StoreInfo') is not None:
            for k in m.get('StoreInfo'):
                temp_model = DescribeStoresResponseBodyStoresStoreInfo()
                self.store_info.append(temp_model.from_map(k))
        return self


class DescribeStoresResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        stores: DescribeStoresResponseBodyStores = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.stores = stores
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.stores:
            self.stores.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.stores is not None:
            result['Stores'] = self.stores.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Stores') is not None:
            temp_model = DescribeStoresResponseBodyStores()
            self.stores = temp_model.from_map(m['Stores'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeStoresResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeStoresResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeStoresResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserLogRequest(TeaModel):
    def __init__(
        self,
        esl_bar_code: str = None,
        from_date: str = None,
        item_bar_code: str = None,
        item_id: int = None,
        item_title: str = None,
        operate_status: str = None,
        operate_type: str = None,
        operate_user_id: int = None,
        page_number: int = None,
        page_size: int = None,
        reverse: bool = None,
        store_id: str = None,
        to_date: str = None,
    ):
        self.esl_bar_code = esl_bar_code
        self.from_date = from_date
        self.item_bar_code = item_bar_code
        self.item_id = item_id
        self.item_title = item_title
        self.operate_status = operate_status
        self.operate_type = operate_type
        self.operate_user_id = operate_user_id
        self.page_number = page_number
        self.page_size = page_size
        self.reverse = reverse
        # This parameter is required.
        self.store_id = store_id
        self.to_date = to_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.from_date is not None:
            result['FromDate'] = self.from_date
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.operate_status is not None:
            result['OperateStatus'] = self.operate_status
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.operate_user_id is not None:
            result['OperateUserId'] = self.operate_user_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.to_date is not None:
            result['ToDate'] = self.to_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('FromDate') is not None:
            self.from_date = m.get('FromDate')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('OperateStatus') is not None:
            self.operate_status = m.get('OperateStatus')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('OperateUserId') is not None:
            self.operate_user_id = m.get('OperateUserId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('ToDate') is not None:
            self.to_date = m.get('ToDate')
        return self


class DescribeUserLogResponseBodyUserLogsUserLogInfo(TeaModel):
    def __init__(
        self,
        esl_bar_code: str = None,
        item_action_price: int = None,
        item_bar_code: str = None,
        item_id: int = None,
        item_title: str = None,
        mac: str = None,
        operate_status: str = None,
        operate_time: str = None,
        operate_type: str = None,
        operate_user_id: int = None,
        shelf_code: str = None,
        store_id: str = None,
    ):
        self.esl_bar_code = esl_bar_code
        self.item_action_price = item_action_price
        self.item_bar_code = item_bar_code
        self.item_id = item_id
        self.item_title = item_title
        self.mac = mac
        self.operate_status = operate_status
        self.operate_time = operate_time
        self.operate_type = operate_type
        self.operate_user_id = operate_user_id
        self.shelf_code = shelf_code
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.item_action_price is not None:
            result['ItemActionPrice'] = self.item_action_price
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_title is not None:
            result['ItemTitle'] = self.item_title
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.operate_status is not None:
            result['OperateStatus'] = self.operate_status
        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.operate_user_id is not None:
            result['OperateUserId'] = self.operate_user_id
        if self.shelf_code is not None:
            result['ShelfCode'] = self.shelf_code
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('ItemActionPrice') is not None:
            self.item_action_price = m.get('ItemActionPrice')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemTitle') is not None:
            self.item_title = m.get('ItemTitle')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('OperateStatus') is not None:
            self.operate_status = m.get('OperateStatus')
        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('OperateUserId') is not None:
            self.operate_user_id = m.get('OperateUserId')
        if m.get('ShelfCode') is not None:
            self.shelf_code = m.get('ShelfCode')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class DescribeUserLogResponseBodyUserLogs(TeaModel):
    def __init__(
        self,
        user_log_info: List[DescribeUserLogResponseBodyUserLogsUserLogInfo] = None,
    ):
        self.user_log_info = user_log_info

    def validate(self):
        if self.user_log_info:
            for k in self.user_log_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UserLogInfo'] = []
        if self.user_log_info is not None:
            for k in self.user_log_info:
                result['UserLogInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_log_info = []
        if m.get('UserLogInfo') is not None:
            for k in m.get('UserLogInfo'):
                temp_model = DescribeUserLogResponseBodyUserLogsUserLogInfo()
                self.user_log_info.append(temp_model.from_map(k))
        return self


class DescribeUserLogResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        user_logs: DescribeUserLogResponseBodyUserLogs = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.user_logs = user_logs

    def validate(self):
        if self.user_logs:
            self.user_logs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.user_logs is not None:
            result['UserLogs'] = self.user_logs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('UserLogs') is not None:
            temp_model = DescribeUserLogResponseBodyUserLogs()
            self.user_logs = temp_model.from_map(m['UserLogs'])
        return self


class DescribeUserLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUserLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeUserLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUsersRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        user_id: str = None,
        user_name: str = None,
        user_type: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.user_id = user_id
        self.user_name = user_name
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class DescribeUsersResponseBodyUsersUserInfo(TeaModel):
    def __init__(
        self,
        stores: str = None,
        user_id: str = None,
        user_name: str = None,
        user_type: str = None,
    ):
        self.stores = stores
        self.user_id = user_id
        self.user_name = user_name
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stores is not None:
            result['Stores'] = self.stores
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Stores') is not None:
            self.stores = m.get('Stores')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class DescribeUsersResponseBodyUsers(TeaModel):
    def __init__(
        self,
        user_info: List[DescribeUsersResponseBodyUsersUserInfo] = None,
    ):
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            for k in self.user_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UserInfo'] = []
        if self.user_info is not None:
            for k in self.user_info:
                result['UserInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_info = []
        if m.get('UserInfo') is not None:
            for k in m.get('UserInfo'):
                temp_model = DescribeUsersResponseBodyUsersUserInfo()
                self.user_info.append(temp_model.from_map(k))
        return self


class DescribeUsersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        users: DescribeUsersResponseBodyUsers = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.users = users

    def validate(self):
        if self.users:
            self.users.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.users is not None:
            result['Users'] = self.users.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Users') is not None:
            temp_model = DescribeUsersResponseBodyUsers()
            self.users = temp_model.from_map(m['Users'])
        return self


class DescribeUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUsersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCompanyResponseBody(TeaModel):
    def __init__(
        self,
        bid: int = None,
        code: str = None,
        company_id: str = None,
        company_type: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        owner_id: int = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.bid = bid
        self.code = code
        self.company_id = company_id
        self.company_type = company_type
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.owner_id = owner_id
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.code is not None:
            result['Code'] = self.code
        if self.company_id is not None:
            result['CompanyId'] = self.company_id
        if self.company_type is not None:
            result['CompanyType'] = self.company_type
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CompanyId') is not None:
            self.company_id = m.get('CompanyId')
        if m.get('CompanyType') is not None:
            self.company_type = m.get('CompanyType')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCompanyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCompanyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetCompanyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetUserResponseBodyUser(TeaModel):
    def __init__(
        self,
        stores: str = None,
        user_id: str = None,
        user_name: str = None,
        user_type: str = None,
    ):
        self.stores = stores
        self.user_id = user_id
        self.user_name = user_name
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stores is not None:
            result['Stores'] = self.stores
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Stores') is not None:
            self.stores = m.get('Stores')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        user: GetUserResponseBodyUser = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.success = success
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('User') is not None:
            temp_model = GetUserResponseBodyUser()
            self.user = temp_model.from_map(m['User'])
        return self


class GetUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MapPlanogramRailRequest(TeaModel):
    def __init__(
        self,
        layer: str = None,
        rail_code: str = None,
        shelf: str = None,
        store_id: str = None,
    ):
        # This parameter is required.
        self.layer = layer
        # This parameter is required.
        self.rail_code = rail_code
        # This parameter is required.
        self.shelf = shelf
        # This parameter is required.
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.layer is not None:
            result['Layer'] = self.layer
        if self.rail_code is not None:
            result['RailCode'] = self.rail_code
        if self.shelf is not None:
            result['Shelf'] = self.shelf
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Layer') is not None:
            self.layer = m.get('Layer')
        if m.get('RailCode') is not None:
            self.rail_code = m.get('RailCode')
        if m.get('Shelf') is not None:
            self.shelf = m.get('Shelf')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class MapPlanogramRailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class MapPlanogramRailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MapPlanogramRailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = MapPlanogramRailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshTaobaoItemRequest(TeaModel):
    def __init__(
        self,
        outer_id: str = None,
        sku_id: str = None,
        store_id: str = None,
        taobao_item_id: str = None,
    ):
        self.outer_id = outer_id
        self.sku_id = sku_id
        # This parameter is required.
        self.store_id = store_id
        self.taobao_item_id = taobao_item_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outer_id is not None:
            result['OuterId'] = self.outer_id
        if self.sku_id is not None:
            result['SkuId'] = self.sku_id
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.taobao_item_id is not None:
            result['TaobaoItemId'] = self.taobao_item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OuterId') is not None:
            self.outer_id = m.get('OuterId')
        if m.get('SkuId') is not None:
            self.sku_id = m.get('SkuId')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('TaobaoItemId') is not None:
            self.taobao_item_id = m.get('TaobaoItemId')
        return self


class RefreshTaobaoItemResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RefreshTaobaoItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefreshTaobaoItemResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RefreshTaobaoItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnassignUserRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UnassignUserResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnassignUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnassignUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UnassignUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindEslDeviceRequest(TeaModel):
    def __init__(
        self,
        esl_bar_code: str = None,
        item_bar_code: str = None,
        store_id: str = None,
    ):
        # This parameter is required.
        self.esl_bar_code = esl_bar_code
        self.item_bar_code = item_bar_code
        # This parameter is required.
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class UnbindEslDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnbindEslDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindEslDeviceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UnbindEslDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindEslDeviceShelfRequest(TeaModel):
    def __init__(
        self,
        esl_bar_code: str = None,
        store_id: str = None,
    ):
        self.esl_bar_code = esl_bar_code
        # This parameter is required.
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class UnbindEslDeviceShelfResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnbindEslDeviceShelfResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindEslDeviceShelfResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UnbindEslDeviceShelfResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnmapPlanogramRailRequest(TeaModel):
    def __init__(
        self,
        rail_code: str = None,
        store_id: str = None,
    ):
        # This parameter is required.
        self.rail_code = rail_code
        # This parameter is required.
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rail_code is not None:
            result['RailCode'] = self.rail_code
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RailCode') is not None:
            self.rail_code = m.get('RailCode')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class UnmapPlanogramRailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnmapPlanogramRailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnmapPlanogramRailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UnmapPlanogramRailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEslDeviceLightRequest(TeaModel):
    def __init__(
        self,
        esl_bar_code: str = None,
        frequency: str = None,
        item_bar_code: str = None,
        led_color: str = None,
        light_up_time: int = None,
        store_id: str = None,
    ):
        self.esl_bar_code = esl_bar_code
        # This parameter is required.
        self.frequency = frequency
        self.item_bar_code = item_bar_code
        # This parameter is required.
        self.led_color = led_color
        # This parameter is required.
        self.light_up_time = light_up_time
        # This parameter is required.
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.esl_bar_code is not None:
            result['EslBarCode'] = self.esl_bar_code
        if self.frequency is not None:
            result['Frequency'] = self.frequency
        if self.item_bar_code is not None:
            result['ItemBarCode'] = self.item_bar_code
        if self.led_color is not None:
            result['LedColor'] = self.led_color
        if self.light_up_time is not None:
            result['LightUpTime'] = self.light_up_time
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EslBarCode') is not None:
            self.esl_bar_code = m.get('EslBarCode')
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')
        if m.get('ItemBarCode') is not None:
            self.item_bar_code = m.get('ItemBarCode')
        if m.get('LedColor') is not None:
            self.led_color = m.get('LedColor')
        if m.get('LightUpTime') is not None:
            self.light_up_time = m.get('LightUpTime')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class UpdateEslDeviceLightResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        fail_count: int = None,
        fail_esl_bar_codes: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        success_count: int = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.fail_count = fail_count
        self.fail_esl_bar_codes = fail_esl_bar_codes
        self.message = message
        self.request_id = request_id
        self.success = success
        self.success_count = success_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        if self.fail_esl_bar_codes is not None:
            result['FailEslBarCodes'] = self.fail_esl_bar_codes
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        if m.get('FailEslBarCodes') is not None:
            self.fail_esl_bar_codes = m.get('FailEslBarCodes')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        return self


class UpdateEslDeviceLightResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateEslDeviceLightResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateEslDeviceLightResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateStoreRequest(TeaModel):
    def __init__(
        self,
        brand: str = None,
        comments: str = None,
        groups: str = None,
        out_id: str = None,
        phone: str = None,
        store_id: str = None,
        store_name: str = None,
    ):
        self.brand = brand
        self.comments = comments
        self.groups = groups
        self.out_id = out_id
        self.phone = phone
        # This parameter is required.
        self.store_id = store_id
        self.store_name = store_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.brand is not None:
            result['Brand'] = self.brand
        if self.comments is not None:
            result['Comments'] = self.comments
        if self.groups is not None:
            result['Groups'] = self.groups
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.store_name is not None:
            result['StoreName'] = self.store_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Brand') is not None:
            self.brand = m.get('Brand')
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')
        if m.get('Groups') is not None:
            self.groups = m.get('Groups')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('StoreName') is not None:
            self.store_name = m.get('StoreName')
        return self


class UpdateStoreResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_code: str = None,
        error_message: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dynamic_code = dynamic_code
        self.dynamic_message = dynamic_message
        self.error_code = error_code
        self.error_message = error_message
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code
        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')
        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateStoreResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateStoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


