# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDedicatedBlockStorageClusterInventoryDataRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dbsc_id: str = None,
        end_time: int = None,
        period: int = None,
        region_id: str = None,
        start_time: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests.
        # 
        # The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure idempotence ](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The ID of the dedicated block storage cluster.
        # 
        # This parameter is required.
        self.dbsc_id = dbsc_id
        # End timestamp of trend data.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The time interval (seconds) between data retrieval points.
        # 
        # This parameter is required.
        self.period = period
        # The region ID of the dedicated block storage cluster.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Start timestamp of trend data.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbsc_id is not None:
            result['DbscId'] = self.dbsc_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.period is not None:
            result['Period'] = self.period

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DbscId') is not None:
            self.dbsc_id = m.get('DbscId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

