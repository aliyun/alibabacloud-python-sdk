# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class GetNacosMcpServerResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetNacosMcpServerResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetNacosMcpServerResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetNacosMcpServerResponseBodyData(DaraModel):
    def __init__(
        self,
        all_versions: List[main_models.GetNacosMcpServerResponseBodyDataAllVersions] = None,
        backend_endpoints: List[main_models.GetNacosMcpServerResponseBodyDataBackendEndpoints] = None,
        capabilities: List[str] = None,
        description: str = None,
        enabled: bool = None,
        front_protocol: str = None,
        id: str = None,
        local_server_config: Dict[str, Any] = None,
        name: str = None,
        protocol: str = None,
        remote_server_config: main_models.GetNacosMcpServerResponseBodyDataRemoteServerConfig = None,
        tool_spec: main_models.GetNacosMcpServerResponseBodyDataToolSpec = None,
        version_detail: main_models.GetNacosMcpServerResponseBodyDataVersionDetail = None,
        yaml_config: str = None,
    ):
        self.all_versions = all_versions
        self.backend_endpoints = backend_endpoints
        self.capabilities = capabilities
        self.description = description
        self.enabled = enabled
        self.front_protocol = front_protocol
        # ID。
        self.id = id
        self.local_server_config = local_server_config
        self.name = name
        self.protocol = protocol
        self.remote_server_config = remote_server_config
        self.tool_spec = tool_spec
        self.version_detail = version_detail
        self.yaml_config = yaml_config

    def validate(self):
        if self.all_versions:
            for v1 in self.all_versions:
                 if v1:
                    v1.validate()
        if self.backend_endpoints:
            for v1 in self.backend_endpoints:
                 if v1:
                    v1.validate()
        if self.remote_server_config:
            self.remote_server_config.validate()
        if self.tool_spec:
            self.tool_spec.validate()
        if self.version_detail:
            self.version_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AllVersions'] = []
        if self.all_versions is not None:
            for k1 in self.all_versions:
                result['AllVersions'].append(k1.to_map() if k1 else None)

        result['BackendEndpoints'] = []
        if self.backend_endpoints is not None:
            for k1 in self.backend_endpoints:
                result['BackendEndpoints'].append(k1.to_map() if k1 else None)

        if self.capabilities is not None:
            result['Capabilities'] = self.capabilities

        if self.description is not None:
            result['Description'] = self.description

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.front_protocol is not None:
            result['FrontProtocol'] = self.front_protocol

        if self.id is not None:
            result['Id'] = self.id

        if self.local_server_config is not None:
            result['LocalServerConfig'] = self.local_server_config

        if self.name is not None:
            result['Name'] = self.name

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.remote_server_config is not None:
            result['RemoteServerConfig'] = self.remote_server_config.to_map()

        if self.tool_spec is not None:
            result['ToolSpec'] = self.tool_spec.to_map()

        if self.version_detail is not None:
            result['VersionDetail'] = self.version_detail.to_map()

        if self.yaml_config is not None:
            result['YamlConfig'] = self.yaml_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.all_versions = []
        if m.get('AllVersions') is not None:
            for k1 in m.get('AllVersions'):
                temp_model = main_models.GetNacosMcpServerResponseBodyDataAllVersions()
                self.all_versions.append(temp_model.from_map(k1))

        self.backend_endpoints = []
        if m.get('BackendEndpoints') is not None:
            for k1 in m.get('BackendEndpoints'):
                temp_model = main_models.GetNacosMcpServerResponseBodyDataBackendEndpoints()
                self.backend_endpoints.append(temp_model.from_map(k1))

        if m.get('Capabilities') is not None:
            self.capabilities = m.get('Capabilities')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('FrontProtocol') is not None:
            self.front_protocol = m.get('FrontProtocol')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LocalServerConfig') is not None:
            self.local_server_config = m.get('LocalServerConfig')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RemoteServerConfig') is not None:
            temp_model = main_models.GetNacosMcpServerResponseBodyDataRemoteServerConfig()
            self.remote_server_config = temp_model.from_map(m.get('RemoteServerConfig'))

        if m.get('ToolSpec') is not None:
            temp_model = main_models.GetNacosMcpServerResponseBodyDataToolSpec()
            self.tool_spec = temp_model.from_map(m.get('ToolSpec'))

        if m.get('VersionDetail') is not None:
            temp_model = main_models.GetNacosMcpServerResponseBodyDataVersionDetail()
            self.version_detail = temp_model.from_map(m.get('VersionDetail'))

        if m.get('YamlConfig') is not None:
            self.yaml_config = m.get('YamlConfig')

        return self

