# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTaskRequest(DaraModel):
    def __init__(
        self,
        entity_id: str = None,
        entity_type: str = None,
        entity_version_id: str = None,
        task_category: str = None,
        task_id: str = None,
        task_type: str = None,
    ):
        # The associated resource ID. **If you do not specify TaskId, you must specify EntityId, EntityType, and TaskCategory at the same time.** The resource ID must match the selected resource type.
        self.entity_id = entity_id
        # The associated resource type. This parameter is required if you do not specify TaskId.
        # 
        # Valid values:
        # - **IMAGE**: Image resource.
        # - **APP**: Application resource.
        # - **SNAPSHOT**: Snapshot resource.
        # 
        # You must also specify a valid TaskCategory. The resource type itself does not mean that all task categories can be queried by resource.
        self.entity_type = entity_type
        # The associated resource version ID. This parameter is used to specify the version when you query by resource. For image resources, specify the image version ID.
        self.entity_version_id = entity_version_id
        # The task category when you query by resource. This parameter is required if you do not specify TaskId.
        # 
        # Valid values:
        # - **IMAGE_BUILDER**: Image creation. Queries tasks for manual creation, automatic creation, or creation based on an instance.
        # - **IMAGE_DISTRIBUTE**: Image distribution across regions.
        self.task_category = task_category
        # The task ID. If you specify this parameter, the system queries the task by this ID, and the resource information query conditions are ignored.
        self.task_id = task_id
        # **Not enabled. Do not specify this parameter.** When you query a task, locate the task by using TaskId or the combination of resource information and TaskCategory. This parameter is not used for task filtering.
        # 
        # The example "Not applicable (not enabled)" is only a description of the field status and is not a valid parameter value.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.entity_version_id is not None:
            result['EntityVersionId'] = self.entity_version_id

        if self.task_category is not None:
            result['TaskCategory'] = self.task_category

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('EntityVersionId') is not None:
            self.entity_version_id = m.get('EntityVersionId')

        if m.get('TaskCategory') is not None:
            self.task_category = m.get('TaskCategory')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

