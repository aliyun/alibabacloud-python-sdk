# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BindPictureSearchAppWithDevicesRequest(DaraModel):
    def __init__(
        self,
        app_instance_id: str = None,
        device_iot_ids: List[str] = None,
        iot_instance_id: str = None,
    ):
        # Instance ID of the image search application instance. You can call the [QueryPictureSearchApps](https://help.aliyun.com/document_detail/206608.html) operation to query instance ID.
        # 
        # This parameter is required.
        self.app_instance_id = app_instance_id
        # The list of device IoT IDs. You can specify the IoT IDs of V-series edge all-in-one devices or cameras.
        # 
        # An IoT ID is a unique identifier issued by IoT Platform for a device.
        # You can call the IoT Platform [QueryDeviceDetail](https://help.aliyun.com/document_detail/69594.html) operation to query the IoT ID.
        # 
        # You can specify up to 20 device IoT IDs in a single call.
        # 
        # This parameter is required.
        self.device_iot_ids = device_iot_ids
        # The instance ID.
        # 
        # - Enterprise Enterprise instance: You must specify this parameter. You can view the ID of your Enterprise Enterprise instance on the **Instance Overview** page in the IoT Platform console.
        # - Public instance: You do not need to specify this parameter.
        self.iot_instance_id = iot_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id

        if self.device_iot_ids is not None:
            result['DeviceIotIds'] = self.device_iot_ids

        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')

        if m.get('DeviceIotIds') is not None:
            self.device_iot_ids = m.get('DeviceIotIds')

        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')

        return self

