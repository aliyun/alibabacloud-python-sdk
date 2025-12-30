# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddUserVpcAuthorizationRequest(DaraModel):
    def __init__(
        self,
        auth_channel: str = None,
        auth_code: str = None,
        auth_type: str = None,
        authorized_user_id: int = None,
    ):
        # The authorization channel. Valid values:
        # 
        # *   AUTH_CODE: A verification code is used for authorization.
        # *   RESOURCE_DIRECTORY: A resource directory is used for authorization.
        # 
        # Default value: AUTH_CODE.
        self.auth_channel = auth_channel
        # The verification code.
        # 
        # > 
        # 
        # *   The specified authentication code is used if the value of AuthChannel is left empty or is set to AUTH_CODE.
        # 
        # *   In other cases, a random 6-digit number is used. Example: 123456.
        self.auth_code = auth_code
        # The authorization scope. Valid values:
        # 
        # *   NORMAL: general authorization
        # *   CLOUD_PRODUCT: cloud service-related authorization
        self.auth_type = auth_type
        # The ID of the Alibaba Cloud account to which the permissions on the resources are granted.
        # 
        # >  You can set an effective scope across accounts only by using an Alibaba Cloud account instead of a RAM user. You can set an effective scope across accounts registered on the same site. For example, you can perform the operation across accounts that are both registered on the Alibaba Cloud China site or Alibaba Cloud international site. You cannot set an effective scope across accounts registered on different sites. For example, you cannot perform the operation across accounts that are separately registered on the Alibaba Cloud China site and Alibaba Cloud international site.
        # 
        # This parameter is required.
        self.authorized_user_id = authorized_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_channel is not None:
            result['AuthChannel'] = self.auth_channel

        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code

        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.authorized_user_id is not None:
            result['AuthorizedUserId'] = self.authorized_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthChannel') is not None:
            self.auth_channel = m.get('AuthChannel')

        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')

        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('AuthorizedUserId') is not None:
            self.authorized_user_id = m.get('AuthorizedUserId')

        return self

