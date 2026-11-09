# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryMqttTraceMessagePublishRequest(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        instance_id: str = None,
        mqtt_region_id: str = None,
        msg_id: str = None,
    ):
        # The beginning of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The end of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can view the instance ID in the **Basic Information** section on the **Instance Details** page that corresponds to the instance in the ApsaraMQ for MQTT console.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region where the ApsaraMQ for MQTT instance resides. For more information, see [Endpoints](https://help.aliyun.com/document_detail/181438.html).
        # 
        # This parameter is required.
        self.mqtt_region_id = mqtt_region_id
        # The message ID.
        # 
        # This parameter is required.
        self.msg_id = msg_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mqtt_region_id is not None:
            result['MqttRegionId'] = self.mqtt_region_id

        if self.msg_id is not None:
            result['MsgId'] = self.msg_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MqttRegionId') is not None:
            self.mqtt_region_id = m.get('MqttRegionId')

        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')

        return self

