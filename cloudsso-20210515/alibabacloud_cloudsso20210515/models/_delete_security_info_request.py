# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSecurityInfoRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        user_id: str = None,
        verify_type: str = None,
    ):
        # The directory ID.
        # 
        # This parameter is required.
        self.directory_id = directory_id
        # The user ID.
        # 
        # This parameter is required.
        self.user_id = user_id
        # The verification type of the security information. Valid values:
        # 
        # - SecurityEmail: security email address.
        # 
        # This parameter is required.
        self.verify_type = verify_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.verify_type is not None:
            result['VerifyType'] = self.verify_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('VerifyType') is not None:
            self.verify_type = m.get('VerifyType')

        return self

