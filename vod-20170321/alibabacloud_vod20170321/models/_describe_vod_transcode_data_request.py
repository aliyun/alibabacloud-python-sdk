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
        # The application ID. If you specify this parameter, transcoding usage data for the specified application is returned. By default, transcoding usage data for all applications is returned. You can obtain the value of this parameter from the AppId response parameter of the [CreateAppInfo](~~CreateAppInfo~~) operation.
        self.app_id = app_id
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        # 
        # This parameter is required.
        self.end_time = end_time
        # The time granularity. Valid values:
        # 
        # - **day**: day.
        # - **hour**: hour.
        self.interval = interval
        self.owner_id = owner_id
        # The storage region. By default, data for all regions is returned. You can specify multiple regions separated by commas (,). Valid values:
        # - **cn-shanghai**: Shanghai.
        # - **cn-beijing**: Beijing.
        # - **eu-central-1**: Germany.
        # - **ap-southeast-1**: Singapore.
        self.region = region
        # The transcoding specification. By default, data for all transcoding specifications is returned. You can specify multiple specifications separated by commas (,). Valid values:
        # - **Audio**: audio-only.
        # - **Segmentation**: container format conversion.
        # - **H264.LD**, **H264.SD**, **H264.HD**, **H264.2K**, **H264.4K**, and more.
        self.specification = specification
        # The start of the time range to query. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        # 
        # This parameter is required.
        self.start_time = start_time
        # The storage name (Alibaba Cloud OSS bucket name). By default, data for all storage locations is returned. You can specify multiple storage names separated by commas (,).
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

