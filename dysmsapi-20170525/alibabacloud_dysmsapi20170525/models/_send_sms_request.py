# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendSmsRequest(DaraModel):
    def __init__(
        self,
        out_id: str = None,
        owner_id: int = None,
        phone_numbers: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name: str = None,
        sms_up_extend_code: str = None,
        template_code: str = None,
        template_param: str = None,
    ):
        # The external transaction ID.
        # 
        # > You can ignore this parameter if you do not have special requirements.
        self.out_id = out_id
        self.owner_id = owner_id
        # The recipient\\"s mobile number. The format varies based on the destination region:
        # 
        # - For messages to the Chinese mainland: A mobile number, with or without a country code. Valid prefixes are +, +86, 0086, and 86. Example: 1390000\\*\\*\\*\\*.
        # 
        # - For international messages or messages to Hong Kong, Macao, or Taiwan: Use the format [Country code][Mobile number]. Example: 852000012\\*\\*\\*\\*.
        # 
        # - To send a test message, bind a test mobile number in the [console](https://dysms.console.aliyun.com/quickstart).
        # 
        # > To send a message to multiple numbers, separate them with commas (,). You can specify up to 1,000 mobile numbers per request. Bulk sending may have higher latency than sending single messages. For time-sensitive messages such as verification codes, we recommend sending them individually.
        # 
        # This parameter is required.
        self.phone_numbers = phone_numbers
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The signature name.
        # 
        # Call the [QuerySmsSignList](https://help.aliyun.com/document_detail/419282.html) API or view your list of signatures in the [Short Message Service console](https://dysms.console.aliyun.com/domestic/text/sign). You must use a signature that has been **approved**.
        # 
        # > - 1\\. If a verification code signature and a general-purpose signature share the same name, the general-purpose signature is used by default.
        # >
        # > - 2\\. The system uses the specified signature to send the message.
        # 
        # This parameter is required.
        self.sign_name = sign_name
        # The upstream SMS extension code. An upstream SMS message is a message sent from a user to a service provider to subscribe to a service, make a query, or perform other tasks. Such messages are charged by the carrier at standard rates.
        # 
        # > The system assigns a default extension code when a signature is created. Use this parameter to specify a different code. You can ignore this parameter if you do not have special requirements.
        self.sms_up_extend_code = sms_up_extend_code
        # The code of the template.
        # 
        # Call the [QuerySmsTemplateList](https://help.aliyun.com/document_detail/419288.html) API or view your list of templates in the [Short Message Service console](https://dysms.console.aliyun.com/domestic/text/template). You must use the code of a template that has been **approved**.
        # 
        # This parameter is required.
        self.template_code = template_code
        # The values for the template variables, specified as a **JSON string**. This parameter is required if the template contains variables. The JSON string must provide a value for each variable.
        # 
        # > - If the JSON string needs to include line breaks, format it according to standard JSON specifications.
        # >
        # > - For more information about template variable formatting, see [SMS template specifications](https://help.aliyun.com/document_detail/463161.html).
        self.template_param = template_param

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.out_id is not None:
            result['OutId'] = self.out_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.phone_numbers is not None:
            result['PhoneNumbers'] = self.phone_numbers

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sign_name is not None:
            result['SignName'] = self.sign_name

        if self.sms_up_extend_code is not None:
            result['SmsUpExtendCode'] = self.sms_up_extend_code

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        if self.template_param is not None:
            result['TemplateParam'] = self.template_param

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneNumbers') is not None:
            self.phone_numbers = m.get('PhoneNumbers')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')

        if m.get('SmsUpExtendCode') is not None:
            self.sms_up_extend_code = m.get('SmsUpExtendCode')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('TemplateParam') is not None:
            self.template_param = m.get('TemplateParam')

        return self

