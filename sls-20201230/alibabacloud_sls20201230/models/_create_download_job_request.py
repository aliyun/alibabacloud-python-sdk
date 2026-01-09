# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class CreateDownloadJobRequest(DaraModel):
    def __init__(
        self,
        configuration: main_models.CreateDownloadJobRequestConfiguration = None,
        description: str = None,
        display_name: str = None,
        name: str = None,
    ):
        # 下载配置
        # 
        # This parameter is required.
        self.configuration = configuration
        # 任务描述
        self.description = description
        # 任务显示名称
        # 
        # This parameter is required.
        self.display_name = display_name
        # 代表资源名称的资源属性字段
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        if self.configuration:
            self.configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = main_models.CreateDownloadJobRequestConfiguration()
            self.configuration = temp_model.from_map(m.get('configuration'))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class CreateDownloadJobRequestConfiguration(DaraModel):
    def __init__(
        self,
        allow_in_complete: bool = None,
        from_time: int = None,
        logstore: str = None,
        power_sql: bool = None,
        query: str = None,
        sink: main_models.CreateDownloadJobRequestConfigurationSink = None,
        to_time: int = None,
    ):
        # This parameter is required.
        self.allow_in_complete = allow_in_complete
        # 起点时间戳（精确到秒）
        # 
        # This parameter is required.
        self.from_time = from_time
        # 源logstore
        # 
        # This parameter is required.
        self.logstore = logstore
        # 是否启用powerSql
        self.power_sql = power_sql
        # 查询语句
        # 
        # This parameter is required.
        self.query = query
        # 导出配置
        # 
        # This parameter is required.
        self.sink = sink
        # 结束时间戳（精确到秒）
        # 
        # This parameter is required.
        self.to_time = to_time

    def validate(self):
        if self.sink:
            self.sink.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_in_complete is not None:
            result['allowInComplete'] = self.allow_in_complete

        if self.from_time is not None:
            result['fromTime'] = self.from_time

        if self.logstore is not None:
            result['logstore'] = self.logstore

        if self.power_sql is not None:
            result['powerSql'] = self.power_sql

        if self.query is not None:
            result['query'] = self.query

        if self.sink is not None:
            result['sink'] = self.sink.to_map()

        if self.to_time is not None:
            result['toTime'] = self.to_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowInComplete') is not None:
            self.allow_in_complete = m.get('allowInComplete')

        if m.get('fromTime') is not None:
            self.from_time = m.get('fromTime')

        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')

        if m.get('powerSql') is not None:
            self.power_sql = m.get('powerSql')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('sink') is not None:
            temp_model = main_models.CreateDownloadJobRequestConfigurationSink()
            self.sink = temp_model.from_map(m.get('sink'))

        if m.get('toTime') is not None:
            self.to_time = m.get('toTime')

        return self

class CreateDownloadJobRequestConfigurationSink(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        compression_type: str = None,
        content_type: str = None,
        prefix: str = None,
        role_arn: str = None,
        type: str = None,
    ):
        # 对象存储桶
        self.bucket = bucket
        # 压缩格式
        # 
        # This parameter is required.
        self.compression_type = compression_type
        # 下载文件格式
        # 
        # This parameter is required.
        self.content_type = content_type
        self.prefix = prefix
        # 下载使用roleArn
        self.role_arn = role_arn
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['bucket'] = self.bucket

        if self.compression_type is not None:
            result['compressionType'] = self.compression_type

        if self.content_type is not None:
            result['contentType'] = self.content_type

        if self.prefix is not None:
            result['prefix'] = self.prefix

        if self.role_arn is not None:
            result['roleArn'] = self.role_arn

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')

        if m.get('compressionType') is not None:
            self.compression_type = m.get('compressionType')

        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')

        if m.get('prefix') is not None:
            self.prefix = m.get('prefix')

        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

