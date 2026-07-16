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
        # The download configuration.
        # 
        # This parameter is required.
        self.configuration = configuration
        # The description of the log download task.
        self.description = description
        # The display name.
        # 
        # This parameter is required.
        self.display_name = display_name
        # The name of the job. The name must meet the following requirements:
        # 
        # The job name must be unique within a project.
        # 
        # - It can contain only lowercase letters, digits, hyphens (-), and underscores (_).
        # 
        # - It must start and end with a lowercase letter or a digit.
        # 
        # - The name must be 2 to 64 characters in length.
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
        # Specifies whether to allow the download of incomplete results. Valid values: \\`true\\` and \\`false\\`.
        # 
        # This parameter is required.
        self.allow_in_complete = allow_in_complete
        # The start time. This is a UNIX timestamp that is accurate to the second.
        # 
        # This parameter is required.
        self.from_time = from_time
        # The source Logstore.
        # 
        # This parameter is required.
        self.logstore = logstore
        # Specifies whether to enable PowerSQL. Valid values: \\`true\\` and \\`false\\`.
        self.power_sql = power_sql
        # The search statement.
        # 
        # This parameter is required.
        self.query = query
        # The export configuration.
        # 
        # This parameter is required.
        self.sink = sink
        # The end time. This is a UNIX timestamp that is accurate to the second.
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
        # The destination Object Storage Service (OSS) bucket.
        self.bucket = bucket
        # The compression format of the file. Valid values: \\`zstd\\`, \\`lz4\\`, \\`gzip\\`, and \\`none\\`.
        # 
        # This parameter is required.
        self.compression_type = compression_type
        # The format of the downloaded file. Valid values: \\`csv\\` and \\`json\\`.
        # 
        # This parameter is required.
        self.content_type = content_type
        # The prefix of the path in the destination OSS bucket.
        self.prefix = prefix
        # The Alibaba Cloud Resource Name (ARN) of the RAM role to use for the download.
        self.role_arn = role_arn
        # The type of the destination. Set the value to \\`AliyunOSS\\`.
        # 
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

