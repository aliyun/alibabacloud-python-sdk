# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class CreateDiagnosticTaskRequest(DaraModel):
    def __init__(
        self,
        ai_job_log_info: main_models.CreateDiagnosticTaskRequestAiJobLogInfo = None,
        cluster_id: str = None,
        diagnostic_type: str = None,
        node_ids: List[str] = None,
    ):
        # The log information.
        self.ai_job_log_info = ai_job_log_info
        # The cluster ID.
        self.cluster_id = cluster_id
        # The diagnostics type.
        self.diagnostic_type = diagnostic_type
        # The IDs of the nodes.
        self.node_ids = node_ids

    def validate(self):
        if self.ai_job_log_info:
            self.ai_job_log_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_job_log_info is not None:
            result['AiJobLogInfo'] = self.ai_job_log_info.to_map()

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.diagnostic_type is not None:
            result['DiagnosticType'] = self.diagnostic_type

        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiJobLogInfo') is not None:
            temp_model = main_models.CreateDiagnosticTaskRequestAiJobLogInfo()
            self.ai_job_log_info = temp_model.from_map(m.get('AiJobLogInfo'))

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DiagnosticType') is not None:
            self.diagnostic_type = m.get('DiagnosticType')

        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        return self

class CreateDiagnosticTaskRequestAiJobLogInfo(DaraModel):
    def __init__(
        self,
        ai_job_logs: List[main_models.CreateDiagnosticTaskRequestAiJobLogInfoAiJobLogs] = None,
        end_time: str = None,
        start_time: str = None,
    ):
        # The task logs.
        self.ai_job_logs = ai_job_logs
        # The end time. The value is in the timestamp format. Unit: seconds.
        # 
        # >  This timestamp must indicate a point in time that is accurate to the minute.
        self.end_time = end_time
        # The start time. The value is in the timestamp format. Unit: seconds.
        # 
        # >  This timestamp must indicate a point in time that is accurate to the minute.
        self.start_time = start_time

    def validate(self):
        if self.ai_job_logs:
            for v1 in self.ai_job_logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AiJobLogs'] = []
        if self.ai_job_logs is not None:
            for k1 in self.ai_job_logs:
                result['AiJobLogs'].append(k1.to_map() if k1 else None)

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ai_job_logs = []
        if m.get('AiJobLogs') is not None:
            for k1 in m.get('AiJobLogs'):
                temp_model = main_models.CreateDiagnosticTaskRequestAiJobLogInfoAiJobLogs()
                self.ai_job_logs.append(temp_model.from_map(k1))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class CreateDiagnosticTaskRequestAiJobLogInfoAiJobLogs(DaraModel):
    def __init__(
        self,
        ai_instance: str = None,
        logs: List[main_models.CreateDiagnosticTaskRequestAiJobLogInfoAiJobLogsLogs] = None,
        node_id: str = None,
    ):
        # The instance ID.
        self.ai_instance = ai_instance
        # The logs.
        self.logs = logs
        # The node ID.
        self.node_id = node_id

    def validate(self):
        if self.logs:
            for v1 in self.logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ai_instance is not None:
            result['AiInstance'] = self.ai_instance

        result['Logs'] = []
        if self.logs is not None:
            for k1 in self.logs:
                result['Logs'].append(k1.to_map() if k1 else None)

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiInstance') is not None:
            self.ai_instance = m.get('AiInstance')

        self.logs = []
        if m.get('Logs') is not None:
            for k1 in m.get('Logs'):
                temp_model = main_models.CreateDiagnosticTaskRequestAiJobLogInfoAiJobLogsLogs()
                self.logs.append(temp_model.from_map(k1))

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        return self

class CreateDiagnosticTaskRequestAiJobLogInfoAiJobLogsLogs(DaraModel):
    def __init__(
        self,
        datetime: str = None,
        log_content: str = None,
    ):
        # The sending date in the yyyymmdd format.
        self.datetime = datetime
        # The log content.
        self.log_content = log_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.datetime is not None:
            result['Datetime'] = self.datetime

        if self.log_content is not None:
            result['LogContent'] = self.log_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Datetime') is not None:
            self.datetime = m.get('Datetime')

        if m.get('LogContent') is not None:
            self.log_content = m.get('LogContent')

        return self

