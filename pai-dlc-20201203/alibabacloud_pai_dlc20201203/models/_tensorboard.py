# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class Tensorboard(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        cpu: int = None,
        data_source_id: str = None,
        data_source_type: str = None,
        display_name: str = None,
        duration: str = None,
        gmt_create_time: str = None,
        gmt_finish_time: str = None,
        gmt_modify_time: str = None,
        job_id: str = None,
        max_running_time_minutes: int = None,
        memory: int = None,
        options: str = None,
        priority: str = None,
        quota_id: str = None,
        quota_name: str = None,
        reason_code: str = None,
        reason_message: str = None,
        request_id: str = None,
        status: str = None,
        summary_path: str = None,
        summary_relative_path: str = None,
        tensorboard_data_sources: List[main_models.TensorboardDataSourceSpec] = None,
        tensorboard_id: str = None,
        tensorboard_spec: main_models.TensorboardSpec = None,
        tensorboard_url: str = None,
        token: str = None,
        user_id: str = None,
        username: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.cpu = cpu
        self.data_source_id = data_source_id
        self.data_source_type = data_source_type
        self.display_name = display_name
        self.duration = duration
        self.gmt_create_time = gmt_create_time
        self.gmt_finish_time = gmt_finish_time
        self.gmt_modify_time = gmt_modify_time
        self.job_id = job_id
        self.max_running_time_minutes = max_running_time_minutes
        self.memory = memory
        self.options = options
        self.priority = priority
        self.quota_id = quota_id
        self.quota_name = quota_name
        self.reason_code = reason_code
        self.reason_message = reason_message
        self.request_id = request_id
        self.status = status
        self.summary_path = summary_path
        self.summary_relative_path = summary_relative_path
        self.tensorboard_data_sources = tensorboard_data_sources
        self.tensorboard_id = tensorboard_id
        self.tensorboard_spec = tensorboard_spec
        self.tensorboard_url = tensorboard_url
        self.token = token
        self.user_id = user_id
        self.username = username
        self.workspace_id = workspace_id

    def validate(self):
        if self.tensorboard_data_sources:
            for v1 in self.tensorboard_data_sources:
                 if v1:
                    v1.validate()
        if self.tensorboard_spec:
            self.tensorboard_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_finish_time is not None:
            result['GmtFinishTime'] = self.gmt_finish_time

        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.max_running_time_minutes is not None:
            result['MaxRunningTimeMinutes'] = self.max_running_time_minutes

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.options is not None:
            result['Options'] = self.options

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id

        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name

        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code

        if self.reason_message is not None:
            result['ReasonMessage'] = self.reason_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.summary_path is not None:
            result['SummaryPath'] = self.summary_path

        if self.summary_relative_path is not None:
            result['SummaryRelativePath'] = self.summary_relative_path

        result['TensorboardDataSources'] = []
        if self.tensorboard_data_sources is not None:
            for k1 in self.tensorboard_data_sources:
                result['TensorboardDataSources'].append(k1.to_map() if k1 else None)

        if self.tensorboard_id is not None:
            result['TensorboardId'] = self.tensorboard_id

        if self.tensorboard_spec is not None:
            result['TensorboardSpec'] = self.tensorboard_spec.to_map()

        if self.tensorboard_url is not None:
            result['TensorboardUrl'] = self.tensorboard_url

        if self.token is not None:
            result['Token'] = self.token

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.username is not None:
            result['Username'] = self.username

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtFinishTime') is not None:
            self.gmt_finish_time = m.get('GmtFinishTime')

        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('MaxRunningTimeMinutes') is not None:
            self.max_running_time_minutes = m.get('MaxRunningTimeMinutes')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')

        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')

        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')

        if m.get('ReasonMessage') is not None:
            self.reason_message = m.get('ReasonMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SummaryPath') is not None:
            self.summary_path = m.get('SummaryPath')

        if m.get('SummaryRelativePath') is not None:
            self.summary_relative_path = m.get('SummaryRelativePath')

        self.tensorboard_data_sources = []
        if m.get('TensorboardDataSources') is not None:
            for k1 in m.get('TensorboardDataSources'):
                temp_model = main_models.TensorboardDataSourceSpec()
                self.tensorboard_data_sources.append(temp_model.from_map(k1))

        if m.get('TensorboardId') is not None:
            self.tensorboard_id = m.get('TensorboardId')

        if m.get('TensorboardSpec') is not None:
            temp_model = main_models.TensorboardSpec()
            self.tensorboard_spec = temp_model.from_map(m.get('TensorboardSpec'))

        if m.get('TensorboardUrl') is not None:
            self.tensorboard_url = m.get('TensorboardUrl')

        if m.get('Token') is not None:
            self.token = m.get('Token')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

