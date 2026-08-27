# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class CreateChatappTemplateRequest(DaraModel):
    def __init__(
        self,
        allow_category_change: bool = None,
        category: str = None,
        category_change_paused: bool = None,
        components: List[main_models.CreateChatappTemplateRequestComponents] = None,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        example: Dict[str, str] = None,
        isv_code: str = None,
        language: str = None,
        message_send_ttl_seconds: int = None,
        name: str = None,
        product_set_id: str = None,
        template_type: str = None,
    ):
        # Specifies whether to allow Facebook to automatically change the template category (to improve the template approval rate). This property is valid only when TemplateType is set to WHATSAPP.
        # >Notice: This property has been deprecated. WhatsApp no longer supports this property.</notice>
        self.allow_category_change = allow_category_change
        # WhatsApp template category. Valid values:
        # 
        # - **UTILITY**: transaction-related.
        # 
        # - **MARKETING**: marketing.
        # 
        # - **AUTHENTICATION**: identity verification.
        # 
        # Viber template category. Valid values:
        # 
        # - **UTILITY**: transaction-related.
        # 
        # - **MARKETING**: marketing.
        # 
        # - **AUTHENTICATION**: identity verification.
        # 
        # This parameter is required.
        self.category = category
        # Specifies whether to pause template sending when a Utility template is changed to Marketing type. This property is valid only for WhatsApp templates.
        self.category_change_paused = category_change_paused
        # The list of message template components.
        # 
        # > When Category=AUTHENTICATION, Components cannot contain nodes with Type=HEADER. When Type=BODY or FOOTER, the Text content must be empty.
        # 
        # This parameter is required.
        self.components = components
        # The SpaceId of the ISV sub-customer or the direct customer instance ID.
        self.cust_space_id = cust_space_id
        # The ISV customer WabaId.
        # 
        # > Deprecated parameter. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id
        # The example for creating the template.
        self.example = example
        # The ISV verification code, used to verify whether the sub-account is authorized by the ISV.
        self.isv_code = isv_code
        # The template language. For detailed language codes, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        # 
        # This parameter is required.
        self.language = language
        # The time-to-live (TTL) for template messages in WhatsApp.
        # - AUTHENTICATION: valid values range from 30 to 900. 
        # - UTILITY: valid values range from 30 to 43200.
        self.message_send_ttl_seconds = message_send_ttl_seconds
        # The template name.
        # 
        # This parameter is required.
        self.name = name
        # productSetId
        self.product_set_id = product_set_id
        # The templatetype. Valid values:
        # 
        # - **WHATSAPP**
        # 
        # - **VIBER**
        # 
        # This parameter is required.
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
        if self.allow_category_change is not None:
            result['AllowCategoryChange'] = self.allow_category_change

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

        if self.name is not None:
            result['Name'] = self.name

        if self.product_set_id is not None:
            result['ProductSetId'] = self.product_set_id

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowCategoryChange') is not None:
            self.allow_category_change = m.get('AllowCategoryChange')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CategoryChangePaused') is not None:
            self.category_change_paused = m.get('CategoryChangePaused')

        self.components = []
        if m.get('Components') is not None:
            for k1 in m.get('Components'):
                temp_model = main_models.CreateChatappTemplateRequestComponents()
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

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProductSetId') is not None:
            self.product_set_id = m.get('ProductSetId')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

