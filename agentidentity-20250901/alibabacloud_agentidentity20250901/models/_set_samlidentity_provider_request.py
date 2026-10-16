# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SetSAMLIdentityProviderRequest(DaraModel):
    def __init__(
        self,
        entity_id: str = None,
        jitprovision_status: str = None,
        jitupdate_status: str = None,
        login_url: str = None,
        samlbinding_type: str = None,
        ssostatus: str = None,
        user_pool_name: str = None,
        x_509certificates: List[str] = None,
    ):
        # The IdP identifier. This is the EntityID from the SAML metadata of the external IdP.
        self.entity_id = entity_id
        # The enabling status of Just-In-Time (JIT) user synchronization and creation. Valid values:
        # - Enabled: Enabled. If a user with the same name does not exist in the user pool during SAML logon, automatic creation is performed.
        # - Disabled: Shutdown. If the user is not found, the logon is failed. Default value.
        self.jitprovision_status = jitprovision_status
        # The enabling status of updating user information through synchronization. Valid values:
        # - Enabled: The update is enabled. If a user with the same name exists during SAML logon, the user information is updated based on the attributes (DisplayName and Description) passed by the IdP.
        # - Disabled: The update is disabled. Only the logon state is updated, and user attributes are not updated. Default value.
        self.jitupdate_status = jitupdate_status
        # The IdP logon URL. When a user logs on, the browser is redirected to this URL to complete SAML authentication.
        self.login_url = login_url
        # The SAML protocol binding type. Valid values:
        # - HTTP-Redirect: AuthnRequest is sent by using HTTP redirect. Default value.
        # - HTTP-POST: AuthnRequest is sent by using HTTP POST.
        self.samlbinding_type = samlbinding_type
        # The enabling status of single sign-on (SSO). Valid values:
        # - Enabled: SAML SSO is enabled, and users can log on through an external IdP.
        # - Disabled: SAML SSO is disabled, and users cannot log on through the IdP. Default value.
        self.ssostatus = ssostatus
        # The name of the user pool.
        self.user_pool_name = user_pool_name
        # The list of X.509 certificates in PEM format. If you specify this parameter, all existing certificates are replaced.
        self.x_509certificates = x_509certificates

    def validate(self):
        pass

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

        if self.user_pool_name is not None:
            result['UserPoolName'] = self.user_pool_name

        if self.x_509certificates is not None:
            result['X509Certificates'] = self.x_509certificates

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

        if m.get('UserPoolName') is not None:
            self.user_pool_name = m.get('UserPoolName')

        if m.get('X509Certificates') is not None:
            self.x_509certificates = m.get('X509Certificates')

        return self

