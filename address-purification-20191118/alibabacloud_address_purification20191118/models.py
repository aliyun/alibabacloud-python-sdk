# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any


class GetAddressDivisionCodeRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
        default_province: str = None,
        default_city: str = None,
        default_district: str = None,
        app_key: str = None,
    ):
        self.service_code = service_code
        self.text = text
        self.default_province = default_province
        self.default_city = default_city
        self.default_district = default_district
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class GetAddressDivisionCodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetAddressDivisionCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAddressDivisionCodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAddressDivisionCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StructureAddressRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
        default_province: str = None,
        default_city: str = None,
        default_district: str = None,
        app_key: str = None,
    ):
        self.service_code = service_code
        self.text = text
        self.default_province = default_province
        self.default_city = default_city
        self.default_district = default_district
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class StructureAddressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class StructureAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StructureAddressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StructureAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExtractExpressRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
        default_province: str = None,
        default_city: str = None,
        default_district: str = None,
        app_key: str = None,
    ):
        self.service_code = service_code
        self.text = text
        self.default_province = default_province
        self.default_city = default_city
        self.default_district = default_district
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class ExtractExpressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ExtractExpressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExtractExpressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ExtractExpressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExtractNameRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
        default_province: str = None,
        default_city: str = None,
        default_district: str = None,
        app_key: str = None,
    ):
        self.service_code = service_code
        self.text = text
        self.default_province = default_province
        self.default_city = default_city
        self.default_district = default_district
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class ExtractNameResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ExtractNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExtractNameResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ExtractNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAddressBlockMappingRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
        default_province: str = None,
        default_city: str = None,
        default_district: str = None,
        app_key: str = None,
    ):
        self.service_code = service_code
        self.text = text
        self.default_province = default_province
        self.default_city = default_city
        self.default_district = default_district
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class GetAddressBlockMappingResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetAddressBlockMappingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAddressBlockMappingResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAddressBlockMappingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAddressSearchRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
        default_province: str = None,
        default_city: str = None,
        default_district: str = None,
        app_key: str = None,
    ):
        self.service_code = service_code
        self.text = text
        self.default_province = default_province
        self.default_city = default_city
        self.default_district = default_district
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class GetAddressSearchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetAddressSearchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAddressSearchResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAddressSearchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PredictPOIRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
        default_province: str = None,
        default_city: str = None,
        default_district: str = None,
        app_key: str = None,
    ):
        self.service_code = service_code
        self.text = text
        self.default_province = default_province
        self.default_city = default_city
        self.default_district = default_district
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class PredictPOIResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class PredictPOIResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PredictPOIResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PredictPOIResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ClassifyPOIRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
        default_province: str = None,
        default_city: str = None,
        default_district: str = None,
        app_key: str = None,
    ):
        self.service_code = service_code
        self.text = text
        self.default_province = default_province
        self.default_city = default_city
        self.default_district = default_district
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class ClassifyPOIResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ClassifyPOIResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ClassifyPOIResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ClassifyPOIResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CorrectAddressRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
        default_province: str = None,
        default_city: str = None,
        default_district: str = None,
        app_key: str = None,
    ):
        self.service_code = service_code
        self.text = text
        self.default_province = default_province
        self.default_city = default_city
        self.default_district = default_district
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class CorrectAddressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class CorrectAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CorrectAddressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CorrectAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetZipcodeRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
        default_province: str = None,
        default_city: str = None,
        default_district: str = None,
        app_key: str = None,
    ):
        self.service_code = service_code
        self.text = text
        self.default_province = default_province
        self.default_city = default_city
        self.default_district = default_district
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class GetZipcodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetZipcodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetZipcodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetZipcodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CompleteAddressRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
        default_province: str = None,
        default_city: str = None,
        default_district: str = None,
        app_key: str = None,
    ):
        self.service_code = service_code
        self.text = text
        self.default_province = default_province
        self.default_city = default_city
        self.default_district = default_district
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class CompleteAddressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class CompleteAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CompleteAddressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CompleteAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAddressSimilarityRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
        default_province: str = None,
        default_city: str = None,
        default_district: str = None,
        app_key: str = None,
    ):
        self.service_code = service_code
        self.text = text
        self.default_province = default_province
        self.default_city = default_city
        self.default_district = default_district
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class GetAddressSimilarityResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetAddressSimilarityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAddressSimilarityResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAddressSimilarityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAddressGeocodeRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
        default_province: str = None,
        default_city: str = None,
        default_district: str = None,
        app_key: str = None,
    ):
        self.service_code = service_code
        self.text = text
        self.default_province = default_province
        self.default_city = default_city
        self.default_district = default_district
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class GetAddressGeocodeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetAddressGeocodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAddressGeocodeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAddressGeocodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferCoordRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
        src_coord: str = None,
        default_province: str = None,
        default_city: str = None,
        default_district: str = None,
        app_key: str = None,
    ):
        self.service_code = service_code
        self.text = text
        self.src_coord = src_coord
        self.default_province = default_province
        self.default_city = default_city
        self.default_district = default_district
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.src_coord is not None:
            result['SrcCoord'] = self.src_coord
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('SrcCoord') is not None:
            self.src_coord = m.get('SrcCoord')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class TransferCoordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class TransferCoordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TransferCoordResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TransferCoordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        parameters: Dict[str, Any] = None,
    ):
        self.service_code = service_code
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class UpdateProjectShrinkRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        parameters_shrink: str = None,
    ):
        self.service_code = service_code
        self.parameters_shrink = parameters_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        return self


class UpdateProjectResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class UpdateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateProjectResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExtractPhoneRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
        default_province: str = None,
        default_city: str = None,
        default_district: str = None,
        app_key: str = None,
    ):
        self.service_code = service_code
        self.text = text
        self.default_province = default_province
        self.default_city = default_city
        self.default_district = default_district
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class ExtractPhoneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ExtractPhoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExtractPhoneResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ExtractPhoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInputSearchRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
        default_province: str = None,
        default_city: str = None,
        default_district: str = None,
        app_key: str = None,
    ):
        self.service_code = service_code
        self.text = text
        self.default_province = default_province
        self.default_city = default_city
        self.default_district = default_district
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class GetInputSearchResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetInputSearchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInputSearchResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetInputSearchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAddressEvaluateRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
        default_province: str = None,
        default_city: str = None,
        default_district: str = None,
        app_key: str = None,
    ):
        self.service_code = service_code
        self.text = text
        self.default_province = default_province
        self.default_city = default_city
        self.default_district = default_district
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class GetAddressEvaluateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetAddressEvaluateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAddressEvaluateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAddressEvaluateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExtractAddressRequest(TeaModel):
    def __init__(
        self,
        service_code: str = None,
        text: str = None,
        default_province: str = None,
        default_city: str = None,
        default_district: str = None,
        app_key: str = None,
    ):
        self.service_code = service_code
        self.text = text
        self.default_province = default_province
        self.default_city = default_city
        self.default_district = default_district
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class ExtractAddressResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ExtractAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExtractAddressResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ExtractAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


