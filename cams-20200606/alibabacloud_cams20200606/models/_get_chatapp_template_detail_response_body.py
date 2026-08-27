# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class GetChatappTemplateDetailResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.GetChatappTemplateDetailResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The access denied detail information.
        self.access_denied_detail = access_denied_detail
        # The request status code.
        # 
        # - OK indicates that the request was successful.
        # 
        # - For other error codes, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
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
            temp_model = main_models.GetChatappTemplateDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetChatappTemplateDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        allow_send: bool = None,
        audit_status: str = None,
        category: str = None,
        category_change_paused: bool = None,
        components: List[main_models.GetChatappTemplateDetailResponseBodyDataComponents] = None,
        example: Dict[str, str] = None,
        language: str = None,
        message_send_ttl_seconds: int = None,
        name: str = None,
        product_set_id: str = None,
        quality_score: str = None,
        reason: str = None,
        template_code: str = None,
        template_type: str = None,
    ):
        # Indicates whether the current template can be used for sending. This parameter is valid only for Marketing templates.
        self.allow_send = allow_send
        # The audit status. Valid values:
        # 
        # - **pass**: Approved.
        # 
        # - **fail**: Rejected.
        # 
        # - **auditing**: Under review.
        # 
        # - **unaudit**: Review suspended.
        self.audit_status = audit_status
        # The WhatsApp template category. Valid values:
        # 
        # - **UTILITY**: transaction-related.
        # 
        # - **MARKETING**: marketing template.
        # 
        # - **AUTHENTICATION**: identity verification.
        # 
        # Viber template category. Valid values:
        # 
        # - **UTILITY**: transaction-related.
        # 
        # - **MARKETING**: marketing template.
        # 
        # - **AUTHENTICATION**: identity verification.
        self.category = category
        # Indicates whether template sending is paused when a Utility template is changed to a Marketing template.
        self.category_change_paused = category_change_paused
        # The list of message template components.
        self.components = components
        # The variable example.
        self.example = example
        # The language of the template. For detailed language codes, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        self.language = language
        # The message time-to-live when sending WhatsApp Authentication template messages.
        self.message_send_ttl_seconds = message_send_ttl_seconds
        # The name of the template.
        self.name = name
        # productSetId
        self.product_set_id = product_set_id
        # The template quality.
        # - RED: Low quality.
        # - YELLOW: Medium quality.
        # - UNKNOWN: Quality unknown.
        # - GREEN: High quality.
        self.quality_score = quality_score
        # The reason for template review rejection.
        self.reason = reason
        # The code of the template.
        self.template_code = template_code
        # The templatetype.
        # 
        # - **WHATSAPP**
        # 
        # - **VIBER**
        self.template_type = template_type

    def validate(self):
        if self.components:
            for v1 in self.components:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_send is not None:
            result['AllowSend'] = self.allow_send

        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status

        if self.category is not None:
            result['Category'] = self.category

        if self.category_change_paused is not None:
            result['CategoryChangePaused'] = self.category_change_paused

        result['Components'] = []
        if self.components is not None:
            for k1 in self.components:
                result['Components'].append(k1.to_map() if k1 else None)

        if self.example is not None:
            result['Example'] = self.example

        if self.language is not None:
            result['Language'] = self.language

        if self.message_send_ttl_seconds is not None:
            result['MessageSendTtlSeconds'] = self.message_send_ttl_seconds

        if self.name is not None:
            result['Name'] = self.name

        if self.product_set_id is not None:
            result['ProductSetId'] = self.product_set_id

        if self.quality_score is not None:
            result['QualityScore'] = self.quality_score

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowSend') is not None:
            self.allow_send = m.get('AllowSend')

        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CategoryChangePaused') is not None:
            self.category_change_paused = m.get('CategoryChangePaused')

        self.components = []
        if m.get('Components') is not None:
            for k1 in m.get('Components'):
                temp_model = main_models.GetChatappTemplateDetailResponseBodyDataComponents()
                self.components.append(temp_model.from_map(k1))

        if m.get('Example') is not None:
            self.example = m.get('Example')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('MessageSendTtlSeconds') is not None:
            self.message_send_ttl_seconds = m.get('MessageSendTtlSeconds')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProductSetId') is not None:
            self.product_set_id = m.get('ProductSetId')

        if m.get('QualityScore') is not None:
            self.quality_score = m.get('QualityScore')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

