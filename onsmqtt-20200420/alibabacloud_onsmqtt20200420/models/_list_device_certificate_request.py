# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDeviceCertificateRequest(DaraModel):
    def __init__(
        self,
        mqtt_instance_id: str = None,
        page_no: str = None,
        page_size: str = None,
    ):
        # The instance ID of the Cloud Message Queue MQTT version, indicating which instance\\"s device certificates need to be viewed.
        # 
        # This parameter is required.
        self.mqtt_instance_id = mqtt_instance_id
        # Indicates which page of the results to return. The starting page is counted from 1.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The maximum number of query records to display per page. Value range: 1 to 100.
        # 
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

