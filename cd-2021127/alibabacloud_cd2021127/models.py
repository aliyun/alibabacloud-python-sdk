# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AddProductImageRequestProductImageList(TeaModel):
    def __init__(
        self,
        product_image_cutout: bool = None,
        product_image_id: str = None,
        product_image_labels: List[str] = None,
        product_image_type: str = None,
        product_image_url: str = None,
    ):
        self.product_image_cutout = product_image_cutout
        self.product_image_id = product_image_id
        self.product_image_labels = product_image_labels
        self.product_image_type = product_image_type
        # This parameter is required.
        self.product_image_url = product_image_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_image_cutout is not None:
            result['ProductImageCutout'] = self.product_image_cutout
        if self.product_image_id is not None:
            result['ProductImageId'] = self.product_image_id
        if self.product_image_labels is not None:
            result['ProductImageLabels'] = self.product_image_labels
        if self.product_image_type is not None:
            result['ProductImageType'] = self.product_image_type
        if self.product_image_url is not None:
            result['ProductImageUrl'] = self.product_image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductImageCutout') is not None:
            self.product_image_cutout = m.get('ProductImageCutout')
        if m.get('ProductImageId') is not None:
            self.product_image_id = m.get('ProductImageId')
        if m.get('ProductImageLabels') is not None:
            self.product_image_labels = m.get('ProductImageLabels')
        if m.get('ProductImageType') is not None:
            self.product_image_type = m.get('ProductImageType')
        if m.get('ProductImageUrl') is not None:
            self.product_image_url = m.get('ProductImageUrl')
        return self


class AddProductImageRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        product_id: str = None,
        product_image_list: List[AddProductImageRequestProductImageList] = None,
        product_name: str = None,
    ):
        self.country = country
        # This parameter is required.
        self.product_id = product_id
        # This parameter is required.
        self.product_image_list = product_image_list
        self.product_name = product_name

    def validate(self):
        if self.product_image_list:
            for k in self.product_image_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        result['ProductImageList'] = []
        if self.product_image_list is not None:
            for k in self.product_image_list:
                result['ProductImageList'].append(k.to_map() if k else None)
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        self.product_image_list = []
        if m.get('ProductImageList') is not None:
            for k in m.get('ProductImageList'):
                temp_model = AddProductImageRequestProductImageList()
                self.product_image_list.append(temp_model.from_map(k))
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        return self


class AddProductImageShrinkRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        product_id: str = None,
        product_image_list_shrink: str = None,
        product_name: str = None,
    ):
        self.country = country
        # This parameter is required.
        self.product_id = product_id
        # This parameter is required.
        self.product_image_list_shrink = product_image_list_shrink
        self.product_name = product_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_image_list_shrink is not None:
            result['ProductImageList'] = self.product_image_list_shrink
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductImageList') is not None:
            self.product_image_list_shrink = m.get('ProductImageList')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        return self


class AddProductImageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddProductImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddProductImageResponseBody = None,
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
            temp_model = AddProductImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddShopToGroupRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        shop_group_id: str = None,
        shop_id_list: List[str] = None,
    ):
        self.country = country
        # This parameter is required.
        self.shop_group_id = shop_group_id
        self.shop_id_list = shop_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.shop_group_id is not None:
            result['ShopGroupId'] = self.shop_group_id
        if self.shop_id_list is not None:
            result['ShopIdList'] = self.shop_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('ShopGroupId') is not None:
            self.shop_group_id = m.get('ShopGroupId')
        if m.get('ShopIdList') is not None:
            self.shop_id_list = m.get('ShopIdList')
        return self


class AddShopToGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        shop_group_id: str = None,
        shop_id_list_shrink: str = None,
    ):
        self.country = country
        # This parameter is required.
        self.shop_group_id = shop_group_id
        self.shop_id_list_shrink = shop_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.shop_group_id is not None:
            result['ShopGroupId'] = self.shop_group_id
        if self.shop_id_list_shrink is not None:
            result['ShopIdList'] = self.shop_id_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('ShopGroupId') is not None:
            self.shop_group_id = m.get('ShopGroupId')
        if m.get('ShopIdList') is not None:
            self.shop_id_list_shrink = m.get('ShopIdList')
        return self


class AddShopToGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddShopToGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddShopToGroupResponseBody = None,
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
            temp_model = AddShopToGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddShopsToGroupRequest(TeaModel):
    def __init__(
        self,
        shop_group_id: str = None,
        shop_id_list: List[str] = None,
    ):
        # This parameter is required.
        self.shop_group_id = shop_group_id
        # This parameter is required.
        self.shop_id_list = shop_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.shop_group_id is not None:
            result['ShopGroupId'] = self.shop_group_id
        if self.shop_id_list is not None:
            result['ShopIdList'] = self.shop_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShopGroupId') is not None:
            self.shop_group_id = m.get('ShopGroupId')
        if m.get('ShopIdList') is not None:
            self.shop_id_list = m.get('ShopIdList')
        return self


class AddShopsToGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        shop_group_id: str = None,
        shop_id_list_shrink: str = None,
    ):
        # This parameter is required.
        self.shop_group_id = shop_group_id
        # This parameter is required.
        self.shop_id_list_shrink = shop_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.shop_group_id is not None:
            result['ShopGroupId'] = self.shop_group_id
        if self.shop_id_list_shrink is not None:
            result['ShopIdList'] = self.shop_id_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShopGroupId') is not None:
            self.shop_group_id = m.get('ShopGroupId')
        if m.get('ShopIdList') is not None:
            self.shop_id_list_shrink = m.get('ShopIdList')
        return self


class AddShopsToGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        shop_id: str = None,
    ):
        self.code = code
        self.message = message
        self.shop_id = shop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.shop_id is not None:
            result['ShopId'] = self.shop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ShopId') is not None:
            self.shop_id = m.get('ShopId')
        return self


class AddShopsToGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[AddShopsToGroupResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AddShopsToGroupResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddShopsToGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddShopsToGroupResponseBody = None,
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
            temp_model = AddShopsToGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BaiLianSseChatRequestInputBizParamsImages(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class BaiLianSseChatRequestInputBizParams(TeaModel):
    def __init__(
        self,
        images: List[BaiLianSseChatRequestInputBizParamsImages] = None,
    ):
        self.images = images

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = BaiLianSseChatRequestInputBizParamsImages()
                self.images.append(temp_model.from_map(k))
        return self


class BaiLianSseChatRequestInput(TeaModel):
    def __init__(
        self,
        biz_params: BaiLianSseChatRequestInputBizParams = None,
        prompt: str = None,
        request_id: str = None,
        session_id: str = None,
    ):
        self.biz_params = biz_params
        self.prompt = prompt
        self.request_id = request_id
        self.session_id = session_id

    def validate(self):
        if self.biz_params:
            self.biz_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_params is not None:
            result['BizParams'] = self.biz_params.to_map()
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizParams') is not None:
            temp_model = BaiLianSseChatRequestInputBizParams()
            self.biz_params = temp_model.from_map(m['BizParams'])
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class BaiLianSseChatRequestParameters(TeaModel):
    def __init__(
        self,
        incremental_output: bool = None,
        vendor_id: str = None,
    ):
        self.incremental_output = incremental_output
        self.vendor_id = vendor_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.incremental_output is not None:
            result['Incremental_output'] = self.incremental_output
        if self.vendor_id is not None:
            result['vendorId'] = self.vendor_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Incremental_output') is not None:
            self.incremental_output = m.get('Incremental_output')
        if m.get('vendorId') is not None:
            self.vendor_id = m.get('vendorId')
        return self


class BaiLianSseChatRequest(TeaModel):
    def __init__(
        self,
        input: BaiLianSseChatRequestInput = None,
        parameters: BaiLianSseChatRequestParameters = None,
    ):
        self.input = input
        self.parameters = parameters

    def validate(self):
        if self.input:
            self.input.validate()
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input is not None:
            result['Input'] = self.input.to_map()
        if self.parameters is not None:
            result['Parameters'] = self.parameters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Input') is not None:
            temp_model = BaiLianSseChatRequestInput()
            self.input = temp_model.from_map(m['Input'])
        if m.get('Parameters') is not None:
            temp_model = BaiLianSseChatRequestParameters()
            self.parameters = temp_model.from_map(m['Parameters'])
        return self


class BaiLianSseChatShrinkRequest(TeaModel):
    def __init__(
        self,
        input_shrink: str = None,
        parameters_shrink: str = None,
    ):
        self.input_shrink = input_shrink
        self.parameters_shrink = parameters_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_shrink is not None:
            result['Input'] = self.input_shrink
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Input') is not None:
            self.input_shrink = m.get('Input')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        return self


class BaiLianSseChatResponseBodyDataOutputChoicesMessage(TeaModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        self.content = content
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class BaiLianSseChatResponseBodyDataOutputChoices(TeaModel):
    def __init__(
        self,
        finish_reason: str = None,
        message: BaiLianSseChatResponseBodyDataOutputChoicesMessage = None,
    ):
        self.finish_reason = finish_reason
        self.message = message

    def validate(self):
        if self.message:
            self.message.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_reason is not None:
            result['FinishReason'] = self.finish_reason
        if self.message is not None:
            result['Message'] = self.message.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishReason') is not None:
            self.finish_reason = m.get('FinishReason')
        if m.get('Message') is not None:
            temp_model = BaiLianSseChatResponseBodyDataOutputChoicesMessage()
            self.message = temp_model.from_map(m['Message'])
        return self


class BaiLianSseChatResponseBodyDataOutput(TeaModel):
    def __init__(
        self,
        choices: List[BaiLianSseChatResponseBodyDataOutputChoices] = None,
        sensitive_phrase_hit: bool = None,
        text: str = None,
        transition: bool = None,
    ):
        self.choices = choices
        self.sensitive_phrase_hit = sensitive_phrase_hit
        self.text = text
        self.transition = transition

    def validate(self):
        if self.choices:
            for k in self.choices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Choices'] = []
        if self.choices is not None:
            for k in self.choices:
                result['Choices'].append(k.to_map() if k else None)
        if self.sensitive_phrase_hit is not None:
            result['SensitivePhraseHit'] = self.sensitive_phrase_hit
        if self.text is not None:
            result['Text'] = self.text
        if self.transition is not None:
            result['Transition'] = self.transition
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.choices = []
        if m.get('Choices') is not None:
            for k in m.get('Choices'):
                temp_model = BaiLianSseChatResponseBodyDataOutputChoices()
                self.choices.append(temp_model.from_map(k))
        if m.get('SensitivePhraseHit') is not None:
            self.sensitive_phrase_hit = m.get('SensitivePhraseHit')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Transition') is not None:
            self.transition = m.get('Transition')
        return self


class BaiLianSseChatResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        output: BaiLianSseChatResponseBodyDataOutput = None,
        request_id: str = None,
        session_id: str = None,
    ):
        self.code = code
        self.message = message
        self.output = output
        self.request_id = request_id
        self.session_id = session_id

    def validate(self):
        if self.output:
            self.output.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.output is not None:
            result['Output'] = self.output.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Output') is not None:
            temp_model = BaiLianSseChatResponseBodyDataOutput()
            self.output = temp_model.from_map(m['Output'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class BaiLianSseChatResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: BaiLianSseChatResponseBodyData = None,
        http_status_code: str = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = BaiLianSseChatResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BaiLianSseChatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BaiLianSseChatResponseBody = None,
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
            temp_model = BaiLianSseChatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchCreateShopRequestShopList(TeaModel):
    def __init__(
        self,
        business_status: int = None,
        latitude: str = None,
        location: str = None,
        longitude: str = None,
        region_address: str = None,
        region_code: str = None,
        remark: str = None,
        shop_group_ids: List[str] = None,
        shop_id: str = None,
        shop_name: str = None,
        weekdays_end_time: str = None,
        weekdays_start_time: str = None,
        weekend_end_time: str = None,
        weekend_start_time: str = None,
    ):
        self.business_status = business_status
        self.latitude = latitude
        self.location = location
        self.longitude = longitude
        self.region_address = region_address
        self.region_code = region_code
        self.remark = remark
        self.shop_group_ids = shop_group_ids
        # This parameter is required.
        self.shop_id = shop_id
        # This parameter is required.
        self.shop_name = shop_name
        self.weekdays_end_time = weekdays_end_time
        self.weekdays_start_time = weekdays_start_time
        self.weekend_end_time = weekend_end_time
        self.weekend_start_time = weekend_start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.location is not None:
            result['Location'] = self.location
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.region_address is not None:
            result['RegionAddress'] = self.region_address
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.shop_group_ids is not None:
            result['ShopGroupIds'] = self.shop_group_ids
        if self.shop_id is not None:
            result['ShopId'] = self.shop_id
        if self.shop_name is not None:
            result['ShopName'] = self.shop_name
        if self.weekdays_end_time is not None:
            result['WeekdaysEndTime'] = self.weekdays_end_time
        if self.weekdays_start_time is not None:
            result['WeekdaysStartTime'] = self.weekdays_start_time
        if self.weekend_end_time is not None:
            result['WeekendEndTime'] = self.weekend_end_time
        if self.weekend_start_time is not None:
            result['WeekendStartTime'] = self.weekend_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('RegionAddress') is not None:
            self.region_address = m.get('RegionAddress')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ShopGroupIds') is not None:
            self.shop_group_ids = m.get('ShopGroupIds')
        if m.get('ShopId') is not None:
            self.shop_id = m.get('ShopId')
        if m.get('ShopName') is not None:
            self.shop_name = m.get('ShopName')
        if m.get('WeekdaysEndTime') is not None:
            self.weekdays_end_time = m.get('WeekdaysEndTime')
        if m.get('WeekdaysStartTime') is not None:
            self.weekdays_start_time = m.get('WeekdaysStartTime')
        if m.get('WeekendEndTime') is not None:
            self.weekend_end_time = m.get('WeekendEndTime')
        if m.get('WeekendStartTime') is not None:
            self.weekend_start_time = m.get('WeekendStartTime')
        return self


class BatchCreateShopRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        shop_list: List[BatchCreateShopRequestShopList] = None,
    ):
        self.country = country
        # This parameter is required.
        self.shop_list = shop_list

    def validate(self):
        if self.shop_list:
            for k in self.shop_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        result['ShopList'] = []
        if self.shop_list is not None:
            for k in self.shop_list:
                result['ShopList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        self.shop_list = []
        if m.get('ShopList') is not None:
            for k in m.get('ShopList'):
                temp_model = BatchCreateShopRequestShopList()
                self.shop_list.append(temp_model.from_map(k))
        return self


class BatchCreateShopShrinkRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        shop_list_shrink: str = None,
    ):
        self.country = country
        # This parameter is required.
        self.shop_list_shrink = shop_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.shop_list_shrink is not None:
            result['ShopList'] = self.shop_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('ShopList') is not None:
            self.shop_list_shrink = m.get('ShopList')
        return self


class BatchCreateShopResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        shop_id: str = None,
    ):
        self.code = code
        self.message = message
        self.shop_id = shop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.shop_id is not None:
            result['ShopId'] = self.shop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ShopId') is not None:
            self.shop_id = m.get('ShopId')
        return self


class BatchCreateShopResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[BatchCreateShopResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = BatchCreateShopResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchCreateShopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchCreateShopResponseBody = None,
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
            temp_model = BatchCreateShopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchCreateShopGroupRequestShopGroupList(TeaModel):
    def __init__(
        self,
        shop_group_id: str = None,
        shop_group_name: str = None,
    ):
        # This parameter is required.
        self.shop_group_id = shop_group_id
        # This parameter is required.
        self.shop_group_name = shop_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.shop_group_id is not None:
            result['ShopGroupId'] = self.shop_group_id
        if self.shop_group_name is not None:
            result['ShopGroupName'] = self.shop_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShopGroupId') is not None:
            self.shop_group_id = m.get('ShopGroupId')
        if m.get('ShopGroupName') is not None:
            self.shop_group_name = m.get('ShopGroupName')
        return self


class BatchCreateShopGroupRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        shop_group_list: List[BatchCreateShopGroupRequestShopGroupList] = None,
    ):
        self.country = country
        # This parameter is required.
        self.shop_group_list = shop_group_list

    def validate(self):
        if self.shop_group_list:
            for k in self.shop_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        result['ShopGroupList'] = []
        if self.shop_group_list is not None:
            for k in self.shop_group_list:
                result['ShopGroupList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        self.shop_group_list = []
        if m.get('ShopGroupList') is not None:
            for k in m.get('ShopGroupList'):
                temp_model = BatchCreateShopGroupRequestShopGroupList()
                self.shop_group_list.append(temp_model.from_map(k))
        return self


class BatchCreateShopGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        shop_group_list_shrink: str = None,
    ):
        self.country = country
        # This parameter is required.
        self.shop_group_list_shrink = shop_group_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.shop_group_list_shrink is not None:
            result['ShopGroupList'] = self.shop_group_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('ShopGroupList') is not None:
            self.shop_group_list_shrink = m.get('ShopGroupList')
        return self


class BatchCreateShopGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        shop_group_id: str = None,
    ):
        self.code = code
        self.message = message
        self.shop_group_id = shop_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.shop_group_id is not None:
            result['ShopGroupId'] = self.shop_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ShopGroupId') is not None:
            self.shop_group_id = m.get('ShopGroupId')
        return self


class BatchCreateShopGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[BatchCreateShopGroupResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = BatchCreateShopGroupResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchCreateShopGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchCreateShopGroupResponseBody = None,
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
            temp_model = BatchCreateShopGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchGetStoreTextDataRequest(TeaModel):
    def __init__(
        self,
        store_ids: List[str] = None,
        country: str = None,
    ):
        # This parameter is required.
        self.store_ids = store_ids
        self.country = country

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.store_ids is not None:
            result['StoreIds'] = self.store_ids
        if self.country is not None:
            result['country'] = self.country
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreIds') is not None:
            self.store_ids = m.get('StoreIds')
        if m.get('country') is not None:
            self.country = m.get('country')
        return self


class BatchGetStoreTextDataShrinkRequest(TeaModel):
    def __init__(
        self,
        store_ids_shrink: str = None,
        country: str = None,
    ):
        # This parameter is required.
        self.store_ids_shrink = store_ids_shrink
        self.country = country

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.store_ids_shrink is not None:
            result['StoreIds'] = self.store_ids_shrink
        if self.country is not None:
            result['country'] = self.country
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreIds') is not None:
            self.store_ids_shrink = m.get('StoreIds')
        if m.get('country') is not None:
            self.country = m.get('country')
        return self


class BatchGetStoreTextDataResponseBodyDataContainersContainerData(TeaModel):
    def __init__(
        self,
        bold: int = None,
        color: str = None,
        mark: str = None,
        sub_text: str = None,
        text: str = None,
    ):
        self.bold = bold
        self.color = color
        self.mark = mark
        self.sub_text = sub_text
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bold is not None:
            result['Bold'] = self.bold
        if self.color is not None:
            result['Color'] = self.color
        if self.mark is not None:
            result['Mark'] = self.mark
        if self.sub_text is not None:
            result['SubText'] = self.sub_text
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bold') is not None:
            self.bold = m.get('Bold')
        if m.get('Color') is not None:
            self.color = m.get('Color')
        if m.get('Mark') is not None:
            self.mark = m.get('Mark')
        if m.get('SubText') is not None:
            self.sub_text = m.get('SubText')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class BatchGetStoreTextDataResponseBodyDataContainers(TeaModel):
    def __init__(
        self,
        container_data: List[BatchGetStoreTextDataResponseBodyDataContainersContainerData] = None,
        title: str = None,
        type: str = None,
        visible: int = None,
    ):
        self.container_data = container_data
        self.title = title
        self.type = type
        self.visible = visible

    def validate(self):
        if self.container_data:
            for k in self.container_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContainerData'] = []
        if self.container_data is not None:
            for k in self.container_data:
                result['ContainerData'].append(k.to_map() if k else None)
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.visible is not None:
            result['Visible'] = self.visible
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.container_data = []
        if m.get('ContainerData') is not None:
            for k in m.get('ContainerData'):
                temp_model = BatchGetStoreTextDataResponseBodyDataContainersContainerData()
                self.container_data.append(temp_model.from_map(k))
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Visible') is not None:
            self.visible = m.get('Visible')
        return self


class BatchGetStoreTextDataResponseBodyData(TeaModel):
    def __init__(
        self,
        containers: List[BatchGetStoreTextDataResponseBodyDataContainers] = None,
        store_id: str = None,
    ):
        self.containers = containers
        self.store_id = store_id

    def validate(self):
        if self.containers:
            for k in self.containers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Containers'] = []
        if self.containers is not None:
            for k in self.containers:
                result['Containers'].append(k.to_map() if k else None)
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.containers = []
        if m.get('Containers') is not None:
            for k in m.get('Containers'):
                temp_model = BatchGetStoreTextDataResponseBodyDataContainers()
                self.containers.append(temp_model.from_map(k))
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class BatchGetStoreTextDataResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[BatchGetStoreTextDataResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = BatchGetStoreTextDataResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchGetStoreTextDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchGetStoreTextDataResponseBody = None,
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
            temp_model = BatchGetStoreTextDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchUpdateStoreTextDataRequestStoreTextDataContainersContainerData(TeaModel):
    def __init__(
        self,
        bold: int = None,
        color: str = None,
        mark: str = None,
        sub_text: str = None,
        text: str = None,
    ):
        self.bold = bold
        self.color = color
        self.mark = mark
        self.sub_text = sub_text
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bold is not None:
            result['Bold'] = self.bold
        if self.color is not None:
            result['Color'] = self.color
        if self.mark is not None:
            result['Mark'] = self.mark
        if self.sub_text is not None:
            result['SubText'] = self.sub_text
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bold') is not None:
            self.bold = m.get('Bold')
        if m.get('Color') is not None:
            self.color = m.get('Color')
        if m.get('Mark') is not None:
            self.mark = m.get('Mark')
        if m.get('SubText') is not None:
            self.sub_text = m.get('SubText')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class BatchUpdateStoreTextDataRequestStoreTextDataContainers(TeaModel):
    def __init__(
        self,
        container_data: List[BatchUpdateStoreTextDataRequestStoreTextDataContainersContainerData] = None,
        title: str = None,
        type: str = None,
        visible: int = None,
    ):
        self.container_data = container_data
        # This parameter is required.
        self.title = title
        # This parameter is required.
        self.type = type
        self.visible = visible

    def validate(self):
        if self.container_data:
            for k in self.container_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContainerData'] = []
        if self.container_data is not None:
            for k in self.container_data:
                result['ContainerData'].append(k.to_map() if k else None)
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.visible is not None:
            result['Visible'] = self.visible
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.container_data = []
        if m.get('ContainerData') is not None:
            for k in m.get('ContainerData'):
                temp_model = BatchUpdateStoreTextDataRequestStoreTextDataContainersContainerData()
                self.container_data.append(temp_model.from_map(k))
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Visible') is not None:
            self.visible = m.get('Visible')
        return self


class BatchUpdateStoreTextDataRequestStoreTextData(TeaModel):
    def __init__(
        self,
        containers: List[BatchUpdateStoreTextDataRequestStoreTextDataContainers] = None,
        store_id: str = None,
    ):
        # This parameter is required.
        self.containers = containers
        # This parameter is required.
        self.store_id = store_id

    def validate(self):
        if self.containers:
            for k in self.containers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Containers'] = []
        if self.containers is not None:
            for k in self.containers:
                result['Containers'].append(k.to_map() if k else None)
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.containers = []
        if m.get('Containers') is not None:
            for k in m.get('Containers'):
                temp_model = BatchUpdateStoreTextDataRequestStoreTextDataContainers()
                self.containers.append(temp_model.from_map(k))
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        return self


class BatchUpdateStoreTextDataRequest(TeaModel):
    def __init__(
        self,
        store_text_data: List[BatchUpdateStoreTextDataRequestStoreTextData] = None,
        country: str = None,
    ):
        # This parameter is required.
        self.store_text_data = store_text_data
        self.country = country

    def validate(self):
        if self.store_text_data:
            for k in self.store_text_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['StoreTextData'] = []
        if self.store_text_data is not None:
            for k in self.store_text_data:
                result['StoreTextData'].append(k.to_map() if k else None)
        if self.country is not None:
            result['country'] = self.country
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.store_text_data = []
        if m.get('StoreTextData') is not None:
            for k in m.get('StoreTextData'):
                temp_model = BatchUpdateStoreTextDataRequestStoreTextData()
                self.store_text_data.append(temp_model.from_map(k))
        if m.get('country') is not None:
            self.country = m.get('country')
        return self


class BatchUpdateStoreTextDataShrinkRequest(TeaModel):
    def __init__(
        self,
        store_text_data_shrink: str = None,
        country: str = None,
    ):
        # This parameter is required.
        self.store_text_data_shrink = store_text_data_shrink
        self.country = country

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.store_text_data_shrink is not None:
            result['StoreTextData'] = self.store_text_data_shrink
        if self.country is not None:
            result['country'] = self.country
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreTextData') is not None:
            self.store_text_data_shrink = m.get('StoreTextData')
        if m.get('country') is not None:
            self.country = m.get('country')
        return self


class BatchUpdateStoreTextDataResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchUpdateStoreTextDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchUpdateStoreTextDataResponseBody = None,
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
            temp_model = BatchUpdateStoreTextDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLabelRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        country: str = None,
        label: str = None,
        title: str = None,
    ):
        # This parameter is required.
        self.category = category
        self.country = country
        # This parameter is required.
        self.label = label
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.country is not None:
            result['Country'] = self.country
        if self.label is not None:
            result['Label'] = self.label
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateLabelResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateLabelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLabelResponseBody = None,
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
            temp_model = CreateLabelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMenuDataRequestProductCombineListProductItemListProductInfo(TeaModel):
    def __init__(
        self,
        chinese_name: str = None,
        current_price: str = None,
        description: str = None,
        english_name: str = None,
        icon_text: str = None,
        original_price: str = None,
        product_id: str = None,
        product_type: str = None,
        temperature: str = None,
    ):
        # This parameter is required.
        self.chinese_name = chinese_name
        self.current_price = current_price
        self.description = description
        self.english_name = english_name
        self.icon_text = icon_text
        self.original_price = original_price
        # This parameter is required.
        self.product_id = product_id
        self.product_type = product_type
        self.temperature = temperature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chinese_name is not None:
            result['ChineseName'] = self.chinese_name
        if self.current_price is not None:
            result['CurrentPrice'] = self.current_price
        if self.description is not None:
            result['Description'] = self.description
        if self.english_name is not None:
            result['EnglishName'] = self.english_name
        if self.icon_text is not None:
            result['IconText'] = self.icon_text
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.temperature is not None:
            result['Temperature'] = self.temperature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChineseName') is not None:
            self.chinese_name = m.get('ChineseName')
        if m.get('CurrentPrice') is not None:
            self.current_price = m.get('CurrentPrice')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnglishName') is not None:
            self.english_name = m.get('EnglishName')
        if m.get('IconText') is not None:
            self.icon_text = m.get('IconText')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('Temperature') is not None:
            self.temperature = m.get('Temperature')
        return self


class CreateMenuDataRequestProductCombineListProductItemList(TeaModel):
    def __init__(
        self,
        order: int = None,
        product_info: CreateMenuDataRequestProductCombineListProductItemListProductInfo = None,
    ):
        # This parameter is required.
        self.order = order
        # This parameter is required.
        self.product_info = product_info

    def validate(self):
        if self.product_info:
            self.product_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order is not None:
            result['Order'] = self.order
        if self.product_info is not None:
            result['ProductInfo'] = self.product_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProductInfo') is not None:
            temp_model = CreateMenuDataRequestProductCombineListProductItemListProductInfo()
            self.product_info = temp_model.from_map(m['ProductInfo'])
        return self


class CreateMenuDataRequestProductCombineList(TeaModel):
    def __init__(
        self,
        english_name: str = None,
        name: str = None,
        order: int = None,
        product_item_list: List[CreateMenuDataRequestProductCombineListProductItemList] = None,
    ):
        self.english_name = english_name
        self.name = name
        # This parameter is required.
        self.order = order
        # This parameter is required.
        self.product_item_list = product_item_list

    def validate(self):
        if self.product_item_list:
            for k in self.product_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.english_name is not None:
            result['EnglishName'] = self.english_name
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        result['ProductItemList'] = []
        if self.product_item_list is not None:
            for k in self.product_item_list:
                result['ProductItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnglishName') is not None:
            self.english_name = m.get('EnglishName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        self.product_item_list = []
        if m.get('ProductItemList') is not None:
            for k in m.get('ProductItemList'):
                temp_model = CreateMenuDataRequestProductCombineListProductItemList()
                self.product_item_list.append(temp_model.from_map(k))
        return self


class CreateMenuDataRequest(TeaModel):
    def __init__(
        self,
        batch_id: str = None,
        country: str = None,
        priority: int = None,
        product_combine_list: List[CreateMenuDataRequestProductCombineList] = None,
        product_container_id: str = None,
        shop_group_id: str = None,
        shop_id_list: List[str] = None,
        type: str = None,
    ):
        self.batch_id = batch_id
        self.country = country
        self.priority = priority
        # This parameter is required.
        self.product_combine_list = product_combine_list
        # This parameter is required.
        self.product_container_id = product_container_id
        self.shop_group_id = shop_group_id
        self.shop_id_list = shop_id_list
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.product_combine_list:
            for k in self.product_combine_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.country is not None:
            result['Country'] = self.country
        if self.priority is not None:
            result['Priority'] = self.priority
        result['ProductCombineList'] = []
        if self.product_combine_list is not None:
            for k in self.product_combine_list:
                result['ProductCombineList'].append(k.to_map() if k else None)
        if self.product_container_id is not None:
            result['ProductContainerId'] = self.product_container_id
        if self.shop_group_id is not None:
            result['ShopGroupId'] = self.shop_group_id
        if self.shop_id_list is not None:
            result['ShopIdList'] = self.shop_id_list
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        self.product_combine_list = []
        if m.get('ProductCombineList') is not None:
            for k in m.get('ProductCombineList'):
                temp_model = CreateMenuDataRequestProductCombineList()
                self.product_combine_list.append(temp_model.from_map(k))
        if m.get('ProductContainerId') is not None:
            self.product_container_id = m.get('ProductContainerId')
        if m.get('ShopGroupId') is not None:
            self.shop_group_id = m.get('ShopGroupId')
        if m.get('ShopIdList') is not None:
            self.shop_id_list = m.get('ShopIdList')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateMenuDataShrinkRequest(TeaModel):
    def __init__(
        self,
        batch_id: str = None,
        country: str = None,
        priority: int = None,
        product_combine_list_shrink: str = None,
        product_container_id: str = None,
        shop_group_id: str = None,
        shop_id_list_shrink: str = None,
        type: str = None,
    ):
        self.batch_id = batch_id
        self.country = country
        self.priority = priority
        # This parameter is required.
        self.product_combine_list_shrink = product_combine_list_shrink
        # This parameter is required.
        self.product_container_id = product_container_id
        self.shop_group_id = shop_group_id
        self.shop_id_list_shrink = shop_id_list_shrink
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.country is not None:
            result['Country'] = self.country
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.product_combine_list_shrink is not None:
            result['ProductCombineList'] = self.product_combine_list_shrink
        if self.product_container_id is not None:
            result['ProductContainerId'] = self.product_container_id
        if self.shop_group_id is not None:
            result['ShopGroupId'] = self.shop_group_id
        if self.shop_id_list_shrink is not None:
            result['ShopIdList'] = self.shop_id_list_shrink
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ProductCombineList') is not None:
            self.product_combine_list_shrink = m.get('ProductCombineList')
        if m.get('ProductContainerId') is not None:
            self.product_container_id = m.get('ProductContainerId')
        if m.get('ShopGroupId') is not None:
            self.shop_group_id = m.get('ShopGroupId')
        if m.get('ShopIdList') is not None:
            self.shop_id_list_shrink = m.get('ShopIdList')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateMenuDataResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateMenuDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMenuDataResponseBody = None,
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
            temp_model = CreateMenuDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateShopRequestShopList(TeaModel):
    def __init__(
        self,
        business_status: int = None,
        latitude: str = None,
        location: str = None,
        longitude: str = None,
        region_address: str = None,
        region_code: str = None,
        remark: str = None,
        shop_group_ids: List[str] = None,
        shop_id: str = None,
        shop_name: str = None,
        weekdays_end_time: str = None,
        weekdays_start_time: str = None,
        weekend_end_time: str = None,
        weekend_start_time: str = None,
    ):
        self.business_status = business_status
        self.latitude = latitude
        self.location = location
        self.longitude = longitude
        self.region_address = region_address
        self.region_code = region_code
        self.remark = remark
        self.shop_group_ids = shop_group_ids
        # This parameter is required.
        self.shop_id = shop_id
        # This parameter is required.
        self.shop_name = shop_name
        self.weekdays_end_time = weekdays_end_time
        self.weekdays_start_time = weekdays_start_time
        self.weekend_end_time = weekend_end_time
        self.weekend_start_time = weekend_start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.location is not None:
            result['Location'] = self.location
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.region_address is not None:
            result['RegionAddress'] = self.region_address
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.shop_group_ids is not None:
            result['ShopGroupIds'] = self.shop_group_ids
        if self.shop_id is not None:
            result['ShopId'] = self.shop_id
        if self.shop_name is not None:
            result['ShopName'] = self.shop_name
        if self.weekdays_end_time is not None:
            result['WeekdaysEndTime'] = self.weekdays_end_time
        if self.weekdays_start_time is not None:
            result['WeekdaysStartTime'] = self.weekdays_start_time
        if self.weekend_end_time is not None:
            result['WeekendEndTime'] = self.weekend_end_time
        if self.weekend_start_time is not None:
            result['WeekendStartTime'] = self.weekend_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('RegionAddress') is not None:
            self.region_address = m.get('RegionAddress')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ShopGroupIds') is not None:
            self.shop_group_ids = m.get('ShopGroupIds')
        if m.get('ShopId') is not None:
            self.shop_id = m.get('ShopId')
        if m.get('ShopName') is not None:
            self.shop_name = m.get('ShopName')
        if m.get('WeekdaysEndTime') is not None:
            self.weekdays_end_time = m.get('WeekdaysEndTime')
        if m.get('WeekdaysStartTime') is not None:
            self.weekdays_start_time = m.get('WeekdaysStartTime')
        if m.get('WeekendEndTime') is not None:
            self.weekend_end_time = m.get('WeekendEndTime')
        if m.get('WeekendStartTime') is not None:
            self.weekend_start_time = m.get('WeekendStartTime')
        return self


class CreateShopRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        shop_list: List[CreateShopRequestShopList] = None,
    ):
        self.country = country
        self.shop_list = shop_list

    def validate(self):
        if self.shop_list:
            for k in self.shop_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        result['ShopList'] = []
        if self.shop_list is not None:
            for k in self.shop_list:
                result['ShopList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        self.shop_list = []
        if m.get('ShopList') is not None:
            for k in m.get('ShopList'):
                temp_model = CreateShopRequestShopList()
                self.shop_list.append(temp_model.from_map(k))
        return self


class CreateShopShrinkRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        shop_list_shrink: str = None,
    ):
        self.country = country
        self.shop_list_shrink = shop_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.shop_list_shrink is not None:
            result['ShopList'] = self.shop_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('ShopList') is not None:
            self.shop_list_shrink = m.get('ShopList')
        return self


class CreateShopResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[str] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateShopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateShopResponseBody = None,
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
            temp_model = CreateShopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateShopGroupRequestShopGroupList(TeaModel):
    def __init__(
        self,
        shop_group_id: str = None,
        shop_group_name: str = None,
    ):
        # This parameter is required.
        self.shop_group_id = shop_group_id
        # This parameter is required.
        self.shop_group_name = shop_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.shop_group_id is not None:
            result['ShopGroupId'] = self.shop_group_id
        if self.shop_group_name is not None:
            result['ShopGroupName'] = self.shop_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShopGroupId') is not None:
            self.shop_group_id = m.get('ShopGroupId')
        if m.get('ShopGroupName') is not None:
            self.shop_group_name = m.get('ShopGroupName')
        return self


class CreateShopGroupRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        shop_group_list: List[CreateShopGroupRequestShopGroupList] = None,
    ):
        self.country = country
        self.shop_group_list = shop_group_list

    def validate(self):
        if self.shop_group_list:
            for k in self.shop_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        result['ShopGroupList'] = []
        if self.shop_group_list is not None:
            for k in self.shop_group_list:
                result['ShopGroupList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        self.shop_group_list = []
        if m.get('ShopGroupList') is not None:
            for k in m.get('ShopGroupList'):
                temp_model = CreateShopGroupRequestShopGroupList()
                self.shop_group_list.append(temp_model.from_map(k))
        return self


class CreateShopGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        shop_group_list_shrink: str = None,
    ):
        self.country = country
        self.shop_group_list_shrink = shop_group_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.shop_group_list_shrink is not None:
            result['ShopGroupList'] = self.shop_group_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('ShopGroupList') is not None:
            self.shop_group_list_shrink = m.get('ShopGroupList')
        return self


class CreateShopGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[str] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateShopGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateShopGroupResponseBody = None,
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
            temp_model = CreateShopGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSpeechTemplateRequest(TeaModel):
    def __init__(
        self,
        contents: str = None,
        type: str = None,
        country: str = None,
    ):
        # This parameter is required.
        self.contents = contents
        # This parameter is required.
        self.type = type
        self.country = country

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contents is not None:
            result['Contents'] = self.contents
        if self.type is not None:
            result['Type'] = self.type
        if self.country is not None:
            result['country'] = self.country
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contents') is not None:
            self.contents = m.get('Contents')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('country') is not None:
            self.country = m.get('country')
        return self


class CreateSpeechTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSpeechTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSpeechTemplateResponseBody = None,
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
            temp_model = CreateSpeechTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLabelRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        label_id: str = None,
    ):
        self.country = country
        # This parameter is required.
        self.label_id = label_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        return self


class DeleteLabelResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteLabelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteLabelResponseBody = None,
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
            temp_model = DeleteLabelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProductImageRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        product_code: str = None,
        product_image_ids: List[str] = None,
    ):
        self.country = country
        self.product_code = product_code
        self.product_image_ids = product_image_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_image_ids is not None:
            result['ProductImageIds'] = self.product_image_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductImageIds') is not None:
            self.product_image_ids = m.get('ProductImageIds')
        return self


class DeleteProductImageShrinkRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        product_code: str = None,
        product_image_ids_shrink: str = None,
    ):
        self.country = country
        self.product_code = product_code
        self.product_image_ids_shrink = product_image_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_image_ids_shrink is not None:
            result['ProductImageIds'] = self.product_image_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductImageIds') is not None:
            self.product_image_ids_shrink = m.get('ProductImageIds')
        return self


class DeleteProductImageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteProductImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteProductImageResponseBody = None,
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
            temp_model = DeleteProductImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteShopRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        shop_id: str = None,
    ):
        self.country = country
        # This parameter is required.
        self.shop_id = shop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.shop_id is not None:
            result['ShopId'] = self.shop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('ShopId') is not None:
            self.shop_id = m.get('ShopId')
        return self


class DeleteShopResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteShopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteShopResponseBody = None,
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
            temp_model = DeleteShopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteShopGroupRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        shop_group_id: str = None,
    ):
        self.country = country
        # This parameter is required.
        self.shop_group_id = shop_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.shop_group_id is not None:
            result['ShopGroupId'] = self.shop_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('ShopGroupId') is not None:
            self.shop_group_id = m.get('ShopGroupId')
        return self


class DeleteShopGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteShopGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteShopGroupResponseBody = None,
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
            temp_model = DeleteShopGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSpeechTemplateRequest(TeaModel):
    def __init__(
        self,
        type: str = None,
        country: str = None,
    ):
        # This parameter is required.
        self.type = type
        self.country = country

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.country is not None:
            result['country'] = self.country
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('country') is not None:
            self.country = m.get('country')
        return self


class DeleteSpeechTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSpeechTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSpeechTemplateResponseBody = None,
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
            temp_model = DeleteSpeechTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMenuDataStatusRequest(TeaModel):
    def __init__(
        self,
        batch_id: str = None,
        country: str = None,
        product_container_id: str = None,
    ):
        self.batch_id = batch_id
        self.country = country
        self.product_container_id = product_container_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.country is not None:
            result['Country'] = self.country
        if self.product_container_id is not None:
            result['ProductContainerId'] = self.product_container_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('ProductContainerId') is not None:
            self.product_container_id = m.get('ProductContainerId')
        return self


class GetMenuDataStatusResponseBody(TeaModel):
    def __init__(
        self,
        batch_id: str = None,
        code: str = None,
        failed: int = None,
        failed_product_container_list: List[str] = None,
        http_status_code: int = None,
        message: str = None,
        product_container_id: str = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.batch_id = batch_id
        self.code = code
        self.failed = failed
        self.failed_product_container_list = failed_product_container_list
        self.http_status_code = http_status_code
        self.message = message
        self.product_container_id = product_container_id
        self.request_id = request_id
        self.success = success
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.code is not None:
            result['Code'] = self.code
        if self.failed is not None:
            result['Failed'] = self.failed
        if self.failed_product_container_list is not None:
            result['FailedProductContainerList'] = self.failed_product_container_list
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.product_container_id is not None:
            result['ProductContainerId'] = self.product_container_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')
        if m.get('FailedProductContainerList') is not None:
            self.failed_product_container_list = m.get('FailedProductContainerList')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ProductContainerId') is not None:
            self.product_container_id = m.get('ProductContainerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetMenuDataStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMenuDataStatusResponseBody = None,
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
            temp_model = GetMenuDataStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetShopRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        shop_id: str = None,
    ):
        self.country = country
        # This parameter is required.
        self.shop_id = shop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.shop_id is not None:
            result['ShopId'] = self.shop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('ShopId') is not None:
            self.shop_id = m.get('ShopId')
        return self


class GetShopResponseBody(TeaModel):
    def __init__(
        self,
        business_status: int = None,
        code: str = None,
        device_mac_list: List[str] = None,
        device_num: int = None,
        gmt_create_time: int = None,
        http_status_code: int = None,
        latitude: str = None,
        location: str = None,
        longitude: str = None,
        message: str = None,
        region_address: str = None,
        region_code: str = None,
        remark: str = None,
        request_id: str = None,
        shop_group_ids: List[str] = None,
        shop_id: str = None,
        shop_name: str = None,
        success: bool = None,
        weekdays_end_time: str = None,
        weekdays_start_time: str = None,
        weekend_end_time: str = None,
        weekend_start_time: str = None,
    ):
        self.business_status = business_status
        self.code = code
        self.device_mac_list = device_mac_list
        self.device_num = device_num
        self.gmt_create_time = gmt_create_time
        self.http_status_code = http_status_code
        self.latitude = latitude
        self.location = location
        self.longitude = longitude
        self.message = message
        self.region_address = region_address
        self.region_code = region_code
        self.remark = remark
        self.request_id = request_id
        self.shop_group_ids = shop_group_ids
        self.shop_id = shop_id
        self.shop_name = shop_name
        self.success = success
        self.weekdays_end_time = weekdays_end_time
        self.weekdays_start_time = weekdays_start_time
        self.weekend_end_time = weekend_end_time
        self.weekend_start_time = weekend_start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.code is not None:
            result['Code'] = self.code
        if self.device_mac_list is not None:
            result['DeviceMacList'] = self.device_mac_list
        if self.device_num is not None:
            result['DeviceNum'] = self.device_num
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.location is not None:
            result['Location'] = self.location
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.message is not None:
            result['Message'] = self.message
        if self.region_address is not None:
            result['RegionAddress'] = self.region_address
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.shop_group_ids is not None:
            result['ShopGroupIds'] = self.shop_group_ids
        if self.shop_id is not None:
            result['ShopId'] = self.shop_id
        if self.shop_name is not None:
            result['ShopName'] = self.shop_name
        if self.success is not None:
            result['Success'] = self.success
        if self.weekdays_end_time is not None:
            result['WeekdaysEndTime'] = self.weekdays_end_time
        if self.weekdays_start_time is not None:
            result['WeekdaysStartTime'] = self.weekdays_start_time
        if self.weekend_end_time is not None:
            result['WeekendEndTime'] = self.weekend_end_time
        if self.weekend_start_time is not None:
            result['WeekendStartTime'] = self.weekend_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DeviceMacList') is not None:
            self.device_mac_list = m.get('DeviceMacList')
        if m.get('DeviceNum') is not None:
            self.device_num = m.get('DeviceNum')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RegionAddress') is not None:
            self.region_address = m.get('RegionAddress')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShopGroupIds') is not None:
            self.shop_group_ids = m.get('ShopGroupIds')
        if m.get('ShopId') is not None:
            self.shop_id = m.get('ShopId')
        if m.get('ShopName') is not None:
            self.shop_name = m.get('ShopName')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('WeekdaysEndTime') is not None:
            self.weekdays_end_time = m.get('WeekdaysEndTime')
        if m.get('WeekdaysStartTime') is not None:
            self.weekdays_start_time = m.get('WeekdaysStartTime')
        if m.get('WeekendEndTime') is not None:
            self.weekend_end_time = m.get('WeekendEndTime')
        if m.get('WeekendStartTime') is not None:
            self.weekend_start_time = m.get('WeekendStartTime')
        return self


class GetShopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetShopResponseBody = None,
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
            temp_model = GetShopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetShopGroupRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        shop_group_id: str = None,
    ):
        self.country = country
        # This parameter is required.
        self.shop_group_id = shop_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.shop_group_id is not None:
            result['ShopGroupId'] = self.shop_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('ShopGroupId') is not None:
            self.shop_group_id = m.get('ShopGroupId')
        return self


class GetShopGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        shop_group_id: str = None,
        shop_group_name: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.shop_group_id = shop_group_id
        self.shop_group_name = shop_group_name
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.shop_group_id is not None:
            result['ShopGroupId'] = self.shop_group_id
        if self.shop_group_name is not None:
            result['ShopGroupName'] = self.shop_group_name
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ShopGroupId') is not None:
            self.shop_group_id = m.get('ShopGroupId')
        if m.get('ShopGroupName') is not None:
            self.shop_group_name = m.get('ShopGroupName')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetShopGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetShopGroupResponseBody = None,
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
            temp_model = GetShopGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSpeechTemplateRequest(TeaModel):
    def __init__(
        self,
        type: str = None,
        country: str = None,
    ):
        # This parameter is required.
        self.type = type
        self.country = country

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.country is not None:
            result['country'] = self.country
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('country') is not None:
            self.country = m.get('country')
        return self


class GetSpeechTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSpeechTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSpeechTemplateResponseBody = None,
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
            temp_model = GetSpeechTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMenuDataRequest(TeaModel):
    def __init__(
        self,
        batch_id: str = None,
        country: str = None,
        create_request_id: str = None,
        page_number: int = None,
        page_size: int = None,
        product_container_id: str = None,
    ):
        self.batch_id = batch_id
        self.country = country
        self.create_request_id = create_request_id
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.product_container_id = product_container_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.country is not None:
            result['Country'] = self.country
        if self.create_request_id is not None:
            result['CreateRequestId'] = self.create_request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_container_id is not None:
            result['ProductContainerId'] = self.product_container_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('CreateRequestId') is not None:
            self.create_request_id = m.get('CreateRequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductContainerId') is not None:
            self.product_container_id = m.get('ProductContainerId')
        return self


class ListMenuDataResponseBodyDataProductCombineListProductItemListProductInfo(TeaModel):
    def __init__(
        self,
        chinese_name: str = None,
        current_price: str = None,
        description: str = None,
        english_name: str = None,
        icon_text: str = None,
        original_price: str = None,
        product_id: str = None,
        product_type: str = None,
        temperature: str = None,
    ):
        self.chinese_name = chinese_name
        self.current_price = current_price
        self.description = description
        self.english_name = english_name
        self.icon_text = icon_text
        self.original_price = original_price
        self.product_id = product_id
        self.product_type = product_type
        self.temperature = temperature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chinese_name is not None:
            result['ChineseName'] = self.chinese_name
        if self.current_price is not None:
            result['CurrentPrice'] = self.current_price
        if self.description is not None:
            result['Description'] = self.description
        if self.english_name is not None:
            result['EnglishName'] = self.english_name
        if self.icon_text is not None:
            result['IconText'] = self.icon_text
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.temperature is not None:
            result['Temperature'] = self.temperature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChineseName') is not None:
            self.chinese_name = m.get('ChineseName')
        if m.get('CurrentPrice') is not None:
            self.current_price = m.get('CurrentPrice')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnglishName') is not None:
            self.english_name = m.get('EnglishName')
        if m.get('IconText') is not None:
            self.icon_text = m.get('IconText')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('Temperature') is not None:
            self.temperature = m.get('Temperature')
        return self


class ListMenuDataResponseBodyDataProductCombineListProductItemList(TeaModel):
    def __init__(
        self,
        order: int = None,
        product_info: ListMenuDataResponseBodyDataProductCombineListProductItemListProductInfo = None,
    ):
        self.order = order
        self.product_info = product_info

    def validate(self):
        if self.product_info:
            self.product_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order is not None:
            result['Order'] = self.order
        if self.product_info is not None:
            result['ProductInfo'] = self.product_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('ProductInfo') is not None:
            temp_model = ListMenuDataResponseBodyDataProductCombineListProductItemListProductInfo()
            self.product_info = temp_model.from_map(m['ProductInfo'])
        return self


