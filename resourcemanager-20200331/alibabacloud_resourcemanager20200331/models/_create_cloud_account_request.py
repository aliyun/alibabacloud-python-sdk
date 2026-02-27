# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCloudAccountRequest(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        email: str = None,
        parent_folder_id: str = None,
        payer_account_id: str = None,
    ):
        # The display name of the member account.
        # 
        # The name must be 2 to 50 characters in length and can contain letters, digits, underscores (_), periods (.), and hyphens (-).
        # 
        # The name must be unique in the current resource directory.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The email address used to log on to the cloud account.
        # 
        # This parameter is required.
        self.email = email
        # The ID of the parent folder.
        self.parent_folder_id = parent_folder_id
        # The ID of the settlement account. If you do not specify this parameter, the current account is used for settlement.
        self.payer_account_id = payer_account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.email is not None:
            result['Email'] = self.email

        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id

        if self.payer_account_id is not None:
            result['PayerAccountId'] = self.payer_account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')

        if m.get('PayerAccountId') is not None:
            self.payer_account_id = m.get('PayerAccountId')

        return self

