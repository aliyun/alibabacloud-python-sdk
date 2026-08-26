# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveRecordNotifyRecordsRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        end_time: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        start_time: str = None,
        status: str = None,
        storage_type: str = None,
        stream_name: str = None,
    ):
        # The name of the application to which the stream belongs.
        self.app_name = app_name
        # The streamer\\"s streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The end time. The end time must be later than the start time. Format: yyyy-MM-ddTHH:mm:ssZ (UTC).
        # 
        # This parameter is required.
        self.end_time = end_time
        self.owner_id = owner_id
        # The page number. Default value: 1. Valid values: 1 to 100000.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page. Default value: 20. Maximum value: 500. Valid values: any integer from 1 to 500.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The region ID.
        self.region_id = region_id
        # The start time. Format: yyyy-MM-ddTHH:mm:ssZ (UTC).
        # 
        # > You can query data within the last 7 days.
        # 
        # This parameter is required.
        self.start_time = start_time
        # Specifies whether the callback was successful. Valid values:
        # - success: The callback was successful.
        # - failed: The callback failed.
        self.status = status
        # The storage type of the recording for which to query callback records. Valid values:
        # 
        # - oss: recorded to OSS
        # 
        # - vod: recorded to ApsaraVideo VOD
        # 
        # - all: queries callback records for all storage types
        self.storage_type = storage_type
        # The stream name.
        self.stream_name = stream_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

