# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class GetDownloadJobResponseBody(DaraModel):
    def __init__(
        self,
        configuration: main_models.GetDownloadJobResponseBodyConfiguration = None,
        create_time: str = None,
        description: str = None,
        display_name: str = None,
        execution_details: main_models.GetDownloadJobResponseBodyExecutionDetails = None,
        name: str = None,
        status: str = None,
    ):
        # 下载配置
        self.configuration = configuration
        # 代表创建时间的资源属性字段
        self.create_time = create_time
        # 任务描述
        self.description = description
        # 任务显示名称
        self.display_name = display_name
        # 任务执行细节
        self.execution_details = execution_details
        # 代表资源名称的资源属性字段
        self.name = name
        # The status of the log download task.
        self.status = status

    def validate(self):
        if self.configuration:
            self.configuration.validate()
        if self.execution_details:
            self.execution_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configuration is not None:
            result['configuration'] = self.configuration.to_map()

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.execution_details is not None:
            result['executionDetails'] = self.execution_details.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configuration') is not None:
            temp_model = main_models.GetDownloadJobResponseBodyConfiguration()
            self.configuration = temp_model.from_map(m.get('configuration'))

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('executionDetails') is not None:
            temp_model = main_models.GetDownloadJobResponseBodyExecutionDetails()
            self.execution_details = temp_model.from_map(m.get('executionDetails'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class GetDownloadJobResponseBodyExecutionDetails(DaraModel):
    def __init__(
        self,
        check_sum: str = None,
        error_message: str = None,
        execute_time: int = None,
        file_path: str = None,
        file_size: int = None,
        log_count: int = None,
        notice: str = None,
        progress: int = None,
    ):
        self.check_sum = check_sum
        # 下载错误信息
        self.error_message = error_message
        # 下载执行时间
        self.execute_time = execute_time
        # 下载结果链接
        self.file_path = file_path
        # 下载文件大小
        self.file_size = file_size
        # 下载日志条数
        self.log_count = log_count
        self.notice = notice
        # 下载进度
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_sum is not None:
            result['checkSum'] = self.check_sum

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.execute_time is not None:
            result['executeTime'] = self.execute_time

        if self.file_path is not None:
            result['filePath'] = self.file_path

        if self.file_size is not None:
            result['fileSize'] = self.file_size

        if self.log_count is not None:
            result['logCount'] = self.log_count

        if self.notice is not None:
            result['notice'] = self.notice

        if self.progress is not None:
            result['progress'] = self.progress

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkSum') is not None:
            self.check_sum = m.get('checkSum')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('executeTime') is not None:
            self.execute_time = m.get('executeTime')

        if m.get('filePath') is not None:
            self.file_path = m.get('filePath')

        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')

        if m.get('logCount') is not None:
            self.log_count = m.get('logCount')

        if m.get('notice') is not None:
            self.notice = m.get('notice')

        if m.get('progress') is not None:
            self.progress = m.get('progress')

        return self

class GetDownloadJobResponseBodyConfiguration(DaraModel):
    def __init__(
        self,
        allow_in_complete: bool = None,
        from_time: int = None,
        logstore: str = None,
        power_sql: bool = None,
        query: str = None,
        sink: main_models.GetDownloadJobResponseBodyConfigurationSink = None,
        to_time: int = None,
    ):
        self.allow_in_complete = allow_in_complete
        # 起点时间戳（精确到秒）
        self.from_time = from_time
        # 源logstore
        self.logstore = logstore
        # 是否启用powerSql
        self.power_sql = power_sql
        # 查询语句
        self.query = query
        # 导出配置
        self.sink = sink
        # 结束时间戳（精确到秒）
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
            temp_model = main_models.GetDownloadJobResponseBodyConfigurationSink()
            self.sink = temp_model.from_map(m.get('sink'))

        if m.get('toTime') is not None:
            self.to_time = m.get('toTime')

        return self

class GetDownloadJobResponseBodyConfigurationSink(DaraModel):
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
        self.compression_type = compression_type
        # 下载文件格式
        self.content_type = content_type
        self.prefix = prefix
        # 下载使用roleArn
        self.role_arn = role_arn
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

