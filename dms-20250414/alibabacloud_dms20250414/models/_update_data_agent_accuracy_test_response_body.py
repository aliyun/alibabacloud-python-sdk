# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class UpdateDataAgentAccuracyTestResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.UpdateDataAgentAccuracyTestResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The response struct.
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.                                 
        # - **false**: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.UpdateDataAgentAccuracyTestResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdateDataAgentAccuracyTestResponseBodyData(DaraModel):
    def __init__(
        self,
        accuracy_test: str = None,
        agent_id: str = None,
        dataset: str = None,
        datasource: str = None,
        desc: str = None,
        evaluation_prompt: str = None,
        file_id: str = None,
        max_concurrent: int = None,
        mode: int = None,
        name: str = None,
        need_delete: bool = None,
        workspace_id: str = None,
    ):
        # The ID of the accuracy test item.
        self.accuracy_test = accuracy_test
        # Agent Id
        self.agent_id = agent_id
        # The data source. We recommend that you configure this parameter in a custom agent.
        self.dataset = dataset
        self.datasource = datasource
        self.desc = desc
        # The accuracy evaluation criteria. An empty value indicates the default criteria.
        self.evaluation_prompt = evaluation_prompt
        # The file ID.
        self.file_id = file_id
        self.max_concurrent = max_concurrent
        # The analysis mode.
        self.mode = mode
        self.name = name
        self.need_delete = need_delete
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accuracy_test is not None:
            result['AccuracyTest'] = self.accuracy_test

        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.dataset is not None:
            result['Dataset'] = self.dataset

        if self.datasource is not None:
            result['Datasource'] = self.datasource

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.evaluation_prompt is not None:
            result['EvaluationPrompt'] = self.evaluation_prompt

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.max_concurrent is not None:
            result['MaxConcurrent'] = self.max_concurrent

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.name is not None:
            result['Name'] = self.name

        if self.need_delete is not None:
            result['NeedDelete'] = self.need_delete

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccuracyTest') is not None:
            self.accuracy_test = m.get('AccuracyTest')

        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('Dataset') is not None:
            self.dataset = m.get('Dataset')

        if m.get('Datasource') is not None:
            self.datasource = m.get('Datasource')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('EvaluationPrompt') is not None:
            self.evaluation_prompt = m.get('EvaluationPrompt')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('MaxConcurrent') is not None:
            self.max_concurrent = m.get('MaxConcurrent')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NeedDelete') is not None:
            self.need_delete = m.get('NeedDelete')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

