# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class GetPipelineRunResponseBody(DaraModel):
    def __init__(
        self,
        pipeline: main_models.GetPipelineRunResponseBodyPipeline = None,
        request_id: str = None,
    ):
        # The information about the process.
        self.pipeline = pipeline
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.pipeline:
            self.pipeline.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pipeline is not None:
            result['Pipeline'] = self.pipeline.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Pipeline') is not None:
            temp_model = main_models.GetPipelineRunResponseBodyPipeline()
            self.pipeline = temp_model.from_map(m.get('Pipeline'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPipelineRunResponseBodyPipeline(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        creator: str = None,
        description: str = None,
        id: str = None,
        message: str = None,
        modify_time: int = None,
        project_id: int = None,
        stages: List[main_models.GetPipelineRunResponseBodyPipelineStages] = None,
        status: str = None,
    ):
        # The time when the process was created. This value is a UNIX timestamp.
        self.create_time = create_time
        # The creator of the process.
        self.creator = creator
        self.description = description
        # The process ID.
        self.id = id
        # The error message returned when the process fails.
        self.message = message
        # The time when the process was modified. This value is a UNIX timestamp.
        self.modify_time = modify_time
        # The DataWorks workspace ID.
        self.project_id = project_id
        # The information about stages in the process.
        self.stages = stages
        # The status of the process.
        # 
        # Valid values:
        # 
        # *   Init
        # *   Running
        # *   Success
        # *   Fail
        # *   Termination
        # *   Cancel
        self.status = status

    def validate(self):
        if self.stages:
            for v1 in self.stages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.message is not None:
            result['Message'] = self.message

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        result['Stages'] = []
        if self.stages is not None:
            for k1 in self.stages:
                result['Stages'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        self.stages = []
        if m.get('Stages') is not None:
            for k1 in m.get('Stages'):
                temp_model = main_models.GetPipelineRunResponseBodyPipelineStages()
                self.stages.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetPipelineRunResponseBodyPipelineStages(DaraModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        detail: Dict[str, Any] = None,
        message: str = None,
        name: str = None,
        status: str = None,
        step: int = None,
        type: str = None,
    ):
        # The code of the stage.
        self.code = code
        # The description of the stage.
        self.description = description
        # The details of the stage.
        self.detail = detail
        # The error message returned for the stage.
        self.message = message
        # The name of the stage.
        self.name = name
        # The status of the stage.
        # 
        # Valid values:
        # 
        # *   Init
        # *   Running
        # *   Success
        # *   Fail
        # *   Termination
        # *   Cancel
        self.status = status
        # The step number of the stage.
        self.step = step
        # The type of the stage.
        # 
        # Valid values:
        # 
        # *   Deploy
        # *   Check
        # *   Offline
        # *   Build
        # *   Delete
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.description is not None:
            result['Description'] = self.description

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.message is not None:
            result['Message'] = self.message

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        if self.step is not None:
            result['Step'] = self.step

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

