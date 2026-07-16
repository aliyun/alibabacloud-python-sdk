# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class GetRCSSignatureResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.GetRCSSignatureResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetRCSSignatureResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetRCSSignatureResponseBodyData(DaraModel):
    def __init__(
        self,
        background_image: str = None,
        bubble_color: str = None,
        category: int = None,
        chatbot_code: str = None,
        chatbot_name: str = None,
        description: str = None,
        latitude: str = None,
        logo: str = None,
        longitude: str = None,
        office_address: str = None,
        register_result_list: List[main_models.GetRCSSignatureResponseBodyDataRegisterResultList] = None,
        service_email: str = None,
        service_phone: str = None,
        service_terms: str = None,
        service_website: str = None,
        shelf_result_list: List[main_models.GetRCSSignatureResponseBodyDataShelfResultList] = None,
        sign_id: int = None,
        sign_name: str = None,
    ):
        self.background_image = background_image
        self.bubble_color = bubble_color
        self.category = category
        self.chatbot_code = chatbot_code
        self.chatbot_name = chatbot_name
        self.description = description
        self.latitude = latitude
        self.logo = logo
        self.longitude = longitude
        self.office_address = office_address
        self.register_result_list = register_result_list
        self.service_email = service_email
        self.service_phone = service_phone
        self.service_terms = service_terms
        self.service_website = service_website
        self.shelf_result_list = shelf_result_list
        self.sign_id = sign_id
        self.sign_name = sign_name

    def validate(self):
        if self.register_result_list:
            for v1 in self.register_result_list:
                 if v1:
                    v1.validate()
        if self.shelf_result_list:
            for v1 in self.shelf_result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.background_image is not None:
            result['BackgroundImage'] = self.background_image

        if self.bubble_color is not None:
            result['BubbleColor'] = self.bubble_color

        if self.category is not None:
            result['Category'] = self.category

        if self.chatbot_code is not None:
            result['ChatbotCode'] = self.chatbot_code

        if self.chatbot_name is not None:
            result['ChatbotName'] = self.chatbot_name

        if self.description is not None:
            result['Description'] = self.description

        if self.latitude is not None:
            result['Latitude'] = self.latitude

        if self.logo is not None:
            result['Logo'] = self.logo

        if self.longitude is not None:
            result['Longitude'] = self.longitude

        if self.office_address is not None:
            result['OfficeAddress'] = self.office_address

        result['RegisterResultList'] = []
        if self.register_result_list is not None:
            for k1 in self.register_result_list:
                result['RegisterResultList'].append(k1.to_map() if k1 else None)

        if self.service_email is not None:
            result['ServiceEmail'] = self.service_email

        if self.service_phone is not None:
            result['ServicePhone'] = self.service_phone

        if self.service_terms is not None:
            result['ServiceTerms'] = self.service_terms

        if self.service_website is not None:
            result['ServiceWebsite'] = self.service_website

        result['ShelfResultList'] = []
        if self.shelf_result_list is not None:
            for k1 in self.shelf_result_list:
                result['ShelfResultList'].append(k1.to_map() if k1 else None)

        if self.sign_id is not None:
            result['SignId'] = self.sign_id

        if self.sign_name is not None:
            result['SignName'] = self.sign_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackgroundImage') is not None:
            self.background_image = m.get('BackgroundImage')

        if m.get('BubbleColor') is not None:
            self.bubble_color = m.get('BubbleColor')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ChatbotCode') is not None:
            self.chatbot_code = m.get('ChatbotCode')

        if m.get('ChatbotName') is not None:
            self.chatbot_name = m.get('ChatbotName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')

        if m.get('Logo') is not None:
            self.logo = m.get('Logo')

        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')

        if m.get('OfficeAddress') is not None:
            self.office_address = m.get('OfficeAddress')

        self.register_result_list = []
        if m.get('RegisterResultList') is not None:
            for k1 in m.get('RegisterResultList'):
                temp_model = main_models.GetRCSSignatureResponseBodyDataRegisterResultList()
                self.register_result_list.append(temp_model.from_map(k1))

        if m.get('ServiceEmail') is not None:
            self.service_email = m.get('ServiceEmail')

        if m.get('ServicePhone') is not None:
            self.service_phone = m.get('ServicePhone')

        if m.get('ServiceTerms') is not None:
            self.service_terms = m.get('ServiceTerms')

        if m.get('ServiceWebsite') is not None:
            self.service_website = m.get('ServiceWebsite')

        self.shelf_result_list = []
        if m.get('ShelfResultList') is not None:
            for k1 in m.get('ShelfResultList'):
                temp_model = main_models.GetRCSSignatureResponseBodyDataShelfResultList()
                self.shelf_result_list.append(temp_model.from_map(k1))

        if m.get('SignId') is not None:
            self.sign_id = m.get('SignId')

        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')

        return self

