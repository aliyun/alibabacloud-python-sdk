# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeAtiCertificateResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.DescribeAtiCertificateResponseBodyAccessDeniedDetail = None,
        agent_host: str = None,
        agent_id: str = None,
        algorithm: str = None,
        cert_pem: str = None,
        cert_type: str = None,
        create_timestamp: int = None,
        issuer: str = None,
        not_after: str = None,
        not_before: str = None,
        request_id: str = None,
        san: str = None,
        serial_number: str = None,
        source: str = None,
        status: str = None,
        subject: str = None,
        tlsa_fingerprint: str = None,
        update_timestamp: int = None,
    ):
        # The access denied details. This field is returned only when RAM authentication fails.
        self.access_denied_detail = access_denied_detail
        # The agent host address.
        self.agent_host = agent_host
        # The agent ID. After CNNIC real-name authentication, CNNIC assigns a unified agent ID. The agent ID serves as the unique identifier that binds the agent to the real-name authenticated registrant.
        self.agent_id = agent_id
        # The encryption algorithm of the certificate.
        self.algorithm = algorithm
        # The certificate file in PEM format.
        self.cert_pem = cert_pem
        # The certificate type. Valid values:
        # - Server: server certificate.
        # - Identity: identity certificate.
        self.cert_type = cert_type
        # The creation time of the health check template (timestamp).
        self.create_timestamp = create_timestamp
        # The issuer information of the certificate, identified in Distinguished Names (DN) format.
        self.issuer = issuer
        # The end time of the certificate validity period.
        self.not_after = not_after
        # The start time of the certificate validity period.
        self.not_before = not_before
        # The request ID.
        self.request_id = request_id
        # The Subject Alternative Name (SAN), which specifies additional identities for the certificate subject.
        self.san = san
        # The serial number that indicates the priority of the returned address. A smaller value indicates a higher priority.
        self.serial_number = serial_number
        # The certificate source.
        self.source = source
        # The validity status of the certificate. Valid values:
        # 
        # - Valid
        # - Invalid
        self.status = status
        # The certificate subject (owner), identified in DN format.
        self.subject = subject
        # The DNS TLSA record value that stores the certificate public key fingerprint.
        self.tlsa_fingerprint = tlsa_fingerprint
        # The update time (timestamp).
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()

        if self.agent_host is not None:
            result['AgentHost'] = self.agent_host

        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.cert_pem is not None:
            result['CertPem'] = self.cert_pem

        if self.cert_type is not None:
            result['CertType'] = self.cert_type

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.issuer is not None:
            result['Issuer'] = self.issuer

        if self.not_after is not None:
            result['NotAfter'] = self.not_after

        if self.not_before is not None:
            result['NotBefore'] = self.not_before

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.san is not None:
            result['San'] = self.san

        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        if self.subject is not None:
            result['Subject'] = self.subject

        if self.tlsa_fingerprint is not None:
            result['TlsaFingerprint'] = self.tlsa_fingerprint

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.DescribeAtiCertificateResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('AgentHost') is not None:
            self.agent_host = m.get('AgentHost')

        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('CertPem') is not None:
            self.cert_pem = m.get('CertPem')

        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('Issuer') is not None:
            self.issuer = m.get('Issuer')

        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')

        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('San') is not None:
            self.san = m.get('San')

        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Subject') is not None:
            self.subject = m.get('Subject')

        if m.get('TlsaFingerprint') is not None:
            self.tlsa_fingerprint = m.get('TlsaFingerprint')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        return self

class DescribeAtiCertificateResponseBodyAccessDeniedDetail(DaraModel):
    def __init__(
        self,
        auth_action: str = None,
        auth_principal_display_name: str = None,
        auth_principal_owner_id: str = None,
        auth_principal_type: str = None,
        encoded_diagnostic_message: str = None,
        no_permission_type: str = None,
        policy_type: str = None,
    ):
        # The unauthorized operation that was attempted.
        self.auth_action = auth_action
        # The display name of the authorization principal.
        self.auth_principal_display_name = auth_principal_display_name
        # The owner ID of the authorization principal.
        self.auth_principal_owner_id = auth_principal_owner_id
        # The identity type.
        self.auth_principal_type = auth_principal_type
        # The encrypted complete diagnostic message.
        self.encoded_diagnostic_message = encoded_diagnostic_message
        # The reason for the authentication failure. Valid values:
        # - ExplicitDeny: Explicit deny.
        # - ImplicitDeny: Implicit deny.
        self.no_permission_type = no_permission_type
        # The policy type.
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_action is not None:
            result['AuthAction'] = self.auth_action

        if self.auth_principal_display_name is not None:
            result['AuthPrincipalDisplayName'] = self.auth_principal_display_name

        if self.auth_principal_owner_id is not None:
            result['AuthPrincipalOwnerId'] = self.auth_principal_owner_id

        if self.auth_principal_type is not None:
            result['AuthPrincipalType'] = self.auth_principal_type

        if self.encoded_diagnostic_message is not None:
            result['EncodedDiagnosticMessage'] = self.encoded_diagnostic_message

        if self.no_permission_type is not None:
            result['NoPermissionType'] = self.no_permission_type

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthAction') is not None:
            self.auth_action = m.get('AuthAction')

        if m.get('AuthPrincipalDisplayName') is not None:
            self.auth_principal_display_name = m.get('AuthPrincipalDisplayName')

        if m.get('AuthPrincipalOwnerId') is not None:
            self.auth_principal_owner_id = m.get('AuthPrincipalOwnerId')

        if m.get('AuthPrincipalType') is not None:
            self.auth_principal_type = m.get('AuthPrincipalType')

        if m.get('EncodedDiagnosticMessage') is not None:
            self.encoded_diagnostic_message = m.get('EncodedDiagnosticMessage')

        if m.get('NoPermissionType') is not None:
            self.no_permission_type = m.get('NoPermissionType')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

