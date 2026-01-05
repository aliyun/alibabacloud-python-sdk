# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QuerySmsAuthorizationLetterRequest(DaraModel):
    def __init__(
        self,
        authorization_letter_id_list: List[int] = None,
        organization_code: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        sign_name: str = None,
        state: str = None,
        status: str = None,
    ):
        # 委托授权书id列表
        self.authorization_letter_id_list = authorization_letter_id_list
        # 授权方社会统一信用代码
        self.organization_code = organization_code
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 签名名称（支持命中签名范围查询）
        self.sign_name = sign_name
        # 授权书审核状态，INT:审核中，PASSED:审核通过
        self.state = state
        # 授权书可用状态，VALID可用，INVALID不可用
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization_letter_id_list is not None:
            result['AuthorizationLetterIdList'] = self.authorization_letter_id_list

        if self.organization_code is not None:
            result['OrganizationCode'] = self.organization_code

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.sign_name is not None:
            result['SignName'] = self.sign_name

        if self.state is not None:
            result['State'] = self.state

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationLetterIdList') is not None:
            self.authorization_letter_id_list = m.get('AuthorizationLetterIdList')

        if m.get('OrganizationCode') is not None:
            self.organization_code = m.get('OrganizationCode')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

