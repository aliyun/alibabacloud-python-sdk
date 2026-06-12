# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GCSIngestionConfigurationSource(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        advanced_parameters: Dict[str, Any] = None,
        bucket: str = None,
        compression_codec: str = None,
        encoding: str = None,
        end_time: int = None,
        endpoint: str = None,
        format: Dict[str, Any] = None,
        interval: str = None,
        pattern: str = None,
        prefix: str = None,
        processor_id: str = None,
        restore_object_enabled: bool = None,
        start_time: int = None,
        tag_pack_id: bool = None,
        time_field: str = None,
        time_format: str = None,
        time_pattern: str = None,
        time_zone: str = None,
    ):
        # The access key ID for authenticating with the GCS service. This parameter is required.
        # 
        # This parameter is required.
        self.access_key_id = access_key_id
        # The secret access key corresponding to the `accessKeyId`. This value is sensitive and must be managed securely.
        # 
        # This parameter is required.
        self.access_key_secret = access_key_secret
        # A nested object for specifying advanced configuration options as key-value pairs.
        self.advanced_parameters = advanced_parameters
        # The name of the GCS bucket that contains the source data files.
        # 
        # This parameter is required.
        self.bucket = bucket
        # The compression format of the source files. Supported values are `none`, `gzip`, and `zstd`. If not specified, the system infers the format from the file extension.
        # 
        # This parameter is required.
        self.compression_codec = compression_codec
        # The character encoding of the source files. The default value is `UTF-8`.
        # 
        # This parameter is required.
        self.encoding = encoding
        # The end of the time range for data ingestion, specified as a Unix timestamp (in seconds). Only objects modified before this time are ingested.
        self.end_time = end_time
        # The service endpoint for GCS. You can use a custom endpoint for private or accelerated connections.
        self.endpoint = endpoint
        # A nested object that defines the format of the source data, such as CSV, JSON, or Parquet.
        # 
        # This parameter is required.
        self.format = format
        # The interval for checking for new data. Specify the value in a duration format, such as `15m` for 15 minutes. Set to `never` to perform a one-time ingestion.
        # 
        # This parameter is required.
        self.interval = interval
        # A regular expression that specifies which files to ingest. The pattern is matched against the full object key within the specified prefix.
        self.pattern = pattern
        # The object key prefix used to discover files. This limits the scope of ingestion to a specific "folder" within the bucket.
        self.prefix = prefix
        # The unique ID of the processor or pipeline that handles the ingested data.
        self.processor_id = processor_id
        # Specifies whether to automatically restore objects from archival storage classes before ingestion. Set to `true` to enable this feature. The default is `false`.
        self.restore_object_enabled = restore_object_enabled
        # The start of the time range for data ingestion, specified as a Unix timestamp (in seconds). Only objects modified at or after this time are ingested.
        self.start_time = start_time
        # The ID of a predefined tag pack to apply to the ingested data. Tag packs contain rules for data enrichment and categorization.
        self.tag_pack_id = tag_pack_id
        # The name of the field in your data that contains the timestamp. This timestamp is used as the event time for the ingested records.
        self.time_field = time_field
        # The format of the timestamp in the `timeField`, specified using the Java `SimpleDateFormat` pattern. For example: `yyyy-MM-dd\\"T\\"HH:mm:ss.SSSZ`.
        self.time_format = time_format
        # A regular expression used to extract a timestamp from unstructured data, such as a log entry or filename, if a structured `timeField` is not available.
        self.time_pattern = time_pattern
        # The time zone for parsing timestamps that lack explicit time zone information. Specify a valid time zone identifier, such as `UTC` or `America/Los_Angeles`.
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id

        if self.access_key_secret is not None:
            result['accessKeySecret'] = self.access_key_secret

        if self.advanced_parameters is not None:
            result['advancedParameters'] = self.advanced_parameters

        if self.bucket is not None:
            result['bucket'] = self.bucket

        if self.compression_codec is not None:
            result['compressionCodec'] = self.compression_codec

        if self.encoding is not None:
            result['encoding'] = self.encoding

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.format is not None:
            result['format'] = self.format

        if self.interval is not None:
            result['interval'] = self.interval

        if self.pattern is not None:
            result['pattern'] = self.pattern

        if self.prefix is not None:
            result['prefix'] = self.prefix

        if self.processor_id is not None:
            result['processorId'] = self.processor_id

        if self.restore_object_enabled is not None:
            result['restoreObjectEnabled'] = self.restore_object_enabled

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.tag_pack_id is not None:
            result['tagPackId'] = self.tag_pack_id

        if self.time_field is not None:
            result['timeField'] = self.time_field

        if self.time_format is not None:
            result['timeFormat'] = self.time_format

        if self.time_pattern is not None:
            result['timePattern'] = self.time_pattern

        if self.time_zone is not None:
            result['timeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')

        if m.get('accessKeySecret') is not None:
            self.access_key_secret = m.get('accessKeySecret')

        if m.get('advancedParameters') is not None:
            self.advanced_parameters = m.get('advancedParameters')

        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')

        if m.get('compressionCodec') is not None:
            self.compression_codec = m.get('compressionCodec')

        if m.get('encoding') is not None:
            self.encoding = m.get('encoding')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('format') is not None:
            self.format = m.get('format')

        if m.get('interval') is not None:
            self.interval = m.get('interval')

        if m.get('pattern') is not None:
            self.pattern = m.get('pattern')

        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')

        if m.get('processorId') is not None:
            self.processor_id = m.get('processorId')

        if m.get('restoreObjectEnabled') is not None:
            self.restore_object_enabled = m.get('restoreObjectEnabled')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('tagPackId') is not None:
            self.tag_pack_id = m.get('tagPackId')

        if m.get('timeField') is not None:
            self.time_field = m.get('timeField')

        if m.get('timeFormat') is not None:
            self.time_format = m.get('timeFormat')

        if m.get('timePattern') is not None:
            self.time_pattern = m.get('timePattern')

        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')

        return self

