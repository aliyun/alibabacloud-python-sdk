# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListDDLPublishRecordsResponseBody(DaraModel):
    def __init__(
        self,
        ddlpublish_record_list: List[main_models.ListDDLPublishRecordsResponseBodyDDLPublishRecordList] = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the publishing records.
        self.ddlpublish_record_list = ddlpublish_record_list
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.ddlpublish_record_list:
            for v1 in self.ddlpublish_record_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DDLPublishRecordList'] = []
        if self.ddlpublish_record_list is not None:
            for k1 in self.ddlpublish_record_list:
                result['DDLPublishRecordList'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ddlpublish_record_list = []
        if m.get('DDLPublishRecordList') is not None:
            for k1 in m.get('DDLPublishRecordList'):
                temp_model = main_models.ListDDLPublishRecordsResponseBodyDDLPublishRecordList()
                self.ddlpublish_record_list.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDDLPublishRecordsResponseBodyDDLPublishRecordList(DaraModel):
    def __init__(
        self,
        audit_expire_time: str = None,
        audit_status: str = None,
        comment: str = None,
        creator_id: int = None,
        finality: bool = None,
        finality_reason: str = None,
        publish_status: str = None,
        publish_task_info_list: List[main_models.ListDDLPublishRecordsResponseBodyDDLPublishRecordListPublishTaskInfoList] = None,
        risk_level: str = None,
        status_desc: str = None,
        workflow_instance_id: int = None,
    ):
        # The time when the approval expires.
        self.audit_expire_time = audit_expire_time
        # The approval state of the ticket. Valid values:
        # 
        # *   **EXEMPT_PASS**: The ticket passes without approval.
        # *   **TO_AUDIT**: The ticket is pending for approval.
        # *   **CANCEL**: The ticket is canceled.
        # *   **SUCCESS**: The ticket is approved.
        # *   **FAIL**: The ticket fails to pass the approval.
        self.audit_status = audit_status
        # Release remarks.
        self.comment = comment
        # The ID of the user who creates the ticket. You can obtain the user ID by calling the [GetUser](https://help.aliyun.com/document_detail/147098.html) operation and querying the value of the UserId parameter. The value is not the unique ID (UID) of the Alibaba Cloud account.
        self.creator_id = creator_id
        # Indicates whether the approval is terminated. Valid values:
        # 
        # *   **true**: The approval is terminated.
        # *   **false**: The approval is not terminated.
        # 
        # > Multiple reasons can terminate the approval. For example, you withdraw the application or your ticket is not approved before the specified time.
        self.finality = finality
        # The reason for the termination.
        self.finality_reason = finality_reason
        # The publishing state of the ticket. Valid values:
        # 
        # *   **START**: The ticket is created.
        # *   **ANALYZE**: The ticket is under analysis.
        # *   **AUDIT**: The ticket is under approval.
        # *   **DISPATCH**: A task is generated for the ticket.
        # *   **SUCCESS**: The task is successful.
        self.publish_status = publish_status
        # The list of publishing tasks.
        self.publish_task_info_list = publish_task_info_list
        # The risk level of the operation. Valid values:
        # 
        # *   **NONE_RISK**: The operation does not have risks.
        # *   **LOW_RISK**: The operation is at low risk.
        # *   **MIDDLE_RISK**: The operation is at medium risk.
        # *   **HIGH_RISK**: The operation is at high risk.
        self.risk_level = risk_level
        # The description of the publishing state.
        self.status_desc = status_desc
        # The ID of the approval process.
        self.workflow_instance_id = workflow_instance_id

    def validate(self):
        if self.publish_task_info_list:
            for v1 in self.publish_task_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_expire_time is not None:
            result['AuditExpireTime'] = self.audit_expire_time

        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.finality is not None:
            result['Finality'] = self.finality

        if self.finality_reason is not None:
            result['FinalityReason'] = self.finality_reason

        if self.publish_status is not None:
            result['PublishStatus'] = self.publish_status

        result['PublishTaskInfoList'] = []
        if self.publish_task_info_list is not None:
            for k1 in self.publish_task_info_list:
                result['PublishTaskInfoList'].append(k1.to_map() if k1 else None)

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc

        if self.workflow_instance_id is not None:
            result['WorkflowInstanceId'] = self.workflow_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditExpireTime') is not None:
            self.audit_expire_time = m.get('AuditExpireTime')

        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('Finality') is not None:
            self.finality = m.get('Finality')

        if m.get('FinalityReason') is not None:
            self.finality_reason = m.get('FinalityReason')

        if m.get('PublishStatus') is not None:
            self.publish_status = m.get('PublishStatus')

        self.publish_task_info_list = []
        if m.get('PublishTaskInfoList') is not None:
            for k1 in m.get('PublishTaskInfoList'):
                temp_model = main_models.ListDDLPublishRecordsResponseBodyDDLPublishRecordListPublishTaskInfoList()
                self.publish_task_info_list.append(temp_model.from_map(k1))

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')

        if m.get('WorkflowInstanceId') is not None:
            self.workflow_instance_id = m.get('WorkflowInstanceId')

        return self

class ListDDLPublishRecordsResponseBodyDDLPublishRecordListPublishTaskInfoList(DaraModel):
    def __init__(
        self,
        db_id: int = None,
        logic: bool = None,
        plan_time: str = None,
        publish_job_list: List[main_models.ListDDLPublishRecordsResponseBodyDDLPublishRecordListPublishTaskInfoListPublishJobList] = None,
        publish_strategy: str = None,
        status_desc: str = None,
        task_job_status: str = None,
    ):
        # The ID of the database.
        self.db_id = db_id
        # Indicates whether the database is a logical database. Valid values:
        # 
        # *   **true**: The database is a logical database.
        # *   **false**: the database is not a logical database.
        self.logic = logic
        # The time to publish the ticket.
        self.plan_time = plan_time
        # The list of the publishing tasks.
        self.publish_job_list = publish_job_list
        # The publishing policy. Valid values:
        # 
        # *   **IMMEDIATELY**: immediately publishes the ticket.
        # *   **REGULARLY**: publishes the ticket at a scheduled time.
        self.publish_strategy = publish_strategy
        # The description of the state.
        self.status_desc = status_desc
        # The state of the task.
        self.task_job_status = task_job_status

    def validate(self):
        if self.publish_job_list:
            for v1 in self.publish_job_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.plan_time is not None:
            result['PlanTime'] = self.plan_time

        result['PublishJobList'] = []
        if self.publish_job_list is not None:
            for k1 in self.publish_job_list:
                result['PublishJobList'].append(k1.to_map() if k1 else None)

        if self.publish_strategy is not None:
            result['PublishStrategy'] = self.publish_strategy

        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc

        if self.task_job_status is not None:
            result['TaskJobStatus'] = self.task_job_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('PlanTime') is not None:
            self.plan_time = m.get('PlanTime')

        self.publish_job_list = []
        if m.get('PublishJobList') is not None:
            for k1 in m.get('PublishJobList'):
                temp_model = main_models.ListDDLPublishRecordsResponseBodyDDLPublishRecordListPublishTaskInfoListPublishJobList()
                self.publish_job_list.append(temp_model.from_map(k1))

        if m.get('PublishStrategy') is not None:
            self.publish_strategy = m.get('PublishStrategy')

        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')

        if m.get('TaskJobStatus') is not None:
            self.task_job_status = m.get('TaskJobStatus')

        return self

class ListDDLPublishRecordsResponseBodyDDLPublishRecordListPublishTaskInfoListPublishJobList(DaraModel):
    def __init__(
        self,
        dbtask_group_id: int = None,
        execute_count: int = None,
        scripts: str = None,
        status_desc: str = None,
        table_name: str = None,
        task_job_status: str = None,
    ):
        # The ID of the SQL task group.
        self.dbtask_group_id = dbtask_group_id
        # The number of SQL statements that are executed.
        self.execute_count = execute_count
        # The script for data changes.
        self.scripts = scripts
        # The description of the state.
        self.status_desc = status_desc
        # The name of the table after the change.
        self.table_name = table_name
        # The state of the publishing task. Valid values:
        # 
        # *   **NONE**: The state of the task is unknown.
        # *   **SUCCESS**: The task is successful.
        # *   **FAIL**: The task fails.
        self.task_job_status = task_job_status

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

        if self.scripts is not None:
            result['Scripts'] = self.scripts

        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.task_job_status is not None:
            result['TaskJobStatus'] = self.task_job_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBTaskGroupId') is not None:
            self.dbtask_group_id = m.get('DBTaskGroupId')

        if m.get('ExecuteCount') is not None:
            self.execute_count = m.get('ExecuteCount')

        if m.get('Scripts') is not None:
            self.scripts = m.get('Scripts')

        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TaskJobStatus') is not None:
            self.task_job_status = m.get('TaskJobStatus')

        return self

