# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any, Dict

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListEnvironmentKubeResourcesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.ListEnvironmentKubeResourcesResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. The status code 200 indicates that the request was successful. Other status codes indicate that the request failed.
        self.code = code
        # The returned struct.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`
        # *   `false`
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListEnvironmentKubeResourcesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListEnvironmentKubeResourcesResponseBodyData(DaraModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: main_models.ListEnvironmentKubeResourcesResponseBodyDataMetadata = None,
        spec: Any = None,
        status: Any = None,
    ):
        # The version number of the API.
        self.api_version = api_version
        # The resource type.
        self.kind = kind
        # The metadata.
        self.metadata = metadata
        # The resource specifications.
        self.spec = spec
        # The status of the resource.
        self.status = status

    def validate(self):
        if self.metadata:
            self.metadata.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_version is not None:
            result['ApiVersion'] = self.api_version

        if self.kind is not None:
            result['Kind'] = self.kind

        if self.metadata is not None:
            result['Metadata'] = self.metadata.to_map()

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiVersion') is not None:
            self.api_version = m.get('ApiVersion')

        if m.get('Kind') is not None:
            self.kind = m.get('Kind')

        if m.get('Metadata') is not None:
            temp_model = main_models.ListEnvironmentKubeResourcesResponseBodyDataMetadata()
            self.metadata = temp_model.from_map(m.get('Metadata'))

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListEnvironmentKubeResourcesResponseBodyDataMetadata(DaraModel):
    def __init__(
        self,
        annotations: Dict[str, str] = None,
        labels: Dict[str, str] = None,
        name: str = None,
        namespace: str = None,
    ):
        # The annotations.
        self.annotations = annotations
        # The tags.
        self.labels = labels
        # The resource name.
        self.name = name
        # The namespace.
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotations is not None:
            result['Annotations'] = self.annotations

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self

