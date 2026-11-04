# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class TransferDeviceInstanceRequest(DaraModel):
    def __init__(
        self,
        device_name_list: List[str] = None,
        product_key: str = None,
        source_instance_id: str = None,
        target_instance_id: str = None,
    ):
        # The list of names of the devices to be transferred. You can specify up to 100 device names.
        # 
        # This parameter is required.
        self.device_name_list = device_name_list
        # The ProductKey of the product to which the devices belong. IoT Platform generates this unique identifier when the product is created.
        # 
        # This parameter is required.
        self.product_key = product_key
        # The ID of the source instance to which the devices belong:
        # 
        # - Public instance ID: iotx-oxssharez200.
        #     > Only the China (Shanghai) region is supported. Enterprise instance ID is iotx-oxssharez200.
        # 
        # - Enterprise Edition instance ID: Log on to the IoT Platform console. On the **Instance Overview** page, click Enterprise instance name. On the **Instance Details** page, view the **Instance ID** in the **Basic Information** section.
        self.source_instance_id = source_instance_id
        # The ID of the target instance to which the devices are transferred. Only Enterprise Edition instances are supported as target instances.
        # 
        # You can log on to the IoT Platform console. On the **Instance Overview** page, click the instance name. On the **Instance Details** page, view the **Instance ID** in the **Basic Information** section.
        # 
        # This parameter is required.
        self.target_instance_id = target_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_name_list is not None:
            result['DeviceNameList'] = self.device_name_list

        if self.product_key is not None:
            result['ProductKey'] = self.product_key

        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id

        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceNameList') is not None:
            self.device_name_list = m.get('DeviceNameList')

        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')

        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')

        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')

        return self

