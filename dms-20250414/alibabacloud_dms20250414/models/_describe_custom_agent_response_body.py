# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class DescribeCustomAgentResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeCustomAgentResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_message = error_message
        # Id of the request
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
        if m.get('Data') is not None:
            temp_model = main_models.DescribeCustomAgentResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeCustomAgentResponseBodyData(DaraModel):
    def __init__(
        self,
        aliyun_parent_uid: str = None,
        aliyun_uid: str = None,
        creator_user_name: str = None,
        custom_agent_id: str = None,
        data_json: str = None,
        description: str = None,
        dms_unit: str = None,
        execution_config: main_models.DescribeCustomAgentResponseBodyDataExecutionConfig = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        instruction: str = None,
        knowledge: str = None,
        modifier: str = None,
        modifier_user_name: str = None,
        name: str = None,
        offline_time: str = None,
        region: str = None,
        release_time: str = None,
        status: str = None,
        text_report_config: str = None,
        web_report_config: str = None,
        workspace_id: str = None,
    ):
        self.aliyun_parent_uid = aliyun_parent_uid
        self.aliyun_uid = aliyun_uid
        self.creator_user_name = creator_user_name
        self.custom_agent_id = custom_agent_id
        self.data_json = data_json
        self.description = description
        self.dms_unit = dms_unit
        self.execution_config = execution_config
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.instruction = instruction
        self.knowledge = knowledge
        self.modifier = modifier
        self.modifier_user_name = modifier_user_name
        self.name = name
        self.offline_time = offline_time
        self.region = region
        self.release_time = release_time
        self.status = status
        self.text_report_config = text_report_config
        self.web_report_config = web_report_config
        self.workspace_id = workspace_id

    def validate(self):
        if self.execution_config:
            self.execution_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_parent_uid is not None:
            result['AliyunParentUid'] = self.aliyun_parent_uid

        if self.aliyun_uid is not None:
            result['AliyunUid'] = self.aliyun_uid

        if self.creator_user_name is not None:
            result['CreatorUserName'] = self.creator_user_name

        if self.custom_agent_id is not None:
            result['CustomAgentId'] = self.custom_agent_id

        if self.data_json is not None:
            result['DataJson'] = self.data_json

        if self.description is not None:
            result['Description'] = self.description

        if self.dms_unit is not None:
            result['DmsUnit'] = self.dms_unit

        if self.execution_config is not None:
            result['ExecutionConfig'] = self.execution_config.to_map()

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.instruction is not None:
            result['Instruction'] = self.instruction

        if self.knowledge is not None:
            result['Knowledge'] = self.knowledge

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.modifier_user_name is not None:
            result['ModifierUserName'] = self.modifier_user_name

        if self.name is not None:
            result['Name'] = self.name

        if self.offline_time is not None:
            result['OfflineTime'] = self.offline_time

        if self.region is not None:
            result['Region'] = self.region

        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time

        if self.status is not None:
            result['Status'] = self.status

        if self.text_report_config is not None:
            result['TextReportConfig'] = self.text_report_config

        if self.web_report_config is not None:
            result['WebReportConfig'] = self.web_report_config

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunParentUid') is not None:
            self.aliyun_parent_uid = m.get('AliyunParentUid')

        if m.get('AliyunUid') is not None:
            self.aliyun_uid = m.get('AliyunUid')

        if m.get('CreatorUserName') is not None:
            self.creator_user_name = m.get('CreatorUserName')

        if m.get('CustomAgentId') is not None:
            self.custom_agent_id = m.get('CustomAgentId')

        if m.get('DataJson') is not None:
            self.data_json = m.get('DataJson')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DmsUnit') is not None:
            self.dms_unit = m.get('DmsUnit')

        if m.get('ExecutionConfig') is not None:
            temp_model = main_models.DescribeCustomAgentResponseBodyDataExecutionConfig()
            self.execution_config = temp_model.from_map(m.get('ExecutionConfig'))

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Instruction') is not None:
            self.instruction = m.get('Instruction')

        if m.get('Knowledge') is not None:
            self.knowledge = m.get('Knowledge')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('ModifierUserName') is not None:
            self.modifier_user_name = m.get('ModifierUserName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OfflineTime') is not None:
            self.offline_time = m.get('OfflineTime')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TextReportConfig') is not None:
            self.text_report_config = m.get('TextReportConfig')

        if m.get('WebReportConfig') is not None:
            self.web_report_config = m.get('WebReportConfig')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class DescribeCustomAgentResponseBodyDataExecutionConfig(DaraModel):
    def __init__(
        self,
        skip_ask_human: bool = None,
        skip_plan: bool = None,
        skip_sql_confirm: bool = None,
        skip_web_report_confirm: bool = None,
    ):
        self.skip_ask_human = skip_ask_human
        self.skip_plan = skip_plan
        self.skip_sql_confirm = skip_sql_confirm
        self.skip_web_report_confirm = skip_web_report_confirm

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.skip_ask_human is not None:
            result['SkipAskHuman'] = self.skip_ask_human

        if self.skip_plan is not None:
            result['SkipPlan'] = self.skip_plan

        if self.skip_sql_confirm is not None:
            result['SkipSqlConfirm'] = self.skip_sql_confirm

        if self.skip_web_report_confirm is not None:
            result['SkipWebReportConfirm'] = self.skip_web_report_confirm

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkipAskHuman') is not None:
            self.skip_ask_human = m.get('SkipAskHuman')

        if m.get('SkipPlan') is not None:
            self.skip_plan = m.get('SkipPlan')

        if m.get('SkipSqlConfirm') is not None:
            self.skip_sql_confirm = m.get('SkipSqlConfirm')

        if m.get('SkipWebReportConfirm') is not None:
            self.skip_web_report_confirm = m.get('SkipWebReportConfirm')

        return self

