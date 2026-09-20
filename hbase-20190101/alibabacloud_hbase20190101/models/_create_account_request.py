# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAccountRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_password: str = None,
        cluster_id: str = None,
    ):
        # The account name. The name must meet the following requirements:
        # 
        # * Starts with a lowercase letter and ends with a letter or digit.
        # * Contains only lowercase letters, digits, or underscores.
        # * Is 2 to 16 characters in length.
        # * Cannot be a reserved username such as root or admin.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The password of the database account. The password must meet the following requirements:
        # - Contains at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # - The supported special characters are `!@#$%^&*()_+-=`.
        # - Is 8 to 32 characters in length.
        # 
        # This parameter is required.
        self.account_password = account_password
        # The instance ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_password is not None:
            result['AccountPassword'] = self.account_password

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        return self

