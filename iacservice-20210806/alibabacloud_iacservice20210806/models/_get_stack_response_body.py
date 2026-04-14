# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class GetStackResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        stack: main_models.GetStackResponseBodyStack = None,
    ):
        self.request_id = request_id
        self.stack = stack

    def validate(self):
        if self.stack:
            self.stack.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.stack is not None:
            result['stack'] = self.stack.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('stack') is not None:
            temp_model = main_models.GetStackResponseBodyStack()
            self.stack = temp_model.from_map(m.get('stack'))

        return self

class GetStackResponseBodyStack(DaraModel):
    def __init__(
        self,
        config: main_models.GetStackResponseBodyStackConfig = None,
        create_time: str = None,
        current_config_version: str = None,
        description: str = None,
        name: str = None,
        ram_role: str = None,
        source: str = None,
        source_path: str = None,
        stack_id: str = None,
        status: str = None,
        trigger_strategy: str = None,
        working_directory: str = None,
    ):
        self.config = config
        self.create_time = create_time
        self.current_config_version = current_config_version
        self.description = description
        self.name = name
        self.ram_role = ram_role
        self.source = source
        self.source_path = source_path
        self.stack_id = stack_id
        self.status = status
        self.trigger_strategy = trigger_strategy
        self.working_directory = working_directory

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config.to_map()

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.current_config_version is not None:
            result['currentConfigVersion'] = self.current_config_version

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.ram_role is not None:
            result['ramRole'] = self.ram_role

        if self.source is not None:
            result['source'] = self.source

        if self.source_path is not None:
            result['sourcePath'] = self.source_path

        if self.stack_id is not None:
            result['stackId'] = self.stack_id

        if self.status is not None:
            result['status'] = self.status

        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy

        if self.working_directory is not None:
            result['workingDirectory'] = self.working_directory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.GetStackResponseBodyStackConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('currentConfigVersion') is not None:
            self.current_config_version = m.get('currentConfigVersion')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')

        if m.get('stackId') is not None:
            self.stack_id = m.get('stackId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')

        if m.get('workingDirectory') is not None:
            self.working_directory = m.get('workingDirectory')

        return self

class GetStackResponseBodyStackConfig(DaraModel):
    def __init__(
        self,
        component_content: str = None,
        deployment_content: str = None,
    ):
        self.component_content = component_content
        self.deployment_content = deployment_content

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_content is not None:
            result['componentContent'] = self.component_content

        if self.deployment_content is not None:
            result['deploymentContent'] = self.deployment_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentContent') is not None:
            self.component_content = m.get('componentContent')

        if m.get('deploymentContent') is not None:
            self.deployment_content = m.get('deploymentContent')

        return self

