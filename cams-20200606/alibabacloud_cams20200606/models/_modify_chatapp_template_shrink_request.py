# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyChatappTemplateShrinkRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        category_change_paused: bool = None,
        components_shrink: str = None,
        cust_space_id: str = None,
        cust_waba_id: str = None,
        example_shrink: str = None,
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
        self.components_shrink = components_shrink
        # The SpaceId of the ISV sub-customer or the instance ID of the direct customer.
        self.cust_space_id = cust_space_id
        # The ISV customer WabaId.
        # 
        # > This parameter is deprecated. Use CustSpaceId instead.
        self.cust_waba_id = cust_waba_id
        # The example for creating a template.
        self.example_shrink = example_shrink
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
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if m.get('ProductSetId') is not None:
            self.product_set_id = m.get('ProductSetId')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

