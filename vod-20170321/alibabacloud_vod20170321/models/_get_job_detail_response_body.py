# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetJobDetailResponseBody(DaraModel):
    def __init__(
        self,
        aijob_detail: main_models.GetJobDetailResponseBodyAIJobDetail = None,
        job_type: str = None,
        request_id: str = None,
        snapshot_job_detail: main_models.GetJobDetailResponseBodySnapshotJobDetail = None,
        transcode_job_detail: main_models.GetJobDetailResponseBodyTranscodeJobDetail = None,
        workflow_task_detail: main_models.GetJobDetailResponseBodyWorkflowTaskDetail = None,
    ):
        # The details of the AI task. This field has a value only when TaskType is AI.
        self.aijob_detail = aijob_detail
        # The task type.
        self.job_type = job_type
        # The request ID.
        self.request_id = request_id
        # The details of the snapshot task. This field has a value only when jobType is Snapshot.
        self.snapshot_job_detail = snapshot_job_detail
        # The details of the transcoding task. This field has a value only when jobType is Transcode.
        self.transcode_job_detail = transcode_job_detail
        # The details of the workflow task. This field has a value only when TaskType is Workflow.
        self.workflow_task_detail = workflow_task_detail

    def validate(self):
        if self.aijob_detail:
            self.aijob_detail.validate()
        if self.snapshot_job_detail:
            self.snapshot_job_detail.validate()
        if self.transcode_job_detail:
            self.transcode_job_detail.validate()
        if self.workflow_task_detail:
            self.workflow_task_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aijob_detail is not None:
            result['AIJobDetail'] = self.aijob_detail.to_map()

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.snapshot_job_detail is not None:
            result['SnapshotJobDetail'] = self.snapshot_job_detail.to_map()

        if self.transcode_job_detail is not None:
            result['TranscodeJobDetail'] = self.transcode_job_detail.to_map()

        if self.workflow_task_detail is not None:
            result['WorkflowTaskDetail'] = self.workflow_task_detail.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AIJobDetail') is not None:
            temp_model = main_models.GetJobDetailResponseBodyAIJobDetail()
            self.aijob_detail = temp_model.from_map(m.get('AIJobDetail'))

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SnapshotJobDetail') is not None:
            temp_model = main_models.GetJobDetailResponseBodySnapshotJobDetail()
            self.snapshot_job_detail = temp_model.from_map(m.get('SnapshotJobDetail'))

        if m.get('TranscodeJobDetail') is not None:
            temp_model = main_models.GetJobDetailResponseBodyTranscodeJobDetail()
            self.transcode_job_detail = temp_model.from_map(m.get('TranscodeJobDetail'))

        if m.get('WorkflowTaskDetail') is not None:
            temp_model = main_models.GetJobDetailResponseBodyWorkflowTaskDetail()
            self.workflow_task_detail = temp_model.from_map(m.get('WorkflowTaskDetail'))

        return self

class GetJobDetailResponseBodyWorkflowTaskDetail(DaraModel):
    def __init__(
        self,
        activity_results: str = None,
        create_time: str = None,
        finish_time: str = None,
        status: str = None,
        task_id: str = None,
        task_input: str = None,
        user_data: str = None,
        workflow: main_models.GetJobDetailResponseBodyWorkflowTaskDetailWorkflow = None,
    ):
        # The processing results of each workflow node, in JSON format.
        self.activity_results = activity_results
        # The time when the task was created, in UTC. Format: YYYY-MM-DDTHH:MM:SSZ.
        self.create_time = create_time
        # The time when the task was completed.
        self.finish_time = finish_time
        # The task status. Valid values:
        # 
        # - Init: started.
        # - Processing: processing in progress.
        # - Succeed: succeeded.
        # - Failed: failed.
        # - Canceled: canceled.
        # - Skip: skipped.
        self.status = status
        # The task ID.
        self.task_id = task_id
        # The media asset information.
        self.task_input = task_input
        # The custom settings. The value is a JSON string that supports message callback, upload acceleration, and other settings.
        self.user_data = user_data
        # The workflow details.
        self.workflow = workflow

    def validate(self):
        if self.workflow:
            self.workflow.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_results is not None:
            result['ActivityResults'] = self.activity_results

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_input is not None:
            result['TaskInput'] = self.task_input

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.workflow is not None:
            result['Workflow'] = self.workflow.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityResults') is not None:
            self.activity_results = m.get('ActivityResults')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskInput') is not None:
            self.task_input = m.get('TaskInput')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('Workflow') is not None:
            temp_model = main_models.GetJobDetailResponseBodyWorkflowTaskDetailWorkflow()
            self.workflow = temp_model.from_map(m.get('Workflow'))

        return self

