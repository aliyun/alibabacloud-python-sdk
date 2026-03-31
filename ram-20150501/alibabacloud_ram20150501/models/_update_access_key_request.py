# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAccessKeyRequest(DaraModel):
    def __init__(
        self,
        status: str = None,
        user_access_key_id: str = None,
        user_name: str = None,
    ):
        # The status of the AccessKey pair. Valid values: `Active` and `Inactive`.
        self.status = status
        # The AccessKey ID in the AccessKey pair whose status you want to change.``
        self.user_access_key_id = user_access_key_id
        # The name of the RAM user.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        if self.user_access_key_id is not None:
            result['UserAccessKeyId'] = self.user_access_key_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserAccessKeyId') is not None:
            self.user_access_key_id = m.get('UserAccessKeyId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