class CreateChatappTemplateRequestComponents(DaraModel):
    def __init__(
        self,
        add_secret_recommendation: bool = None,
        buttons: List[main_models.CreateChatappTemplateRequestComponentsButtons] = None,
        caption: str = None,
        cards: List[main_models.CreateChatappTemplateRequestComponentsCards] = None,
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
        # The button list. Applicable only to **BUTTONS** components.
        # 
        # > WhatsApp button quantity rules:
        # > - For WhatsApp templates with Category MARKETING/UTILITY, a maximum of 10 buttons are allowed.
        # > - Only 1 PHONE_NUMBER button is allowed.
        # > - A maximum of 2 URL buttons are allowed.
        # > - QUICK_REPLY buttons cannot appear in mixed order with PHONE_NUMBER/URL buttons.
        # 
        # > Viber button quantity rules:
        # > - Only URL type is supported, and only one button is allowed.
        # > - When the HEADER contains a VIDEO, the button type is URL, but you cannot set a URL address.
        self.buttons = buttons
        # The description of the file.
        self.caption = caption
        # The Carousel template card list.
        self.cards = cards
        # The validity period (in minutes) of the verification code for WhatsApp AUTHENTICATION templates. Valid only for WhatsApp messages when Category is AUTHENTICATION and Component Type is Footer (displayed in the Footer position).
        self.code_expiration_minutes = code_expiration_minutes
        # The duration (in seconds) of Viber video messages. Valid values: 0 to 600.
        self.duration = duration
        # The name of the file.
        self.file_name = file_name
        # The file type for Viber file messages.
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
        # Specifies whether the coupon code has an expiration time. This parameter is used when type = LIMITED_TIME_OFFER.
        self.has_expiration = has_expiration
        # The text of the message to be sent.
        # 
        # > For WHATSAPP type, this property value is empty when Category=AUTHENTICATION.
        self.text = text
        # The thumbnail for Viber video messages.
        self.thumb_url = thumb_url
        # The component type. Valid values:
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
        # > - For Viber templates, the **FOOTER**, **CAROUSEL**, and **LIMITED_TIME_OFFER** types are invalid.
        # > - For Viber templates, images, videos, and files are placed in the **HEADER** (the device displays images below the text). Text is placed in the **BODY**.
        # 
        # This parameter is required.
        self.type = type
        # The media resource path.
        # 
        # > For Viber type, the recommended image size is 800 px × 800 px.
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
                temp_model = main_models.CreateChatappTemplateRequestComponentsButtons()
                self.buttons.append(temp_model.from_map(k1))

        if m.get('Caption') is not None:
            self.caption = m.get('Caption')

        self.cards = []
        if m.get('Cards') is not None:
            for k1 in m.get('Cards'):
                temp_model = main_models.CreateChatappTemplateRequestComponentsCards()
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

class CreateChatappTemplateRequestComponentsCards(DaraModel):
    def __init__(
        self,
        card_components: List[main_models.CreateChatappTemplateRequestComponentsCardsCardComponents] = None,
    ):
        # The list of components in the Carousel card.
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
                temp_model = main_models.CreateChatappTemplateRequestComponentsCardsCardComponents()
                self.card_components.append(temp_model.from_map(k1))

        return self

class CreateChatappTemplateRequestComponentsCardsCardComponents(DaraModel):
    def __init__(
        self,
        buttons: List[main_models.CreateChatappTemplateRequestComponentsCardsCardComponentsButtons] = None,
        format: str = None,
        text: str = None,
        type: str = None,
        url: str = None,
    ):
        # The button list. Applicable only to BUTTONS components. Each Carousel card can have a maximum of two buttons.
        self.buttons = buttons
        # The media resource type. Valid when Type = HEADER.
        # 
        # - **IMAGE**: image 
        # 
        # - **VIDEO**: video
        self.format = format
        # The BODY content in the Carousel card.
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
        # The material path.
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
                temp_model = main_models.CreateChatappTemplateRequestComponentsCardsCardComponentsButtons()
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

class CreateChatappTemplateRequestComponentsCardsCardComponentsButtons(DaraModel):
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
        # - **PHONE_NUMBER**: dial phone button
        # 
        # - **URL**: web button
        # 
        # - **QUICK_REPLY**: quick reply button
        # 
        # This parameter is required.
        self.type = type
        # The URL that is accessed when the button is clicked.
        self.url = url
        # The URL type. 
        # 
        # - **static**: Static.
        # 
        # - **dynamic**: Dynamic.
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

class CreateChatappTemplateRequestComponentsButtons(DaraModel):
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
        supported_apps: List[main_models.CreateChatappTemplateRequestComponentsButtonsSupportedApps] = None,
        text: str = None,
        type: str = None,
        url: str = None,
        url_type: str = None,
    ):
        # Required for WhatsApp templates when Category is AUTHENTICATION and Button Type is ONE_TAP/ZERO_TAP. The button text for the WhatsApp Autofill operation.
        self.autofill_text = autofill_text
        # The coupon code value. Only letters and numbers are supported. You can pass in a variable such as $(couponCode) and provide the actual coupon code when sending.
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
        # The navigate screen. Required when FlowAction=NAVIGATE.
        self.navigate_screen = navigate_screen
        # Use the properties under SupportedApps instead.
        self.package_name = package_name
        # The phone number. Valid only when the button type is **PHONE_NUMBER**.
        self.phone_number = phone_number
        # Use the properties under SupportedApps instead.
        self.signature_hash = signature_hash
        # The list of supported applications.
        self.supported_apps = supported_apps
        # The display name of the button.
        self.text = text
        # The button type.
        # 
        # - **PHONE_NUMBER**: dial phone button
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
        # > - For WhatsApp templates with Category AUTHENTICATION, only one button is allowed, and the type can only be COPY_CODE/ONE_TAP. When COPY_CODE is selected, Text is required. When ONE_TAP is selected, Text (displayed when the target application is not installed on the device, representing the copy verification code button name), SignatureHash, PackageName, and AutofillText are required.
        # > - Viber templates allow only one Button, and it must be URL type.
        # 
        # This parameter is required.
        self.type = type
        # The URL to visit when the link button is clicked.
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
                temp_model = main_models.CreateChatappTemplateRequestComponentsButtonsSupportedApps()
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

class CreateChatappTemplateRequestComponentsButtonsSupportedApps(DaraModel):
    def __init__(
        self,
        package_name: str = None,
        signature_hash: str = None,
    ):
        # Required for WhatsApp templates when Category is AUTHENTICATION and Button Type is ONE_TAP/ZERO_TAP. The package name of the application invoked by WhatsApp.
        self.package_name = package_name
        # Required for WhatsApp templates when Category is AUTHENTICATION and Button Type is ONE_TAP/ZERO_TAP. The signature hash value for the application invoked by WhatsApp.
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

