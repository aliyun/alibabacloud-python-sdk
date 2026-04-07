# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetNodeResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetNodeResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the node.
        self.data = data
        # The ID of the node. You can call the [ListNodes](https://help.aliyun.com/document_detail/173979.html) operation to query the node ID.
        self.error_code = error_code
        # The connection string.
        self.error_message = error_message
        # The operation that you want to perform. Set the value to **GetNode**.
        self.http_status_code = http_status_code
        # Other parameters.
        self.request_id = request_id
        # The ID of the workflow.
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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetNodeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetNodeResponseBodyData(DaraModel):
    def __init__(
        self,
        baseline_id: int = None,
        business_id: int = None,
        connection: str = None,
        create_time: int = None,
        cron_express: str = None,
        deploy_date: int = None,
        description: str = None,
        dqc_description: str = None,
        dqc_type: int = None,
        file_id: int = None,
        file_type: int = None,
        file_version: int = None,
        modify_time: int = None,
        node_id: int = None,
        node_name: str = None,
        owner_id: str = None,
        param_values: str = None,
        priority: int = None,
        program_type: str = None,
        project_id: int = None,
        related_flow_id: int = None,
        repeat_interval: int = None,
        repeat_mode: int = None,
        repeatability: str = None,
        res_group_identifier: str = None,
        res_group_name: str = None,
        scheduler_type: str = None,
    ):
        # The description of the node.
        self.baseline_id = baseline_id
        # The operation that you want to perform. Set the value to **GetNode**.
        self.business_id = business_id
        # The environment of the workspace. Valid values: PROD and DEV.
        self.connection = connection
        # The creation time.
        self.create_time = create_time
        # The environment of the workspace. Valid values: PROD and DEV.
        self.cron_express = cron_express
        # The deployment date.
        self.deploy_date = deploy_date
        # The name of the resource group.
        self.description = description
        # The ID of the node. You can call the [ListNodes](https://help.aliyun.com/document_detail/173979.html) operation to query the node ID.
        self.dqc_description = dqc_description
        # The error message returned.
        self.dqc_type = dqc_type
        # The file ID.
        # 
        # **
        # 
        # **Warning** The field is deprecated.
        self.file_id = file_id
        # The file type. Different file types have different codes. For more information, see [DataWorks node collection](https://help.aliyun.com/document_detail/600169.html).
        self.file_type = file_type
        # The version of the file.
        self.file_version = file_version
        # The modification time.
        self.modify_time = modify_time
        # The HTTP status code returned.
        self.node_id = node_id
        # The scheduling type of the node. Valid values:
        # 
        # *   NORMAL: The node is an auto triggered node.
        # *   MANUAL: The node is a manually triggered node. Manually triggered nodes cannot be automatically triggered.
        # *   PAUSE: The node is a paused node.
        # *   SKIP: The node is a dry-run node. Dry-run nodes are started as scheduled but the system sets the status of the nodes to successful when it starts to run them.
        self.node_name = node_name
        # The ID of the node.
        self.owner_id = owner_id
        # The CRON expression returned.
        self.param_values = param_values
        # The HTTP status code returned.
        self.priority = priority
        # The ID of the owner of the node.
        self.program_type = program_type
        # Indicates whether the node can be rerun.
        self.project_id = project_id
        # Indicates whether the node is associated with Data Quality. Valid values: 0 and 1. A value of 0 indicates that the node is associated with Data Quality. A value of 1 indicates that the node is not associated with Data Quality.
        self.related_flow_id = related_flow_id
        # The ID of the workflow to which the node belongs.
        self.repeat_interval = repeat_interval
        # Rerun mode. 0 indicates that you can rerun only if you fail, 1 indicates that you can rerun in all cases, and 2 indicates that you cannot rerun in all cases.
        self.repeat_mode = repeat_mode
        # The type of the node.
        self.repeatability = repeatability
        # The unique identifier of the resource group.
        self.res_group_identifier = res_group_identifier
        # The ID of the request. You can use the ID to locate logs and troubleshoot issues.
        self.res_group_name = res_group_name
        # The ID of the workspace.
        self.scheduler_type = scheduler_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        if self.business_id is not None:
            result['BusinessId'] = self.business_id

        if self.connection is not None:
            result['Connection'] = self.connection

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cron_express is not None:
            result['CronExpress'] = self.cron_express

        if self.deploy_date is not None:
            result['DeployDate'] = self.deploy_date

        if self.description is not None:
            result['Description'] = self.description

        if self.dqc_description is not None:
            result['DqcDescription'] = self.dqc_description

        if self.dqc_type is not None:
            result['DqcType'] = self.dqc_type

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.file_version is not None:
            result['FileVersion'] = self.file_version

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.param_values is not None:
            result['ParamValues'] = self.param_values

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.program_type is not None:
            result['ProgramType'] = self.program_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.related_flow_id is not None:
            result['RelatedFlowId'] = self.related_flow_id

        if self.repeat_interval is not None:
            result['RepeatInterval'] = self.repeat_interval

        if self.repeat_mode is not None:
            result['RepeatMode'] = self.repeat_mode

        if self.repeatability is not None:
            result['Repeatability'] = self.repeatability

        if self.res_group_identifier is not None:
            result['ResGroupIdentifier'] = self.res_group_identifier

        if self.res_group_name is not None:
            result['ResGroupName'] = self.res_group_name

        if self.scheduler_type is not None:
            result['SchedulerType'] = self.scheduler_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')

        if m.get('Connection') is not None:
            self.connection = m.get('Connection')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CronExpress') is not None:
            self.cron_express = m.get('CronExpress')

        if m.get('DeployDate') is not None:
            self.deploy_date = m.get('DeployDate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DqcDescription') is not None:
            self.dqc_description = m.get('DqcDescription')

        if m.get('DqcType') is not None:
            self.dqc_type = m.get('DqcType')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('FileVersion') is not None:
            self.file_version = m.get('FileVersion')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ParamValues') is not None:
            self.param_values = m.get('ParamValues')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ProgramType') is not None:
            self.program_type = m.get('ProgramType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RelatedFlowId') is not None:
            self.related_flow_id = m.get('RelatedFlowId')

        if m.get('RepeatInterval') is not None:
            self.repeat_interval = m.get('RepeatInterval')

        if m.get('RepeatMode') is not None:
            self.repeat_mode = m.get('RepeatMode')

        if m.get('Repeatability') is not None:
            self.repeatability = m.get('Repeatability')

        if m.get('ResGroupIdentifier') is not None:
            self.res_group_identifier = m.get('ResGroupIdentifier')

        if m.get('ResGroupName') is not None:
            self.res_group_name = m.get('ResGroupName')

        if m.get('SchedulerType') is not None:
            self.scheduler_type = m.get('SchedulerType')

        return self

