# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteMFADeviceForUserRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        mfadevice_id: str = None,
        mfa_type: str = None,
        user_id: str = None,
    ):
        # The directory ID.
        self.directory_id = directory_id
        # The MFA device ID.
        # 
        # You can call [ListMFADevicesForUser](https://help.aliyun.com/document_detail/333531.html) to query the MFA device ID.
        self.mfadevice_id = mfadevice_id
        self.mfa_type = mfa_type
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.mfadevice_id is not None:
            result['MFADeviceId'] = self.mfadevice_id

        if self.mfa_type is not None:
            result['MfaType'] = self.mfa_type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('MFADeviceId') is not None:
            self.mfadevice_id = m.get('MFADeviceId')

        if m.get('MfaType') is not None:
            self.mfa_type = m.get('MfaType')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

