# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyImageSharePermissionRequest(DaraModel):
    def __init__(
        self,
        add_accounts: str = None,
        image_id: str = None,
        remove_accounts: str = None,
    ):
        # The ID of the Alibaba Cloud account with which you want to share the image. You can specify multiple Alibaba Cloud IDs. Separate multiple IDs with commas (,).
        self.add_accounts = add_accounts
        # The ID of the image. You can specify only one image ID. Custom images and public images are supported.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The ID of the Alibaba Cloud account from which you want to unshare the image. You can specify only one Alibaba Cloud account ID.
        self.remove_accounts = remove_accounts

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_accounts is not None:
            result['AddAccounts'] = self.add_accounts

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.remove_accounts is not None:
            result['RemoveAccounts'] = self.remove_accounts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddAccounts') is not None:
            self.add_accounts = m.get('AddAccounts')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('RemoveAccounts') is not None:
            self.remove_accounts = m.get('RemoveAccounts')

        return self

