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
        # The authorizing party, that is, the owner of the signature. Only the middle dot `·`, Chinese `【】（）`, English `()`, and spaces are supported. Other symbols or purely numeric input are not allowed. The length cannot exceed 150 characters.
        # 
        # This parameter is required.
        self.authorization = authorization
        # The validity period of the authorization letter. Format: `YYYY-MM-DD~YYYY-MM-DD`.
        # 
        # > The recommended validity period is 1 to 3 years. Set a reasonable time period and avoid making the validity period too long or too short.
        # 
        # This parameter is required.
        self.authorization_letter_exp_date = authorization_letter_exp_date
        # The name of the authorization letter. The name cannot be the same as any of your other authorization letters. Only Chinese characters, English characters, or a combination with numbers are supported. Symbols or purely numeric input are not allowed. The length cannot exceed 100 characters.
        # 
        # This parameter is required.
        self.authorization_letter_name = authorization_letter_name
        # The fileKey of the authorization letter.
        # 
        # 1. The authorization letter file uploaded to OSS. Download the [Authorization Letter Template](https://help-static-aliyun-doc.aliyuncs.com/file-manage-files/zh-CN/20250414/bvpcmo/%E6%8E%88%E6%9D%83%E5%A7%94%E6%89%98%E4%B9%A6%E6%A8%A1%E7%89%88.doc), then fill it out and stamp it according to the [specifications](https://help.aliyun.com/document_detail/56741.html) before uploading. File upload requirements:
        # - The name of the file to be uploaded cannot contain Chinese characters or special characters.
        # - Only images in JPG, PNG, GIF, or JPEG format are supported, and the image must not exceed 5 MB.
        # 
        # 2. To obtain the fileKey, see [Upload files through OSS](https://help.aliyun.com/document_detail/2833114.html).
        # 
        # This parameter is required.
        self.authorization_letter_pic = authorization_letter_pic
        # The unified social credit code of the authorizing party. The length cannot exceed 150 characters. The credit code must be consistent with the unified social credit code field in the qualification information bound to the signature. Otherwise, the signature creation will fail.
        # 
        # This parameter is required.
        self.organization_code = organization_code
        self.owner_id = owner_id
        # The authorized party, that is, the signature applicant. Only the middle dot `·`, Chinese `【】（）`, English `()`, and spaces are supported. Other symbols or purely numeric input are not allowed. The length cannot exceed 150 characters.
        # 
        # This parameter is required.
        self.proxy_authorization = proxy_authorization
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The list of authorized signatures. The number of signatures cannot exceed 100.
        # 
        # > We recommend that you authorize all signatures that may be used at once in the authorization letter. This prevents subsequent signature applications from falling outside the scope of the authorization letter, which would cause review failure and require you to supplement the authorization letter.
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

