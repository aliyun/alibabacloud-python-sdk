# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class SetSAMLIdentityProviderResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        ssoidentity_provider_configuration: main_models.SetSAMLIdentityProviderResponseBodySSOIdentityProviderConfiguration = None,
    ):
        self.request_id = request_id
        self.ssoidentity_provider_configuration = ssoidentity_provider_configuration

    def validate(self):
        if self.ssoidentity_provider_configuration:
            self.ssoidentity_provider_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.ssoidentity_provider_configuration is not None:
            result['SSOIdentityProviderConfiguration'] = self.ssoidentity_provider_configuration.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SSOIdentityProviderConfiguration') is not None:
            temp_model = main_models.SetSAMLIdentityProviderResponseBodySSOIdentityProviderConfiguration()
            self.ssoidentity_provider_configuration = temp_model.from_map(m.get('SSOIdentityProviderConfiguration'))

        return self

class SetSAMLIdentityProviderResponseBodySSOIdentityProviderConfiguration(DaraModel):
    def __init__(
        self,
        entity_id: str = None,
        jitprovision_status: str = None,
        jitupdate_status: str = None,
        login_url: str = None,
        samlbinding_type: str = None,
        ssostatus: str = None,
        x_509certificates: List[main_models.SetSAMLIdentityProviderResponseBodySSOIdentityProviderConfigurationX509Certificates] = None,
    ):
        self.entity_id = entity_id
        self.jitprovision_status = jitprovision_status
        self.jitupdate_status = jitupdate_status
        self.login_url = login_url
        self.samlbinding_type = samlbinding_type
        self.ssostatus = ssostatus
        self.x_509certificates = x_509certificates

    def validate(self):
        if self.x_509certificates:
            for v1 in self.x_509certificates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.jitprovision_status is not None:
            result['JITProvisionStatus'] = self.jitprovision_status

        if self.jitupdate_status is not None:
            result['JITUpdateStatus'] = self.jitupdate_status

        if self.login_url is not None:
            result['LoginURL'] = self.login_url

        if self.samlbinding_type is not None:
            result['SAMLBindingType'] = self.samlbinding_type

        if self.ssostatus is not None:
            result['SSOStatus'] = self.ssostatus

        result['X509Certificates'] = []
        if self.x_509certificates is not None:
            for k1 in self.x_509certificates:
                result['X509Certificates'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('JITProvisionStatus') is not None:
            self.jitprovision_status = m.get('JITProvisionStatus')

        if m.get('JITUpdateStatus') is not None:
            self.jitupdate_status = m.get('JITUpdateStatus')

        if m.get('LoginURL') is not None:
            self.login_url = m.get('LoginURL')

        if m.get('SAMLBindingType') is not None:
            self.samlbinding_type = m.get('SAMLBindingType')

        if m.get('SSOStatus') is not None:
            self.ssostatus = m.get('SSOStatus')

        self.x_509certificates = []
        if m.get('X509Certificates') is not None:
            for k1 in m.get('X509Certificates'):
                temp_model = main_models.SetSAMLIdentityProviderResponseBodySSOIdentityProviderConfigurationX509Certificates()
                self.x_509certificates.append(temp_model.from_map(k1))

        return self

class SetSAMLIdentityProviderResponseBodySSOIdentityProviderConfigurationX509Certificates(DaraModel):
    def __init__(
        self,
        certificate_id: str = None,
        x_509certificate: str = None,
    ):
        self.certificate_id = certificate_id
        self.x_509certificate = x_509certificate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id

        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')

        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')

        return self

