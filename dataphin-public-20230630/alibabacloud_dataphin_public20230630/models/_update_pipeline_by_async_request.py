# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdatePipelineByAsyncRequest(DaraModel):
    def __init__(
        self,
        context: main_models.UpdatePipelineByAsyncRequestContext = None,
        op_tenant_id: int = None,
        update_command: main_models.UpdatePipelineByAsyncRequestUpdateCommand = None,
    ):
        # The request context information.
        # 
        # This parameter is required.
        self.context = context
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The pipeline node update configuration.
        # 
        # This parameter is required.
        self.update_command = update_command

    def validate(self):
        if self.context:
            self.context.validate()
        if self.update_command:
            self.update_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context is not None:
            result['Context'] = self.context.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.update_command is not None:
            result['UpdateCommand'] = self.update_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            temp_model = main_models.UpdatePipelineByAsyncRequestContext()
            self.context = temp_model.from_map(m.get('Context'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('UpdateCommand') is not None:
            temp_model = main_models.UpdatePipelineByAsyncRequestUpdateCommand()
            self.update_command = temp_model.from_map(m.get('UpdateCommand'))

        return self

class UpdatePipelineByAsyncRequestUpdateCommand(DaraModel):
    def __init__(
        self,
        comment: str = None,
        mode: str = None,
        node_info: main_models.UpdatePipelineByAsyncRequestUpdateCommandNodeInfo = None,
        pipeline_config: main_models.UpdatePipelineByAsyncRequestUpdateCommandPipelineConfig = None,
        pipeline_json: str = None,
        pipeline_type: int = None,
        schedule_config: str = None,
        settings: str = None,
        submit: bool = None,
    ):
        # The remarks.
        self.comment = comment
        # The integration pipeline configuration mode. Valid values:
        # 
        # - PIPELINE: pipeline mode (default).
        # - JSON: script mode.
        # 
        # This parameter is not applicable to workflow nodes.
        self.mode = mode
        # The basic information of the integration pipeline node.
        # 
        # This parameter is required.
        self.node_info = node_info
        # The integration pipeline component configuration.
        # 
        # This parameter is required.
        self.pipeline_config = pipeline_config
        # The integration pipeline configuration in JSON string format for script mode. Workflow nodes do not support script mode.
        self.pipeline_json = pipeline_json
        # The node type. Valid values:
        # 
        # - 0: batch integration (default).
        # - 1: real-time integration.
        # - 14: workflow node.
        self.pipeline_type = pipeline_type
        # The scheduling configuration in JSON string format. Refer to the toJsonString method of the utility class com.alibaba.dataphin.pipeline.common.facade.openapi.model.OAScheduleConfig.
        # 
        # This parameter is required.
        self.schedule_config = schedule_config
        # The channel configuration in JSON string format. Refer to the toJsonString method of the utility class com.alibaba.dataphin.pipeline.common.facade.openapi.model.OAPipelineSetting.
        self.settings = settings
        # Specifies whether to submit the node. Default value: true.
        self.submit = submit

    def validate(self):
        if self.node_info:
            self.node_info.validate()
        if self.pipeline_config:
            self.pipeline_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.node_info is not None:
            result['NodeInfo'] = self.node_info.to_map()

        if self.pipeline_config is not None:
            result['PipelineConfig'] = self.pipeline_config.to_map()

        if self.pipeline_json is not None:
            result['PipelineJson'] = self.pipeline_json

        if self.pipeline_type is not None:
            result['PipelineType'] = self.pipeline_type

        if self.schedule_config is not None:
            result['ScheduleConfig'] = self.schedule_config

        if self.settings is not None:
            result['Settings'] = self.settings

        if self.submit is not None:
            result['Submit'] = self.submit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('NodeInfo') is not None:
            temp_model = main_models.UpdatePipelineByAsyncRequestUpdateCommandNodeInfo()
            self.node_info = temp_model.from_map(m.get('NodeInfo'))

        if m.get('PipelineConfig') is not None:
            temp_model = main_models.UpdatePipelineByAsyncRequestUpdateCommandPipelineConfig()
            self.pipeline_config = temp_model.from_map(m.get('PipelineConfig'))

        if m.get('PipelineJson') is not None:
            self.pipeline_json = m.get('PipelineJson')

        if m.get('PipelineType') is not None:
            self.pipeline_type = m.get('PipelineType')

        if m.get('ScheduleConfig') is not None:
            self.schedule_config = m.get('ScheduleConfig')

        if m.get('Settings') is not None:
            self.settings = m.get('Settings')

        if m.get('Submit') is not None:
            self.submit = m.get('Submit')

        return self

class UpdatePipelineByAsyncRequestUpdateCommandPipelineConfig(DaraModel):
    def __init__(
        self,
        hops: List[main_models.UpdatePipelineByAsyncRequestUpdateCommandPipelineConfigHops] = None,
        steps: List[main_models.UpdatePipelineByAsyncRequestUpdateCommandPipelineConfigSteps] = None,
    ):
        # The DAG (directed acyclic graph) link configurations that describe the connections between all components.
        # 
        # This parameter is required.
        self.hops = hops
        # The component configurations, including detailed configurations of all components used.
        # 
        # This parameter is required.
        self.steps = steps

    def validate(self):
        if self.hops:
            for v1 in self.hops:
                 if v1:
                    v1.validate()
        if self.steps:
            for v1 in self.steps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Hops'] = []
        if self.hops is not None:
            for k1 in self.hops:
                result['Hops'].append(k1.to_map() if k1 else None)

        result['Steps'] = []
        if self.steps is not None:
            for k1 in self.steps:
                result['Steps'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hops = []
        if m.get('Hops') is not None:
            for k1 in m.get('Hops'):
                temp_model = main_models.UpdatePipelineByAsyncRequestUpdateCommandPipelineConfigHops()
                self.hops.append(temp_model.from_map(k1))

        self.steps = []
        if m.get('Steps') is not None:
            for k1 in m.get('Steps'):
                temp_model = main_models.UpdatePipelineByAsyncRequestUpdateCommandPipelineConfigSteps()
                self.steps.append(temp_model.from_map(k1))

        return self

class UpdatePipelineByAsyncRequestUpdateCommandPipelineConfigSteps(DaraModel):
    def __init__(
        self,
        is_distribute: bool = None,
        key: str = None,
        plugin_config: str = None,
        step_name: str = None,
        step_type: str = None,
    ):
        # Specifies the data distribution method when the current component has multiple downstream components. Valid values:
        # 
        # - true: the data of the current component is distributed to all downstream components in a round-robin manner. For example, if the current component has 100 records and two downstream components, each downstream component receives 50 records. Default value: true.
        # - false: the full data of the current component is sent to all downstream components. For example, if the current component has 100 records and two downstream components, both downstream components receive 100 records.
        # 
        # This parameter is not applicable to workflow nodes.
        self.is_distribute = is_distribute
        # The plugin ID. Each plugin or operator has a unique identifier. Refer to the stepKey field of the utility class com.alibaba.dataphin.pipeline.common.facade.openapi.model.plugin.OABasePluginConfig. Developers should inherit the component or operator configuration class and implement the corresponding configuration. Each component or operator configuration has the same structure as the configuration created on the Dataphin console.
        # 
        # This parameter is required.
        self.key = key
        # The specific component configuration in JSON string format. Refer to the toJsonString method of the utility class com.alibaba.dataphin.pipeline.common.facade.openapi.model.plugin.OABasePluginConfig (or com.alibaba.dataphin.pipeline.common.facade.openapi.model.plugin.unstructured.BaseOAUnstructuredNeuronConfig for workflow operators) and its subclasses. Developers should inherit the component or operator configuration class and implement the corresponding configuration. Each component or operator configuration has the same structure as the node configuration created on the Dataphin console.
        # 
        # This parameter is required.
        self.plugin_config = plugin_config
        # The step name. Step names must be unique within the same pipeline node.
        # 
        # This parameter is required.
        self.step_name = step_name
        # The component type. Valid values:
        # 
        # - input: an input component.
        # - output: an output component.
        # - transfrom: a transform component.
        # - process: a flow control component.
        # 
        # For workflow nodes, this parameter specifies the operator type, such as image for images and text for text. Refer to the stepType field of the utility class com.alibaba.dataphin.pipeline.common.facade.openapi.model.plugin.OABasePluginConfig. Developers should inherit the component or operator configuration class and implement the corresponding configuration. Each component or operator configuration has the same structure as the configuration created on the Dataphin console.
        # 
        # This parameter is required.
        self.step_type = step_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_distribute is not None:
            result['IsDistribute'] = self.is_distribute

        if self.key is not None:
            result['Key'] = self.key

        if self.plugin_config is not None:
            result['PluginConfig'] = self.plugin_config

        if self.step_name is not None:
            result['StepName'] = self.step_name

        if self.step_type is not None:
            result['StepType'] = self.step_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDistribute') is not None:
            self.is_distribute = m.get('IsDistribute')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('PluginConfig') is not None:
            self.plugin_config = m.get('PluginConfig')

        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')

        if m.get('StepType') is not None:
            self.step_type = m.get('StepType')

        return self

class UpdatePipelineByAsyncRequestUpdateCommandPipelineConfigHops(DaraModel):
    def __init__(
        self,
        send_to: bool = None,
        source: str = None,
        target: str = None,
    ):
        # For conditional distribution components, set this parameter to true when the downstream condition is true, and to false otherwise. This parameter is not applicable to workflow nodes.
        self.send_to = send_to
        # The input step name, which corresponds to Steps[*].StepName.
        # 
        # This parameter is required.
        self.source = source
        # The output step name, which corresponds to Steps[*].StepName.
        # 
        # This parameter is required.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.send_to is not None:
            result['SendTo'] = self.send_to

        if self.source is not None:
            result['Source'] = self.source

        if self.target is not None:
            result['Target'] = self.target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SendTo') is not None:
            self.send_to = m.get('SendTo')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        return self

class UpdatePipelineByAsyncRequestUpdateCommandNodeInfo(DaraModel):
    def __init__(
        self,
        directory: str = None,
        file_id: int = None,
        node_id: str = None,
        node_name: str = None,
        pipeline_id: int = None,
    ):
        # The folder of the integration pipeline node. Default value: root folder. The folder must exist. If it does not exist, call the relevant API operation to create a folder of the offlinePipeline type.
        self.directory = directory
        # The pipeline file ID. Leave this parameter empty for initial creation. When updating a pipeline node, specify at least one of pipelineId, fileId, or nodeId.
        self.file_id = file_id
        # The scheduling node ID of the pipeline node. Leave this parameter empty for initial creation. When updating a pipeline node, specify at least one of pipelineId, fileId, or nodeId.
        self.node_id = node_id
        # The name of the integration pipeline node.
        # 
        # This parameter is required.
        self.node_name = node_name
        # The pipeline node ID. Leave this parameter empty for initial creation. When updating a pipeline node, specify at least one of pipelineId, fileId, or nodeId.
        self.pipeline_id = pipeline_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory is not None:
            result['Directory'] = self.directory

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Directory') is not None:
            self.directory = m.get('Directory')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        return self

class UpdatePipelineByAsyncRequestContext(DaraModel):
    def __init__(
        self,
        env: str = None,
        project_id: int = None,
    ):
        # The current operating environment. Valid values:
        # 
        # - DEV: the development environment.
        # - PROD: the production environment.
        # 
        # This parameter is required.
        self.env = env
        # The ID of the project to which the integration pipeline node belongs.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env is not None:
            result['Env'] = self.env

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

