# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRecordRequest(DaraModel):
    def __init__(
        self,
        begin_time: int = None,
        current_page: int = None,
        device_name: str = None,
        end_time: int = None,
        iot_id: str = None,
        iot_instance_id: str = None,
        need_snapshot: bool = None,
        page_size: int = None,
        product_key: str = None,
        record_type: int = None,
        stream_type: int = None,
    ):
        # The start time of the query range. The time is a 10-digit timestamp in seconds.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The number of the page to return. Default value: 1.
        self.current_page = current_page
        # The DeviceName of the IP camera. You can view the **DeviceName** on the **Devices** page in the IoT Platform console.
        # >Notice:  If you specify this parameter, you must also specify **ProductKey**.
        self.device_name = device_name
        # The end time of the query range. The time is a 10-digit timestamp in seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the IP camera. The ID is issued by IoT Platform and is the unique identifier of the device. You can call the [QueryDeviceDetail](https://help.aliyun.com/document_detail/69594.html) operation of IoT Platform to query the ID.
        # 
        # >Notice:  If you specify this parameter, you do not need to specify **ProductKey** or **DeviceName**. The **IotId** is the unique identifier of the device and corresponds to the combination of **ProductKey** and **DeviceName**. If you specify both **IotId** and the combination of **ProductKey** and **DeviceName**, **IotId** takes precedence.
        self.iot_id = iot_id
        # The instance ID. You can view the ID of the current instance on the **Overview** tab in the IoT Platform console.
        # 
        # >Notice: 
        # - If your instance has an ID, you must specify the **ID**. Otherwise, the call fails.
        # - If your instance does not have an ID, you do not need to specify this parameter.
        # 
        # 
        # 
        # For more information about instances, see [Instance overview](https://help.aliyun.com/document_detail/356505.html).
        self.iot_instance_id = iot_instance_id
        # Specifies whether to return thumbnails. Valid values:
        # 
        # - **true**: yes.
        # - **false** (default): no.
        self.need_snapshot = need_snapshot
        # The number of entries to return on each page. Default value: 10. Maximum value: 50.
        self.page_size = page_size
        # The ProductKey of the product to which the IP camera belongs. You can view the ProductKey on the **Products** page in the IoT Platform console or call the [QueryProductList](https://help.aliyun.com/document_detail/69271.html) operation to query the information of all products under the current account.
        # >Notice:  If you specify this parameter, you must also specify **DeviceName**.
        self.product_key = product_key
        # The recording type. Valid values:
        # 
        # - **0**: continuous recording.
        # - **1**: intelligent alert event recording.
        # - **2** (default): manual recording.
        # 
        # If this parameter is left empty, all recording types are returned.
        self.record_type = record_type
        # The stream type. Valid values:
        # - **0** (default): main stream.
        # - **1**: sub stream.
        self.stream_type = stream_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.iot_id is not None:
            result['IotId'] = self.iot_id

        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id

        if self.need_snapshot is not None:
            result['NeedSnapshot'] = self.need_snapshot

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_key is not None:
            result['ProductKey'] = self.product_key

        if self.record_type is not None:
            result['RecordType'] = self.record_type

        if self.stream_type is not None:
            result['StreamType'] = self.stream_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')

        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')

        if m.get('NeedSnapshot') is not None:
            self.need_snapshot = m.get('NeedSnapshot')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')

        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')

        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')

        return self

