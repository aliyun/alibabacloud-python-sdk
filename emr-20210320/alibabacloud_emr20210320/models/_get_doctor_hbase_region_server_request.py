# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDoctorHBaseRegionServerRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        date_time: str = None,
        region_id: str = None,
        region_server_host: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The date.
        # 
        # This parameter is required.
        self.date_time = date_time
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The host of the region server.
        # 
        # This parameter is required.
        self.region_server_host = region_server_host

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.date_time is not None:
            result['DateTime'] = self.date_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.region_server_host is not None:
            result['RegionServerHost'] = self.region_server_host

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DateTime') is not None:
            self.date_time = m.get('DateTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionServerHost') is not None:
            self.region_server_host = m.get('RegionServerHost')

        return self

