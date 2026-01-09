# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class AzureBlobIngestionConfigurationSource(DaraModel):
    def __init__(
        self,
        account_key: str = None,
        account_name: str = None,
        compression_codec: str = None,
        container_name: str = None,
        encoding: str = None,
        end_time: int = None,
        format: Dict[str, Any] = None,
        interval: str = None,
        pattern: str = None,
        prefix: str = None,
        processor_id: str = None,
        start_time: int = None,
        tag_pack_id: bool = None,
        time_field: str = None,
        time_format: str = None,
        time_pattern: str = None,
        time_zone: str = None,
    ):
        # This parameter is required.
        self.account_key = account_key
        # This parameter is required.
        self.account_name = account_name
        # This parameter is required.
        self.compression_codec = compression_codec
        # This parameter is required.
        self.container_name = container_name
        # This parameter is required.
        self.encoding = encoding
        self.end_time = end_time
        # This parameter is required.
        self.format = format
        # This parameter is required.
        self.interval = interval
        self.pattern = pattern
        self.prefix = prefix
        self.processor_id = processor_id
        self.start_time = start_time
        self.tag_pack_id = tag_pack_id
        self.time_field = time_field
        self.time_format = time_format
        self.time_pattern = time_pattern
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_key is not None:
            result['accountKey'] = self.account_key

        if self.account_name is not None:
            result['accountName'] = self.account_name

        if self.compression_codec is not None:
            result['compressionCodec'] = self.compression_codec

        if self.container_name is not None:
            result['containerName'] = self.container_name

        if self.encoding is not None:
            result['encoding'] = self.encoding

        if self.end_time is not None:
            result['endTime'] = self.end_time

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
        if m.get('accountKey') is not None:
            self.account_key = m.get('accountKey')

        if m.get('accountName') is not None:
            self.account_name = m.get('accountName')

        if m.get('compressionCodec') is not None:
            self.compression_codec = m.get('compressionCodec')

        if m.get('containerName') is not None:
            self.container_name = m.get('containerName')

        if m.get('encoding') is not None:
            self.encoding = m.get('encoding')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

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

