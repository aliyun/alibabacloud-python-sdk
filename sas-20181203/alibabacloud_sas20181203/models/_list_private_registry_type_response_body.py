# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListPrivateRegistryTypeResponseBody(DaraModel):
    def __init__(
        self,
        registry_type_infos: List[main_models.ListPrivateRegistryTypeResponseBodyRegistryTypeInfos] = None,
        request_id: str = None,
    ):
        # An array that consists of image repository types.
        self.registry_type_infos = registry_type_infos
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.registry_type_infos:
            for v1 in self.registry_type_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RegistryTypeInfos'] = []
        if self.registry_type_infos is not None:
            for k1 in self.registry_type_infos:
                result['RegistryTypeInfos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.registry_type_infos = []
        if m.get('RegistryTypeInfos') is not None:
            for k1 in m.get('RegistryTypeInfos'):
                temp_model = main_models.ListPrivateRegistryTypeResponseBodyRegistryTypeInfos()
                self.registry_type_infos.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPrivateRegistryTypeResponseBodyRegistryTypeInfos(DaraModel):
    def __init__(
        self,
        count: int = None,
        registry_type: str = None,
    ):
        # The number of image repositories.
        self.count = count
        # The name of the image repository type. Valid values:
        # 
        # *   **acr**: Container Registry
        # *   **harbor**: Harbor
        # *   **quay**: Quay
        # *   **CI/CD**: Jenkins
        self.registry_type = registry_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.registry_type is not None:
            result['RegistryType'] = self.registry_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('RegistryType') is not None:
            self.registry_type = m.get('RegistryType')

        return self

