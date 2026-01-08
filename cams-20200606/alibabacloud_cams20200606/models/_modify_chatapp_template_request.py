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
        template_code: str = None,
        template_name: str = None,
        template_type: str = None,
    ):
        # The category of the Viber message template. Valid values:
        # 
        # *   **text**: the template that contains only text
        # *   **image**: the template that contains only images
        # *   **text_image_button**: the template that contains text, images, and buttons
        # *   **text_button**: the template that contains text and buttons
        # *   **document**: the template that contains only documents
        # *   **video**: the template that contains only videos
        # *   **text_video**: the template that contains text and videos
        # *   **text_video_button**: the template that contains text, videos, and buttons
        # *   **text_image**: the template that contains text and images
        # 
        # > This parameter applies only to Viber message templates.
        self.category = category
        self.category_change_paused = category_change_paused
        # The components of the message template.
        # 
        # >  If Category is set to AUTHENTICATION, the Type sub-parameter of the Components parameter cannot be set to HEADER. If the Type sub-parameter is set to BODY or FOOTER, you do not need to set the Text sub-parameter of the Components parameter because the value is automatically generated.
        # 
        # This parameter is required.
        self.components = components
        # The space ID of the user within the ISV account.
        self.cust_space_id = cust_space_id
        # The WhatsApp Business account (WABA) ID of the user within the independent software vendor (ISV) account.
        # 
        # > CustWabaId is an obsolete parameter. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id
        # The examples of variables that are used when you create the message template.
        self.example = example
        # The ISV verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        # The language that is used in the message template. For more information, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        # 
        # This parameter is required.
        self.language = language
        # Validity period of authentication template message sending in WhatsApp
        # 
        # >This attribute requires providing waba in advance to Alibaba operators to open the whitelist, otherwise it will result in template submission failure
        self.message_send_ttl_seconds = message_send_ttl_seconds
        # The message template code.
        self.template_code = template_code
        # Template name.
        self.template_name = template_name
        # The type of the message template.
        # 
        # *   **WHATSAPP**
        # *   **VIBER**
        # *   LINE: the Line message template. This type of message template will be released later.
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
        # The note indicating that customers cannot share verification codes with others. The note is displayed in the message body. This parameter is valid if Category is set to AUTHENTICATION and the Type sub-parameter of the Components parameter is set to BODY for a WhatsApp message template.
        self.add_secret_recommendation = add_secret_recommendation
        # The buttons. Specify this parameter only if you set the Type sub-parameter of the Components parameter to **BUTTONS**.
        # 
        # >  ####
        # 
        # *   A marketing or utility WhatsApp message template can contain up to 10 buttons.
        # 
        # *   A WhatsApp message template can contain only one phone call button.
        # 
        # *   A WhatsApp message template can contain up to two URL buttons.
        # 
        # *   In a WhatsApp message template, a quick reply button cannot be used together with a phone call button or a URL button.
        self.buttons = buttons
        # The description of the media resource.
        # 
        # >  If the Type sub-parameter of the Components parameter is set to **HEADER** and the Format parameter is set to **IMAGE, DOCUMENT, or VIDEO**, you can specify this parameter.
        self.caption = caption
        # The carousel cards of the carousel template.
        self.cards = cards
        # The validity period of the verification code in the WhatsApp authentication template. Unit: minutes. This parameter is valid only when Category is set to AUTHENTICATION and the Type sub-parameter of the Components parameter is set to FOOTER. The validity period of the verification code is displayed in the footer.
        self.code_expiration_minutes = code_expiration_minutes
        # The length of the video in the Viber message template. Unit: seconds. Valid values: 0 to 600.
        self.duration = duration
        # The name of the document.
        # 
        # >  If the Type sub-parameter of the Components parameter is set to **HEADER** and the Format parameter is set to **DOCUMENT**, you can specify this parameter.
        self.file_name = file_name
        # The type of the document attached in the Viber message template.
        self.file_type = file_type
        # The type of the media resource. Valid values:
        # 
        # *   **TEXT**
        # *   **IMAGE**
        # *   **DOCUMENT**
        # *   **VIDEO**
        self.format = format
        # Specifies whether the coupon code has an expiration time. Specify this parameter if the Type sub-parameter of the Components parameter is set to LIMITED_TIME_OFFER.
        self.has_expiration = has_expiration
        # The text of the message that you want to send.
        # 
        # >  If Category is set to AUTHENTICATION, do not specify the Text sub-parameter of the Components parameter.
        self.text = text
        # The thumbnail URL of the video in the Viber message template.
        self.thumb_url = thumb_url
        # The component type. Valid values:
        # 
        # *   **BODY**
        # *   **HEADER**
        # *   **FOOTER**
        # *   **BUTTONS**
        # *   **CAROUSEL**
        # *   **LIMITED_TIME_OFFER**
        # 
        # > 
        # 
        # *   In a WhatsApp message template, a **Body** component cannot exceed 1,024 characters in length. A **HEADER** or **FOOTER** component cannot exceed 60 characters in length.
        # 
        # *   **FOOTER**, **CAROUSEL**, and **LIMITED_TIME_OFFER** components are not supported in Viber message templates.
        # 
        # *   In Viber message templates, media resources such as images, videos, and documents are placed in the **HEADER** component. If a Viber message contains text and an image, the image is placed below the text in the message received on a device.
        # 
        # This parameter is required.
        self.type = type
        # The URL of the media resource.
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
        # The components of the carousel card.
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
        # The buttons. Specify this parameter only if you set the Type sub-parameter of the CardComponents parameter to BUTTONS. A carousel card can contain up to two buttons.
        self.buttons = buttons
        # The type of the media resource. This parameter is valid if the Type sub-parameter of the CardComponents parameter is set to HEADER. Valid values:
        # 
        # *   **IMAGE**
        # *   **VIDEO**
        self.format = format
        # The body content of the carousel card.
        self.text = text
        # The component type. Valid values:
        # 
        # *   **BODY**
        # *   **HEADER**
        # *   **BUTTONS**
        # 
        # This parameter is required.
        self.type = type
        # The URL of the media resource.
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
        # The text of the button.
        self.text = text
        # The button type. Valid values:
        # 
        # *   **PHONE_NUMBER**: phone call button
        # *   **URL**: URL button
        # *   **QUICK_REPLY**: quick reply button
        # 
        # This parameter is required.
        self.type = type
        # The URL to which you are redirected when you click the URL button.
        self.url = url
        # The URL type. Valid values:
        # 
        # *   **static**
        # *   **dynamic**
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
        # The text of the one-tap autofill button. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP for a WhatsApp message template.
        self.autofill_text = autofill_text
        # The coupon code. It can contain only letters and digits. You can set this parameter to a variable such as $(couponCode). Specify the value of couponCode when you send a message.
        self.coupon_code = coupon_code
        # The Flow action.
        # 
        # Valid values:
        # 
        # *   DATA_EXCHANGE
        # *   NAVIGATE
        self.flow_action = flow_action
        # The Flow ID.
        self.flow_id = flow_id
        # The unsubscribe button. This parameter is valid if Category is set to MARKETING and the Type sub-parameter of the Buttons parameter is set to QUICK_REPLY for a WhatsApp message template. Marketing messages will not be sent to customers if you configure message sending in the Chat App Message Service console and the customers click this button.
        self.is_opt_out = is_opt_out
        # The first screen in the Flow. This parameter is required if FlowAction is set to NAVIGATE.
        self.navigate_screen = navigate_screen
        # The app package name that WhatsApp uses to load your app. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP for a WhatsApp message template.
        self.package_name = package_name
        # The phone number.
        self.phone_number = phone_number
        # The app signing key hash that WhatsApp uses to load your app. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP for a WhatsApp message template.
        self.signature_hash = signature_hash
        # List of supported apps.
        self.supported_apps = supported_apps
        # The text of the button.
        self.text = text
        # The button type. Valid values:
        # 
        # *   **PHONE_NUMBER**: phone call button
        # *   **URL**: URL button
        # *   **QUICK_REPLY**: quick reply button
        # *   **COPY_CODE**: copy code button
        # *   **ONE_TAP**: one-tap autofill button if Category is set to AUTHENTICATION
        # 
        # > 
        # 
        # *   If Category is set to AUTHENTICATION for a WhatsApp message template, you can add only one button to the WhatsApp message template and you must set the Type sub-parameter of the Buttons parameter to COPY_CODE or ONE_TAP. If Type is set to COPY_CODE, the Text sub-parameter of the Buttons parameter is required. If Type is set to ONE_TAP, the Text, SignatureHash, PackageName, and AutofillText sub-parameters of the Buttons parameter are required. The value of Text is displayed if the desired app is not installed on the device. The value of Text indicates that you must manually copy the verification code.
        # 
        # *   You can add only one button to a Viber message template, and you must set the Type sub-parameter of the Buttons parameter to URL.
        # 
        # This parameter is required.
        self.type = type
        # The URL to which you are redirected when you click the URL button.
        self.url = url
        # The URL type. Valid values:
        # 
        # *   **static**
        # *   **dynamic**
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
        # The Whatsapp template is required when the Category is\\" Authorisation \\"and the Button Type is\\" ONE_TAP/ZERO-TAP\\", indicating the signature hash value of the Whatsapp call application.
        self.package_name = package_name
        # The Whatsapp template is required when the Category is\\" Authorisation \\"and the Button Type is\\" ONE_TAP/ZERO-TAP\\", indicating the signature hash value of the Whatsapp call application.
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