class GetRCSSignatureResponseBodyDataShelfResultList(DaraModel):
    def __init__(
        self,
        operator_code: str = None,
        product_type: int = None,
        shelf_status: int = None,
        shelf_status_reasons: List[main_models.GetRCSSignatureResponseBodyDataShelfResultListShelfStatusReasons] = None,
    ):
        self.operator_code = operator_code
        self.product_type = product_type
        self.shelf_status = shelf_status
        self.shelf_status_reasons = shelf_status_reasons

    def validate(self):
        if self.shelf_status_reasons:
            for v1 in self.shelf_status_reasons:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operator_code is not None:
            result['OperatorCode'] = self.operator_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.shelf_status is not None:
            result['ShelfStatus'] = self.shelf_status

        result['ShelfStatusReasons'] = []
        if self.shelf_status_reasons is not None:
            for k1 in self.shelf_status_reasons:
                result['ShelfStatusReasons'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperatorCode') is not None:
            self.operator_code = m.get('OperatorCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ShelfStatus') is not None:
            self.shelf_status = m.get('ShelfStatus')

        self.shelf_status_reasons = []
        if m.get('ShelfStatusReasons') is not None:
            for k1 in m.get('ShelfStatusReasons'):
                temp_model = main_models.GetRCSSignatureResponseBodyDataShelfResultListShelfStatusReasons()
                self.shelf_status_reasons.append(temp_model.from_map(k1))

        return self

class GetRCSSignatureResponseBodyDataShelfResultListShelfStatusReasons(DaraModel):
    def __init__(
        self,
        reason_code: str = None,
        reason_desc_list: List[str] = None,
    ):
        self.reason_code = reason_code
        self.reason_desc_list = reason_desc_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        if self.reason_desc_list is not None:
            result['ReasonDescList'] = self.reason_desc_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        if m.get('ReasonDescList') is not None:
            self.reason_desc_list = m.get('ReasonDescList')

        return self

class GetRCSSignatureResponseBodyDataRegisterResultList(DaraModel):
    def __init__(
        self,
        operator_code: str = None,
        product_type: int = None,
        register_complete_time: str = None,
        register_status: int = None,
        register_status_reasons: List[main_models.GetRCSSignatureResponseBodyDataRegisterResultListRegisterStatusReasons] = None,
    ):
        self.operator_code = operator_code
        self.product_type = product_type
        self.register_complete_time = register_complete_time
        self.register_status = register_status
        self.register_status_reasons = register_status_reasons

    def validate(self):
        if self.register_status_reasons:
            for v1 in self.register_status_reasons:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operator_code is not None:
            result['OperatorCode'] = self.operator_code

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.register_complete_time is not None:
            result['RegisterCompleteTime'] = self.register_complete_time

        if self.register_status is not None:
            result['RegisterStatus'] = self.register_status

        result['RegisterStatusReasons'] = []
        if self.register_status_reasons is not None:
            for k1 in self.register_status_reasons:
                result['RegisterStatusReasons'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperatorCode') is not None:
            self.operator_code = m.get('OperatorCode')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RegisterCompleteTime') is not None:
            self.register_complete_time = m.get('RegisterCompleteTime')

        if m.get('RegisterStatus') is not None:
            self.register_status = m.get('RegisterStatus')

        self.register_status_reasons = []
        if m.get('RegisterStatusReasons') is not None:
            for k1 in m.get('RegisterStatusReasons'):
                temp_model = main_models.GetRCSSignatureResponseBodyDataRegisterResultListRegisterStatusReasons()
                self.register_status_reasons.append(temp_model.from_map(k1))

        return self

class GetRCSSignatureResponseBodyDataRegisterResultListRegisterStatusReasons(DaraModel):
    def __init__(
        self,
        reason_code: str = None,
        reason_desc_list: List[str] = None,
    ):
        self.reason_code = reason_code
        self.reason_desc_list = reason_desc_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        if self.reason_desc_list is not None:
            result['ReasonDescList'] = self.reason_desc_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        if m.get('ReasonDescList') is not None:
            self.reason_desc_list = m.get('ReasonDescList')

        return self

