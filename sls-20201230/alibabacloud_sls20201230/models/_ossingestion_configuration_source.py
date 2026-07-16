# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class OSSIngestionConfigurationSource(DaraModel):
    def __init__(
        self,
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
        role_arn: str = None,
        start_time: int = None,
        tag_pack_id: bool = None,
        time_field: str = None,
        time_format: str = None,
        time_pattern: str = None,
        time_zone: str = None,
        use_meta_index: bool = None,
    ):
        self.advanced_parameters = advanced_parameters
        # The name of the OSS bucket.
        # 
        # This parameter is required.
        self.bucket = bucket
        # The compression type of the source files.
        # 
        # This parameter is required.
        self.compression_codec = compression_codec
        # The encoding of the source files.
        # 
        # This parameter is required.
        self.encoding = encoding
        # Imports only files modified before this time. The value is a Unix timestamp in seconds.
        self.end_time = end_time
        # The OSS endpoint.
        # 
        # This parameter is required.
        self.endpoint = endpoint
        # Defines the format of the source data.
        # 
        # This parameter is required.
        self.format = format
        # The check interval for new files.
        # 
        # This parameter is required.
        self.interval = interval
        # A regular expression to filter files by path.
        self.pattern = pattern
        # The path prefix for filtering files.
        self.prefix = prefix
        # The ID of the writer processor.
        self.processor_id = processor_id
        # Specifies whether to import archived files.
        self.restore_object_enabled = restore_object_enabled
        # The Role ARN to use for accessing the OSS bucket.
        self.role_arn = role_arn
        # Imports only files modified after this time. The value is a Unix timestamp in seconds.
        self.start_time = start_time
        # Specifies whether to enable context retrieval.
        self.tag_pack_id = tag_pack_id
        # The field containing the log time.
        self.time_field = time_field
        # The format of the time field.
        self.time_format = time_format
        # The regular expression to extract the time value from a log.
        self.time_pattern = time_pattern
        # The time zone of the timestamp in the source data.
        self.time_zone = time_zone
        # Specifies whether to use the OSS metadata index to accelerate file discovery.
        # 
        # This parameter is required.
        self.use_meta_index = use_meta_index

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.role_arn is not None:
            result['roleARN'] = self.role_arn

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

        if self.use_meta_index is not None:
            result['useMetaIndex'] = self.use_meta_index

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('roleARN') is not None:
            self.role_arn = m.get('roleARN')

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

        if m.get('useMetaIndex') is not None:
            self.use_meta_index = m.get('useMetaIndex')

        return self

