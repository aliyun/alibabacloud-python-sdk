# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserDeviceWorkloadTrendRequest(DaraModel):
    def __init__(
        self,
        device_tag: str = None,
        from_: int = None,
        to: int = None,
        workload_type: str = None,
    ):
        # The endpoint device ID. You can obtain this value from the following operations:
        # - [GetUserDevice](~~GetUserDevice~~): Queries the details of a user endpoint device.
        # - [ListUserDevices](~~ListUserDevices~~): Queries user endpoint devices in batches.
        # 
        # This parameter is required.
        self.device_tag = device_tag
        # The start time of the query time range. This value is a UNIX timestamp in seconds. The value must be greater than or equal to 0 and less than the value of To.
        # 
        # This parameter is required.
        self.from_ = from_
        # The end time of the query time range. This value is a UNIX timestamp in seconds. The value must be greater than the value of From.
        # 
        # This parameter is required.
        self.to = to
        # The workload type. Valid values:
        # - **cpu**: CPU usage.
        # - **mem**: memory usage.
        # 
        # This parameter is required.
        self.workload_type = workload_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_tag is not None:
            result['DeviceTag'] = self.device_tag

        if self.from_ is not None:
            result['From'] = self.from_

        if self.to is not None:
            result['To'] = self.to

        if self.workload_type is not None:
            result['WorkloadType'] = self.workload_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceTag') is not None:
            self.device_tag = m.get('DeviceTag')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('To') is not None:
            self.to = m.get('To')

        if m.get('WorkloadType') is not None:
            self.workload_type = m.get('WorkloadType')

        return self

