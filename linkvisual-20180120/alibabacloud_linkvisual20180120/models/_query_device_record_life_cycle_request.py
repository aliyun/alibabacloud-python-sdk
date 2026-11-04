# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QueryDeviceRecordLifeCycleRequest(DaraModel):
    def __init__(
        self,
        device_list: List[str] = None,
    ):
        # The list of IoT IDs of the IPC devices. An IoT ID is a unique identifier issued by IoT Platform for a device. You can call the IoT Platform [QueryDeviceDetail](https://help.aliyun.com/document_detail/69594.html) operation to query the IoT ID.
        # 
        # This parameter is required.
        self.device_list = device_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_list is not None:
            result['DeviceList'] = self.device_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceList') is not None:
            self.device_list = m.get('DeviceList')

        return self

