# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class OSSExportConfiguration(DaraModel):
    def __init__(
        self,
        from_time: int = None,
        logstore: str = None,
        role_arn: str = None,
        sink: main_models.OSSExportConfigurationSink = None,
        to_time: int = None,
    ):
        self.from_time = from_time
        self.logstore = logstore
        self.role_arn = role_arn
        self.sink = sink
        self.to_time = to_time

    def validate(self):
        if self.sink:
            self.sink.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_time is not None:
            result['fromTime'] = self.from_time

        if self.logstore is not None:
            result['logstore'] = self.logstore

        if self.role_arn is not None:
            result['roleArn'] = self.role_arn

        if self.sink is not None:
            result['sink'] = self.sink.to_map()

        if self.to_time is not None:
            result['toTime'] = self.to_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fromTime') is not None:
            self.from_time = m.get('fromTime')

        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')

        if m.get('sink') is not None:
            temp_model = main_models.OSSExportConfigurationSink()
            self.sink = temp_model.from_map(m.get('sink'))

        if m.get('toTime') is not None:
            self.to_time = m.get('toTime')

        return self

class OSSExportConfigurationSink(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        buffer_interval: int = None,
        buffer_size: int = None,
        compression_type: str = None,
        content_detail: Dict[str, Any] = None,
        content_type: str = None,
        delay_sec: int = None,
        delay_seconds: int = None,
        endpoint: str = None,
        path_format: str = None,
        path_format_type: str = None,
        prefix: str = None,
        role_arn: str = None,
        suffix: str = None,
        time_zone: str = None,
    ):
        # This parameter is required.
        self.bucket = bucket
        self.buffer_interval = buffer_interval
        self.buffer_size = buffer_size
        self.compression_type = compression_type
        self.content_detail = content_detail
        self.content_type = content_type
        self.delay_sec = delay_sec
        self.delay_seconds = delay_seconds
        # This parameter is required.
        self.endpoint = endpoint
        # This parameter is required.
        self.path_format = path_format
        # This parameter is required.
        self.path_format_type = path_format_type
        self.prefix = prefix
        # This parameter is required.
        self.role_arn = role_arn
        self.suffix = suffix
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['bucket'] = self.bucket

        if self.buffer_interval is not None:
            result['bufferInterval'] = self.buffer_interval

        if self.buffer_size is not None:
            result['bufferSize'] = self.buffer_size

        if self.compression_type is not None:
            result['compressionType'] = self.compression_type

        if self.content_detail is not None:
            result['contentDetail'] = self.content_detail

        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.delay_sec is not None:
            result['delaySec'] = self.delay_sec

        if self.delay_seconds is not None:
            result['delaySeconds'] = self.delay_seconds

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.path_format is not None:
            result['pathFormat'] = self.path_format

        if self.path_format_type is not None:
            result['pathFormatType'] = self.path_format_type

        if self.prefix is not None:
            result['prefix'] = self.prefix

        if self.role_arn is not None:
            result['roleArn'] = self.role_arn

        if self.suffix is not None:
            result['suffix'] = self.suffix

        if self.time_zone is not None:
            result['timeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')

        if m.get('bufferInterval') is not None:
            self.buffer_interval = m.get('bufferInterval')

        if m.get('bufferSize') is not None:
            self.buffer_size = m.get('bufferSize')

        if m.get('compressionType') is not None:
            self.compression_type = m.get('compressionType')

        if m.get('contentDetail') is not None:
            self.content_detail = m.get('contentDetail')

        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('delaySec') is not None:
            self.delay_sec = m.get('delaySec')

        if m.get('delaySeconds') is not None:
            self.delay_seconds = m.get('delaySeconds')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('pathFormat') is not None:
            self.path_format = m.get('pathFormat')

        if m.get('pathFormatType') is not None:
            self.path_format_type = m.get('pathFormatType')

        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')

        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')

        if m.get('suffix') is not None:
            self.suffix = m.get('suffix')

        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')

        return self

