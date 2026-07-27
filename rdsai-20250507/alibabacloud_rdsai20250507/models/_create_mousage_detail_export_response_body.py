# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class CreateMOUsageDetailExportResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.CreateMOUsageDetailExportResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.CreateMOUsageDetailExportResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateMOUsageDetailExportResponseBodyData(DaraModel):
    def __init__(
        self,
        completed_at: str = None,
        created_at: str = None,
        download_url: str = None,
        error_message: str = None,
        expires_at: str = None,
        file_size: int = None,
        filters: main_models.CreateMOUsageDetailExportResponseBodyDataFilters = None,
        format: str = None,
        oss_key: str = None,
        row_count: int = None,
        status: str = None,
    ):
        self.completed_at = completed_at
        self.created_at = created_at
        self.download_url = download_url
        self.error_message = error_message
        # 下载 URL 失效时间（UTC ISO8601）
        self.expires_at = expires_at
        self.file_size = file_size
        self.filters = filters
        self.format = format
        self.oss_key = oss_key
        self.row_count = row_count
        # pending / processing / completed / failed / expired
        self.status = status

    def validate(self):
        if self.filters:
            self.filters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.completed_at is not None:
            result['CompletedAt'] = self.completed_at

        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.expires_at is not None:
            result['ExpiresAt'] = self.expires_at

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.filters is not None:
            result['Filters'] = self.filters.to_map()

        if self.format is not None:
            result['Format'] = self.format

        if self.oss_key is not None:
            result['OssKey'] = self.oss_key

        if self.row_count is not None:
            result['RowCount'] = self.row_count

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompletedAt') is not None:
            self.completed_at = m.get('CompletedAt')

        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('ExpiresAt') is not None:
            self.expires_at = m.get('ExpiresAt')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('Filters') is not None:
            temp_model = main_models.CreateMOUsageDetailExportResponseBodyDataFilters()
            self.filters = temp_model.from_map(m.get('Filters'))

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')

        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class CreateMOUsageDetailExportResponseBodyDataFilters(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        end_time: str = None,
        instance_id: str = None,
        model: str = None,
        start_time: str = None,
    ):
        self.api_key = api_key
        self.end_time = end_time
        self.instance_id = instance_id
        self.model = model
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.model is not None:
            result['Model'] = self.model

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