class ListMenuDataResponseBodyDataProductCombineList(TeaModel):
    def __init__(
        self,
        name: str = None,
        order: int = None,
        product_item_list: List[ListMenuDataResponseBodyDataProductCombineListProductItemList] = None,
    ):
        self.name = name
        self.order = order
        self.product_item_list = product_item_list

    def validate(self):
        if self.product_item_list:
            for k in self.product_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        result['ProductItemList'] = []
        if self.product_item_list is not None:
            for k in self.product_item_list:
                result['ProductItemList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        self.product_item_list = []
        if m.get('ProductItemList') is not None:
            for k in m.get('ProductItemList'):
                temp_model = ListMenuDataResponseBodyDataProductCombineListProductItemList()
                self.product_item_list.append(temp_model.from_map(k))
        return self


class ListMenuDataResponseBodyData(TeaModel):
    def __init__(
        self,
        batch_id: str = None,
        priority: int = None,
        product_combine_list: List[ListMenuDataResponseBodyDataProductCombineList] = None,
        product_container_id: str = None,
        shop_group_id: str = None,
        shop_id_list: List[str] = None,
        type: str = None,
    ):
        self.batch_id = batch_id
        self.priority = priority
        self.product_combine_list = product_combine_list
        self.product_container_id = product_container_id
        self.shop_group_id = shop_group_id
        self.shop_id_list = shop_id_list
        self.type = type

    def validate(self):
        if self.product_combine_list:
            for k in self.product_combine_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.priority is not None:
            result['Priority'] = self.priority
        result['ProductCombineList'] = []
        if self.product_combine_list is not None:
            for k in self.product_combine_list:
                result['ProductCombineList'].append(k.to_map() if k else None)
        if self.product_container_id is not None:
            result['ProductContainerId'] = self.product_container_id
        if self.shop_group_id is not None:
            result['ShopGroupId'] = self.shop_group_id
        if self.shop_id_list is not None:
            result['ShopIdList'] = self.shop_id_list
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        self.product_combine_list = []
        if m.get('ProductCombineList') is not None:
            for k in m.get('ProductCombineList'):
                temp_model = ListMenuDataResponseBodyDataProductCombineList()
                self.product_combine_list.append(temp_model.from_map(k))
        if m.get('ProductContainerId') is not None:
            self.product_container_id = m.get('ProductContainerId')
        if m.get('ShopGroupId') is not None:
            self.shop_group_id = m.get('ShopGroupId')
        if m.get('ShopIdList') is not None:
            self.shop_id_list = m.get('ShopIdList')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListMenuDataResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListMenuDataResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListMenuDataResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
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


class ListMenuDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMenuDataResponseBody = None,
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
            temp_model = ListMenuDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListShopRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        page_number: int = None,
        page_size: int = None,
        shop_group_ids: List[str] = None,
        shop_id: str = None,
        shop_name: str = None,
    ):
        self.country = country
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.shop_group_ids = shop_group_ids
        self.shop_id = shop_id
        self.shop_name = shop_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.shop_group_ids is not None:
            result['ShopGroupIds'] = self.shop_group_ids
        if self.shop_id is not None:
            result['ShopId'] = self.shop_id
        if self.shop_name is not None:
            result['ShopName'] = self.shop_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ShopGroupIds') is not None:
            self.shop_group_ids = m.get('ShopGroupIds')
        if m.get('ShopId') is not None:
            self.shop_id = m.get('ShopId')
        if m.get('ShopName') is not None:
            self.shop_name = m.get('ShopName')
        return self


class ListShopShrinkRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        page_number: int = None,
        page_size: int = None,
        shop_group_ids_shrink: str = None,
        shop_id: str = None,
        shop_name: str = None,
    ):
        self.country = country
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.shop_group_ids_shrink = shop_group_ids_shrink
        self.shop_id = shop_id
        self.shop_name = shop_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.shop_group_ids_shrink is not None:
            result['ShopGroupIds'] = self.shop_group_ids_shrink
        if self.shop_id is not None:
            result['ShopId'] = self.shop_id
        if self.shop_name is not None:
            result['ShopName'] = self.shop_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ShopGroupIds') is not None:
            self.shop_group_ids_shrink = m.get('ShopGroupIds')
        if m.get('ShopId') is not None:
            self.shop_id = m.get('ShopId')
        if m.get('ShopName') is not None:
            self.shop_name = m.get('ShopName')
        return self


class ListShopResponseBodyData(TeaModel):
    def __init__(
        self,
        business_status: int = None,
        device_mac_list: List[str] = None,
        device_num: int = None,
        gmt_create_time: int = None,
        latitude: str = None,
        location: str = None,
        longitude: str = None,
        region_address: str = None,
        region_code: str = None,
        remark: str = None,
        shop_group_ids: List[str] = None,
        shop_id: str = None,
        shop_name: str = None,
        weekdays_end_time: str = None,
        weekdays_start_time: str = None,
        weekend_end_time: str = None,
        weekend_start_time: str = None,
    ):
        self.business_status = business_status
        self.device_mac_list = device_mac_list
        self.device_num = device_num
        self.gmt_create_time = gmt_create_time
        self.latitude = latitude
        self.location = location
        self.longitude = longitude
        self.region_address = region_address
        self.region_code = region_code
        self.remark = remark
        self.shop_group_ids = shop_group_ids
        self.shop_id = shop_id
        self.shop_name = shop_name
        self.weekdays_end_time = weekdays_end_time
        self.weekdays_start_time = weekdays_start_time
        self.weekend_end_time = weekend_end_time
        self.weekend_start_time = weekend_start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.device_mac_list is not None:
            result['DeviceMacList'] = self.device_mac_list
        if self.device_num is not None:
            result['DeviceNum'] = self.device_num
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.location is not None:
            result['Location'] = self.location
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.region_address is not None:
            result['RegionAddress'] = self.region_address
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.shop_group_ids is not None:
            result['ShopGroupIds'] = self.shop_group_ids
        if self.shop_id is not None:
            result['ShopId'] = self.shop_id
        if self.shop_name is not None:
            result['ShopName'] = self.shop_name
        if self.weekdays_end_time is not None:
            result['WeekdaysEndTime'] = self.weekdays_end_time
        if self.weekdays_start_time is not None:
            result['WeekdaysStartTime'] = self.weekdays_start_time
        if self.weekend_end_time is not None:
            result['WeekendEndTime'] = self.weekend_end_time
        if self.weekend_start_time is not None:
            result['WeekendStartTime'] = self.weekend_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('DeviceMacList') is not None:
            self.device_mac_list = m.get('DeviceMacList')
        if m.get('DeviceNum') is not None:
            self.device_num = m.get('DeviceNum')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('RegionAddress') is not None:
            self.region_address = m.get('RegionAddress')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ShopGroupIds') is not None:
            self.shop_group_ids = m.get('ShopGroupIds')
        if m.get('ShopId') is not None:
            self.shop_id = m.get('ShopId')
        if m.get('ShopName') is not None:
            self.shop_name = m.get('ShopName')
        if m.get('WeekdaysEndTime') is not None:
            self.weekdays_end_time = m.get('WeekdaysEndTime')
        if m.get('WeekdaysStartTime') is not None:
            self.weekdays_start_time = m.get('WeekdaysStartTime')
        if m.get('WeekendEndTime') is not None:
            self.weekend_end_time = m.get('WeekendEndTime')
        if m.get('WeekendStartTime') is not None:
            self.weekend_start_time = m.get('WeekendStartTime')
        return self


class ListShopResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListShopResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListShopResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
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


class ListShopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListShopResponseBody = None,
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
            temp_model = ListShopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListShopGroupRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        page_number: int = None,
        page_size: int = None,
        shop_group_id: str = None,
        shop_group_name: str = None,
    ):
        self.country = country
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.shop_group_id = shop_group_id
        self.shop_group_name = shop_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.shop_group_id is not None:
            result['ShopGroupId'] = self.shop_group_id
        if self.shop_group_name is not None:
            result['ShopGroupName'] = self.shop_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ShopGroupId') is not None:
            self.shop_group_id = m.get('ShopGroupId')
        if m.get('ShopGroupName') is not None:
            self.shop_group_name = m.get('ShopGroupName')
        return self


class ListShopGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        shop_group_id: str = None,
        shop_group_name: str = None,
    ):
        self.shop_group_id = shop_group_id
        self.shop_group_name = shop_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.shop_group_id is not None:
            result['ShopGroupId'] = self.shop_group_id
        if self.shop_group_name is not None:
            result['ShopGroupName'] = self.shop_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShopGroupId') is not None:
            self.shop_group_id = m.get('ShopGroupId')
        if m.get('ShopGroupName') is not None:
            self.shop_group_name = m.get('ShopGroupName')
        return self


class ListShopGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListShopGroupResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListShopGroupResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
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


class ListShopGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListShopGroupResponseBody = None,
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
            temp_model = ListShopGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushStoreSpeechDataRequestSpeechContents(TeaModel):
    def __init__(
        self,
        content: str = None,
        placeholder: str = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.placeholder = placeholder

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.placeholder is not None:
            result['Placeholder'] = self.placeholder
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Placeholder') is not None:
            self.placeholder = m.get('Placeholder')
        return self


class PushStoreSpeechDataRequestSpeech(TeaModel):
    def __init__(
        self,
        contents: List[PushStoreSpeechDataRequestSpeechContents] = None,
        speech: bool = None,
        speed: str = None,
        type: str = None,
        voice: str = None,
        volume: int = None,
    ):
        self.contents = contents
        self.speech = speech
        self.speed = speed
        # This parameter is required.
        self.type = type
        self.voice = voice
        self.volume = volume

    def validate(self):
        if self.contents:
            for k in self.contents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Contents'] = []
        if self.contents is not None:
            for k in self.contents:
                result['Contents'].append(k.to_map() if k else None)
        if self.speech is not None:
            result['Speech'] = self.speech
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.type is not None:
            result['Type'] = self.type
        if self.voice is not None:
            result['Voice'] = self.voice
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contents = []
        if m.get('Contents') is not None:
            for k in m.get('Contents'):
                temp_model = PushStoreSpeechDataRequestSpeechContents()
                self.contents.append(temp_model.from_map(k))
        if m.get('Speech') is not None:
            self.speech = m.get('Speech')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Voice') is not None:
            self.voice = m.get('Voice')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class PushStoreSpeechDataRequest(TeaModel):
    def __init__(
        self,
        speech: List[PushStoreSpeechDataRequestSpeech] = None,
        store_id: str = None,
        country: str = None,
    ):
        # This parameter is required.
        self.speech = speech
        # This parameter is required.
        self.store_id = store_id
        self.country = country

    def validate(self):
        if self.speech:
            for k in self.speech:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Speech'] = []
        if self.speech is not None:
            for k in self.speech:
                result['Speech'].append(k.to_map() if k else None)
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.country is not None:
            result['country'] = self.country
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.speech = []
        if m.get('Speech') is not None:
            for k in m.get('Speech'):
                temp_model = PushStoreSpeechDataRequestSpeech()
                self.speech.append(temp_model.from_map(k))
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('country') is not None:
            self.country = m.get('country')
        return self


class PushStoreSpeechDataShrinkRequest(TeaModel):
    def __init__(
        self,
        speech_shrink: str = None,
        store_id: str = None,
        country: str = None,
    ):
        # This parameter is required.
        self.speech_shrink = speech_shrink
        # This parameter is required.
        self.store_id = store_id
        self.country = country

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.speech_shrink is not None:
            result['Speech'] = self.speech_shrink
        if self.store_id is not None:
            result['StoreId'] = self.store_id
        if self.country is not None:
            result['country'] = self.country
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Speech') is not None:
            self.speech_shrink = m.get('Speech')
        if m.get('StoreId') is not None:
            self.store_id = m.get('StoreId')
        if m.get('country') is not None:
            self.country = m.get('country')
        return self


class PushStoreSpeechDataResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PushStoreSpeechDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushStoreSpeechDataResponseBody = None,
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
            temp_model = PushStoreSpeechDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceDataListRequest(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.device_name = device_name
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryDeviceDataListResponseBodyData(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        business_status: str = None,
        city: str = None,
        device_group_list: str = None,
        device_model: str = None,
        device_name: str = None,
        device_specific_model: str = None,
        device_type: str = None,
        last_online_time: str = None,
        mac: str = None,
        province: str = None,
        region: str = None,
        region_address: str = None,
        shop_id: str = None,
        shop_name: str = None,
        sn: str = None,
        status: str = None,
    ):
        self.app_version = app_version
        self.business_status = business_status
        self.city = city
        self.device_group_list = device_group_list
        self.device_model = device_model
        self.device_name = device_name
        self.device_specific_model = device_specific_model
        self.device_type = device_type
        self.last_online_time = last_online_time
        self.mac = mac
        self.province = province
        self.region = region
        self.region_address = region_address
        self.shop_id = shop_id
        self.shop_name = shop_name
        # SN
        self.sn = sn
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.city is not None:
            result['City'] = self.city
        if self.device_group_list is not None:
            result['DeviceGroupList'] = self.device_group_list
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_specific_model is not None:
            result['DeviceSpecificModel'] = self.device_specific_model
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.last_online_time is not None:
            result['LastOnlineTime'] = self.last_online_time
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.province is not None:
            result['Province'] = self.province
        if self.region is not None:
            result['Region'] = self.region
        if self.region_address is not None:
            result['RegionAddress'] = self.region_address
        if self.shop_id is not None:
            result['ShopId'] = self.shop_id
        if self.shop_name is not None:
            result['ShopName'] = self.shop_name
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('DeviceGroupList') is not None:
            self.device_group_list = m.get('DeviceGroupList')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceSpecificModel') is not None:
            self.device_specific_model = m.get('DeviceSpecificModel')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('LastOnlineTime') is not None:
            self.last_online_time = m.get('LastOnlineTime')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RegionAddress') is not None:
            self.region_address = m.get('RegionAddress')
        if m.get('ShopId') is not None:
            self.shop_id = m.get('ShopId')
        if m.get('ShopName') is not None:
            self.shop_name = m.get('ShopName')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryDeviceDataListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[QueryDeviceDataListResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        # The returned data.
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryDeviceDataListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
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


class QueryDeviceDataListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDeviceDataListResponseBody = None,
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
            temp_model = QueryDeviceDataListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaultBriefListRequest(TeaModel):
    def __init__(
        self,
        shop_id_list: List[str] = None,
    ):
        self.shop_id_list = shop_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.shop_id_list is not None:
            result['ShopIdList'] = self.shop_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShopIdList') is not None:
            self.shop_id_list = m.get('ShopIdList')
        return self


class QueryFaultBriefListShrinkRequest(TeaModel):
    def __init__(
        self,
        shop_id_list_shrink: str = None,
    ):
        self.shop_id_list_shrink = shop_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.shop_id_list_shrink is not None:
            result['ShopIdList'] = self.shop_id_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShopIdList') is not None:
            self.shop_id_list_shrink = m.get('ShopIdList')
        return self


class QueryFaultBriefListResponseBodyData(TeaModel):
    def __init__(
        self,
        fault_num: int = None,
        fault_type: int = None,
        recovery_num: int = None,
    ):
        self.fault_num = fault_num
        self.fault_type = fault_type
        self.recovery_num = recovery_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fault_num is not None:
            result['FaultNum'] = self.fault_num
        if self.fault_type is not None:
            result['FaultType'] = self.fault_type
        if self.recovery_num is not None:
            result['RecoveryNum'] = self.recovery_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaultNum') is not None:
            self.fault_num = m.get('FaultNum')
        if m.get('FaultType') is not None:
            self.fault_type = m.get('FaultType')
        if m.get('RecoveryNum') is not None:
            self.recovery_num = m.get('RecoveryNum')
        return self


class QueryFaultBriefListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[QueryFaultBriefListResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryFaultBriefListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaultBriefListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryFaultBriefListResponseBody = None,
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
            temp_model = QueryFaultBriefListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaultDeviceListRequest(TeaModel):
    def __init__(
        self,
        daily_online_time: int = None,
        end_date: str = None,
        fault_type: str = None,
        page_number: int = None,
        page_size: int = None,
        shop_id_list: List[str] = None,
        start_date: str = None,
    ):
        self.daily_online_time = daily_online_time
        self.end_date = end_date
        self.fault_type = fault_type
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.shop_id_list = shop_id_list
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.daily_online_time is not None:
            result['DailyOnlineTime'] = self.daily_online_time
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.fault_type is not None:
            result['FaultType'] = self.fault_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.shop_id_list is not None:
            result['ShopIdList'] = self.shop_id_list
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DailyOnlineTime') is not None:
            self.daily_online_time = m.get('DailyOnlineTime')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('FaultType') is not None:
            self.fault_type = m.get('FaultType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ShopIdList') is not None:
            self.shop_id_list = m.get('ShopIdList')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class QueryFaultDeviceListShrinkRequest(TeaModel):
    def __init__(
        self,
        daily_online_time: int = None,
        end_date: str = None,
        fault_type: str = None,
        page_number: int = None,
        page_size: int = None,
        shop_id_list_shrink: str = None,
        start_date: str = None,
    ):
        self.daily_online_time = daily_online_time
        self.end_date = end_date
        self.fault_type = fault_type
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.shop_id_list_shrink = shop_id_list_shrink
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.daily_online_time is not None:
            result['DailyOnlineTime'] = self.daily_online_time
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.fault_type is not None:
            result['FaultType'] = self.fault_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.shop_id_list_shrink is not None:
            result['ShopIdList'] = self.shop_id_list_shrink
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DailyOnlineTime') is not None:
            self.daily_online_time = m.get('DailyOnlineTime')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('FaultType') is not None:
            self.fault_type = m.get('FaultType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ShopIdList') is not None:
            self.shop_id_list_shrink = m.get('ShopIdList')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class QueryFaultDeviceListResponseBodyData(TeaModel):
    def __init__(
        self,
        belong_shop: str = None,
        daily_online_time: str = None,
        device_name: str = None,
        fault_num: int = None,
        last_online_time: str = None,
        mac: str = None,
        status: str = None,
        ticket_num: str = None,
        version: str = None,
    ):
        self.belong_shop = belong_shop
        self.daily_online_time = daily_online_time
        self.device_name = device_name
        self.fault_num = fault_num
        self.last_online_time = last_online_time
        self.mac = mac
        self.status = status
        self.ticket_num = ticket_num
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.belong_shop is not None:
            result['BelongShop'] = self.belong_shop
        if self.daily_online_time is not None:
            result['DailyOnlineTime'] = self.daily_online_time
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.fault_num is not None:
            result['FaultNum'] = self.fault_num
        if self.last_online_time is not None:
            result['LastOnlineTime'] = self.last_online_time
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.status is not None:
            result['Status'] = self.status
        if self.ticket_num is not None:
            result['TicketNum'] = self.ticket_num
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BelongShop') is not None:
            self.belong_shop = m.get('BelongShop')
        if m.get('DailyOnlineTime') is not None:
            self.daily_online_time = m.get('DailyOnlineTime')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('FaultNum') is not None:
            self.fault_num = m.get('FaultNum')
        if m.get('LastOnlineTime') is not None:
            self.last_online_time = m.get('LastOnlineTime')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TicketNum') is not None:
            self.ticket_num = m.get('TicketNum')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class QueryFaultDeviceListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[QueryFaultDeviceListResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryFaultDeviceListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
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


class QueryFaultDeviceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryFaultDeviceListResponseBody = None,
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
            temp_model = QueryFaultDeviceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryLabelRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        country: str = None,
        label: str = None,
        label_id: str = None,
        page_no: int = None,
        page_size: int = None,
        title: str = None,
    ):
        # This parameter is required.
        self.category = category
        self.country = country
        self.label = label
        self.label_id = label_id
        # This parameter is required.
        self.page_no = page_no
        # This parameter is required.
        self.page_size = page_size
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.country is not None:
            result['Country'] = self.country
        if self.label is not None:
            result['Label'] = self.label
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class QueryLabelResponseBodyData(TeaModel):
    def __init__(
        self,
        category: str = None,
        label: str = None,
        label_id: str = None,
        title: str = None,
    ):
        self.category = category
        self.label = label
        self.label_id = label_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.label is not None:
            result['Label'] = self.label
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class QueryLabelResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[QueryLabelResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total = total

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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
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
            for k in m.get('Data'):
                temp_model = QueryLabelResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
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


class QueryLabelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryLabelResponseBody = None,
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
            temp_model = QueryLabelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOperationIndexRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        end_date: str = None,
        shop_id_list: List[str] = None,
        start_date: str = None,
    ):
        self.country = country
        self.end_date = end_date
        self.shop_id_list = shop_id_list
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.shop_id_list is not None:
            result['ShopIdList'] = self.shop_id_list
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ShopIdList') is not None:
            self.shop_id_list = m.get('ShopIdList')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class QueryOperationIndexShrinkRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        end_date: str = None,
        shop_id_list_shrink: str = None,
        start_date: str = None,
    ):
        self.country = country
        self.end_date = end_date
        self.shop_id_list_shrink = shop_id_list_shrink
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.shop_id_list_shrink is not None:
            result['ShopIdList'] = self.shop_id_list_shrink
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ShopIdList') is not None:
            self.shop_id_list_shrink = m.get('ShopIdList')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class QueryOperationIndexResponseBodyDataDeviceIndex(TeaModel):
    def __init__(
        self,
        cpu_average: int = None,
        fault_device_num: int = None,
        high_freq_fault_device_num: int = None,
        network_traffic: int = None,
        normal_device_num: int = None,
        online_num: int = None,
        storage_average: int = None,
        total_working_device_num: int = None,
    ):
        self.cpu_average = cpu_average
        self.fault_device_num = fault_device_num
        self.high_freq_fault_device_num = high_freq_fault_device_num
        self.network_traffic = network_traffic
        self.normal_device_num = normal_device_num
        self.online_num = online_num
        self.storage_average = storage_average
        self.total_working_device_num = total_working_device_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_average is not None:
            result['CpuAverage'] = self.cpu_average
        if self.fault_device_num is not None:
            result['FaultDeviceNum'] = self.fault_device_num
        if self.high_freq_fault_device_num is not None:
            result['HighFreqFaultDeviceNum'] = self.high_freq_fault_device_num
        if self.network_traffic is not None:
            result['NetworkTraffic'] = self.network_traffic
        if self.normal_device_num is not None:
            result['NormalDeviceNum'] = self.normal_device_num
        if self.online_num is not None:
            result['OnlineNum'] = self.online_num
        if self.storage_average is not None:
            result['StorageAverage'] = self.storage_average
        if self.total_working_device_num is not None:
            result['TotalWorkingDeviceNum'] = self.total_working_device_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuAverage') is not None:
            self.cpu_average = m.get('CpuAverage')
        if m.get('FaultDeviceNum') is not None:
            self.fault_device_num = m.get('FaultDeviceNum')
        if m.get('HighFreqFaultDeviceNum') is not None:
            self.high_freq_fault_device_num = m.get('HighFreqFaultDeviceNum')
        if m.get('NetworkTraffic') is not None:
            self.network_traffic = m.get('NetworkTraffic')
        if m.get('NormalDeviceNum') is not None:
            self.normal_device_num = m.get('NormalDeviceNum')
        if m.get('OnlineNum') is not None:
            self.online_num = m.get('OnlineNum')
        if m.get('StorageAverage') is not None:
            self.storage_average = m.get('StorageAverage')
        if m.get('TotalWorkingDeviceNum') is not None:
            self.total_working_device_num = m.get('TotalWorkingDeviceNum')
        return self


class QueryOperationIndexResponseBodyDataShopIndex(TeaModel):
    def __init__(
        self,
        fault_shop_num: int = None,
        high_freq_fault_shop_num: int = None,
        installed_shop_num: int = None,
        net_work_shop_num: int = None,
        normal_shop_num: int = None,
        not_work_shop_num: int = None,
        shop_total: int = None,
        uphold_shop_num: int = None,
    ):
        self.fault_shop_num = fault_shop_num
        self.high_freq_fault_shop_num = high_freq_fault_shop_num
        self.installed_shop_num = installed_shop_num
        self.net_work_shop_num = net_work_shop_num
        self.normal_shop_num = normal_shop_num
        self.not_work_shop_num = not_work_shop_num
        self.shop_total = shop_total
        self.uphold_shop_num = uphold_shop_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fault_shop_num is not None:
            result['FaultShopNum'] = self.fault_shop_num
        if self.high_freq_fault_shop_num is not None:
            result['HighFreqFaultShopNum'] = self.high_freq_fault_shop_num
        if self.installed_shop_num is not None:
            result['InstalledShopNum'] = self.installed_shop_num
        if self.net_work_shop_num is not None:
            result['NetWorkShopNum'] = self.net_work_shop_num
        if self.normal_shop_num is not None:
            result['NormalShopNum'] = self.normal_shop_num
        if self.not_work_shop_num is not None:
            result['NotWorkShopNum'] = self.not_work_shop_num
        if self.shop_total is not None:
            result['ShopTotal'] = self.shop_total
        if self.uphold_shop_num is not None:
            result['UpholdShopNum'] = self.uphold_shop_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaultShopNum') is not None:
            self.fault_shop_num = m.get('FaultShopNum')
        if m.get('HighFreqFaultShopNum') is not None:
            self.high_freq_fault_shop_num = m.get('HighFreqFaultShopNum')
        if m.get('InstalledShopNum') is not None:
            self.installed_shop_num = m.get('InstalledShopNum')
        if m.get('NetWorkShopNum') is not None:
            self.net_work_shop_num = m.get('NetWorkShopNum')
        if m.get('NormalShopNum') is not None:
            self.normal_shop_num = m.get('NormalShopNum')
        if m.get('NotWorkShopNum') is not None:
            self.not_work_shop_num = m.get('NotWorkShopNum')
        if m.get('ShopTotal') is not None:
            self.shop_total = m.get('ShopTotal')
        if m.get('UpholdShopNum') is not None:
            self.uphold_shop_num = m.get('UpholdShopNum')
        return self


class QueryOperationIndexResponseBodyDataTicketIndex(TeaModel):
    def __init__(
        self,
        auto_recover_rate: float = None,
        auto_recover_ticket_num: int = None,
        open_ticket_num: int = None,
        recover_rate: float = None,
        total_ticket_num: int = None,
    ):
        self.auto_recover_rate = auto_recover_rate
        self.auto_recover_ticket_num = auto_recover_ticket_num
        self.open_ticket_num = open_ticket_num
        self.recover_rate = recover_rate
        self.total_ticket_num = total_ticket_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_recover_rate is not None:
            result['AutoRecoverRate'] = self.auto_recover_rate
        if self.auto_recover_ticket_num is not None:
            result['AutoRecoverTicketNum'] = self.auto_recover_ticket_num
        if self.open_ticket_num is not None:
            result['OpenTicketNum'] = self.open_ticket_num
        if self.recover_rate is not None:
            result['RecoverRate'] = self.recover_rate
        if self.total_ticket_num is not None:
            result['TotalTicketNum'] = self.total_ticket_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRecoverRate') is not None:
            self.auto_recover_rate = m.get('AutoRecoverRate')
        if m.get('AutoRecoverTicketNum') is not None:
            self.auto_recover_ticket_num = m.get('AutoRecoverTicketNum')
        if m.get('OpenTicketNum') is not None:
            self.open_ticket_num = m.get('OpenTicketNum')
        if m.get('RecoverRate') is not None:
            self.recover_rate = m.get('RecoverRate')
        if m.get('TotalTicketNum') is not None:
            self.total_ticket_num = m.get('TotalTicketNum')
        return self


class QueryOperationIndexResponseBodyData(TeaModel):
    def __init__(
        self,
        device_index: QueryOperationIndexResponseBodyDataDeviceIndex = None,
        shop_index: QueryOperationIndexResponseBodyDataShopIndex = None,
        ticket_index: QueryOperationIndexResponseBodyDataTicketIndex = None,
    ):
        self.device_index = device_index
        self.shop_index = shop_index
        self.ticket_index = ticket_index

    def validate(self):
        if self.device_index:
            self.device_index.validate()
        if self.shop_index:
            self.shop_index.validate()
        if self.ticket_index:
            self.ticket_index.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_index is not None:
            result['DeviceIndex'] = self.device_index.to_map()
        if self.shop_index is not None:
            result['ShopIndex'] = self.shop_index.to_map()
        if self.ticket_index is not None:
            result['TicketIndex'] = self.ticket_index.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceIndex') is not None:
            temp_model = QueryOperationIndexResponseBodyDataDeviceIndex()
            self.device_index = temp_model.from_map(m['DeviceIndex'])
        if m.get('ShopIndex') is not None:
            temp_model = QueryOperationIndexResponseBodyDataShopIndex()
            self.shop_index = temp_model.from_map(m['ShopIndex'])
        if m.get('TicketIndex') is not None:
            temp_model = QueryOperationIndexResponseBodyDataTicketIndex()
            self.ticket_index = temp_model.from_map(m['TicketIndex'])
        return self


class QueryOperationIndexResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryOperationIndexResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # The returned data.
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = QueryOperationIndexResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryOperationIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryOperationIndexResponseBody = None,
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
            temp_model = QueryOperationIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryShopIndexRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        shop_id_list: List[str] = None,
    ):
        self.country = country
        self.shop_id_list = shop_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.shop_id_list is not None:
            result['ShopIdList'] = self.shop_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('ShopIdList') is not None:
            self.shop_id_list = m.get('ShopIdList')
        return self


class QueryShopIndexShrinkRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        shop_id_list_shrink: str = None,
    ):
        self.country = country
        self.shop_id_list_shrink = shop_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.shop_id_list_shrink is not None:
            result['ShopIdList'] = self.shop_id_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('ShopIdList') is not None:
            self.shop_id_list_shrink = m.get('ShopIdList')
        return self


class QueryShopIndexResponseBodyDataShopIndex(TeaModel):
    def __init__(
        self,
        fault_shop_num: int = None,
        high_freq_fault_shop_num: int = None,
        installed_shop_num: int = None,
        net_work_shop_num: int = None,
        normal_shop_num: int = None,
        not_work_shop_num: int = None,
        shop_total: int = None,
        uphold_shop_num: int = None,
    ):
        self.fault_shop_num = fault_shop_num
        self.high_freq_fault_shop_num = high_freq_fault_shop_num
        self.installed_shop_num = installed_shop_num
        self.net_work_shop_num = net_work_shop_num
        self.normal_shop_num = normal_shop_num
        self.not_work_shop_num = not_work_shop_num
        self.shop_total = shop_total
        self.uphold_shop_num = uphold_shop_num

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fault_shop_num is not None:
            result['FaultShopNum'] = self.fault_shop_num
        if self.high_freq_fault_shop_num is not None:
            result['HighFreqFaultShopNum'] = self.high_freq_fault_shop_num
        if self.installed_shop_num is not None:
            result['InstalledShopNum'] = self.installed_shop_num
        if self.net_work_shop_num is not None:
            result['NetWorkShopNum'] = self.net_work_shop_num
        if self.normal_shop_num is not None:
            result['NormalShopNum'] = self.normal_shop_num
        if self.not_work_shop_num is not None:
            result['NotWorkShopNum'] = self.not_work_shop_num
        if self.shop_total is not None:
            result['ShopTotal'] = self.shop_total
        if self.uphold_shop_num is not None:
            result['UpholdShopNum'] = self.uphold_shop_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaultShopNum') is not None:
            self.fault_shop_num = m.get('FaultShopNum')
        if m.get('HighFreqFaultShopNum') is not None:
            self.high_freq_fault_shop_num = m.get('HighFreqFaultShopNum')
        if m.get('InstalledShopNum') is not None:
            self.installed_shop_num = m.get('InstalledShopNum')
        if m.get('NetWorkShopNum') is not None:
            self.net_work_shop_num = m.get('NetWorkShopNum')
        if m.get('NormalShopNum') is not None:
            self.normal_shop_num = m.get('NormalShopNum')
        if m.get('NotWorkShopNum') is not None:
            self.not_work_shop_num = m.get('NotWorkShopNum')
        if m.get('ShopTotal') is not None:
            self.shop_total = m.get('ShopTotal')
        if m.get('UpholdShopNum') is not None:
            self.uphold_shop_num = m.get('UpholdShopNum')
        return self


class QueryShopIndexResponseBodyDataShopScheduleIndexFailShops(TeaModel):
    def __init__(
        self,
        shop_id: str = None,
        shop_name: str = None,
    ):
        self.shop_id = shop_id
        self.shop_name = shop_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.shop_id is not None:
            result['ShopId'] = self.shop_id
        if self.shop_name is not None:
            result['ShopName'] = self.shop_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShopId') is not None:
            self.shop_id = m.get('ShopId')
        if m.get('ShopName') is not None:
            self.shop_name = m.get('ShopName')
        return self


class QueryShopIndexResponseBodyDataShopScheduleIndex(TeaModel):
    def __init__(
        self,
        cost_time: float = None,
        fail_shop_num: int = None,
        fail_shops: List[QueryShopIndexResponseBodyDataShopScheduleIndexFailShops] = None,
        schedule_num: int = None,
        schedule_shop_num: int = None,
        success_rate: float = None,
    ):
        self.cost_time = cost_time
        self.fail_shop_num = fail_shop_num
        self.fail_shops = fail_shops
        self.schedule_num = schedule_num
        self.schedule_shop_num = schedule_shop_num
        self.success_rate = success_rate

    def validate(self):
        if self.fail_shops:
            for k in self.fail_shops:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.fail_shop_num is not None:
            result['FailShopNum'] = self.fail_shop_num
        result['FailShops'] = []
        if self.fail_shops is not None:
            for k in self.fail_shops:
                result['FailShops'].append(k.to_map() if k else None)
        if self.schedule_num is not None:
            result['ScheduleNum'] = self.schedule_num
        if self.schedule_shop_num is not None:
            result['ScheduleShopNum'] = self.schedule_shop_num
        if self.success_rate is not None:
            result['SuccessRate'] = self.success_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('FailShopNum') is not None:
            self.fail_shop_num = m.get('FailShopNum')
        self.fail_shops = []
        if m.get('FailShops') is not None:
            for k in m.get('FailShops'):
                temp_model = QueryShopIndexResponseBodyDataShopScheduleIndexFailShops()
                self.fail_shops.append(temp_model.from_map(k))
        if m.get('ScheduleNum') is not None:
            self.schedule_num = m.get('ScheduleNum')
        if m.get('ScheduleShopNum') is not None:
            self.schedule_shop_num = m.get('ScheduleShopNum')
        if m.get('SuccessRate') is not None:
            self.success_rate = m.get('SuccessRate')
        return self


class QueryShopIndexResponseBodyData(TeaModel):
    def __init__(
        self,
        shop_index: QueryShopIndexResponseBodyDataShopIndex = None,
        shop_schedule_index: QueryShopIndexResponseBodyDataShopScheduleIndex = None,
    ):
        self.shop_index = shop_index
        self.shop_schedule_index = shop_schedule_index

    def validate(self):
        if self.shop_index:
            self.shop_index.validate()
        if self.shop_schedule_index:
            self.shop_schedule_index.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.shop_index is not None:
            result['ShopIndex'] = self.shop_index.to_map()
        if self.shop_schedule_index is not None:
            result['ShopScheduleIndex'] = self.shop_schedule_index.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShopIndex') is not None:
            temp_model = QueryShopIndexResponseBodyDataShopIndex()
            self.shop_index = temp_model.from_map(m['ShopIndex'])
        if m.get('ShopScheduleIndex') is not None:
            temp_model = QueryShopIndexResponseBodyDataShopScheduleIndex()
            self.shop_schedule_index = temp_model.from_map(m['ShopScheduleIndex'])
        return self


class QueryShopIndexResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryShopIndexResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # The returned data.
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = QueryShopIndexResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryShopIndexResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryShopIndexResponseBody = None,
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
            temp_model = QueryShopIndexResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTicketListRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        end_time: int = None,
        page_number: int = None,
        page_size: int = None,
        shop_id_list: List[str] = None,
        start_time: int = None,
        status: int = None,
        ticket_id_list: List[str] = None,
        ticket_type_list: List[str] = None,
    ):
        self.country = country
        self.end_time = end_time
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.shop_id_list = shop_id_list
        self.start_time = start_time
        self.status = status
        self.ticket_id_list = ticket_id_list
        self.ticket_type_list = ticket_type_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.shop_id_list is not None:
            result['ShopIdList'] = self.shop_id_list
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.ticket_id_list is not None:
            result['TicketIdList'] = self.ticket_id_list
        if self.ticket_type_list is not None:
            result['TicketTypeList'] = self.ticket_type_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ShopIdList') is not None:
            self.shop_id_list = m.get('ShopIdList')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TicketIdList') is not None:
            self.ticket_id_list = m.get('TicketIdList')
        if m.get('TicketTypeList') is not None:
            self.ticket_type_list = m.get('TicketTypeList')
        return self


class QueryTicketListShrinkRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        end_time: int = None,
        page_number: int = None,
        page_size: int = None,
        shop_id_list_shrink: str = None,
        start_time: int = None,
        status: int = None,
        ticket_id_list_shrink: str = None,
        ticket_type_list_shrink: str = None,
    ):
        self.country = country
        self.end_time = end_time
        # This parameter is required.
        self.page_number = page_number
        # This parameter is required.
        self.page_size = page_size
        self.shop_id_list_shrink = shop_id_list_shrink
        self.start_time = start_time
        self.status = status
        self.ticket_id_list_shrink = ticket_id_list_shrink
        self.ticket_type_list_shrink = ticket_type_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.shop_id_list_shrink is not None:
            result['ShopIdList'] = self.shop_id_list_shrink
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.ticket_id_list_shrink is not None:
            result['TicketIdList'] = self.ticket_id_list_shrink
        if self.ticket_type_list_shrink is not None:
            result['TicketTypeList'] = self.ticket_type_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ShopIdList') is not None:
            self.shop_id_list_shrink = m.get('ShopIdList')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TicketIdList') is not None:
            self.ticket_id_list_shrink = m.get('TicketIdList')
        if m.get('TicketTypeList') is not None:
            self.ticket_type_list_shrink = m.get('TicketTypeList')
        return self


