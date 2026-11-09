# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryMqttTraceMessageOfClientRequest(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        client_id: str = None,
        current_page: int = None,
        end_time: int = None,
        instance_id: str = None,
        mqtt_region_id: str = None,
        page_size: int = None,
        reverse: bool = None,
    ):
        # The beginning of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The client ID of the device whose messages you want to query.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The number of the page to return. Pages start from page 1. If the input parameter value is greater than the total number of pages, the returned result is empty.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The end of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can view the instance ID in the **Basic Information** section of the **Instance Details** page that corresponds to the instance in the ApsaraMQ for MQTT console.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the region where the ApsaraMQ for MQTT instance resides. For more information, see [Endpoints](https://help.aliyun.com/document_detail/181438.html).
        # 
        # This parameter is required.
        self.mqtt_region_id = mqtt_region_id
        # The number of entries to return on each page. Valid values: 1 to 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Specifies whether the returned results are displayed in reverse chronological order. Valid values:
        # 
        # *   **true**: The returned results are displayed in reverse order of the time when messages are sent or received. This means that the latest sent or received message is displayed as the first entry and the earliest sent or received message is displayed as the last entry.
        # *   **false**: The returned results are displayed in order of the time when messages are sent or received. This means that the earliest sent or received message is displayed as the first entry and the latest sent or received message is displayed as the last entry.
        # 
        # If this parameter is not specified, the returned results are displayed in order of the time when messages are sent or received.
        self.reverse = reverse

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.mqtt_region_id is not None:
            result['MqttRegionId'] = self.mqtt_region_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.reverse is not None:
            result['Reverse'] = self.reverse

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MqttRegionId') is not None:
            self.mqtt_region_id = m.get('MqttRegionId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')

        return self

