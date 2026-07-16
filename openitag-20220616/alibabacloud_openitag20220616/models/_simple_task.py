# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_openitag20220616 import models as main_models
from darabonba.model import DaraModel

class SimpleTask(DaraModel):
    def __init__(
        self,
        archived: bool = None,
        archived_infos: str = None,
        creator: main_models.SimpleUser = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        label_style: str = None,
        modifier: main_models.SimpleUser = None,
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
        # Indicates whether the job is archived. Possible values:  
        # - false: Not archived.  
        # - true: Archived.
        self.archived = archived
        # Data archiving information.
        self.archived_infos = archived_infos
        # Creator information.
        self.creator = creator
        # UTC creation time.
        self.gmt_create_time = gmt_create_time
        # UTC time of the last update.
        self.gmt_modified_time = gmt_modified_time
        # Label style.
        self.label_style = label_style
        # Updated By information.
        self.modifier = modifier
        # Auto triggered task ID.
        self.ref_task_id = ref_task_id
        # Remarks.
        self.remark = remark
        # Current streaming node. Possible values:  
        # - MARK: Annotating.  
        # - CHECK: Checking.  
        # - FINISHED: Completed.
        self.stage = stage
        # Task Status. Possible values:  
        # - CREATED  
        # - SUCCESS
        self.status = status
        # List of job labels.
        self.tags = tags
        # Job ID.
        self.task_id = task_id
        # Job name.
        self.task_name = task_name
        # Task Type.
        self.task_type = task_type
        # Template ID.
        self.template_id = template_id
        # Tenant ID.
        self.tenant_id = tenant_id
        # UUID.
        self.uuid = uuid
        # Pipeline nodes.
        self.workflow_nodes = workflow_nodes

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.modifier:
            self.modifier.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            temp_model = main_models.SimpleUser()
            self.creator = temp_model.from_map(m.get('Creator'))

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('LabelStyle') is not None:
            self.label_style = m.get('LabelStyle')

        if m.get('Modifier') is not None:
            temp_model = main_models.SimpleUser()
            self.modifier = temp_model.from_map(m.get('Modifier'))

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

