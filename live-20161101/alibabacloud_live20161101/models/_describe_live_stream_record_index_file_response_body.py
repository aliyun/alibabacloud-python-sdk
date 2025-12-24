# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveStreamRecordIndexFileResponseBody(DaraModel):
    def __init__(
        self,
        record_index_info: main_models.DescribeLiveStreamRecordIndexFileResponseBodyRecordIndexInfo = None,
        request_id: str = None,
    ):
        # The information about the index file.
        self.record_index_info = record_index_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.record_index_info:
            self.record_index_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.record_index_info is not None:
            result['RecordIndexInfo'] = self.record_index_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecordIndexInfo') is not None:
            temp_model = main_models.DescribeLiveStreamRecordIndexFileResponseBodyRecordIndexInfo()
            self.record_index_info = temp_model.from_map(m.get('RecordIndexInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLiveStreamRecordIndexFileResponseBodyRecordIndexInfo(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        create_time: str = None,
        domain_name: str = None,
        duration: float = None,
        end_time: str = None,
        format: str = None,
        height: int = None,
        oss_bucket: str = None,
        oss_endpoint: str = None,
        oss_object: str = None,
        record_id: str = None,
        record_url: str = None,
        start_time: str = None,
        stream_name: str = None,
        width: int = None,
    ):
        # The name of the application to which the live stream belongs.
        self.app_name = app_name
        # The time when the index file was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.create_time = create_time
        # The main streaming domain.
        self.domain_name = domain_name
        # The recording length. Unit: seconds.
        self.duration = duration
        # The end time of the index file. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.end_time = end_time
        # The video format.
        self.format = format
        # The video height.
        self.height = height
        # The name of the Object Storage Service (OSS) bucket.
        self.oss_bucket = oss_bucket
        # The endpoint of the OSS bucket.
        self.oss_endpoint = oss_endpoint
        # The name of the storage file in OSS.
        self.oss_object = oss_object
        # The ID of the index file.
        self.record_id = record_id
        # The URL of the index file.
        self.record_url = record_url
        # The start time of the index file. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.start_time = start_time
        # The name of the live stream.
        self.stream_name = stream_name
        # The video width.
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.format is not None:
            result['Format'] = self.format

        if self.height is not None:
            result['Height'] = self.height

        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket

        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint

        if self.oss_object is not None:
            result['OssObject'] = self.oss_object

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.record_url is not None:
            result['RecordUrl'] = self.record_url

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.width is not None:
            result['Width'] = self.width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Height') is not None:
            self.height = m.get('Height')

        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')

        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')

        if m.get('OssObject') is not None:
            self.oss_object = m.get('OssObject')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('RecordUrl') is not None:
            self.record_url = m.get('RecordUrl')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('Width') is not None:
            self.width = m.get('Width')

        return self

