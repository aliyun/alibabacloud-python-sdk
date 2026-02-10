# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListImageRegistryExtraResponseBody(DaraModel):
    def __init__(
        self,
        image_registry_extra_infos: List[main_models.ListImageRegistryExtraResponseBodyImageRegistryExtraInfos] = None,
        request_id: str = None,
    ):
        # The additional configuration information about the image repository.
        self.image_registry_extra_infos = image_registry_extra_infos
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.image_registry_extra_infos:
            for v1 in self.image_registry_extra_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImageRegistryExtraInfos'] = []
        if self.image_registry_extra_infos is not None:
            for k1 in self.image_registry_extra_infos:
                result['ImageRegistryExtraInfos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_registry_extra_infos = []
        if m.get('ImageRegistryExtraInfos') is not None:
            for k1 in m.get('ImageRegistryExtraInfos'):
                temp_model = main_models.ListImageRegistryExtraResponseBodyImageRegistryExtraInfos()
                self.image_registry_extra_infos.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListImageRegistryExtraResponseBodyImageRegistryExtraInfos(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        auth_token: str = None,
        id: int = None,
        namespace: str = None,
        registry_id: int = None,
        registry_type: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The authorization token.
        self.auth_token = auth_token
        # The configuration ID.
        self.id = id
        # The namespace of the image.
        self.namespace = namespace
        # The ID of the image repository.
        self.registry_id = registry_id
        # The type of the image repository. Valid values:
        # 
        # *   **acr**: Container Registry.
        # *   **harbor**: Harbor.
        # *   **quay**: Quay.
        # *   **CI/CD**: Jenkins.
        self.registry_type = registry_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.auth_token is not None:
            result['AuthToken'] = self.auth_token

        if self.id is not None:
            result['Id'] = self.id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.registry_id is not None:
            result['RegistryId'] = self.registry_id

        if self.registry_type is not None:
            result['RegistryType'] = self.registry_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('AuthToken') is not None:
            self.auth_token = m.get('AuthToken')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('RegistryId') is not None:
            self.registry_id = m.get('RegistryId')

        if m.get('RegistryType') is not None:
            self.registry_type = m.get('RegistryType')

        return self

