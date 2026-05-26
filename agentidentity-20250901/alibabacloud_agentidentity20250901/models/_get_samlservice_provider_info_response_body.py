# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class GetSAMLServiceProviderInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        samlservice_provider_info: main_models.GetSAMLServiceProviderInfoResponseBodySAMLServiceProviderInfo = None,
    ):
        self.request_id = request_id
        self.samlservice_provider_info = samlservice_provider_info

    def validate(self):
        if self.samlservice_provider_info:
            self.samlservice_provider_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.samlservice_provider_info is not None:
            result['SAMLServiceProviderInfo'] = self.samlservice_provider_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SAMLServiceProviderInfo') is not None:
            temp_model = main_models.GetSAMLServiceProviderInfoResponseBodySAMLServiceProviderInfo()
            self.samlservice_provider_info = temp_model.from_map(m.get('SAMLServiceProviderInfo'))

        return self

class GetSAMLServiceProviderInfoResponseBodySAMLServiceProviderInfo(DaraModel):
    def __init__(
        self,
        acsurl: str = None,
        entity_id: str = None,
        spmetadata_document: str = None,
        user_pool_id: str = None,
    ):
        self.acsurl = acsurl
        self.entity_id = entity_id
        self.spmetadata_document = spmetadata_document
        self.user_pool_id = user_pool_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acsurl is not None:
            result['ACSURL'] = self.acsurl

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.spmetadata_document is not None:
            result['SPMetadataDocument'] = self.spmetadata_document

        if self.user_pool_id is not None:
            result['UserPoolId'] = self.user_pool_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ACSURL') is not None:
            self.acsurl = m.get('ACSURL')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('SPMetadataDocument') is not None:
            self.spmetadata_document = m.get('SPMetadataDocument')

        if m.get('UserPoolId') is not None:
            self.user_pool_id = m.get('UserPoolId')

        return self

