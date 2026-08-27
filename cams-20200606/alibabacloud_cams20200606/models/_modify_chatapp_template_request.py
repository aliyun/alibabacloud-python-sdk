# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class ModifyChatappTemplateRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        category_change_paused: bool = None,
        components: List[main_models.ModifyChatappTemplateRequestComponents] = None,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        example: Dict[str, str] = None,
        isv_code: str = None,
        language: str = None,
        message_send_ttl_seconds: int = None,
        product_set_id: str = None,
        template_code: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # The templatetype cannot be modified.
        self.category = category
        # When a Utility template is changed to Marketing type, the template is paused for sending.
        self.category_change_paused = category_change_paused
        # The list of message template components.
        # 
        # > When Category is AUTHENTICATION, Components cannot contain a node with Type set to HEADER. When Type is BODY/FOOTER, the Text content is empty and is automatically generated.
        # 
        # This parameter is required.
        self.components = components
        # The SpaceId of the ISV sub-customer or the instance ID of the direct customer.
        self.cust_space_id = cust_space_id
        # The ISV customer WabaId.
        # 
        # > This parameter is deprecated. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id
        # The example for creating a template.
        self.example = example
        # The ISV verification code used to verify whether the sub-account is authorized by the ISV.
        self.isv_code = isv_code
        # The template language. For language codes, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        # 
        # This parameter is required.
        self.language = language
        # The validity period for sending template messages in WhatsApp.
        # - AUTHENTICATION: valid values range from 30 to 900. 
        # - UTILITY: valid values range from 30 to 43200.
        self.message_send_ttl_seconds = message_send_ttl_seconds
        # productSetId
        self.product_set_id = product_set_id
        # The message template code.
        self.template_code = template_code
        # The template name.
        self.template_name = template_name
        # The templatetype.
        # 
        # - **WHATSAPP**
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
        if self.category is not None:
            result['Category'] = self.category

        if self.category_change_paused is not None:
            result['CategoryChangePaused'] = self.category_change_paused

        result['Components'] = []
        if self.components is not None:
            for k1 in self.components:
                result['Components'].append(k1.to_map() if k1 else None)

        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id

        if self.example is not None:
            result['Example'] = self.example

        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code

        if self.language is not None:
            result['Language'] = self.language

        if self.message_send_ttl_seconds is not None:
            result['MessageSendTtlSeconds'] = self.message_send_ttl_seconds

        if self.product_set_id is not None:
            result['ProductSetId'] = self.product_set_id

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CategoryChangePaused') is not None:
            self.category_change_paused = m.get('CategoryChangePaused')

        self.components = []
        if m.get('Components') is not None:
            for k1 in m.get('Components'):
                temp_model = main_models.ModifyChatappTemplateRequestComponents()
                self.components.append(temp_model.from_map(k1))

        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')

        if m.get('Example') is not None:
            self.example = m.get('Example')

        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('MessageSendTtlSeconds') is not None:
            self.message_send_ttl_seconds = m.get('MessageSendTtlSeconds')

        if m.get('ProductSetId') is not None:
            self.product_set_id = m.get('ProductSetId')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

