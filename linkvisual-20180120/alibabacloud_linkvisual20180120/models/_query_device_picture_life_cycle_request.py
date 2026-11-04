# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDevicePictureLifeCycleRequest(DaraModel):
    def __init__(
        self,
        iot_id: str = None,
    ):
        # The ID of the IPC device. The ID is issued by IoT Platform and uniquely identifies the device. You can call the IoT Platform [QueryDeviceDetail](https://help.aliyun.com/document_detail/69594.html) operation to query the ID.
        # 
        # This parameter is required.
        self.iot_id = iot_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.iot_id is not None:
            result['IotId'] = self.iot_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')

        return self

