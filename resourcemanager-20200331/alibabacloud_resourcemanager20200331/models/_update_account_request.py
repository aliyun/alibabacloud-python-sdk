# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAccountRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        new_account_type: str = None,
        new_display_name: str = None,
    ):
        # The ID of the Alibaba Cloud account that corresponds to the member.
        # 
        # This parameter is required.
        self.account_id = account_id
        # The new type of the member. Valid values:
        # 
        # *   ResourceAccount: resource account
        # *   CloudAccount: cloud account
        # 
        # >  You can configure either the `NewDisplayName` or `NewAccountType` parameter.
        self.new_account_type = new_account_type
        # The new display name of the member.
        # 
        # >  You can configure either the `NewDisplayName` or `NewAccountType` parameter.
        self.new_display_name = new_display_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.new_account_type is not None:
            result['NewAccountType'] = self.new_account_type

        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('NewAccountType') is not None:
            self.new_account_type = m.get('NewAccountType')

        if m.get('NewDisplayName') is not None:
            self.new_display_name = m.get('NewDisplayName')

        return self

