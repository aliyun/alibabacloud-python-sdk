# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetStructSyncJobDetailResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        struct_sync_job_detail: main_models.GetStructSyncJobDetailResponseBodyStructSyncJobDetail = None,
        success: bool = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The request ID.
        self.request_id = request_id
        # The details of the schema synchronization task.
        self.struct_sync_job_detail = struct_sync_job_detail
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.struct_sync_job_detail:
            self.struct_sync_job_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.struct_sync_job_detail is not None:
            result['StructSyncJobDetail'] = self.struct_sync_job_detail.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StructSyncJobDetail') is not None:
            temp_model = main_models.GetStructSyncJobDetailResponseBodyStructSyncJobDetail()
            self.struct_sync_job_detail = temp_model.from_map(m.get('StructSyncJobDetail'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetStructSyncJobDetailResponseBodyStructSyncJobDetail(DaraModel):
    def __init__(
        self,
        dbtask_group_id: int = None,
        execute_count: int = None,
        job_status: str = None,
        message: str = None,
        security_rule: str = None,
        sql_count: int = None,
        table_analyzed: int = None,
        table_count: int = None,
    ):
        # The ID of the SQL task group.
        self.dbtask_group_id = dbtask_group_id
        # The number of SQL statements that have been executed.
        self.execute_count = execute_count
        # The status of the task. Valid values:
        # 
        # *   **NEW**: The task was created.
        # *   **COMPARING**: The schemas of tables were being compared.
        # *   **COMPARE_BREAK**: The schema comparison was interrupted.
        # *   **COMPARE_FINISH**: The comparison was finished.
        # *   **NOT_SCRIPTS**: The comparison was finished but no executable script was available.
        # *   **SUBMITED_DBTASK**: The task was submitted.
        # *   **DBTASK_SUCCESS**: The task was complete.
        # *   **SUBMITED_WORKFLOW**: The ticket was submitted.
        # *   **WORKFLOW_SUCCESS**: The ticket was approved.
        self.job_status = job_status
        # The description of the task.
        self.message = message
        # The type of security rule. Valid values:
        # 
        # *   **CANNOT_SYNC**: Synchronization cannot be performed.
        # *   **WITH_APPROVE**: The schema synchronization can be performed after the ticket is approved. You can call the [SubmitStructSyncOrderApproval](https://help.aliyun.com/document_detail/206166.html) operation to submit the ticket for approval.
        # *   **WITHOUT_APPROVE**: The schema synchronization can be performed without approval.
        self.security_rule = security_rule
        # The total number of SQL statements.
        self.sql_count = sql_count
        # The number of tables that have been analyzed.
        self.table_analyzed = table_analyzed
        # The total number of tables.
        self.table_count = table_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbtask_group_id is not None:
            result['DBTaskGroupId'] = self.dbtask_group_id

        if self.execute_count is not None:
            result['ExecuteCount'] = self.execute_count

        if self.job_status is not None:
            result['JobStatus'] = self.job_status

        if self.message is not None:
            result['Message'] = self.message

        if self.security_rule is not None:
            result['SecurityRule'] = self.security_rule

        if self.sql_count is not None:
            result['SqlCount'] = self.sql_count

        if self.table_analyzed is not None:
            result['TableAnalyzed'] = self.table_analyzed

        if self.table_count is not None:
            result['TableCount'] = self.table_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBTaskGroupId') is not None:
            self.dbtask_group_id = m.get('DBTaskGroupId')

        if m.get('ExecuteCount') is not None:
            self.execute_count = m.get('ExecuteCount')

        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('SecurityRule') is not None:
            self.security_rule = m.get('SecurityRule')

        if m.get('SqlCount') is not None:
            self.sql_count = m.get('SqlCount')

        if m.get('TableAnalyzed') is not None:
            self.table_analyzed = m.get('TableAnalyzed')

        if m.get('TableCount') is not None:
            self.table_count = m.get('TableCount')

        return self

