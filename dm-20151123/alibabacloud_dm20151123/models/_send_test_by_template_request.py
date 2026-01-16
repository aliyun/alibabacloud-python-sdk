# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendTestByTemplateRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        birthday: str = None,
        email: str = None,
        gender: str = None,
        mobile: str = None,
        nick_name: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        template_id: int = None,
        template_params: str = None,
        user_name: str = None,
    ):
        # Sender address, with a maximum length of 60 characters
        # 
        # This parameter is required.
        self.account_name = account_name
        # Birthday, with a maximum length of 30 characters
        self.birthday = birthday
        # Recipient address, with a maximum length of 60 characters
        # 
        # This parameter is required.
        self.email = email
        # Gender, with a maximum length of 30 characters
        self.gender = gender
        # Mobile, with a maximum length of 30 characters
        self.mobile = mobile
        # NickName, with a maximum length of 30 characters
        self.nick_name = nick_name
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Template ID
        # 
        # This parameter is required.
        self.template_id = template_id
        self.template_params = template_params
        # UserName, with a maximum length of 30 characters
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.birthday is not None:
            result['Birthday'] = self.birthday

        if self.email is not None:
            result['Email'] = self.email

        if self.gender is not None:
            result['Gender'] = self.gender

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_params is not None:
            result['TemplateParams'] = self.template_params

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('Birthday') is not None:
            self.birthday = m.get('Birthday')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Gender') is not None:
            self.gender = m.get('Gender')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateParams') is not None:
            self.template_params = m.get('TemplateParams')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

