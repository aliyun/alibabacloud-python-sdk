# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVodStorageDataRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        end_time: str = None,
        owner_id: int = None,
        region: str = None,
        start_time: str = None,
        storage: str = None,
        storage_type: str = None,
    ):
        # The application ID. If you have activated the multi-application feature, you can specify this parameter to query the storage usage of a specific application. If you do not specify this parameter, the total storage usage of all applications is returned. You can obtain the value of this parameter from the AppId response parameter of the [CreateAppInfo](~~CreateAppInfo~~) operation. For more information, see [Multi-application](https://help.aliyun.com/document_detail/113601.html).
        self.app_id = app_id
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        # 
        # This parameter is required.
        self.end_time = end_time
        self.owner_id = owner_id
        # The storage region. By default, data of all regions is returned. You can specify multiple regions separated by commas (,). Valid values:
        # 
        # - **cn-shanghai**: Shanghai.
        # - **cn-beijing**: Beijing.
        # - **eu-central-1**: Germany.
        # - **ap-southeast-1**: Singapore.
        self.region = region
        # The start of the time range to query. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        # 
        # This parameter is required.
        self.start_time = start_time
        # The storage name (Alibaba Cloud OSS bucket name). By default, data of all storage buckets is returned. You can specify multiple storage names separated by commas (,).
        self.storage = storage
        # The storage type. Set the value to **OSS**.
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region is not None:
            result['Region'] = self.region

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.storage is not None:
            result['Storage'] = self.storage

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Storage') is not None:
            self.storage = m.get('Storage')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