class ModifyChatappTemplateRequestComponents(DaraModel):
    def __init__(
        self,
        add_secret_recommendation: bool = None,
        buttons: List[main_models.ModifyChatappTemplateRequestComponentsButtons] = None,
        caption: str = None,
        cards: List[main_models.ModifyChatappTemplateRequestComponentsCards] = None,
        code_expiration_minutes: int = None,
        duration: int = None,
        file_name: str = None,
        file_type: str = None,
        format: str = None,
        has_expiration: bool = None,
        text: str = None,
        thumb_url: str = None,
        type: str = None,
        url: str = None,
    ):
        # Valid for WhatsApp templates when Category is AUTHENTICATION and Component Type is Body. Displays a prompt above the Body advising not to share the verification code with others.
        self.add_secret_recommendation = add_secret_recommendation
        # The list of buttons. Applicable only to **BUTTONS** components.
        # 
        # > WhatsApp button quantity rules:
        # > - When Category is MARKETING/UTILITY, a maximum of 10 buttons are allowed.
        # > - Only 1 PHONE_NUMBER button is allowed.
        # > - A maximum of 2 URL buttons are allowed.
        # > - QUICK_REPLY buttons cannot appear out of order with PHONE_NUMBER/URL buttons.
        self.buttons = buttons
        # The description.
        # > A description can be added when Type is **HEADER** and Format is **IMAGE/DOCUMENT/VIDEO**.
        self.caption = caption
        # The list of Carousel template cards.
        self.cards = cards
        # The validity period (in minutes) of the verification code for WhatsApp AUTHENTICATION templates. Valid only for WhatsApp messages when Category is AUTHENTICATION and Component Type is Footer. This information is displayed in the Footer position.
        self.code_expiration_minutes = code_expiration_minutes
        # Invalid field.
        self.duration = duration
        # The file name.
        # > Specifies the file name when Type is **HEADER** and Format is **DOCUMENT**.
        self.file_name = file_name
        # Invalid field.
        self.file_type = file_type
        # The media resource type.
        # 
        # - **TEXT**: text 
        # 
        # - **IMAGE**: image 
        # 
        # - **DOCUMENT**: document 
        # 
        # - **VIDEO**: video
        self.format = format
        # Specifies whether the coupon code has an expiration time. This parameter is used when type is LIMITED_TIME_OFFER.
        self.has_expiration = has_expiration
        # The text of the message to be sent.
        # 
        # > When Category is AUTHENTICATION, this property value is empty.
        self.text = text
        # Invalid field.
        self.thumb_url = thumb_url
        # The component type.
        # 
        # - **BODY**
        # 
        # - **HEADER**
        # 
        # - **FOOTER**
        # 
        #  - **BUTTONS**
        # 
        # - **CAROUSEL**
        # 
        # - **LIMITED_TIME_OFFER**
        # 
        # > - For WhatsApp templates, the **BODY** component cannot exceed 1024 characters. The **HEADER** and **FOOTER** components cannot exceed 60 characters.
        # 
        # This parameter is required.
        self.type = type
        # The media resource path.
        self.url = url

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

        if self.has_expiration is not None:
            result['HasExpiration'] = self.has_expiration

        if self.text is not None:
            result['Text'] = self.text

        if self.thumb_url is not None:
            result['ThumbUrl'] = self.thumb_url

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddSecretRecommendation') is not None:
            self.add_secret_recommendation = m.get('AddSecretRecommendation')

        self.buttons = []
        if m.get('Buttons') is not None:
            for k1 in m.get('Buttons'):
                temp_model = main_models.ModifyChatappTemplateRequestComponentsButtons()
                self.buttons.append(temp_model.from_map(k1))

        if m.get('Caption') is not None:
            self.caption = m.get('Caption')

        self.cards = []
        if m.get('Cards') is not None:
            for k1 in m.get('Cards'):
                temp_model = main_models.ModifyChatappTemplateRequestComponentsCards()
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

        if m.get('HasExpiration') is not None:
            self.has_expiration = m.get('HasExpiration')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('ThumbUrl') is not None:
            self.thumb_url = m.get('ThumbUrl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class ModifyChatappTemplateRequestComponentsCards(DaraModel):
    def __init__(
        self,
        card_components: List[main_models.ModifyChatappTemplateRequestComponentsCardsCardComponents] = None,
    ):
        # The list of controls in a Carousel card.
        # 
        # This parameter is required.
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
                temp_model = main_models.ModifyChatappTemplateRequestComponentsCardsCardComponents()
                self.card_components.append(temp_model.from_map(k1))

        return self

class ModifyChatappTemplateRequestComponentsCardsCardComponents(DaraModel):
    def __init__(
        self,
        buttons: List[main_models.ModifyChatappTemplateRequestComponentsCardsCardComponentsButtons] = None,
        format: str = None,
        text: str = None,
        type: str = None,
        url: str = None,
    ):
        # The list of buttons. Applicable only to BUTTONS components. Each Carousel card can have a maximum of two buttons.
        self.buttons = buttons
        # The media resource type. Valid when Type is HEADER.
        # 
        # - **IMAGE**: image 
        # 
        # - **VIDEO**: video
        self.format = format
        # The BODY content in a Carousel card.
        self.text = text
        # The component type. Valid values:
        # 
        # - **BODY**
        # 
        # - **HEADER**
        # 
        # - **BUTTONS**
        # 
        # This parameter is required.
        self.type = type
        # The media resource path.
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
                temp_model = main_models.ModifyChatappTemplateRequestComponentsCardsCardComponentsButtons()
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

class ModifyChatappTemplateRequestComponentsCardsCardComponentsButtons(DaraModel):
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
        # The button text.
        self.text = text
        # The button type.
        # 
        # - **PHONE_NUMBER**: phone call button
        # 
        # - **URL**: web button
        # 
        # - **QUICK_REPLY**: quick reply button
        # 
        # This parameter is required.
        self.type = type
        # The URL to visit when the button is clicked.
        self.url = url
        # The URL type.
        # 
        # - **static**: static
        # 
        # - **dynamic**: dynamic
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

class ModifyChatappTemplateRequestComponentsButtons(DaraModel):
    def __init__(
        self,
        autofill_text: str = None,
        coupon_code: str = None,
        flow_action: str = None,
        flow_id: str = None,
        is_opt_out: bool = None,
        navigate_screen: str = None,
        package_name: str = None,
        phone_number: str = None,
        signature_hash: str = None,
        supported_apps: List[main_models.ModifyChatappTemplateRequestComponentsButtonsSupportedApps] = None,
        text: str = None,
        type: str = None,
        url: str = None,
        url_type: str = None,
    ):
        # Required for WhatsApp templates when Category is AUTHENTICATION and Button Type is ONE_TAP/ZERO_TAP. The button text for the WhatsApp Autofill operation.
        self.autofill_text = autofill_text
        # The coupon code value. Only letters and numbers are supported. You can pass in a variable such as $(couponCode) and provide the actual coupon code when sending the message.
        self.coupon_code = coupon_code
        # The Flow data event type. Valid values:
        # 
        # - DATA_EXCHANGE: data exchange.
        # 
        # - NAVIGATE: navigation.
        self.flow_action = flow_action
        # Flow ID。
        self.flow_id = flow_id
        # Valid for WhatsApp templates when Category is Marketing and Button type is QUICK_REPLY. Indicates the button is a marketing opt-out button. If the customer clicks this button and send control is configured on ChatApp, subsequent Marketing messages will not be sent to the customer.
        self.is_opt_out = is_opt_out
        # The navigate screen. Required when FlowAction is NAVIGATE.
        self.navigate_screen = navigate_screen
        # Use the properties under SupportedApps instead.
        self.package_name = package_name
        # The phone number.
        self.phone_number = phone_number
        # Use the properties under SupportedApps instead.
        self.signature_hash = signature_hash
        # The list of supported applications.
        self.supported_apps = supported_apps
        # The button text.
        self.text = text
        # The button type.
        # 
        # - **PHONE_NUMBER**: phone call button
        # 
        # - **URL**: web button
        # 
        # - **QUICK_REPLY**: quick reply button
        # 
        # - **COPY_CODE**: copy verification code or coupon code
        # 
        # - **ONE_TAP**: autofill button for AUTHENTICATION templates
        # 
        # - **ZERO_TAP**: autofill button for AUTHENTICATION templates
        # 
        # - **MPM**: multi-product catalog
        # 
        # - **CATALOG**: catalog
        # 
        # - **FLOW**: open WhatsApp flow
        # 
        # > - For WhatsApp templates with Category set to AUTHENTICATION, only one button is allowed, and the type can only be COPY_CODE or ONE_TAP. When the type is COPY_CODE, Text is required. When the type is ONE_TAP, Text (displayed when the target application is not installed on the device, representing the copy verification code button name), SignatureHash, PackageName, and AutofillText are required.
        # 
        # This parameter is required.
        self.type = type
        # The URL to visit when the button is clicked.
        self.url = url
        # The URL type.
        # 
        # - **static**: static
        # 
        # - **dynamic**: dynamic
        self.url_type = url_type

    def validate(self):
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
                temp_model = main_models.ModifyChatappTemplateRequestComponentsButtonsSupportedApps()
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

class ModifyChatappTemplateRequestComponentsButtonsSupportedApps(DaraModel):
    def __init__(
        self,
        package_name: str = None,
        signature_hash: str = None,
    ):
        # Required for WhatsApp templates when Category is AUTHENTICATION and Button Type is ONE_TAP/ZERO_TAP. The package name of the application invoked by WhatsApp.
        self.package_name = package_name
        # Required for WhatsApp templates when Category is AUTHENTICATION and Button Type is ONE_TAP/ZERO_TAP. The signature hash value of the application invoked by WhatsApp.
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

