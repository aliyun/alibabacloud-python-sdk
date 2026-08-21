# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetAppPlayKeyRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        owner_id: int = None,
        play_key: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The application ID. Default value: **app-1000000**. For more information, see [Multi-application](https://help.aliyun.com/document_detail/113600.html).
        self.app_id = app_id
        self.owner_id = owner_id
        # The playback key.
        # - Only uppercase letters, lowercase letters, and digits are supported. The length must be 8 to 20 characters.
        # - UTF-8 encoding.
        self.play_key = play_key
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.play_key is not None:
            result['PlayKey'] = self.play_key

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PlayKey') is not None:
            self.play_key = m.get('PlayKey')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

