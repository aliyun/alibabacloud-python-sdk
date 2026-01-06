# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class SinkOSSParameters(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        compression_type: str = None,
        content_transform: main_models.SinkOSSParametersContentTransform = None,
        endpoint: str = None,
        path_format: str = None,
        region_id: str = None,
        role_arn: str = None,
        rotate_interval_ms: str = None,
        rotate_size_bytes: str = None,
        sslenabled: bool = None,
        task_concurrency: str = None,
        time_zone: str = None,
    ):
        self.bucket_name = bucket_name
        self.compression_type = compression_type
        self.content_transform = content_transform
        self.endpoint = endpoint
        self.path_format = path_format
        self.region_id = region_id
        self.role_arn = role_arn
        self.rotate_interval_ms = rotate_interval_ms
        self.rotate_size_bytes = rotate_size_bytes
        self.sslenabled = sslenabled
        self.task_concurrency = task_concurrency
        self.time_zone = time_zone

    def validate(self):
        if self.content_transform:
            self.content_transform.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.compression_type is not None:
            result['CompressionType'] = self.compression_type

        if self.content_transform is not None:
            result['ContentTransform'] = self.content_transform.to_map()

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.path_format is not None:
            result['PathFormat'] = self.path_format

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        if self.rotate_interval_ms is not None:
            result['RotateIntervalMs'] = self.rotate_interval_ms

        if self.rotate_size_bytes is not None:
            result['RotateSizeBytes'] = self.rotate_size_bytes

        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled

        if self.task_concurrency is not None:
            result['TaskConcurrency'] = self.task_concurrency

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('CompressionType') is not None:
            self.compression_type = m.get('CompressionType')

        if m.get('ContentTransform') is not None:
            temp_model = main_models.SinkOSSParametersContentTransform()
            self.content_transform = temp_model.from_map(m.get('ContentTransform'))

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('PathFormat') is not None:
            self.path_format = m.get('PathFormat')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        if m.get('RotateIntervalMs') is not None:
            self.rotate_interval_ms = m.get('RotateIntervalMs')

        if m.get('RotateSizeBytes') is not None:
            self.rotate_size_bytes = m.get('RotateSizeBytes')

        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')

        if m.get('TaskConcurrency') is not None:
            self.task_concurrency = m.get('TaskConcurrency')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        return self

class SinkOSSParametersContentTransform(DaraModel):
    def __init__(
        self,
        form: str = None,
        template: str = None,
        value: str = None,
    ):
        self.form = form
        self.template = template
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.form is not None:
            result['Form'] = self.form

        if self.template is not None:
            result['Template'] = self.template

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Form') is not None:
            self.form = m.get('Form')

        if m.get('Template') is not None:
            self.template = m.get('Template')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

