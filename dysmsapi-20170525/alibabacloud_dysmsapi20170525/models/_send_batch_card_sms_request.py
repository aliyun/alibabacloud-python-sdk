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
        # The code of the card SMS template. On the **Card SMS** [Template Management](https://dysms.console.aliyun.com/domestic/card) page in the console, select the code of a card SMS template that has been **approved**.
        # 
        # This parameter is required.
        self.card_template_code = card_template_code
        # The actual values of the variables in the card SMS template. This parameter is required when the card SMS template specified by **CardTemplateCode** contains variables.
        # 
        # >If the JSON contains line breaks, handle them based on the standard JSON protocol.
        self.card_template_param_json = card_template_param_json
        # The code of the digital SMS template used for fallback. This parameter is required when **FallbackType** is set to **DIGITALSMS** (fallback to digital SMS).
        # 
        # You can view the list of digital SMS templates on the **Domestic Digital SMS** [Template Management](https://dysms.console.aliyun.com/domestic/digit) page in the console.
        # >The template must be added and approved.
        self.digital_template_code = digital_template_code
        # The actual values of the variables in the digital SMS template. This parameter is required when the fallback digital SMS template specified by **DigitalTemplateCode** contains variables.
        # >If the JSON contains line breaks, handle them based on the standard JSON protocol.
        self.digital_template_param_json = digital_template_param_json
        # The fallback type. Valid values:
        # - **SMS**: Phone numbers that do not support card SMS messages fall back to text SMS messages.
        # - **DIGITALSMS**: Phone numbers that do not support card SMS messages fall back to digital SMS messages.
        # - **NONE**: No fallback is required.
        # 
        # This parameter is required.
        self.fallback_type = fallback_type
        # The ID reserved for the caller.
        self.out_id = out_id
        # The mobile phone numbers that receive the SMS messages.
        # 
        # This parameter is required.
        self.phone_number_json = phone_number_json
        # The name of the SMS signature.
        # You can call the [QuerySmsSignList](https://help.aliyun.com/document_detail/419282.html) operation to query the signatures that have been submitted under the current account, or you can view the list of signatures in the [Short Message Service console](https://dysms.console.aliyun.com/domestic/text/sign).
        # >The signature must be added and approved. The number of SMS signatures must be the same as the number of phone numbers, and the signatures must be in one-to-one correspondence with the phone numbers.
        # 
        # This parameter is required.
        self.sign_name_json = sign_name_json
        # The code of the text SMS template used for fallback. This parameter is required when **FallbackType** is set to **SMS** (fallback to text SMS).
        # 
        # You can call the [QuerySmsTemplateList](https://help.aliyun.com/document_detail/419288.html) operation to query the templates that have been submitted under the current account, or you can view the list of templates in the [Short Message Service console](https://dysms.console.aliyun.com/domestic/text/template).
        # >The template must be added and approved.
        self.sms_template_code = sms_template_code
        # The actual values of the variables in the text SMS template. This parameter is required when the fallback text SMS template specified by **SmsTemplateCode** contains variables.
        # 
        # >If the JSON contains line breaks, handle them based on the standard JSON protocol.
        self.sms_template_param_json = sms_template_param_json
        # The extension code of the MO (mobile-originated) SMS message.
        self.sms_up_extend_code_json = sms_up_extend_code_json
        # The code of the custom send content template.
        # 
        # The custom content is sent to the terminal in the form of the selected text SMS template plus the card parsing link. You can log on to the [Short Message Service console](https://dysms.console.aliyun.com/overview), choose **Domestic Messages** or **International/Hong Kong, Macao, and Taiwan Messages**, and then view the **Template Code** on the **Template Management** page.
        # 
        # > - The template must be added and approved. To send international or Hong Kong, Macao, and Taiwan messages, use an international or Hong Kong, Macao, and Taiwan SMS template.
        # > - For example, the selected text SMS template content is: You have a message to check; the card parsing link is: `1*.cn/2**d`. The final delivered content is: `You have a message to check 1*.cn/2**d`. Perform testing and control the number of characters before sending.
        self.template_code = template_code
        # The actual values of the variables in the custom send content template. This parameter is required when the SMS template specified by **TemplateCode** contains variables.
        # 
        # > - If the JSON contains line breaks, handle them based on the standard JSON protocol.
        # > - The number of template variable values must be the same as the number of phone numbers and signatures, and they must be in one-to-one correspondence. This indicates that an SMS message with the corresponding signature is sent to the specified phone number, and the variable parameters in the SMS template are replaced with the corresponding values.
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

