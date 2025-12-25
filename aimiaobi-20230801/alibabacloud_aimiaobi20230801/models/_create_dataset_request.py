# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class CreateDatasetRequest(DaraModel):
    def __init__(
        self,
        dataset_config: main_models.CreateDatasetRequestDatasetConfig = None,
        dataset_description: str = None,
        dataset_name: str = None,
        dataset_type: str = None,
        document_handle_config: main_models.CreateDatasetRequestDocumentHandleConfig = None,
        invoke_type: str = None,
        search_dataset_enable: int = None,
        workspace_id: str = None,
    ):
        self.dataset_config = dataset_config
        self.dataset_description = dataset_description
        # This parameter is required.
        self.dataset_name = dataset_name
        self.dataset_type = dataset_type
        self.document_handle_config = document_handle_config
        self.invoke_type = invoke_type
        self.search_dataset_enable = search_dataset_enable
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.dataset_config:
            self.dataset_config.validate()
        if self.document_handle_config:
            self.document_handle_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_config is not None:
            result['DatasetConfig'] = self.dataset_config.to_map()

        if self.dataset_description is not None:
            result['DatasetDescription'] = self.dataset_description

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.dataset_type is not None:
            result['DatasetType'] = self.dataset_type

        if self.document_handle_config is not None:
            result['DocumentHandleConfig'] = self.document_handle_config.to_map()

        if self.invoke_type is not None:
            result['InvokeType'] = self.invoke_type

        if self.search_dataset_enable is not None:
            result['SearchDatasetEnable'] = self.search_dataset_enable

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetConfig') is not None:
            temp_model = main_models.CreateDatasetRequestDatasetConfig()
            self.dataset_config = temp_model.from_map(m.get('DatasetConfig'))

        if m.get('DatasetDescription') is not None:
            self.dataset_description = m.get('DatasetDescription')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('DatasetType') is not None:
            self.dataset_type = m.get('DatasetType')

        if m.get('DocumentHandleConfig') is not None:
            temp_model = main_models.CreateDatasetRequestDocumentHandleConfig()
            self.document_handle_config = temp_model.from_map(m.get('DocumentHandleConfig'))

        if m.get('InvokeType') is not None:
            self.invoke_type = m.get('InvokeType')

        if m.get('SearchDatasetEnable') is not None:
            self.search_dataset_enable = m.get('SearchDatasetEnable')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class CreateDatasetRequestDocumentHandleConfig(DaraModel):
    def __init__(
        self,
        disable_handle_multimodal_media: bool = None,
    ):
        self.disable_handle_multimodal_media = disable_handle_multimodal_media

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disable_handle_multimodal_media is not None:
            result['DisableHandleMultimodalMedia'] = self.disable_handle_multimodal_media

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisableHandleMultimodalMedia') is not None:
            self.disable_handle_multimodal_media = m.get('DisableHandleMultimodalMedia')

        return self

