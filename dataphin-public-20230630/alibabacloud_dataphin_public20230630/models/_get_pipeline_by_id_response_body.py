# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetPipelineByIdResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetPipelineByIdResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetPipelineByIdResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetPipelineByIdResponseBodyData(DaraModel):
    def __init__(
        self,
        mode: str = None,
        node_info: main_models.GetPipelineByIdResponseBodyDataNodeInfo = None,
        pipeline_config: main_models.GetPipelineByIdResponseBodyDataPipelineConfig = None,
        pipeline_json: str = None,
        pipeline_type: int = None,
        schedule_config: str = None,
        settings: str = None,
    ):
        self.mode = mode
        self.node_info = node_info
        self.pipeline_config = pipeline_config
        self.pipeline_json = pipeline_json
        self.pipeline_type = pipeline_type
        self.schedule_config = schedule_config
        self.settings = settings

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('NodeInfo') is not None:
            temp_model = main_models.GetPipelineByIdResponseBodyDataNodeInfo()
            self.node_info = temp_model.from_map(m.get('NodeInfo'))

        if m.get('PipelineConfig') is not None:
            temp_model = main_models.GetPipelineByIdResponseBodyDataPipelineConfig()
            self.pipeline_config = temp_model.from_map(m.get('PipelineConfig'))

        if m.get('PipelineJson') is not None:
            self.pipeline_json = m.get('PipelineJson')

        if m.get('PipelineType') is not None:
            self.pipeline_type = m.get('PipelineType')

        if m.get('ScheduleConfig') is not None:
            self.schedule_config = m.get('ScheduleConfig')

        if m.get('Settings') is not None:
            self.settings = m.get('Settings')

        return self

class GetPipelineByIdResponseBodyDataPipelineConfig(DaraModel):
    def __init__(
        self,
        hops: List[main_models.GetPipelineByIdResponseBodyDataPipelineConfigHops] = None,
        steps: List[main_models.GetPipelineByIdResponseBodyDataPipelineConfigSteps] = None,
    ):
        self.hops = hops
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
                temp_model = main_models.GetPipelineByIdResponseBodyDataPipelineConfigHops()
                self.hops.append(temp_model.from_map(k1))

        self.steps = []
        if m.get('Steps') is not None:
            for k1 in m.get('Steps'):
                temp_model = main_models.GetPipelineByIdResponseBodyDataPipelineConfigSteps()
                self.steps.append(temp_model.from_map(k1))

        return self

class GetPipelineByIdResponseBodyDataPipelineConfigSteps(DaraModel):
    def __init__(
        self,
        is_distribute: bool = None,
        key: str = None,
        plugin_config: str = None,
        step_name: str = None,
        step_type: str = None,
    ):
        self.is_distribute = is_distribute
        self.key = key
        self.plugin_config = plugin_config
        self.step_name = step_name
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

class GetPipelineByIdResponseBodyDataPipelineConfigHops(DaraModel):
    def __init__(
        self,
        send_to: bool = None,
        source: str = None,
        target: str = None,
    ):
        self.send_to = send_to
        self.source = source
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

class GetPipelineByIdResponseBodyDataNodeInfo(DaraModel):
    def __init__(
        self,
        desc: str = None,
        directory: str = None,
        file_id: int = None,
        node_id: str = None,
        node_name: str = None,
        pipeline_id: int = None,
    ):
        self.desc = desc
        self.directory = directory
        self.file_id = file_id
        self.node_id = node_id
        self.node_name = node_name
        self.pipeline_id = pipeline_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['Desc'] = self.desc

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
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

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

