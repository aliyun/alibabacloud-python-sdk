# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_openitag20220616 import models as main_models
from darabonba.model import DaraModel

class TaskDetail(DaraModel):
    def __init__(
        self,
        admins: List[main_models.SimpleUser] = None,
        alert_time: int = None,
        allow_append_data: bool = None,
        archived: bool = None,
        archived_infos: str = None,
        assign_config: Dict[str, Any] = None,
        creator: main_models.SimpleUser = None,
        dataset_proxy_relations: List[main_models.TaskDetailDatasetProxyRelations] = None,
        exif: Dict[str, Any] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        label_style: str = None,
        mine_configs: Dict[str, Any] = None,
        modifier: main_models.SimpleUser = None,
        notice_config: Dict[str, Any] = None,
        period_config: Dict[str, Any] = None,
        ref_task_id: str = None,
        relate_task_config: Dict[str, Any] = None,
        remark: str = None,
        result_callback_config: Dict[str, Any] = None,
        stage: str = None,
        status: str = None,
        tags: List[str] = None,
        task_id: str = None,
        task_name: str = None,
        task_template_config: main_models.TaskDetailTaskTemplateConfig = None,
        task_type: str = None,
        task_workflow: List[main_models.TaskDetailTaskWorkflow] = None,
        template_id: str = None,
        tenant_id: str = None,
        tenant_name: str = None,
        uuid: str = None,
        vote_configs: Dict[str, Any] = None,
        workflow_nodes: List[str] = None,
        run_msg: str = None,
    ):
        # List of job administrators.
        self.admins = admins
        # Alert time.
        self.alert_time = alert_time
        # Indicates whether data appending is allowed.
        self.allow_append_data = allow_append_data
        # Indicates whether the job has been archived.
        self.archived = archived
        # Data archiving information.
        self.archived_infos = archived_infos
        # Job assignment configuration.
        self.assign_config = assign_config
        # Creator information.
        self.creator = creator
        # List of Data proxy relationships.
        self.dataset_proxy_relations = dataset_proxy_relations
        # Additional configuration.
        self.exif = exif
        # Creation UTC time.
        self.gmt_create_time = gmt_create_time
        # UTC time of the last modification.
        self.gmt_modified_time = gmt_modified_time
        # Annotation style.
        self.label_style = label_style
        # My configuration.
        self.mine_configs = mine_configs
        # Updated By information.
        self.modifier = modifier
        # Notice configuration.
        self.notice_config = notice_config
        # Time configuration.
        self.period_config = period_config
        # Auto triggered task ID.
        self.ref_task_id = ref_task_id
        # Related job configuration.
        self.relate_task_config = relate_task_config
        # Remark information.
        self.remark = remark
        # Result callback configuration.
        self.result_callback_config = result_callback_config
        # Current edge zone. Possible values:
        # - MARK: Annotating.
        # - CHECK: Checking.
        # - SAMPLING: Validating.
        self.stage = stage
        # Task Status. Possible values:
        # - CREATED
        # - SUCCESS
        self.status = status
        # List of job tags.
        self.tags = tags
        # Job ID.
        self.task_id = task_id
        # Task Name.
        self.task_name = task_name
        # Supplementary configuration for the Job template.
        self.task_template_config = task_template_config
        # Task Type.
        self.task_type = task_type
        # List of job stream configurations.
        self.task_workflow = task_workflow
        # Template ID.
        self.template_id = template_id
        # Tenant ID.
        self.tenant_id = tenant_id
        # Tenant name.
        self.tenant_name = tenant_name
        # UUID.
        self.uuid = uuid
        # Voting configuration.
        self.vote_configs = vote_configs
        # List of pipeline nodes.
        self.workflow_nodes = workflow_nodes
        # Run message.
        self.run_msg = run_msg

    def validate(self):
        if self.admins:
            for v1 in self.admins:
                 if v1:
                    v1.validate()
        if self.creator:
            self.creator.validate()
        if self.dataset_proxy_relations:
            for v1 in self.dataset_proxy_relations:
                 if v1:
                    v1.validate()
        if self.modifier:
            self.modifier.validate()
        if self.task_template_config:
            self.task_template_config.validate()
        if self.task_workflow:
            for v1 in self.task_workflow:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Admins'] = []
        if self.admins is not None:
            for k1 in self.admins:
                result['Admins'].append(k1.to_map() if k1 else None)

        if self.alert_time is not None:
            result['AlertTime'] = self.alert_time

        if self.allow_append_data is not None:
            result['AllowAppendData'] = self.allow_append_data

        if self.archived is not None:
            result['Archived'] = self.archived

        if self.archived_infos is not None:
            result['ArchivedInfos'] = self.archived_infos

        if self.assign_config is not None:
            result['AssignConfig'] = self.assign_config

        if self.creator is not None:
            result['Creator'] = self.creator.to_map()

        result['DatasetProxyRelations'] = []
        if self.dataset_proxy_relations is not None:
            for k1 in self.dataset_proxy_relations:
                result['DatasetProxyRelations'].append(k1.to_map() if k1 else None)

        if self.exif is not None:
            result['Exif'] = self.exif

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.label_style is not None:
            result['LabelStyle'] = self.label_style

        if self.mine_configs is not None:
            result['MineConfigs'] = self.mine_configs

        if self.modifier is not None:
            result['Modifier'] = self.modifier.to_map()

        if self.notice_config is not None:
            result['NoticeConfig'] = self.notice_config

        if self.period_config is not None:
            result['PeriodConfig'] = self.period_config

        if self.ref_task_id is not None:
            result['RefTaskId'] = self.ref_task_id

        if self.relate_task_config is not None:
            result['RelateTaskConfig'] = self.relate_task_config

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.result_callback_config is not None:
            result['ResultCallbackConfig'] = self.result_callback_config

        if self.stage is not None:
            result['Stage'] = self.stage

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_template_config is not None:
            result['TaskTemplateConfig'] = self.task_template_config.to_map()

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        result['TaskWorkflow'] = []
        if self.task_workflow is not None:
            for k1 in self.task_workflow:
                result['TaskWorkflow'].append(k1.to_map() if k1 else None)

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name

        if self.uuid is not None:
            result['UUID'] = self.uuid

        if self.vote_configs is not None:
            result['VoteConfigs'] = self.vote_configs

        if self.workflow_nodes is not None:
            result['WorkflowNodes'] = self.workflow_nodes

        if self.run_msg is not None:
            result['runMsg'] = self.run_msg

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.admins = []
        if m.get('Admins') is not None:
            for k1 in m.get('Admins'):
                temp_model = main_models.SimpleUser()
                self.admins.append(temp_model.from_map(k1))

        if m.get('AlertTime') is not None:
            self.alert_time = m.get('AlertTime')

        if m.get('AllowAppendData') is not None:
            self.allow_append_data = m.get('AllowAppendData')

        if m.get('Archived') is not None:
            self.archived = m.get('Archived')

        if m.get('ArchivedInfos') is not None:
            self.archived_infos = m.get('ArchivedInfos')

        if m.get('AssignConfig') is not None:
            self.assign_config = m.get('AssignConfig')

        if m.get('Creator') is not None:
            temp_model = main_models.SimpleUser()
            self.creator = temp_model.from_map(m.get('Creator'))

        self.dataset_proxy_relations = []
        if m.get('DatasetProxyRelations') is not None:
            for k1 in m.get('DatasetProxyRelations'):
                temp_model = main_models.TaskDetailDatasetProxyRelations()
                self.dataset_proxy_relations.append(temp_model.from_map(k1))

        if m.get('Exif') is not None:
            self.exif = m.get('Exif')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('LabelStyle') is not None:
            self.label_style = m.get('LabelStyle')

        if m.get('MineConfigs') is not None:
            self.mine_configs = m.get('MineConfigs')

        if m.get('Modifier') is not None:
            temp_model = main_models.SimpleUser()
            self.modifier = temp_model.from_map(m.get('Modifier'))

        if m.get('NoticeConfig') is not None:
            self.notice_config = m.get('NoticeConfig')

        if m.get('PeriodConfig') is not None:
            self.period_config = m.get('PeriodConfig')

        if m.get('RefTaskId') is not None:
            self.ref_task_id = m.get('RefTaskId')

        if m.get('RelateTaskConfig') is not None:
            self.relate_task_config = m.get('RelateTaskConfig')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResultCallbackConfig') is not None:
            self.result_callback_config = m.get('ResultCallbackConfig')

        if m.get('Stage') is not None:
            self.stage = m.get('Stage')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskTemplateConfig') is not None:
            temp_model = main_models.TaskDetailTaskTemplateConfig()
            self.task_template_config = temp_model.from_map(m.get('TaskTemplateConfig'))

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        self.task_workflow = []
        if m.get('TaskWorkflow') is not None:
            for k1 in m.get('TaskWorkflow'):
                temp_model = main_models.TaskDetailTaskWorkflow()
                self.task_workflow.append(temp_model.from_map(k1))

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')

        if m.get('UUID') is not None:
            self.uuid = m.get('UUID')

        if m.get('VoteConfigs') is not None:
            self.vote_configs = m.get('VoteConfigs')

        if m.get('WorkflowNodes') is not None:
            self.workflow_nodes = m.get('WorkflowNodes')

        if m.get('runMsg') is not None:
            self.run_msg = m.get('runMsg')

        return self