class CreateDatasetRequestDatasetConfig(DaraModel):
    def __init__(
        self,
        search_source_configs: List[main_models.CreateDatasetRequestDatasetConfigSearchSourceConfigs] = None,
    ):
        self.search_source_configs = search_source_configs

    def validate(self):
        if self.search_source_configs:
            for v1 in self.search_source_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SearchSourceConfigs'] = []
        if self.search_source_configs is not None:
            for k1 in self.search_source_configs:
                result['SearchSourceConfigs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.search_source_configs = []
        if m.get('SearchSourceConfigs') is not None:
            for k1 in m.get('SearchSourceConfigs'):
                temp_model = main_models.CreateDatasetRequestDatasetConfigSearchSourceConfigs()
                self.search_source_configs.append(temp_model.from_map(k1))

        return self

class CreateDatasetRequestDatasetConfigSearchSourceConfigs(DaraModel):
    def __init__(
        self,
        demo_query: str = None,
        search_source_request_config: main_models.CreateDatasetRequestDatasetConfigSearchSourceConfigsSearchSourceRequestConfig = None,
        search_source_response_config: main_models.CreateDatasetRequestDatasetConfigSearchSourceConfigsSearchSourceResponseConfig = None,
        size: int = None,
    ):
        self.demo_query = demo_query
        self.search_source_request_config = search_source_request_config
        self.search_source_response_config = search_source_response_config
        self.size = size

    def validate(self):
        if self.search_source_request_config:
            self.search_source_request_config.validate()
        if self.search_source_response_config:
            self.search_source_response_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.demo_query is not None:
            result['DemoQuery'] = self.demo_query

        if self.search_source_request_config is not None:
            result['SearchSourceRequestConfig'] = self.search_source_request_config.to_map()

        if self.search_source_response_config is not None:
            result['SearchSourceResponseConfig'] = self.search_source_response_config.to_map()

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DemoQuery') is not None:
            self.demo_query = m.get('DemoQuery')

        if m.get('SearchSourceRequestConfig') is not None:
            temp_model = main_models.CreateDatasetRequestDatasetConfigSearchSourceConfigsSearchSourceRequestConfig()
            self.search_source_request_config = temp_model.from_map(m.get('SearchSourceRequestConfig'))

        if m.get('SearchSourceResponseConfig') is not None:
            temp_model = main_models.CreateDatasetRequestDatasetConfigSearchSourceConfigsSearchSourceResponseConfig()
            self.search_source_response_config = temp_model.from_map(m.get('SearchSourceResponseConfig'))

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

class CreateDatasetRequestDatasetConfigSearchSourceConfigsSearchSourceResponseConfig(DaraModel):
    def __init__(
        self,
        jq_nodes: List[main_models.CreateDatasetRequestDatasetConfigSearchSourceConfigsSearchSourceResponseConfigJqNodes] = None,
    ):
        self.jq_nodes = jq_nodes

    def validate(self):
        if self.jq_nodes:
            for v1 in self.jq_nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['JqNodes'] = []
        if self.jq_nodes is not None:
            for k1 in self.jq_nodes:
                result['JqNodes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.jq_nodes = []
        if m.get('JqNodes') is not None:
            for k1 in m.get('JqNodes'):
                temp_model = main_models.CreateDatasetRequestDatasetConfigSearchSourceConfigsSearchSourceResponseConfigJqNodes()
                self.jq_nodes.append(temp_model.from_map(k1))

        return self

class CreateDatasetRequestDatasetConfigSearchSourceConfigsSearchSourceResponseConfigJqNodes(DaraModel):
    def __init__(
        self,
        jq_nodes: List[main_models.CreateDatasetRequestDatasetConfigSearchSourceConfigsSearchSourceResponseConfigJqNodesJqNodes] = None,
        key: str = None,
        path: str = None,
        type: str = None,
    ):
        self.jq_nodes = jq_nodes
        self.key = key
        self.path = path
        self.type = type

    def validate(self):
        if self.jq_nodes:
            for v1 in self.jq_nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['JqNodes'] = []
        if self.jq_nodes is not None:
            for k1 in self.jq_nodes:
                result['JqNodes'].append(k1.to_map() if k1 else None)

        if self.key is not None:
            result['Key'] = self.key

        if self.path is not None:
            result['Path'] = self.path

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.jq_nodes = []
        if m.get('JqNodes') is not None:
            for k1 in m.get('JqNodes'):
                temp_model = main_models.CreateDatasetRequestDatasetConfigSearchSourceConfigsSearchSourceResponseConfigJqNodesJqNodes()
                self.jq_nodes.append(temp_model.from_map(k1))

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateDatasetRequestDatasetConfigSearchSourceConfigsSearchSourceResponseConfigJqNodesJqNodes(DaraModel):
    def __init__(
        self,
        jq_nodes: List[main_models.CreateDatasetRequestDatasetConfigSearchSourceConfigsSearchSourceResponseConfigJqNodesJqNodesJqNodes] = None,
        key: str = None,
        path: str = None,
        type: str = None,
    ):
        self.jq_nodes = jq_nodes
        self.key = key
        self.path = path
        self.type = type

    def validate(self):
        if self.jq_nodes:
            for v1 in self.jq_nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['JqNodes'] = []
        if self.jq_nodes is not None:
            for k1 in self.jq_nodes:
                result['JqNodes'].append(k1.to_map() if k1 else None)

        if self.key is not None:
            result['Key'] = self.key

        if self.path is not None:
            result['Path'] = self.path

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.jq_nodes = []
        if m.get('JqNodes') is not None:
            for k1 in m.get('JqNodes'):
                temp_model = main_models.CreateDatasetRequestDatasetConfigSearchSourceConfigsSearchSourceResponseConfigJqNodesJqNodesJqNodes()
                self.jq_nodes.append(temp_model.from_map(k1))

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateDatasetRequestDatasetConfigSearchSourceConfigsSearchSourceResponseConfigJqNodesJqNodesJqNodes(DaraModel):
    def __init__(
        self,
        key: str = None,
        path: str = None,
        type: str = None,
    ):
        self.key = key
        self.path = path
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.path is not None:
            result['Path'] = self.path

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateDatasetRequestDatasetConfigSearchSourceConfigsSearchSourceRequestConfig(DaraModel):
    def __init__(
        self,
        body: str = None,
        connect_timeout: int = None,
        headers: List[main_models.CreateDatasetRequestDatasetConfigSearchSourceConfigsSearchSourceRequestConfigHeaders] = None,
        method: str = None,
        params: List[main_models.CreateDatasetRequestDatasetConfigSearchSourceConfigsSearchSourceRequestConfigParams] = None,
        path_params_enable: bool = None,
        socket_timeout: int = None,
        url: str = None,
    ):
        self.body = body
        self.connect_timeout = connect_timeout
        self.headers = headers
        self.method = method
        self.params = params
        self.path_params_enable = path_params_enable
        self.socket_timeout = socket_timeout
        self.url = url

    def validate(self):
        if self.headers:
            for v1 in self.headers:
                 if v1:
                    v1.validate()
        if self.params:
            for v1 in self.params:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['Body'] = self.body

        if self.connect_timeout is not None:
            result['ConnectTimeout'] = self.connect_timeout

        result['Headers'] = []
        if self.headers is not None:
            for k1 in self.headers:
                result['Headers'].append(k1.to_map() if k1 else None)

        if self.method is not None:
            result['Method'] = self.method

        result['Params'] = []
        if self.params is not None:
            for k1 in self.params:
                result['Params'].append(k1.to_map() if k1 else None)

        if self.path_params_enable is not None:
            result['PathParamsEnable'] = self.path_params_enable

        if self.socket_timeout is not None:
            result['SocketTimeout'] = self.socket_timeout

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')

        if m.get('ConnectTimeout') is not None:
            self.connect_timeout = m.get('ConnectTimeout')

        self.headers = []
        if m.get('Headers') is not None:
            for k1 in m.get('Headers'):
                temp_model = main_models.CreateDatasetRequestDatasetConfigSearchSourceConfigsSearchSourceRequestConfigHeaders()
                self.headers.append(temp_model.from_map(k1))

        if m.get('Method') is not None:
            self.method = m.get('Method')

        self.params = []
        if m.get('Params') is not None:
            for k1 in m.get('Params'):
                temp_model = main_models.CreateDatasetRequestDatasetConfigSearchSourceConfigsSearchSourceRequestConfigParams()
                self.params.append(temp_model.from_map(k1))

        if m.get('PathParamsEnable') is not None:
            self.path_params_enable = m.get('PathParamsEnable')

        if m.get('SocketTimeout') is not None:
            self.socket_timeout = m.get('SocketTimeout')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class CreateDatasetRequestDatasetConfigSearchSourceConfigsSearchSourceRequestConfigParams(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
        value_format: str = None,
        value_type: str = None,
    ):
        self.name = name
        self.value = value
        self.value_format = value_format
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        if self.value_format is not None:
            result['ValueFormat'] = self.value_format

        if self.value_type is not None:
            result['ValueType'] = self.value_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('ValueFormat') is not None:
            self.value_format = m.get('ValueFormat')

        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')

        return self

class CreateDatasetRequestDatasetConfigSearchSourceConfigsSearchSourceRequestConfigHeaders(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
        value_format: str = None,
        value_type: str = None,
    ):
        self.name = name
        self.value = value
        self.value_format = value_format
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        if self.value_format is not None:
            result['ValueFormat'] = self.value_format

        if self.value_type is not None:
            result['ValueType'] = self.value_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('ValueFormat') is not None:
            self.value_format = m.get('ValueFormat')

        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')

        return self

