# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import Dict, Any
except ImportError:
    pass


class GetAddressGeocodeRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text                # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key          # type: str

    def validate(self):
        self.validate_required(self.service_code, 'service_code')
        self.validate_required(self.text, 'text')
        self.validate_required(self.app_key, 'app_key')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('ServiceCode') is not None:
            self.service_code = map.get('ServiceCode')
        if map.get('Text') is not None:
            self.text = map.get('Text')
        if map.get('DefaultProvince') is not None:
            self.default_province = map.get('DefaultProvince')
        if map.get('DefaultCity') is not None:
            self.default_city = map.get('DefaultCity')
        if map.get('DefaultDistrict') is not None:
            self.default_district = map.get('DefaultDistrict')
        if map.get('AppKey') is not None:
            self.app_key = map.get('AppKey')
        return self


class GetAddressGeocodeResponse(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data                # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.data, 'data')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('Data') is not None:
            self.data = map.get('Data')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class CompleteAddressRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text                # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key          # type: str

    def validate(self):
        self.validate_required(self.service_code, 'service_code')
        self.validate_required(self.text, 'text')
        self.validate_required(self.app_key, 'app_key')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('ServiceCode') is not None:
            self.service_code = map.get('ServiceCode')
        if map.get('Text') is not None:
            self.text = map.get('Text')
        if map.get('DefaultProvince') is not None:
            self.default_province = map.get('DefaultProvince')
        if map.get('DefaultCity') is not None:
            self.default_city = map.get('DefaultCity')
        if map.get('DefaultDistrict') is not None:
            self.default_district = map.get('DefaultDistrict')
        if map.get('AppKey') is not None:
            self.app_key = map.get('AppKey')
        return self


class CompleteAddressResponse(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data                # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.data, 'data')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('Data') is not None:
            self.data = map.get('Data')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class GetZipcodeRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text                # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key          # type: str

    def validate(self):
        self.validate_required(self.service_code, 'service_code')
        self.validate_required(self.text, 'text')
        self.validate_required(self.app_key, 'app_key')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('ServiceCode') is not None:
            self.service_code = map.get('ServiceCode')
        if map.get('Text') is not None:
            self.text = map.get('Text')
        if map.get('DefaultProvince') is not None:
            self.default_province = map.get('DefaultProvince')
        if map.get('DefaultCity') is not None:
            self.default_city = map.get('DefaultCity')
        if map.get('DefaultDistrict') is not None:
            self.default_district = map.get('DefaultDistrict')
        if map.get('AppKey') is not None:
            self.app_key = map.get('AppKey')
        return self


class GetZipcodeResponse(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data                # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.data, 'data')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('Data') is not None:
            self.data = map.get('Data')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class ExtractPhoneRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text                # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key          # type: str

    def validate(self):
        self.validate_required(self.service_code, 'service_code')
        self.validate_required(self.text, 'text')
        self.validate_required(self.app_key, 'app_key')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('ServiceCode') is not None:
            self.service_code = map.get('ServiceCode')
        if map.get('Text') is not None:
            self.text = map.get('Text')
        if map.get('DefaultProvince') is not None:
            self.default_province = map.get('DefaultProvince')
        if map.get('DefaultCity') is not None:
            self.default_city = map.get('DefaultCity')
        if map.get('DefaultDistrict') is not None:
            self.default_district = map.get('DefaultDistrict')
        if map.get('AppKey') is not None:
            self.app_key = map.get('AppKey')
        return self


class ExtractPhoneResponse(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data                # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.data, 'data')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('Data') is not None:
            self.data = map.get('Data')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class ExtractNameRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text                # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key          # type: str

    def validate(self):
        self.validate_required(self.service_code, 'service_code')
        self.validate_required(self.text, 'text')
        self.validate_required(self.app_key, 'app_key')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('ServiceCode') is not None:
            self.service_code = map.get('ServiceCode')
        if map.get('Text') is not None:
            self.text = map.get('Text')
        if map.get('DefaultProvince') is not None:
            self.default_province = map.get('DefaultProvince')
        if map.get('DefaultCity') is not None:
            self.default_city = map.get('DefaultCity')
        if map.get('DefaultDistrict') is not None:
            self.default_district = map.get('DefaultDistrict')
        if map.get('AppKey') is not None:
            self.app_key = map.get('AppKey')
        return self


class ExtractNameResponse(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data                # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.data, 'data')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('Data') is not None:
            self.data = map.get('Data')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class GetAddressDivisionCodeRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text                # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key          # type: str

    def validate(self):
        self.validate_required(self.service_code, 'service_code')
        self.validate_required(self.text, 'text')
        self.validate_required(self.app_key, 'app_key')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('ServiceCode') is not None:
            self.service_code = map.get('ServiceCode')
        if map.get('Text') is not None:
            self.text = map.get('Text')
        if map.get('DefaultProvince') is not None:
            self.default_province = map.get('DefaultProvince')
        if map.get('DefaultCity') is not None:
            self.default_city = map.get('DefaultCity')
        if map.get('DefaultDistrict') is not None:
            self.default_district = map.get('DefaultDistrict')
        if map.get('AppKey') is not None:
            self.app_key = map.get('AppKey')
        return self


class GetAddressDivisionCodeResponse(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data                # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.data, 'data')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('Data') is not None:
            self.data = map.get('Data')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class ClassifyPOIRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text                # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key          # type: str

    def validate(self):
        self.validate_required(self.service_code, 'service_code')
        self.validate_required(self.text, 'text')
        self.validate_required(self.app_key, 'app_key')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('ServiceCode') is not None:
            self.service_code = map.get('ServiceCode')
        if map.get('Text') is not None:
            self.text = map.get('Text')
        if map.get('DefaultProvince') is not None:
            self.default_province = map.get('DefaultProvince')
        if map.get('DefaultCity') is not None:
            self.default_city = map.get('DefaultCity')
        if map.get('DefaultDistrict') is not None:
            self.default_district = map.get('DefaultDistrict')
        if map.get('AppKey') is not None:
            self.app_key = map.get('AppKey')
        return self


class ClassifyPOIResponse(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data                # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.data, 'data')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('Data') is not None:
            self.data = map.get('Data')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class StructureAddressRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text                # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key          # type: str

    def validate(self):
        self.validate_required(self.service_code, 'service_code')
        self.validate_required(self.text, 'text')
        self.validate_required(self.app_key, 'app_key')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('ServiceCode') is not None:
            self.service_code = map.get('ServiceCode')
        if map.get('Text') is not None:
            self.text = map.get('Text')
        if map.get('DefaultProvince') is not None:
            self.default_province = map.get('DefaultProvince')
        if map.get('DefaultCity') is not None:
            self.default_city = map.get('DefaultCity')
        if map.get('DefaultDistrict') is not None:
            self.default_district = map.get('DefaultDistrict')
        if map.get('AppKey') is not None:
            self.app_key = map.get('AppKey')
        return self


class StructureAddressResponse(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data                # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.data, 'data')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('Data') is not None:
            self.data = map.get('Data')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class ExtractAddressRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text                # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key          # type: str

    def validate(self):
        self.validate_required(self.service_code, 'service_code')
        self.validate_required(self.text, 'text')
        self.validate_required(self.app_key, 'app_key')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('ServiceCode') is not None:
            self.service_code = map.get('ServiceCode')
        if map.get('Text') is not None:
            self.text = map.get('Text')
        if map.get('DefaultProvince') is not None:
            self.default_province = map.get('DefaultProvince')
        if map.get('DefaultCity') is not None:
            self.default_city = map.get('DefaultCity')
        if map.get('DefaultDistrict') is not None:
            self.default_district = map.get('DefaultDistrict')
        if map.get('AppKey') is not None:
            self.app_key = map.get('AppKey')
        return self


class ExtractAddressResponse(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data                # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.data, 'data')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('Data') is not None:
            self.data = map.get('Data')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class UpdateProjectRequest(TeaModel):
    def __init__(self, service_code=None, parameters=None):
        self.service_code = service_code  # type: str
        self.parameters = parameters    # type: Dict[str, Any]

    def validate(self):
        self.validate_required(self.service_code, 'service_code')
        self.validate_required(self.parameters, 'parameters')

    def to_map(self):
        result = {}
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, map={}):
        if map.get('ServiceCode') is not None:
            self.service_code = map.get('ServiceCode')
        if map.get('Parameters') is not None:
            self.parameters = map.get('Parameters')
        return self


class UpdateProjectShrinkRequest(TeaModel):
    def __init__(self, service_code=None, parameters_shrink=None):
        self.service_code = service_code  # type: str
        self.parameters_shrink = parameters_shrink  # type: str

    def validate(self):
        self.validate_required(self.service_code, 'service_code')
        self.validate_required(self.parameters_shrink, 'parameters_shrink')

    def to_map(self):
        result = {}
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        return result

    def from_map(self, map={}):
        if map.get('ServiceCode') is not None:
            self.service_code = map.get('ServiceCode')
        if map.get('Parameters') is not None:
            self.parameters_shrink = map.get('Parameters')
        return self


class UpdateProjectResponse(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data                # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.data, 'data')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('Data') is not None:
            self.data = map.get('Data')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class CorrectAddressRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text                # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key          # type: str

    def validate(self):
        self.validate_required(self.service_code, 'service_code')
        self.validate_required(self.text, 'text')
        self.validate_required(self.app_key, 'app_key')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('ServiceCode') is not None:
            self.service_code = map.get('ServiceCode')
        if map.get('Text') is not None:
            self.text = map.get('Text')
        if map.get('DefaultProvince') is not None:
            self.default_province = map.get('DefaultProvince')
        if map.get('DefaultCity') is not None:
            self.default_city = map.get('DefaultCity')
        if map.get('DefaultDistrict') is not None:
            self.default_district = map.get('DefaultDistrict')
        if map.get('AppKey') is not None:
            self.app_key = map.get('AppKey')
        return self


class CorrectAddressResponse(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data                # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.data, 'data')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('Data') is not None:
            self.data = map.get('Data')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self


class GetAddressSimilarityRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text                # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key          # type: str

    def validate(self):
        self.validate_required(self.service_code, 'service_code')
        self.validate_required(self.text, 'text')
        self.validate_required(self.app_key, 'app_key')

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('ServiceCode') is not None:
            self.service_code = map.get('ServiceCode')
        if map.get('Text') is not None:
            self.text = map.get('Text')
        if map.get('DefaultProvince') is not None:
            self.default_province = map.get('DefaultProvince')
        if map.get('DefaultCity') is not None:
            self.default_city = map.get('DefaultCity')
        if map.get('DefaultDistrict') is not None:
            self.default_district = map.get('DefaultDistrict')
        if map.get('AppKey') is not None:
            self.app_key = map.get('AppKey')
        return self


class GetAddressSimilarityResponse(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data                # type: str
        self.request_id = request_id    # type: str

    def validate(self):
        self.validate_required(self.data, 'data')
        self.validate_required(self.request_id, 'request_id')

    def to_map(self):
        result = {}
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('Data') is not None:
            self.data = map.get('Data')
        if map.get('RequestId') is not None:
            self.request_id = map.get('RequestId')
        return self