class GetNacosMcpServerResponseBodyDataVersionDetail(DaraModel):
    def __init__(
        self,
        is_latest: bool = None,
        release_date: str = None,
        version: str = None,
    ):
        self.is_latest = is_latest
        self.release_date = release_date
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_latest is not None:
            result['IsLatest'] = self.is_latest

        if self.release_date is not None:
            result['ReleaseDate'] = self.release_date

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsLatest') is not None:
            self.is_latest = m.get('IsLatest')

        if m.get('ReleaseDate') is not None:
            self.release_date = m.get('ReleaseDate')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetNacosMcpServerResponseBodyDataToolSpec(DaraModel):
    def __init__(
        self,
        security_schemes: Any = None,
        specification_type: str = None,
        tool_decrypt_status: str = None,
        tools: List[main_models.GetNacosMcpServerResponseBodyDataToolSpecTools] = None,
        tools_meta: Dict[str, main_models.DataToolSpecToolsMetaValue] = None,
    ):
        self.security_schemes = security_schemes
        self.specification_type = specification_type
        self.tool_decrypt_status = tool_decrypt_status
        self.tools = tools
        self.tools_meta = tools_meta

    def validate(self):
        if self.tools:
            for v1 in self.tools:
                 if v1:
                    v1.validate()
        if self.tools_meta:
            for v1 in self.tools_meta.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_schemes is not None:
            result['SecuritySchemes'] = self.security_schemes

        if self.specification_type is not None:
            result['SpecificationType'] = self.specification_type

        if self.tool_decrypt_status is not None:
            result['ToolDecryptStatus'] = self.tool_decrypt_status

        result['Tools'] = []
        if self.tools is not None:
            for k1 in self.tools:
                result['Tools'].append(k1.to_map() if k1 else None)

        result['ToolsMeta'] = {}
        if self.tools_meta is not None:
            for k1, v1 in self.tools_meta.items():
                result['ToolsMeta'][k1] = v1.to_map() if v1 else None

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecuritySchemes') is not None:
            self.security_schemes = m.get('SecuritySchemes')

        if m.get('SpecificationType') is not None:
            self.specification_type = m.get('SpecificationType')

        if m.get('ToolDecryptStatus') is not None:
            self.tool_decrypt_status = m.get('ToolDecryptStatus')

        self.tools = []
        if m.get('Tools') is not None:
            for k1 in m.get('Tools'):
                temp_model = main_models.GetNacosMcpServerResponseBodyDataToolSpecTools()
                self.tools.append(temp_model.from_map(k1))

        self.tools_meta = {}
        if m.get('ToolsMeta') is not None:
            for k1, v1 in m.get('ToolsMeta').items():
                temp_model = main_models.DataToolSpecToolsMetaValue()
                self.tools_meta[k1] = temp_model.from_map(v1)

        return self

class GetNacosMcpServerResponseBodyDataToolSpecTools(DaraModel):
    def __init__(
        self,
        description: str = None,
        input_schema: Dict[str, Any] = None,
        name: str = None,
    ):
        self.description = description
        self.input_schema = input_schema
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.input_schema is not None:
            result['InputSchema'] = self.input_schema

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InputSchema') is not None:
            self.input_schema = m.get('InputSchema')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetNacosMcpServerResponseBodyDataRemoteServerConfig(DaraModel):
    def __init__(
        self,
        export_path: str = None,
        service_ref: main_models.GetNacosMcpServerResponseBodyDataRemoteServerConfigServiceRef = None,
    ):
        self.export_path = export_path
        self.service_ref = service_ref

    def validate(self):
        if self.service_ref:
            self.service_ref.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.export_path is not None:
            result['ExportPath'] = self.export_path

        if self.service_ref is not None:
            result['ServiceRef'] = self.service_ref.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportPath') is not None:
            self.export_path = m.get('ExportPath')

        if m.get('ServiceRef') is not None:
            temp_model = main_models.GetNacosMcpServerResponseBodyDataRemoteServerConfigServiceRef()
            self.service_ref = temp_model.from_map(m.get('ServiceRef'))

        return self

class GetNacosMcpServerResponseBodyDataRemoteServerConfigServiceRef(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        namespace_id: str = None,
        service_name: str = None,
    ):
        self.group_name = group_name
        self.namespace_id = namespace_id
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

class GetNacosMcpServerResponseBodyDataBackendEndpoints(DaraModel):
    def __init__(
        self,
        address: str = None,
        path: str = None,
        port: int = None,
    ):
        self.address = address
        self.path = path
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.path is not None:
            result['Path'] = self.path

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

class GetNacosMcpServerResponseBodyDataAllVersions(DaraModel):
    def __init__(
        self,
        is_latest: bool = None,
        release_date: str = None,
        version: str = None,
    ):
        self.is_latest = is_latest
        self.release_date = release_date
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_latest is not None:
            result['Is_latest'] = self.is_latest

        if self.release_date is not None:
            result['Release_date'] = self.release_date

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Is_latest') is not None:
            self.is_latest = m.get('Is_latest')

        if m.get('Release_date') is not None:
            self.release_date = m.get('Release_date')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

