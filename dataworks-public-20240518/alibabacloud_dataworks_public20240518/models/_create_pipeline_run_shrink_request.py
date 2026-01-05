# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePipelineRunShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        object_ids_shrink: str = None,
        project_id: int = None,
        type: str = None,
    ):
        # The description of the process.
        self.description = description
        # The IDs of entities to which you want to apply the process.
        # 
        # >  A process can be applied to only a single entity and its child entities. If you specify multiple entities in the array, the process is applied only to the first entity in the array and its child entities. Make sure that the array in your request contains only one element. Extra elements will be ignored.
        # 
        # This parameter is required.
        self.object_ids_shrink = object_ids_shrink
        # The DataWorks workspace ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the Workspace page to query the ID. You must configure this parameter to specify the DataWorks workspace to which the API operation is applied.
        # 
        # This parameter is required.
        self.project_id = project_id
        # Specifies whether to deploy or undeploy the entity. Valid values:
        # 
        # *   Online: deploys the entity.
        # *   Offline: undeploys the entity.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.object_ids_shrink is not None:
            result['ObjectIds'] = self.object_ids_shrink

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ObjectIds') is not None:
            self.object_ids_shrink = m.get('ObjectIds')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

