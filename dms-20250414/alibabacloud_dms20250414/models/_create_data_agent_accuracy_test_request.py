# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDataAgentAccuracyTestRequest(DaraModel):
    def __init__(
        self,
        custom_agent_id: str = None,
        dataset: str = None,
        datasource: str = None,
        desc: str = None,
        dms_unit: str = None,
        evaluation_prompt: str = None,
        file_id: str = None,
        language: str = None,
        max_concurrent: int = None,
        mode: int = None,
        name: str = None,
        need_delete: bool = None,
        region_id: str = None,
        workspace_id: str = None,
    ):
        # The ID of the custom agent to be tested for accuracy.
        self.custom_agent_id = custom_agent_id
        # Deprecated.
        self.dataset = dataset
        # The data source. We recommend that you configure this in the custom agent.
        self.datasource = datasource
        # The description.
        self.desc = desc
        # The DMS unit used to create the resource.
        self.dms_unit = dms_unit
        # The accuracy evaluation criteria. An empty value indicates the default criteria.
        self.evaluation_prompt = evaluation_prompt
        # The file ID in the data center.
        self.file_id = file_id
        # The language used for the analysis task.
        self.language = language
        # The maximum number of concurrent sessions during the test.
        self.max_concurrent = max_concurrent
        # The analysis mode.
        self.mode = mode
        # The name of the test item.
        self.name = name
        # Specifies whether sessions are displayed after analysis. This parameter is not supported.
        self.need_delete = need_delete
        # The region ID.
        self.region_id = region_id
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_agent_id is not None:
            result['CustomAgentId'] = self.custom_agent_id

        if self.dataset is not None:
            result['Dataset'] = self.dataset

        if self.datasource is not None:
            result['Datasource'] = self.datasource

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.dms_unit is not None:
            result['DmsUnit'] = self.dms_unit

        if self.evaluation_prompt is not None:
            result['EvaluationPrompt'] = self.evaluation_prompt

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.language is not None:
            result['Language'] = self.language

        if self.max_concurrent is not None:
            result['MaxConcurrent'] = self.max_concurrent

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.name is not None:
            result['Name'] = self.name

        if self.need_delete is not None:
            result['NeedDelete'] = self.need_delete

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomAgentId') is not None:
            self.custom_agent_id = m.get('CustomAgentId')

        if m.get('Dataset') is not None:
            self.dataset = m.get('Dataset')

        if m.get('Datasource') is not None:
            self.datasource = m.get('Datasource')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('DmsUnit') is not None:
            self.dms_unit = m.get('DmsUnit')

        if m.get('EvaluationPrompt') is not None:
            self.evaluation_prompt = m.get('EvaluationPrompt')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('MaxConcurrent') is not None:
            self.max_concurrent = m.get('MaxConcurrent')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NeedDelete') is not None:
            self.need_delete = m.get('NeedDelete')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

