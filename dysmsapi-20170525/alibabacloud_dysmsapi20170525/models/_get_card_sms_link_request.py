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
        # The encoding type of the short URL for the card message. Valid values:
        # - 1: bulk sending.
        # - 2: personalized.
        self.card_code_type = card_code_type
        # The type of the short URL for the card message. Valid values:
        # - 1: standard short URL.
        # - 2: custom short URL.
        # 
        # > If **CardLinkType** is left empty, the default value is standard short URL. To generate a custom short URL, contact Alibaba Cloud operations to register in advance.
        self.card_link_type = card_link_type
        # The code of the card message template. In the console, go to the [Card Messages > Template Management](https://dysms.console.aliyun.com/domestic/card) page and select the code of an approved card message template.
        # 
        # This parameter is required.
        self.card_template_code = card_template_code
        # The variables of the card message template.
        self.card_template_param_json = card_template_param_json
        # The custom short code. The value must be 4 to 8 digits or letters.
        # 
        # > This parameter is required when the generation type is custom short URL.
        self.custom_short_code_json = custom_short_code_json
        # The short URL domain assigned to the sending account. The domain must be registered in advance.
        # 
        # > - When **CardLinkType** is set to **2**, the **Domain** parameter is required.
        # > - If the **Domain** parameter is left empty, the system default domain is used. The value can be up to 100 characters in length.
        self.domain = domain
        # The external extension field.
        self.out_id = out_id
        # The phone number, user ID, or internal system identifier.
        # 
        # > - Supports up to 10,000 phone numbers.
        # > - You can also specify a custom identifier of up to 60 characters.
        # > - For OPPO templates, you can submit up to 10 requests at a time.
        self.phone_number_json = phone_number_json
        # The signature name of the SMS message.
        # In the console, go to the [Domestic Messages > Signature Management](https://dysms.console.aliyun.com/domestic/text/sign) tab and view the name in the **Signature Name** column. You can also call the [QuerySmsSignList](https://www.alibabacloud.com/help/en/sms/developer-reference/api-dysmsapi-2017-05-25-querysmssignlist) operation to view SMS signature names.
        # 
        # > The signature must be added and approved. The number of SMS signatures must match the number of phone numbers, and each signature must correspond to a phone number.
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

