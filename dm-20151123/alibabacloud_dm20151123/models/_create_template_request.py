# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTemplateRequest(DaraModel):
    def __init__(
        self,
        from_type: int = None,
        owner_id: int = None,
        remark: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sms_content: str = None,
        sms_type: int = None,
        template_name: str = None,
        template_nick_name: str = None,
        template_subject: str = None,
        template_text: str = None,
        template_type: int = None,
    ):
        # Deprecated. This parameter is retained for backward compatibility.
        self.from_type = from_type
        self.owner_id = owner_id
        # Deprecated. This parameter is retained for backward compatibility.
        self.remark = remark
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Deprecated. This parameter is retained for backward compatibility.
        self.sms_content = sms_content
        # Deprecated. This parameter is retained for backward compatibility.
        self.sms_type = sms_type
        # The template name.
        # 
        # This parameter is required.
        self.template_name = template_name
        # The sender name.
        self.template_nick_name = template_nick_name
        # The email subject.
        self.template_subject = template_subject
        # The email HTML body.
        self.template_text = template_text
        # The template type.
        self.template_type = template_type

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

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_nick_name is not None:
            result['TemplateNickName'] = self.template_nick_name

        if self.template_subject is not None:
            result['TemplateSubject'] = self.template_subject

        if self.template_text is not None:
            result['TemplateText'] = self.template_text

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

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

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateNickName') is not None:
            self.template_nick_name = m.get('TemplateNickName')

        if m.get('TemplateSubject') is not None:
            self.template_subject = m.get('TemplateSubject')

        if m.get('TemplateText') is not None:
            self.template_text = m.get('TemplateText')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

