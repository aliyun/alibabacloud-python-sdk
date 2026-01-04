# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBandwitdhByInternetChargeTypeResponseBody(DaraModel):
    def __init__(
        self,
        bandwidth_value: int = None,
        internet_charge_type: str = None,
        request_id: str = None,
        time_stamp: str = None,
    ):
        # The bandwidth. Unit: bit/s.
        self.bandwidth_value = bandwidth_value
        # The metering method. Valid values:
        # 
        # *   BandwidthByDay: Pay by daily peak bandwidth
        # *   95BandwidthByMonth: Pay by monthly 95th percentile bandwidth
        # *   PayByBandwidth4thMonth: Pay by monthly fourth peak bandwidth
        # *   PayByBandwidth: Pay by fixed bandwidth
        # 
        # You can specify only one metering method for network usage and cannot overwrite the existing metering method.
        self.internet_charge_type = internet_charge_type
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use the ID to troubleshoot issues.
        self.request_id = request_id
        # The timestamp. The time follows the ISO 8601 standard. The time is displayed in UTC. Example: 2016-10-20T04:00:00Z.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth_value is not None:
            result['BandwidthValue'] = self.bandwidth_value

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BandwidthValue') is not None:
            self.bandwidth_value = m.get('BandwidthValue')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

