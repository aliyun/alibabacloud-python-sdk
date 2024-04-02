# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AuditItemSubmitRequestData(TeaModel):
    def __init__(
        self,
        custom_result: str = None,
        custom_risk_type: str = None,
        id: int = None,
    ):
        self.custom_result = custom_result
        self.custom_risk_type = custom_risk_type
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_result is not None:
            result['CustomResult'] = self.custom_result
        if self.custom_risk_type is not None:
            result['CustomRiskType'] = self.custom_risk_type
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomResult') is not None:
            self.custom_result = m.get('CustomResult')
        if m.get('CustomRiskType') is not None:
            self.custom_risk_type = m.get('CustomRiskType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class AuditItemSubmitRequest(TeaModel):
    def __init__(
        self,
        data: List[AuditItemSubmitRequestData] = None,
    ):
        self.data = data

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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AuditItemSubmitRequestData()
                self.data.append(temp_model.from_map(k))
        return self


class AuditItemSubmitResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AuditItemSubmitResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AuditItemSubmitResponseBody = None,
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
            temp_model = AuditItemSubmitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatCustomOcrTemplateRequest(TeaModel):
    def __init__(
        self,
        img_url: str = None,
        name: str = None,
        recognize_area: str = None,
        refer_area: str = None,
    ):
        self.img_url = img_url
        self.name = name
        self.recognize_area = recognize_area
        self.refer_area = refer_area

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.img_url is not None:
            result['ImgUrl'] = self.img_url
        if self.name is not None:
            result['Name'] = self.name
        if self.recognize_area is not None:
            result['RecognizeArea'] = self.recognize_area
        if self.refer_area is not None:
            result['ReferArea'] = self.refer_area
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImgUrl') is not None:
            self.img_url = m.get('ImgUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RecognizeArea') is not None:
            self.recognize_area = m.get('RecognizeArea')
        if m.get('ReferArea') is not None:
            self.refer_area = m.get('ReferArea')
        return self


class CreatCustomOcrTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatCustomOcrTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatCustomOcrTemplateResponseBody = None,
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
            temp_model = CreatCustomOcrTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAuditCallbackRequest(TeaModel):
    def __init__(
        self,
        callback_suggestions: str = None,
        callback_types: str = None,
        crypt_type: str = None,
        name: str = None,
        url: str = None,
    ):
        self.callback_suggestions = callback_suggestions
        self.callback_types = callback_types
        self.crypt_type = crypt_type
        self.name = name
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_suggestions is not None:
            result['CallbackSuggestions'] = self.callback_suggestions
        if self.callback_types is not None:
            result['CallbackTypes'] = self.callback_types
        if self.crypt_type is not None:
            result['CryptType'] = self.crypt_type
        if self.name is not None:
            result['Name'] = self.name
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackSuggestions') is not None:
            self.callback_suggestions = m.get('CallbackSuggestions')
        if m.get('CallbackTypes') is not None:
            self.callback_types = m.get('CallbackTypes')
        if m.get('CryptType') is not None:
            self.crypt_type = m.get('CryptType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateAuditCallbackResponseBody(TeaModel):
    def __init__(
        self,
        callback_suggestions: List[str] = None,
        callback_types: List[str] = None,
        create_time: str = None,
        crypt_type: str = None,
        id: int = None,
        modified_time: str = None,
        name: str = None,
        request_id: str = None,
        seed: str = None,
        url: str = None,
    ):
        self.callback_suggestions = callback_suggestions
        self.callback_types = callback_types
        self.create_time = create_time
        self.crypt_type = crypt_type
        self.id = id
        self.modified_time = modified_time
        self.name = name
        self.request_id = request_id
        self.seed = seed
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_suggestions is not None:
            result['CallbackSuggestions'] = self.callback_suggestions
        if self.callback_types is not None:
            result['CallbackTypes'] = self.callback_types
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.crypt_type is not None:
            result['CryptType'] = self.crypt_type
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.seed is not None:
            result['Seed'] = self.seed
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackSuggestions') is not None:
            self.callback_suggestions = m.get('CallbackSuggestions')
        if m.get('CallbackTypes') is not None:
            self.callback_types = m.get('CallbackTypes')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CryptType') is not None:
            self.crypt_type = m.get('CryptType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Seed') is not None:
            self.seed = m.get('Seed')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateAuditCallbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAuditCallbackResponseBody = None,
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
            temp_model = CreateAuditCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBizTypeRequest(TeaModel):
    def __init__(
        self,
        biz_type_import: str = None,
        biz_type_name: str = None,
        cite_template: bool = None,
        description: str = None,
        industry_info: str = None,
    ):
        self.biz_type_import = biz_type_import
        self.biz_type_name = biz_type_name
        self.cite_template = cite_template
        self.description = description
        self.industry_info = industry_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_import is not None:
            result['BizTypeImport'] = self.biz_type_import
        if self.biz_type_name is not None:
            result['BizTypeName'] = self.biz_type_name
        if self.cite_template is not None:
            result['CiteTemplate'] = self.cite_template
        if self.description is not None:
            result['Description'] = self.description
        if self.industry_info is not None:
            result['IndustryInfo'] = self.industry_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTypeImport') is not None:
            self.biz_type_import = m.get('BizTypeImport')
        if m.get('BizTypeName') is not None:
            self.biz_type_name = m.get('BizTypeName')
        if m.get('CiteTemplate') is not None:
            self.cite_template = m.get('CiteTemplate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IndustryInfo') is not None:
            self.industry_info = m.get('IndustryInfo')
        return self


class CreateBizTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBizTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateBizTypeResponseBody = None,
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
            temp_model = CreateBizTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCdiBagRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        commodity_code: str = None,
        flow_out_spec: int = None,
        order_num: int = None,
        order_type: str = None,
        owner_id: int = None,
    ):
        self.client_token = client_token
        self.commodity_code = commodity_code
        self.flow_out_spec = flow_out_spec
        self.order_num = order_num
        self.order_type = order_type
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.flow_out_spec is not None:
            result['FlowOutSpec'] = self.flow_out_spec
        if self.order_num is not None:
            result['OrderNum'] = self.order_num
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('FlowOutSpec') is not None:
            self.flow_out_spec = m.get('FlowOutSpec')
        if m.get('OrderNum') is not None:
            self.order_num = m.get('OrderNum')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class CreateCdiBagResponseBodyInstanceIds(TeaModel):
    def __init__(
        self,
        string: List[str] = None,
    ):
        self.string = string

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.string is not None:
            result['String'] = self.string
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('String') is not None:
            self.string = m.get('String')
        return self


class CreateCdiBagResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        instance_ids: CreateCdiBagResponseBodyInstanceIds = None,
        message: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.instance_ids = instance_ids
        self.message = message
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceIds') is not None:
            temp_model = CreateCdiBagResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m['InstanceIds'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCdiBagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCdiBagResponseBody = None,
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
            temp_model = CreateCdiBagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCdiBaseBagRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        commodity_code: str = None,
        duration: int = None,
        flow_out_spec: int = None,
        order_type: str = None,
        owner_id: int = None,
    ):
        self.client_token = client_token
        self.commodity_code = commodity_code
        self.duration = duration
        self.flow_out_spec = flow_out_spec
        self.order_type = order_type
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.flow_out_spec is not None:
            result['FlowOutSpec'] = self.flow_out_spec
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('FlowOutSpec') is not None:
            self.flow_out_spec = m.get('FlowOutSpec')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class CreateCdiBaseBagResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        instance_id: str = None,
        message: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.instance_id = instance_id
        self.message = message
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCdiBaseBagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCdiBaseBagResponseBody = None,
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
            temp_model = CreateCdiBaseBagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageLibRequest(TeaModel):
    def __init__(
        self,
        biz_types: str = None,
        category: str = None,
        enable: bool = None,
        name: str = None,
        scene: str = None,
        service_module: str = None,
        source_ip: str = None,
    ):
        self.biz_types = biz_types
        self.category = category
        self.enable = enable
        self.name = name
        self.scene = scene
        self.service_module = service_module
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_types is not None:
            result['BizTypes'] = self.biz_types
        if self.category is not None:
            result['Category'] = self.category
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.name is not None:
            result['Name'] = self.name
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.service_module is not None:
            result['ServiceModule'] = self.service_module
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTypes') is not None:
            self.biz_types = m.get('BizTypes')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('ServiceModule') is not None:
            self.service_module = m.get('ServiceModule')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class CreateImageLibResponseBody(TeaModel):
    def __init__(
        self,
        id: int = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateImageLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateImageLibResponseBody = None,
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
            temp_model = CreateImageLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateKeywordRequest(TeaModel):
    def __init__(
        self,
        keyword_lib_id: int = None,
        keywords: str = None,
        lang: str = None,
        source_ip: str = None,
    ):
        self.keyword_lib_id = keyword_lib_id
        self.keywords = keywords
        self.lang = lang
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword_lib_id is not None:
            result['KeywordLibId'] = self.keyword_lib_id
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeywordLibId') is not None:
            self.keyword_lib_id = m.get('KeywordLibId')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class CreateKeywordResponseBodyValidKeywordList(TeaModel):
    def __init__(
        self,
        id: int = None,
        keyword: str = None,
    ):
        self.id = id
        self.keyword = keyword

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.keyword is not None:
            result['keyword'] = self.keyword
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        return self


class CreateKeywordResponseBody(TeaModel):
    def __init__(
        self,
        invalid_keyword_list: List[str] = None,
        request_id: str = None,
        success_count: int = None,
        valid_keyword_list: List[CreateKeywordResponseBodyValidKeywordList] = None,
    ):
        self.invalid_keyword_list = invalid_keyword_list
        self.request_id = request_id
        self.success_count = success_count
        self.valid_keyword_list = valid_keyword_list

    def validate(self):
        if self.valid_keyword_list:
            for k in self.valid_keyword_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invalid_keyword_list is not None:
            result['InvalidKeywordList'] = self.invalid_keyword_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        result['validKeywordList'] = []
        if self.valid_keyword_list is not None:
            for k in self.valid_keyword_list:
                result['validKeywordList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvalidKeywordList') is not None:
            self.invalid_keyword_list = m.get('InvalidKeywordList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        self.valid_keyword_list = []
        if m.get('validKeywordList') is not None:
            for k in m.get('validKeywordList'):
                temp_model = CreateKeywordResponseBodyValidKeywordList()
                self.valid_keyword_list.append(temp_model.from_map(k))
        return self


class CreateKeywordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateKeywordResponseBody = None,
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
            temp_model = CreateKeywordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateKeywordLibRequest(TeaModel):
    def __init__(
        self,
        biz_types: str = None,
        category: str = None,
        enable: bool = None,
        lang: str = None,
        language: str = None,
        lib_type: str = None,
        match_mode: str = None,
        name: str = None,
        resource_type: str = None,
        service_module: str = None,
        source_ip: str = None,
    ):
        self.biz_types = biz_types
        self.category = category
        self.enable = enable
        self.lang = lang
        self.language = language
        self.lib_type = lib_type
        self.match_mode = match_mode
        self.name = name
        self.resource_type = resource_type
        self.service_module = service_module
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_types is not None:
            result['BizTypes'] = self.biz_types
        if self.category is not None:
            result['Category'] = self.category
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.language is not None:
            result['Language'] = self.language
        if self.lib_type is not None:
            result['LibType'] = self.lib_type
        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_module is not None:
            result['ServiceModule'] = self.service_module
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTypes') is not None:
            self.biz_types = m.get('BizTypes')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LibType') is not None:
            self.lib_type = m.get('LibType')
        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceModule') is not None:
            self.service_module = m.get('ServiceModule')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class CreateKeywordLibResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateKeywordLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateKeywordLibResponseBody = None,
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
            temp_model = CreateKeywordLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWebSiteInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        duration: int = None,
        order_num: int = None,
        order_type: str = None,
        owner_id: int = None,
        pricing_cycle: str = None,
    ):
        self.client_token = client_token
        self.duration = duration
        self.order_num = order_num
        self.order_type = order_type
        self.owner_id = owner_id
        self.pricing_cycle = pricing_cycle

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.order_num is not None:
            result['OrderNum'] = self.order_num
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('OrderNum') is not None:
            self.order_num = m.get('OrderNum')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        return self


class CreateWebSiteInstanceResponseBodyInstanceIds(TeaModel):
    def __init__(
        self,
        string: List[str] = None,
    ):
        self.string = string

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.string is not None:
            result['String'] = self.string
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('String') is not None:
            self.string = m.get('String')
        return self


class CreateWebSiteInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        instance_ids: CreateWebSiteInstanceResponseBodyInstanceIds = None,
        message: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.instance_ids = instance_ids
        self.message = message
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceIds') is not None:
            temp_model = CreateWebSiteInstanceResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m['InstanceIds'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateWebSiteInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateWebSiteInstanceResponseBody = None,
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
            temp_model = CreateWebSiteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateWebsiteIndexPageBaselineRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        lang: str = None,
        source_ip: str = None,
    ):
        self.instance_id = instance_id
        self.lang = lang
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class CreateWebsiteIndexPageBaselineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateWebsiteIndexPageBaselineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateWebsiteIndexPageBaselineResponseBody = None,
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
            temp_model = CreateWebsiteIndexPageBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBizTypeRequest(TeaModel):
    def __init__(
        self,
        biz_type_name: str = None,
    ):
        self.biz_type_name = biz_type_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_name is not None:
            result['BizTypeName'] = self.biz_type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTypeName') is not None:
            self.biz_type_name = m.get('BizTypeName')
        return self


class DeleteBizTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteBizTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteBizTypeResponseBody = None,
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
            temp_model = DeleteBizTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomOcrTemplateRequest(TeaModel):
    def __init__(
        self,
        ids: str = None,
    ):
        self.ids = ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        return self


class DeleteCustomOcrTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteCustomOcrTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCustomOcrTemplateResponseBody = None,
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
            temp_model = DeleteCustomOcrTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImageFromLibRequest(TeaModel):
    def __init__(
        self,
        ids: str = None,
        source_ip: str = None,
    ):
        self.ids = ids
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DeleteImageFromLibResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteImageFromLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteImageFromLibResponseBody = None,
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
            temp_model = DeleteImageFromLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteImageLibRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        source_ip: str = None,
    ):
        self.id = id
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DeleteImageLibResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteImageLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteImageLibResponseBody = None,
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
            temp_model = DeleteImageLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteKeywordRequest(TeaModel):
    def __init__(
        self,
        ids: str = None,
        keyword_lib_id: str = None,
        keywords: str = None,
        lang: str = None,
        source_ip: str = None,
    ):
        self.ids = ids
        self.keyword_lib_id = keyword_lib_id
        self.keywords = keywords
        self.lang = lang
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.keyword_lib_id is not None:
            result['KeywordLibId'] = self.keyword_lib_id
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('KeywordLibId') is not None:
            self.keyword_lib_id = m.get('KeywordLibId')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DeleteKeywordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteKeywordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteKeywordResponseBody = None,
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
            temp_model = DeleteKeywordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteKeywordLibRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        lang: str = None,
        source_ip: str = None,
    ):
        self.id = id
        self.lang = lang
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DeleteKeywordLibResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteKeywordLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteKeywordLibResponseBody = None,
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
            temp_model = DeleteKeywordLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNotificationContactsRequest(TeaModel):
    def __init__(
        self,
        contact_types: str = None,
        lang: str = None,
        source_ip: str = None,
    ):
        self.contact_types = contact_types
        self.lang = lang
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_types is not None:
            result['ContactTypes'] = self.contact_types
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactTypes') is not None:
            self.contact_types = m.get('ContactTypes')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DeleteNotificationContactsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteNotificationContactsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteNotificationContactsResponseBody = None,
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
            temp_model = DeleteNotificationContactsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppInfoRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        platform: str = None,
        source_ip: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.lang = lang
        self.page_size = page_size
        self.platform = platform
        self.source_ip = source_ip
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAppInfoResponseBodyAppInfoListDebugPackageInfo(TeaModel):
    def __init__(
        self,
        version: str = None,
    ):
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeAppInfoResponseBodyAppInfoListPackageInfo(TeaModel):
    def __init__(
        self,
        version: str = None,
    ):
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeAppInfoResponseBodyAppInfoList(TeaModel):
    def __init__(
        self,
        debug_package_info: DescribeAppInfoResponseBodyAppInfoListDebugPackageInfo = None,
        end_date: str = None,
        icon: str = None,
        id: int = None,
        name: str = None,
        package_info: DescribeAppInfoResponseBodyAppInfoListPackageInfo = None,
        package_name: str = None,
        start_date: str = None,
        type: int = None,
    ):
        self.debug_package_info = debug_package_info
        self.end_date = end_date
        self.icon = icon
        self.id = id
        self.name = name
        self.package_info = package_info
        self.package_name = package_name
        self.start_date = start_date
        self.type = type

    def validate(self):
        if self.debug_package_info:
            self.debug_package_info.validate()
        if self.package_info:
            self.package_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debug_package_info is not None:
            result['DebugPackageInfo'] = self.debug_package_info.to_map()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.package_info is not None:
            result['PackageInfo'] = self.package_info.to_map()
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebugPackageInfo') is not None:
            temp_model = DescribeAppInfoResponseBodyAppInfoListDebugPackageInfo()
            self.debug_package_info = temp_model.from_map(m['DebugPackageInfo'])
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PackageInfo') is not None:
            temp_model = DescribeAppInfoResponseBodyAppInfoListPackageInfo()
            self.package_info = temp_model.from_map(m['PackageInfo'])
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeAppInfoResponseBody(TeaModel):
    def __init__(
        self,
        app_info_list: List[DescribeAppInfoResponseBodyAppInfoList] = None,
        current_page: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.app_info_list = app_info_list
        self.current_page = current_page
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.app_info_list:
            for k in self.app_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppInfoList'] = []
        if self.app_info_list is not None:
            for k in self.app_info_list:
                result['AppInfoList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_info_list = []
        if m.get('AppInfoList') is not None:
            for k in m.get('AppInfoList'):
                temp_model = DescribeAppInfoResponseBodyAppInfoList()
                self.app_info_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAppInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAppInfoResponseBody = None,
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
            temp_model = DescribeAppInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditCallbackResponseBody(TeaModel):
    def __init__(
        self,
        callback: str = None,
        crypt_type: int = None,
        request_id: str = None,
        seed: str = None,
    ):
        self.callback = callback
        self.crypt_type = crypt_type
        self.request_id = request_id
        self.seed = seed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.crypt_type is not None:
            result['CryptType'] = self.crypt_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.seed is not None:
            result['Seed'] = self.seed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CryptType') is not None:
            self.crypt_type = m.get('CryptType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Seed') is not None:
            self.seed = m.get('Seed')
        return self


class DescribeAuditCallbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAuditCallbackResponseBody = None,
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
            temp_model = DescribeAuditCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditCallbackListResponseBodyCallbackList(TeaModel):
    def __init__(
        self,
        callback_suggestions: List[str] = None,
        callback_types: List[str] = None,
        create_time: str = None,
        crypt_type: str = None,
        id: int = None,
        modified_time: str = None,
        name: str = None,
        seed: str = None,
        url: str = None,
    ):
        self.callback_suggestions = callback_suggestions
        self.callback_types = callback_types
        self.create_time = create_time
        self.crypt_type = crypt_type
        self.id = id
        self.modified_time = modified_time
        self.name = name
        self.seed = seed
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_suggestions is not None:
            result['CallbackSuggestions'] = self.callback_suggestions
        if self.callback_types is not None:
            result['CallbackTypes'] = self.callback_types
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.crypt_type is not None:
            result['CryptType'] = self.crypt_type
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.seed is not None:
            result['Seed'] = self.seed
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackSuggestions') is not None:
            self.callback_suggestions = m.get('CallbackSuggestions')
        if m.get('CallbackTypes') is not None:
            self.callback_types = m.get('CallbackTypes')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CryptType') is not None:
            self.crypt_type = m.get('CryptType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Seed') is not None:
            self.seed = m.get('Seed')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeAuditCallbackListResponseBody(TeaModel):
    def __init__(
        self,
        callback_list: List[DescribeAuditCallbackListResponseBodyCallbackList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.callback_list = callback_list
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.callback_list:
            for k in self.callback_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CallbackList'] = []
        if self.callback_list is not None:
            for k in self.callback_list:
                result['CallbackList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.callback_list = []
        if m.get('CallbackList') is not None:
            for k in m.get('CallbackList'):
                temp_model = DescribeAuditCallbackListResponseBodyCallbackList()
                self.callback_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAuditCallbackListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAuditCallbackListResponseBody = None,
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
            temp_model = DescribeAuditCallbackListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditContentRequest(TeaModel):
    def __init__(
        self,
        audit_result: str = None,
        biz_type: str = None,
        current_page: int = None,
        data_id: str = None,
        end_date: str = None,
        image_id: str = None,
        keyword_id: str = None,
        label: str = None,
        lang: str = None,
        lib_type: str = None,
        page_size: int = None,
        resource_type: str = None,
        scene: str = None,
        source_ip: str = None,
        start_date: str = None,
        suggestion: str = None,
        task_id: str = None,
        total_count: int = None,
    ):
        self.audit_result = audit_result
        self.biz_type = biz_type
        self.current_page = current_page
        self.data_id = data_id
        self.end_date = end_date
        self.image_id = image_id
        self.keyword_id = keyword_id
        self.label = label
        self.lang = lang
        self.lib_type = lib_type
        self.page_size = page_size
        self.resource_type = resource_type
        self.scene = scene
        self.source_ip = source_ip
        self.start_date = start_date
        self.suggestion = suggestion
        self.task_id = task_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_result is not None:
            result['AuditResult'] = self.audit_result
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.keyword_id is not None:
            result['KeywordId'] = self.keyword_id
        if self.label is not None:
            result['Label'] = self.label
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.lib_type is not None:
            result['LibType'] = self.lib_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditResult') is not None:
            self.audit_result = m.get('AuditResult')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('KeywordId') is not None:
            self.keyword_id = m.get('KeywordId')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('LibType') is not None:
            self.lib_type = m.get('LibType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAuditContentResponseBodyAuditContentListFrameResults(TeaModel):
    def __init__(
        self,
        label: str = None,
        offset: int = None,
        url: str = None,
    ):
        self.label = label
        self.offset = offset
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeAuditContentResponseBodyAuditContentListResults(TeaModel):
    def __init__(
        self,
        label: str = None,
        scene: str = None,
        suggestion: str = None,
    ):
        self.label = label
        self.scene = scene
        self.suggestion = suggestion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        return self


class DescribeAuditContentResponseBodyAuditContentList(TeaModel):
    def __init__(
        self,
        audit: int = None,
        audit_illegal_reasons: List[str] = None,
        audit_result: str = None,
        biz_type: str = None,
        content: str = None,
        data_id: str = None,
        frame_results: List[DescribeAuditContentResponseBodyAuditContentListFrameResults] = None,
        id: int = None,
        new_url: str = None,
        request_time: str = None,
        results: List[DescribeAuditContentResponseBodyAuditContentListResults] = None,
        scan_finished_time: str = None,
        suggestion: str = None,
        task_id: str = None,
        thumbnail: str = None,
        url: str = None,
    ):
        self.audit = audit
        self.audit_illegal_reasons = audit_illegal_reasons
        self.audit_result = audit_result
        self.biz_type = biz_type
        self.content = content
        self.data_id = data_id
        self.frame_results = frame_results
        self.id = id
        self.new_url = new_url
        self.request_time = request_time
        self.results = results
        self.scan_finished_time = scan_finished_time
        self.suggestion = suggestion
        self.task_id = task_id
        self.thumbnail = thumbnail
        self.url = url

    def validate(self):
        if self.frame_results:
            for k in self.frame_results:
                if k:
                    k.validate()
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit is not None:
            result['Audit'] = self.audit
        if self.audit_illegal_reasons is not None:
            result['AuditIllegalReasons'] = self.audit_illegal_reasons
        if self.audit_result is not None:
            result['AuditResult'] = self.audit_result
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.content is not None:
            result['Content'] = self.content
        if self.data_id is not None:
            result['DataId'] = self.data_id
        result['FrameResults'] = []
        if self.frame_results is not None:
            for k in self.frame_results:
                result['FrameResults'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        if self.new_url is not None:
            result['NewUrl'] = self.new_url
        if self.request_time is not None:
            result['RequestTime'] = self.request_time
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.scan_finished_time is not None:
            result['ScanFinishedTime'] = self.scan_finished_time
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.thumbnail is not None:
            result['Thumbnail'] = self.thumbnail
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audit') is not None:
            self.audit = m.get('Audit')
        if m.get('AuditIllegalReasons') is not None:
            self.audit_illegal_reasons = m.get('AuditIllegalReasons')
        if m.get('AuditResult') is not None:
            self.audit_result = m.get('AuditResult')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        self.frame_results = []
        if m.get('FrameResults') is not None:
            for k in m.get('FrameResults'):
                temp_model = DescribeAuditContentResponseBodyAuditContentListFrameResults()
                self.frame_results.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NewUrl') is not None:
            self.new_url = m.get('NewUrl')
        if m.get('RequestTime') is not None:
            self.request_time = m.get('RequestTime')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = DescribeAuditContentResponseBodyAuditContentListResults()
                self.results.append(temp_model.from_map(k))
        if m.get('ScanFinishedTime') is not None:
            self.scan_finished_time = m.get('ScanFinishedTime')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Thumbnail') is not None:
            self.thumbnail = m.get('Thumbnail')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeAuditContentResponseBody(TeaModel):
    def __init__(
        self,
        audit_content_list: List[DescribeAuditContentResponseBodyAuditContentList] = None,
        current_page: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.audit_content_list = audit_content_list
        self.current_page = current_page
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.audit_content_list:
            for k in self.audit_content_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AuditContentList'] = []
        if self.audit_content_list is not None:
            for k in self.audit_content_list:
                result['AuditContentList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audit_content_list = []
        if m.get('AuditContentList') is not None:
            for k in m.get('AuditContentList'):
                temp_model = DescribeAuditContentResponseBodyAuditContentList()
                self.audit_content_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAuditContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAuditContentResponseBody = None,
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
            temp_model = DescribeAuditContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditContentItemRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        resource_type: str = None,
        source_ip: str = None,
        task_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.lang = lang
        self.page_size = page_size
        self.resource_type = resource_type
        self.source_ip = source_ip
        self.task_id = task_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAuditContentItemResponseBodyAuditContentItemList(TeaModel):
    def __init__(
        self,
        audit: int = None,
        audit_illegal_reasons: List[str] = None,
        audit_result: str = None,
        content: str = None,
        end_time: str = None,
        id: int = None,
        parent_task_id: str = None,
        sn: int = None,
        start_time: str = None,
        suggestion: str = None,
    ):
        self.audit = audit
        self.audit_illegal_reasons = audit_illegal_reasons
        self.audit_result = audit_result
        self.content = content
        self.end_time = end_time
        self.id = id
        self.parent_task_id = parent_task_id
        self.sn = sn
        self.start_time = start_time
        self.suggestion = suggestion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit is not None:
            result['Audit'] = self.audit
        if self.audit_illegal_reasons is not None:
            result['AuditIllegalReasons'] = self.audit_illegal_reasons
        if self.audit_result is not None:
            result['AuditResult'] = self.audit_result
        if self.content is not None:
            result['Content'] = self.content
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.parent_task_id is not None:
            result['ParentTaskId'] = self.parent_task_id
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audit') is not None:
            self.audit = m.get('Audit')
        if m.get('AuditIllegalReasons') is not None:
            self.audit_illegal_reasons = m.get('AuditIllegalReasons')
        if m.get('AuditResult') is not None:
            self.audit_result = m.get('AuditResult')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ParentTaskId') is not None:
            self.parent_task_id = m.get('ParentTaskId')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        return self


class DescribeAuditContentItemResponseBody(TeaModel):
    def __init__(
        self,
        audit_content_item_list: List[DescribeAuditContentItemResponseBodyAuditContentItemList] = None,
        current_page: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.audit_content_item_list = audit_content_item_list
        self.current_page = current_page
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.audit_content_item_list:
            for k in self.audit_content_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AuditContentItemList'] = []
        if self.audit_content_item_list is not None:
            for k in self.audit_content_item_list:
                result['AuditContentItemList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audit_content_item_list = []
        if m.get('AuditContentItemList') is not None:
            for k in m.get('AuditContentItemList'):
                temp_model = DescribeAuditContentItemResponseBodyAuditContentItemList()
                self.audit_content_item_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAuditContentItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAuditContentItemResponseBody = None,
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
            temp_model = DescribeAuditContentItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditRangeResponseBodyAuditRange(TeaModel):
    def __init__(
        self,
        block: bool = None,
        pass_: bool = None,
        review: bool = None,
    ):
        self.block = block
        self.pass_ = pass_
        self.review = review

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block is not None:
            result['block'] = self.block
        if self.pass_ is not None:
            result['pass'] = self.pass_
        if self.review is not None:
            result['review'] = self.review
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('block') is not None:
            self.block = m.get('block')
        if m.get('pass') is not None:
            self.pass_ = m.get('pass')
        if m.get('review') is not None:
            self.review = m.get('review')
        return self


class DescribeAuditRangeResponseBody(TeaModel):
    def __init__(
        self,
        audit_range: DescribeAuditRangeResponseBodyAuditRange = None,
        request_id: str = None,
    ):
        self.audit_range = audit_range
        self.request_id = request_id

    def validate(self):
        if self.audit_range:
            self.audit_range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_range is not None:
            result['AuditRange'] = self.audit_range.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditRange') is not None:
            temp_model = DescribeAuditRangeResponseBodyAuditRange()
            self.audit_range = temp_model.from_map(m['AuditRange'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeAuditRangeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAuditRangeResponseBody = None,
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
            temp_model = DescribeAuditRangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAuditSettingRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
    ):
        self.lang = lang
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeAuditSettingResponseBodyAuditRange(TeaModel):
    def __init__(
        self,
        block: bool = None,
        pass_: bool = None,
        review: bool = None,
    ):
        self.block = block
        self.pass_ = pass_
        self.review = review

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block is not None:
            result['block'] = self.block
        if self.pass_ is not None:
            result['pass'] = self.pass_
        if self.review is not None:
            result['review'] = self.review
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('block') is not None:
            self.block = m.get('block')
        if m.get('pass') is not None:
            self.pass_ = m.get('pass')
        if m.get('review') is not None:
            self.review = m.get('review')
        return self


class DescribeAuditSettingResponseBody(TeaModel):
    def __init__(
        self,
        audit_range: DescribeAuditSettingResponseBodyAuditRange = None,
        callback: str = None,
        request_id: str = None,
        seed: str = None,
    ):
        self.audit_range = audit_range
        self.callback = callback
        self.request_id = request_id
        self.seed = seed

    def validate(self):
        if self.audit_range:
            self.audit_range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_range is not None:
            result['AuditRange'] = self.audit_range.to_map()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.seed is not None:
            result['Seed'] = self.seed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditRange') is not None:
            temp_model = DescribeAuditSettingResponseBodyAuditRange()
            self.audit_range = temp_model.from_map(m['AuditRange'])
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Seed') is not None:
            self.seed = m.get('Seed')
        return self


class DescribeAuditSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAuditSettingResponseBody = None,
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
            temp_model = DescribeAuditSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBizTypeImageLibRequest(TeaModel):
    def __init__(
        self,
        biz_type_name: str = None,
        resource_type: str = None,
        scene: str = None,
    ):
        self.biz_type_name = biz_type_name
        self.resource_type = resource_type
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_name is not None:
            result['BizTypeName'] = self.biz_type_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTypeName') is not None:
            self.biz_type_name = m.get('BizTypeName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class DescribeBizTypeImageLibResponseBodyBlackAll(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeImageLibResponseBodyBlackSelected(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeImageLibResponseBodyBlack(TeaModel):
    def __init__(
        self,
        all: List[DescribeBizTypeImageLibResponseBodyBlackAll] = None,
        selected: List[DescribeBizTypeImageLibResponseBodyBlackSelected] = None,
    ):
        self.all = all
        self.selected = selected

    def validate(self):
        if self.all:
            for k in self.all:
                if k:
                    k.validate()
        if self.selected:
            for k in self.selected:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['All'] = []
        if self.all is not None:
            for k in self.all:
                result['All'].append(k.to_map() if k else None)
        result['Selected'] = []
        if self.selected is not None:
            for k in self.selected:
                result['Selected'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.all = []
        if m.get('All') is not None:
            for k in m.get('All'):
                temp_model = DescribeBizTypeImageLibResponseBodyBlackAll()
                self.all.append(temp_model.from_map(k))
        self.selected = []
        if m.get('Selected') is not None:
            for k in m.get('Selected'):
                temp_model = DescribeBizTypeImageLibResponseBodyBlackSelected()
                self.selected.append(temp_model.from_map(k))
        return self


class DescribeBizTypeImageLibResponseBodyReviewAll(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeImageLibResponseBodyReviewSelected(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeImageLibResponseBodyReview(TeaModel):
    def __init__(
        self,
        all: List[DescribeBizTypeImageLibResponseBodyReviewAll] = None,
        selected: List[DescribeBizTypeImageLibResponseBodyReviewSelected] = None,
    ):
        self.all = all
        self.selected = selected

    def validate(self):
        if self.all:
            for k in self.all:
                if k:
                    k.validate()
        if self.selected:
            for k in self.selected:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['All'] = []
        if self.all is not None:
            for k in self.all:
                result['All'].append(k.to_map() if k else None)
        result['Selected'] = []
        if self.selected is not None:
            for k in self.selected:
                result['Selected'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.all = []
        if m.get('All') is not None:
            for k in m.get('All'):
                temp_model = DescribeBizTypeImageLibResponseBodyReviewAll()
                self.all.append(temp_model.from_map(k))
        self.selected = []
        if m.get('Selected') is not None:
            for k in m.get('Selected'):
                temp_model = DescribeBizTypeImageLibResponseBodyReviewSelected()
                self.selected.append(temp_model.from_map(k))
        return self


class DescribeBizTypeImageLibResponseBodyWhiteAll(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeImageLibResponseBodyWhiteSelected(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeImageLibResponseBodyWhite(TeaModel):
    def __init__(
        self,
        all: List[DescribeBizTypeImageLibResponseBodyWhiteAll] = None,
        selected: List[DescribeBizTypeImageLibResponseBodyWhiteSelected] = None,
    ):
        self.all = all
        self.selected = selected

    def validate(self):
        if self.all:
            for k in self.all:
                if k:
                    k.validate()
        if self.selected:
            for k in self.selected:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['All'] = []
        if self.all is not None:
            for k in self.all:
                result['All'].append(k.to_map() if k else None)
        result['Selected'] = []
        if self.selected is not None:
            for k in self.selected:
                result['Selected'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.all = []
        if m.get('All') is not None:
            for k in m.get('All'):
                temp_model = DescribeBizTypeImageLibResponseBodyWhiteAll()
                self.all.append(temp_model.from_map(k))
        self.selected = []
        if m.get('Selected') is not None:
            for k in m.get('Selected'):
                temp_model = DescribeBizTypeImageLibResponseBodyWhiteSelected()
                self.selected.append(temp_model.from_map(k))
        return self


class DescribeBizTypeImageLibResponseBody(TeaModel):
    def __init__(
        self,
        black: DescribeBizTypeImageLibResponseBodyBlack = None,
        request_id: str = None,
        review: DescribeBizTypeImageLibResponseBodyReview = None,
        white: DescribeBizTypeImageLibResponseBodyWhite = None,
    ):
        self.black = black
        self.request_id = request_id
        self.review = review
        self.white = white

    def validate(self):
        if self.black:
            self.black.validate()
        if self.review:
            self.review.validate()
        if self.white:
            self.white.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black is not None:
            result['Black'] = self.black.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.review is not None:
            result['Review'] = self.review.to_map()
        if self.white is not None:
            result['White'] = self.white.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Black') is not None:
            temp_model = DescribeBizTypeImageLibResponseBodyBlack()
            self.black = temp_model.from_map(m['Black'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Review') is not None:
            temp_model = DescribeBizTypeImageLibResponseBodyReview()
            self.review = temp_model.from_map(m['Review'])
        if m.get('White') is not None:
            temp_model = DescribeBizTypeImageLibResponseBodyWhite()
            self.white = temp_model.from_map(m['White'])
        return self


class DescribeBizTypeImageLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBizTypeImageLibResponseBody = None,
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
            temp_model = DescribeBizTypeImageLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBizTypeSettingRequest(TeaModel):
    def __init__(
        self,
        biz_type_name: str = None,
        resource_type: str = None,
    ):
        self.biz_type_name = biz_type_name
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_name is not None:
            result['BizTypeName'] = self.biz_type_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTypeName') is not None:
            self.biz_type_name = m.get('BizTypeName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DescribeBizTypeSettingResponseBodyAd(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
    ):
        self.categories = categories

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeBizTypeSettingResponseBodyAntispam(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
    ):
        self.categories = categories

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeBizTypeSettingResponseBodyLive(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
    ):
        self.categories = categories

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeBizTypeSettingResponseBodyPorn(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
    ):
        self.categories = categories

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeBizTypeSettingResponseBodyTerrorism(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
    ):
        self.categories = categories

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeBizTypeSettingResponseBody(TeaModel):
    def __init__(
        self,
        ad: DescribeBizTypeSettingResponseBodyAd = None,
        antispam: DescribeBizTypeSettingResponseBodyAntispam = None,
        live: DescribeBizTypeSettingResponseBodyLive = None,
        porn: DescribeBizTypeSettingResponseBodyPorn = None,
        request_id: str = None,
        terrorism: DescribeBizTypeSettingResponseBodyTerrorism = None,
    ):
        self.ad = ad
        self.antispam = antispam
        self.live = live
        self.porn = porn
        self.request_id = request_id
        self.terrorism = terrorism

    def validate(self):
        if self.ad:
            self.ad.validate()
        if self.antispam:
            self.antispam.validate()
        if self.live:
            self.live.validate()
        if self.porn:
            self.porn.validate()
        if self.terrorism:
            self.terrorism.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad is not None:
            result['Ad'] = self.ad.to_map()
        if self.antispam is not None:
            result['Antispam'] = self.antispam.to_map()
        if self.live is not None:
            result['Live'] = self.live.to_map()
        if self.porn is not None:
            result['Porn'] = self.porn.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.terrorism is not None:
            result['Terrorism'] = self.terrorism.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ad') is not None:
            temp_model = DescribeBizTypeSettingResponseBodyAd()
            self.ad = temp_model.from_map(m['Ad'])
        if m.get('Antispam') is not None:
            temp_model = DescribeBizTypeSettingResponseBodyAntispam()
            self.antispam = temp_model.from_map(m['Antispam'])
        if m.get('Live') is not None:
            temp_model = DescribeBizTypeSettingResponseBodyLive()
            self.live = temp_model.from_map(m['Live'])
        if m.get('Porn') is not None:
            temp_model = DescribeBizTypeSettingResponseBodyPorn()
            self.porn = temp_model.from_map(m['Porn'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Terrorism') is not None:
            temp_model = DescribeBizTypeSettingResponseBodyTerrorism()
            self.terrorism = temp_model.from_map(m['Terrorism'])
        return self


class DescribeBizTypeSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBizTypeSettingResponseBody = None,
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
            temp_model = DescribeBizTypeSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBizTypeTextLibRequest(TeaModel):
    def __init__(
        self,
        biz_type_name: str = None,
        resource_type: str = None,
        scene: str = None,
    ):
        self.biz_type_name = biz_type_name
        self.resource_type = resource_type
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_name is not None:
            result['BizTypeName'] = self.biz_type_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTypeName') is not None:
            self.biz_type_name = m.get('BizTypeName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class DescribeBizTypeTextLibResponseBodyBlackAll(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeTextLibResponseBodyBlackSelected(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeTextLibResponseBodyBlack(TeaModel):
    def __init__(
        self,
        all: List[DescribeBizTypeTextLibResponseBodyBlackAll] = None,
        selected: List[DescribeBizTypeTextLibResponseBodyBlackSelected] = None,
    ):
        self.all = all
        self.selected = selected

    def validate(self):
        if self.all:
            for k in self.all:
                if k:
                    k.validate()
        if self.selected:
            for k in self.selected:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['All'] = []
        if self.all is not None:
            for k in self.all:
                result['All'].append(k.to_map() if k else None)
        result['Selected'] = []
        if self.selected is not None:
            for k in self.selected:
                result['Selected'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.all = []
        if m.get('All') is not None:
            for k in m.get('All'):
                temp_model = DescribeBizTypeTextLibResponseBodyBlackAll()
                self.all.append(temp_model.from_map(k))
        self.selected = []
        if m.get('Selected') is not None:
            for k in m.get('Selected'):
                temp_model = DescribeBizTypeTextLibResponseBodyBlackSelected()
                self.selected.append(temp_model.from_map(k))
        return self


class DescribeBizTypeTextLibResponseBodyIgnoreAll(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeTextLibResponseBodyIgnoreSelected(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeTextLibResponseBodyIgnore(TeaModel):
    def __init__(
        self,
        all: List[DescribeBizTypeTextLibResponseBodyIgnoreAll] = None,
        selected: List[DescribeBizTypeTextLibResponseBodyIgnoreSelected] = None,
    ):
        self.all = all
        self.selected = selected

    def validate(self):
        if self.all:
            for k in self.all:
                if k:
                    k.validate()
        if self.selected:
            for k in self.selected:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['All'] = []
        if self.all is not None:
            for k in self.all:
                result['All'].append(k.to_map() if k else None)
        result['Selected'] = []
        if self.selected is not None:
            for k in self.selected:
                result['Selected'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.all = []
        if m.get('All') is not None:
            for k in m.get('All'):
                temp_model = DescribeBizTypeTextLibResponseBodyIgnoreAll()
                self.all.append(temp_model.from_map(k))
        self.selected = []
        if m.get('Selected') is not None:
            for k in m.get('Selected'):
                temp_model = DescribeBizTypeTextLibResponseBodyIgnoreSelected()
                self.selected.append(temp_model.from_map(k))
        return self


class DescribeBizTypeTextLibResponseBodyReviewAll(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeTextLibResponseBodyReviewSelected(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeTextLibResponseBodyReview(TeaModel):
    def __init__(
        self,
        all: List[DescribeBizTypeTextLibResponseBodyReviewAll] = None,
        selected: List[DescribeBizTypeTextLibResponseBodyReviewSelected] = None,
    ):
        self.all = all
        self.selected = selected

    def validate(self):
        if self.all:
            for k in self.all:
                if k:
                    k.validate()
        if self.selected:
            for k in self.selected:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['All'] = []
        if self.all is not None:
            for k in self.all:
                result['All'].append(k.to_map() if k else None)
        result['Selected'] = []
        if self.selected is not None:
            for k in self.selected:
                result['Selected'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.all = []
        if m.get('All') is not None:
            for k in m.get('All'):
                temp_model = DescribeBizTypeTextLibResponseBodyReviewAll()
                self.all.append(temp_model.from_map(k))
        self.selected = []
        if m.get('Selected') is not None:
            for k in m.get('Selected'):
                temp_model = DescribeBizTypeTextLibResponseBodyReviewSelected()
                self.selected.append(temp_model.from_map(k))
        return self


class DescribeBizTypeTextLibResponseBodyWhiteAll(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeTextLibResponseBodyWhiteSelected(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeBizTypeTextLibResponseBodyWhite(TeaModel):
    def __init__(
        self,
        all: List[DescribeBizTypeTextLibResponseBodyWhiteAll] = None,
        selected: List[DescribeBizTypeTextLibResponseBodyWhiteSelected] = None,
    ):
        self.all = all
        self.selected = selected

    def validate(self):
        if self.all:
            for k in self.all:
                if k:
                    k.validate()
        if self.selected:
            for k in self.selected:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['All'] = []
        if self.all is not None:
            for k in self.all:
                result['All'].append(k.to_map() if k else None)
        result['Selected'] = []
        if self.selected is not None:
            for k in self.selected:
                result['Selected'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.all = []
        if m.get('All') is not None:
            for k in m.get('All'):
                temp_model = DescribeBizTypeTextLibResponseBodyWhiteAll()
                self.all.append(temp_model.from_map(k))
        self.selected = []
        if m.get('Selected') is not None:
            for k in m.get('Selected'):
                temp_model = DescribeBizTypeTextLibResponseBodyWhiteSelected()
                self.selected.append(temp_model.from_map(k))
        return self


class DescribeBizTypeTextLibResponseBody(TeaModel):
    def __init__(
        self,
        black: DescribeBizTypeTextLibResponseBodyBlack = None,
        ignore: DescribeBizTypeTextLibResponseBodyIgnore = None,
        request_id: str = None,
        review: DescribeBizTypeTextLibResponseBodyReview = None,
        white: DescribeBizTypeTextLibResponseBodyWhite = None,
    ):
        self.black = black
        self.ignore = ignore
        self.request_id = request_id
        self.review = review
        self.white = white

    def validate(self):
        if self.black:
            self.black.validate()
        if self.ignore:
            self.ignore.validate()
        if self.review:
            self.review.validate()
        if self.white:
            self.white.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.black is not None:
            result['Black'] = self.black.to_map()
        if self.ignore is not None:
            result['Ignore'] = self.ignore.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.review is not None:
            result['Review'] = self.review.to_map()
        if self.white is not None:
            result['White'] = self.white.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Black') is not None:
            temp_model = DescribeBizTypeTextLibResponseBodyBlack()
            self.black = temp_model.from_map(m['Black'])
        if m.get('Ignore') is not None:
            temp_model = DescribeBizTypeTextLibResponseBodyIgnore()
            self.ignore = temp_model.from_map(m['Ignore'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Review') is not None:
            temp_model = DescribeBizTypeTextLibResponseBodyReview()
            self.review = temp_model.from_map(m['Review'])
        if m.get('White') is not None:
            temp_model = DescribeBizTypeTextLibResponseBodyWhite()
            self.white = temp_model.from_map(m['White'])
        return self


class DescribeBizTypeTextLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBizTypeTextLibResponseBody = None,
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
            temp_model = DescribeBizTypeTextLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBizTypesRequest(TeaModel):
    def __init__(
        self,
        import_flag: bool = None,
    ):
        self.import_flag = import_flag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.import_flag is not None:
            result['ImportFlag'] = self.import_flag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportFlag') is not None:
            self.import_flag = m.get('ImportFlag')
        return self


class DescribeBizTypesResponseBody(TeaModel):
    def __init__(
        self,
        biz_type_list: List[str] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.biz_type_list = biz_type_list
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_list is not None:
            result['BizTypeList'] = self.biz_type_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTypeList') is not None:
            self.biz_type_list = m.get('BizTypeList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeBizTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeBizTypesResponseBody = None,
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
            temp_model = DescribeBizTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCloudMonitorServicesRequest(TeaModel):
    def __init__(
        self,
        page: str = None,
        page_size: str = None,
        source_ip: str = None,
    ):
        self.page = page
        self.page_size = page_size
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeCloudMonitorServicesResponseBody(TeaModel):
    def __init__(
        self,
        items: List[str] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.items = items
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.items is not None:
            result['Items'] = self.items
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            self.items = m.get('Items')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCloudMonitorServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCloudMonitorServicesResponseBody = None,
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
            temp_model = DescribeCloudMonitorServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCustomOcrTemplateRequest(TeaModel):
    def __init__(
        self,
        ids: str = None,
    ):
        self.ids = ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        return self


class DescribeCustomOcrTemplateResponseBodyOcrTemplateListRecognizeArea(TeaModel):
    def __init__(
        self,
        height: int = None,
        name: str = None,
        width: int = None,
        x: int = None,
        y: int = None,
    ):
        self.height = height
        self.name = name
        self.width = width
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.name is not None:
            result['Name'] = self.name
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeCustomOcrTemplateResponseBodyOcrTemplateListReferArea(TeaModel):
    def __init__(
        self,
        height: int = None,
        name: str = None,
        width: int = None,
        x: int = None,
        y: int = None,
    ):
        self.height = height
        self.name = name
        self.width = width
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.name is not None:
            result['Name'] = self.name
        if self.width is not None:
            result['Width'] = self.width
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeCustomOcrTemplateResponseBodyOcrTemplateList(TeaModel):
    def __init__(
        self,
        id: int = None,
        img_url: str = None,
        name: str = None,
        recognize_area: List[DescribeCustomOcrTemplateResponseBodyOcrTemplateListRecognizeArea] = None,
        refer_area: List[DescribeCustomOcrTemplateResponseBodyOcrTemplateListReferArea] = None,
        status: int = None,
    ):
        self.id = id
        self.img_url = img_url
        self.name = name
        self.recognize_area = recognize_area
        self.refer_area = refer_area
        self.status = status

    def validate(self):
        if self.recognize_area:
            for k in self.recognize_area:
                if k:
                    k.validate()
        if self.refer_area:
            for k in self.refer_area:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.img_url is not None:
            result['ImgUrl'] = self.img_url
        if self.name is not None:
            result['Name'] = self.name
        result['RecognizeArea'] = []
        if self.recognize_area is not None:
            for k in self.recognize_area:
                result['RecognizeArea'].append(k.to_map() if k else None)
        result['ReferArea'] = []
        if self.refer_area is not None:
            for k in self.refer_area:
                result['ReferArea'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImgUrl') is not None:
            self.img_url = m.get('ImgUrl')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.recognize_area = []
        if m.get('RecognizeArea') is not None:
            for k in m.get('RecognizeArea'):
                temp_model = DescribeCustomOcrTemplateResponseBodyOcrTemplateListRecognizeArea()
                self.recognize_area.append(temp_model.from_map(k))
        self.refer_area = []
        if m.get('ReferArea') is not None:
            for k in m.get('ReferArea'):
                temp_model = DescribeCustomOcrTemplateResponseBodyOcrTemplateListReferArea()
                self.refer_area.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeCustomOcrTemplateResponseBody(TeaModel):
    def __init__(
        self,
        ocr_template_list: List[DescribeCustomOcrTemplateResponseBodyOcrTemplateList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.ocr_template_list = ocr_template_list
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.ocr_template_list:
            for k in self.ocr_template_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OcrTemplateList'] = []
        if self.ocr_template_list is not None:
            for k in self.ocr_template_list:
                result['OcrTemplateList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ocr_template_list = []
        if m.get('OcrTemplateList') is not None:
            for k in m.get('OcrTemplateList'):
                temp_model = DescribeCustomOcrTemplateResponseBodyOcrTemplateList()
                self.ocr_template_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeCustomOcrTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeCustomOcrTemplateResponseBody = None,
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
            temp_model = DescribeCustomOcrTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageFromLibRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        end_date: str = None,
        id: int = None,
        image_lib_id: int = None,
        model_id: int = None,
        page_size: int = None,
        source_ip: str = None,
        start_date: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.end_date = end_date
        self.id = id
        self.image_lib_id = image_lib_id
        self.model_id = model_id
        self.page_size = page_size
        self.source_ip = source_ip
        self.start_date = start_date
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.id is not None:
            result['Id'] = self.id
        if self.image_lib_id is not None:
            result['ImageLibId'] = self.image_lib_id
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImageLibId') is not None:
            self.image_lib_id = m.get('ImageLibId')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeImageFromLibResponseBodyImageFromLibList(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        id: int = None,
        image: str = None,
        image_hit_count: int = None,
        thumbnail: str = None,
        video_hit_count: int = None,
    ):
        self.create_time = create_time
        self.id = id
        self.image = image
        self.image_hit_count = image_hit_count
        self.thumbnail = thumbnail
        self.video_hit_count = video_hit_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.image is not None:
            result['Image'] = self.image
        if self.image_hit_count is not None:
            result['ImageHitCount'] = self.image_hit_count
        if self.thumbnail is not None:
            result['Thumbnail'] = self.thumbnail
        if self.video_hit_count is not None:
            result['VideoHitCount'] = self.video_hit_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('ImageHitCount') is not None:
            self.image_hit_count = m.get('ImageHitCount')
        if m.get('Thumbnail') is not None:
            self.thumbnail = m.get('Thumbnail')
        if m.get('VideoHitCount') is not None:
            self.video_hit_count = m.get('VideoHitCount')
        return self


class DescribeImageFromLibResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        image_from_lib_list: List[DescribeImageFromLibResponseBodyImageFromLibList] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.image_from_lib_list = image_from_lib_list
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.image_from_lib_list:
            for k in self.image_from_lib_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['ImageFromLibList'] = []
        if self.image_from_lib_list is not None:
            for k in self.image_from_lib_list:
                result['ImageFromLibList'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.image_from_lib_list = []
        if m.get('ImageFromLibList') is not None:
            for k in m.get('ImageFromLibList'):
                temp_model = DescribeImageFromLibResponseBodyImageFromLibList()
                self.image_from_lib_list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeImageFromLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeImageFromLibResponseBody = None,
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
            temp_model = DescribeImageFromLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageLibRequest(TeaModel):
    def __init__(
        self,
        service_module: str = None,
        source_ip: str = None,
    ):
        self.service_module = service_module
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_module is not None:
            result['ServiceModule'] = self.service_module
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceModule') is not None:
            self.service_module = m.get('ServiceModule')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeImageLibResponseBodyImageLibList(TeaModel):
    def __init__(
        self,
        biz_types: List[str] = None,
        category: str = None,
        code: str = None,
        enable: str = None,
        id: int = None,
        image_count: int = None,
        modified_time: str = None,
        name: str = None,
        scene: str = None,
        service_module: str = None,
        source: str = None,
    ):
        self.biz_types = biz_types
        self.category = category
        self.code = code
        self.enable = enable
        self.id = id
        self.image_count = image_count
        self.modified_time = modified_time
        self.name = name
        self.scene = scene
        self.service_module = service_module
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_types is not None:
            result['BizTypes'] = self.biz_types
        if self.category is not None:
            result['Category'] = self.category
        if self.code is not None:
            result['Code'] = self.code
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.id is not None:
            result['Id'] = self.id
        if self.image_count is not None:
            result['ImageCount'] = self.image_count
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.service_module is not None:
            result['ServiceModule'] = self.service_module
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTypes') is not None:
            self.biz_types = m.get('BizTypes')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImageCount') is not None:
            self.image_count = m.get('ImageCount')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('ServiceModule') is not None:
            self.service_module = m.get('ServiceModule')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DescribeImageLibResponseBody(TeaModel):
    def __init__(
        self,
        image_lib_list: List[DescribeImageLibResponseBodyImageLibList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.image_lib_list = image_lib_list
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.image_lib_list:
            for k in self.image_lib_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ImageLibList'] = []
        if self.image_lib_list is not None:
            for k in self.image_lib_list:
                result['ImageLibList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_lib_list = []
        if m.get('ImageLibList') is not None:
            for k in m.get('ImageLibList'):
                temp_model = DescribeImageLibResponseBodyImageLibList()
                self.image_lib_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeImageLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeImageLibResponseBody = None,
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
            temp_model = DescribeImageLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeImageUploadInfoRequest(TeaModel):
    def __init__(
        self,
        source_ip: str = None,
    ):
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeImageUploadInfoResponseBody(TeaModel):
    def __init__(
        self,
        accessid: str = None,
        expire: int = None,
        folder: str = None,
        host: str = None,
        policy: str = None,
        request_id: str = None,
        signature: str = None,
    ):
        self.accessid = accessid
        self.expire = expire
        self.folder = folder
        self.host = host
        self.policy = policy
        self.request_id = request_id
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessid is not None:
            result['Accessid'] = self.accessid
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.folder is not None:
            result['Folder'] = self.folder
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessid') is not None:
            self.accessid = m.get('Accessid')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Folder') is not None:
            self.folder = m.get('Folder')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class DescribeImageUploadInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeImageUploadInfoResponseBody = None,
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
            temp_model = DescribeImageUploadInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeKeywordRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        keyword: str = None,
        keyword_lib_id: int = None,
        lang: str = None,
        page_size: int = None,
        source_ip: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.keyword = keyword
        self.keyword_lib_id = keyword_lib_id
        self.lang = lang
        self.page_size = page_size
        self.source_ip = source_ip
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.keyword_lib_id is not None:
            result['KeywordLibId'] = self.keyword_lib_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('KeywordLibId') is not None:
            self.keyword_lib_id = m.get('KeywordLibId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeKeywordResponseBodyKeywordList(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        hit_count: int = None,
        id: int = None,
        keyword: str = None,
    ):
        self.create_time = create_time
        self.hit_count = hit_count
        self.id = id
        self.keyword = keyword

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.hit_count is not None:
            result['HitCount'] = self.hit_count
        if self.id is not None:
            result['Id'] = self.id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('HitCount') is not None:
            self.hit_count = m.get('HitCount')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        return self


class DescribeKeywordResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        keyword_list: List[DescribeKeywordResponseBodyKeywordList] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.keyword_list = keyword_list
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.keyword_list:
            for k in self.keyword_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['KeywordList'] = []
        if self.keyword_list is not None:
            for k in self.keyword_list:
                result['KeywordList'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.keyword_list = []
        if m.get('KeywordList') is not None:
            for k in m.get('KeywordList'):
                temp_model = DescribeKeywordResponseBodyKeywordList()
                self.keyword_list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeKeywordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeKeywordResponseBody = None,
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
            temp_model = DescribeKeywordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeKeywordLibRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        service_module: str = None,
        source_ip: str = None,
    ):
        self.lang = lang
        self.service_module = service_module
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.service_module is not None:
            result['ServiceModule'] = self.service_module
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ServiceModule') is not None:
            self.service_module = m.get('ServiceModule')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeKeywordLibResponseBodyKeywordLibList(TeaModel):
    def __init__(
        self,
        biz_types: List[str] = None,
        category: str = None,
        code: str = None,
        count: int = None,
        enable: bool = None,
        id: int = None,
        language: str = None,
        lib_type: str = None,
        match_mode: str = None,
        modified_time: str = None,
        name: str = None,
        resource_type: str = None,
        service_module: str = None,
        source: str = None,
    ):
        self.biz_types = biz_types
        self.category = category
        self.code = code
        self.count = count
        self.enable = enable
        self.id = id
        self.language = language
        self.lib_type = lib_type
        self.match_mode = match_mode
        self.modified_time = modified_time
        self.name = name
        self.resource_type = resource_type
        self.service_module = service_module
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_types is not None:
            result['BizTypes'] = self.biz_types
        if self.category is not None:
            result['Category'] = self.category
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.id is not None:
            result['Id'] = self.id
        if self.language is not None:
            result['Language'] = self.language
        if self.lib_type is not None:
            result['LibType'] = self.lib_type
        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_module is not None:
            result['ServiceModule'] = self.service_module
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTypes') is not None:
            self.biz_types = m.get('BizTypes')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LibType') is not None:
            self.lib_type = m.get('LibType')
        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceModule') is not None:
            self.service_module = m.get('ServiceModule')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DescribeKeywordLibResponseBody(TeaModel):
    def __init__(
        self,
        keyword_lib_list: List[DescribeKeywordLibResponseBodyKeywordLibList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.keyword_lib_list = keyword_lib_list
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.keyword_lib_list:
            for k in self.keyword_lib_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['KeywordLibList'] = []
        if self.keyword_lib_list is not None:
            for k in self.keyword_lib_list:
                result['KeywordLibList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.keyword_lib_list = []
        if m.get('KeywordLibList') is not None:
            for k in m.get('KeywordLibList'):
                temp_model = DescribeKeywordLibResponseBodyKeywordLibList()
                self.keyword_lib_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeKeywordLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeKeywordLibResponseBody = None,
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
            temp_model = DescribeKeywordLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNotificationSettingRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
    ):
        self.lang = lang
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeNotificationSettingResponseBody(TeaModel):
    def __init__(
        self,
        email: str = None,
        phone: str = None,
        realtime_message_list: List[str] = None,
        reminder_mode_list: List[str] = None,
        request_id: str = None,
        schedule_message_time: int = None,
        schedule_message_time_zone: int = None,
    ):
        self.email = email
        self.phone = phone
        self.realtime_message_list = realtime_message_list
        self.reminder_mode_list = reminder_mode_list
        self.request_id = request_id
        self.schedule_message_time = schedule_message_time
        self.schedule_message_time_zone = schedule_message_time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.realtime_message_list is not None:
            result['RealtimeMessageList'] = self.realtime_message_list
        if self.reminder_mode_list is not None:
            result['ReminderModeList'] = self.reminder_mode_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.schedule_message_time is not None:
            result['ScheduleMessageTime'] = self.schedule_message_time
        if self.schedule_message_time_zone is not None:
            result['ScheduleMessageTimeZone'] = self.schedule_message_time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('RealtimeMessageList') is not None:
            self.realtime_message_list = m.get('RealtimeMessageList')
        if m.get('ReminderModeList') is not None:
            self.reminder_mode_list = m.get('ReminderModeList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScheduleMessageTime') is not None:
            self.schedule_message_time = m.get('ScheduleMessageTime')
        if m.get('ScheduleMessageTimeZone') is not None:
            self.schedule_message_time_zone = m.get('ScheduleMessageTimeZone')
        return self


class DescribeNotificationSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNotificationSettingResponseBody = None,
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
            temp_model = DescribeNotificationSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOpenApiRcpStatsRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        end_date: str = None,
        resource_type: str = None,
        start_date: str = None,
    ):
        self.biz_type = biz_type
        self.end_date = end_date
        self.resource_type = resource_type
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class DescribeOpenApiRcpStatsResponseBodyStatList(TeaModel):
    def __init__(
        self,
        block_count: int = None,
        date: str = None,
        pass_count: int = None,
        resource_type: str = None,
        review_count: int = None,
        total_count: int = None,
        total_duration: int = None,
    ):
        self.block_count = block_count
        self.date = date
        self.pass_count = pass_count
        self.resource_type = resource_type
        self.review_count = review_count
        self.total_count = total_count
        self.total_duration = total_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_count is not None:
            result['BlockCount'] = self.block_count
        if self.date is not None:
            result['Date'] = self.date
        if self.pass_count is not None:
            result['PassCount'] = self.pass_count
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.review_count is not None:
            result['ReviewCount'] = self.review_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_duration is not None:
            result['TotalDuration'] = self.total_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockCount') is not None:
            self.block_count = m.get('BlockCount')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('PassCount') is not None:
            self.pass_count = m.get('PassCount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ReviewCount') is not None:
            self.review_count = m.get('ReviewCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalDuration') is not None:
            self.total_duration = m.get('TotalDuration')
        return self


class DescribeOpenApiRcpStatsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        stat_list: List[DescribeOpenApiRcpStatsResponseBodyStatList] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.stat_list = stat_list
        self.total_count = total_count

    def validate(self):
        if self.stat_list:
            for k in self.stat_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StatList'] = []
        if self.stat_list is not None:
            for k in self.stat_list:
                result['StatList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stat_list = []
        if m.get('StatList') is not None:
            for k in m.get('StatList'):
                temp_model = DescribeOpenApiRcpStatsResponseBodyStatList()
                self.stat_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeOpenApiRcpStatsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOpenApiRcpStatsResponseBody = None,
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
            temp_model = DescribeOpenApiRcpStatsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOpenApiUsageRequest(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        resource_type: str = None,
        source_ip: str = None,
        start_date: str = None,
    ):
        self.end_date = end_date
        self.resource_type = resource_type
        self.source_ip = source_ip
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class DescribeOpenApiUsageResponseBodyOpenApiUsageList(TeaModel):
    def __init__(
        self,
        block_count: int = None,
        block_duration: int = None,
        date: str = None,
        inner_total_count: int = None,
        outer_total_count: int = None,
        pass_count: int = None,
        pass_duration: int = None,
        resource_type: str = None,
        review_count: int = None,
        review_duration: int = None,
        scene: str = None,
        total_count: int = None,
        total_duration: int = None,
    ):
        self.block_count = block_count
        self.block_duration = block_duration
        self.date = date
        self.inner_total_count = inner_total_count
        self.outer_total_count = outer_total_count
        self.pass_count = pass_count
        self.pass_duration = pass_duration
        self.resource_type = resource_type
        self.review_count = review_count
        self.review_duration = review_duration
        self.scene = scene
        self.total_count = total_count
        self.total_duration = total_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_count is not None:
            result['BlockCount'] = self.block_count
        if self.block_duration is not None:
            result['BlockDuration'] = self.block_duration
        if self.date is not None:
            result['Date'] = self.date
        if self.inner_total_count is not None:
            result['InnerTotalCount'] = self.inner_total_count
        if self.outer_total_count is not None:
            result['OuterTotalCount'] = self.outer_total_count
        if self.pass_count is not None:
            result['PassCount'] = self.pass_count
        if self.pass_duration is not None:
            result['PassDuration'] = self.pass_duration
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.review_count is not None:
            result['ReviewCount'] = self.review_count
        if self.review_duration is not None:
            result['ReviewDuration'] = self.review_duration
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_duration is not None:
            result['TotalDuration'] = self.total_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockCount') is not None:
            self.block_count = m.get('BlockCount')
        if m.get('BlockDuration') is not None:
            self.block_duration = m.get('BlockDuration')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('InnerTotalCount') is not None:
            self.inner_total_count = m.get('InnerTotalCount')
        if m.get('OuterTotalCount') is not None:
            self.outer_total_count = m.get('OuterTotalCount')
        if m.get('PassCount') is not None:
            self.pass_count = m.get('PassCount')
        if m.get('PassDuration') is not None:
            self.pass_duration = m.get('PassDuration')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ReviewCount') is not None:
            self.review_count = m.get('ReviewCount')
        if m.get('ReviewDuration') is not None:
            self.review_duration = m.get('ReviewDuration')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalDuration') is not None:
            self.total_duration = m.get('TotalDuration')
        return self


class DescribeOpenApiUsageResponseBody(TeaModel):
    def __init__(
        self,
        open_api_usage_list: List[DescribeOpenApiUsageResponseBodyOpenApiUsageList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.open_api_usage_list = open_api_usage_list
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.open_api_usage_list:
            for k in self.open_api_usage_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OpenApiUsageList'] = []
        if self.open_api_usage_list is not None:
            for k in self.open_api_usage_list:
                result['OpenApiUsageList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.open_api_usage_list = []
        if m.get('OpenApiUsageList') is not None:
            for k in m.get('OpenApiUsageList'):
                temp_model = DescribeOpenApiUsageResponseBodyOpenApiUsageList()
                self.open_api_usage_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeOpenApiUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOpenApiUsageResponseBody = None,
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
            temp_model = DescribeOpenApiUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssCallbackSettingResponseBody(TeaModel):
    def __init__(
        self,
        audit_callback: bool = None,
        callback_seed: str = None,
        callback_url: str = None,
        request_id: str = None,
        scan_callback: bool = None,
        scan_callback_suggestions: List[str] = None,
        service_modules: List[str] = None,
    ):
        self.audit_callback = audit_callback
        self.callback_seed = callback_seed
        self.callback_url = callback_url
        self.request_id = request_id
        self.scan_callback = scan_callback
        self.scan_callback_suggestions = scan_callback_suggestions
        self.service_modules = service_modules

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_callback is not None:
            result['AuditCallback'] = self.audit_callback
        if self.callback_seed is not None:
            result['CallbackSeed'] = self.callback_seed
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scan_callback is not None:
            result['ScanCallback'] = self.scan_callback
        if self.scan_callback_suggestions is not None:
            result['ScanCallbackSuggestions'] = self.scan_callback_suggestions
        if self.service_modules is not None:
            result['ServiceModules'] = self.service_modules
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditCallback') is not None:
            self.audit_callback = m.get('AuditCallback')
        if m.get('CallbackSeed') is not None:
            self.callback_seed = m.get('CallbackSeed')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScanCallback') is not None:
            self.scan_callback = m.get('ScanCallback')
        if m.get('ScanCallbackSuggestions') is not None:
            self.scan_callback_suggestions = m.get('ScanCallbackSuggestions')
        if m.get('ServiceModules') is not None:
            self.service_modules = m.get('ServiceModules')
        return self


class DescribeOssCallbackSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOssCallbackSettingResponseBody = None,
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
            temp_model = DescribeOssCallbackSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssIncrementCheckSettingRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
    ):
        self.lang = lang
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeOssIncrementCheckSettingResponseBodyAudioAntispamFreezeConfig(TeaModel):
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


class DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigAd(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
    ):
        self.categories = categories

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigLive(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
    ):
        self.categories = categories

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigPorn(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
    ):
        self.categories = categories

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigTerrorism(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
    ):
        self.categories = categories

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfig(TeaModel):
    def __init__(
        self,
        ad: DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigAd = None,
        live: DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigLive = None,
        porn: DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigPorn = None,
        terrorism: DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigTerrorism = None,
    ):
        self.ad = ad
        self.live = live
        self.porn = porn
        self.terrorism = terrorism

    def validate(self):
        if self.ad:
            self.ad.validate()
        if self.live:
            self.live.validate()
        if self.porn:
            self.porn.validate()
        if self.terrorism:
            self.terrorism.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad is not None:
            result['Ad'] = self.ad.to_map()
        if self.live is not None:
            result['Live'] = self.live.to_map()
        if self.porn is not None:
            result['Porn'] = self.porn.to_map()
        if self.terrorism is not None:
            result['Terrorism'] = self.terrorism.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ad') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigAd()
            self.ad = temp_model.from_map(m['Ad'])
        if m.get('Live') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigLive()
            self.live = temp_model.from_map(m['Live'])
        if m.get('Porn') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigPorn()
            self.porn = temp_model.from_map(m['Porn'])
        if m.get('Terrorism') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfigTerrorism()
            self.terrorism = temp_model.from_map(m['Terrorism'])
        return self


class DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigAd(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
    ):
        self.categories = categories

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigLive(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
    ):
        self.categories = categories

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigPorn(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
    ):
        self.categories = categories

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigTerrorism(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
    ):
        self.categories = categories

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfig(TeaModel):
    def __init__(
        self,
        ad: DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigAd = None,
        live: DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigLive = None,
        porn: DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigPorn = None,
        terrorism: DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigTerrorism = None,
    ):
        self.ad = ad
        self.live = live
        self.porn = porn
        self.terrorism = terrorism

    def validate(self):
        if self.ad:
            self.ad.validate()
        if self.live:
            self.live.validate()
        if self.porn:
            self.porn.validate()
        if self.terrorism:
            self.terrorism.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad is not None:
            result['Ad'] = self.ad.to_map()
        if self.live is not None:
            result['Live'] = self.live.to_map()
        if self.porn is not None:
            result['Porn'] = self.porn.to_map()
        if self.terrorism is not None:
            result['Terrorism'] = self.terrorism.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ad') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigAd()
            self.ad = temp_model.from_map(m['Ad'])
        if m.get('Live') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigLive()
            self.live = temp_model.from_map(m['Live'])
        if m.get('Porn') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigPorn()
            self.porn = temp_model.from_map(m['Porn'])
        if m.get('Terrorism') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfigTerrorism()
            self.terrorism = temp_model.from_map(m['Terrorism'])
        return self


class DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVoiceConfigAntispam(TeaModel):
    def __init__(
        self,
        categories: List[str] = None,
    ):
        self.categories = categories

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.categories is not None:
            result['Categories'] = self.categories
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')
        return self


class DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVoiceConfig(TeaModel):
    def __init__(
        self,
        antispam: DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVoiceConfigAntispam = None,
    ):
        self.antispam = antispam

    def validate(self):
        if self.antispam:
            self.antispam.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.antispam is not None:
            result['Antispam'] = self.antispam.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Antispam') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVoiceConfigAntispam()
            self.antispam = temp_model.from_map(m['Antispam'])
        return self


class DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplate(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        description: str = None,
        image_config: DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfig = None,
        include_channel: int = None,
        name: str = None,
        video_config: DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfig = None,
        voice_config: DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVoiceConfig = None,
    ):
        self.biz_type = biz_type
        self.description = description
        self.image_config = image_config
        self.include_channel = include_channel
        self.name = name
        self.video_config = video_config
        self.voice_config = voice_config

    def validate(self):
        if self.image_config:
            self.image_config.validate()
        if self.video_config:
            self.video_config.validate()
        if self.voice_config:
            self.voice_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.description is not None:
            result['Description'] = self.description
        if self.image_config is not None:
            result['ImageConfig'] = self.image_config.to_map()
        if self.include_channel is not None:
            result['IncludeChannel'] = self.include_channel
        if self.name is not None:
            result['Name'] = self.name
        if self.video_config is not None:
            result['VideoConfig'] = self.video_config.to_map()
        if self.voice_config is not None:
            result['VoiceConfig'] = self.voice_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageConfig') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateImageConfig()
            self.image_config = temp_model.from_map(m['ImageConfig'])
        if m.get('IncludeChannel') is not None:
            self.include_channel = m.get('IncludeChannel')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VideoConfig') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVideoConfig()
            self.video_config = temp_model.from_map(m['VideoConfig'])
        if m.get('VoiceConfig') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplateVoiceConfig()
            self.voice_config = temp_model.from_map(m['VoiceConfig'])
        return self


class DescribeOssIncrementCheckSettingResponseBodyBucketConfigList(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        prefixes: List[str] = None,
        selected: bool = None,
        type: str = None,
    ):
        self.bucket = bucket
        self.prefixes = prefixes
        self.selected = selected
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.prefixes is not None:
            result['Prefixes'] = self.prefixes
        if self.selected is not None:
            result['Selected'] = self.selected
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Prefixes') is not None:
            self.prefixes = m.get('Prefixes')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeOssIncrementCheckSettingResponseBodyImageAdFreezeConfig(TeaModel):
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


class DescribeOssIncrementCheckSettingResponseBodyImageAutoFreeze(TeaModel):
    def __init__(
        self,
        ad: str = None,
        enabled: bool = None,
        live: str = None,
        porn: str = None,
        terrorism: str = None,
    ):
        self.ad = ad
        self.enabled = enabled
        self.live = live
        self.porn = porn
        self.terrorism = terrorism

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad is not None:
            result['Ad'] = self.ad
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.live is not None:
            result['Live'] = self.live
        if self.porn is not None:
            result['Porn'] = self.porn
        if self.terrorism is not None:
            result['Terrorism'] = self.terrorism
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ad') is not None:
            self.ad = m.get('Ad')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Live') is not None:
            self.live = m.get('Live')
        if m.get('Porn') is not None:
            self.porn = m.get('Porn')
        if m.get('Terrorism') is not None:
            self.terrorism = m.get('Terrorism')
        return self


class DescribeOssIncrementCheckSettingResponseBodyImageLiveFreezeConfig(TeaModel):
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


class DescribeOssIncrementCheckSettingResponseBodyImagePornFreezeConfig(TeaModel):
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


class DescribeOssIncrementCheckSettingResponseBodyImageTerrorismFreezeConfig(TeaModel):
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


class DescribeOssIncrementCheckSettingResponseBodyVideoAdFreezeConfig(TeaModel):
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


class DescribeOssIncrementCheckSettingResponseBodyVideoLiveFreezeConfig(TeaModel):
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


class DescribeOssIncrementCheckSettingResponseBodyVideoPornFreezeConfig(TeaModel):
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


class DescribeOssIncrementCheckSettingResponseBodyVideoTerrorismFreezeConfig(TeaModel):
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


class DescribeOssIncrementCheckSettingResponseBodyVideoVoiceAntispamFreezeConfig(TeaModel):
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


class DescribeOssIncrementCheckSettingResponseBody(TeaModel):
    def __init__(
        self,
        audio_antispam_freeze_config: DescribeOssIncrementCheckSettingResponseBodyAudioAntispamFreezeConfig = None,
        audio_auto_freeze_opened: bool = None,
        audio_max_size: int = None,
        audio_scan_limit: int = None,
        audio_scene_list: List[str] = None,
        auto_freeze_type: str = None,
        biz_type: str = None,
        biz_type_template: DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplate = None,
        bucket_config_list: List[DescribeOssIncrementCheckSettingResponseBodyBucketConfigList] = None,
        callback_id: str = None,
        callback_name: str = None,
        end_time: str = None,
        image_ad_freeze_config: DescribeOssIncrementCheckSettingResponseBodyImageAdFreezeConfig = None,
        image_auto_freeze: DescribeOssIncrementCheckSettingResponseBodyImageAutoFreeze = None,
        image_auto_freeze_opened: bool = None,
        image_enable_limit: bool = None,
        image_live_freeze_config: DescribeOssIncrementCheckSettingResponseBodyImageLiveFreezeConfig = None,
        image_porn_freeze_config: DescribeOssIncrementCheckSettingResponseBodyImagePornFreezeConfig = None,
        image_scan_limit: int = None,
        image_scene_list: List[str] = None,
        image_terrorism_freeze_config: DescribeOssIncrementCheckSettingResponseBodyImageTerrorismFreezeConfig = None,
        request_id: str = None,
        scan_image_no_file_type: bool = None,
        start_time: str = None,
        video_ad_freeze_config: DescribeOssIncrementCheckSettingResponseBodyVideoAdFreezeConfig = None,
        video_auto_freeze_opened: bool = None,
        video_auto_freeze_scene_list: List[str] = None,
        video_frame_interval: int = None,
        video_live_freeze_config: DescribeOssIncrementCheckSettingResponseBodyVideoLiveFreezeConfig = None,
        video_max_frames: int = None,
        video_max_size: int = None,
        video_porn_freeze_config: DescribeOssIncrementCheckSettingResponseBodyVideoPornFreezeConfig = None,
        video_scan_limit: int = None,
        video_scene_list: List[str] = None,
        video_terrorism_freeze_config: DescribeOssIncrementCheckSettingResponseBodyVideoTerrorismFreezeConfig = None,
        video_voice_antispam_freeze_config: DescribeOssIncrementCheckSettingResponseBodyVideoVoiceAntispamFreezeConfig = None,
    ):
        self.audio_antispam_freeze_config = audio_antispam_freeze_config
        self.audio_auto_freeze_opened = audio_auto_freeze_opened
        self.audio_max_size = audio_max_size
        self.audio_scan_limit = audio_scan_limit
        self.audio_scene_list = audio_scene_list
        self.auto_freeze_type = auto_freeze_type
        self.biz_type = biz_type
        self.biz_type_template = biz_type_template
        self.bucket_config_list = bucket_config_list
        self.callback_id = callback_id
        self.callback_name = callback_name
        self.end_time = end_time
        self.image_ad_freeze_config = image_ad_freeze_config
        self.image_auto_freeze = image_auto_freeze
        self.image_auto_freeze_opened = image_auto_freeze_opened
        self.image_enable_limit = image_enable_limit
        self.image_live_freeze_config = image_live_freeze_config
        self.image_porn_freeze_config = image_porn_freeze_config
        self.image_scan_limit = image_scan_limit
        self.image_scene_list = image_scene_list
        self.image_terrorism_freeze_config = image_terrorism_freeze_config
        self.request_id = request_id
        self.scan_image_no_file_type = scan_image_no_file_type
        self.start_time = start_time
        self.video_ad_freeze_config = video_ad_freeze_config
        self.video_auto_freeze_opened = video_auto_freeze_opened
        self.video_auto_freeze_scene_list = video_auto_freeze_scene_list
        self.video_frame_interval = video_frame_interval
        self.video_live_freeze_config = video_live_freeze_config
        self.video_max_frames = video_max_frames
        self.video_max_size = video_max_size
        self.video_porn_freeze_config = video_porn_freeze_config
        self.video_scan_limit = video_scan_limit
        self.video_scene_list = video_scene_list
        self.video_terrorism_freeze_config = video_terrorism_freeze_config
        self.video_voice_antispam_freeze_config = video_voice_antispam_freeze_config

    def validate(self):
        if self.audio_antispam_freeze_config:
            self.audio_antispam_freeze_config.validate()
        if self.biz_type_template:
            self.biz_type_template.validate()
        if self.bucket_config_list:
            for k in self.bucket_config_list:
                if k:
                    k.validate()
        if self.image_ad_freeze_config:
            self.image_ad_freeze_config.validate()
        if self.image_auto_freeze:
            self.image_auto_freeze.validate()
        if self.image_live_freeze_config:
            self.image_live_freeze_config.validate()
        if self.image_porn_freeze_config:
            self.image_porn_freeze_config.validate()
        if self.image_terrorism_freeze_config:
            self.image_terrorism_freeze_config.validate()
        if self.video_ad_freeze_config:
            self.video_ad_freeze_config.validate()
        if self.video_live_freeze_config:
            self.video_live_freeze_config.validate()
        if self.video_porn_freeze_config:
            self.video_porn_freeze_config.validate()
        if self.video_terrorism_freeze_config:
            self.video_terrorism_freeze_config.validate()
        if self.video_voice_antispam_freeze_config:
            self.video_voice_antispam_freeze_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_antispam_freeze_config is not None:
            result['AudioAntispamFreezeConfig'] = self.audio_antispam_freeze_config.to_map()
        if self.audio_auto_freeze_opened is not None:
            result['AudioAutoFreezeOpened'] = self.audio_auto_freeze_opened
        if self.audio_max_size is not None:
            result['AudioMaxSize'] = self.audio_max_size
        if self.audio_scan_limit is not None:
            result['AudioScanLimit'] = self.audio_scan_limit
        if self.audio_scene_list is not None:
            result['AudioSceneList'] = self.audio_scene_list
        if self.auto_freeze_type is not None:
            result['AutoFreezeType'] = self.auto_freeze_type
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.biz_type_template is not None:
            result['BizTypeTemplate'] = self.biz_type_template.to_map()
        result['BucketConfigList'] = []
        if self.bucket_config_list is not None:
            for k in self.bucket_config_list:
                result['BucketConfigList'].append(k.to_map() if k else None)
        if self.callback_id is not None:
            result['CallbackId'] = self.callback_id
        if self.callback_name is not None:
            result['CallbackName'] = self.callback_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.image_ad_freeze_config is not None:
            result['ImageAdFreezeConfig'] = self.image_ad_freeze_config.to_map()
        if self.image_auto_freeze is not None:
            result['ImageAutoFreeze'] = self.image_auto_freeze.to_map()
        if self.image_auto_freeze_opened is not None:
            result['ImageAutoFreezeOpened'] = self.image_auto_freeze_opened
        if self.image_enable_limit is not None:
            result['ImageEnableLimit'] = self.image_enable_limit
        if self.image_live_freeze_config is not None:
            result['ImageLiveFreezeConfig'] = self.image_live_freeze_config.to_map()
        if self.image_porn_freeze_config is not None:
            result['ImagePornFreezeConfig'] = self.image_porn_freeze_config.to_map()
        if self.image_scan_limit is not None:
            result['ImageScanLimit'] = self.image_scan_limit
        if self.image_scene_list is not None:
            result['ImageSceneList'] = self.image_scene_list
        if self.image_terrorism_freeze_config is not None:
            result['ImageTerrorismFreezeConfig'] = self.image_terrorism_freeze_config.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scan_image_no_file_type is not None:
            result['ScanImageNoFileType'] = self.scan_image_no_file_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.video_ad_freeze_config is not None:
            result['VideoAdFreezeConfig'] = self.video_ad_freeze_config.to_map()
        if self.video_auto_freeze_opened is not None:
            result['VideoAutoFreezeOpened'] = self.video_auto_freeze_opened
        if self.video_auto_freeze_scene_list is not None:
            result['VideoAutoFreezeSceneList'] = self.video_auto_freeze_scene_list
        if self.video_frame_interval is not None:
            result['VideoFrameInterval'] = self.video_frame_interval
        if self.video_live_freeze_config is not None:
            result['VideoLiveFreezeConfig'] = self.video_live_freeze_config.to_map()
        if self.video_max_frames is not None:
            result['VideoMaxFrames'] = self.video_max_frames
        if self.video_max_size is not None:
            result['VideoMaxSize'] = self.video_max_size
        if self.video_porn_freeze_config is not None:
            result['VideoPornFreezeConfig'] = self.video_porn_freeze_config.to_map()
        if self.video_scan_limit is not None:
            result['VideoScanLimit'] = self.video_scan_limit
        if self.video_scene_list is not None:
            result['VideoSceneList'] = self.video_scene_list
        if self.video_terrorism_freeze_config is not None:
            result['VideoTerrorismFreezeConfig'] = self.video_terrorism_freeze_config.to_map()
        if self.video_voice_antispam_freeze_config is not None:
            result['VideoVoiceAntispamFreezeConfig'] = self.video_voice_antispam_freeze_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioAntispamFreezeConfig') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyAudioAntispamFreezeConfig()
            self.audio_antispam_freeze_config = temp_model.from_map(m['AudioAntispamFreezeConfig'])
        if m.get('AudioAutoFreezeOpened') is not None:
            self.audio_auto_freeze_opened = m.get('AudioAutoFreezeOpened')
        if m.get('AudioMaxSize') is not None:
            self.audio_max_size = m.get('AudioMaxSize')
        if m.get('AudioScanLimit') is not None:
            self.audio_scan_limit = m.get('AudioScanLimit')
        if m.get('AudioSceneList') is not None:
            self.audio_scene_list = m.get('AudioSceneList')
        if m.get('AutoFreezeType') is not None:
            self.auto_freeze_type = m.get('AutoFreezeType')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BizTypeTemplate') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyBizTypeTemplate()
            self.biz_type_template = temp_model.from_map(m['BizTypeTemplate'])
        self.bucket_config_list = []
        if m.get('BucketConfigList') is not None:
            for k in m.get('BucketConfigList'):
                temp_model = DescribeOssIncrementCheckSettingResponseBodyBucketConfigList()
                self.bucket_config_list.append(temp_model.from_map(k))
        if m.get('CallbackId') is not None:
            self.callback_id = m.get('CallbackId')
        if m.get('CallbackName') is not None:
            self.callback_name = m.get('CallbackName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ImageAdFreezeConfig') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyImageAdFreezeConfig()
            self.image_ad_freeze_config = temp_model.from_map(m['ImageAdFreezeConfig'])
        if m.get('ImageAutoFreeze') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyImageAutoFreeze()
            self.image_auto_freeze = temp_model.from_map(m['ImageAutoFreeze'])
        if m.get('ImageAutoFreezeOpened') is not None:
            self.image_auto_freeze_opened = m.get('ImageAutoFreezeOpened')
        if m.get('ImageEnableLimit') is not None:
            self.image_enable_limit = m.get('ImageEnableLimit')
        if m.get('ImageLiveFreezeConfig') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyImageLiveFreezeConfig()
            self.image_live_freeze_config = temp_model.from_map(m['ImageLiveFreezeConfig'])
        if m.get('ImagePornFreezeConfig') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyImagePornFreezeConfig()
            self.image_porn_freeze_config = temp_model.from_map(m['ImagePornFreezeConfig'])
        if m.get('ImageScanLimit') is not None:
            self.image_scan_limit = m.get('ImageScanLimit')
        if m.get('ImageSceneList') is not None:
            self.image_scene_list = m.get('ImageSceneList')
        if m.get('ImageTerrorismFreezeConfig') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyImageTerrorismFreezeConfig()
            self.image_terrorism_freeze_config = temp_model.from_map(m['ImageTerrorismFreezeConfig'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScanImageNoFileType') is not None:
            self.scan_image_no_file_type = m.get('ScanImageNoFileType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('VideoAdFreezeConfig') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyVideoAdFreezeConfig()
            self.video_ad_freeze_config = temp_model.from_map(m['VideoAdFreezeConfig'])
        if m.get('VideoAutoFreezeOpened') is not None:
            self.video_auto_freeze_opened = m.get('VideoAutoFreezeOpened')
        if m.get('VideoAutoFreezeSceneList') is not None:
            self.video_auto_freeze_scene_list = m.get('VideoAutoFreezeSceneList')
        if m.get('VideoFrameInterval') is not None:
            self.video_frame_interval = m.get('VideoFrameInterval')
        if m.get('VideoLiveFreezeConfig') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyVideoLiveFreezeConfig()
            self.video_live_freeze_config = temp_model.from_map(m['VideoLiveFreezeConfig'])
        if m.get('VideoMaxFrames') is not None:
            self.video_max_frames = m.get('VideoMaxFrames')
        if m.get('VideoMaxSize') is not None:
            self.video_max_size = m.get('VideoMaxSize')
        if m.get('VideoPornFreezeConfig') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyVideoPornFreezeConfig()
            self.video_porn_freeze_config = temp_model.from_map(m['VideoPornFreezeConfig'])
        if m.get('VideoScanLimit') is not None:
            self.video_scan_limit = m.get('VideoScanLimit')
        if m.get('VideoSceneList') is not None:
            self.video_scene_list = m.get('VideoSceneList')
        if m.get('VideoTerrorismFreezeConfig') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyVideoTerrorismFreezeConfig()
            self.video_terrorism_freeze_config = temp_model.from_map(m['VideoTerrorismFreezeConfig'])
        if m.get('VideoVoiceAntispamFreezeConfig') is not None:
            temp_model = DescribeOssIncrementCheckSettingResponseBodyVideoVoiceAntispamFreezeConfig()
            self.video_voice_antispam_freeze_config = temp_model.from_map(m['VideoVoiceAntispamFreezeConfig'])
        return self


class DescribeOssIncrementCheckSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOssIncrementCheckSettingResponseBody = None,
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
            temp_model = DescribeOssIncrementCheckSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssIncrementOverviewRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
    ):
        self.lang = lang
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeOssIncrementOverviewResponseBody(TeaModel):
    def __init__(
        self,
        ad_unhandle_count: int = None,
        audio_count: int = None,
        image_count: int = None,
        live_unhandle_count: int = None,
        porn_unhandle_count: int = None,
        request_id: str = None,
        terrorism_unhandle_count: int = None,
        video_count: int = None,
        video_frame_count: int = None,
        voice_antispam_unhandle_count: int = None,
    ):
        self.ad_unhandle_count = ad_unhandle_count
        self.audio_count = audio_count
        self.image_count = image_count
        self.live_unhandle_count = live_unhandle_count
        self.porn_unhandle_count = porn_unhandle_count
        self.request_id = request_id
        self.terrorism_unhandle_count = terrorism_unhandle_count
        self.video_count = video_count
        self.video_frame_count = video_frame_count
        self.voice_antispam_unhandle_count = voice_antispam_unhandle_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad_unhandle_count is not None:
            result['AdUnhandleCount'] = self.ad_unhandle_count
        if self.audio_count is not None:
            result['AudioCount'] = self.audio_count
        if self.image_count is not None:
            result['ImageCount'] = self.image_count
        if self.live_unhandle_count is not None:
            result['LiveUnhandleCount'] = self.live_unhandle_count
        if self.porn_unhandle_count is not None:
            result['PornUnhandleCount'] = self.porn_unhandle_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.terrorism_unhandle_count is not None:
            result['TerrorismUnhandleCount'] = self.terrorism_unhandle_count
        if self.video_count is not None:
            result['VideoCount'] = self.video_count
        if self.video_frame_count is not None:
            result['VideoFrameCount'] = self.video_frame_count
        if self.voice_antispam_unhandle_count is not None:
            result['VoiceAntispamUnhandleCount'] = self.voice_antispam_unhandle_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdUnhandleCount') is not None:
            self.ad_unhandle_count = m.get('AdUnhandleCount')
        if m.get('AudioCount') is not None:
            self.audio_count = m.get('AudioCount')
        if m.get('ImageCount') is not None:
            self.image_count = m.get('ImageCount')
        if m.get('LiveUnhandleCount') is not None:
            self.live_unhandle_count = m.get('LiveUnhandleCount')
        if m.get('PornUnhandleCount') is not None:
            self.porn_unhandle_count = m.get('PornUnhandleCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TerrorismUnhandleCount') is not None:
            self.terrorism_unhandle_count = m.get('TerrorismUnhandleCount')
        if m.get('VideoCount') is not None:
            self.video_count = m.get('VideoCount')
        if m.get('VideoFrameCount') is not None:
            self.video_frame_count = m.get('VideoFrameCount')
        if m.get('VoiceAntispamUnhandleCount') is not None:
            self.voice_antispam_unhandle_count = m.get('VoiceAntispamUnhandleCount')
        return self


class DescribeOssIncrementOverviewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOssIncrementOverviewResponseBody = None,
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
            temp_model = DescribeOssIncrementOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssIncrementStatsRequest(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        lang: str = None,
        resource_type: str = None,
        scene: str = None,
        source_ip: str = None,
        start_date: str = None,
    ):
        self.end_date = end_date
        self.lang = lang
        self.resource_type = resource_type
        self.scene = scene
        self.source_ip = source_ip
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class DescribeOssIncrementStatsResponseBodyStatList(TeaModel):
    def __init__(
        self,
        block_count: int = None,
        date: str = None,
        pass_count: int = None,
        resource_type: str = None,
        review_count: int = None,
        scene: str = None,
        total_count: int = None,
    ):
        self.block_count = block_count
        self.date = date
        self.pass_count = pass_count
        self.resource_type = resource_type
        self.review_count = review_count
        self.scene = scene
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.block_count is not None:
            result['BlockCount'] = self.block_count
        if self.date is not None:
            result['Date'] = self.date
        if self.pass_count is not None:
            result['PassCount'] = self.pass_count
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.review_count is not None:
            result['ReviewCount'] = self.review_count
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockCount') is not None:
            self.block_count = m.get('BlockCount')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('PassCount') is not None:
            self.pass_count = m.get('PassCount')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ReviewCount') is not None:
            self.review_count = m.get('ReviewCount')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeOssIncrementStatsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        stat_list: List[DescribeOssIncrementStatsResponseBodyStatList] = None,
        total_count: int = None,
    ):
        self.request_id = request_id
        self.stat_list = stat_list
        self.total_count = total_count

    def validate(self):
        if self.stat_list:
            for k in self.stat_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['StatList'] = []
        if self.stat_list is not None:
            for k in self.stat_list:
                result['StatList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.stat_list = []
        if m.get('StatList') is not None:
            for k in m.get('StatList'):
                temp_model = DescribeOssIncrementStatsResponseBodyStatList()
                self.stat_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeOssIncrementStatsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOssIncrementStatsResponseBody = None,
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
            temp_model = DescribeOssIncrementStatsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssResultItemsRequest(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        current_page: int = None,
        end_date: str = None,
        lang: str = None,
        max_score: float = None,
        min_score: float = None,
        object: str = None,
        page_size: int = None,
        query_id: str = None,
        resource_type: str = None,
        scene: str = None,
        source_ip: str = None,
        start_date: str = None,
        stock: bool = None,
        stock_task_id: int = None,
        suggestion: str = None,
        total_count: int = None,
    ):
        self.bucket = bucket
        self.current_page = current_page
        self.end_date = end_date
        self.lang = lang
        self.max_score = max_score
        self.min_score = min_score
        self.object = object
        self.page_size = page_size
        self.query_id = query_id
        self.resource_type = resource_type
        self.scene = scene
        self.source_ip = source_ip
        self.start_date = start_date
        self.stock = stock
        self.stock_task_id = stock_task_id
        self.suggestion = suggestion
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_score is not None:
            result['MaxScore'] = self.max_score
        if self.min_score is not None:
            result['MinScore'] = self.min_score
        if self.object is not None:
            result['Object'] = self.object
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.stock is not None:
            result['Stock'] = self.stock
        if self.stock_task_id is not None:
            result['StockTaskId'] = self.stock_task_id
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxScore') is not None:
            self.max_score = m.get('MaxScore')
        if m.get('MinScore') is not None:
            self.min_score = m.get('MinScore')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Stock') is not None:
            self.stock = m.get('Stock')
        if m.get('StockTaskId') is not None:
            self.stock_task_id = m.get('StockTaskId')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeOssResultItemsResponseBodyScanResultListFrameResults(TeaModel):
    def __init__(
        self,
        offset: int = None,
        thumbnail: str = None,
        url: str = None,
    ):
        self.offset = offset
        self.thumbnail = thumbnail
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.thumbnail is not None:
            result['Thumbnail'] = self.thumbnail
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('Thumbnail') is not None:
            self.thumbnail = m.get('Thumbnail')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeOssResultItemsResponseBodyScanResultListVoiceSegmentAntispamResults(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        label: str = None,
        start_time: int = None,
        text: str = None,
    ):
        self.end_time = end_time
        self.label = label
        self.start_time = start_time
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.label is not None:
            result['Label'] = self.label
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class DescribeOssResultItemsResponseBodyScanResultList(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        content: str = None,
        create_time: str = None,
        data_id: str = None,
        frame_results: List[DescribeOssResultItemsResponseBodyScanResultListFrameResults] = None,
        handle_status: int = None,
        id: int = None,
        new_url: str = None,
        object: str = None,
        request_time: str = None,
        resource_status: int = None,
        scan_finished_time: str = None,
        score: str = None,
        suggestion: str = None,
        task_id: str = None,
        thumbnail: str = None,
        voice_segment_antispam_results: List[DescribeOssResultItemsResponseBodyScanResultListVoiceSegmentAntispamResults] = None,
    ):
        self.bucket = bucket
        self.content = content
        self.create_time = create_time
        self.data_id = data_id
        self.frame_results = frame_results
        self.handle_status = handle_status
        self.id = id
        self.new_url = new_url
        self.object = object
        self.request_time = request_time
        self.resource_status = resource_status
        self.scan_finished_time = scan_finished_time
        self.score = score
        self.suggestion = suggestion
        self.task_id = task_id
        self.thumbnail = thumbnail
        self.voice_segment_antispam_results = voice_segment_antispam_results

    def validate(self):
        if self.frame_results:
            for k in self.frame_results:
                if k:
                    k.validate()
        if self.voice_segment_antispam_results:
            for k in self.voice_segment_antispam_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data_id is not None:
            result['DataId'] = self.data_id
        result['FrameResults'] = []
        if self.frame_results is not None:
            for k in self.frame_results:
                result['FrameResults'].append(k.to_map() if k else None)
        if self.handle_status is not None:
            result['HandleStatus'] = self.handle_status
        if self.id is not None:
            result['Id'] = self.id
        if self.new_url is not None:
            result['NewUrl'] = self.new_url
        if self.object is not None:
            result['Object'] = self.object
        if self.request_time is not None:
            result['RequestTime'] = self.request_time
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        if self.scan_finished_time is not None:
            result['ScanFinishedTime'] = self.scan_finished_time
        if self.score is not None:
            result['Score'] = self.score
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.thumbnail is not None:
            result['Thumbnail'] = self.thumbnail
        result['VoiceSegmentAntispamResults'] = []
        if self.voice_segment_antispam_results is not None:
            for k in self.voice_segment_antispam_results:
                result['VoiceSegmentAntispamResults'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        self.frame_results = []
        if m.get('FrameResults') is not None:
            for k in m.get('FrameResults'):
                temp_model = DescribeOssResultItemsResponseBodyScanResultListFrameResults()
                self.frame_results.append(temp_model.from_map(k))
        if m.get('HandleStatus') is not None:
            self.handle_status = m.get('HandleStatus')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NewUrl') is not None:
            self.new_url = m.get('NewUrl')
        if m.get('Object') is not None:
            self.object = m.get('Object')
        if m.get('RequestTime') is not None:
            self.request_time = m.get('RequestTime')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        if m.get('ScanFinishedTime') is not None:
            self.scan_finished_time = m.get('ScanFinishedTime')
        if m.get('Score') is not None:
            self.score = m.get('Score')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Thumbnail') is not None:
            self.thumbnail = m.get('Thumbnail')
        self.voice_segment_antispam_results = []
        if m.get('VoiceSegmentAntispamResults') is not None:
            for k in m.get('VoiceSegmentAntispamResults'):
                temp_model = DescribeOssResultItemsResponseBodyScanResultListVoiceSegmentAntispamResults()
                self.voice_segment_antispam_results.append(temp_model.from_map(k))
        return self


class DescribeOssResultItemsResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        query_id: str = None,
        request_id: str = None,
        scan_result_list: List[DescribeOssResultItemsResponseBodyScanResultList] = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.query_id = query_id
        self.request_id = request_id
        self.scan_result_list = scan_result_list
        self.total_count = total_count

    def validate(self):
        if self.scan_result_list:
            for k in self.scan_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ScanResultList'] = []
        if self.scan_result_list is not None:
            for k in self.scan_result_list:
                result['ScanResultList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.scan_result_list = []
        if m.get('ScanResultList') is not None:
            for k in m.get('ScanResultList'):
                temp_model = DescribeOssResultItemsResponseBodyScanResultList()
                self.scan_result_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeOssResultItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOssResultItemsResponseBody = None,
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
            temp_model = DescribeOssResultItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeOssStockStatusRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
        stock_task_id: int = None,
    ):
        self.lang = lang
        self.source_ip = source_ip
        self.stock_task_id = stock_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.stock_task_id is not None:
            result['StockTaskId'] = self.stock_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StockTaskId') is not None:
            self.stock_task_id = m.get('StockTaskId')
        return self


class DescribeOssStockStatusResponseBodyBucketList(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        prefixes: List[str] = None,
        selected: bool = None,
    ):
        self.bucket = bucket
        self.prefixes = prefixes
        self.selected = selected

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.prefixes is not None:
            result['Prefixes'] = self.prefixes
        if self.selected is not None:
            result['Selected'] = self.selected
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Prefixes') is not None:
            self.prefixes = m.get('Prefixes')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        return self


class DescribeOssStockStatusResponseBody(TeaModel):
    def __init__(
        self,
        audio_antispam_count: int = None,
        audio_total_count: int = None,
        bucket_list: List[DescribeOssStockStatusResponseBodyBucketList] = None,
        finished_time: str = None,
        image_ad_count: int = None,
        image_live_count: int = None,
        image_porn_count: int = None,
        image_terrorism_count: int = None,
        image_total_count: int = None,
        request_id: str = None,
        resouce_type_list: List[str] = None,
        scene_list: List[str] = None,
        stock_status: int = None,
        video_ad_count: int = None,
        video_live_count: int = None,
        video_porn_count: int = None,
        video_terrorism_count: int = None,
        video_total_count: int = None,
        video_voice_antispam_count: int = None,
    ):
        self.audio_antispam_count = audio_antispam_count
        self.audio_total_count = audio_total_count
        self.bucket_list = bucket_list
        self.finished_time = finished_time
        self.image_ad_count = image_ad_count
        self.image_live_count = image_live_count
        self.image_porn_count = image_porn_count
        self.image_terrorism_count = image_terrorism_count
        self.image_total_count = image_total_count
        self.request_id = request_id
        self.resouce_type_list = resouce_type_list
        self.scene_list = scene_list
        self.stock_status = stock_status
        self.video_ad_count = video_ad_count
        self.video_live_count = video_live_count
        self.video_porn_count = video_porn_count
        self.video_terrorism_count = video_terrorism_count
        self.video_total_count = video_total_count
        self.video_voice_antispam_count = video_voice_antispam_count

    def validate(self):
        if self.bucket_list:
            for k in self.bucket_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_antispam_count is not None:
            result['AudioAntispamCount'] = self.audio_antispam_count
        if self.audio_total_count is not None:
            result['AudioTotalCount'] = self.audio_total_count
        result['BucketList'] = []
        if self.bucket_list is not None:
            for k in self.bucket_list:
                result['BucketList'].append(k.to_map() if k else None)
        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time
        if self.image_ad_count is not None:
            result['ImageAdCount'] = self.image_ad_count
        if self.image_live_count is not None:
            result['ImageLiveCount'] = self.image_live_count
        if self.image_porn_count is not None:
            result['ImagePornCount'] = self.image_porn_count
        if self.image_terrorism_count is not None:
            result['ImageTerrorismCount'] = self.image_terrorism_count
        if self.image_total_count is not None:
            result['ImageTotalCount'] = self.image_total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resouce_type_list is not None:
            result['ResouceTypeList'] = self.resouce_type_list
        if self.scene_list is not None:
            result['SceneList'] = self.scene_list
        if self.stock_status is not None:
            result['StockStatus'] = self.stock_status
        if self.video_ad_count is not None:
            result['VideoAdCount'] = self.video_ad_count
        if self.video_live_count is not None:
            result['VideoLiveCount'] = self.video_live_count
        if self.video_porn_count is not None:
            result['VideoPornCount'] = self.video_porn_count
        if self.video_terrorism_count is not None:
            result['VideoTerrorismCount'] = self.video_terrorism_count
        if self.video_total_count is not None:
            result['VideoTotalCount'] = self.video_total_count
        if self.video_voice_antispam_count is not None:
            result['VideoVoiceAntispamCount'] = self.video_voice_antispam_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioAntispamCount') is not None:
            self.audio_antispam_count = m.get('AudioAntispamCount')
        if m.get('AudioTotalCount') is not None:
            self.audio_total_count = m.get('AudioTotalCount')
        self.bucket_list = []
        if m.get('BucketList') is not None:
            for k in m.get('BucketList'):
                temp_model = DescribeOssStockStatusResponseBodyBucketList()
                self.bucket_list.append(temp_model.from_map(k))
        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')
        if m.get('ImageAdCount') is not None:
            self.image_ad_count = m.get('ImageAdCount')
        if m.get('ImageLiveCount') is not None:
            self.image_live_count = m.get('ImageLiveCount')
        if m.get('ImagePornCount') is not None:
            self.image_porn_count = m.get('ImagePornCount')
        if m.get('ImageTerrorismCount') is not None:
            self.image_terrorism_count = m.get('ImageTerrorismCount')
        if m.get('ImageTotalCount') is not None:
            self.image_total_count = m.get('ImageTotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResouceTypeList') is not None:
            self.resouce_type_list = m.get('ResouceTypeList')
        if m.get('SceneList') is not None:
            self.scene_list = m.get('SceneList')
        if m.get('StockStatus') is not None:
            self.stock_status = m.get('StockStatus')
        if m.get('VideoAdCount') is not None:
            self.video_ad_count = m.get('VideoAdCount')
        if m.get('VideoLiveCount') is not None:
            self.video_live_count = m.get('VideoLiveCount')
        if m.get('VideoPornCount') is not None:
            self.video_porn_count = m.get('VideoPornCount')
        if m.get('VideoTerrorismCount') is not None:
            self.video_terrorism_count = m.get('VideoTerrorismCount')
        if m.get('VideoTotalCount') is not None:
            self.video_total_count = m.get('VideoTotalCount')
        if m.get('VideoVoiceAntispamCount') is not None:
            self.video_voice_antispam_count = m.get('VideoVoiceAntispamCount')
        return self


class DescribeOssStockStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeOssStockStatusResponseBody = None,
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
            temp_model = DescribeOssStockStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSdkUrlRequest(TeaModel):
    def __init__(
        self,
        debug: bool = None,
        id: int = None,
        lang: str = None,
        source_ip: str = None,
    ):
        self.debug = debug
        self.id = id
        self.lang = lang
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debug is not None:
            result['Debug'] = self.debug
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Debug') is not None:
            self.debug = m.get('Debug')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeSdkUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sdk_url: str = None,
    ):
        self.request_id = request_id
        self.sdk_url = sdk_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sdk_url is not None:
            result['SdkUrl'] = self.sdk_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SdkUrl') is not None:
            self.sdk_url = m.get('SdkUrl')
        return self


class DescribeSdkUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSdkUrlResponseBody = None,
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
            temp_model = DescribeSdkUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUpdatePackageResultRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
        task_id: str = None,
    ):
        self.lang = lang
        self.source_ip = source_ip
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeUpdatePackageResultResponseBodyAppInfoDebugPackageInfo(TeaModel):
    def __init__(
        self,
        version: str = None,
    ):
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeUpdatePackageResultResponseBodyAppInfoPackageInfo(TeaModel):
    def __init__(
        self,
        version: str = None,
    ):
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeUpdatePackageResultResponseBodyAppInfo(TeaModel):
    def __init__(
        self,
        debug_package_info: DescribeUpdatePackageResultResponseBodyAppInfoDebugPackageInfo = None,
        end_date: str = None,
        icon: str = None,
        id: int = None,
        name: str = None,
        package_info: DescribeUpdatePackageResultResponseBodyAppInfoPackageInfo = None,
        package_name: str = None,
        start_date: str = None,
        type: int = None,
    ):
        self.debug_package_info = debug_package_info
        self.end_date = end_date
        self.icon = icon
        self.id = id
        self.name = name
        self.package_info = package_info
        self.package_name = package_name
        self.start_date = start_date
        self.type = type

    def validate(self):
        if self.debug_package_info:
            self.debug_package_info.validate()
        if self.package_info:
            self.package_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debug_package_info is not None:
            result['DebugPackageInfo'] = self.debug_package_info.to_map()
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.icon is not None:
            result['Icon'] = self.icon
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.package_info is not None:
            result['PackageInfo'] = self.package_info.to_map()
        if self.package_name is not None:
            result['PackageName'] = self.package_name
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DebugPackageInfo') is not None:
            temp_model = DescribeUpdatePackageResultResponseBodyAppInfoDebugPackageInfo()
            self.debug_package_info = temp_model.from_map(m['DebugPackageInfo'])
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Icon') is not None:
            self.icon = m.get('Icon')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PackageInfo') is not None:
            temp_model = DescribeUpdatePackageResultResponseBodyAppInfoPackageInfo()
            self.package_info = temp_model.from_map(m['PackageInfo'])
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeUpdatePackageResultResponseBody(TeaModel):
    def __init__(
        self,
        app_info: DescribeUpdatePackageResultResponseBodyAppInfo = None,
        request_id: str = None,
    ):
        self.app_info = app_info
        self.request_id = request_id

    def validate(self):
        if self.app_info:
            self.app_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_info is not None:
            result['AppInfo'] = self.app_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInfo') is not None:
            temp_model = DescribeUpdatePackageResultResponseBodyAppInfo()
            self.app_info = temp_model.from_map(m['AppInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUpdatePackageResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUpdatePackageResultResponseBody = None,
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
            temp_model = DescribeUpdatePackageResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUploadInfoRequest(TeaModel):
    def __init__(
        self,
        biz: str = None,
        lang: str = None,
        source_ip: str = None,
    ):
        self.biz = biz
        self.lang = lang
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz is not None:
            result['Biz'] = self.biz
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Biz') is not None:
            self.biz = m.get('Biz')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeUploadInfoResponseBody(TeaModel):
    def __init__(
        self,
        accessid: str = None,
        expire: int = None,
        folder: str = None,
        host: str = None,
        policy: str = None,
        request_id: str = None,
        signature: str = None,
    ):
        self.accessid = accessid
        self.expire = expire
        self.folder = folder
        self.host = host
        self.policy = policy
        self.request_id = request_id
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accessid is not None:
            result['Accessid'] = self.accessid
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.folder is not None:
            result['Folder'] = self.folder
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessid') is not None:
            self.accessid = m.get('Accessid')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Folder') is not None:
            self.folder = m.get('Folder')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class DescribeUploadInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUploadInfoResponseBody = None,
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
            temp_model = DescribeUploadInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUsageBillRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        day: str = None,
        page_size: int = None,
        total_count: int = None,
        type: str = None,
    ):
        self.current_page = current_page
        self.day = day
        self.page_size = page_size
        self.total_count = total_count
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.day is not None:
            result['Day'] = self.day
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeUsageBillResponseBodyBillList(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        confirm_count: int = None,
        day: str = None,
        free_count: int = None,
        region: str = None,
        review_count: int = None,
        scene: str = None,
        sub_uid: str = None,
        total_count: int = None,
    ):
        self.biz_type = biz_type
        self.confirm_count = confirm_count
        self.day = day
        self.free_count = free_count
        self.region = region
        self.review_count = review_count
        self.scene = scene
        self.sub_uid = sub_uid
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.confirm_count is not None:
            result['ConfirmCount'] = self.confirm_count
        if self.day is not None:
            result['Day'] = self.day
        if self.free_count is not None:
            result['FreeCount'] = self.free_count
        if self.region is not None:
            result['Region'] = self.region
        if self.review_count is not None:
            result['ReviewCount'] = self.review_count
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.sub_uid is not None:
            result['SubUid'] = self.sub_uid
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ConfirmCount') is not None:
            self.confirm_count = m.get('ConfirmCount')
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('FreeCount') is not None:
            self.free_count = m.get('FreeCount')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ReviewCount') is not None:
            self.review_count = m.get('ReviewCount')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SubUid') is not None:
            self.sub_uid = m.get('SubUid')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeUsageBillResponseBody(TeaModel):
    def __init__(
        self,
        bill_list: List[DescribeUsageBillResponseBodyBillList] = None,
        current_page: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.bill_list = bill_list
        self.current_page = current_page
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.bill_list:
            for k in self.bill_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BillList'] = []
        if self.bill_list is not None:
            for k in self.bill_list:
                result['BillList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bill_list = []
        if m.get('BillList') is not None:
            for k in m.get('BillList'):
                temp_model = DescribeUsageBillResponseBodyBillList()
                self.bill_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeUsageBillResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUsageBillResponseBody = None,
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
            temp_model = DescribeUsageBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserBizTypesRequest(TeaModel):
    def __init__(
        self,
        customized: bool = None,
    ):
        self.customized = customized

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customized is not None:
            result['Customized'] = self.customized
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Customized') is not None:
            self.customized = m.get('Customized')
        return self


class DescribeUserBizTypesResponseBodyBizTypeList(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        cite_template: bool = None,
        description: str = None,
        gray: bool = None,
        industry_info: str = None,
        source: str = None,
        source_biz_type: str = None,
    ):
        self.biz_type = biz_type
        self.cite_template = cite_template
        self.description = description
        self.gray = gray
        self.industry_info = industry_info
        self.source = source
        self.source_biz_type = source_biz_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.cite_template is not None:
            result['CiteTemplate'] = self.cite_template
        if self.description is not None:
            result['Description'] = self.description
        if self.gray is not None:
            result['Gray'] = self.gray
        if self.industry_info is not None:
            result['IndustryInfo'] = self.industry_info
        if self.source is not None:
            result['Source'] = self.source
        if self.source_biz_type is not None:
            result['SourceBizType'] = self.source_biz_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CiteTemplate') is not None:
            self.cite_template = m.get('CiteTemplate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Gray') is not None:
            self.gray = m.get('Gray')
        if m.get('IndustryInfo') is not None:
            self.industry_info = m.get('IndustryInfo')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceBizType') is not None:
            self.source_biz_type = m.get('SourceBizType')
        return self


class DescribeUserBizTypesResponseBodyBizTypeListImport(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        cite_template: bool = None,
        description: str = None,
        gray: bool = None,
        industry_info: str = None,
        source: str = None,
        source_biz_type: str = None,
    ):
        self.biz_type = biz_type
        self.cite_template = cite_template
        self.description = description
        self.gray = gray
        self.industry_info = industry_info
        self.source = source
        self.source_biz_type = source_biz_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.cite_template is not None:
            result['CiteTemplate'] = self.cite_template
        if self.description is not None:
            result['Description'] = self.description
        if self.gray is not None:
            result['Gray'] = self.gray
        if self.industry_info is not None:
            result['IndustryInfo'] = self.industry_info
        if self.source is not None:
            result['Source'] = self.source
        if self.source_biz_type is not None:
            result['SourceBizType'] = self.source_biz_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CiteTemplate') is not None:
            self.cite_template = m.get('CiteTemplate')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Gray') is not None:
            self.gray = m.get('Gray')
        if m.get('IndustryInfo') is not None:
            self.industry_info = m.get('IndustryInfo')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceBizType') is not None:
            self.source_biz_type = m.get('SourceBizType')
        return self


class DescribeUserBizTypesResponseBody(TeaModel):
    def __init__(
        self,
        biz_type_list: List[DescribeUserBizTypesResponseBodyBizTypeList] = None,
        biz_type_list_import: List[DescribeUserBizTypesResponseBodyBizTypeListImport] = None,
        request_id: str = None,
    ):
        self.biz_type_list = biz_type_list
        self.biz_type_list_import = biz_type_list_import
        self.request_id = request_id

    def validate(self):
        if self.biz_type_list:
            for k in self.biz_type_list:
                if k:
                    k.validate()
        if self.biz_type_list_import:
            for k in self.biz_type_list_import:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BizTypeList'] = []
        if self.biz_type_list is not None:
            for k in self.biz_type_list:
                result['BizTypeList'].append(k.to_map() if k else None)
        result['BizTypeListImport'] = []
        if self.biz_type_list_import is not None:
            for k in self.biz_type_list_import:
                result['BizTypeListImport'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.biz_type_list = []
        if m.get('BizTypeList') is not None:
            for k in m.get('BizTypeList'):
                temp_model = DescribeUserBizTypesResponseBodyBizTypeList()
                self.biz_type_list.append(temp_model.from_map(k))
        self.biz_type_list_import = []
        if m.get('BizTypeListImport') is not None:
            for k in m.get('BizTypeListImport'):
                temp_model = DescribeUserBizTypesResponseBodyBizTypeListImport()
                self.biz_type_list_import.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeUserBizTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUserBizTypesResponseBody = None,
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
            temp_model = DescribeUserBizTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUserStatusRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
    ):
        self.lang = lang
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeUserStatusResponseBody(TeaModel):
    def __init__(
        self,
        agree_channel: int = None,
        buyed: bool = None,
        in_dept: bool = None,
        open_api_begin_time: str = None,
        open_api_used: bool = None,
        oss_check_status: str = None,
        oss_video_size_limit: int = None,
        request_id: str = None,
        uid: str = None,
    ):
        self.agree_channel = agree_channel
        self.buyed = buyed
        self.in_dept = in_dept
        self.open_api_begin_time = open_api_begin_time
        self.open_api_used = open_api_used
        self.oss_check_status = oss_check_status
        self.oss_video_size_limit = oss_video_size_limit
        self.request_id = request_id
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agree_channel is not None:
            result['AgreeChannel'] = self.agree_channel
        if self.buyed is not None:
            result['Buyed'] = self.buyed
        if self.in_dept is not None:
            result['InDept'] = self.in_dept
        if self.open_api_begin_time is not None:
            result['OpenApiBeginTime'] = self.open_api_begin_time
        if self.open_api_used is not None:
            result['OpenApiUsed'] = self.open_api_used
        if self.oss_check_status is not None:
            result['OssCheckStatus'] = self.oss_check_status
        if self.oss_video_size_limit is not None:
            result['OssVideoSizeLimit'] = self.oss_video_size_limit
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgreeChannel') is not None:
            self.agree_channel = m.get('AgreeChannel')
        if m.get('Buyed') is not None:
            self.buyed = m.get('Buyed')
        if m.get('InDept') is not None:
            self.in_dept = m.get('InDept')
        if m.get('OpenApiBeginTime') is not None:
            self.open_api_begin_time = m.get('OpenApiBeginTime')
        if m.get('OpenApiUsed') is not None:
            self.open_api_used = m.get('OpenApiUsed')
        if m.get('OssCheckStatus') is not None:
            self.oss_check_status = m.get('OssCheckStatus')
        if m.get('OssVideoSizeLimit') is not None:
            self.oss_video_size_limit = m.get('OssVideoSizeLimit')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class DescribeUserStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUserStatusResponseBody = None,
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
            temp_model = DescribeUserStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeViewContentRequest(TeaModel):
    def __init__(
        self,
        audit_result: str = None,
        biz_type: str = None,
        current_page: int = None,
        data_id: str = None,
        end_date: str = None,
        image_id: str = None,
        keyword: str = None,
        keyword_id: str = None,
        label: str = None,
        lib_type: str = None,
        page_size: int = None,
        resource_type: str = None,
        scene: str = None,
        start_date: str = None,
        suggestion: str = None,
        task_id: str = None,
        total_count: int = None,
    ):
        self.audit_result = audit_result
        self.biz_type = biz_type
        self.current_page = current_page
        self.data_id = data_id
        self.end_date = end_date
        self.image_id = image_id
        self.keyword = keyword
        self.keyword_id = keyword_id
        self.label = label
        self.lib_type = lib_type
        self.page_size = page_size
        self.resource_type = resource_type
        self.scene = scene
        self.start_date = start_date
        self.suggestion = suggestion
        self.task_id = task_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_result is not None:
            result['AuditResult'] = self.audit_result
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.keyword_id is not None:
            result['KeywordId'] = self.keyword_id
        if self.label is not None:
            result['Label'] = self.label
        if self.lib_type is not None:
            result['LibType'] = self.lib_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditResult') is not None:
            self.audit_result = m.get('AuditResult')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('KeywordId') is not None:
            self.keyword_id = m.get('KeywordId')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('LibType') is not None:
            self.lib_type = m.get('LibType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeViewContentResponseBodyViewContentListFaceResultsAge(TeaModel):
    def __init__(
        self,
        rate: float = None,
        value: int = None,
    ):
        self.rate = rate
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeViewContentResponseBodyViewContentListFaceResultsBang(TeaModel):
    def __init__(
        self,
        rate: float = None,
        value: str = None,
    ):
        self.rate = rate
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeViewContentResponseBodyViewContentListFaceResultsGender(TeaModel):
    def __init__(
        self,
        rate: float = None,
        value: str = None,
    ):
        self.rate = rate
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeViewContentResponseBodyViewContentListFaceResultsGlasses(TeaModel):
    def __init__(
        self,
        rate: float = None,
        value: str = None,
    ):
        self.rate = rate
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeViewContentResponseBodyViewContentListFaceResultsHairstyle(TeaModel):
    def __init__(
        self,
        rate: float = None,
        value: str = None,
    ):
        self.rate = rate
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeViewContentResponseBodyViewContentListFaceResultsHat(TeaModel):
    def __init__(
        self,
        rate: float = None,
        value: str = None,
    ):
        self.rate = rate
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeViewContentResponseBodyViewContentListFaceResultsImage(TeaModel):
    def __init__(
        self,
        height: int = None,
        width: int = None,
    ):
        self.height = height
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class DescribeViewContentResponseBodyViewContentListFaceResultsLocation(TeaModel):
    def __init__(
        self,
        h: int = None,
        w: int = None,
        x: int = None,
        y: int = None,
    ):
        self.h = h
        self.w = w
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.h is not None:
            result['H'] = self.h
        if self.w is not None:
            result['W'] = self.w
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('H') is not None:
            self.h = m.get('H')
        if m.get('W') is not None:
            self.w = m.get('W')
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class DescribeViewContentResponseBodyViewContentListFaceResultsMustache(TeaModel):
    def __init__(
        self,
        rate: float = None,
        value: str = None,
    ):
        self.rate = rate
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeViewContentResponseBodyViewContentListFaceResultsQuality(TeaModel):
    def __init__(
        self,
        blur: float = None,
        pitch: float = None,
        roll: float = None,
        yaw: float = None,
    ):
        self.blur = blur
        self.pitch = pitch
        self.roll = roll
        self.yaw = yaw

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blur is not None:
            result['Blur'] = self.blur
        if self.pitch is not None:
            result['Pitch'] = self.pitch
        if self.roll is not None:
            result['Roll'] = self.roll
        if self.yaw is not None:
            result['Yaw'] = self.yaw
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Blur') is not None:
            self.blur = m.get('Blur')
        if m.get('Pitch') is not None:
            self.pitch = m.get('Pitch')
        if m.get('Roll') is not None:
            self.roll = m.get('Roll')
        if m.get('Yaw') is not None:
            self.yaw = m.get('Yaw')
        return self


class DescribeViewContentResponseBodyViewContentListFaceResultsRespirator(TeaModel):
    def __init__(
        self,
        rate: float = None,
        value: str = None,
    ):
        self.rate = rate
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeViewContentResponseBodyViewContentListFaceResultsSmile(TeaModel):
    def __init__(
        self,
        rate: float = None,
        value: float = None,
    ):
        self.rate = rate
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rate is not None:
            result['Rate'] = self.rate
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Rate') is not None:
            self.rate = m.get('Rate')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeViewContentResponseBodyViewContentListFaceResults(TeaModel):
    def __init__(
        self,
        age: DescribeViewContentResponseBodyViewContentListFaceResultsAge = None,
        bang: DescribeViewContentResponseBodyViewContentListFaceResultsBang = None,
        bualified: bool = None,
        gender: DescribeViewContentResponseBodyViewContentListFaceResultsGender = None,
        glasses: DescribeViewContentResponseBodyViewContentListFaceResultsGlasses = None,
        hairstyle: DescribeViewContentResponseBodyViewContentListFaceResultsHairstyle = None,
        hat: DescribeViewContentResponseBodyViewContentListFaceResultsHat = None,
        image: DescribeViewContentResponseBodyViewContentListFaceResultsImage = None,
        location: DescribeViewContentResponseBodyViewContentListFaceResultsLocation = None,
        mustache: DescribeViewContentResponseBodyViewContentListFaceResultsMustache = None,
        quality: DescribeViewContentResponseBodyViewContentListFaceResultsQuality = None,
        respirator: DescribeViewContentResponseBodyViewContentListFaceResultsRespirator = None,
        smile: DescribeViewContentResponseBodyViewContentListFaceResultsSmile = None,
    ):
        self.age = age
        self.bang = bang
        self.bualified = bualified
        self.gender = gender
        self.glasses = glasses
        self.hairstyle = hairstyle
        self.hat = hat
        self.image = image
        self.location = location
        self.mustache = mustache
        self.quality = quality
        self.respirator = respirator
        self.smile = smile

    def validate(self):
        if self.age:
            self.age.validate()
        if self.bang:
            self.bang.validate()
        if self.gender:
            self.gender.validate()
        if self.glasses:
            self.glasses.validate()
        if self.hairstyle:
            self.hairstyle.validate()
        if self.hat:
            self.hat.validate()
        if self.image:
            self.image.validate()
        if self.location:
            self.location.validate()
        if self.mustache:
            self.mustache.validate()
        if self.quality:
            self.quality.validate()
        if self.respirator:
            self.respirator.validate()
        if self.smile:
            self.smile.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.age is not None:
            result['Age'] = self.age.to_map()
        if self.bang is not None:
            result['Bang'] = self.bang.to_map()
        if self.bualified is not None:
            result['Bualified'] = self.bualified
        if self.gender is not None:
            result['Gender'] = self.gender.to_map()
        if self.glasses is not None:
            result['Glasses'] = self.glasses.to_map()
        if self.hairstyle is not None:
            result['Hairstyle'] = self.hairstyle.to_map()
        if self.hat is not None:
            result['Hat'] = self.hat.to_map()
        if self.image is not None:
            result['Image'] = self.image.to_map()
        if self.location is not None:
            result['Location'] = self.location.to_map()
        if self.mustache is not None:
            result['Mustache'] = self.mustache.to_map()
        if self.quality is not None:
            result['Quality'] = self.quality.to_map()
        if self.respirator is not None:
            result['Respirator'] = self.respirator.to_map()
        if self.smile is not None:
            result['Smile'] = self.smile.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Age') is not None:
            temp_model = DescribeViewContentResponseBodyViewContentListFaceResultsAge()
            self.age = temp_model.from_map(m['Age'])
        if m.get('Bang') is not None:
            temp_model = DescribeViewContentResponseBodyViewContentListFaceResultsBang()
            self.bang = temp_model.from_map(m['Bang'])
        if m.get('Bualified') is not None:
            self.bualified = m.get('Bualified')
        if m.get('Gender') is not None:
            temp_model = DescribeViewContentResponseBodyViewContentListFaceResultsGender()
            self.gender = temp_model.from_map(m['Gender'])
        if m.get('Glasses') is not None:
            temp_model = DescribeViewContentResponseBodyViewContentListFaceResultsGlasses()
            self.glasses = temp_model.from_map(m['Glasses'])
        if m.get('Hairstyle') is not None:
            temp_model = DescribeViewContentResponseBodyViewContentListFaceResultsHairstyle()
            self.hairstyle = temp_model.from_map(m['Hairstyle'])
        if m.get('Hat') is not None:
            temp_model = DescribeViewContentResponseBodyViewContentListFaceResultsHat()
            self.hat = temp_model.from_map(m['Hat'])
        if m.get('Image') is not None:
            temp_model = DescribeViewContentResponseBodyViewContentListFaceResultsImage()
            self.image = temp_model.from_map(m['Image'])
        if m.get('Location') is not None:
            temp_model = DescribeViewContentResponseBodyViewContentListFaceResultsLocation()
            self.location = temp_model.from_map(m['Location'])
        if m.get('Mustache') is not None:
            temp_model = DescribeViewContentResponseBodyViewContentListFaceResultsMustache()
            self.mustache = temp_model.from_map(m['Mustache'])
        if m.get('Quality') is not None:
            temp_model = DescribeViewContentResponseBodyViewContentListFaceResultsQuality()
            self.quality = temp_model.from_map(m['Quality'])
        if m.get('Respirator') is not None:
            temp_model = DescribeViewContentResponseBodyViewContentListFaceResultsRespirator()
            self.respirator = temp_model.from_map(m['Respirator'])
        if m.get('Smile') is not None:
            temp_model = DescribeViewContentResponseBodyViewContentListFaceResultsSmile()
            self.smile = temp_model.from_map(m['Smile'])
        return self


class DescribeViewContentResponseBodyViewContentListFrameResults(TeaModel):
    def __init__(
        self,
        label: str = None,
        offset: int = None,
        url: str = None,
    ):
        self.label = label
        self.offset = offset
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeViewContentResponseBodyViewContentListResults(TeaModel):
    def __init__(
        self,
        label: str = None,
        scene: str = None,
        suggestion: str = None,
    ):
        self.label = label
        self.scene = scene
        self.suggestion = suggestion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        return self


class DescribeViewContentResponseBodyViewContentList(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        content: str = None,
        data_id: str = None,
        face_results: List[DescribeViewContentResponseBodyViewContentListFaceResults] = None,
        frame_results: List[DescribeViewContentResponseBodyViewContentListFrameResults] = None,
        id: int = None,
        new_url: str = None,
        request_time: str = None,
        results: List[DescribeViewContentResponseBodyViewContentListResults] = None,
        scan_finished_time: str = None,
        scan_result: str = None,
        suggestion: str = None,
        task_id: str = None,
        thumbnail: str = None,
        url: str = None,
    ):
        self.biz_type = biz_type
        self.content = content
        self.data_id = data_id
        self.face_results = face_results
        self.frame_results = frame_results
        self.id = id
        self.new_url = new_url
        self.request_time = request_time
        self.results = results
        self.scan_finished_time = scan_finished_time
        self.scan_result = scan_result
        self.suggestion = suggestion
        self.task_id = task_id
        self.thumbnail = thumbnail
        self.url = url

    def validate(self):
        if self.face_results:
            for k in self.face_results:
                if k:
                    k.validate()
        if self.frame_results:
            for k in self.frame_results:
                if k:
                    k.validate()
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.content is not None:
            result['Content'] = self.content
        if self.data_id is not None:
            result['DataId'] = self.data_id
        result['FaceResults'] = []
        if self.face_results is not None:
            for k in self.face_results:
                result['FaceResults'].append(k.to_map() if k else None)
        result['FrameResults'] = []
        if self.frame_results is not None:
            for k in self.frame_results:
                result['FrameResults'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        if self.new_url is not None:
            result['NewUrl'] = self.new_url
        if self.request_time is not None:
            result['RequestTime'] = self.request_time
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        if self.scan_finished_time is not None:
            result['ScanFinishedTime'] = self.scan_finished_time
        if self.scan_result is not None:
            result['ScanResult'] = self.scan_result
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.thumbnail is not None:
            result['Thumbnail'] = self.thumbnail
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        self.face_results = []
        if m.get('FaceResults') is not None:
            for k in m.get('FaceResults'):
                temp_model = DescribeViewContentResponseBodyViewContentListFaceResults()
                self.face_results.append(temp_model.from_map(k))
        self.frame_results = []
        if m.get('FrameResults') is not None:
            for k in m.get('FrameResults'):
                temp_model = DescribeViewContentResponseBodyViewContentListFrameResults()
                self.frame_results.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('NewUrl') is not None:
            self.new_url = m.get('NewUrl')
        if m.get('RequestTime') is not None:
            self.request_time = m.get('RequestTime')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = DescribeViewContentResponseBodyViewContentListResults()
                self.results.append(temp_model.from_map(k))
        if m.get('ScanFinishedTime') is not None:
            self.scan_finished_time = m.get('ScanFinishedTime')
        if m.get('ScanResult') is not None:
            self.scan_result = m.get('ScanResult')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Thumbnail') is not None:
            self.thumbnail = m.get('Thumbnail')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeViewContentResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        view_content_list: List[DescribeViewContentResponseBodyViewContentList] = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.view_content_list = view_content_list

    def validate(self):
        if self.view_content_list:
            for k in self.view_content_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['ViewContentList'] = []
        if self.view_content_list is not None:
            for k in self.view_content_list:
                result['ViewContentList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.view_content_list = []
        if m.get('ViewContentList') is not None:
            for k in m.get('ViewContentList'):
                temp_model = DescribeViewContentResponseBodyViewContentList()
                self.view_content_list.append(temp_model.from_map(k))
        return self


class DescribeViewContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeViewContentResponseBody = None,
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
            temp_model = DescribeViewContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebsiteIndexPageBaselineRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        lang: str = None,
        source_ip: str = None,
    ):
        self.instance_id = instance_id
        self.lang = lang
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeWebsiteIndexPageBaselineResponseBody(TeaModel):
    def __init__(
        self,
        base_line_status: str = None,
        create_time: str = None,
        request_id: str = None,
        snapshot: str = None,
    ):
        self.base_line_status = base_line_status
        self.create_time = create_time
        self.request_id = request_id
        self.snapshot = snapshot

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_line_status is not None:
            result['BaseLineStatus'] = self.base_line_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.snapshot is not None:
            result['Snapshot'] = self.snapshot
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseLineStatus') is not None:
            self.base_line_status = m.get('BaseLineStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Snapshot') is not None:
            self.snapshot = m.get('Snapshot')
        return self


class DescribeWebsiteIndexPageBaselineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeWebsiteIndexPageBaselineResponseBody = None,
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
            temp_model = DescribeWebsiteIndexPageBaselineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebsiteInstanceRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        instance_id: str = None,
        lang: str = None,
        page_size: int = None,
        source_ip: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.instance_id = instance_id
        self.lang = lang
        self.page_size = page_size
        self.source_ip = source_ip
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeWebsiteInstanceResponseBodyWebsiteInstanceList(TeaModel):
    def __init__(
        self,
        buy_time: str = None,
        domain: str = None,
        expired_time: str = None,
        index_page: str = None,
        index_page_scan_interval: int = None,
        instance_id: str = None,
        protocol: str = None,
        status: str = None,
        website_scan_interval: int = None,
    ):
        self.buy_time = buy_time
        self.domain = domain
        self.expired_time = expired_time
        self.index_page = index_page
        self.index_page_scan_interval = index_page_scan_interval
        self.instance_id = instance_id
        self.protocol = protocol
        self.status = status
        self.website_scan_interval = website_scan_interval

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buy_time is not None:
            result['BuyTime'] = self.buy_time
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.index_page is not None:
            result['IndexPage'] = self.index_page
        if self.index_page_scan_interval is not None:
            result['IndexPageScanInterval'] = self.index_page_scan_interval
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.status is not None:
            result['Status'] = self.status
        if self.website_scan_interval is not None:
            result['WebsiteScanInterval'] = self.website_scan_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyTime') is not None:
            self.buy_time = m.get('BuyTime')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('IndexPage') is not None:
            self.index_page = m.get('IndexPage')
        if m.get('IndexPageScanInterval') is not None:
            self.index_page_scan_interval = m.get('IndexPageScanInterval')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WebsiteScanInterval') is not None:
            self.website_scan_interval = m.get('WebsiteScanInterval')
        return self


class DescribeWebsiteInstanceResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        website_instance_list: List[DescribeWebsiteInstanceResponseBodyWebsiteInstanceList] = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.website_instance_list = website_instance_list

    def validate(self):
        if self.website_instance_list:
            for k in self.website_instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['WebsiteInstanceList'] = []
        if self.website_instance_list is not None:
            for k in self.website_instance_list:
                result['WebsiteInstanceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.website_instance_list = []
        if m.get('WebsiteInstanceList') is not None:
            for k in m.get('WebsiteInstanceList'):
                temp_model = DescribeWebsiteInstanceResponseBodyWebsiteInstanceList()
                self.website_instance_list.append(temp_model.from_map(k))
        return self


class DescribeWebsiteInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeWebsiteInstanceResponseBody = None,
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
            temp_model = DescribeWebsiteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebsiteInstanceIdRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
    ):
        self.lang = lang
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeWebsiteInstanceIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        website_instance_id_list: List[str] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.website_instance_id_list = website_instance_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.website_instance_id_list is not None:
            result['WebsiteInstanceIdList'] = self.website_instance_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('WebsiteInstanceIdList') is not None:
            self.website_instance_id_list = m.get('WebsiteInstanceIdList')
        return self


class DescribeWebsiteInstanceIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeWebsiteInstanceIdResponseBody = None,
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
            temp_model = DescribeWebsiteInstanceIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebsiteInstanceKeyUrlRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        lang: str = None,
        source_ip: str = None,
    ):
        self.instance_id = instance_id
        self.lang = lang
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeWebsiteInstanceKeyUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        website_instance_key_url_list: List[str] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.website_instance_key_url_list = website_instance_key_url_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.website_instance_key_url_list is not None:
            result['WebsiteInstanceKeyUrlList'] = self.website_instance_key_url_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('WebsiteInstanceKeyUrlList') is not None:
            self.website_instance_key_url_list = m.get('WebsiteInstanceKeyUrlList')
        return self


class DescribeWebsiteInstanceKeyUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeWebsiteInstanceKeyUrlResponseBody = None,
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
            temp_model = DescribeWebsiteInstanceKeyUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebsiteScanResultRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        domain: str = None,
        handle_status: str = None,
        label: str = None,
        lang: str = None,
        page_size: int = None,
        site_url: str = None,
        source_ip: str = None,
        sub_service_module: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.domain = domain
        self.handle_status = handle_status
        self.label = label
        self.lang = lang
        self.page_size = page_size
        self.site_url = site_url
        self.source_ip = source_ip
        self.sub_service_module = sub_service_module
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.handle_status is not None:
            result['HandleStatus'] = self.handle_status
        if self.label is not None:
            result['Label'] = self.label
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.site_url is not None:
            result['SiteUrl'] = self.site_url
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.sub_service_module is not None:
            result['SubServiceModule'] = self.sub_service_module
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('HandleStatus') is not None:
            self.handle_status = m.get('HandleStatus')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SiteUrl') is not None:
            self.site_url = m.get('SiteUrl')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('SubServiceModule') is not None:
            self.sub_service_module = m.get('SubServiceModule')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeWebsiteScanResultResponseBodyWebsiteScanResultList(TeaModel):
    def __init__(
        self,
        domain: str = None,
        handle_status: int = None,
        id: int = None,
        image_risk_count: int = None,
        instance_id: str = None,
        labels: List[str] = None,
        scan_time: str = None,
        source_risk_count: int = None,
        task_id: str = None,
        text_risk_count: int = None,
        url: str = None,
    ):
        self.domain = domain
        self.handle_status = handle_status
        self.id = id
        self.image_risk_count = image_risk_count
        self.instance_id = instance_id
        self.labels = labels
        self.scan_time = scan_time
        self.source_risk_count = source_risk_count
        self.task_id = task_id
        self.text_risk_count = text_risk_count
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.handle_status is not None:
            result['HandleStatus'] = self.handle_status
        if self.id is not None:
            result['Id'] = self.id
        if self.image_risk_count is not None:
            result['ImageRiskCount'] = self.image_risk_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.scan_time is not None:
            result['ScanTime'] = self.scan_time
        if self.source_risk_count is not None:
            result['SourceRiskCount'] = self.source_risk_count
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.text_risk_count is not None:
            result['TextRiskCount'] = self.text_risk_count
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('HandleStatus') is not None:
            self.handle_status = m.get('HandleStatus')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ImageRiskCount') is not None:
            self.image_risk_count = m.get('ImageRiskCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('ScanTime') is not None:
            self.scan_time = m.get('ScanTime')
        if m.get('SourceRiskCount') is not None:
            self.source_risk_count = m.get('SourceRiskCount')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TextRiskCount') is not None:
            self.text_risk_count = m.get('TextRiskCount')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeWebsiteScanResultResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        website_scan_result_list: List[DescribeWebsiteScanResultResponseBodyWebsiteScanResultList] = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.website_scan_result_list = website_scan_result_list

    def validate(self):
        if self.website_scan_result_list:
            for k in self.website_scan_result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['WebsiteScanResultList'] = []
        if self.website_scan_result_list is not None:
            for k in self.website_scan_result_list:
                result['WebsiteScanResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.website_scan_result_list = []
        if m.get('WebsiteScanResultList') is not None:
            for k in m.get('WebsiteScanResultList'):
                temp_model = DescribeWebsiteScanResultResponseBodyWebsiteScanResultList()
                self.website_scan_result_list.append(temp_model.from_map(k))
        return self


class DescribeWebsiteScanResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeWebsiteScanResultResponseBody = None,
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
            temp_model = DescribeWebsiteScanResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebsiteScanResultDetailRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        lang: str = None,
        resource_type: str = None,
        source_ip: str = None,
    ):
        self.id = id
        self.lang = lang
        self.resource_type = resource_type
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeWebsiteScanResultDetailResponseBodyImageScanResults(TeaModel):
    def __init__(
        self,
        labels: List[str] = None,
        url: str = None,
    ):
        self.labels = labels
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeWebsiteScanResultDetailResponseBody(TeaModel):
    def __init__(
        self,
        baseline: str = None,
        content: str = None,
        hit_keywords: List[str] = None,
        image_scan_results: List[DescribeWebsiteScanResultDetailResponseBodyImageScanResults] = None,
        request_id: str = None,
        resource_type: str = None,
        tampered_source: str = None,
    ):
        self.baseline = baseline
        self.content = content
        self.hit_keywords = hit_keywords
        self.image_scan_results = image_scan_results
        self.request_id = request_id
        self.resource_type = resource_type
        self.tampered_source = tampered_source

    def validate(self):
        if self.image_scan_results:
            for k in self.image_scan_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baseline is not None:
            result['Baseline'] = self.baseline
        if self.content is not None:
            result['Content'] = self.content
        if self.hit_keywords is not None:
            result['HitKeywords'] = self.hit_keywords
        result['ImageScanResults'] = []
        if self.image_scan_results is not None:
            for k in self.image_scan_results:
                result['ImageScanResults'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tampered_source is not None:
            result['TamperedSource'] = self.tampered_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Baseline') is not None:
            self.baseline = m.get('Baseline')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('HitKeywords') is not None:
            self.hit_keywords = m.get('HitKeywords')
        self.image_scan_results = []
        if m.get('ImageScanResults') is not None:
            for k in m.get('ImageScanResults'):
                temp_model = DescribeWebsiteScanResultDetailResponseBodyImageScanResults()
                self.image_scan_results.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TamperedSource') is not None:
            self.tampered_source = m.get('TamperedSource')
        return self


class DescribeWebsiteScanResultDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeWebsiteScanResultDetailResponseBody = None,
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
            temp_model = DescribeWebsiteScanResultDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebsiteStatRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
    ):
        self.lang = lang
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeWebsiteStatResponseBodyWebsiteStatList(TeaModel):
    def __init__(
        self,
        instance_count: int = None,
        risk_count: int = None,
        scan_count: int = None,
        sub_service_module: str = None,
    ):
        self.instance_count = instance_count
        self.risk_count = risk_count
        self.scan_count = scan_count
        self.sub_service_module = sub_service_module

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count
        if self.scan_count is not None:
            result['ScanCount'] = self.scan_count
        if self.sub_service_module is not None:
            result['SubServiceModule'] = self.sub_service_module
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')
        if m.get('ScanCount') is not None:
            self.scan_count = m.get('ScanCount')
        if m.get('SubServiceModule') is not None:
            self.sub_service_module = m.get('SubServiceModule')
        return self


class DescribeWebsiteStatResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        website_stat_list: List[DescribeWebsiteStatResponseBodyWebsiteStatList] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.website_stat_list = website_stat_list

    def validate(self):
        if self.website_stat_list:
            for k in self.website_stat_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['WebsiteStatList'] = []
        if self.website_stat_list is not None:
            for k in self.website_stat_list:
                result['WebsiteStatList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.website_stat_list = []
        if m.get('WebsiteStatList') is not None:
            for k in m.get('WebsiteStatList'):
                temp_model = DescribeWebsiteStatResponseBodyWebsiteStatList()
                self.website_stat_list.append(temp_model.from_map(k))
        return self


class DescribeWebsiteStatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeWebsiteStatResponseBody = None,
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
            temp_model = DescribeWebsiteStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebsiteVerifyInfoRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        lang: str = None,
        source_ip: str = None,
    ):
        self.instance_id = instance_id
        self.lang = lang
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class DescribeWebsiteVerifyInfoResponseBody(TeaModel):
    def __init__(
        self,
        cname: str = None,
        domain: str = None,
        host_file: str = None,
        index_page: str = None,
        protocol: str = None,
        request_id: str = None,
        verify_method: str = None,
    ):
        self.cname = cname
        self.domain = domain
        self.host_file = host_file
        self.index_page = index_page
        self.protocol = protocol
        self.request_id = request_id
        self.verify_method = verify_method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.host_file is not None:
            result['HostFile'] = self.host_file
        if self.index_page is not None:
            result['IndexPage'] = self.index_page
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.verify_method is not None:
            result['VerifyMethod'] = self.verify_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('HostFile') is not None:
            self.host_file = m.get('HostFile')
        if m.get('IndexPage') is not None:
            self.index_page = m.get('IndexPage')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VerifyMethod') is not None:
            self.verify_method = m.get('VerifyMethod')
        return self


class DescribeWebsiteVerifyInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeWebsiteVerifyInfoResponseBody = None,
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
            temp_model = DescribeWebsiteVerifyInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportKeywordsRequest(TeaModel):
    def __init__(
        self,
        keyword_lib_id: int = None,
    ):
        self.keyword_lib_id = keyword_lib_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword_lib_id is not None:
            result['KeywordLibId'] = self.keyword_lib_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeywordLibId') is not None:
            self.keyword_lib_id = m.get('KeywordLibId')
        return self


class ExportKeywordsResponseBody(TeaModel):
    def __init__(
        self,
        download_url: str = None,
        request_id: str = None,
    ):
        self.download_url = download_url
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportKeywordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportKeywordsResponseBody = None,
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
            temp_model = ExportKeywordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportOpenApiRcpStatsRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        end_date: str = None,
        resource_type: str = None,
        start_date: str = None,
    ):
        self.biz_type = biz_type
        self.end_date = end_date
        self.resource_type = resource_type
        self.start_date = start_date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class ExportOpenApiRcpStatsResponseBody(TeaModel):
    def __init__(
        self,
        download_url: str = None,
        request_id: str = None,
    ):
        self.download_url = download_url
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportOpenApiRcpStatsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportOpenApiRcpStatsResponseBody = None,
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
            temp_model = ExportOpenApiRcpStatsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportOssResultRequest(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        current_page: int = None,
        end_date: str = None,
        lang: str = None,
        max_score: float = None,
        min_score: float = None,
        page_size: int = None,
        resource_type: str = None,
        scene: str = None,
        source_ip: str = None,
        start_date: str = None,
        stock: bool = None,
        stock_task_id: int = None,
        suggestion: str = None,
        total_count: int = None,
    ):
        self.bucket = bucket
        self.current_page = current_page
        self.end_date = end_date
        self.lang = lang
        self.max_score = max_score
        self.min_score = min_score
        self.page_size = page_size
        self.resource_type = resource_type
        self.scene = scene
        self.source_ip = source_ip
        self.start_date = start_date
        self.stock = stock
        self.stock_task_id = stock_task_id
        self.suggestion = suggestion
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.max_score is not None:
            result['MaxScore'] = self.max_score
        if self.min_score is not None:
            result['MinScore'] = self.min_score
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.stock is not None:
            result['Stock'] = self.stock
        if self.stock_task_id is not None:
            result['StockTaskId'] = self.stock_task_id
        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MaxScore') is not None:
            self.max_score = m.get('MaxScore')
        if m.get('MinScore') is not None:
            self.min_score = m.get('MinScore')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('Stock') is not None:
            self.stock = m.get('Stock')
        if m.get('StockTaskId') is not None:
            self.stock_task_id = m.get('StockTaskId')
        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ExportOssResultResponseBody(TeaModel):
    def __init__(
        self,
        file_url: str = None,
        request_id: str = None,
    ):
        self.file_url = file_url
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportOssResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportOssResultResponseBody = None,
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
            temp_model = ExportOssResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuditItemDetailRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        type: str = None,
    ):
        self.task_id = task_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetAuditItemDetailResponseBody(TeaModel):
    def __init__(
        self,
        api_result: str = None,
        api_risk_type: str = None,
        api_ts: str = None,
        new_url: str = None,
        request_id: str = None,
    ):
        self.api_result = api_result
        self.api_risk_type = api_risk_type
        self.api_ts = api_ts
        self.new_url = new_url
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_result is not None:
            result['ApiResult'] = self.api_result
        if self.api_risk_type is not None:
            result['ApiRiskType'] = self.api_risk_type
        if self.api_ts is not None:
            result['ApiTs'] = self.api_ts
        if self.new_url is not None:
            result['NewUrl'] = self.new_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiResult') is not None:
            self.api_result = m.get('ApiResult')
        if m.get('ApiRiskType') is not None:
            self.api_risk_type = m.get('ApiRiskType')
        if m.get('ApiTs') is not None:
            self.api_ts = m.get('ApiTs')
        if m.get('NewUrl') is not None:
            self.new_url = m.get('NewUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAuditItemDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAuditItemDetailResponseBody = None,
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
            temp_model = GetAuditItemDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuditItemListRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        current_page: int = None,
        custom_result: str = None,
        custom_risk_type: str = None,
        data_id: str = None,
        end_date: str = None,
        page_size: int = None,
        rcp_result: str = None,
        rcp_risk_type: str = None,
        start_date: str = None,
        task_id: str = None,
        type: str = None,
    ):
        self.biz_type = biz_type
        self.current_page = current_page
        self.custom_result = custom_result
        self.custom_risk_type = custom_risk_type
        self.data_id = data_id
        self.end_date = end_date
        self.page_size = page_size
        self.rcp_result = rcp_result
        self.rcp_risk_type = rcp_risk_type
        self.start_date = start_date
        self.task_id = task_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.custom_result is not None:
            result['CustomResult'] = self.custom_result
        if self.custom_risk_type is not None:
            result['CustomRiskType'] = self.custom_risk_type
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.rcp_result is not None:
            result['RcpResult'] = self.rcp_result
        if self.rcp_risk_type is not None:
            result['RcpRiskType'] = self.rcp_risk_type
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('CustomResult') is not None:
            self.custom_result = m.get('CustomResult')
        if m.get('CustomRiskType') is not None:
            self.custom_risk_type = m.get('CustomRiskType')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RcpResult') is not None:
            self.rcp_result = m.get('RcpResult')
        if m.get('RcpRiskType') is not None:
            self.rcp_risk_type = m.get('RcpRiskType')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetAuditItemListResponseBodyItems(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        content: str = None,
        create: str = None,
        custom_result: str = None,
        custom_risk_type: str = None,
        custom_ts: str = None,
        data_id: str = None,
        id: int = None,
        operator: str = None,
        rcp_result: str = None,
        rcp_risk_type: str = None,
        rcp_ts: str = None,
        sub_uid: str = None,
        task_id: str = None,
        thumbnail: str = None,
        type: str = None,
        uid: str = None,
        url: str = None,
    ):
        self.biz_type = biz_type
        self.content = content
        self.create = create
        self.custom_result = custom_result
        self.custom_risk_type = custom_risk_type
        self.custom_ts = custom_ts
        self.data_id = data_id
        self.id = id
        self.operator = operator
        self.rcp_result = rcp_result
        self.rcp_risk_type = rcp_risk_type
        self.rcp_ts = rcp_ts
        self.sub_uid = sub_uid
        self.task_id = task_id
        self.thumbnail = thumbnail
        self.type = type
        self.uid = uid
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.content is not None:
            result['Content'] = self.content
        if self.create is not None:
            result['Create'] = self.create
        if self.custom_result is not None:
            result['CustomResult'] = self.custom_result
        if self.custom_risk_type is not None:
            result['CustomRiskType'] = self.custom_risk_type
        if self.custom_ts is not None:
            result['CustomTs'] = self.custom_ts
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.id is not None:
            result['Id'] = self.id
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.rcp_result is not None:
            result['RcpResult'] = self.rcp_result
        if self.rcp_risk_type is not None:
            result['RcpRiskType'] = self.rcp_risk_type
        if self.rcp_ts is not None:
            result['RcpTs'] = self.rcp_ts
        if self.sub_uid is not None:
            result['SubUid'] = self.sub_uid
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.thumbnail is not None:
            result['Thumbnail'] = self.thumbnail
        if self.type is not None:
            result['Type'] = self.type
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Create') is not None:
            self.create = m.get('Create')
        if m.get('CustomResult') is not None:
            self.custom_result = m.get('CustomResult')
        if m.get('CustomRiskType') is not None:
            self.custom_risk_type = m.get('CustomRiskType')
        if m.get('CustomTs') is not None:
            self.custom_ts = m.get('CustomTs')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('RcpResult') is not None:
            self.rcp_result = m.get('RcpResult')
        if m.get('RcpRiskType') is not None:
            self.rcp_risk_type = m.get('RcpRiskType')
        if m.get('RcpTs') is not None:
            self.rcp_ts = m.get('RcpTs')
        if m.get('SubUid') is not None:
            self.sub_uid = m.get('SubUid')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Thumbnail') is not None:
            self.thumbnail = m.get('Thumbnail')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetAuditItemListResponseBody(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[GetAuditItemListResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.items = items
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = GetAuditItemListResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetAuditItemListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAuditItemListResponseBody = None,
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
            temp_model = GetAuditItemListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuditUserConfResponseBody(TeaModel):
    def __init__(
        self,
        custom_audit: bool = None,
        rcp_labels: Dict[str, List[str]] = None,
        request_id: str = None,
        user_labels: Dict[str, List[str]] = None,
    ):
        self.custom_audit = custom_audit
        self.rcp_labels = rcp_labels
        self.request_id = request_id
        self.user_labels = user_labels

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_audit is not None:
            result['CustomAudit'] = self.custom_audit
        if self.rcp_labels is not None:
            result['RcpLabels'] = self.rcp_labels
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_labels is not None:
            result['UserLabels'] = self.user_labels
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomAudit') is not None:
            self.custom_audit = m.get('CustomAudit')
        if m.get('RcpLabels') is not None:
            self.rcp_labels = m.get('RcpLabels')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserLabels') is not None:
            self.user_labels = m.get('UserLabels')
        return self


class GetAuditUserConfResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAuditUserConfResponseBody = None,
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
            temp_model = GetAuditUserConfResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportKeywordsRequest(TeaModel):
    def __init__(
        self,
        keyword_lib_id: int = None,
        keywords_object: str = None,
    ):
        self.keyword_lib_id = keyword_lib_id
        self.keywords_object = keywords_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword_lib_id is not None:
            result['KeywordLibId'] = self.keyword_lib_id
        if self.keywords_object is not None:
            result['KeywordsObject'] = self.keywords_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeywordLibId') is not None:
            self.keyword_lib_id = m.get('KeywordLibId')
        if m.get('KeywordsObject') is not None:
            self.keywords_object = m.get('KeywordsObject')
        return self


class ImportKeywordsResponseBody(TeaModel):
    def __init__(
        self,
        invalid_keyword_list: List[str] = None,
        request_id: str = None,
        success_count: int = None,
        valid_keyword_list: List[str] = None,
    ):
        self.invalid_keyword_list = invalid_keyword_list
        self.request_id = request_id
        self.success_count = success_count
        self.valid_keyword_list = valid_keyword_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invalid_keyword_list is not None:
            result['InvalidKeywordList'] = self.invalid_keyword_list
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        if self.valid_keyword_list is not None:
            result['validKeywordList'] = self.valid_keyword_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvalidKeywordList') is not None:
            self.invalid_keyword_list = m.get('InvalidKeywordList')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        if m.get('validKeywordList') is not None:
            self.valid_keyword_list = m.get('validKeywordList')
        return self


class ImportKeywordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImportKeywordsResponseBody = None,
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
            temp_model = ImportKeywordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MarkAuditContentRequest(TeaModel):
    def __init__(
        self,
        audit_illegal_reasons: str = None,
        audit_result: str = None,
        biz_types: str = None,
        ids: str = None,
        source_ip: str = None,
    ):
        self.audit_illegal_reasons = audit_illegal_reasons
        self.audit_result = audit_result
        self.biz_types = biz_types
        self.ids = ids
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_illegal_reasons is not None:
            result['AuditIllegalReasons'] = self.audit_illegal_reasons
        if self.audit_result is not None:
            result['AuditResult'] = self.audit_result
        if self.biz_types is not None:
            result['BizTypes'] = self.biz_types
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditIllegalReasons') is not None:
            self.audit_illegal_reasons = m.get('AuditIllegalReasons')
        if m.get('AuditResult') is not None:
            self.audit_result = m.get('AuditResult')
        if m.get('BizTypes') is not None:
            self.biz_types = m.get('BizTypes')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class MarkAuditContentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MarkAuditContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MarkAuditContentResponseBody = None,
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
            temp_model = MarkAuditContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MarkAuditContentItemRequest(TeaModel):
    def __init__(
        self,
        audit_illegal_reasons: str = None,
        audit_result: str = None,
        biz_types: str = None,
        ids: str = None,
        lang: str = None,
        source_ip: str = None,
    ):
        self.audit_illegal_reasons = audit_illegal_reasons
        self.audit_result = audit_result
        self.biz_types = biz_types
        self.ids = ids
        self.lang = lang
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_illegal_reasons is not None:
            result['AuditIllegalReasons'] = self.audit_illegal_reasons
        if self.audit_result is not None:
            result['AuditResult'] = self.audit_result
        if self.biz_types is not None:
            result['BizTypes'] = self.biz_types
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditIllegalReasons') is not None:
            self.audit_illegal_reasons = m.get('AuditIllegalReasons')
        if m.get('AuditResult') is not None:
            self.audit_result = m.get('AuditResult')
        if m.get('BizTypes') is not None:
            self.biz_types = m.get('BizTypes')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class MarkAuditContentItemResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MarkAuditContentItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MarkAuditContentItemResponseBody = None,
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
            temp_model = MarkAuditContentItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MarkOssResultRequest(TeaModel):
    def __init__(
        self,
        ids: str = None,
        lang: str = None,
        operation: str = None,
        resource_type: str = None,
        scene: str = None,
        source_ip: str = None,
        stock: bool = None,
    ):
        self.ids = ids
        self.lang = lang
        self.operation = operation
        self.resource_type = resource_type
        self.scene = scene
        self.source_ip = source_ip
        self.stock = stock

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.stock is not None:
            result['Stock'] = self.stock
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Stock') is not None:
            self.stock = m.get('Stock')
        return self


class MarkOssResultResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MarkOssResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MarkOssResultResponseBody = None,
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
            temp_model = MarkOssResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MarkWebsiteScanResultRequest(TeaModel):
    def __init__(
        self,
        ids: str = None,
        lang: str = None,
        source_ip: str = None,
    ):
        self.ids = ids
        self.lang = lang
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class MarkWebsiteScanResultResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MarkWebsiteScanResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MarkWebsiteScanResultResponseBody = None,
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
            temp_model = MarkWebsiteScanResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefundCdiBagRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        resource_owner_id: str = None,
    ):
        self.instance_id = instance_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class RefundCdiBagResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefundCdiBagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefundCdiBagResponseBody = None,
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
            temp_model = RefundCdiBagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefundCdiBaseBagRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        resource_owner_id: str = None,
    ):
        self.instance_id = instance_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class RefundCdiBaseBagResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefundCdiBaseBagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefundCdiBaseBagResponseBody = None,
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
            temp_model = RefundCdiBaseBagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefundWebSiteInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        resource_owner_id: str = None,
    ):
        self.instance_id = instance_id
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class RefundWebSiteInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefundWebSiteInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RefundWebSiteInstanceResponseBody = None,
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
            temp_model = RefundWebSiteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewWebSiteInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        commodity_code: str = None,
        duration: int = None,
        instance_id: str = None,
        order_num: int = None,
        order_type: str = None,
        owner_id: int = None,
        pricing_cycle: str = None,
    ):
        self.client_token = client_token
        self.commodity_code = commodity_code
        self.duration = duration
        self.instance_id = instance_id
        self.order_num = order_num
        self.order_type = order_type
        self.owner_id = owner_id
        self.pricing_cycle = pricing_cycle

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_num is not None:
            result['OrderNum'] = self.order_num
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderNum') is not None:
            self.order_num = m.get('OrderNum')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        return self


class RenewWebSiteInstanceResponseBodyInstanceIds(TeaModel):
    def __init__(
        self,
        string: List[str] = None,
    ):
        self.string = string

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.string is not None:
            result['String'] = self.string
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('String') is not None:
            self.string = m.get('String')
        return self


class RenewWebSiteInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        instance_id: str = None,
        instance_ids: RenewWebSiteInstanceResponseBodyInstanceIds = None,
        message: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.instance_id = instance_id
        self.instance_ids = instance_ids
        self.message = message
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceIds') is not None:
            temp_model = RenewWebSiteInstanceResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m['InstanceIds'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenewWebSiteInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenewWebSiteInstanceResponseBody = None,
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
            temp_model = RenewWebSiteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendVerifyCodeToEmailRequest(TeaModel):
    def __init__(
        self,
        email: str = None,
        lang: str = None,
        source_ip: str = None,
    ):
        self.email = email
        self.lang = lang
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class SendVerifyCodeToEmailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendVerifyCodeToEmailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendVerifyCodeToEmailResponseBody = None,
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
            temp_model = SendVerifyCodeToEmailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendVerifyCodeToPhoneRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        phone: str = None,
        source_ip: str = None,
    ):
        self.lang = lang
        self.phone = phone
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class SendVerifyCodeToPhoneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendVerifyCodeToPhoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendVerifyCodeToPhoneResponseBody = None,
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
            temp_model = SendVerifyCodeToPhoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendWebsiteFeedbackRequest(TeaModel):
    def __init__(
        self,
        feedback: str = None,
        lang: str = None,
        source_ip: str = None,
        urls: str = None,
    ):
        self.feedback = feedback
        self.lang = lang
        self.source_ip = source_ip
        self.urls = urls

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.urls is not None:
            result['Urls'] = self.urls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Urls') is not None:
            self.urls = m.get('Urls')
        return self


class SendWebsiteFeedbackResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendWebsiteFeedbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendWebsiteFeedbackResponseBody = None,
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
            temp_model = SendWebsiteFeedbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppPackageRequest(TeaModel):
    def __init__(
        self,
        debug: bool = None,
        id: int = None,
        lang: str = None,
        package_url: str = None,
        platform: str = None,
        source_ip: str = None,
    ):
        self.debug = debug
        self.id = id
        self.lang = lang
        self.package_url = package_url
        self.platform = platform
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debug is not None:
            result['Debug'] = self.debug
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.package_url is not None:
            result['PackageUrl'] = self.package_url
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Debug') is not None:
            self.debug = m.get('Debug')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class UpdateAppPackageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpdateAppPackageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAppPackageResponseBody = None,
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
            temp_model = UpdateAppPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAuditCallbackRequest(TeaModel):
    def __init__(
        self,
        callback: str = None,
        crypt_type: int = None,
        seed: str = None,
    ):
        self.callback = callback
        self.crypt_type = crypt_type
        self.seed = seed

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.crypt_type is not None:
            result['CryptType'] = self.crypt_type
        if self.seed is not None:
            result['Seed'] = self.seed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CryptType') is not None:
            self.crypt_type = m.get('CryptType')
        if m.get('Seed') is not None:
            self.seed = m.get('Seed')
        return self


class UpdateAuditCallbackResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAuditCallbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAuditCallbackResponseBody = None,
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
            temp_model = UpdateAuditCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAuditRangeRequest(TeaModel):
    def __init__(
        self,
        audit_range: str = None,
    ):
        self.audit_range = audit_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_range is not None:
            result['AuditRange'] = self.audit_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditRange') is not None:
            self.audit_range = m.get('AuditRange')
        return self


class UpdateAuditRangeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAuditRangeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAuditRangeResponseBody = None,
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
            temp_model = UpdateAuditRangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAuditSettingRequest(TeaModel):
    def __init__(
        self,
        audit_range: str = None,
        callback: str = None,
        seed: str = None,
        source_ip: str = None,
    ):
        self.audit_range = audit_range
        self.callback = callback
        self.seed = seed
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_range is not None:
            result['AuditRange'] = self.audit_range
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.seed is not None:
            result['Seed'] = self.seed
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditRange') is not None:
            self.audit_range = m.get('AuditRange')
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('Seed') is not None:
            self.seed = m.get('Seed')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class UpdateAuditSettingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAuditSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAuditSettingResponseBody = None,
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
            temp_model = UpdateAuditSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBizTypeRequest(TeaModel):
    def __init__(
        self,
        biz_type_name: str = None,
        description: str = None,
    ):
        self.biz_type_name = biz_type_name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_name is not None:
            result['BizTypeName'] = self.biz_type_name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTypeName') is not None:
            self.biz_type_name = m.get('BizTypeName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class UpdateBizTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateBizTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateBizTypeResponseBody = None,
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
            temp_model = UpdateBizTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBizTypeImageLibRequest(TeaModel):
    def __init__(
        self,
        biz_type_name: str = None,
        black: str = None,
        resource_type: str = None,
        review: str = None,
        scene: str = None,
        white: str = None,
    ):
        self.biz_type_name = biz_type_name
        self.black = black
        self.resource_type = resource_type
        self.review = review
        self.scene = scene
        self.white = white

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_name is not None:
            result['BizTypeName'] = self.biz_type_name
        if self.black is not None:
            result['Black'] = self.black
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.review is not None:
            result['Review'] = self.review
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.white is not None:
            result['White'] = self.white
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTypeName') is not None:
            self.biz_type_name = m.get('BizTypeName')
        if m.get('Black') is not None:
            self.black = m.get('Black')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Review') is not None:
            self.review = m.get('Review')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('White') is not None:
            self.white = m.get('White')
        return self


class UpdateBizTypeImageLibResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateBizTypeImageLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateBizTypeImageLibResponseBody = None,
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
            temp_model = UpdateBizTypeImageLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBizTypeSettingRequest(TeaModel):
    def __init__(
        self,
        ad: str = None,
        antispam: str = None,
        biz_type_name: str = None,
        live: str = None,
        porn: str = None,
        resource_type: str = None,
        terrorism: str = None,
    ):
        self.ad = ad
        self.antispam = antispam
        self.biz_type_name = biz_type_name
        self.live = live
        self.porn = porn
        self.resource_type = resource_type
        self.terrorism = terrorism

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad is not None:
            result['Ad'] = self.ad
        if self.antispam is not None:
            result['Antispam'] = self.antispam
        if self.biz_type_name is not None:
            result['BizTypeName'] = self.biz_type_name
        if self.live is not None:
            result['Live'] = self.live
        if self.porn is not None:
            result['Porn'] = self.porn
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.terrorism is not None:
            result['Terrorism'] = self.terrorism
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ad') is not None:
            self.ad = m.get('Ad')
        if m.get('Antispam') is not None:
            self.antispam = m.get('Antispam')
        if m.get('BizTypeName') is not None:
            self.biz_type_name = m.get('BizTypeName')
        if m.get('Live') is not None:
            self.live = m.get('Live')
        if m.get('Porn') is not None:
            self.porn = m.get('Porn')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Terrorism') is not None:
            self.terrorism = m.get('Terrorism')
        return self


class UpdateBizTypeSettingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateBizTypeSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateBizTypeSettingResponseBody = None,
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
            temp_model = UpdateBizTypeSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateBizTypeTextLibRequest(TeaModel):
    def __init__(
        self,
        biz_type_name: str = None,
        black: str = None,
        ignore: str = None,
        resource_type: str = None,
        review: str = None,
        scene: str = None,
        white: str = None,
    ):
        self.biz_type_name = biz_type_name
        self.black = black
        self.ignore = ignore
        self.resource_type = resource_type
        self.review = review
        self.scene = scene
        self.white = white

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type_name is not None:
            result['BizTypeName'] = self.biz_type_name
        if self.black is not None:
            result['Black'] = self.black
        if self.ignore is not None:
            result['Ignore'] = self.ignore
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.review is not None:
            result['Review'] = self.review
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.white is not None:
            result['White'] = self.white
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTypeName') is not None:
            self.biz_type_name = m.get('BizTypeName')
        if m.get('Black') is not None:
            self.black = m.get('Black')
        if m.get('Ignore') is not None:
            self.ignore = m.get('Ignore')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Review') is not None:
            self.review = m.get('Review')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('White') is not None:
            self.white = m.get('White')
        return self


class UpdateBizTypeTextLibResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateBizTypeTextLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateBizTypeTextLibResponseBody = None,
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
            temp_model = UpdateBizTypeTextLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCustomOcrTemplateRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        recognize_area: str = None,
        refer_area: str = None,
    ):
        self.id = id
        self.name = name
        self.recognize_area = recognize_area
        self.refer_area = refer_area

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.recognize_area is not None:
            result['RecognizeArea'] = self.recognize_area
        if self.refer_area is not None:
            result['ReferArea'] = self.refer_area
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RecognizeArea') is not None:
            self.recognize_area = m.get('RecognizeArea')
        if m.get('ReferArea') is not None:
            self.refer_area = m.get('ReferArea')
        return self


class UpdateCustomOcrTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateCustomOcrTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCustomOcrTemplateResponseBody = None,
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
            temp_model = UpdateCustomOcrTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateKeywordLibRequest(TeaModel):
    def __init__(
        self,
        biz_types: str = None,
        enable: bool = None,
        id: int = None,
        lang: str = None,
        match_mode: str = None,
        name: str = None,
        source_ip: str = None,
    ):
        self.biz_types = biz_types
        self.enable = enable
        self.id = id
        self.lang = lang
        self.match_mode = match_mode
        self.name = name
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_types is not None:
            result['BizTypes'] = self.biz_types
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.id is not None:
            result['Id'] = self.id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode
        if self.name is not None:
            result['Name'] = self.name
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTypes') is not None:
            self.biz_types = m.get('BizTypes')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class UpdateKeywordLibResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateKeywordLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateKeywordLibResponseBody = None,
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
            temp_model = UpdateKeywordLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNotificationSettingRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        realtime_message_list: str = None,
        reminder_mode_list: str = None,
        schedule_message_time: int = None,
        schedule_message_time_zone: int = None,
        source_ip: str = None,
    ):
        self.lang = lang
        self.realtime_message_list = realtime_message_list
        self.reminder_mode_list = reminder_mode_list
        self.schedule_message_time = schedule_message_time
        self.schedule_message_time_zone = schedule_message_time_zone
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.realtime_message_list is not None:
            result['RealtimeMessageList'] = self.realtime_message_list
        if self.reminder_mode_list is not None:
            result['ReminderModeList'] = self.reminder_mode_list
        if self.schedule_message_time is not None:
            result['ScheduleMessageTime'] = self.schedule_message_time
        if self.schedule_message_time_zone is not None:
            result['ScheduleMessageTimeZone'] = self.schedule_message_time_zone
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RealtimeMessageList') is not None:
            self.realtime_message_list = m.get('RealtimeMessageList')
        if m.get('ReminderModeList') is not None:
            self.reminder_mode_list = m.get('ReminderModeList')
        if m.get('ScheduleMessageTime') is not None:
            self.schedule_message_time = m.get('ScheduleMessageTime')
        if m.get('ScheduleMessageTimeZone') is not None:
            self.schedule_message_time_zone = m.get('ScheduleMessageTimeZone')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        return self


class UpdateNotificationSettingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateNotificationSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateNotificationSettingResponseBody = None,
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
            temp_model = UpdateNotificationSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateOssCallbackSettingRequest(TeaModel):
    def __init__(
        self,
        audit_callback: bool = None,
        callback_seed: str = None,
        callback_url: str = None,
        scan_callback: bool = None,
        scan_callback_suggestions: str = None,
        service_modules: str = None,
    ):
        self.audit_callback = audit_callback
        self.callback_seed = callback_seed
        self.callback_url = callback_url
        self.scan_callback = scan_callback
        self.scan_callback_suggestions = scan_callback_suggestions
        self.service_modules = service_modules

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_callback is not None:
            result['AuditCallback'] = self.audit_callback
        if self.callback_seed is not None:
            result['CallbackSeed'] = self.callback_seed
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.scan_callback is not None:
            result['ScanCallback'] = self.scan_callback
        if self.scan_callback_suggestions is not None:
            result['ScanCallbackSuggestions'] = self.scan_callback_suggestions
        if self.service_modules is not None:
            result['ServiceModules'] = self.service_modules
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditCallback') is not None:
            self.audit_callback = m.get('AuditCallback')
        if m.get('CallbackSeed') is not None:
            self.callback_seed = m.get('CallbackSeed')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('ScanCallback') is not None:
            self.scan_callback = m.get('ScanCallback')
        if m.get('ScanCallbackSuggestions') is not None:
            self.scan_callback_suggestions = m.get('ScanCallbackSuggestions')
        if m.get('ServiceModules') is not None:
            self.service_modules = m.get('ServiceModules')
        return self


class UpdateOssCallbackSettingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateOssCallbackSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateOssCallbackSettingResponseBody = None,
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
            temp_model = UpdateOssCallbackSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateOssIncrementCheckSettingRequest(TeaModel):
    def __init__(
        self,
        audio_antispam_freeze_config: str = None,
        audio_auto_freeze_opened: bool = None,
        audio_max_size: int = None,
        audio_scan_limit: int = None,
        audio_scene_list: str = None,
        auto_freeze_type: str = None,
        biz_type: str = None,
        bucket_config_list: str = None,
        callback_id: str = None,
        image_ad_freeze_config: str = None,
        image_auto_freeze: str = None,
        image_auto_freeze_opened: bool = None,
        image_live_freeze_config: str = None,
        image_porn_freeze_config: str = None,
        image_scan_limit: str = None,
        image_scene_list: str = None,
        image_terrorism_freeze_config: str = None,
        lang: str = None,
        scan_image_no_file_type: bool = None,
        source_ip: str = None,
        video_ad_freeze_config: str = None,
        video_auto_freeze_opened: bool = None,
        video_auto_freeze_scene_list: str = None,
        video_frame_interval: int = None,
        video_live_freeze_config: str = None,
        video_max_frames: int = None,
        video_max_size: int = None,
        video_porn_freeze_config: str = None,
        video_scan_limit: int = None,
        video_scene_list: str = None,
        video_terrorism_freeze_config: str = None,
        video_voice_antispam_freeze_config: str = None,
    ):
        self.audio_antispam_freeze_config = audio_antispam_freeze_config
        self.audio_auto_freeze_opened = audio_auto_freeze_opened
        self.audio_max_size = audio_max_size
        self.audio_scan_limit = audio_scan_limit
        self.audio_scene_list = audio_scene_list
        self.auto_freeze_type = auto_freeze_type
        self.biz_type = biz_type
        self.bucket_config_list = bucket_config_list
        self.callback_id = callback_id
        self.image_ad_freeze_config = image_ad_freeze_config
        self.image_auto_freeze = image_auto_freeze
        self.image_auto_freeze_opened = image_auto_freeze_opened
        self.image_live_freeze_config = image_live_freeze_config
        self.image_porn_freeze_config = image_porn_freeze_config
        self.image_scan_limit = image_scan_limit
        self.image_scene_list = image_scene_list
        self.image_terrorism_freeze_config = image_terrorism_freeze_config
        self.lang = lang
        self.scan_image_no_file_type = scan_image_no_file_type
        self.source_ip = source_ip
        self.video_ad_freeze_config = video_ad_freeze_config
        self.video_auto_freeze_opened = video_auto_freeze_opened
        self.video_auto_freeze_scene_list = video_auto_freeze_scene_list
        self.video_frame_interval = video_frame_interval
        self.video_live_freeze_config = video_live_freeze_config
        self.video_max_frames = video_max_frames
        self.video_max_size = video_max_size
        self.video_porn_freeze_config = video_porn_freeze_config
        self.video_scan_limit = video_scan_limit
        self.video_scene_list = video_scene_list
        self.video_terrorism_freeze_config = video_terrorism_freeze_config
        self.video_voice_antispam_freeze_config = video_voice_antispam_freeze_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_antispam_freeze_config is not None:
            result['AudioAntispamFreezeConfig'] = self.audio_antispam_freeze_config
        if self.audio_auto_freeze_opened is not None:
            result['AudioAutoFreezeOpened'] = self.audio_auto_freeze_opened
        if self.audio_max_size is not None:
            result['AudioMaxSize'] = self.audio_max_size
        if self.audio_scan_limit is not None:
            result['AudioScanLimit'] = self.audio_scan_limit
        if self.audio_scene_list is not None:
            result['AudioSceneList'] = self.audio_scene_list
        if self.auto_freeze_type is not None:
            result['AutoFreezeType'] = self.auto_freeze_type
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.bucket_config_list is not None:
            result['BucketConfigList'] = self.bucket_config_list
        if self.callback_id is not None:
            result['CallbackId'] = self.callback_id
        if self.image_ad_freeze_config is not None:
            result['ImageAdFreezeConfig'] = self.image_ad_freeze_config
        if self.image_auto_freeze is not None:
            result['ImageAutoFreeze'] = self.image_auto_freeze
        if self.image_auto_freeze_opened is not None:
            result['ImageAutoFreezeOpened'] = self.image_auto_freeze_opened
        if self.image_live_freeze_config is not None:
            result['ImageLiveFreezeConfig'] = self.image_live_freeze_config
        if self.image_porn_freeze_config is not None:
            result['ImagePornFreezeConfig'] = self.image_porn_freeze_config
        if self.image_scan_limit is not None:
            result['ImageScanLimit'] = self.image_scan_limit
        if self.image_scene_list is not None:
            result['ImageSceneList'] = self.image_scene_list
        if self.image_terrorism_freeze_config is not None:
            result['ImageTerrorismFreezeConfig'] = self.image_terrorism_freeze_config
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.scan_image_no_file_type is not None:
            result['ScanImageNoFileType'] = self.scan_image_no_file_type
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.video_ad_freeze_config is not None:
            result['VideoAdFreezeConfig'] = self.video_ad_freeze_config
        if self.video_auto_freeze_opened is not None:
            result['VideoAutoFreezeOpened'] = self.video_auto_freeze_opened
        if self.video_auto_freeze_scene_list is not None:
            result['VideoAutoFreezeSceneList'] = self.video_auto_freeze_scene_list
        if self.video_frame_interval is not None:
            result['VideoFrameInterval'] = self.video_frame_interval
        if self.video_live_freeze_config is not None:
            result['VideoLiveFreezeConfig'] = self.video_live_freeze_config
        if self.video_max_frames is not None:
            result['VideoMaxFrames'] = self.video_max_frames
        if self.video_max_size is not None:
            result['VideoMaxSize'] = self.video_max_size
        if self.video_porn_freeze_config is not None:
            result['VideoPornFreezeConfig'] = self.video_porn_freeze_config
        if self.video_scan_limit is not None:
            result['VideoScanLimit'] = self.video_scan_limit
        if self.video_scene_list is not None:
            result['VideoSceneList'] = self.video_scene_list
        if self.video_terrorism_freeze_config is not None:
            result['VideoTerrorismFreezeConfig'] = self.video_terrorism_freeze_config
        if self.video_voice_antispam_freeze_config is not None:
            result['VideoVoiceAntispamFreezeConfig'] = self.video_voice_antispam_freeze_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioAntispamFreezeConfig') is not None:
            self.audio_antispam_freeze_config = m.get('AudioAntispamFreezeConfig')
        if m.get('AudioAutoFreezeOpened') is not None:
            self.audio_auto_freeze_opened = m.get('AudioAutoFreezeOpened')
        if m.get('AudioMaxSize') is not None:
            self.audio_max_size = m.get('AudioMaxSize')
        if m.get('AudioScanLimit') is not None:
            self.audio_scan_limit = m.get('AudioScanLimit')
        if m.get('AudioSceneList') is not None:
            self.audio_scene_list = m.get('AudioSceneList')
        if m.get('AutoFreezeType') is not None:
            self.auto_freeze_type = m.get('AutoFreezeType')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('BucketConfigList') is not None:
            self.bucket_config_list = m.get('BucketConfigList')
        if m.get('CallbackId') is not None:
            self.callback_id = m.get('CallbackId')
        if m.get('ImageAdFreezeConfig') is not None:
            self.image_ad_freeze_config = m.get('ImageAdFreezeConfig')
        if m.get('ImageAutoFreeze') is not None:
            self.image_auto_freeze = m.get('ImageAutoFreeze')
        if m.get('ImageAutoFreezeOpened') is not None:
            self.image_auto_freeze_opened = m.get('ImageAutoFreezeOpened')
        if m.get('ImageLiveFreezeConfig') is not None:
            self.image_live_freeze_config = m.get('ImageLiveFreezeConfig')
        if m.get('ImagePornFreezeConfig') is not None:
            self.image_porn_freeze_config = m.get('ImagePornFreezeConfig')
        if m.get('ImageScanLimit') is not None:
            self.image_scan_limit = m.get('ImageScanLimit')
        if m.get('ImageSceneList') is not None:
            self.image_scene_list = m.get('ImageSceneList')
        if m.get('ImageTerrorismFreezeConfig') is not None:
            self.image_terrorism_freeze_config = m.get('ImageTerrorismFreezeConfig')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('ScanImageNoFileType') is not None:
            self.scan_image_no_file_type = m.get('ScanImageNoFileType')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('VideoAdFreezeConfig') is not None:
            self.video_ad_freeze_config = m.get('VideoAdFreezeConfig')
        if m.get('VideoAutoFreezeOpened') is not None:
            self.video_auto_freeze_opened = m.get('VideoAutoFreezeOpened')
        if m.get('VideoAutoFreezeSceneList') is not None:
            self.video_auto_freeze_scene_list = m.get('VideoAutoFreezeSceneList')
        if m.get('VideoFrameInterval') is not None:
            self.video_frame_interval = m.get('VideoFrameInterval')
        if m.get('VideoLiveFreezeConfig') is not None:
            self.video_live_freeze_config = m.get('VideoLiveFreezeConfig')
        if m.get('VideoMaxFrames') is not None:
            self.video_max_frames = m.get('VideoMaxFrames')
        if m.get('VideoMaxSize') is not None:
            self.video_max_size = m.get('VideoMaxSize')
        if m.get('VideoPornFreezeConfig') is not None:
            self.video_porn_freeze_config = m.get('VideoPornFreezeConfig')
        if m.get('VideoScanLimit') is not None:
            self.video_scan_limit = m.get('VideoScanLimit')
        if m.get('VideoSceneList') is not None:
            self.video_scene_list = m.get('VideoSceneList')
        if m.get('VideoTerrorismFreezeConfig') is not None:
            self.video_terrorism_freeze_config = m.get('VideoTerrorismFreezeConfig')
        if m.get('VideoVoiceAntispamFreezeConfig') is not None:
            self.video_voice_antispam_freeze_config = m.get('VideoVoiceAntispamFreezeConfig')
        return self


class UpdateOssIncrementCheckSettingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateOssIncrementCheckSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateOssIncrementCheckSettingResponseBody = None,
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
            temp_model = UpdateOssIncrementCheckSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateOssStockStatusRequest(TeaModel):
    def __init__(
        self,
        audio_auto_freeze_scene_list: str = None,
        audio_max_size: int = None,
        auto_freeze_type: str = None,
        bucket_config_list: str = None,
        end_date: str = None,
        image_auto_freeze: str = None,
        lang: str = None,
        operation: str = None,
        resource_type_list: str = None,
        scene_list: str = None,
        source_ip: str = None,
        start_date: str = None,
        video_auto_freeze_scene_list: str = None,
        video_frame_interval: int = None,
        video_max_frames: int = None,
        video_max_size: int = None,
    ):
        self.audio_auto_freeze_scene_list = audio_auto_freeze_scene_list
        self.audio_max_size = audio_max_size
        self.auto_freeze_type = auto_freeze_type
        self.bucket_config_list = bucket_config_list
        self.end_date = end_date
        self.image_auto_freeze = image_auto_freeze
        self.lang = lang
        self.operation = operation
        self.resource_type_list = resource_type_list
        self.scene_list = scene_list
        self.source_ip = source_ip
        self.start_date = start_date
        self.video_auto_freeze_scene_list = video_auto_freeze_scene_list
        self.video_frame_interval = video_frame_interval
        self.video_max_frames = video_max_frames
        self.video_max_size = video_max_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_auto_freeze_scene_list is not None:
            result['AudioAutoFreezeSceneList'] = self.audio_auto_freeze_scene_list
        if self.audio_max_size is not None:
            result['AudioMaxSize'] = self.audio_max_size
        if self.auto_freeze_type is not None:
            result['AutoFreezeType'] = self.auto_freeze_type
        if self.bucket_config_list is not None:
            result['BucketConfigList'] = self.bucket_config_list
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.image_auto_freeze is not None:
            result['ImageAutoFreeze'] = self.image_auto_freeze
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.operation is not None:
            result['Operation'] = self.operation
        if self.resource_type_list is not None:
            result['ResourceTypeList'] = self.resource_type_list
        if self.scene_list is not None:
            result['SceneList'] = self.scene_list
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        if self.video_auto_freeze_scene_list is not None:
            result['VideoAutoFreezeSceneList'] = self.video_auto_freeze_scene_list
        if self.video_frame_interval is not None:
            result['VideoFrameInterval'] = self.video_frame_interval
        if self.video_max_frames is not None:
            result['VideoMaxFrames'] = self.video_max_frames
        if self.video_max_size is not None:
            result['VideoMaxSize'] = self.video_max_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioAutoFreezeSceneList') is not None:
            self.audio_auto_freeze_scene_list = m.get('AudioAutoFreezeSceneList')
        if m.get('AudioMaxSize') is not None:
            self.audio_max_size = m.get('AudioMaxSize')
        if m.get('AutoFreezeType') is not None:
            self.auto_freeze_type = m.get('AutoFreezeType')
        if m.get('BucketConfigList') is not None:
            self.bucket_config_list = m.get('BucketConfigList')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('ImageAutoFreeze') is not None:
            self.image_auto_freeze = m.get('ImageAutoFreeze')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')
        if m.get('ResourceTypeList') is not None:
            self.resource_type_list = m.get('ResourceTypeList')
        if m.get('SceneList') is not None:
            self.scene_list = m.get('SceneList')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        if m.get('VideoAutoFreezeSceneList') is not None:
            self.video_auto_freeze_scene_list = m.get('VideoAutoFreezeSceneList')
        if m.get('VideoFrameInterval') is not None:
            self.video_frame_interval = m.get('VideoFrameInterval')
        if m.get('VideoMaxFrames') is not None:
            self.video_max_frames = m.get('VideoMaxFrames')
        if m.get('VideoMaxSize') is not None:
            self.video_max_size = m.get('VideoMaxSize')
        return self


class UpdateOssStockStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateOssStockStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateOssStockStatusResponseBody = None,
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
            temp_model = UpdateOssStockStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWebsiteInstanceRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        index_page: str = None,
        index_page_scan_interval: int = None,
        instance_id: str = None,
        lang: str = None,
        site_protocol: str = None,
        source_ip: str = None,
        website_scan_interval: int = None,
    ):
        self.domain = domain
        self.index_page = index_page
        self.index_page_scan_interval = index_page_scan_interval
        self.instance_id = instance_id
        self.lang = lang
        self.site_protocol = site_protocol
        self.source_ip = source_ip
        self.website_scan_interval = website_scan_interval

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.index_page is not None:
            result['IndexPage'] = self.index_page
        if self.index_page_scan_interval is not None:
            result['IndexPageScanInterval'] = self.index_page_scan_interval
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.site_protocol is not None:
            result['SiteProtocol'] = self.site_protocol
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.website_scan_interval is not None:
            result['WebsiteScanInterval'] = self.website_scan_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('IndexPage') is not None:
            self.index_page = m.get('IndexPage')
        if m.get('IndexPageScanInterval') is not None:
            self.index_page_scan_interval = m.get('IndexPageScanInterval')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SiteProtocol') is not None:
            self.site_protocol = m.get('SiteProtocol')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('WebsiteScanInterval') is not None:
            self.website_scan_interval = m.get('WebsiteScanInterval')
        return self


class UpdateWebsiteInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateWebsiteInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateWebsiteInstanceResponseBody = None,
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
            temp_model = UpdateWebsiteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWebsiteInstanceKeyUrlRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        lang: str = None,
        source_ip: str = None,
        urls: str = None,
    ):
        self.instance_id = instance_id
        self.lang = lang
        self.source_ip = source_ip
        self.urls = urls

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.urls is not None:
            result['Urls'] = self.urls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Urls') is not None:
            self.urls = m.get('Urls')
        return self


class UpdateWebsiteInstanceKeyUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateWebsiteInstanceKeyUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateWebsiteInstanceKeyUrlResponseBody = None,
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
            temp_model = UpdateWebsiteInstanceKeyUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWebsiteInstanceStatusRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        lang: str = None,
        source_ip: str = None,
        status: str = None,
    ):
        self.instance_id = instance_id
        self.lang = lang
        self.source_ip = source_ip
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateWebsiteInstanceStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateWebsiteInstanceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateWebsiteInstanceStatusResponseBody = None,
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
            temp_model = UpdateWebsiteInstanceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeCdiBaseBagRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        commodity_code: str = None,
        flow_out_spec: int = None,
        instance_id: str = None,
        order_type: str = None,
        owner_id: int = None,
    ):
        self.client_token = client_token
        self.commodity_code = commodity_code
        self.flow_out_spec = flow_out_spec
        self.instance_id = instance_id
        self.order_type = order_type
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.flow_out_spec is not None:
            result['FlowOutSpec'] = self.flow_out_spec
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('FlowOutSpec') is not None:
            self.flow_out_spec = m.get('FlowOutSpec')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class UpgradeCdiBaseBagResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        instance_id: str = None,
        message: str = None,
        order_id: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.instance_id = instance_id
        self.message = message
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpgradeCdiBaseBagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeCdiBaseBagResponseBody = None,
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
            temp_model = UpgradeCdiBaseBagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadImageToLibRequest(TeaModel):
    def __init__(
        self,
        image_lib_id: int = None,
        images: str = None,
        source_ip: str = None,
        urls: str = None,
    ):
        self.image_lib_id = image_lib_id
        self.images = images
        self.source_ip = source_ip
        self.urls = urls

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_lib_id is not None:
            result['ImageLibId'] = self.image_lib_id
        if self.images is not None:
            result['Images'] = self.images
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.urls is not None:
            result['Urls'] = self.urls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageLibId') is not None:
            self.image_lib_id = m.get('ImageLibId')
        if m.get('Images') is not None:
            self.images = m.get('Images')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('Urls') is not None:
            self.urls = m.get('Urls')
        return self


class UploadImageToLibResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UploadImageToLibResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UploadImageToLibResponseBody = None,
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
            temp_model = UploadImageToLibResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyCustomOcrTemplateRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        test_img_url: str = None,
    ):
        self.id = id
        self.test_img_url = test_img_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.test_img_url is not None:
            result['TestImgUrl'] = self.test_img_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TestImgUrl') is not None:
            self.test_img_url = m.get('TestImgUrl')
        return self


class VerifyCustomOcrTemplateResponseBody(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        recognize_info: str = None,
        request_id: str = None,
    ):
        self.image_url = image_url
        self.recognize_info = recognize_info
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.recognize_info is not None:
            result['RecognizeInfo'] = self.recognize_info
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('RecognizeInfo') is not None:
            self.recognize_info = m.get('RecognizeInfo')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifyCustomOcrTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyCustomOcrTemplateResponseBody = None,
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
            temp_model = VerifyCustomOcrTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyEmailRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        source_ip: str = None,
        verify_code: str = None,
    ):
        self.lang = lang
        self.source_ip = source_ip
        self.verify_code = verify_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')
        return self


class VerifyEmailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifyEmailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyEmailResponseBody = None,
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
            temp_model = VerifyEmailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyPhoneRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
        phone: str = None,
        source_ip: str = None,
        verify_code: str = None,
    ):
        self.lang = lang
        self.phone = phone
        self.source_ip = source_ip
        self.verify_code = verify_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.verify_code is not None:
            result['VerifyCode'] = self.verify_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('VerifyCode') is not None:
            self.verify_code = m.get('VerifyCode')
        return self


class VerifyPhoneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifyPhoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyPhoneResponseBody = None,
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
            temp_model = VerifyPhoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyWebsiteInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        lang: str = None,
        source_ip: str = None,
        verify_method: str = None,
    ):
        self.instance_id = instance_id
        self.lang = lang
        self.source_ip = source_ip
        self.verify_method = verify_method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip
        if self.verify_method is not None:
            result['VerifyMethod'] = self.verify_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')
        if m.get('VerifyMethod') is not None:
            self.verify_method = m.get('VerifyMethod')
        return self


class VerifyWebsiteInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifyWebsiteInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyWebsiteInstanceResponseBody = None,
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
            temp_model = VerifyWebsiteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


