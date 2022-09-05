# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class SimpleUser(TeaModel):
    def __init__(
        self,
        account_no: str = None,
        account_type: str = None,
        role: str = None,
        user_id: int = None,
        user_name: str = None,
    ):
        self.account_no = account_no
        self.account_type = account_type
        self.role = role
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_no is not None:
            result['AccountNo'] = self.account_no
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.role is not None:
            result['Role'] = self.role
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNo') is not None:
            self.account_no = m.get('AccountNo')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateTaskDetailAdmins(TeaModel):
    def __init__(
        self,
        users: List[SimpleUser] = None,
    ):
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = SimpleUser()
                self.users.append(temp_model.from_map(k))
        return self


class CreateTaskDetailTaskWorkflow(TeaModel):
    def __init__(
        self,
        node_name: str = None,
    ):
        self.node_name = node_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        return self


class TaskAssginConfig(TeaModel):
    def __init__(
        self,
        assign_count: int = None,
        assign_field: str = None,
        assign_sub_task_count: str = None,
        assign_type: str = None,
    ):
        self.assign_count = assign_count
        self.assign_field = assign_field
        self.assign_sub_task_count = assign_sub_task_count
        self.assign_type = assign_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assign_count is not None:
            result['AssignCount'] = self.assign_count
        if self.assign_field is not None:
            result['AssignField'] = self.assign_field
        if self.assign_sub_task_count is not None:
            result['AssignSubTaskCount'] = self.assign_sub_task_count
        if self.assign_type is not None:
            result['AssignType'] = self.assign_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssignCount') is not None:
            self.assign_count = m.get('AssignCount')
        if m.get('AssignField') is not None:
            self.assign_field = m.get('AssignField')
        if m.get('AssignSubTaskCount') is not None:
            self.assign_sub_task_count = m.get('AssignSubTaskCount')
        if m.get('AssignType') is not None:
            self.assign_type = m.get('AssignType')
        return self


class DatasetProxyConfig(TeaModel):
    def __init__(
        self,
        dataset_type: str = None,
        source: str = None,
        source_dataset_id: str = None,
    ):
        self.dataset_type = dataset_type
        self.source = source
        self.source_dataset_id = source_dataset_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_type is not None:
            result['DatasetType'] = self.dataset_type
        if self.source is not None:
            result['Source'] = self.source
        if self.source_dataset_id is not None:
            result['SourceDatasetId'] = self.source_dataset_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetType') is not None:
            self.dataset_type = m.get('DatasetType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceDatasetId') is not None:
            self.source_dataset_id = m.get('SourceDatasetId')
        return self


class TaskTemplateConfig(TeaModel):
    def __init__(
        self,
        exif: Dict[str, str] = None,
        resource_key: str = None,
        select_questions: List[str] = None,
        template_option_map: Dict[str, str] = None,
        template_relation_id: str = None,
    ):
        self.exif = exif
        self.resource_key = resource_key
        self.select_questions = select_questions
        self.template_option_map = template_option_map
        self.template_relation_id = template_relation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exif is not None:
            result['Exif'] = self.exif
        if self.resource_key is not None:
            result['ResourceKey'] = self.resource_key
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
        if m.get('SelectQuestions') is not None:
            self.select_questions = m.get('SelectQuestions')
        if m.get('TemplateOptionMap') is not None:
            self.template_option_map = m.get('TemplateOptionMap')
        if m.get('TemplateRelationId') is not None:
            self.template_relation_id = m.get('TemplateRelationId')
        return self


