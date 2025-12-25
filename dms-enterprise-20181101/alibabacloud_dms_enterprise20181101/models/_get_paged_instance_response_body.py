# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetPagedInstanceResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetPagedInstanceResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total: int = None,
        trace_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message that is returned if the request failed.
        self.error_message = error_message
        # The page number.
        self.page_index = page_index
        # The number of entries to return on each page.
        self.page_size = page_size
        # The request ID. You can use the request ID to query logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**: The request failed.
        self.success = success
        # The total number of instances.
        self.total = total
        # The trace ID, which is used to track the request.
        self.trace_id = trace_id

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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetPagedInstanceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class GetPagedInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        instance: List[main_models.GetPagedInstanceResponseBodyDataInstance] = None,
    ):
        # The information about the task.
        self.instance = instance

    def validate(self):
        if self.instance:
            for v1 in self.instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instance'] = []
        if self.instance is not None:
            for k1 in self.instance:
                result['Instance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k1 in m.get('Instance'):
                temp_model = main_models.GetPagedInstanceResponseBodyDataInstance()
                self.instance.append(temp_model.from_map(k1))

        return self

class GetPagedInstanceResponseBodyDataInstance(DaraModel):
    def __init__(
        self,
        business_time: str = None,
        check_status: int = None,
        dag_id: int = None,
        delete: str = None,
        end_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        history_dag_id: int = None,
        id: int = None,
        last_running_context: str = None,
        msg: str = None,
        status: int = None,
        task_type: int = None,
        tenant_id: str = None,
        trigger_type: int = None,
        version: str = None,
    ):
        # The data timestamp of the task node.
        self.business_time = business_time
        # The state of archived data verification. Valid values:
        # 
        # *   **0**: The verification was successful.
        # *   **1**: Inconsistent data was detected.
        # *   **2**: The verification was not performed.
        # *   **3**: The verification is in progress.
        # *   **4**: The verification was interrupted.
        self.check_status = check_status
        # The unique ID of the task flow.
        self.dag_id = dag_id
        # Indicates whether the source data is deleted. Valid values:
        # 
        # *   **true**: deletes the jobs in the application group.
        # *   **false**
        self.delete = delete
        # The time when the task ended.
        self.end_time = end_time
        # The time when the task flow was created.
        self.gmt_create = gmt_create
        # The time when the task flow was last modified.
        self.gmt_modified = gmt_modified
        # The ID of the historical task flow.
        self.history_dag_id = history_dag_id
        # The task flow ID.
        self.id = id
        # The context of the last execution of the task flow.
        self.last_running_context = last_running_context
        # The details of the current task execution.
        self.msg = msg
        # The state of the archiving task.
        # 
        # *   **0**: Pending.
        # *   **1**: Running.
        # *   **2**: Paused.
        # *   **3**: Failed.
        # *   **4**: Succeeded.
        self.status = status
        # The task type. Valid values:
        # 
        # *   **1**: data archiving
        # *   **2**: archived data restoration
        # *   **3**: archived data verification
        self.task_type = task_type
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # The mode in which the task flow is triggered. Valid values:
        # 
        # *   **0**: The task flow was triggered based on a schedule.
        # *   **1**: The task flow was manually triggered.
        self.trigger_type = trigger_type
        # The version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_time is not None:
            result['BusinessTime'] = self.business_time

        if self.check_status is not None:
            result['CheckStatus'] = self.check_status

        if self.dag_id is not None:
            result['DagId'] = self.dag_id

        if self.delete is not None:
            result['Delete'] = self.delete

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.history_dag_id is not None:
            result['HistoryDagId'] = self.history_dag_id

        if self.id is not None:
            result['Id'] = self.id

        if self.last_running_context is not None:
            result['LastRunningContext'] = self.last_running_context

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.status is not None:
            result['Status'] = self.status

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessTime') is not None:
            self.business_time = m.get('BusinessTime')

        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')

        if m.get('DagId') is not None:
            self.dag_id = m.get('DagId')

        if m.get('Delete') is not None:
            self.delete = m.get('Delete')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('HistoryDagId') is not None:
            self.history_dag_id = m.get('HistoryDagId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LastRunningContext') is not None:
            self.last_running_context = m.get('LastRunningContext')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

