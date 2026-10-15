# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetResellerUserStatusRequest(DaraModel):
    def __init__(
        self,
        business_type: str = None,
        owner_id: str = None,
        status: str = None,
        stop_mode: str = None,
    ):
        # The type of business operation. Valid values:
        # FREEZE: Freeze operations.
        # TRUSTEESHIP: Hosting operations.
        # 
        # This parameter is required.
        self.business_type = business_type
        # This parameter is required.
        self.owner_id = owner_id
        # The status to set for the user account. Valid values:
        # Freeze: The user account is frozen.
        # Thaw: The user account is restored.
        # Trusteeship: The user account is hosted.
        # TrusteeshipCancel: The user account is not hosted.
        # 
        # This parameter is required.
        self.status = status
        # The stopping mode. Valid values:
        # 0: Normal shutdown.
        # 1: Immediate shutdown.
        self.stop_mode = stop_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_type is not None:
            result['BusinessType'] = self.business_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.status is not None:
            result['Status'] = self.status

        if self.stop_mode is not None:
            result['StopMode'] = self.stop_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StopMode') is not None:
            self.stop_mode = m.get('StopMode')

        return self