class CreateTaskDetail(TeaModel):
    def __init__(
        self,
        admins: CreateTaskDetailAdmins = None,
        allow_append_data: bool = None,
        assign_config: TaskAssginConfig = None,
        dataset_proxy_relations: List[DatasetProxyConfig] = None,
        exif: Dict[str, Any] = None,
        tags: List[str] = None,
        task_name: str = None,
        task_template_config: TaskTemplateConfig = None,
        task_workflow: List[CreateTaskDetailTaskWorkflow] = None,
        template_id: str = None,
        uuid: str = None,
    ):
        self.admins = admins
        self.allow_append_data = allow_append_data
        self.assign_config = assign_config
        self.dataset_proxy_relations = dataset_proxy_relations
        self.exif = exif
        self.tags = tags
        self.task_name = task_name
        self.task_template_config = task_template_config
        self.task_workflow = task_workflow
        self.template_id = template_id
        self.uuid = uuid

    def validate(self):
        if self.admins:
            self.admins.validate()
        if self.assign_config:
            self.assign_config.validate()
        if self.dataset_proxy_relations:
            for k in self.dataset_proxy_relations:
                if k:
                    k.validate()
        if self.task_template_config:
            self.task_template_config.validate()
        if self.task_workflow:
            for k in self.task_workflow:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admins is not None:
            result['Admins'] = self.admins.to_map()
        if self.allow_append_data is not None:
            result['AllowAppendData'] = self.allow_append_data
        if self.assign_config is not None:
            result['AssignConfig'] = self.assign_config.to_map()
        result['DatasetProxyRelations'] = []
        if self.dataset_proxy_relations is not None:
            for k in self.dataset_proxy_relations:
                result['DatasetProxyRelations'].append(k.to_map() if k else None)
        if self.exif is not None:
            result['Exif'] = self.exif
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_template_config is not None:
            result['TaskTemplateConfig'] = self.task_template_config.to_map()
        result['TaskWorkflow'] = []
        if self.task_workflow is not None:
            for k in self.task_workflow:
                result['TaskWorkflow'].append(k.to_map() if k else None)
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.uuid is not None:
            result['UUID'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Admins') is not None:
            temp_model = CreateTaskDetailAdmins()
            self.admins = temp_model.from_map(m['Admins'])
        if m.get('AllowAppendData') is not None:
            self.allow_append_data = m.get('AllowAppendData')
        if m.get('AssignConfig') is not None:
            temp_model = TaskAssginConfig()
            self.assign_config = temp_model.from_map(m['AssignConfig'])
        self.dataset_proxy_relations = []
        if m.get('DatasetProxyRelations') is not None:
            for k in m.get('DatasetProxyRelations'):
                temp_model = DatasetProxyConfig()
                self.dataset_proxy_relations.append(temp_model.from_map(k))
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskTemplateConfig') is not None:
            temp_model = TaskTemplateConfig()
            self.task_template_config = temp_model.from_map(m['TaskTemplateConfig'])
        self.task_workflow = []
        if m.get('TaskWorkflow') is not None:
            for k in m.get('TaskWorkflow'):
                temp_model = CreateTaskDetailTaskWorkflow()
                self.task_workflow.append(temp_model.from_map(k))
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('UUID') is not None:
            self.uuid = m.get('UUID')
        return self


class FlowJobInfo(TeaModel):
    def __init__(
        self,
        display: bool = None,
        job_id: str = None,
        job_type: str = None,
        message_id: str = None,
        process_type: str = None,
        task_id: str = None,
    ):
        self.display = display
        self.job_id = job_id
        self.job_type = job_type
        self.message_id = message_id
        self.process_type = process_type
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['Display'] = self.display
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.process_type is not None:
            result['ProcessType'] = self.process_type
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('ProcessType') is not None:
            self.process_type = m.get('ProcessType')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class JobJobResult(TeaModel):
    def __init__(
        self,
        result_link: str = None,
    ):
        self.result_link = result_link

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.result_link is not None:
            result['ResultLink'] = self.result_link
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultLink') is not None:
            self.result_link = m.get('ResultLink')
        return self


class Job(TeaModel):
    def __init__(
        self,
        creator: SimpleUser = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        job_id: str = None,
        job_result: JobJobResult = None,
        job_type: str = None,
        status: str = None,
    ):
        self.creator = creator
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.job_id = job_id
        self.job_result = job_result
        self.job_type = job_type
        self.status = status

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.job_result:
            self.job_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['Creator'] = self.creator.to_map()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_result is not None:
            result['JobResult'] = self.job_result.to_map()
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            temp_model = SimpleUser()
            self.creator = temp_model.from_map(m['Creator'])
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobResult') is not None:
            temp_model = JobJobResult()
            self.job_result = temp_model.from_map(m['JobResult'])
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class MarkResult(TeaModel):
    def __init__(
        self,
        is_need_vote_judge: bool = None,
        mark_result: str = None,
        mark_result_id: str = None,
        mark_time: str = None,
        mark_title: str = None,
        progress: str = None,
        question_id: str = None,
        result_type: str = None,
        user_mark_result_id: str = None,
        version: str = None,
    ):
        self.is_need_vote_judge = is_need_vote_judge
        self.mark_result = mark_result
        self.mark_result_id = mark_result_id
        self.mark_time = mark_time
        self.mark_title = mark_title
        self.progress = progress
        self.question_id = question_id
        self.result_type = result_type
        self.user_mark_result_id = user_mark_result_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_need_vote_judge is not None:
            result['IsNeedVoteJudge'] = self.is_need_vote_judge
        if self.mark_result is not None:
            result['MarkResult'] = self.mark_result
        if self.mark_result_id is not None:
            result['MarkResultId'] = self.mark_result_id
        if self.mark_time is not None:
            result['MarkTime'] = self.mark_time
        if self.mark_title is not None:
            result['MarkTitle'] = self.mark_title
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.question_id is not None:
            result['QuestionId'] = self.question_id
        if self.result_type is not None:
            result['ResultType'] = self.result_type
        if self.user_mark_result_id is not None:
            result['UserMarkResultId'] = self.user_mark_result_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsNeedVoteJudge') is not None:
            self.is_need_vote_judge = m.get('IsNeedVoteJudge')
        if m.get('MarkResult') is not None:
            self.mark_result = m.get('MarkResult')
        if m.get('MarkResultId') is not None:
            self.mark_result_id = m.get('MarkResultId')
        if m.get('MarkTime') is not None:
            self.mark_time = m.get('MarkTime')
        if m.get('MarkTitle') is not None:
            self.mark_title = m.get('MarkTitle')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('QuestionId') is not None:
            self.question_id = m.get('QuestionId')
        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')
        if m.get('UserMarkResultId') is not None:
            self.user_mark_result_id = m.get('UserMarkResultId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class QuestionOption(TeaModel):
    def __init__(
        self,
        children: List['QuestionOption'] = None,
        color: str = None,
        key: str = None,
        label: str = None,
        remark: str = None,
        shortcut: str = None,
    ):
        self.children = children
        self.color = color
        self.key = key
        self.label = label
        self.remark = remark
        self.shortcut = shortcut

    def validate(self):
        if self.children:
            for k in self.children:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Children'] = []
        if self.children is not None:
            for k in self.children:
                result['Children'].append(k.to_map() if k else None)
        if self.color is not None:
            result['Color'] = self.color
        if self.key is not None:
            result['Key'] = self.key
        if self.label is not None:
            result['Label'] = self.label
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.shortcut is not None:
            result['Shortcut'] = self.shortcut
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.children = []
        if m.get('Children') is not None:
            for k in m.get('Children'):
                temp_model = QuestionOption()
                self.children.append(temp_model.from_map(k))
        if m.get('Color') is not None:
            self.color = m.get('Color')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Shortcut') is not None:
            self.shortcut = m.get('Shortcut')
        return self


class QuestionPlugin(TeaModel):
    def __init__(
        self,
        can_select: bool = None,
        children: List['QuestionPlugin'] = None,
        default_result: str = None,
        display: bool = None,
        exif: Dict[str, Any] = None,
        hot_key_map: str = None,
        mark_title: str = None,
        mark_title_alias: str = None,
        must_fill: bool = None,
        options: List[QuestionOption] = None,
        pre_options: List[str] = None,
        question_id: str = None,
        rule: str = None,
        select_group: str = None,
        selected: bool = None,
        type: str = None,
    ):
        self.can_select = can_select
        self.children = children
        self.default_result = default_result
        self.display = display
        self.exif = exif
        self.hot_key_map = hot_key_map
        self.mark_title = mark_title
        self.mark_title_alias = mark_title_alias
        self.must_fill = must_fill
        self.options = options
        self.pre_options = pre_options
        self.question_id = question_id
        self.rule = rule
        self.select_group = select_group
        self.selected = selected
        self.type = type

    def validate(self):
        if self.children:
            for k in self.children:
                if k:
                    k.validate()
        if self.options:
            for k in self.options:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_select is not None:
            result['CanSelect'] = self.can_select
        result['Children'] = []
        if self.children is not None:
            for k in self.children:
                result['Children'].append(k.to_map() if k else None)
        if self.default_result is not None:
            result['DefaultResult'] = self.default_result
        if self.display is not None:
            result['Display'] = self.display
        if self.exif is not None:
            result['Exif'] = self.exif
        if self.hot_key_map is not None:
            result['HotKeyMap'] = self.hot_key_map
        if self.mark_title is not None:
            result['MarkTitle'] = self.mark_title
        if self.mark_title_alias is not None:
            result['MarkTitleAlias'] = self.mark_title_alias
        if self.must_fill is not None:
            result['MustFill'] = self.must_fill
        result['Options'] = []
        if self.options is not None:
            for k in self.options:
                result['Options'].append(k.to_map() if k else None)
        if self.pre_options is not None:
            result['PreOptions'] = self.pre_options
        if self.question_id is not None:
            result['QuestionId'] = self.question_id
        if self.rule is not None:
            result['Rule'] = self.rule
        if self.select_group is not None:
            result['SelectGroup'] = self.select_group
        if self.selected is not None:
            result['Selected'] = self.selected
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanSelect') is not None:
            self.can_select = m.get('CanSelect')
        self.children = []
        if m.get('Children') is not None:
            for k in m.get('Children'):
                temp_model = QuestionPlugin()
                self.children.append(temp_model.from_map(k))
        if m.get('DefaultResult') is not None:
            self.default_result = m.get('DefaultResult')
        if m.get('Display') is not None:
            self.display = m.get('Display')
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')
        if m.get('HotKeyMap') is not None:
            self.hot_key_map = m.get('HotKeyMap')
        if m.get('MarkTitle') is not None:
            self.mark_title = m.get('MarkTitle')
        if m.get('MarkTitleAlias') is not None:
            self.mark_title_alias = m.get('MarkTitleAlias')
        if m.get('MustFill') is not None:
            self.must_fill = m.get('MustFill')
        self.options = []
        if m.get('Options') is not None:
            for k in m.get('Options'):
                temp_model = QuestionOption()
                self.options.append(temp_model.from_map(k))
        if m.get('PreOptions') is not None:
            self.pre_options = m.get('PreOptions')
        if m.get('QuestionId') is not None:
            self.question_id = m.get('QuestionId')
        if m.get('Rule') is not None:
            self.rule = m.get('Rule')
        if m.get('SelectGroup') is not None:
            self.select_group = m.get('SelectGroup')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SimpleSubtaskItems(TeaModel):
    def __init__(
        self,
        abandon_flag: bool = None,
        abandon_remark: str = None,
        data_id: str = None,
        feedback_flag: bool = None,
        feedback_remark: str = None,
        fixed_flag: bool = None,
        item_id: int = None,
        mine: int = None,
        reject_flag: bool = None,
        state: str = None,
        weight: int = None,
    ):
        self.abandon_flag = abandon_flag
        self.abandon_remark = abandon_remark
        self.data_id = data_id
        self.feedback_flag = feedback_flag
        self.feedback_remark = feedback_remark
        self.fixed_flag = fixed_flag
        self.item_id = item_id
        self.mine = mine
        self.reject_flag = reject_flag
        self.state = state
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abandon_flag is not None:
            result['AbandonFlag'] = self.abandon_flag
        if self.abandon_remark is not None:
            result['AbandonRemark'] = self.abandon_remark
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.feedback_flag is not None:
            result['FeedbackFlag'] = self.feedback_flag
        if self.feedback_remark is not None:
            result['FeedbackRemark'] = self.feedback_remark
        if self.fixed_flag is not None:
            result['FixedFlag'] = self.fixed_flag
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.mine is not None:
            result['Mine'] = self.mine
        if self.reject_flag is not None:
            result['RejectFlag'] = self.reject_flag
        if self.state is not None:
            result['State'] = self.state
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbandonFlag') is not None:
            self.abandon_flag = m.get('AbandonFlag')
        if m.get('AbandonRemark') is not None:
            self.abandon_remark = m.get('AbandonRemark')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('FeedbackFlag') is not None:
            self.feedback_flag = m.get('FeedbackFlag')
        if m.get('FeedbackRemark') is not None:
            self.feedback_remark = m.get('FeedbackRemark')
        if m.get('FixedFlag') is not None:
            self.fixed_flag = m.get('FixedFlag')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Mine') is not None:
            self.mine = m.get('Mine')
        if m.get('RejectFlag') is not None:
            self.reject_flag = m.get('RejectFlag')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class SimpleSubtask(TeaModel):
    def __init__(
        self,
        items: List[SimpleSubtaskItems] = None,
        status: str = None,
        subtask_id: int = None,
    ):
        self.items = items
        self.status = status
        self.subtask_id = subtask_id

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.subtask_id is not None:
            result['SubtaskId'] = self.subtask_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = SimpleSubtaskItems()
                self.items.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubtaskId') is not None:
            self.subtask_id = m.get('SubtaskId')
        return self


class SimpleTask(TeaModel):
    def __init__(
        self,
        archived: bool = None,
        archived_infos: str = None,
        creator: SimpleUser = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        label_style: str = None,
        modifier: SimpleUser = None,
        ref_task_id: str = None,
        remark: str = None,
        stage: str = None,
        status: str = None,
        tags: List[str] = None,
        task_id: str = None,
        task_name: str = None,
        task_type: str = None,
        template_id: str = None,
        tenant_id: str = None,
        uuid: str = None,
        workflow_nodes: List[str] = None,
    ):
        self.archived = archived
        self.archived_infos = archived_infos
        self.creator = creator
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.label_style = label_style
        self.modifier = modifier
        self.ref_task_id = ref_task_id
        self.remark = remark
        self.stage = stage
        self.status = status
        self.tags = tags
        self.task_id = task_id
        self.task_name = task_name
        self.task_type = task_type
        self.template_id = template_id
        self.tenant_id = tenant_id
        self.uuid = uuid
        self.workflow_nodes = workflow_nodes

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.modifier:
            self.modifier.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archived is not None:
            result['Archived'] = self.archived
        if self.archived_infos is not None:
            result['ArchivedInfos'] = self.archived_infos
        if self.creator is not None:
            result['Creator'] = self.creator.to_map()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.label_style is not None:
            result['LabelStyle'] = self.label_style
        if self.modifier is not None:
            result['Modifier'] = self.modifier.to_map()
        if self.ref_task_id is not None:
            result['RefTaskId'] = self.ref_task_id
        if self.remark is not None:
            result['Remark'] = self.remark
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
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.uuid is not None:
            result['UUID'] = self.uuid
        if self.workflow_nodes is not None:
            result['WorkflowNodes'] = self.workflow_nodes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Archived') is not None:
            self.archived = m.get('Archived')
        if m.get('ArchivedInfos') is not None:
            self.archived_infos = m.get('ArchivedInfos')
        if m.get('Creator') is not None:
            temp_model = SimpleUser()
            self.creator = temp_model.from_map(m['Creator'])
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('LabelStyle') is not None:
            self.label_style = m.get('LabelStyle')
        if m.get('Modifier') is not None:
            temp_model = SimpleUser()
            self.modifier = temp_model.from_map(m['Modifier'])
        if m.get('RefTaskId') is not None:
            self.ref_task_id = m.get('RefTaskId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
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
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UUID') is not None:
            self.uuid = m.get('UUID')
        if m.get('WorkflowNodes') is not None:
            self.workflow_nodes = m.get('WorkflowNodes')
        return self


class SimpleTemplate(TeaModel):
    def __init__(
        self,
        abandon_reasons: str = None,
        description: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        shared_mode: str = None,
        status: str = None,
        tags: List[str] = None,
        template_id: str = None,
        template_name: str = None,
        tenant_id: str = None,
        type: str = None,
    ):
        self.abandon_reasons = abandon_reasons
        self.description = description
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.shared_mode = shared_mode
        self.status = status
        self.tags = tags
        self.template_id = template_id
        self.template_name = template_name
        self.tenant_id = tenant_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abandon_reasons is not None:
            result['AbandonReasons'] = self.abandon_reasons
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.shared_mode is not None:
            result['SharedMode'] = self.shared_mode
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbandonReasons') is not None:
            self.abandon_reasons = m.get('AbandonReasons')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('SharedMode') is not None:
            self.shared_mode = m.get('SharedMode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SimpleTenant(TeaModel):
    def __init__(
        self,
        creator: SimpleUser = None,
        description: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        modifier: SimpleUser = None,
        role: str = None,
        tenant_id: str = None,
        tenant_name: str = None,
        uuid: str = None,
    ):
        self.creator = creator
        self.description = description
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.modifier = modifier
        self.role = role
        self.tenant_id = tenant_id
        self.tenant_name = tenant_name
        self.uuid = uuid

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.modifier:
            self.modifier.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['Creator'] = self.creator.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.modifier is not None:
            result['Modifier'] = self.modifier.to_map()
        if self.role is not None:
            result['Role'] = self.role
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.uuid is not None:
            result['UUID'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            temp_model = SimpleUser()
            self.creator = temp_model.from_map(m['Creator'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Modifier') is not None:
            temp_model = SimpleUser()
            self.modifier = temp_model.from_map(m['Modifier'])
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('UUID') is not None:
            self.uuid = m.get('UUID')
        return self


class SimpleWorkforce(TeaModel):
    def __init__(
        self,
        user_ids: List[int] = None,
        work_node_id: int = None,
    ):
        self.user_ids = user_ids
        self.work_node_id = work_node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        if self.work_node_id is not None:
            result['WorkNodeId'] = self.work_node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        if m.get('WorkNodeId') is not None:
            self.work_node_id = m.get('WorkNodeId')
        return self


class SingleTenant(TeaModel):
    def __init__(
        self,
        description: str = None,
        status: str = None,
        tenant_id: str = None,
        tenant_name: str = None,
        uuid: str = None,
    ):
        self.description = description
        self.status = status
        self.tenant_id = tenant_id
        self.tenant_name = tenant_name
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        if self.uuid is not None:
            result['UUID'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        if m.get('UUID') is not None:
            self.uuid = m.get('UUID')
        return self


class SubtaskDetailItems(TeaModel):
    def __init__(
        self,
        abandon_flag: bool = None,
        abandon_remark: str = None,
        data_id: str = None,
        feedback_flag: bool = None,
        feedback_remark: str = None,
        fixed_flag: bool = None,
        mine: int = None,
        reject_flag: bool = None,
        state: str = None,
        weight: int = None,
    ):
        self.abandon_flag = abandon_flag
        self.abandon_remark = abandon_remark
        self.data_id = data_id
        self.feedback_flag = feedback_flag
        self.feedback_remark = feedback_remark
        self.fixed_flag = fixed_flag
        self.mine = mine
        self.reject_flag = reject_flag
        self.state = state
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abandon_flag is not None:
            result['AbandonFlag'] = self.abandon_flag
        if self.abandon_remark is not None:
            result['AbandonRemark'] = self.abandon_remark
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.feedback_flag is not None:
            result['FeedbackFlag'] = self.feedback_flag
        if self.feedback_remark is not None:
            result['FeedbackRemark'] = self.feedback_remark
        if self.fixed_flag is not None:
            result['FixedFlag'] = self.fixed_flag
        if self.mine is not None:
            result['Mine'] = self.mine
        if self.reject_flag is not None:
            result['RejectFlag'] = self.reject_flag
        if self.state is not None:
            result['State'] = self.state
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbandonFlag') is not None:
            self.abandon_flag = m.get('AbandonFlag')
        if m.get('AbandonRemark') is not None:
            self.abandon_remark = m.get('AbandonRemark')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('FeedbackFlag') is not None:
            self.feedback_flag = m.get('FeedbackFlag')
        if m.get('FeedbackRemark') is not None:
            self.feedback_remark = m.get('FeedbackRemark')
        if m.get('FixedFlag') is not None:
            self.fixed_flag = m.get('FixedFlag')
        if m.get('Mine') is not None:
            self.mine = m.get('Mine')
        if m.get('RejectFlag') is not None:
            self.reject_flag = m.get('RejectFlag')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class Workforce(TeaModel):
    def __init__(
        self,
        node_type: str = None,
        users: List[SimpleUser] = None,
        work_node_id: int = None,
    ):
        self.node_type = node_type
        self.users = users
        self.work_node_id = work_node_id

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        if self.work_node_id is not None:
            result['WorkNodeId'] = self.work_node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = SimpleUser()
                self.users.append(temp_model.from_map(k))
        if m.get('WorkNodeId') is not None:
            self.work_node_id = m.get('WorkNodeId')
        return self


class SubtaskDetail(TeaModel):
    def __init__(
        self,
        can_discard: bool = None,
        can_reassign: bool = None,
        can_release: bool = None,
        current_work_node: str = None,
        ext_configs: str = None,
        items: List[SubtaskDetailItems] = None,
        status: str = None,
        subtask_id: str = None,
        task_id: str = None,
        weight: int = None,
        work_node_state: str = None,
        workforce: List[Workforce] = None,
    ):
        self.can_discard = can_discard
        self.can_reassign = can_reassign
        self.can_release = can_release
        self.current_work_node = current_work_node
        self.ext_configs = ext_configs
        self.items = items
        self.status = status
        self.subtask_id = subtask_id
        self.task_id = task_id
        self.weight = weight
        self.work_node_state = work_node_state
        self.workforce = workforce

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()
        if self.workforce:
            for k in self.workforce:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_discard is not None:
            result['CanDiscard'] = self.can_discard
        if self.can_reassign is not None:
            result['CanReassign'] = self.can_reassign
        if self.can_release is not None:
            result['CanRelease'] = self.can_release
        if self.current_work_node is not None:
            result['CurrentWorkNode'] = self.current_work_node
        if self.ext_configs is not None:
            result['ExtConfigs'] = self.ext_configs
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.subtask_id is not None:
            result['SubtaskId'] = self.subtask_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.work_node_state is not None:
            result['WorkNodeState'] = self.work_node_state
        result['Workforce'] = []
        if self.workforce is not None:
            for k in self.workforce:
                result['Workforce'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanDiscard') is not None:
            self.can_discard = m.get('CanDiscard')
        if m.get('CanReassign') is not None:
            self.can_reassign = m.get('CanReassign')
        if m.get('CanRelease') is not None:
            self.can_release = m.get('CanRelease')
        if m.get('CurrentWorkNode') is not None:
            self.current_work_node = m.get('CurrentWorkNode')
        if m.get('ExtConfigs') is not None:
            self.ext_configs = m.get('ExtConfigs')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = SubtaskDetailItems()
                self.items.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubtaskId') is not None:
            self.subtask_id = m.get('SubtaskId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('WorkNodeState') is not None:
            self.work_node_state = m.get('WorkNodeState')
        self.workforce = []
        if m.get('Workforce') is not None:
            for k in m.get('Workforce'):
                temp_model = Workforce()
                self.workforce.append(temp_model.from_map(k))
        return self


class SubtaskItemDetailAnnotations(TeaModel):
    def __init__(
        self,
        abandon_flag: bool = None,
        abandon_remark: str = None,
        data_id: str = None,
        feedback_flag: bool = None,
        feedback_remark: str = None,
        fixed_flag: bool = None,
        mine: int = None,
        reject_flag: bool = None,
        state: str = None,
        weight: int = None,
    ):
        self.abandon_flag = abandon_flag
        self.abandon_remark = abandon_remark
        self.data_id = data_id
        self.feedback_flag = feedback_flag
        self.feedback_remark = feedback_remark
        self.fixed_flag = fixed_flag
        self.mine = mine
        self.reject_flag = reject_flag
        self.state = state
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abandon_flag is not None:
            result['AbandonFlag'] = self.abandon_flag
        if self.abandon_remark is not None:
            result['AbandonRemark'] = self.abandon_remark
        if self.data_id is not None:
            result['DataId'] = self.data_id
        if self.feedback_flag is not None:
            result['FeedbackFlag'] = self.feedback_flag
        if self.feedback_remark is not None:
            result['FeedbackRemark'] = self.feedback_remark
        if self.fixed_flag is not None:
            result['FixedFlag'] = self.fixed_flag
        if self.mine is not None:
            result['Mine'] = self.mine
        if self.reject_flag is not None:
            result['RejectFlag'] = self.reject_flag
        if self.state is not None:
            result['State'] = self.state
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbandonFlag') is not None:
            self.abandon_flag = m.get('AbandonFlag')
        if m.get('AbandonRemark') is not None:
            self.abandon_remark = m.get('AbandonRemark')
        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')
        if m.get('FeedbackFlag') is not None:
            self.feedback_flag = m.get('FeedbackFlag')
        if m.get('FeedbackRemark') is not None:
            self.feedback_remark = m.get('FeedbackRemark')
        if m.get('FixedFlag') is not None:
            self.fixed_flag = m.get('FixedFlag')
        if m.get('Mine') is not None:
            self.mine = m.get('Mine')
        if m.get('RejectFlag') is not None:
            self.reject_flag = m.get('RejectFlag')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class SubtaskItemDetail(TeaModel):
    def __init__(
        self,
        annotations: List[SubtaskItemDetailAnnotations] = None,
        data_source: Dict[str, Any] = None,
        item_id: int = None,
    ):
        self.annotations = annotations
        self.data_source = data_source
        self.item_id = item_id

    def validate(self):
        if self.annotations:
            for k in self.annotations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Annotations'] = []
        if self.annotations is not None:
            for k in self.annotations:
                result['Annotations'].append(k.to_map() if k else None)
        if self.data_source is not None:
            result['DataSource'] = self.data_source
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.annotations = []
        if m.get('Annotations') is not None:
            for k in m.get('Annotations'):
                temp_model = SubtaskItemDetailAnnotations()
                self.annotations.append(temp_model.from_map(k))
        if m.get('DataSource') is not None:
            self.data_source = m.get('DataSource')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        return self


class TaskDetailDatasetProxyRelations(TeaModel):
    def __init__(
        self,
        dataset_id: str = None,
        dataset_type: str = None,
        exif: Dict[str, Any] = None,
        source: str = None,
        source_biz_id: str = None,
        source_dataset_id: str = None,
    ):
        self.dataset_id = dataset_id
        self.dataset_type = dataset_type
        self.exif = exif
        self.source = source
        self.source_biz_id = source_biz_id
        self.source_dataset_id = source_dataset_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class TaskDetailTaskTemplateConfig(TeaModel):
    def __init__(
        self,
        exif: Dict[str, Any] = None,
        resource_key: str = None,
        robot_config: Dict[str, Any] = None,
        select_questions: List[str] = None,
        template_option_map: Dict[str, Any] = None,
        template_relation_id: str = None,
    ):
        self.exif = exif
        self.resource_key = resource_key
        self.robot_config = robot_config
        self.select_questions = select_questions
        self.template_option_map = template_option_map
        self.template_relation_id = template_relation_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class TaskDetailTaskWorkflow(TeaModel):
    def __init__(
        self,
        exif: Dict[str, Any] = None,
        groups: List[str] = None,
        node_name: str = None,
        users: List[SimpleUser] = None,
    ):
        self.exif = exif
        self.groups = groups
        self.node_name = node_name
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exif is not None:
            result['Exif'] = self.exif
        if self.groups is not None:
            result['Groups'] = self.groups
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
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
            for k in m.get('Users'):
                temp_model = SimpleUser()
                self.users.append(temp_model.from_map(k))
        return self


class TaskDetail(TeaModel):
    def __init__(
        self,
        admins: List[SimpleUser] = None,
        alert_time: int = None,
        allow_append_data: bool = None,
        archived: bool = None,
        archived_infos: str = None,
        assign_config: Dict[str, Any] = None,
        creator: SimpleUser = None,
        dataset_proxy_relations: List[TaskDetailDatasetProxyRelations] = None,
        exif: Dict[str, Any] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        label_style: str = None,
        mine_configs: Dict[str, Any] = None,
        modifier: SimpleUser = None,
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
        task_template_config: TaskDetailTaskTemplateConfig = None,
        task_type: str = None,
        task_workflow: List[TaskDetailTaskWorkflow] = None,
        template_id: str = None,
        tenant_id: str = None,
        tenant_name: str = None,
        uuid: str = None,
        vote_configs: Dict[str, Any] = None,
        workflow_nodes: List[str] = None,
        run_msg: str = None,
    ):
        self.admins = admins
        self.alert_time = alert_time
        self.allow_append_data = allow_append_data
        self.archived = archived
        self.archived_infos = archived_infos
        self.assign_config = assign_config
        self.creator = creator
        self.dataset_proxy_relations = dataset_proxy_relations
        self.exif = exif
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.label_style = label_style
        self.mine_configs = mine_configs
        self.modifier = modifier
        self.notice_config = notice_config
        self.period_config = period_config
        self.ref_task_id = ref_task_id
        self.relate_task_config = relate_task_config
        self.remark = remark
        self.result_callback_config = result_callback_config
        self.stage = stage
        self.status = status
        self.tags = tags
        self.task_id = task_id
        self.task_name = task_name
        self.task_template_config = task_template_config
        self.task_type = task_type
        self.task_workflow = task_workflow
        self.template_id = template_id
        self.tenant_id = tenant_id
        self.tenant_name = tenant_name
        self.uuid = uuid
        self.vote_configs = vote_configs
        self.workflow_nodes = workflow_nodes
        self.run_msg = run_msg

    def validate(self):
        if self.admins:
            for k in self.admins:
                if k:
                    k.validate()
        if self.creator:
            self.creator.validate()
        if self.dataset_proxy_relations:
            for k in self.dataset_proxy_relations:
                if k:
                    k.validate()
        if self.modifier:
            self.modifier.validate()
        if self.task_template_config:
            self.task_template_config.validate()
        if self.task_workflow:
            for k in self.task_workflow:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Admins'] = []
        if self.admins is not None:
            for k in self.admins:
                result['Admins'].append(k.to_map() if k else None)
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
            for k in self.dataset_proxy_relations:
                result['DatasetProxyRelations'].append(k.to_map() if k else None)
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
            for k in self.task_workflow:
                result['TaskWorkflow'].append(k.to_map() if k else None)
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
            for k in m.get('Admins'):
                temp_model = SimpleUser()
                self.admins.append(temp_model.from_map(k))
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
            temp_model = SimpleUser()
            self.creator = temp_model.from_map(m['Creator'])
        self.dataset_proxy_relations = []
        if m.get('DatasetProxyRelations') is not None:
            for k in m.get('DatasetProxyRelations'):
                temp_model = TaskDetailDatasetProxyRelations()
                self.dataset_proxy_relations.append(temp_model.from_map(k))
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
            temp_model = SimpleUser()
            self.modifier = temp_model.from_map(m['Modifier'])
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
            temp_model = TaskDetailTaskTemplateConfig()
            self.task_template_config = temp_model.from_map(m['TaskTemplateConfig'])
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        self.task_workflow = []
        if m.get('TaskWorkflow') is not None:
            for k in m.get('TaskWorkflow'):
                temp_model = TaskDetailTaskWorkflow()
                self.task_workflow.append(temp_model.from_map(k))
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


class TaskStatistic(TeaModel):
    def __init__(
        self,
        accept_item_count: float = None,
        check_abandon: float = None,
        check_accuracy: float = None,
        check_efficiency: float = None,
        checked_accuracy: float = None,
        checked_error: float = None,
        checked_reject_count: float = None,
        final_abandon_count: float = None,
        finished_item_count: int = None,
        finished_subtask_count: int = None,
        mark_efficiency: float = None,
        pre_mark_fixed_count: float = None,
        sampled_accuracy: float = None,
        sampled_error_count: float = None,
        sampled_reject_count: float = None,
        sampling_accuracy: float = None,
        total_check_count: float = None,
        total_check_time: float = None,
        total_checked_count: float = None,
        total_item_count: int = None,
        total_mark_time: float = None,
        total_sampled_count: float = None,
        total_sampling_count: float = None,
        total_subtask_count: int = None,
        total_work_time: float = None,
    ):
        self.accept_item_count = accept_item_count
        self.check_abandon = check_abandon
        self.check_accuracy = check_accuracy
        self.check_efficiency = check_efficiency
        self.checked_accuracy = checked_accuracy
        self.checked_error = checked_error
        self.checked_reject_count = checked_reject_count
        self.final_abandon_count = final_abandon_count
        self.finished_item_count = finished_item_count
        self.finished_subtask_count = finished_subtask_count
        self.mark_efficiency = mark_efficiency
        self.pre_mark_fixed_count = pre_mark_fixed_count
        self.sampled_accuracy = sampled_accuracy
        self.sampled_error_count = sampled_error_count
        self.sampled_reject_count = sampled_reject_count
        self.sampling_accuracy = sampling_accuracy
        self.total_check_count = total_check_count
        self.total_check_time = total_check_time
        self.total_checked_count = total_checked_count
        self.total_item_count = total_item_count
        self.total_mark_time = total_mark_time
        self.total_sampled_count = total_sampled_count
        self.total_sampling_count = total_sampling_count
        self.total_subtask_count = total_subtask_count
        self.total_work_time = total_work_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_item_count is not None:
            result['AcceptItemCount'] = self.accept_item_count
        if self.check_abandon is not None:
            result['CheckAbandon'] = self.check_abandon
        if self.check_accuracy is not None:
            result['CheckAccuracy'] = self.check_accuracy
        if self.check_efficiency is not None:
            result['CheckEfficiency'] = self.check_efficiency
        if self.checked_accuracy is not None:
            result['CheckedAccuracy'] = self.checked_accuracy
        if self.checked_error is not None:
            result['CheckedError'] = self.checked_error
        if self.checked_reject_count is not None:
            result['CheckedRejectCount'] = self.checked_reject_count
        if self.final_abandon_count is not None:
            result['FinalAbandonCount'] = self.final_abandon_count
        if self.finished_item_count is not None:
            result['FinishedItemCount'] = self.finished_item_count
        if self.finished_subtask_count is not None:
            result['FinishedSubtaskCount'] = self.finished_subtask_count
        if self.mark_efficiency is not None:
            result['MarkEfficiency'] = self.mark_efficiency
        if self.pre_mark_fixed_count is not None:
            result['PreMarkFixedCount'] = self.pre_mark_fixed_count
        if self.sampled_accuracy is not None:
            result['SampledAccuracy'] = self.sampled_accuracy
        if self.sampled_error_count is not None:
            result['SampledErrorCount'] = self.sampled_error_count
        if self.sampled_reject_count is not None:
            result['SampledRejectCount'] = self.sampled_reject_count
        if self.sampling_accuracy is not None:
            result['SamplingAccuracy'] = self.sampling_accuracy
        if self.total_check_count is not None:
            result['TotalCheckCount'] = self.total_check_count
        if self.total_check_time is not None:
            result['TotalCheckTime'] = self.total_check_time
        if self.total_checked_count is not None:
            result['TotalCheckedCount'] = self.total_checked_count
        if self.total_item_count is not None:
            result['TotalItemCount'] = self.total_item_count
        if self.total_mark_time is not None:
            result['TotalMarkTime'] = self.total_mark_time
        if self.total_sampled_count is not None:
            result['TotalSampledCount'] = self.total_sampled_count
        if self.total_sampling_count is not None:
            result['TotalSamplingCount'] = self.total_sampling_count
        if self.total_subtask_count is not None:
            result['TotalSubtaskCount'] = self.total_subtask_count
        if self.total_work_time is not None:
            result['TotalWorkTime'] = self.total_work_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptItemCount') is not None:
            self.accept_item_count = m.get('AcceptItemCount')
        if m.get('CheckAbandon') is not None:
            self.check_abandon = m.get('CheckAbandon')
        if m.get('CheckAccuracy') is not None:
            self.check_accuracy = m.get('CheckAccuracy')
        if m.get('CheckEfficiency') is not None:
            self.check_efficiency = m.get('CheckEfficiency')
        if m.get('CheckedAccuracy') is not None:
            self.checked_accuracy = m.get('CheckedAccuracy')
        if m.get('CheckedError') is not None:
            self.checked_error = m.get('CheckedError')
        if m.get('CheckedRejectCount') is not None:
            self.checked_reject_count = m.get('CheckedRejectCount')
        if m.get('FinalAbandonCount') is not None:
            self.final_abandon_count = m.get('FinalAbandonCount')
        if m.get('FinishedItemCount') is not None:
            self.finished_item_count = m.get('FinishedItemCount')
        if m.get('FinishedSubtaskCount') is not None:
            self.finished_subtask_count = m.get('FinishedSubtaskCount')
        if m.get('MarkEfficiency') is not None:
            self.mark_efficiency = m.get('MarkEfficiency')
        if m.get('PreMarkFixedCount') is not None:
            self.pre_mark_fixed_count = m.get('PreMarkFixedCount')
        if m.get('SampledAccuracy') is not None:
            self.sampled_accuracy = m.get('SampledAccuracy')
        if m.get('SampledErrorCount') is not None:
            self.sampled_error_count = m.get('SampledErrorCount')
        if m.get('SampledRejectCount') is not None:
            self.sampled_reject_count = m.get('SampledRejectCount')
        if m.get('SamplingAccuracy') is not None:
            self.sampling_accuracy = m.get('SamplingAccuracy')
        if m.get('TotalCheckCount') is not None:
            self.total_check_count = m.get('TotalCheckCount')
        if m.get('TotalCheckTime') is not None:
            self.total_check_time = m.get('TotalCheckTime')
        if m.get('TotalCheckedCount') is not None:
            self.total_checked_count = m.get('TotalCheckedCount')
        if m.get('TotalItemCount') is not None:
            self.total_item_count = m.get('TotalItemCount')
        if m.get('TotalMarkTime') is not None:
            self.total_mark_time = m.get('TotalMarkTime')
        if m.get('TotalSampledCount') is not None:
            self.total_sampled_count = m.get('TotalSampledCount')
        if m.get('TotalSamplingCount') is not None:
            self.total_sampling_count = m.get('TotalSamplingCount')
        if m.get('TotalSubtaskCount') is not None:
            self.total_subtask_count = m.get('TotalSubtaskCount')
        if m.get('TotalWorkTime') is not None:
            self.total_work_time = m.get('TotalWorkTime')
        return self


class ViewPluginVisitInfo(TeaModel):
    def __init__(
        self,
        afts_conf: Dict[str, Any] = None,
        oss_conf: Dict[str, Any] = None,
    ):
        self.afts_conf = afts_conf
        self.oss_conf = oss_conf

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.afts_conf is not None:
            result['aftsConf'] = self.afts_conf
        if self.oss_conf is not None:
            result['ossConf'] = self.oss_conf
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aftsConf') is not None:
            self.afts_conf = m.get('aftsConf')
        if m.get('ossConf') is not None:
            self.oss_conf = m.get('ossConf')
        return self


class ViewPlugin(TeaModel):
    def __init__(
        self,
        bind_field: str = None,
        convertor: str = None,
        cors_proxy: bool = None,
        display_ori_img: bool = None,
        exif: Dict[str, Any] = None,
        hide: bool = None,
        plugins: Dict[str, Any] = None,
        relation_question_ids: List[str] = None,
        type: str = None,
        visit_info: ViewPluginVisitInfo = None,
    ):
        self.bind_field = bind_field
        self.convertor = convertor
        self.cors_proxy = cors_proxy
        self.display_ori_img = display_ori_img
        self.exif = exif
        self.hide = hide
        self.plugins = plugins
        self.relation_question_ids = relation_question_ids
        self.type = type
        self.visit_info = visit_info

    def validate(self):
        if self.visit_info:
            self.visit_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_field is not None:
            result['BindField'] = self.bind_field
        if self.convertor is not None:
            result['Convertor'] = self.convertor
        if self.cors_proxy is not None:
            result['CorsProxy'] = self.cors_proxy
        if self.display_ori_img is not None:
            result['DisplayOriImg'] = self.display_ori_img
        if self.exif is not None:
            result['Exif'] = self.exif
        if self.hide is not None:
            result['Hide'] = self.hide
        if self.plugins is not None:
            result['Plugins'] = self.plugins
        if self.relation_question_ids is not None:
            result['RelationQuestionIds'] = self.relation_question_ids
        if self.type is not None:
            result['Type'] = self.type
        if self.visit_info is not None:
            result['VisitInfo'] = self.visit_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindField') is not None:
            self.bind_field = m.get('BindField')
        if m.get('Convertor') is not None:
            self.convertor = m.get('Convertor')
        if m.get('CorsProxy') is not None:
            self.cors_proxy = m.get('CorsProxy')
        if m.get('DisplayOriImg') is not None:
            self.display_ori_img = m.get('DisplayOriImg')
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')
        if m.get('Hide') is not None:
            self.hide = m.get('Hide')
        if m.get('Plugins') is not None:
            self.plugins = m.get('Plugins')
        if m.get('RelationQuestionIds') is not None:
            self.relation_question_ids = m.get('RelationQuestionIds')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VisitInfo') is not None:
            temp_model = ViewPluginVisitInfo()
            self.visit_info = temp_model.from_map(m['VisitInfo'])
        return self


class TemplateDTOViewConfigs(TeaModel):
    def __init__(
        self,
        view_plugins: List[ViewPlugin] = None,
    ):
        self.view_plugins = view_plugins

    def validate(self):
        if self.view_plugins:
            for k in self.view_plugins:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ViewPlugins'] = []
        if self.view_plugins is not None:
            for k in self.view_plugins:
                result['ViewPlugins'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.view_plugins = []
        if m.get('ViewPlugins') is not None:
            for k in m.get('ViewPlugins'):
                temp_model = ViewPlugin()
                self.view_plugins.append(temp_model.from_map(k))
        return self


class TemplateDTO(TeaModel):
    def __init__(
        self,
        classify: str = None,
        description: str = None,
        exif: Dict[str, Any] = None,
        question_configs: List[QuestionPlugin] = None,
        robot_configs: List[Dict[str, Any]] = None,
        shared_mode: str = None,
        tags: List[str] = None,
        template_id: str = None,
        template_name: str = None,
        view_configs: TemplateDTOViewConfigs = None,
    ):
        self.classify = classify
        self.description = description
        self.exif = exif
        self.question_configs = question_configs
        self.robot_configs = robot_configs
        self.shared_mode = shared_mode
        self.tags = tags
        self.template_id = template_id
        self.template_name = template_name
        self.view_configs = view_configs

    def validate(self):
        if self.question_configs:
            for k in self.question_configs:
                if k:
                    k.validate()
        if self.view_configs:
            self.view_configs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.classify is not None:
            result['Classify'] = self.classify
        if self.description is not None:
            result['Description'] = self.description
        if self.exif is not None:
            result['Exif'] = self.exif
        result['QuestionConfigs'] = []
        if self.question_configs is not None:
            for k in self.question_configs:
                result['QuestionConfigs'].append(k.to_map() if k else None)
        if self.robot_configs is not None:
            result['RobotConfigs'] = self.robot_configs
        if self.shared_mode is not None:
            result['SharedMode'] = self.shared_mode
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.view_configs is not None:
            result['ViewConfigs'] = self.view_configs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classify') is not None:
            self.classify = m.get('Classify')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')
        self.question_configs = []
        if m.get('QuestionConfigs') is not None:
            for k in m.get('QuestionConfigs'):
                temp_model = QuestionPlugin()
                self.question_configs.append(temp_model.from_map(k))
        if m.get('RobotConfigs') is not None:
            self.robot_configs = m.get('RobotConfigs')
        if m.get('SharedMode') is not None:
            self.shared_mode = m.get('SharedMode')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('ViewConfigs') is not None:
            temp_model = TemplateDTOViewConfigs()
            self.view_configs = temp_model.from_map(m['ViewConfigs'])
        return self


class TemplateDetailViewConfigs(TeaModel):
    def __init__(
        self,
        view_plugins: List[ViewPlugin] = None,
    ):
        self.view_plugins = view_plugins

    def validate(self):
        if self.view_plugins:
            for k in self.view_plugins:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ViewPlugins'] = []
        if self.view_plugins is not None:
            for k in self.view_plugins:
                result['ViewPlugins'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.view_plugins = []
        if m.get('ViewPlugins') is not None:
            for k in m.get('ViewPlugins'):
                temp_model = ViewPlugin()
                self.view_plugins.append(temp_model.from_map(k))
        return self


class TemplateDetail(TeaModel):
    def __init__(
        self,
        abandon_reasons: List[str] = None,
        classify: str = None,
        creator: SimpleUser = None,
        description: str = None,
        exif: Dict[str, Any] = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        modifier: SimpleUser = None,
        question_configs: List[QuestionPlugin] = None,
        shared_mode: str = None,
        status: str = None,
        tags: List[str] = None,
        template_id: str = None,
        template_name: str = None,
        tenant_id: str = None,
        type: str = None,
        view_configs: TemplateDetailViewConfigs = None,
    ):
        self.abandon_reasons = abandon_reasons
        self.classify = classify
        self.creator = creator
        self.description = description
        self.exif = exif
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.modifier = modifier
        self.question_configs = question_configs
        self.shared_mode = shared_mode
        self.status = status
        self.tags = tags
        self.template_id = template_id
        self.template_name = template_name
        self.tenant_id = tenant_id
        self.type = type
        self.view_configs = view_configs

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.modifier:
            self.modifier.validate()
        if self.question_configs:
            for k in self.question_configs:
                if k:
                    k.validate()
        if self.view_configs:
            self.view_configs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.abandon_reasons is not None:
            result['AbandonReasons'] = self.abandon_reasons
        if self.classify is not None:
            result['Classify'] = self.classify
        if self.creator is not None:
            result['Creator'] = self.creator.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.exif is not None:
            result['Exif'] = self.exif
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.modifier is not None:
            result['Modifier'] = self.modifier.to_map()
        result['QuestionConfigs'] = []
        if self.question_configs is not None:
            for k in self.question_configs:
                result['QuestionConfigs'].append(k.to_map() if k else None)
        if self.shared_mode is not None:
            result['SharedMode'] = self.shared_mode
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.type is not None:
            result['Type'] = self.type
        if self.view_configs is not None:
            result['ViewConfigs'] = self.view_configs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbandonReasons') is not None:
            self.abandon_reasons = m.get('AbandonReasons')
        if m.get('Classify') is not None:
            self.classify = m.get('Classify')
        if m.get('Creator') is not None:
            temp_model = SimpleUser()
            self.creator = temp_model.from_map(m['Creator'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Modifier') is not None:
            temp_model = SimpleUser()
            self.modifier = temp_model.from_map(m['Modifier'])
        self.question_configs = []
        if m.get('QuestionConfigs') is not None:
            for k in m.get('QuestionConfigs'):
                temp_model = QuestionPlugin()
                self.question_configs.append(temp_model.from_map(k))
        if m.get('SharedMode') is not None:
            self.shared_mode = m.get('SharedMode')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ViewConfigs') is not None:
            temp_model = TemplateDetailViewConfigs()
            self.view_configs = temp_model.from_map(m['ViewConfigs'])
        return self


class TemplateQuestion(TeaModel):
    def __init__(
        self,
        children: List['TemplateQuestion'] = None,
        exif: Dict[str, Any] = None,
        mark_title: str = None,
        options: List[QuestionOption] = None,
        pre_options: List[str] = None,
        question_id: int = None,
        type: str = None,
    ):
        self.children = children
        self.exif = exif
        self.mark_title = mark_title
        self.options = options
        self.pre_options = pre_options
        self.question_id = question_id
        self.type = type

    def validate(self):
        if self.children:
            for k in self.children:
                if k:
                    k.validate()
        if self.options:
            for k in self.options:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Children'] = []
        if self.children is not None:
            for k in self.children:
                result['Children'].append(k.to_map() if k else None)
        if self.exif is not None:
            result['Exif'] = self.exif
        if self.mark_title is not None:
            result['MarkTitle'] = self.mark_title
        result['Options'] = []
        if self.options is not None:
            for k in self.options:
                result['Options'].append(k.to_map() if k else None)
        if self.pre_options is not None:
            result['PreOptions'] = self.pre_options
        if self.question_id is not None:
            result['QuestionId'] = self.question_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.children = []
        if m.get('Children') is not None:
            for k in m.get('Children'):
                temp_model = TemplateQuestion()
                self.children.append(temp_model.from_map(k))
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')
        if m.get('MarkTitle') is not None:
            self.mark_title = m.get('MarkTitle')
        self.options = []
        if m.get('Options') is not None:
            for k in m.get('Options'):
                temp_model = QuestionOption()
                self.options.append(temp_model.from_map(k))
        if m.get('PreOptions') is not None:
            self.pre_options = m.get('PreOptions')
        if m.get('QuestionId') is not None:
            self.question_id = m.get('QuestionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class TemplateViewFieldsVisitInfo(TeaModel):
    def __init__(
        self,
        afts_conf: Dict[str, Any] = None,
        oss_conf: Dict[str, Any] = None,
    ):
        self.afts_conf = afts_conf
        self.oss_conf = oss_conf

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.afts_conf is not None:
            result['AftsConf'] = self.afts_conf
        if self.oss_conf is not None:
            result['OssConf'] = self.oss_conf
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AftsConf') is not None:
            self.afts_conf = m.get('AftsConf')
        if m.get('OssConf') is not None:
            self.oss_conf = m.get('OssConf')
        return self


class TemplateViewFields(TeaModel):
    def __init__(
        self,
        display_ori_img: bool = None,
        field_name: str = None,
        type: str = None,
        visit_info: TemplateViewFieldsVisitInfo = None,
    ):
        self.display_ori_img = display_ori_img
        self.field_name = field_name
        self.type = type
        self.visit_info = visit_info

    def validate(self):
        if self.visit_info:
            self.visit_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_ori_img is not None:
            result['DisplayOriImg'] = self.display_ori_img
        if self.field_name is not None:
            result['FieldName'] = self.field_name
        if self.type is not None:
            result['Type'] = self.type
        if self.visit_info is not None:
            result['VisitInfo'] = self.visit_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayOriImg') is not None:
            self.display_ori_img = m.get('DisplayOriImg')
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VisitInfo') is not None:
            temp_model = TemplateViewFieldsVisitInfo()
            self.visit_info = temp_model.from_map(m['VisitInfo'])
        return self


class TemplateView(TeaModel):
    def __init__(
        self,
        fields: List[TemplateViewFields] = None,
    ):
        self.fields = fields

    def validate(self):
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = TemplateViewFields()
                self.fields.append(temp_model.from_map(k))
        return self


class UpdateTaskDTO(TeaModel):
    def __init__(
        self,
        exif: Dict[str, str] = None,
        remark: str = None,
        tags: List[str] = None,
        task_name: str = None,
    ):
        self.exif = exif
        self.remark = remark
        self.tags = tags
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exif is not None:
            result['Exif'] = self.exif
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exif') is not None:
            self.exif = m.get('Exif')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class UserStatistic(TeaModel):
    def __init__(
        self,
        accepted_mark_items_count: float = None,
        check_count: float = None,
        checked_accepted_count: float = None,
        checked_accuracy: float = None,
        mark_efficiency: float = None,
        mark_time: float = None,
        sampling_accuracy: float = None,
        sampling_count: float = None,
        sampling_error_count: float = None,
        total_mark_items_count: float = None,
        user_id: str = None,
    ):
        self.accepted_mark_items_count = accepted_mark_items_count
        self.check_count = check_count
        self.checked_accepted_count = checked_accepted_count
        self.checked_accuracy = checked_accuracy
        self.mark_efficiency = mark_efficiency
        self.mark_time = mark_time
        self.sampling_accuracy = sampling_accuracy
        self.sampling_count = sampling_count
        self.sampling_error_count = sampling_error_count
        self.total_mark_items_count = total_mark_items_count
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accepted_mark_items_count is not None:
            result['AcceptedMarkItemsCount'] = self.accepted_mark_items_count
        if self.check_count is not None:
            result['CheckCount'] = self.check_count
        if self.checked_accepted_count is not None:
            result['CheckedAcceptedCount'] = self.checked_accepted_count
        if self.checked_accuracy is not None:
            result['CheckedAccuracy'] = self.checked_accuracy
        if self.mark_efficiency is not None:
            result['MarkEfficiency'] = self.mark_efficiency
        if self.mark_time is not None:
            result['MarkTime'] = self.mark_time
        if self.sampling_accuracy is not None:
            result['SamplingAccuracy'] = self.sampling_accuracy
        if self.sampling_count is not None:
            result['SamplingCount'] = self.sampling_count
        if self.sampling_error_count is not None:
            result['SamplingErrorCount'] = self.sampling_error_count
        if self.total_mark_items_count is not None:
            result['TotalMarkItemsCount'] = self.total_mark_items_count
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptedMarkItemsCount') is not None:
            self.accepted_mark_items_count = m.get('AcceptedMarkItemsCount')
        if m.get('CheckCount') is not None:
            self.check_count = m.get('CheckCount')
        if m.get('CheckedAcceptedCount') is not None:
            self.checked_accepted_count = m.get('CheckedAcceptedCount')
        if m.get('CheckedAccuracy') is not None:
            self.checked_accuracy = m.get('CheckedAccuracy')
        if m.get('MarkEfficiency') is not None:
            self.mark_efficiency = m.get('MarkEfficiency')
        if m.get('MarkTime') is not None:
            self.mark_time = m.get('MarkTime')
        if m.get('SamplingAccuracy') is not None:
            self.sampling_accuracy = m.get('SamplingAccuracy')
        if m.get('SamplingCount') is not None:
            self.sampling_count = m.get('SamplingCount')
        if m.get('SamplingErrorCount') is not None:
            self.sampling_error_count = m.get('SamplingErrorCount')
        if m.get('TotalMarkItemsCount') is not None:
            self.total_mark_items_count = m.get('TotalMarkItemsCount')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AddWorkNodeWorkforceRequest(TeaModel):
    def __init__(
        self,
        user_ids: List[int] = None,
    ):
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class AddWorkNodeWorkforceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddWorkNodeWorkforceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddWorkNodeWorkforceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddWorkNodeWorkforceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTaskRequest(TeaModel):
    def __init__(
        self,
        body: CreateTaskDetail = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = CreateTaskDetail()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTemplateRequest(TeaModel):
    def __init__(
        self,
        body: TemplateDTO = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = TemplateDTO()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        template_id: str = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.request_id = request_id
        self.success = success
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserRequest(TeaModel):
    def __init__(
        self,
        account_no: str = None,
        account_type: str = None,
        role: str = None,
        user_name: str = None,
    ):
        self.account_no = account_no
        self.account_type = account_type
        self.role = role
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_no is not None:
            result['AccountNo'] = self.account_no
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.role is not None:
            result['Role'] = self.role
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountNo') is not None:
            self.account_no = m.get('AccountNo')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateUserResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        user_id: int = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.request_id = request_id
        self.success = success
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        template_id: str = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.request_id = request_id
        self.success = success
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DeleteTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportAnnotationsRequest(TeaModel):
    def __init__(
        self,
        oss_path: str = None,
        register_dataset: str = None,
        target: str = None,
    ):
        self.oss_path = oss_path
        self.register_dataset = register_dataset
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_path is not None:
            result['OssPath'] = self.oss_path
        if self.register_dataset is not None:
            result['RegisterDataset'] = self.register_dataset
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssPath') is not None:
            self.oss_path = m.get('OssPath')
        if m.get('RegisterDataset') is not None:
            self.register_dataset = m.get('RegisterDataset')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class ExportAnnotationsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        flow_job: FlowJobInfo = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.details = details
        self.flow_job = flow_job
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.flow_job:
            self.flow_job.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.flow_job is not None:
            result['FlowJob'] = self.flow_job.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('FlowJob') is not None:
            temp_model = FlowJobInfo()
            self.flow_job = temp_model.from_map(m['FlowJob'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExportAnnotationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportAnnotationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExportAnnotationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobRequest(TeaModel):
    def __init__(
        self,
        job_type: str = None,
    ):
        self.job_type = job_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_type is not None:
            result['JobType'] = self.job_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        return self


class GetJobResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        job: Job = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.details = details
        self.job = job
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.job:
            self.job.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.job is not None:
            result['Job'] = self.job.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Job') is not None:
            temp_model = Job()
            self.job = temp_model.from_map(m['Job'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSubtaskResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        request_id: str = None,
        subtask: SimpleSubtask = None,
        success: bool = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.request_id = request_id
        self.subtask = subtask
        self.success = success

    def validate(self):
        if self.subtask:
            self.subtask.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.subtask is not None:
            result['Subtask'] = self.subtask.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Subtask') is not None:
            temp_model = SimpleSubtask()
            self.subtask = temp_model.from_map(m['Subtask'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSubtaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSubtaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSubtaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSubtaskItemResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        item: SubtaskItemDetail = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.details = details
        self.item = item
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.item:
            self.item.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.item is not None:
            result['Item'] = self.item.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Item') is not None:
            temp_model = SubtaskItemDetail()
            self.item = temp_model.from_map(m['Item'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSubtaskItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSubtaskItemResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSubtaskItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task: TaskDetail = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task = task

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task is not None:
            result['Task'] = self.task.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Task') is not None:
            temp_model = TaskDetail()
            self.task = temp_model.from_map(m['Task'])
        return self


class GetTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskStatisticsRequest(TeaModel):
    def __init__(
        self,
        stat_type: str = None,
    ):
        self.stat_type = stat_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stat_type is not None:
            result['StatType'] = self.stat_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StatType') is not None:
            self.stat_type = m.get('StatType')
        return self


class GetTaskStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_statistics: TaskStatistic = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_statistics = task_statistics

    def validate(self):
        if self.task_statistics:
            self.task_statistics.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_statistics is not None:
            result['TaskStatistics'] = self.task_statistics.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskStatistics') is not None:
            temp_model = TaskStatistic()
            self.task_statistics = temp_model.from_map(m['TaskStatistics'])
        return self


class GetTaskStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTaskStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_status: str = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class GetTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTaskStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        template: TemplateDetail = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.request_id = request_id
        self.success = success
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.template is not None:
            result['Template'] = self.template.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Template') is not None:
            temp_model = TemplateDetail()
            self.template = temp_model.from_map(m['Template'])
        return self


class GetTaskTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTaskTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskTemplateQuestionsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        questions: List[QuestionPlugin] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.questions = questions
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.questions:
            for k in self.questions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        result['Questions'] = []
        if self.questions is not None:
            for k in self.questions:
                result['Questions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.questions = []
        if m.get('Questions') is not None:
            for k in m.get('Questions'):
                temp_model = QuestionPlugin()
                self.questions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetTaskTemplateQuestionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTaskTemplateQuestionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskTemplateQuestionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskTemplateViewsResponseBodyViews(TeaModel):
    def __init__(
        self,
        view_plugins: List[ViewPlugin] = None,
    ):
        self.view_plugins = view_plugins

    def validate(self):
        if self.view_plugins:
            for k in self.view_plugins:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ViewPlugins'] = []
        if self.view_plugins is not None:
            for k in self.view_plugins:
                result['ViewPlugins'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.view_plugins = []
        if m.get('ViewPlugins') is not None:
            for k in m.get('ViewPlugins'):
                temp_model = ViewPlugin()
                self.view_plugins.append(temp_model.from_map(k))
        return self


class GetTaskTemplateViewsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        views: GetTaskTemplateViewsResponseBodyViews = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.request_id = request_id
        self.success = success
        self.views = views

    def validate(self):
        if self.views:
            self.views.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.views is not None:
            result['Views'] = self.views.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Views') is not None:
            temp_model = GetTaskTemplateViewsResponseBodyViews()
            self.views = temp_model.from_map(m['Views'])
        return self


class GetTaskTemplateViewsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTaskTemplateViewsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskTemplateViewsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskWorkforceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        workforce: List[Workforce] = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.request_id = request_id
        self.success = success
        self.workforce = workforce

    def validate(self):
        if self.workforce:
            for k in self.workforce:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['Workforce'] = []
        if self.workforce is not None:
            for k in self.workforce:
                result['Workforce'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.workforce = []
        if m.get('Workforce') is not None:
            for k in m.get('Workforce'):
                temp_model = Workforce()
                self.workforce.append(temp_model.from_map(k))
        return self


class GetTaskWorkforceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTaskWorkforceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskWorkforceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskWorkforceStatisticRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        stat_type: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.stat_type = stat_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.stat_type is not None:
            result['StatType'] = self.stat_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StatType') is not None:
            self.stat_type = m.get('StatType')
        return self


class GetTaskWorkforceStatisticResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        total_page: int = None,
        users_statistic: List[UserStatistic] = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.total_page = total_page
        self.users_statistic = users_statistic

    def validate(self):
        if self.users_statistic:
            for k in self.users_statistic:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        result['UsersStatistic'] = []
        if self.users_statistic is not None:
            for k in self.users_statistic:
                result['UsersStatistic'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        self.users_statistic = []
        if m.get('UsersStatistic') is not None:
            for k in m.get('UsersStatistic'):
                temp_model = UserStatistic()
                self.users_statistic.append(temp_model.from_map(k))
        return self


class GetTaskWorkforceStatisticResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTaskWorkforceStatisticResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskWorkforceStatisticResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        template: TemplateDetail = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.request_id = request_id
        self.success = success
        self.template = template

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.template is not None:
            result['Template'] = self.template.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Template') is not None:
            temp_model = TemplateDetail()
            self.template = temp_model.from_map(m['Template'])
        return self


class GetTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateQuestionsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        question_configs: List[QuestionPlugin] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.question_configs = question_configs
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.question_configs:
            for k in self.question_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        result['QuestionConfigs'] = []
        if self.question_configs is not None:
            for k in self.question_configs:
                result['QuestionConfigs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.question_configs = []
        if m.get('QuestionConfigs') is not None:
            for k in m.get('QuestionConfigs'):
                temp_model = QuestionPlugin()
                self.question_configs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetTemplateQuestionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTemplateQuestionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTemplateQuestionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateViewResponseBodyViewConfigs(TeaModel):
    def __init__(
        self,
        view_plugins: List[ViewPlugin] = None,
    ):
        self.view_plugins = view_plugins

    def validate(self):
        if self.view_plugins:
            for k in self.view_plugins:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ViewPlugins'] = []
        if self.view_plugins is not None:
            for k in self.view_plugins:
                result['ViewPlugins'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.view_plugins = []
        if m.get('ViewPlugins') is not None:
            for k in m.get('ViewPlugins'):
                temp_model = ViewPlugin()
                self.view_plugins.append(temp_model.from_map(k))
        return self


class GetTemplateViewResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        view_configs: GetTemplateViewResponseBodyViewConfigs = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.request_id = request_id
        self.success = success
        self.view_configs = view_configs

    def validate(self):
        if self.view_configs:
            self.view_configs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.view_configs is not None:
            result['ViewConfigs'] = self.view_configs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ViewConfigs') is not None:
            temp_model = GetTemplateViewResponseBodyViewConfigs()
            self.view_configs = temp_model.from_map(m['ViewConfigs'])
        return self


class GetTemplateViewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTemplateViewResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTemplateViewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTenantResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        tenant: SingleTenant = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.request_id = request_id
        self.success = success
        self.tenant = tenant

    def validate(self):
        if self.tenant:
            self.tenant.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.tenant is not None:
            result['Tenant'] = self.tenant.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Tenant') is not None:
            temp_model = SingleTenant()
            self.tenant = temp_model.from_map(m['Tenant'])
        return self


class GetTenantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTenantResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTenantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        user: SimpleUser = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.request_id = request_id
        self.success = success
        self.user = user

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('User') is not None:
            temp_model = SimpleUser()
            self.user = temp_model.from_map(m['User'])
        return self


class GetUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobsRequest(TeaModel):
    def __init__(
        self,
        job_type: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.job_type = job_type
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListJobsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        jobs: List[Job] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.code = code
        self.details = details
        self.jobs = jobs
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.jobs:
            for k in self.jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        result['Jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['Jobs'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        self.jobs = []
        if m.get('Jobs') is not None:
            for k in m.get('Jobs'):
                temp_model = Job()
                self.jobs.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListJobsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubtaskItemsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListSubtaskItemsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        items: List[SubtaskItemDetail] = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.code = code
        self.details = details
        self.items = items
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = SubtaskItemDetail()
                self.items.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListSubtaskItemsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSubtaskItemsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSubtaskItemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubtasksRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListSubtasksResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        subtasks: List[SubtaskDetail] = None,
        success: bool = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.subtasks = subtasks
        self.success = success
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.subtasks:
            for k in self.subtasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Subtasks'] = []
        if self.subtasks is not None:
            for k in self.subtasks:
                result['Subtasks'].append(k.to_map() if k else None)
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.subtasks = []
        if m.get('Subtasks') is not None:
            for k in m.get('Subtasks'):
                temp_model = SubtaskDetail()
                self.subtasks.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListSubtasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSubtasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSubtasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTasksRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListTasksResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        tasks: List[SimpleTask] = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.tasks = tasks
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = SimpleTask()
                self.tasks.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplatesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        search_key: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.search_key is not None:
            result['SearchKey'] = self.search_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')
        return self


class ListTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        templates: List[SimpleTemplate] = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.templates = templates
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = SimpleTemplate()
                self.templates.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTenantsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListTenantsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        tenants: List[SimpleTenant] = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.tenants = tenants
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.tenants:
            for k in self.tenants:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        result['Tenants'] = []
        if self.tenants is not None:
            for k in self.tenants:
                result['Tenants'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.tenants = []
        if m.get('Tenants') is not None:
            for k in m.get('Tenants'):
                temp_model = SimpleTenant()
                self.tenants.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListTenantsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTenantsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTenantsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        total_page: int = None,
        users: List[SimpleUser] = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.total_page = total_page
        self.users = users

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = SimpleUser()
                self.users.append(temp_model.from_map(k))
        return self


class ListUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUsersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveWorkNodeWorkforceRequest(TeaModel):
    def __init__(
        self,
        user_ids: List[int] = None,
    ):
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class RemoveWorkNodeWorkforceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveWorkNodeWorkforceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveWorkNodeWorkforceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveWorkNodeWorkforceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTaskRequest(TeaModel):
    def __init__(
        self,
        body: UpdateTaskDTO = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = UpdateTaskDTO()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTaskWorkforceRequest(TeaModel):
    def __init__(
        self,
        workforce: List[SimpleWorkforce] = None,
    ):
        self.workforce = workforce

    def validate(self):
        if self.workforce:
            for k in self.workforce:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Workforce'] = []
        if self.workforce is not None:
            for k in self.workforce:
                result['Workforce'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.workforce = []
        if m.get('Workforce') is not None:
            for k in m.get('Workforce'):
                temp_model = SimpleWorkforce()
                self.workforce.append(temp_model.from_map(k))
        return self


class UpdateTaskWorkforceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateTaskWorkforceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTaskWorkforceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTaskWorkforceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTemplateRequest(TeaModel):
    def __init__(
        self,
        body: TemplateDTO = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = TemplateDTO()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        template_id: str = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.request_id = request_id
        self.success = success
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class UpdateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTenantRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        tenant_name: str = None,
    ):
        self.description = description
        self.tenant_name = tenant_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        return self


class UpdateTenantResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateTenantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTenantResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTenantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserRequest(TeaModel):
    def __init__(
        self,
        role: str = None,
        user_name: str = None,
    ):
        self.role = role
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role is not None:
            result['Role'] = self.role
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class UpdateUserResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        details: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        user_id: str = None,
    ):
        self.code = code
        self.details = details
        self.message = message
        self.request_id = request_id
        self.success = success
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.details is not None:
            result['Details'] = self.details
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UpdateUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


