# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCardSmsLinkRequest(DaraModel):
    def __init__(
        self,
        card_code_type: int = None,
        card_link_type: int = None,
        card_template_code: str = None,
        card_template_param_json: str = None,
        custom_short_code_json: str = None,
        domain: str = None,
        out_id: str = None,
        phone_number_json: str = None,
        sign_name_json: str = None,
    ):
        # The code type of the URLs.
        # 
        # *   **1**: group texting
        # *   **2**: personalization
        self.card_code_type = card_code_type
        # The type of the short URLs.
        # 
        # *   1: standard short code.
        # *   2: custom short code.
        # 
        # > If the **CardLinkType** is not specified, standard short codes are generated. If you need to generate custom short codes, contact Alibaba Cloud SMS technical support.
        self.card_link_type = card_link_type
        # The code of the message template. You can view the template code in the **Template Code** column on the **Templates** tab of the **Go China** page in the Alibaba Cloud SMS console.
        # 
        # > Make sure that the message template has been approved.
        # 
        # This parameter is required.
        self.card_template_code = card_template_code
        # The variables of the message template.
        self.card_template_param_json = card_template_param_json
        # The custom short code. It can contain 4 to 8 digits or letters.
        # 
        # > If the CardLinkType parameter is set to 2, the CustomShortCodeJson parameter is required.
        self.custom_short_code_json = custom_short_code_json
        # The original domain name. You must submit domain names for approval in advance.
        # 
        # > 
        # 
        # *   If the **CardLinkType** parameter is set to **2**, the **Domain** parameter is required.
        # 
        # *   The **Domain** parameter cannot exceed 100 characters in length. If the parameter is not specified, a default domain name is used.
        self.domain = domain
        # The extension field.
        self.out_id = out_id
        # The mobile phone numbers of recipients, custom identifiers, or system identifiers.
        # 
        # > 
        # 
        # *   A maximum of 10,000 mobile phone numbers are supported.
        # 
        # *   You can enter custom identifier. Each identifier can be a maximum of 60 characters in length.
        # 
        # *   You can apply for a maximum of 10 OPPO templates at a time.
        self.phone_number_json = phone_number_json
        # The signature. You can view the template code in the **Signature** column on the **Signaturess** tab of the **Go China** page in the Alibaba Cloud SMS console.
        # 
        # > The signatures must be approved and correspond to the mobile numbers in sequence.
        # 
        # This parameter is required.
        self.sign_name_json = sign_name_json

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.card_code_type is not None:
            result['CardCodeType'] = self.card_code_type

        if self.card_link_type is not None:
            result['CardLinkType'] = self.card_link_type

        if self.card_template_code is not None:
            result['CardTemplateCode'] = self.card_template_code

        if self.card_template_param_json is not None:
            result['CardTemplateParamJson'] = self.card_template_param_json

        if self.custom_short_code_json is not None:
            result['CustomShortCodeJson'] = self.custom_short_code_json

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.out_id is not None:
            result['OutId'] = self.out_id

        if self.phone_number_json is not None:
            result['PhoneNumberJson'] = self.phone_number_json

        if self.sign_name_json is not None:
            result['SignNameJson'] = self.sign_name_json

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CardCodeType') is not None:
            self.card_code_type = m.get('CardCodeType')

        if m.get('CardLinkType') is not None:
            self.card_link_type = m.get('CardLinkType')

        if m.get('CardTemplateCode') is not None:
            self.card_template_code = m.get('CardTemplateCode')

        if m.get('CardTemplateParamJson') is not None:
            self.card_template_param_json = m.get('CardTemplateParamJson')

        if m.get('CustomShortCodeJson') is not None:
            self.custom_short_code_json = m.get('CustomShortCodeJson')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('PhoneNumberJson') is not None:
            self.phone_number_json = m.get('PhoneNumberJson')

        if m.get('SignNameJson') is not None:
            self.sign_name_json = m.get('SignNameJson')

        return self

