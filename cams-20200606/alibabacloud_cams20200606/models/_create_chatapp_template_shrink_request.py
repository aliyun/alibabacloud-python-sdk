# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateChatappTemplateShrinkRequest(DaraModel):
    def __init__(
        self,
        allow_category_change: bool = None,
        category: str = None,
        category_change_paused: bool = None,
        components_shrink: str = None,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        example_shrink: str = None,
        isv_code: str = None,
        language: str = None,
        message_send_ttl_seconds: int = None,
        name: str = None,
        template_type: str = None,
    ):
        # Specifies whether to allow Facebook to automatically change the directory of the template. If you set this parameter to true, the review success rate of the template is improved. This parameter is valid only when TemplateType is set to WHATSAPP.
        self.allow_category_change = allow_category_change
        # The category of the template if TemplateType is set to WHATSAPP. Valid values:
        # 
        # *   **UTILITY**: the transaction template
        # *   **MARKETING**: the marketing template
        # *   **AUTHENTICATION**: the authentication template
        # 
        # The category of the template if TemplateType is set to VIBER. Valid values:
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
        # This parameter is required.
        self.category = category
        self.category_change_paused = category_change_paused
        # The components of the message template.
        # 
        # >  If Category is set to AUTHENTICATION, the Type sub-parameter of the Components parameter cannot be set to HEADER. If the Type sub-parameter is set to BODY or FOOTER, the Text sub-parameter of the Components parameter must be empty.
        # 
        # This parameter is required.
        self.components_shrink = components_shrink
        # The space ID of the user within the ISV account.
        self.cust_space_id = cust_space_id
        # The WhatsApp Business account (WABA) ID of the user within the independent software vendor (ISV) account.
        # 
        # > CustWabaId is an obsolete parameter. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id
        # The examples of variables that are used when you create the message template.
        self.example_shrink = example_shrink
        # The independent software vendor (ISV) verification code, which is used to verify whether the user is authorized by the ISV account.
        self.isv_code = isv_code
        # The language that is used in the message template. For more information, see [Language codes](https://help.aliyun.com/document_detail/463420.html).
        # 
        # This parameter is required.
        self.language = language
        # Validity period of authentication template message sending in WhatsApp
        # 
        # > This attribute requires providing waba in advance to Alibaba operators to open the whitelist, otherwise it will result in template submission failure
        self.message_send_ttl_seconds = message_send_ttl_seconds
        # The name of the message template.
        # 
        # This parameter is required.
        self.name = name
        # The type of the message template.
        # 
        # *   **WHATSAPP**
        # *   **VIBER**
        # *   LINE: the Line message template. This type of message template will be released later.
        # 
        # This parameter is required.
        self.template_type = template_type

    def validate(self):
        pass

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

        if self.components_shrink is not None:
            result['Components'] = self.components_shrink

        if self.cust_space_id is not None:
            result['CustSpaceId'] = self.cust_space_id

        if self.cust_waba_id is not None:
            result['CustWabaId'] = self.cust_waba_id

        if self.example_shrink is not None:
            result['Example'] = self.example_shrink

        if self.isv_code is not None:
            result['IsvCode'] = self.isv_code

        if self.language is not None:
            result['Language'] = self.language

        if self.message_send_ttl_seconds is not None:
            result['MessageSendTtlSeconds'] = self.message_send_ttl_seconds

        if self.name is not None:
            result['Name'] = self.name

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

        if m.get('Components') is not None:
            self.components_shrink = m.get('Components')

        if m.get('CustSpaceId') is not None:
            self.cust_space_id = m.get('CustSpaceId')

        if m.get('CustWabaId') is not None:
            self.cust_waba_id = m.get('CustWabaId')

        if m.get('Example') is not None:
            self.example_shrink = m.get('Example')

        if m.get('IsvCode') is not None:
            self.isv_code = m.get('IsvCode')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('MessageSendTtlSeconds') is not None:
            self.message_send_ttl_seconds = m.get('MessageSendTtlSeconds')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

