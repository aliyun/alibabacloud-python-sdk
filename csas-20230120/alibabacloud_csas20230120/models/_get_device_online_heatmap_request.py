# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDeviceOnlineHeatmapRequest(DaraModel):
    def __init__(
        self,
        date: str = None,
        dev_tag: str = None,
        sase_user_id: str = None,
    ):
        # The date to query, in the format yyyyMMdd with a fixed length of 8 characters. Online data is retained for only 8 days. Dates beyond the retention period return an empty list.
        # 
        # This parameter is required.
        self.date = date
        # The terminal device ID.
        # 
        # This parameter is required.
        self.dev_tag = dev_tag
        # The user ID. You can obtain this value from the following operations:
        # - [ListUserDevices](~~ListUserDevices~~): Lists user terminal devices.
        # - [GetUserDevice](~~GetUserDevice~~): Queries the details of a user terminal device.
        # 
        # This parameter is required.
        self.sase_user_id = sase_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.dev_tag is not None:
            result['DevTag'] = self.dev_tag

        if self.sase_user_id is not None:
            result['SaseUserId'] = self.sase_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('DevTag') is not None:
            self.dev_tag = m.get('DevTag')

        if m.get('SaseUserId') is not None:
            self.sase_user_id = m.get('SaseUserId')

        return self

