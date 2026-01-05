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
        # The extension field of the external record. The value is a string that contains no more than 256 characters.
        # 
        # > The parameter is optional.
        self.out_id = out_id
        self.owner_id = owner_id
        # The mobile number of the recipient. Format:
        # 
        # *   Message delivery to the Chinese mainland: +/+86/0086/86 or an 11-digit mobile number without a prefix. Example: 1590000\\*\\*\\*\\*.
        # *   Message delivery to countries or regions outside the Chinese mainland: Dialing code + Mobile number. Example: 852000012\\*\\*\\*\\*.
        # 
        # > We recommend that you call the SendSms operation to send verification codes.
        # 
        # This parameter is required.
        self.phone_number_json = phone_number_json
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The signature.
        # 
        # Log on to the Alibaba Cloud SMS console. In the left-side navigation pane, click **Go Globe** or **Go China**. You can view the signature in the **Signature** column on the **Signatures** tab.
        # 
        # > The signatures must be approved and correspond to the mobile numbers in sequence.
        # 
        # This parameter is required.
        self.sign_name_json = sign_name_json
        # The extension code of the MO message. Format: JSON array.
        # 
        # > The parameter is optional.
        self.sms_up_extend_code_json = sms_up_extend_code_json
        # The code of the message template.
        # 
        # Log on to the Alibaba Cloud SMS console. In the left-side navigation pane, click **Go Globe** or **Go China**. You can view the message template in the **Template Code** column on the **Message Templates** tab.
        # 
        # > The message templates must be created on the Go Globe page and approved.
        # 
        # This parameter is required.
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

