# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePipelineRunShrinkRequest(DaraModel):
    def __init__(
        self,
        auto_run_until_stage: str = None,
        description: str = None,
        object_ids_shrink: str = None,
        project_id: int = None,
        run_mode: str = None,
        type: str = None,
    ):
        # The code of the stage in the publish process. This parameter takes effect only when RunMode is set to Auto. After the publish process is created, it automatically runs to the specified stage.
        # 
        # >Notice: The specified stage is automatically completed. For example, if you set this parameter to DEV, the automatic run stops after the DEV stage reaches the desired state.
        self.auto_run_until_stage = auto_run_until_stage
        # The description of the publish process.
        self.description = description
        # The list of entity IDs that you want to publish in this publish process.
        # >Notice: Only a single entity and its child entities can be published at a time. Only the first entity in this array and its child entities are published. Make sure that the length of this array is 1. Entities beyond the first one are ignored.
        # 
        # This parameter is required.
        self.object_ids_shrink = object_ids_shrink
        # The ID of the DataWorks workspace. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console) and go to the workspace configuration page to obtain the workspace ID.
        # This parameter specifies the DataWorks workspace for this API call.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The run mode of the publish process. Default value: Normal. If you set this parameter to Auto, the publish process is automatically driven to the specified stage. This parameter is used together with the AutoRunUntilStage parameter.
        # 
        # Valid values:
        # - Normal
        # - Auto
        self.run_mode = run_mode
        # Specifies whether the publish process is used to bring an entity online or offline.
        # 
        # - Online: online
        # 
        # - Offline: offline
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
        if self.auto_run_until_stage is not None:
            result['AutoRunUntilStage'] = self.auto_run_until_stage

        if self.description is not None:
            result['Description'] = self.description

        if self.object_ids_shrink is not None:
            result['ObjectIds'] = self.object_ids_shrink

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.run_mode is not None:
            result['RunMode'] = self.run_mode

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRunUntilStage') is not None:
            self.auto_run_until_stage = m.get('AutoRunUntilStage')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ObjectIds') is not None:
            self.object_ids_shrink = m.get('ObjectIds')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

