# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dysmsapi20170525 import models as main_models
from darabonba.model import DaraModel

class QuerySmsAuthorizationLetterResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[main_models.QuerySmsAuthorizationLetterResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QuerySmsAuthorizationLetterResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QuerySmsAuthorizationLetterResponseBodyData(DaraModel):
    def __init__(
        self,
        authorization: str = None,
        authorization_letter_exp_date: str = None,
        authorization_letter_id: int = None,
        authorization_letter_name: str = None,
        authorization_letter_pic: str = None,
        organization_code: str = None,
        proxy_authorization: str = None,
        sign_scope: str = None,
        state: str = None,
        status: str = None,
    ):
        # 委托授权方
        self.authorization = authorization
        # 委托授权书有效期
        self.authorization_letter_exp_date = authorization_letter_exp_date
        # 委托授权书id
        self.authorization_letter_id = authorization_letter_id
        # 委托授权书命名
        self.authorization_letter_name = authorization_letter_name
        # 委托授权书图片地址
        self.authorization_letter_pic = authorization_letter_pic
        # 授权方统一社会信用代码
        self.organization_code = organization_code
        # 被委托授权方
        self.proxy_authorization = proxy_authorization
        # 委托授权签名范围
        self.sign_scope = sign_scope
        # 委托授权书审核状态（初始化INT/审核通过PASSED）
        self.state = state
        # 委托授权书可用状态（可用VALID/不可用INVALID）
        self.status = status

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

        if self.authorization_letter_id is not None:
            result['AuthorizationLetterId'] = self.authorization_letter_id

        if self.authorization_letter_name is not None:
            result['AuthorizationLetterName'] = self.authorization_letter_name

        if self.authorization_letter_pic is not None:
            result['AuthorizationLetterPic'] = self.authorization_letter_pic

        if self.organization_code is not None:
            result['OrganizationCode'] = self.organization_code

        if self.proxy_authorization is not None:
            result['ProxyAuthorization'] = self.proxy_authorization

        if self.sign_scope is not None:
            result['SignScope'] = self.sign_scope

        if self.state is not None:
            result['State'] = self.state

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')

        if m.get('AuthorizationLetterExpDate') is not None:
            self.authorization_letter_exp_date = m.get('AuthorizationLetterExpDate')

        if m.get('AuthorizationLetterId') is not None:
            self.authorization_letter_id = m.get('AuthorizationLetterId')

        if m.get('AuthorizationLetterName') is not None:
            self.authorization_letter_name = m.get('AuthorizationLetterName')

        if m.get('AuthorizationLetterPic') is not None:
            self.authorization_letter_pic = m.get('AuthorizationLetterPic')

        if m.get('OrganizationCode') is not None:
            self.organization_code = m.get('OrganizationCode')

        if m.get('ProxyAuthorization') is not None:
            self.proxy_authorization = m.get('ProxyAuthorization')

        if m.get('SignScope') is not None:
            self.sign_scope = m.get('SignScope')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

