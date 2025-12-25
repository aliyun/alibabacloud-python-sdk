# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class RunTranslateGenerationRequest(DaraModel):
    def __init__(
        self,
        prompt: str = None,
        reference_data: main_models.RunTranslateGenerationRequestReferenceData = None,
        task_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.prompt = prompt
        # This parameter is required.
        self.reference_data = reference_data
        self.task_id = task_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.reference_data:
            self.reference_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.reference_data is not None:
            result['ReferenceData'] = self.reference_data.to_map()

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('ReferenceData') is not None:
            temp_model = main_models.RunTranslateGenerationRequestReferenceData()
            self.reference_data = temp_model.from_map(m.get('ReferenceData'))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class RunTranslateGenerationRequestReferenceData(DaraModel):
    def __init__(
        self,
        contents: List[str] = None,
    ):
        # This parameter is required.
        self.contents = contents

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contents is not None:
            result['Contents'] = self.contents

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contents') is not None:
            self.contents = m.get('Contents')

        return self

