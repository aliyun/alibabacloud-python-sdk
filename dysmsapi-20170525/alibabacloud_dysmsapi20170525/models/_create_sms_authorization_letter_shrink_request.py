# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSmsAuthorizationLetterShrinkRequest(DaraModel):
    def __init__(
        self,
        authorization: str = None,
        authorization_letter_exp_date: str = None,
        authorization_letter_name: str = None,
        authorization_letter_pic: str = None,
        organization_code: str = None,
        owner_id: int = None,
        proxy_authorization: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_list_shrink: str = None,
    ):
        # 授权方，授权方命名长度不超过1000个字符，暂不支持包含除中点（·）、空格、中文括号【】、英文括号()外的任何符号或纯数字输入
        # 
        # This parameter is required.
        self.authorization = authorization
        # 委托授权书有效期
        # 
        # This parameter is required.
        self.authorization_letter_exp_date = authorization_letter_exp_date
        # 委托授权书命名非空，不超过100个字符，支持中文、英文或与数字组合进行命名，暂不支持任何符号或纯数字输入
        # 
        # This parameter is required.
        self.authorization_letter_name = authorization_letter_name
        # 上传oss的委托授权书图片标识
        # 
        # This parameter is required.
        self.authorization_letter_pic = authorization_letter_pic
        # 授权方社会统一信用代码，长度不超过150个字符
        # 
        # This parameter is required.
        self.organization_code = organization_code
        self.owner_id = owner_id
        # 被授权方，被授权方命名长度不超过1000个字符，暂不支持包含除中点（·）、空格、中文括号【】、英文括号()外的任何符号或纯数字输入
        # 
        # This parameter is required.
        self.proxy_authorization = proxy_authorization
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 委托授权签名列表，签名数量限制100个以内
        # 
        # This parameter is required.
        self.sign_list_shrink = sign_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization is not None:
            result['Authorization'] = self.authorization

        if self.authorization_letter_exp_date is not None:
            result['AuthorizationLetterExpDate'] = self.authorization_letter_exp_date

        if self.authorization_letter_name is not None:
            result['AuthorizationLetterName'] = self.authorization_letter_name

        if self.authorization_letter_pic is not None:
            result['AuthorizationLetterPic'] = self.authorization_letter_pic

        if self.organization_code is not None:
            result['OrganizationCode'] = self.organization_code

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.proxy_authorization is not None:
            result['ProxyAuthorization'] = self.proxy_authorization

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sign_list_shrink is not None:
            result['SignList'] = self.sign_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')

        if m.get('AuthorizationLetterExpDate') is not None:
            self.authorization_letter_exp_date = m.get('AuthorizationLetterExpDate')

        if m.get('AuthorizationLetterName') is not None:
            self.authorization_letter_name = m.get('AuthorizationLetterName')

        if m.get('AuthorizationLetterPic') is not None:
            self.authorization_letter_pic = m.get('AuthorizationLetterPic')

        if m.get('OrganizationCode') is not None:
            self.organization_code = m.get('OrganizationCode')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProxyAuthorization') is not None:
            self.proxy_authorization = m.get('ProxyAuthorization')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SignList') is not None:
            self.sign_list_shrink = m.get('SignList')

        return self

