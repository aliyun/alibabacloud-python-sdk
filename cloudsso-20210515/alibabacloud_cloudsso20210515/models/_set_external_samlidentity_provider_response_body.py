# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class SetExternalSAMLIdentityProviderResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        samlidentity_provider_configuration: main_models.SetExternalSAMLIdentityProviderResponseBodySAMLIdentityProviderConfiguration = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The configurations of the IdP.
        self.samlidentity_provider_configuration = samlidentity_provider_configuration

    def validate(self):
        if self.samlidentity_provider_configuration:
            self.samlidentity_provider_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.samlidentity_provider_configuration is not None:
            result['SAMLIdentityProviderConfiguration'] = self.samlidentity_provider_configuration.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SAMLIdentityProviderConfiguration') is not None:
            temp_model = main_models.SetExternalSAMLIdentityProviderResponseBodySAMLIdentityProviderConfiguration()
            self.samlidentity_provider_configuration = temp_model.from_map(m.get('SAMLIdentityProviderConfiguration'))

        return self

class SetExternalSAMLIdentityProviderResponseBodySAMLIdentityProviderConfiguration(DaraModel):
    def __init__(
        self,
        binding_type: str = None,
        certificate_ids: List[str] = None,
        create_time: str = None,
        directory_id: str = None,
        encoded_metadata_document: str = None,
        entity_id: str = None,
        login_url: str = None,
        ssostatus: str = None,
        update_time: str = None,
        want_request_signed: bool = None,
    ):
        # The binding for sending SAML requests. Valid values:
        # 
        # *   Post: HTTP Post bindings.
        # *   Redirect: HTTP Redirect bindings.
        self.binding_type = binding_type
        # The IDs of the SAML signing certificates.
        self.certificate_ids = certificate_ids
        # The time when the IdP was configured for the first time.
        self.create_time = create_time
        # The ID of the directory.
        self.directory_id = directory_id
        # The metadata file of the IdP. The value of this parameter is Base64-encoded.
        self.encoded_metadata_document = encoded_metadata_document
        # The entity ID of the IdP.
        self.entity_id = entity_id
        # The logon URL of the IdP.
        self.login_url = login_url
        # The status of SSO logon. Valid values:
        # 
        # *   Enabled
        # *   Disabled
        self.ssostatus = ssostatus
        # The time when the IdP configurations were last modified.
        self.update_time = update_time
        # Indicates whether CloudSSO needs to sign SAML requests. The requests are sent when users log on to the CloudSSO user portal to initiate SAML-based SSO. Valid values:
        # 
        # *   true
        # *   false (default)
        self.want_request_signed = want_request_signed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.binding_type is not None:
            result['BindingType'] = self.binding_type

        if self.certificate_ids is not None:
            result['CertificateIds'] = self.certificate_ids

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.encoded_metadata_document is not None:
            result['EncodedMetadataDocument'] = self.encoded_metadata_document

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.login_url is not None:
            result['LoginUrl'] = self.login_url

        if self.ssostatus is not None:
            result['SSOStatus'] = self.ssostatus

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.want_request_signed is not None:
            result['WantRequestSigned'] = self.want_request_signed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')

        if m.get('CertificateIds') is not None:
            self.certificate_ids = m.get('CertificateIds')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('EncodedMetadataDocument') is not None:
            self.encoded_metadata_document = m.get('EncodedMetadataDocument')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('LoginUrl') is not None:
            self.login_url = m.get('LoginUrl')

        if m.get('SSOStatus') is not None:
            self.ssostatus = m.get('SSOStatus')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('WantRequestSigned') is not None:
            self.want_request_signed = m.get('WantRequestSigned')

        return self

