# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetExternalSAMLIdentityProviderRequest(DaraModel):
    def __init__(
        self,
        binding_type: str = None,
        directory_id: str = None,
        encoded_metadata_document: str = None,
        entity_id: str = None,
        login_url: str = None,
        ssostatus: str = None,
        want_request_signed: bool = None,
        x_509certificate: str = None,
    ):
        # The binding for sending SAML requests. Valid values:
        # 
        # *   Post: HTTP Post bindings.
        # *   Redirect: HTTP Redirect bindings.
        self.binding_type = binding_type
        # The ID of the directory.
        self.directory_id = directory_id
        # The metadata file of the IdP. The value of this parameter is Base64-encoded.
        # 
        # The file is provided by the IdP that supports SAML 2.0.
        self.encoded_metadata_document = encoded_metadata_document
        # The entity ID of the IdP.
        self.entity_id = entity_id
        # The logon URL of the IdP.
        self.login_url = login_url
        # The status of SSO logon. Valid values:
        # 
        # *   Enabled
        # *   Disabled (default)
        self.ssostatus = ssostatus
        # Specifies whether CloudSSO needs to sign SAML requests. The requests are sent when users log on to the CloudSSO user portal to initiate SAML-based SSO. Valid values:
        # 
        # *   true
        # *   false (default)
        self.want_request_signed = want_request_signed
        # The X.509 certificate in the PEM format. If you specify this parameter, all existing certificates are replaced.
        self.x_509certificate = x_509certificate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.binding_type is not None:
            result['BindingType'] = self.binding_type

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

        if self.want_request_signed is not None:
            result['WantRequestSigned'] = self.want_request_signed

        if self.x_509certificate is not None:
            result['X509Certificate'] = self.x_509certificate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindingType') is not None:
            self.binding_type = m.get('BindingType')

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

        if m.get('WantRequestSigned') is not None:
            self.want_request_signed = m.get('WantRequestSigned')

        if m.get('X509Certificate') is not None:
            self.x_509certificate = m.get('X509Certificate')

        return self

