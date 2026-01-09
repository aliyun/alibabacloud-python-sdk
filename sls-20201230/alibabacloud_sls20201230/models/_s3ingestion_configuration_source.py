# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class S3IngestionConfigurationSource(DaraModel):
    def __init__(
        self,
        aws_access_key: str = None,
        aws_access_key_secret: str = None,
        aws_region: str = None,
        aws_sqsqueue_url: str = None,
        aws_use_sqs: bool = None,
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
        start_time: int = None,
        tag_pack_id: bool = None,
        time_field: str = None,
        time_format: str = None,
        time_pattern: str = None,
        time_zone: str = None,
        use_aws_sqsonly: bool = None,
    ):
        # This parameter is required.
        self.aws_access_key = aws_access_key
        # This parameter is required.
        self.aws_access_key_secret = aws_access_key_secret
        # This parameter is required.
        self.aws_region = aws_region
        self.aws_sqsqueue_url = aws_sqsqueue_url
        self.aws_use_sqs = aws_use_sqs
        # This parameter is required.
        self.bucket = bucket
        # This parameter is required.
        self.compression_codec = compression_codec
        # This parameter is required.
        self.encoding = encoding
        self.end_time = end_time
        self.endpoint = endpoint
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
        self.use_aws_sqsonly = use_aws_sqsonly

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aws_access_key is not None:
            result['awsAccessKey'] = self.aws_access_key

        if self.aws_access_key_secret is not None:
            result['awsAccessKeySecret'] = self.aws_access_key_secret

        if self.aws_region is not None:
            result['awsRegion'] = self.aws_region

        if self.aws_sqsqueue_url is not None:
            result['awsSQSQueueUrl'] = self.aws_sqsqueue_url

        if self.aws_use_sqs is not None:
            result['awsUseSQS'] = self.aws_use_sqs

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

        if self.use_aws_sqsonly is not None:
            result['useAwsSQSOnly'] = self.use_aws_sqsonly

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('awsAccessKey') is not None:
            self.aws_access_key = m.get('awsAccessKey')

        if m.get('awsAccessKeySecret') is not None:
            self.aws_access_key_secret = m.get('awsAccessKeySecret')

        if m.get('awsRegion') is not None:
            self.aws_region = m.get('awsRegion')

        if m.get('awsSQSQueueUrl') is not None:
            self.aws_sqsqueue_url = m.get('awsSQSQueueUrl')

        if m.get('awsUseSQS') is not None:
            self.aws_use_sqs = m.get('awsUseSQS')

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

        if m.get('useAwsSQSOnly') is not None:
            self.use_aws_sqsonly = m.get('useAwsSQSOnly')

        return self