class GetJobDetailResponseBodyWorkflowTaskDetailWorkflow(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        create_time: str = None,
        modified_time: str = None,
        name: str = None,
        status: str = None,
        type: str = None,
        workflow_id: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The time when the workflow was created, in UTC. Format: YYYY-MM-DDTHH:MM:SSZ.
        self.create_time = create_time
        # The time when the workflow was last modified.
        self.modified_time = modified_time
        # The workflow name.
        self.name = name
        # The workflow status. Valid values:
        # - Active: activated.
        # - Inactive: not activated.
        # - Deleted: deleted.
        self.status = status
        # The workflow type. Not populated by default.
        self.type = type
        # The workflow ID.
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

class GetJobDetailResponseBodyTranscodeJobDetail(DaraModel):
    def __init__(
        self,
        complete_time: str = None,
        create_time: str = None,
        definition: str = None,
        job_id: str = None,
        status: str = None,
        template_id: str = None,
        user_id: int = None,
        video_id: str = None,
    ):
        # The time when the task was completed.
        self.complete_time = complete_time
        # The time when the task was created, in UTC. Format: YYYY-MM-DDTHH:MM:SSZ.
        self.create_time = create_time
        # The definition.
        self.definition = definition
        # The task ID.
        self.job_id = job_id
        # The task status. Valid values:
        # 
        # - Submitted: submitted.
        # - Transcoding: transcoding in progress.
        # - TranscodeSuccess: transcoding succeeded.
        # - TranscodeFail: transcoding failed.
        # - TranscodeCancelled: transcoding canceled.
        self.status = status
        # The template ID.
        self.template_id = template_id
        # The ID of the user who initiated the task.
        self.user_id = user_id
        # The media asset ID.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.definition is not None:
            result['Definition'] = self.definition

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.status is not None:
            result['Status'] = self.status

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Definition') is not None:
            self.definition = m.get('Definition')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

class GetJobDetailResponseBodySnapshotJobDetail(DaraModel):
    def __init__(
        self,
        complete_time: str = None,
        create_time: str = None,
        job_id: str = None,
        normal_config: str = None,
        sprite_config: str = None,
        status: str = None,
        trigger: str = None,
        user_id: int = None,
        video_id: str = None,
    ):
        # The time when the task was completed.
        self.complete_time = complete_time
        # The time when the task was created, in UTC. Format: YYYY-MM-DDTHH:MM:SSZ.
        self.create_time = create_time
        # The task ID.
        self.job_id = job_id
        # The normal snapshot configuration.
        self.normal_config = normal_config
        # The sprite configuration.
        self.sprite_config = sprite_config
        # The task status. Valid values:
        # 
        # - Processing: processing in progress.
        # - Fail: task failed.
        # - Success: task succeeded.
        self.status = status
        # The trigger method. Valid values:
        # 
        # - Auto: automatically triggered by a workflow.
        # - Manual: manually submitted.
        self.trigger = trigger
        # The ID of the user who initiated the task.
        self.user_id = user_id
        # The media asset ID.
        self.video_id = video_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.normal_config is not None:
            result['NormalConfig'] = self.normal_config

        if self.sprite_config is not None:
            result['SpriteConfig'] = self.sprite_config

        if self.status is not None:
            result['Status'] = self.status

        if self.trigger is not None:
            result['Trigger'] = self.trigger

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.video_id is not None:
            result['VideoId'] = self.video_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('NormalConfig') is not None:
            self.normal_config = m.get('NormalConfig')

        if m.get('SpriteConfig') is not None:
            self.sprite_config = m.get('SpriteConfig')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Trigger') is not None:
            self.trigger = m.get('Trigger')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('VideoId') is not None:
            self.video_id = m.get('VideoId')

        return self

class GetJobDetailResponseBodyAIJobDetail(DaraModel):
    def __init__(
        self,
        complete_time: str = None,
        create_time: str = None,
        job_id: str = None,
        job_type: str = None,
        media_id: str = None,
        status: str = None,
        template_config: str = None,
        trigger: str = None,
        user_id: int = None,
    ):
        # The time when the task was completed.
        self.complete_time = complete_time
        # The time when the task was created, in UTC. Format: YYYY-MM-DDTHH:MM:SSZ.
        self.create_time = create_time
        # The task ID.
        self.job_id = job_id
        # The AI task type.
        self.job_type = job_type
        # The media asset ID.
        self.media_id = media_id
        # The task status. Valid values:
        # - reserved: submitted.
        # - init: started.
        # - success: execution succeeded.
        # - fail: execution failed.
        # - processing: processing in progress.
        # - analysing: analysis in progress.
        self.status = status
        # The template configuration.
        self.template_config = template_config
        # The trigger method. Valid values:
        # 
        # - Auto: automatically triggered by a workflow.
        # - Manual: manually submitted.
        self.trigger = trigger
        # The ID of the user who initiated the task.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.status is not None:
            result['Status'] = self.status

        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config

        if self.trigger is not None:
            result['Trigger'] = self.trigger

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')

        if m.get('Trigger') is not None:
            self.trigger = m.get('Trigger')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

