# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class GetDatasetResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetDatasetResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            temp_model = main_models.GetDatasetResponseBodyData()
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

class GetDatasetResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        create_user: str = None,
        dataset_config: main_models.GetDatasetResponseBodyDataDatasetConfig = None,
        dataset_description: str = None,
        dataset_id: int = None,
        dataset_name: str = None,
        dataset_type: str = None,
        document_handle_config: main_models.GetDatasetResponseBodyDataDocumentHandleConfig = None,
        search_dataset_enable: int = None,
    ):
        self.create_time = create_time
        self.create_user = create_user
        self.dataset_config = dataset_config
        self.dataset_description = dataset_description
        self.dataset_id = dataset_id
        self.dataset_name = dataset_name
        self.dataset_type = dataset_type
        self.document_handle_config = document_handle_config
        self.search_dataset_enable = search_dataset_enable

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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.dataset_config is not None:
            result['DatasetConfig'] = self.dataset_config.to_map()

        if self.dataset_description is not None:
            result['DatasetDescription'] = self.dataset_description

        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.dataset_type is not None:
            result['DatasetType'] = self.dataset_type

        if self.document_handle_config is not None:
            result['DocumentHandleConfig'] = self.document_handle_config.to_map()

        if self.search_dataset_enable is not None:
            result['SearchDatasetEnable'] = self.search_dataset_enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('DatasetConfig') is not None:
            temp_model = main_models.GetDatasetResponseBodyDataDatasetConfig()
            self.dataset_config = temp_model.from_map(m.get('DatasetConfig'))

        if m.get('DatasetDescription') is not None:
            self.dataset_description = m.get('DatasetDescription')

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('DatasetType') is not None:
            self.dataset_type = m.get('DatasetType')

        if m.get('DocumentHandleConfig') is not None:
            temp_model = main_models.GetDatasetResponseBodyDataDocumentHandleConfig()
            self.document_handle_config = temp_model.from_map(m.get('DocumentHandleConfig'))

        if m.get('SearchDatasetEnable') is not None:
            self.search_dataset_enable = m.get('SearchDatasetEnable')

        return self

class GetDatasetResponseBodyDataDocumentHandleConfig(DaraModel):
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

class GetDatasetResponseBodyDataDatasetConfig(DaraModel):
    def __init__(
        self,
        search_source_configs: List[main_models.GetDatasetResponseBodyDataDatasetConfigSearchSourceConfigs] = None,
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
                temp_model = main_models.GetDatasetResponseBodyDataDatasetConfigSearchSourceConfigs()
                self.search_source_configs.append(temp_model.from_map(k1))

        return self

class GetDatasetResponseBodyDataDatasetConfigSearchSourceConfigs(DaraModel):
    def __init__(
        self,
        demo_query: str = None,
        search_source_request_config: main_models.GetDatasetResponseBodyDataDatasetConfigSearchSourceConfigsSearchSourceRequestConfig = None,
        search_source_response_config: main_models.GetDatasetResponseBodyDataDatasetConfigSearchSourceConfigsSearchSourceResponseConfig = None,
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
            temp_model = main_models.GetDatasetResponseBodyDataDatasetConfigSearchSourceConfigsSearchSourceRequestConfig()
            self.search_source_request_config = temp_model.from_map(m.get('SearchSourceRequestConfig'))

        if m.get('SearchSourceResponseConfig') is not None:
            temp_model = main_models.GetDatasetResponseBodyDataDatasetConfigSearchSourceConfigsSearchSourceResponseConfig()
            self.search_source_response_config = temp_model.from_map(m.get('SearchSourceResponseConfig'))

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

class GetDatasetResponseBodyDataDatasetConfigSearchSourceConfigsSearchSourceResponseConfig(DaraModel):
    def __init__(
        self,
        jq_nodes: List[main_models.GetDatasetResponseBodyDataDatasetConfigSearchSourceConfigsSearchSourceResponseConfigJqNodes] = None,
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
                temp_model = main_models.GetDatasetResponseBodyDataDatasetConfigSearchSourceConfigsSearchSourceResponseConfigJqNodes()
                self.jq_nodes.append(temp_model.from_map(k1))

        return self

class GetDatasetResponseBodyDataDatasetConfigSearchSourceConfigsSearchSourceResponseConfigJqNodes(DaraModel):
    def __init__(
        self,
        jq_nodes: List[main_models.GetDatasetResponseBodyDataDatasetConfigSearchSourceConfigsSearchSourceResponseConfigJqNodesJqNodes] = None,
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
                temp_model = main_models.GetDatasetResponseBodyDataDatasetConfigSearchSourceConfigsSearchSourceResponseConfigJqNodesJqNodes()
                self.jq_nodes.append(temp_model.from_map(k1))

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetDatasetResponseBodyDataDatasetConfigSearchSourceConfigsSearchSourceResponseConfigJqNodesJqNodes(DaraModel):
    def __init__(
        self,
        jq_nodes: List[main_models.GetDatasetResponseBodyDataDatasetConfigSearchSourceConfigsSearchSourceResponseConfigJqNodesJqNodesJqNodes] = None,
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
                temp_model = main_models.GetDatasetResponseBodyDataDatasetConfigSearchSourceConfigsSearchSourceResponseConfigJqNodesJqNodesJqNodes()
                self.jq_nodes.append(temp_model.from_map(k1))

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetDatasetResponseBodyDataDatasetConfigSearchSourceConfigsSearchSourceResponseConfigJqNodesJqNodesJqNodes(DaraModel):
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

class GetDatasetResponseBodyDataDatasetConfigSearchSourceConfigsSearchSourceRequestConfig(DaraModel):
    def __init__(
        self,
        body: str = None,
        connect_timeout: int = None,
        headers: List[main_models.GetDatasetResponseBodyDataDatasetConfigSearchSourceConfigsSearchSourceRequestConfigHeaders] = None,
        method: str = None,
        params: List[main_models.GetDatasetResponseBodyDataDatasetConfigSearchSourceConfigsSearchSourceRequestConfigParams] = None,
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
                temp_model = main_models.GetDatasetResponseBodyDataDatasetConfigSearchSourceConfigsSearchSourceRequestConfigHeaders()
                self.headers.append(temp_model.from_map(k1))

        if m.get('Method') is not None:
            self.method = m.get('Method')

        self.params = []
        if m.get('Params') is not None:
            for k1 in m.get('Params'):
                temp_model = main_models.GetDatasetResponseBodyDataDatasetConfigSearchSourceConfigsSearchSourceRequestConfigParams()
                self.params.append(temp_model.from_map(k1))

        if m.get('PathParamsEnable') is not None:
            self.path_params_enable = m.get('PathParamsEnable')

        if m.get('SocketTimeout') is not None:
            self.socket_timeout = m.get('SocketTimeout')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class GetDatasetResponseBodyDataDatasetConfigSearchSourceConfigsSearchSourceRequestConfigParams(DaraModel):
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

class GetDatasetResponseBodyDataDatasetConfigSearchSourceConfigsSearchSourceRequestConfigHeaders(DaraModel):
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

