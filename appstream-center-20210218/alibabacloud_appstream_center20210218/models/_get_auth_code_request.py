# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAuthCodeRequest(DaraModel):
    def __init__(
        self,
        account_type: str = None,
        ad_domain: str = None,
        ad_password: str = None,
        auto_create_user: bool = None,
        end_user_id: str = None,
        external_user_id: str = None,
        policy: str = None,
        token_type: str = None,
    ):
        # The account type. Valid values: ad (enterprise AD account) and simple (convenience account).
        self.account_type = account_type
        # The Active Directory domain name. This parameter is required when the account type is ad.
        self.ad_domain = ad_domain
        # The password of the enterprise AD account.
        self.ad_password = ad_password
        # Specifies whether to synchronously create an EndUserId based on ExternalUserId. This parameter takes effect only when EndUserId is left empty.
        self.auto_create_user = auto_create_user
        # The username of the Wuying convenience account. The username must be unique within an Alibaba Cloud account. This parameter and ExternalUserId cannot be left empty at the same time.
        self.end_user_id = end_user_id
        # The external user ID. This ID is customized by the caller and must be unique within an Alibaba Cloud account. This parameter and ExternalUserId cannot be left empty at the same time.
        self.external_user_id = external_user_id
        # The access policy that restricts the access permissions of the authorization code. If this parameter is left empty, no restrictions are applied.
        # 
        # Syntax:
        # 
        # ```json
        # {
        #       "Version": "1",
        #       "Resource": {
        #             "Type": "<resource type>",
        #             "Id": "<resource ID>"
        #       }
        # }
        # ```
        # 
        # Valid values for <resource type>:
        # 
        # - AppInstanceGroup: app instance group. You can call the ListAppInstanceGroup operation to obtain the ID.
        # - AppInstance: app instance. This is a dedicated field.
        # - App: application. You can call the ListAppInstanceGroup operation to obtain the ID.
        self.policy = policy
        # The token type. Valid values: LoginToken (logon token) and StsToken (temporary identity credential).
        self.token_type = token_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.ad_domain is not None:
            result['AdDomain'] = self.ad_domain

        if self.ad_password is not None:
            result['AdPassword'] = self.ad_password

        if self.auto_create_user is not None:
            result['AutoCreateUser'] = self.auto_create_user

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.external_user_id is not None:
            result['ExternalUserId'] = self.external_user_id

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.token_type is not None:
            result['TokenType'] = self.token_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('AdDomain') is not None:
            self.ad_domain = m.get('AdDomain')

        if m.get('AdPassword') is not None:
            self.ad_password = m.get('AdPassword')

        if m.get('AutoCreateUser') is not None:
            self.auto_create_user = m.get('AutoCreateUser')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('ExternalUserId') is not None:
            self.external_user_id = m.get('ExternalUserId')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('TokenType') is not None:
            self.token_type = m.get('TokenType')

        return self

