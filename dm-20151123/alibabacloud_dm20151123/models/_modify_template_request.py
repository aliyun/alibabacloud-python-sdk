# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyTemplateRequest(DaraModel):
    def __init__(
        self,
        from_type: int = None,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sms_content: str = None,
        sms_type: int = None,
        template_id: int = None,
        template_name: str = None,
        template_nick_name: str = None,
        template_subject: str = None,
        template_text: str = None,
    ):
        # The source channel through which the user accesses the service. Default value: 1. Valid values:
        # 
        # - 1: Direct access through Alibaba Cloud.
        # - 2: Access through a partner channel.
        self.from_type = from_type
        self.owner_id = owner_id
        # The remarks or application description for the SMS template. This parameter is required only when the templatetype is SMS. Maximum length: 100 characters.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The body content of the SMS template. This parameter is required only when the templatetype is SMS. Length: 2 to 400 characters.
        self.sms_content = sms_content
        # The business type of the SMS template. This parameter is required only when the templatetype is SMS. Valid values:
        # 
        # - 0: verification code
        # - 2: notification or promotion.
        self.sms_type = sms_type
        # The template ID.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The template name. Maximum length: 30 characters.
        # 
        # This parameter is required.
        self.template_name = template_name
        # The nickname of the template or the alias of the sender. This parameter is required only when the templatetype is email. Maximum length: 30 characters.
        self.template_nick_name = template_nick_name
        # The subject of the email template. This parameter is required only when the templatetype is email. Maximum length: 256 characters.
        self.template_subject = template_subject
        # The body content of the email. This parameter is required only when the templatetype is email. Maximum size: 1 MB.
        self.template_text = template_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_type is not None:
            result['FromType'] = self.from_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sms_content is not None:
            result['SmsContent'] = self.sms_content

        if self.sms_type is not None:
            result['SmsType'] = self.sms_type

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_nick_name is not None:
            result['TemplateNickName'] = self.template_nick_name

        if self.template_subject is not None:
            result['TemplateSubject'] = self.template_subject

        if self.template_text is not None:
            result['TemplateText'] = self.template_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromType') is not None:
            self.from_type = m.get('FromType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SmsContent') is not None:
            self.sms_content = m.get('SmsContent')

        if m.get('SmsType') is not None:
            self.sms_type = m.get('SmsType')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateNickName') is not None:
            self.template_nick_name = m.get('TemplateNickName')

        if m.get('TemplateSubject') is not None:
            self.template_subject = m.get('TemplateSubject')

        if m.get('TemplateText') is not None:
            self.template_text = m.get('TemplateText')

        return self

