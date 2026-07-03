# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ServiceInfo(DaraModel):
    def __init__(
        self,
        express_type: str = None,
        group_name: str = None,
        name: str = None,
        namespace: str = None,
        pai_workspace_id: str = None,
        pai_workspace_name: str = None,
        ports: List[main_models.ServiceInfoPorts] = None,
        qualifier: str = None,
        service_id: str = None,
        source_type: str = None,
        status: str = None,
        versions: List[main_models.ServiceInfoVersions] = None,
    ):
        self.express_type = express_type
        self.group_name = group_name
        self.name = name
        self.namespace = namespace
        self.pai_workspace_id = pai_workspace_id
        self.pai_workspace_name = pai_workspace_name
        self.ports = ports
        self.qualifier = qualifier
        self.service_id = service_id
        self.source_type = source_type
        self.status = status
        self.versions = versions

    def validate(self):
        if self.ports:
            for v1 in self.ports:
                 if v1:
                    v1.validate()
        if self.versions:
            for v1 in self.versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.express_type is not None:
            result['expressType'] = self.express_type

        if self.group_name is not None:
            result['groupName'] = self.group_name

        if self.name is not None:
            result['name'] = self.name

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.pai_workspace_id is not None:
            result['paiWorkspaceId'] = self.pai_workspace_id

        if self.pai_workspace_name is not None:
            result['paiWorkspaceName'] = self.pai_workspace_name

        result['ports'] = []
        if self.ports is not None:
            for k1 in self.ports:
                result['ports'].append(k1.to_map() if k1 else None)

        if self.qualifier is not None:
            result['qualifier'] = self.qualifier

        if self.service_id is not None:
            result['serviceId'] = self.service_id

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.status is not None:
            result['status'] = self.status

        result['versions'] = []
        if self.versions is not None:
            for k1 in self.versions:
                result['versions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expressType') is not None:
            self.express_type = m.get('expressType')

        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('paiWorkspaceId') is not None:
            self.pai_workspace_id = m.get('paiWorkspaceId')

        if m.get('paiWorkspaceName') is not None:
            self.pai_workspace_name = m.get('paiWorkspaceName')

        self.ports = []
        if m.get('ports') is not None:
            for k1 in m.get('ports'):
                temp_model = main_models.ServiceInfoPorts()
                self.ports.append(temp_model.from_map(k1))

        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')

        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('status') is not None:
            self.status = m.get('status')

        self.versions = []
        if m.get('versions') is not None:
            for k1 in m.get('versions'):
                temp_model = main_models.ServiceInfoVersions()
                self.versions.append(temp_model.from_map(k1))

        return self

class ServiceInfoVersions(DaraModel):
    def __init__(
        self,
        labels: List[main_models.ServiceInfoVersionsLabels] = None,
        name: str = None,
    ):
        self.labels = labels
        self.name = name

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['labels'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.labels = []
        if m.get('labels') is not None:
            for k1 in m.get('labels'):
                temp_model = main_models.ServiceInfoVersionsLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class ServiceInfoVersionsLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class ServiceInfoPorts(DaraModel):
    def __init__(
        self,
        name: str = None,
        port: int = None,
        protocol: str = None,
    ):
        self.name = name
        self.port = port
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.port is not None:
            result['port'] = self.port

        if self.protocol is not None:
            result['protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        return self

