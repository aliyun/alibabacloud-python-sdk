# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListVccFlowInfosRequest(DaraModel):
    def __init__(
        self,
        direction: str = None,
        from_: int = None,
        metric_name: str = None,
        region_id: str = None,
        to: int = None,
        vcc_id: str = None,
    ):
        # Direction
        # 
        # Valid value:
        # 
        # *   IN: inbound.
        # *   OUT: the outbound.
        self.direction = direction
        # The start time. The default value is 5 minutes ago.
        self.from_ = from_
        # Metric
        # 
        # Valid value:
        # 
        # *   totalPacketsRate: Total Packet Rate.
        # *   dropBytesRate: the of the stream drop rate.
        # *   dropPacketsRate: Dropped Packet Rate.
        # *   totalBytesRate: the total streaming rate.
        # *   passBytesRate: by stream rate.
        # *   passPacketsRate: by packet rate.
        self.metric_name = metric_name
        # The region ID.
        self.region_id = region_id
        # The end time. The default time is the current time.
        self.to = to
        # Lingjun Connection ID
        self.vcc_id = vcc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direction is not None:
            result['Direction'] = self.direction

        if self.from_ is not None:
            result['From'] = self.from_

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.to is not None:
            result['To'] = self.to

        if self.vcc_id is not None:
            result['VccId'] = self.vcc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('To') is not None:
            self.to = m.get('To')

        if m.get('VccId') is not None:
            self.vcc_id = m.get('VccId')

        return self

