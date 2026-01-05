# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendBatchCardSmsRequest(DaraModel):
    def __init__(
        self,
        card_template_code: str = None,
        card_template_param_json: str = None,
        digital_template_code: str = None,
        digital_template_param_json: str = None,
        fallback_type: str = None,
        out_id: str = None,
        phone_number_json: str = None,
        sign_name_json: str = None,
        sms_template_code: str = None,
        sms_template_param_json: str = None,
        sms_up_extend_code_json: str = None,
        template_code: str = None,
        template_param_json: str = None,
    ):
        # The code of the message template. You can view the template code in the **Template Code** column on the **Templates** tab of the **Go China** page in the Alibaba Cloud SMS console.
        # 
        # > Make sure that the message template has been approved.
        # 
        # This parameter is required.
        self.card_template_code = card_template_code
        # The variables of the card message template.
        self.card_template_param_json = card_template_param_json
        # The code of the digital message template that applies when the card message is rolled back. You can view the template code in the **Template Code** column on the **Templates** tab of the **Go China** page in the Alibaba Cloud SMS console.
        # 
        # > Make sure that the message template has been approved.
        self.digital_template_code = digital_template_code
        # The variables of the digital message template.
        self.digital_template_param_json = digital_template_param_json
        # The rollback type. Valid values:
        # 
        # *   **SMS**: text message
        # *   **DIGITALSMS**: digital message
        # *   **NONE**: none
        # 
        # This parameter is required.
        self.fallback_type = fallback_type
        # The ID that is reserved for the caller of the operation.
        self.out_id = out_id
        # The mobile numbers of the recipients.
        # 
        # This parameter is required.
        self.phone_number_json = phone_number_json
        # The signature. You can view the template code in the **Signature** column on the **Signaturess** tab of the **Go China** page in the Alibaba Cloud SMS console.
        # 
        # > The signatures must be approved and correspond to the mobile numbers in sequence.
        # 
        # This parameter is required.
        self.sign_name_json = sign_name_json
        # The code of the text message template that applies when the card message is rolled back. You can view the template code in the **Template Code** column on the **Templates** tab of the **Go China** page in the Alibaba Cloud SMS console.
        # 
        # > Make sure that the message template has been approved.
        self.sms_template_code = sms_template_code
        # The variables of the text message template.
        self.sms_template_param_json = sms_template_param_json
        # The extension code of the upstream message.
        self.sms_up_extend_code_json = sms_up_extend_code_json
        # The code of the message template.
        # 
        # You can log on to the [Alibaba Cloud console](https://dysms.console.aliyun.com/dysms.htm?spm=5176.12818093.categories-n-products.ddysms.3b2816d0xml2NA#/overview), click **Go China** or **Go Globe** in the left-side navigation pane, and then view the **template code** on the **Templates** tab.
        # 
        # > You must specify a message template that is created in the SMS console and approved by Alibaba Cloud. If you send messages to countries or regions outside the Chinese mainland, use the corresponding message templates.
        self.template_code = template_code
        # The value of the variable in the message template.
        # 
        # > If you need to add line breaks to the JSON template, make sure that the format is valid. In addition, the sequence of variable values must be the same as that of the mobile numbers and signatures.
        self.template_param_json = template_param_json

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.card_template_code is not None:
            result['CardTemplateCode'] = self.card_template_code

        if self.card_template_param_json is not None:
            result['CardTemplateParamJson'] = self.card_template_param_json

        if self.digital_template_code is not None:
            result['DigitalTemplateCode'] = self.digital_template_code

        if self.digital_template_param_json is not None:
            result['DigitalTemplateParamJson'] = self.digital_template_param_json

        if self.fallback_type is not None:
            result['FallbackType'] = self.fallback_type

        if self.out_id is not None:
            result['OutId'] = self.out_id

        if self.phone_number_json is not None:
            result['PhoneNumberJson'] = self.phone_number_json

        if self.sign_name_json is not None:
            result['SignNameJson'] = self.sign_name_json

        if self.sms_template_code is not None:
            result['SmsTemplateCode'] = self.sms_template_code

        if self.sms_template_param_json is not None:
            result['SmsTemplateParamJson'] = self.sms_template_param_json

        if self.sms_up_extend_code_json is not None:
            result['SmsUpExtendCodeJson'] = self.sms_up_extend_code_json

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        if self.template_param_json is not None:
            result['TemplateParamJson'] = self.template_param_json

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CardTemplateCode') is not None:
            self.card_template_code = m.get('CardTemplateCode')

        if m.get('CardTemplateParamJson') is not None:
            self.card_template_param_json = m.get('CardTemplateParamJson')

        if m.get('DigitalTemplateCode') is not None:
            self.digital_template_code = m.get('DigitalTemplateCode')

        if m.get('DigitalTemplateParamJson') is not None:
            self.digital_template_param_json = m.get('DigitalTemplateParamJson')

        if m.get('FallbackType') is not None:
            self.fallback_type = m.get('FallbackType')

        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('PhoneNumberJson') is not None:
            self.phone_number_json = m.get('PhoneNumberJson')

        if m.get('SignNameJson') is not None:
            self.sign_name_json = m.get('SignNameJson')

        if m.get('SmsTemplateCode') is not None:
            self.sms_template_code = m.get('SmsTemplateCode')

        if m.get('SmsTemplateParamJson') is not None:
            self.sms_template_param_json = m.get('SmsTemplateParamJson')

        if m.get('SmsUpExtendCodeJson') is not None:
            self.sms_up_extend_code_json = m.get('SmsUpExtendCodeJson')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('TemplateParamJson') is not None:
            self.template_param_json = m.get('TemplateParamJson')

        return self

