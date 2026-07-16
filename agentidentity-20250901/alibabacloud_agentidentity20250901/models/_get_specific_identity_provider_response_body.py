# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class GetSpecificIdentityProviderResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        specific_identity_provider_configuration: main_models.GetSpecificIdentityProviderResponseBodySpecificIdentityProviderConfiguration = None,
    ):
        self.request_id = request_id
        self.specific_identity_provider_configuration = specific_identity_provider_configuration

    def validate(self):
        if self.specific_identity_provider_configuration:
            self.specific_identity_provider_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.specific_identity_provider_configuration is not None:
            result['SpecificIdentityProviderConfiguration'] = self.specific_identity_provider_configuration.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SpecificIdentityProviderConfiguration') is not None:
            temp_model = main_models.GetSpecificIdentityProviderResponseBodySpecificIdentityProviderConfiguration()
            self.specific_identity_provider_configuration = temp_model.from_map(m.get('SpecificIdentityProviderConfiguration'))

        return self

class GetSpecificIdentityProviderResponseBodySpecificIdentityProviderConfiguration(DaraModel):
    def __init__(
        self,
        idpmetadata: str = None,
        identity_provider_type: str = None,
        ssostatus: str = None,
    ):
        self.idpmetadata = idpmetadata
        self.identity_provider_type = identity_provider_type
        self.ssostatus = ssostatus

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.idpmetadata is not None:
            result['IDPMetadata'] = self.idpmetadata

        if self.identity_provider_type is not None:
            result['IdentityProviderType'] = self.identity_provider_type

        if self.ssostatus is not None:
            result['SSOStatus'] = self.ssostatus

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IDPMetadata') is not None:
            self.idpmetadata = m.get('IDPMetadata')

        if m.get('IdentityProviderType') is not None:
            self.identity_provider_type = m.get('IdentityProviderType')

        if m.get('SSOStatus') is not None:
            self.ssostatus = m.get('SSOStatus')

        return self

