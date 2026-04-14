# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class ListStackConfigsResponseBody(DaraModel):
    def __init__(
        self,
        configs: List[main_models.ListStackConfigsResponseBodyConfigs] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.configs = configs
        self.max_results = max_results
        # This parameter is required.
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.configs:
            for v1 in self.configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['configs'] = []
        if self.configs is not None:
            for k1 in self.configs:
                result['configs'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('configs') is not None:
            for k1 in m.get('configs'):
                temp_model = main_models.ListStackConfigsResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListStackConfigsResponseBodyConfigs(DaraModel):
    def __init__(
        self,
        component_config: main_models.ListStackConfigsResponseBodyConfigsComponentConfig = None,
        component_content: str = None,
        create_time: str = None,
        deployment_config: main_models.ListStackConfigsResponseBodyConfigsDeploymentConfig = None,
        deployment_content: str = None,
        status: str = None,
        version: str = None,
    ):
        self.component_config = component_config
        self.component_content = component_content
        self.create_time = create_time
        self.deployment_config = deployment_config
        self.deployment_content = deployment_content
        self.status = status
        self.version = version

    def validate(self):
        if self.component_config:
            self.component_config.validate()
        if self.deployment_config:
            self.deployment_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_config is not None:
            result['componentConfig'] = self.component_config.to_map()

        if self.component_content is not None:
            result['componentContent'] = self.component_content

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.deployment_config is not None:
            result['deploymentConfig'] = self.deployment_config.to_map()

        if self.deployment_content is not None:
            result['deploymentContent'] = self.deployment_content

        if self.status is not None:
            result['status'] = self.status

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentConfig') is not None:
            temp_model = main_models.ListStackConfigsResponseBodyConfigsComponentConfig()
            self.component_config = temp_model.from_map(m.get('componentConfig'))

        if m.get('componentContent') is not None:
            self.component_content = m.get('componentContent')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('deploymentConfig') is not None:
            temp_model = main_models.ListStackConfigsResponseBodyConfigsDeploymentConfig()
            self.deployment_config = temp_model.from_map(m.get('deploymentConfig'))

        if m.get('deploymentContent') is not None:
            self.deployment_content = m.get('deploymentContent')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class ListStackConfigsResponseBodyConfigsDeploymentConfig(DaraModel):
    def __init__(
        self,
        deployment: List[main_models.ListStackConfigsResponseBodyConfigsDeploymentConfigDeployment] = None,
        publish_output: List[main_models.ListStackConfigsResponseBodyConfigsDeploymentConfigPublishOutput] = None,
        upstream_input: List[main_models.ListStackConfigsResponseBodyConfigsDeploymentConfigUpstreamInput] = None,
    ):
        self.deployment = deployment
        self.publish_output = publish_output
        self.upstream_input = upstream_input

    def validate(self):
        if self.deployment:
            for v1 in self.deployment:
                 if v1:
                    v1.validate()
        if self.publish_output:
            for v1 in self.publish_output:
                 if v1:
                    v1.validate()
        if self.upstream_input:
            for v1 in self.upstream_input:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['deployment'] = []
        if self.deployment is not None:
            for k1 in self.deployment:
                result['deployment'].append(k1.to_map() if k1 else None)

        result['publishOutput'] = []
        if self.publish_output is not None:
            for k1 in self.publish_output:
                result['publishOutput'].append(k1.to_map() if k1 else None)

        result['upstreamInput'] = []
        if self.upstream_input is not None:
            for k1 in self.upstream_input:
                result['upstreamInput'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.deployment = []
        if m.get('deployment') is not None:
            for k1 in m.get('deployment'):
                temp_model = main_models.ListStackConfigsResponseBodyConfigsDeploymentConfigDeployment()
                self.deployment.append(temp_model.from_map(k1))

        self.publish_output = []
        if m.get('publishOutput') is not None:
            for k1 in m.get('publishOutput'):
                temp_model = main_models.ListStackConfigsResponseBodyConfigsDeploymentConfigPublishOutput()
                self.publish_output.append(temp_model.from_map(k1))

        self.upstream_input = []
        if m.get('upstreamInput') is not None:
            for k1 in m.get('upstreamInput'):
                temp_model = main_models.ListStackConfigsResponseBodyConfigsDeploymentConfigUpstreamInput()
                self.upstream_input.append(temp_model.from_map(k1))

        return self

class ListStackConfigsResponseBodyConfigsDeploymentConfigUpstreamInput(DaraModel):
    def __init__(
        self,
        name: str = None,
        source: str = None,
    ):
        self.name = name
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.source is not None:
            result['source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('source') is not None:
            self.source = m.get('source')

        return self

class ListStackConfigsResponseBodyConfigsDeploymentConfigPublishOutput(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        result: str = None,
        type: str = None,
        value: str = None,
    ):
        self.description = description
        self.name = name
        self.result = result
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.result is not None:
            result['result'] = self.result

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('result') is not None:
            self.result = m.get('result')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class ListStackConfigsResponseBodyConfigsDeploymentConfigDeployment(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class ListStackConfigsResponseBodyConfigsComponentConfig(DaraModel):
    def __init__(
        self,
        component: List[main_models.ListStackConfigsResponseBodyConfigsComponentConfigComponent] = None,
        output: List[main_models.ListStackConfigsResponseBodyConfigsComponentConfigOutput] = None,
        variable: List[main_models.ListStackConfigsResponseBodyConfigsComponentConfigVariable] = None,
    ):
        self.component = component
        self.output = output
        self.variable = variable

    def validate(self):
        if self.component:
            for v1 in self.component:
                 if v1:
                    v1.validate()
        if self.output:
            for v1 in self.output:
                 if v1:
                    v1.validate()
        if self.variable:
            for v1 in self.variable:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['component'] = []
        if self.component is not None:
            for k1 in self.component:
                result['component'].append(k1.to_map() if k1 else None)

        result['output'] = []
        if self.output is not None:
            for k1 in self.output:
                result['output'].append(k1.to_map() if k1 else None)

        result['variable'] = []
        if self.variable is not None:
            for k1 in self.variable:
                result['variable'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.component = []
        if m.get('component') is not None:
            for k1 in m.get('component'):
                temp_model = main_models.ListStackConfigsResponseBodyConfigsComponentConfigComponent()
                self.component.append(temp_model.from_map(k1))

        self.output = []
        if m.get('output') is not None:
            for k1 in m.get('output'):
                temp_model = main_models.ListStackConfigsResponseBodyConfigsComponentConfigOutput()
                self.output.append(temp_model.from_map(k1))

        self.variable = []
        if m.get('variable') is not None:
            for k1 in m.get('variable'):
                temp_model = main_models.ListStackConfigsResponseBodyConfigsComponentConfigVariable()
                self.variable.append(temp_model.from_map(k1))

        return self

class ListStackConfigsResponseBodyConfigsComponentConfigVariable(DaraModel):
    def __init__(
        self,
        default: str = None,
        description: str = None,
        name: str = None,
        type: str = None,
    ):
        self.default = default
        self.description = description
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default is not None:
            result['default'] = self.default

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('default') is not None:
            self.default = m.get('default')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListStackConfigsResponseBodyConfigsComponentConfigOutput(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        self.description = description
        self.name = name
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class ListStackConfigsResponseBodyConfigsComponentConfigComponent(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        return self

