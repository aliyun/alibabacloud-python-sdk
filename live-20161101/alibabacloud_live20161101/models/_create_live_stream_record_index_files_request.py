# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLiveStreamRecordIndexFilesRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        domain_name: str = None,
        end_time: str = None,
        end_time_included: bool = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        oss_object: str = None,
        owner_id: int = None,
        security_token: str = None,
        start_time: str = None,
        stream_name: str = None,
    ):
        # The name of the application to which the stream belongs. The AppName must match the AppName in the ingest URL for the template to take effect. To match all AppName values, set this parameter to *.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The streamer streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The end time of the index file. TS files uploaded before this time are included in the index file. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        # 
        # This parameter is required.
        self.end_time = end_time
        # Specifies whether to include the end time. If you set this parameter to true, the system attempts to include one additional TS file so that the created index file fully covers the period between StartTime and EndTime.
        self.end_time_included = end_time_included
        # The name of the OSS bucket.
        # 
        # This parameter is required.
        self.oss_bucket = oss_bucket
        # The endpoint of the OSS bucket.
        # 
        # This parameter is required.
        self.oss_endpoint = oss_endpoint
        # The name of the recording file stored in OSS.
        # 
        # This parameter is required.
        self.oss_object = oss_object
        self.owner_id = owner_id
        self.security_token = security_token
        # The start time of the index file. TS files uploaded after this time are included in the index file. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        # 
        # This parameter is required.
        self.start_time = start_time
        # The stream name. The StreamName must match the StreamName in the ingest URL for the template to take effect. To match all StreamName values, set this parameter to *.
        # 
        # The stream must have had actual stream ingest activity under the specified DomainName and AppName. Otherwise, the InvalidStream.NotFound error is returned.
        # 
        # This parameter is required.
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

        if self.end_time_included is not None:
            result['EndTimeIncluded'] = self.end_time_included

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint

        if self.oss_object is not None:
            result['OssObject'] = self.oss_object

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.start_time is not None:
            result['StartTime'] = self.start_time

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

        if m.get('EndTimeIncluded') is not None:
            self.end_time_included = m.get('EndTimeIncluded')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')

        if m.get('OssObject') is not None:
            self.oss_object = m.get('OssObject')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        return self

