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
        source_secure_transport: bool = None,
        to_time: int = None,
    ):
        # The start time for the export, specified as a Unix timestamp. Set to 1 to export from the earliest available data in the Logstore.
        self.from_time = from_time
        # The name of the source Logstore.
        self.logstore = logstore
        # The ARN of the Resource Access Management (RAM) role that Log Service assumes to read data from the Logstore. You must specify the ARN of your role.
        self.role_arn = role_arn
        # The configuration of the destination OSS sink.
        self.sink = sink
        self.source_secure_transport = source_secure_transport
        # The end time for the export, specified as a Unix timestamp. Set to 0 to run the task continuously until it is stopped.
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

        if self.source_secure_transport is not None:
            result['sourceSecureTransport'] = self.source_secure_transport

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

        if m.get('sourceSecureTransport') is not None:
            self.source_secure_transport = m.get('sourceSecureTransport')

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
        # The name of the destination OSS bucket.
        # 
        # This parameter is required.
        self.bucket = bucket
        # The time in seconds to buffer data before exporting. The value must be an integer from 300 to 900.
        self.buffer_interval = buffer_interval
        # The amount of data in MB to buffer before exporting. The value must be an integer from 5 to 256.
        self.buffer_size = buffer_size
        # The compression type for the exported files. Valid values: `snappy`, `gzip`, `zstd`, and `none` (no compression).
        self.compression_type = compression_type
        # Format-specific settings. The structure of this JSON object depends on the `contentType` value.
        self.content_detail = content_detail
        # The format of the files stored in OSS. Valid values: `json`, `parquet`, `csv`, and `orc`.
        self.content_type = content_type
        # The delivery delay.
        # 
        # > - This parameter is deprecated.
        self.delay_sec = delay_sec
        # The delivery delay, in seconds. This value cannot exceed the data retention period of the source Logstore.
        self.delay_seconds = delay_seconds
        # - For Object Storage Service (OSS): The OSS internal endpoint. You must use an endpoint in the same region as the Logstore. For more information, see [OSS access domains and data centers](https://help.aliyun.com/document_detail/31837.html). The endpoint must use the HTTPS protocol.
        # 
        # - For OSS-HDFS: The OSS-HDFS internal endpoint. You must use an endpoint in the same region as the Logstore.
        # 
        # This parameter is required.
        self.endpoint = endpoint
        # The path format for exported files. For more information, see [Path format](https://help.aliyun.com/document_detail/371934.html).
        # 
        # This parameter is required.
        self.path_format = path_format
        # The type of the path format.
        # 
        # This parameter is required.
        self.path_format_type = path_format_type
        # The prefix for files exported to the OSS bucket.
        self.prefix = prefix
        # The ARN of the RAM role that Log Service assumes to write data to the OSS bucket. You must specify the ARN of your role.
        # 
        # This parameter is required.
        self.role_arn = role_arn
        # The suffix for the exported files.
        self.suffix = suffix
        # The time zone used for the path format. For more information, see [Time zones](https://help.aliyun.com/document_detail/375323.html).
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

