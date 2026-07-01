# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendBatchSmsRequest(DaraModel):
    def __init__(
        self,
        out_id: str = None,
        owner_id: int = None,
        phone_number_json: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name_json: str = None,
        sms_up_extend_code_json: str = None,
        template_code: str = None,
        template_param_json: str = None,
    ):
        # An external business ID. It must be a string of fewer than 256 characters.
        # 
        # > You can leave this parameter empty if you have no special requirements.
        self.out_id = out_id
        self.owner_id = owner_id
        # The recipient phone numbers. Format:
        # 
        # - For domestic SMS: Phone numbers with or without a country code such as `+`, `+86`, `0086`, or `86`. Example: `1590000****`.
        # 
        # - For international SMS: The country code followed by the phone number. Example: `852000012****`.
        # 
        # > For time-sensitive messages like verification codes, use the [SendSms](https://help.aliyun.com/document_detail/419273.html) operation to send messages individually.
        # 
        # This parameter is required.
        self.phone_number_json = phone_number_json
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The signature names. The number of signatures must match the number of phone numbers.
        # 
        # You can call the [QuerySmsSignList](https://help.aliyun.com/document_detail/419282.html) operation or check the [Short Message Service console](https://dysms.console.aliyun.com/domestic/text/sign) to find approved signatures. You must use an approved signature.
        # 
        # > - The system uses the selected signature to send SMS messages.
        # 
        # This parameter is required.
        self.sign_name_json = sign_name_json
        # A JSON array of MO SMS extension codes.
        # 
        # > You can leave this parameter empty if you have no special requirements.
        self.sms_up_extend_code_json = sms_up_extend_code_json
        # The message template code. You cannot use templates for domestic SMS and international SMS interchangeably.
        # 
        # You can call the [QuerySmsTemplateList](https://help.aliyun.com/document_detail/419288.html) operation or check the [Short Message Service console](https://dysms.console.aliyun.com/domestic/text/template) to find approved template codes. You must use an approved template code.
        # 
        # This parameter is required.
        self.template_code = template_code
        # The actual values for the template variables. This parameter is required if the template contains variables.
        # 
        # > - The number of template variable sets must match the number of phone numbers and signatures. The elements in the PhoneNumberJson, SignNameJson, and TemplateParamJson arrays must correspond by index to ensure each message is sent with the correct signature and variable values.
        # >
        # > - If you need to include a line break in the JSON string, follow the standard JSON format.
        self.template_param_json = template_param_json

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

        if self.phone_number_json is not None:
            result['PhoneNumberJson'] = self.phone_number_json

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sign_name_json is not None:
            result['SignNameJson'] = self.sign_name_json

        if self.sms_up_extend_code_json is not None:
            result['SmsUpExtendCodeJson'] = self.sms_up_extend_code_json

        if self.template_code is not None:
            result['TemplateCode'] = self.template_code

        if self.template_param_json is not None:
            result['TemplateParamJson'] = self.template_param_json

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PhoneNumberJson') is not None:
            self.phone_number_json = m.get('PhoneNumberJson')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SignNameJson') is not None:
            self.sign_name_json = m.get('SignNameJson')

        if m.get('SmsUpExtendCodeJson') is not None:
            self.sms_up_extend_code_json = m.get('SmsUpExtendCodeJson')

        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')

        if m.get('TemplateParamJson') is not None:
            self.template_param_json = m.get('TemplateParamJson')

        return self

