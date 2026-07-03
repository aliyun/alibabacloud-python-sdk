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
        evaluation_prompt: str = None,
        file_id: str = None,
        mode: int = None,
        workspace_id: str = None,
    ):
        # The ID of the accuracy test item.
        self.accuracy_test = accuracy_test
        # Agent Id
        self.agent_id = agent_id
        # The data source. We recommend that you configure this in the custom agent.
        self.dataset = dataset
        # The accuracy evaluation criteria. An empty value indicates the default criteria.
        self.evaluation_prompt = evaluation_prompt
        # The file ID.
        self.file_id = file_id
        # The analysis mode.
        self.mode = mode
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

        if self.evaluation_prompt is not None:
            result['EvaluationPrompt'] = self.evaluation_prompt

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.mode is not None:
            result['Mode'] = self.mode

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

        if m.get('EvaluationPrompt') is not None:
            self.evaluation_prompt = m.get('EvaluationPrompt')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