class GetChatappTemplateDetailResponseBodyDataComponents(DaraModel):
    def __init__(
        self,
        add_secret_recommendation: bool = None,
        buttons: List[main_models.GetChatappTemplateDetailResponseBodyDataComponentsButtons] = None,
        caption: str = None,
        cards: List[main_models.GetChatappTemplateDetailResponseBodyDataComponentsCards] = None,
        code_expiration_minutes: int = None,
        duration: int = None,
        file_name: str = None,
        file_type: str = None,
        format: str = None,
        latitude: str = None,
        location_address: str = None,
        location_name: str = None,
        longitude: str = None,
        offer_expiration_time_ms: str = None,
        text: str = None,
        thumb_url: str = None,
        type: str = None,
        url: str = None,
        has_expiration: bool = None,
    ):
        # Valid for WhatsApp templates when Category is Authentication and Component Type is Body. Indicates whether a security recommendation message that advises users not to share the verification code is displayed above the Body.
        self.add_secret_recommendation = add_secret_recommendation
        # The button list. Applicable only to the **BUTTONS** component.
        # 
        # > WhatsApp button quantity rules:
        # > - For WhatsApp templates with Category set to MARKETING or UTILITY, a maximum of 10 buttons are allowed.
        # > - Only 1 PHONE_NUMBER button is allowed.
        # > - A maximum of 2 URL buttons are allowed.
        # > - QUICK_REPLY buttons cannot be mixed in random order with PHONE_NUMBER or URL buttons.
        self.buttons = buttons
        # The file description.
        self.caption = caption
        # The list of carousel cards.
        self.cards = cards
        # The verification code validity period in minutes for WhatsApp Authentication templates. Valid only when the message type is WhatsApp, Category is Authentication, and Component Type is Footer. This information is displayed in the Footer position.
        self.code_expiration_minutes = code_expiration_minutes
        # The video duration of a Viber video message. Valid values: 0 to 600.
        self.duration = duration
        # The file name.
        self.file_name = file_name
        # The file type of a Viber file message.
        self.file_type = file_type
        # The format.
        self.format = format
        # The latitude of the location.
        self.latitude = latitude
        # The location address.
        self.location_address = location_address
        # The location name.
        self.location_name = location_name
        # The longitude of the location.
        self.longitude = longitude
        # The offer code expiration variable in a Limited Time Offer (LTO) template.
        self.offer_expiration_time_ms = offer_expiration_time_ms
        # The text of the message to be sent.
        self.text = text
        # The thumbnail for a Viber video message.
        self.thumb_url = thumb_url
        # The component type.
        # 
        # - **BODY**
        # 
        # - **HEADER**
        # 
        # - **FOOTER**
        # 
        # - **BUTTONS**
        # 
        # - **CAROUSEL**
        # 
        # - **LIMITED_TIME_OFFER**
        # 
        # > - For WhatsApp templates, the **BODY** component cannot exceed 1024 characters. The **HEADER** and **FOOTER** components cannot exceed 60 characters.
        # > - For Viber templates, the **FOOTER**, **CAROUSEL**, and **LIMITED_TIME_OFFER** types are invalid.
        # > - For Viber templates, images, videos, and files are placed in the **HEADER** (the device displays images below the text).
        self.type = type
        # The material URL.
        self.url = url
        # Specifies whether the offer code has an expiration time in a Limited Time Offer (LTO) template.
        self.has_expiration = has_expiration

    def validate(self):
        if self.buttons:
            for v1 in self.buttons:
                 if v1:
                    v1.validate()
        if self.cards:
            for v1 in self.cards:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_secret_recommendation is not None:
            result['AddSecretRecommendation'] = self.add_secret_recommendation

        result['Buttons'] = []
        if self.buttons is not None:
            for k1 in self.buttons:
                result['Buttons'].append(k1.to_map() if k1 else None)

        if self.caption is not None:
            result['Caption'] = self.caption

        result['Cards'] = []
        if self.cards is not None:
            for k1 in self.cards:
                result['Cards'].append(k1.to_map() if k1 else None)

        if self.code_expiration_minutes is not None:
            result['CodeExpirationMinutes'] = self.code_expiration_minutes

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.format is not None:
            result['Format'] = self.format

        if self.latitude is not None:
            result['Latitude'] = self.latitude

        if self.location_address is not None:
            result['LocationAddress'] = self.location_address

        if self.location_name is not None:
            result['LocationName'] = self.location_name

        if self.longitude is not None:
            result['Longitude'] = self.longitude

        if self.offer_expiration_time_ms is not None:
            result['OfferExpirationTimeMs'] = self.offer_expiration_time_ms

        if self.text is not None:
            result['Text'] = self.text

        if self.thumb_url is not None:
            result['ThumbUrl'] = self.thumb_url

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        if self.has_expiration is not None:
            result['hasExpiration'] = self.has_expiration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddSecretRecommendation') is not None:
            self.add_secret_recommendation = m.get('AddSecretRecommendation')

        self.buttons = []
        if m.get('Buttons') is not None:
            for k1 in m.get('Buttons'):
                temp_model = main_models.GetChatappTemplateDetailResponseBodyDataComponentsButtons()
                self.buttons.append(temp_model.from_map(k1))

        if m.get('Caption') is not None:
            self.caption = m.get('Caption')

        self.cards = []
        if m.get('Cards') is not None:
            for k1 in m.get('Cards'):
                temp_model = main_models.GetChatappTemplateDetailResponseBodyDataComponentsCards()
                self.cards.append(temp_model.from_map(k1))

        if m.get('CodeExpirationMinutes') is not None:
            self.code_expiration_minutes = m.get('CodeExpirationMinutes')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')

        if m.get('LocationAddress') is not None:
            self.location_address = m.get('LocationAddress')

        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')

        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')

        if m.get('OfferExpirationTimeMs') is not None:
            self.offer_expiration_time_ms = m.get('OfferExpirationTimeMs')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('ThumbUrl') is not None:
            self.thumb_url = m.get('ThumbUrl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('hasExpiration') is not None:
            self.has_expiration = m.get('hasExpiration')

        return self

class GetChatappTemplateDetailResponseBodyDataComponentsCards(DaraModel):
    def __init__(
        self,
        card_components: List[main_models.GetChatappTemplateDetailResponseBodyDataComponentsCardsCardComponents] = None,
    ):
        # The list of card components.
        self.card_components = card_components

    def validate(self):
        if self.card_components:
            for v1 in self.card_components:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CardComponents'] = []
        if self.card_components is not None:
            for k1 in self.card_components:
                result['CardComponents'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.card_components = []
        if m.get('CardComponents') is not None:
            for k1 in m.get('CardComponents'):
                temp_model = main_models.GetChatappTemplateDetailResponseBodyDataComponentsCardsCardComponents()
                self.card_components.append(temp_model.from_map(k1))

        return self

class GetChatappTemplateDetailResponseBodyDataComponentsCardsCardComponents(DaraModel):
    def __init__(
        self,
        buttons: List[main_models.GetChatappTemplateDetailResponseBodyDataComponentsCardsCardComponentsButtons] = None,
        format: str = None,
        text: str = None,
        type: str = None,
        url: str = None,
    ):
        # The list of card buttons.
        self.buttons = buttons
        # The header type in a carousel template. Only IMAGE and VIDEO are supported. All cards must have the same header type.
        self.format = format
        # The card text content.
        self.text = text
        # The component type.
        self.type = type
        # The web URL.
        self.url = url

    def validate(self):
        if self.buttons:
            for v1 in self.buttons:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Buttons'] = []
        if self.buttons is not None:
            for k1 in self.buttons:
                result['Buttons'].append(k1.to_map() if k1 else None)

        if self.format is not None:
            result['Format'] = self.format

        if self.text is not None:
            result['Text'] = self.text

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.buttons = []
        if m.get('Buttons') is not None:
            for k1 in m.get('Buttons'):
                temp_model = main_models.GetChatappTemplateDetailResponseBodyDataComponentsCardsCardComponentsButtons()
                self.buttons.append(temp_model.from_map(k1))

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class GetChatappTemplateDetailResponseBodyDataComponentsCardsCardComponentsButtons(DaraModel):
    def __init__(
        self,
        phone_number: str = None,
        text: str = None,
        type: str = None,
        url: str = None,
        url_type: str = None,
    ):
        # The phone number.
        self.phone_number = phone_number
        # The button content.
        self.text = text
        # The button type for a carousel template. Valid values: URL, PHONE_NUMBER, or QUICK_REPLY.
        self.type = type
        # The URL to visit when the button is clicked.
        self.url = url
        # The URL type. Valid values:
        #  
        # - static: static.
        # 
        # - dynamic: dynamic.
        self.url_type = url_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.text is not None:
            result['Text'] = self.text

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        if self.url_type is not None:
            result['UrlType'] = self.url_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('UrlType') is not None:
            self.url_type = m.get('UrlType')

        return self

class GetChatappTemplateDetailResponseBodyDataComponentsButtons(DaraModel):
    def __init__(
        self,
        autofill_text: str = None,
        coupon_code: str = None,
        extend_attrs: main_models.GetChatappTemplateDetailResponseBodyDataComponentsButtonsExtendAttrs = None,
        flow_action: str = None,
        flow_id: str = None,
        is_opt_out: bool = None,
        navigate_screen: str = None,
        package_name: str = None,
        phone_number: str = None,
        signature_hash: str = None,
        supported_apps: List[main_models.GetChatappTemplateDetailResponseBodyDataComponentsButtonsSupportedApps] = None,
        text: str = None,
        type: str = None,
        url: str = None,
        url_type: str = None,
    ):
        # Required for WhatsApp templates with Category set to Authentication and Button Type set to ONE_TAP. Specifies the button text for the WhatsApp Autofill operation.
        self.autofill_text = autofill_text
        # The coupon code.
        self.coupon_code = coupon_code
        # The extended fields.
        self.extend_attrs = extend_attrs
        # The Flow data event type. Valid values:
        # 
        # - NAVIGATE: navigation.
        # 
        # - DATA_EXCHANGE: data exchange.
        self.flow_action = flow_action
        # Flow ID
        self.flow_id = flow_id
        # Valid for WhatsApp templates with Category set to Marketing and Button Type set to QUICK_REPLY. Indicates that the button is a marketing opt-out button. If a customer clicks this button and the send control operation is configured on the Chat App Message Service platform, subsequent Marketing messages will not be sent to the customer.
        self.is_opt_out = is_opt_out
        # The navigate screen. Required when FlowAction is set to NAVIGATE.
        self.navigate_screen = navigate_screen
        # Required for WhatsApp templates with Category set to Authentication and Button Type set to ONE_TAP. Specifies the package name for WhatsApp to launch the application.
        self.package_name = package_name
        # The phone number. Valid only when the button type is **PHONE_NUMBER**.
        self.phone_number = phone_number
        # Required for WhatsApp templates with Category set to Authentication and Button Type set to ONE_TAP. Specifies the signature hash value for WhatsApp to launch the application.
        self.signature_hash = signature_hash
        # The applications supported by the ONE_TAP/ZERO_TAP verification code.
        self.supported_apps = supported_apps
        # The display name of the button.
        self.text = text
        # The button type.
        # 
        # - **PHONE_NUMBER**: phone call button.
        # 
        # - **URL**: web page button.
        # 
        # - **QUICK_REPLY**: quick reply button.
        # 
        # - **COPY_CODE**: copy verification code or coupon code.
        # 
        # - **ONE_TAP**: autofill button for AUTHENTICATION templates.
        # 
        # - **ZERO_TAP**: autofill button for AUTHENTICATION templates.
        # 
        # - **MPM**: multi-product catalog.
        # 
        # - **CATALOG**: catalog.
        # 
        # - **FLOW**: open WhatsApp flow.
        # 
        # > - For WhatsApp templates with Category set to AUTHENTICATION, only one button is allowed, and the type can only be COPY_CODE or ONE_TAP. If the type is COPY_CODE, Text is required. If the type is ONE_TAP, Text (displayed when the target application is not installed on the device, indicating the name of the copy verification code button), SignatureHash, PackageName, and AutofillText are required.
        # > - Viber templates allow only one button, and it must be of the URL type.
        self.type = type
        # The URL that is accessed when the link button is clicked.
        self.url = url
        # The URL type.
        # 
        # - **static**: static.
        # 
        # - **dynamic**: dynamic.
        self.url_type = url_type

    def validate(self):
        if self.extend_attrs:
            self.extend_attrs.validate()
        if self.supported_apps:
            for v1 in self.supported_apps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.autofill_text is not None:
            result['AutofillText'] = self.autofill_text

        if self.coupon_code is not None:
            result['CouponCode'] = self.coupon_code

        if self.extend_attrs is not None:
            result['ExtendAttrs'] = self.extend_attrs.to_map()

        if self.flow_action is not None:
            result['FlowAction'] = self.flow_action

        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.is_opt_out is not None:
            result['IsOptOut'] = self.is_opt_out

        if self.navigate_screen is not None:
            result['NavigateScreen'] = self.navigate_screen

        if self.package_name is not None:
            result['PackageName'] = self.package_name

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.signature_hash is not None:
            result['SignatureHash'] = self.signature_hash

        result['SupportedApps'] = []
        if self.supported_apps is not None:
            for k1 in self.supported_apps:
                result['SupportedApps'].append(k1.to_map() if k1 else None)

        if self.text is not None:
            result['Text'] = self.text

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        if self.url_type is not None:
            result['UrlType'] = self.url_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutofillText') is not None:
            self.autofill_text = m.get('AutofillText')

        if m.get('CouponCode') is not None:
            self.coupon_code = m.get('CouponCode')

        if m.get('ExtendAttrs') is not None:
            temp_model = main_models.GetChatappTemplateDetailResponseBodyDataComponentsButtonsExtendAttrs()
            self.extend_attrs = temp_model.from_map(m.get('ExtendAttrs'))

        if m.get('FlowAction') is not None:
            self.flow_action = m.get('FlowAction')

        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('IsOptOut') is not None:
            self.is_opt_out = m.get('IsOptOut')

        if m.get('NavigateScreen') is not None:
            self.navigate_screen = m.get('NavigateScreen')

        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('SignatureHash') is not None:
            self.signature_hash = m.get('SignatureHash')

        self.supported_apps = []
        if m.get('SupportedApps') is not None:
            for k1 in m.get('SupportedApps'):
                temp_model = main_models.GetChatappTemplateDetailResponseBodyDataComponentsButtonsSupportedApps()
                self.supported_apps.append(temp_model.from_map(k1))

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('UrlType') is not None:
            self.url_type = m.get('UrlType')

        return self

class GetChatappTemplateDetailResponseBodyDataComponentsButtonsSupportedApps(DaraModel):
    def __init__(
        self,
        package_name: str = None,
        signature_hash: str = None,
    ):
        # The package name.
        self.package_name = package_name
        # The package signature hash.
        self.signature_hash = signature_hash

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.package_name is not None:
            result['PackageName'] = self.package_name

        if self.signature_hash is not None:
            result['SignatureHash'] = self.signature_hash

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')

        if m.get('SignatureHash') is not None:
            self.signature_hash = m.get('SignatureHash')

        return self

class GetChatappTemplateDetailResponseBodyDataComponentsButtonsExtendAttrs(DaraModel):
    def __init__(
        self,
        action: str = None,
        intent_code: str = None,
        next_language_code: str = None,
        next_template_code: str = None,
        next_template_name: str = None,
    ):
        # The event type.
        self.action = action
        # The intent code.
        self.intent_code = intent_code
        # The next template language.
        self.next_language_code = next_language_code
        # The next template code.
        self.next_template_code = next_template_code
        # The next template name.
        self.next_template_name = next_template_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.intent_code is not None:
            result['IntentCode'] = self.intent_code

        if self.next_language_code is not None:
            result['NextLanguageCode'] = self.next_language_code

        if self.next_template_code is not None:
            result['NextTemplateCode'] = self.next_template_code

        if self.next_template_name is not None:
            result['NextTemplateName'] = self.next_template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('IntentCode') is not None:
            self.intent_code = m.get('IntentCode')

        if m.get('NextLanguageCode') is not None:
            self.next_language_code = m.get('NextLanguageCode')

        if m.get('NextTemplateCode') is not None:
            self.next_template_code = m.get('NextTemplateCode')

        if m.get('NextTemplateName') is not None:
            self.next_template_name = m.get('NextTemplateName')

        return self

