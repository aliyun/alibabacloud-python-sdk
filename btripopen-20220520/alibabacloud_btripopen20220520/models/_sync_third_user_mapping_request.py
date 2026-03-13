# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SyncThirdUserMappingRequest(DaraModel):
    def __init__(
        self,
        status: int = None,
        third_channel_type: str = None,
        third_user_id: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.status = status
        # This parameter is required.
        self.third_channel_type = third_channel_type
        # This parameter is required.
        self.third_user_id = third_user_id
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['status'] = self.status

        if self.third_channel_type is not None:
            result['third_channel_type'] = self.third_channel_type

        if self.third_user_id is not None:
            result['third_user_id'] = self.third_user_id

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('third_channel_type') is not None:
            self.third_channel_type = m.get('third_channel_type')

        if m.get('third_user_id') is not None:
            self.third_user_id = m.get('third_user_id')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

