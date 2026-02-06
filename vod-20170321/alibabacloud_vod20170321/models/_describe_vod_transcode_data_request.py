# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVodTranscodeDataRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        end_time: str = None,
        interval: str = None,
        owner_id: int = None,
        region: str = None,
        specification: str = None,
        start_time: str = None,
        storage: str = None,
    ):
        # The ID of the application. You can specify this parameter to query the transcoding statistics of a specific application. By default, the transcoding statistics of all applications is returned. You can obtain the application ID from the `AppId` parameter in the response to the [CreateAppInfo](~~CreateAppInfo~~) operation.
        self.app_id = app_id
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The interval at which you want to query data. Valid values:
        # 
        # *   **day**: days
        # *   **hour**: hours
        self.interval = interval
        self.owner_id = owner_id
        # The region in which you want to query data. If you leave this parameter empty, data in all regions is returned. Separate multiple regions with commas (,). Valid values:
        # 
        # *   **cn-shanghai**: China (Shanghai)
        # *   **cn-beijing**: China (Beijing)
        # *   **eu-central-1**: Germany (Frankfurt)
        # *   **ap-southeast-1**: Singapore
        self.region = region
        # The transcoding specification. If you leave this parameter empty, data of all transcoding specifications is returned. Separate multiple transcoding specifications with commas (,). Valid values:
        # 
        # *   **Audio**: audio transcoding
        # *   **Segmentation**: container format conversion
        # *   **H264.LD**, **H264.SD**, **H264.HD**, **H264.2K**, **H264.4K**, and more
        self.specification = specification
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The name of the Object Storage Service (OSS) bucket. If you leave this parameter empty, data of all buckets is returned. Separate multiple bucket names with commas (,).
        self.storage = storage

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

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region is not None:
            result['Region'] = self.region

        if self.specification is not None:
            result['Specification'] = self.specification

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.storage is not None:
            result['Storage'] = self.storage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Specification') is not None:
            self.specification = m.get('Specification')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Storage') is not None:
            self.storage = m.get('Storage')

        return self