class QueryTicketListResponseBodyData(TeaModel):
    def __init__(
        self,
        device_alias: str = None,
        device_sn: str = None,
        shop_id: str = None,
        shop_name: str = None,
        status: int = None,
        submit_date: int = None,
        ticket_id: str = None,
        ticket_type: str = None,
        update_date: int = None,
    ):
        self.device_alias = device_alias
        self.device_sn = device_sn
        self.shop_id = shop_id
        self.shop_name = shop_name
        self.status = status
        self.submit_date = submit_date
        self.ticket_id = ticket_id
        self.ticket_type = ticket_type
        self.update_date = update_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_alias is not None:
            result['DeviceAlias'] = self.device_alias
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.shop_id is not None:
            result['ShopId'] = self.shop_id
        if self.shop_name is not None:
            result['ShopName'] = self.shop_name
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_date is not None:
            result['SubmitDate'] = self.submit_date
        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id
        if self.ticket_type is not None:
            result['TicketType'] = self.ticket_type
        if self.update_date is not None:
            result['UpdateDate'] = self.update_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceAlias') is not None:
            self.device_alias = m.get('DeviceAlias')
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('ShopId') is not None:
            self.shop_id = m.get('ShopId')
        if m.get('ShopName') is not None:
            self.shop_name = m.get('ShopName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitDate') is not None:
            self.submit_date = m.get('SubmitDate')
        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')
        if m.get('TicketType') is not None:
            self.ticket_type = m.get('TicketType')
        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')
        return self


class QueryTicketListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[QueryTicketListResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryTicketListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
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


class QueryTicketListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryTicketListResponseBody = None,
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
            temp_model = QueryTicketListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveShopFromGroupRequest(TeaModel):
    def __init__(
        self,
        shop_group_id: str = None,
        shop_id_list: List[str] = None,
    ):
        # This parameter is required.
        self.shop_group_id = shop_group_id
        self.shop_id_list = shop_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.shop_group_id is not None:
            result['ShopGroupId'] = self.shop_group_id
        if self.shop_id_list is not None:
            result['ShopIdList'] = self.shop_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShopGroupId') is not None:
            self.shop_group_id = m.get('ShopGroupId')
        if m.get('ShopIdList') is not None:
            self.shop_id_list = m.get('ShopIdList')
        return self


class RemoveShopFromGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        shop_group_id: str = None,
        shop_id_list_shrink: str = None,
    ):
        # This parameter is required.
        self.shop_group_id = shop_group_id
        self.shop_id_list_shrink = shop_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.shop_group_id is not None:
            result['ShopGroupId'] = self.shop_group_id
        if self.shop_id_list_shrink is not None:
            result['ShopIdList'] = self.shop_id_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ShopGroupId') is not None:
            self.shop_group_id = m.get('ShopGroupId')
        if m.get('ShopIdList') is not None:
            self.shop_id_list_shrink = m.get('ShopIdList')
        return self


class RemoveShopFromGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveShopFromGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveShopFromGroupResponseBody = None,
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
            temp_model = RemoveShopFromGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveShopsFromGroupRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        shop_group_id: str = None,
        shop_id_list: List[str] = None,
    ):
        self.country = country
        # This parameter is required.
        self.shop_group_id = shop_group_id
        # This parameter is required.
        self.shop_id_list = shop_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.shop_group_id is not None:
            result['ShopGroupId'] = self.shop_group_id
        if self.shop_id_list is not None:
            result['ShopIdList'] = self.shop_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('ShopGroupId') is not None:
            self.shop_group_id = m.get('ShopGroupId')
        if m.get('ShopIdList') is not None:
            self.shop_id_list = m.get('ShopIdList')
        return self


class RemoveShopsFromGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        shop_group_id: str = None,
        shop_id_list_shrink: str = None,
    ):
        self.country = country
        # This parameter is required.
        self.shop_group_id = shop_group_id
        # This parameter is required.
        self.shop_id_list_shrink = shop_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.shop_group_id is not None:
            result['ShopGroupId'] = self.shop_group_id
        if self.shop_id_list_shrink is not None:
            result['ShopIdList'] = self.shop_id_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('ShopGroupId') is not None:
            self.shop_group_id = m.get('ShopGroupId')
        if m.get('ShopIdList') is not None:
            self.shop_id_list_shrink = m.get('ShopIdList')
        return self


class RemoveShopsFromGroupResponseBodyData(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        shop_id: str = None,
    ):
        self.code = code
        self.message = message
        self.shop_id = shop_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.shop_id is not None:
            result['ShopId'] = self.shop_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ShopId') is not None:
            self.shop_id = m.get('ShopId')
        return self


class RemoveShopsFromGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[RemoveShopsFromGroupResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = RemoveShopsFromGroupResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveShopsFromGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveShopsFromGroupResponseBody = None,
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
            temp_model = RemoveShopsFromGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLabelRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        label: str = None,
        label_id: str = None,
        title: str = None,
    ):
        self.country = country
        self.label = label
        # This parameter is required.
        self.label_id = label_id
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.label is not None:
            result['Label'] = self.label
        if self.label_id is not None:
            result['LabelId'] = self.label_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('LabelId') is not None:
            self.label_id = m.get('LabelId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateLabelResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateLabelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLabelResponseBody = None,
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
            temp_model = UpdateLabelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateShopRequest(TeaModel):
    def __init__(
        self,
        business_status: int = None,
        country: str = None,
        latitude: str = None,
        location: str = None,
        longitude: str = None,
        region_address: str = None,
        region_code: str = None,
        remark: str = None,
        shop_group_ids: List[str] = None,
        shop_id: str = None,
        shop_name: str = None,
        weekdays_end_time: str = None,
        weekdays_start_time: str = None,
        weekend_end_time: str = None,
        weekend_start_time: str = None,
    ):
        self.business_status = business_status
        self.country = country
        self.latitude = latitude
        self.location = location
        self.longitude = longitude
        self.region_address = region_address
        self.region_code = region_code
        self.remark = remark
        self.shop_group_ids = shop_group_ids
        # This parameter is required.
        self.shop_id = shop_id
        # This parameter is required.
        self.shop_name = shop_name
        self.weekdays_end_time = weekdays_end_time
        self.weekdays_start_time = weekdays_start_time
        self.weekend_end_time = weekend_end_time
        self.weekend_start_time = weekend_start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.country is not None:
            result['Country'] = self.country
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.location is not None:
            result['Location'] = self.location
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.region_address is not None:
            result['RegionAddress'] = self.region_address
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.shop_group_ids is not None:
            result['ShopGroupIds'] = self.shop_group_ids
        if self.shop_id is not None:
            result['ShopId'] = self.shop_id
        if self.shop_name is not None:
            result['ShopName'] = self.shop_name
        if self.weekdays_end_time is not None:
            result['WeekdaysEndTime'] = self.weekdays_end_time
        if self.weekdays_start_time is not None:
            result['WeekdaysStartTime'] = self.weekdays_start_time
        if self.weekend_end_time is not None:
            result['WeekendEndTime'] = self.weekend_end_time
        if self.weekend_start_time is not None:
            result['WeekendStartTime'] = self.weekend_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('RegionAddress') is not None:
            self.region_address = m.get('RegionAddress')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ShopGroupIds') is not None:
            self.shop_group_ids = m.get('ShopGroupIds')
        if m.get('ShopId') is not None:
            self.shop_id = m.get('ShopId')
        if m.get('ShopName') is not None:
            self.shop_name = m.get('ShopName')
        if m.get('WeekdaysEndTime') is not None:
            self.weekdays_end_time = m.get('WeekdaysEndTime')
        if m.get('WeekdaysStartTime') is not None:
            self.weekdays_start_time = m.get('WeekdaysStartTime')
        if m.get('WeekendEndTime') is not None:
            self.weekend_end_time = m.get('WeekendEndTime')
        if m.get('WeekendStartTime') is not None:
            self.weekend_start_time = m.get('WeekendStartTime')
        return self


class UpdateShopShrinkRequest(TeaModel):
    def __init__(
        self,
        business_status: int = None,
        country: str = None,
        latitude: str = None,
        location: str = None,
        longitude: str = None,
        region_address: str = None,
        region_code: str = None,
        remark: str = None,
        shop_group_ids_shrink: str = None,
        shop_id: str = None,
        shop_name: str = None,
        weekdays_end_time: str = None,
        weekdays_start_time: str = None,
        weekend_end_time: str = None,
        weekend_start_time: str = None,
    ):
        self.business_status = business_status
        self.country = country
        self.latitude = latitude
        self.location = location
        self.longitude = longitude
        self.region_address = region_address
        self.region_code = region_code
        self.remark = remark
        self.shop_group_ids_shrink = shop_group_ids_shrink
        # This parameter is required.
        self.shop_id = shop_id
        # This parameter is required.
        self.shop_name = shop_name
        self.weekdays_end_time = weekdays_end_time
        self.weekdays_start_time = weekdays_start_time
        self.weekend_end_time = weekend_end_time
        self.weekend_start_time = weekend_start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status
        if self.country is not None:
            result['Country'] = self.country
        if self.latitude is not None:
            result['Latitude'] = self.latitude
        if self.location is not None:
            result['Location'] = self.location
        if self.longitude is not None:
            result['Longitude'] = self.longitude
        if self.region_address is not None:
            result['RegionAddress'] = self.region_address
        if self.region_code is not None:
            result['RegionCode'] = self.region_code
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.shop_group_ids_shrink is not None:
            result['ShopGroupIds'] = self.shop_group_ids_shrink
        if self.shop_id is not None:
            result['ShopId'] = self.shop_id
        if self.shop_name is not None:
            result['ShopName'] = self.shop_name
        if self.weekdays_end_time is not None:
            result['WeekdaysEndTime'] = self.weekdays_end_time
        if self.weekdays_start_time is not None:
            result['WeekdaysStartTime'] = self.weekdays_start_time
        if self.weekend_end_time is not None:
            result['WeekendEndTime'] = self.weekend_end_time
        if self.weekend_start_time is not None:
            result['WeekendStartTime'] = self.weekend_start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')
        if m.get('Location') is not None:
            self.location = m.get('Location')
        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')
        if m.get('RegionAddress') is not None:
            self.region_address = m.get('RegionAddress')
        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ShopGroupIds') is not None:
            self.shop_group_ids_shrink = m.get('ShopGroupIds')
        if m.get('ShopId') is not None:
            self.shop_id = m.get('ShopId')
        if m.get('ShopName') is not None:
            self.shop_name = m.get('ShopName')
        if m.get('WeekdaysEndTime') is not None:
            self.weekdays_end_time = m.get('WeekdaysEndTime')
        if m.get('WeekdaysStartTime') is not None:
            self.weekdays_start_time = m.get('WeekdaysStartTime')
        if m.get('WeekendEndTime') is not None:
            self.weekend_end_time = m.get('WeekendEndTime')
        if m.get('WeekendStartTime') is not None:
            self.weekend_start_time = m.get('WeekendStartTime')
        return self


class UpdateShopResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateShopResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateShopResponseBody = None,
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
            temp_model = UpdateShopResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateShopGroupRequest(TeaModel):
    def __init__(
        self,
        country: str = None,
        shop_group_id: str = None,
        shop_group_name: str = None,
    ):
        self.country = country
        # This parameter is required.
        self.shop_group_id = shop_group_id
        # This parameter is required.
        self.shop_group_name = shop_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country is not None:
            result['Country'] = self.country
        if self.shop_group_id is not None:
            result['ShopGroupId'] = self.shop_group_id
        if self.shop_group_name is not None:
            result['ShopGroupName'] = self.shop_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('ShopGroupId') is not None:
            self.shop_group_id = m.get('ShopGroupId')
        if m.get('ShopGroupName') is not None:
            self.shop_group_name = m.get('ShopGroupName')
        return self


class UpdateShopGroupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
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
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateShopGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateShopGroupResponseBody = None,
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
            temp_model = UpdateShopGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSpeechTemplateRequest(TeaModel):
    def __init__(
        self,
        contents: str = None,
        type: str = None,
        country: str = None,
    ):
        # This parameter is required.
        self.contents = contents
        # This parameter is required.
        self.type = type
        self.country = country

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contents is not None:
            result['Contents'] = self.contents
        if self.type is not None:
            result['Type'] = self.type
        if self.country is not None:
            result['country'] = self.country
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contents') is not None:
            self.contents = m.get('Contents')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('country') is not None:
            self.country = m.get('country')
        return self


class UpdateSpeechTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateSpeechTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSpeechTemplateResponseBody = None,
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
            temp_model = UpdateSpeechTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


