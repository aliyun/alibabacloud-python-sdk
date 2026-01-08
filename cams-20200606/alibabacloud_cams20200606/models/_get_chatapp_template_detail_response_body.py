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
    ):
        # Access denied details.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code.
        # 
        # *   Example: OK. This value indicates that the request is successful.
        # *   Other codes indicate that the request fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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
        quality_score: str = None,
        reason: str = None,
        template_code: str = None,
        template_type: str = None,
    ):
        self.allow_send = allow_send
        # The review status of the message template. Valid values:
        # 
        # *   **pass**: The message template is approved.
        # *   **fail**: The message template is rejected.
        # *   **auditing**: The message template is being reviewed.
        # *   **unaudit**: The review is suspended.
        self.audit_status = audit_status
        # The category of the template when the returned value of TemplateType is WHATSAPP. Valid values:
        # 
        # *   **UTILITY**: a transactional template
        # *   **MARKETING**: a marketing template
        # *   **AUTHENTICATION**: an identity authentication template
        # 
        # The category of the template when the returned value of the TemplateType parameter is VIBER. Valid values:
        # 
        # *   **text**: a template that contains only text
        # *   **image**: a template that contains only images
        # *   **text_image_button**: a template that contains text, images, and buttons
        # *   **text_button**: a template that contains text and buttons
        # *   **document**: a template that contains only files
        # *   **video**: a template that contains only videos
        # *   **text_video**: a template that contains text and videos
        # *   **text_video_button**: a template that contains text, videos, and buttons
        # *   **text_image**: a template that contains text and images
        # 
        # > If Category is set to text_video_button, users cannot open a web page by clicking the button. Users can open only the video in the message. In this case, you do not need to specify the Url parameter for the URL button in the template.
        self.category = category
        self.category_change_paused = category_change_paused
        # The components of the message template.
        self.components = components
        # The examples of variables.
        self.example = example
        # The language that is used in the message template. For more information, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        self.language = language
        # The validity period of the WhatsApp authentication message.
        self.message_send_ttl_seconds = message_send_ttl_seconds
        # The name of the message template.
        self.name = name
        # The quality of the template.
        self.quality_score = quality_score
        # The reason why the template was rejected.
        self.reason = reason
        # The code of the message template.
        self.template_code = template_code
        # The type of the message template. Valid values:
        # 
        # *   **WHATSAPP**
        # *   **VIBER**
        # *   LINE (developing)
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
        # The note indicating that customers cannot share verification codes with others. The note is displayed in the message body. This parameter is valid if Category is set to AUTHENTICATION and the Type sub-parameter of the Components parameter is set to BODY for a WhatsApp message template.
        self.add_secret_recommendation = add_secret_recommendation
        # The buttons. This parameter is returned only if the Type sub-parameter of the Components parameter is set to **BUTTONS**.
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
        # The description of the document.
        self.caption = caption
        # The carousel cards.
        self.cards = cards
        # The validity period of the verification code in the WhatsApp authentication template. Unit: minutes. This parameter is valid only when Category is set to AUTHENTICATION and the Type sub-parameter of the Components parameter is set to FOOTER for a WhatsApp message template. The validity period of the verification code is displayed in the footer.
        self.code_expiration_minutes = code_expiration_minutes
        # The length of the video in the Viber message template. Unit: seconds. Valid values: 0 to 600.
        self.duration = duration
        # The name of the document.
        self.file_name = file_name
        # The type of the document attached in the Viber message template.
        self.file_type = file_type
        # The format.
        self.format = format
        # The latitude of the location.
        self.latitude = latitude
        # The address of the location.
        self.location_address = location_address
        # The name of the location.
        self.location_name = location_name
        # The longitude of the location.
        self.longitude = longitude
        # The variable when the coupon code expires in the limited-time offer template.
        self.offer_expiration_time_ms = offer_expiration_time_ms
        # The text of the message that you want to send.
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
        self.type = type
        # The URL of the media resource.
        self.url = url
        # Indicates whether the coupon code has an expiration time in the limited-time offer template.
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
        # The components of the carousel card.
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
        # The buttons of the carousel card.
        self.buttons = buttons
        # The type of the header in the carousel template. The header can only be an image or a video. The headers of all carousel cards must be the same. The type of the media resources that are included in the message. Valid values: IMGAGE and VIDEO.
        self.format = format
        # The text of the carousel card.
        self.text = text
        # The component type.
        self.type = type
        # The URL.
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
        # The button text.
        self.text = text
        # The type of the button in the carousel template. Valid values: URL, PHONE_NUMBER, and QUICK_REQLY.
        self.type = type
        # The URL to which you are redirected when you click the URL button.
        self.url = url
        # The type of the URL. Valid values: static and dynamic.
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
        # The text of the one-tap autofill button. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP in a WhatsApp message template.
        self.autofill_text = autofill_text
        # The coupon code.
        self.coupon_code = coupon_code
        # The extended fields.
        self.extend_attrs = extend_attrs
        # The Flow action. Valid values: NAVIGATE and DATA_EXCHANGE.
        self.flow_action = flow_action
        # The Flow ID.
        self.flow_id = flow_id
        # The unsubscribe button. This parameter is valid if Category is set to MARKETING and the Type sub-parameter of the Buttons parameter is set to QUICK_REPLY for a WhatsApp message template. Marketing messages will not be sent to customers if you configure message sending in the Chat App Message Service console and the customers click this button.
        self.is_opt_out = is_opt_out
        # The first screen in the Flow. This parameter is returned if FlowAction is set to NAVIGATE.
        self.navigate_screen = navigate_screen
        # The app package name that WhatsApp uses to load your app. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP in a WhatsApp message template.
        self.package_name = package_name
        # The phone number. This parameter is valid only if the Type sub-parameter of the Buttons parameter is set to **PHONE_NUMBER**.
        self.phone_number = phone_number
        # The app signing key hash that WhatsApp uses to load your app. This parameter is required if Category is set to AUTHENTICATION and the Type sub-parameter of the Buttons parameter is set to ONE_TAP in a WhatsApp message template.
        self.signature_hash = signature_hash
        # The apps that support one-tap authentication and zero-tap authentication.
        self.supported_apps = supported_apps
        # The display name of the button.
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
        self.type = type
        # The URL to which you are redirected when you click the URL button.
        self.url = url
        # The URL type. Valid values:
        # 
        # *   **static**
        # *   **dynamic**
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
        # The app package name.
        self.package_name = package_name
        # The app signing key hash.
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
        # The language of the next template.
        self.next_language_code = next_language_code
        # The code of the next template.
        self.next_template_code = next_template_code
        # The name of the next template.
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

