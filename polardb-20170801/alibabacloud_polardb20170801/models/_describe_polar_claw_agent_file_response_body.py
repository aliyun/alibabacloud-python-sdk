# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribePolarClawAgentFileResponseBody(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        application_id: str = None,
        code: int = None,
        file: main_models.DescribePolarClawAgentFileResponseBodyFile = None,
        message: str = None,
        request_id: str = None,
        workspace: str = None,
    ):
        # Agent ID
        self.agent_id = agent_id
        # The application ID.
        self.application_id = application_id
        # The response status code.
        self.code = code
        # The file details.
        self.file = file
        # The response message.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # The working directory path.
        self.workspace = workspace

    def validate(self):
        if self.file:
            self.file.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.code is not None:
            result['Code'] = self.code

        if self.file is not None:
            result['File'] = self.file.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.workspace is not None:
            result['Workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('File') is not None:
            temp_model = main_models.DescribePolarClawAgentFileResponseBodyFile()
            self.file = temp_model.from_map(m.get('File'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')

        return self

class DescribePolarClawAgentFileResponseBodyFile(DaraModel):
    def __init__(
        self,
        content: str = None,
        missing: bool = None,
        name: str = None,
        path: str = None,
        size: int = None,
        updated_at_ms: int = None,
    ):
        # The file content.
        self.content = content
        # Indicates whether the file is missing.
        self.missing = missing
        # The file name.
        self.name = name
        # The file path.
        self.path = path
        # The file size, in bytes.
        self.size = size
        # The last updated UNIX timestamp, in milliseconds.
        self.updated_at_ms = updated_at_ms

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.missing is not None:
            result['Missing'] = self.missing

        if self.name is not None:
            result['Name'] = self.name

        if self.path is not None:
            result['Path'] = self.path

        if self.size is not None:
            result['Size'] = self.size

        if self.updated_at_ms is not None:
            result['UpdatedAtMs'] = self.updated_at_ms

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Missing') is not None:
            self.missing = m.get('Missing')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('UpdatedAtMs') is not None:
            self.updated_at_ms = m.get('UpdatedAtMs')

        return self

