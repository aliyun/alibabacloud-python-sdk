# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAccountPasswordRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        cluster_id: str = None,
        new_account_password: str = None,
    ):
        # The name of the account.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The ID of target instance. You can call the DescribeInstances operation to obtain target instance ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The new password of the account. The password must meet the following requirements:
        # * Contains at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # * Is 8 to 32 characters in length.
        # * Special characters include `!@#$%^&*()_+-=`.
        # 
        # This parameter is required.
        self.new_account_password = new_account_password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.new_account_password is not None:
            result['NewAccountPassword'] = self.new_account_password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('NewAccountPassword') is not None:
            self.new_account_password = m.get('NewAccountPassword')

        return self

