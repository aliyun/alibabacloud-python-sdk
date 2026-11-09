# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryMqttTraceDeviceRequest(DaraModel):
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
        # The beginning of the time range to query. Unit: milliseconds.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The client ID of the device whose trace information you want to query.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The number of the page to return. Pages start from page 1. If the value of this parameter exceeds the total number of pages, an empty result is returned.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The end of the time range to query. Unit: milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the ApsaraMQ for MQTT instance. This value must match the instance ID that the client actually uses. You can view the instance ID in the **Basic Information** area on the **Instance Details** page in the console.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the ApsaraMQ for MQTT instance. For more information, see [Endpoints](https://help.aliyun.com/document_detail/181438.html).
        # 
        # This parameter is required.
        self.mqtt_region_id = mqtt_region_id
        # The maximum number of MSMQ to display on each page for paging. Minimum value: 1. Maximum value: 100.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Specifies whether to display the results in reverse chronological order. Valid values:
        # 
        # - **true**: Results are displayed in reverse chronological order of device activity time. The most recent device activity is displayed first, and the earliest device activity is displayed last.
        # 
        # - **false**: Results are displayed in chronological order of device activity time. The earliest device activity is displayed first, and the most recent device activity is displayed last.
        # 
        # If this parameter is not specified, results are displayed in chronological order by default.
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