class TaskDetailTaskWorkflow(DaraModel):
    def __init__(
        self,
        exif: Dict[str, Any] = None,
        groups: List[str] = None,
        node_name: str = None,
        users: List[main_models.SimpleUser] = None,
    ):
        # Extra information.
        self.exif = exif
        # Group list.
        self.groups = groups
        # Edge zone name. Possible values:  
        # - MARK  
        # - CHECK  
        # - SAMPLING
        self.node_name = node_name
        # User List.
        self.users = users

    def validate(self):
        if self.users:
            for v1 in self.users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exif is not None:
            result['Exif'] = self.exif

        if self.groups is not None:
            result['Groups'] = self.groups

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        result['Users'] = []
        if self.users is not None:
            for k1 in self.users:
                result['Users'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')

        if m.get('Groups') is not None:
            self.groups = m.get('Groups')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        self.users = []
        if m.get('Users') is not None:
            for k1 in m.get('Users'):
                temp_model = main_models.SimpleUser()
                self.users.append(temp_model.from_map(k1))

        return self

class TaskDetailTaskTemplateConfig(DaraModel):
    def __init__(
        self,
        exif: Dict[str, Any] = None,
        resource_key: str = None,
        robot_config: Dict[str, Any] = None,
        select_questions: List[str] = None,
        template_option_map: Dict[str, Any] = None,
        template_relation_id: str = None,
    ):
        # Additional information for template configuration.
        self.exif = exif
        # Resource key.
        self.resource_key = resource_key
        # Robot configuration.
        self.robot_config = robot_config
        # If the number of questions in the Job is less than that in the template, you can select the required questions from the List.
        self.select_questions = select_questions
        # Options configuration.
        self.template_option_map = template_option_map
        # Template relation ID.
        self.template_relation_id = template_relation_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exif is not None:
            result['Exif'] = self.exif

        if self.resource_key is not None:
            result['ResourceKey'] = self.resource_key

        if self.robot_config is not None:
            result['RobotConfig'] = self.robot_config

        if self.select_questions is not None:
            result['SelectQuestions'] = self.select_questions

        if self.template_option_map is not None:
            result['TemplateOptionMap'] = self.template_option_map

        if self.template_relation_id is not None:
            result['TemplateRelationId'] = self.template_relation_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')

        if m.get('ResourceKey') is not None:
            self.resource_key = m.get('ResourceKey')

        if m.get('RobotConfig') is not None:
            self.robot_config = m.get('RobotConfig')

        if m.get('SelectQuestions') is not None:
            self.select_questions = m.get('SelectQuestions')

        if m.get('TemplateOptionMap') is not None:
            self.template_option_map = m.get('TemplateOptionMap')

        if m.get('TemplateRelationId') is not None:
            self.template_relation_id = m.get('TemplateRelationId')

        return self

class TaskDetailDatasetProxyRelations(DaraModel):
    def __init__(
        self,
        dataset_id: str = None,
        dataset_type: str = None,
        exif: Dict[str, Any] = None,
        source: str = None,
        source_biz_id: str = None,
        source_dataset_id: str = None,
    ):
        # Dataset ID.
        self.dataset_id = dataset_id
        # Dataset type.
        self.dataset_type = dataset_type
        # Additional information.
        self.exif = exif
        # Dataset source.
        self.source = source
        # Source business ID.
        self.source_biz_id = source_biz_id
        # Source dataset ID.
        self.source_dataset_id = source_dataset_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.dataset_type is not None:
            result['DatasetType'] = self.dataset_type

        if self.exif is not None:
            result['Exif'] = self.exif

        if self.source is not None:
            result['Source'] = self.source

        if self.source_biz_id is not None:
            result['SourceBizId'] = self.source_biz_id

        if self.source_dataset_id is not None:
            result['SourceDatasetId'] = self.source_dataset_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('DatasetType') is not None:
            self.dataset_type = m.get('DatasetType')

        if m.get('Exif') is not None:
            self.exif = m.get('Exif')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceBizId') is not None:
            self.source_biz_id = m.get('SourceBizId')

        if m.get('SourceDatasetId') is not None:
            self.source_dataset_id = m.get('SourceDatasetId')

        return self

