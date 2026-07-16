# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDomainRealNameVerificationInfoResponseBody(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        identity_credential: str = None,
        identity_credential_no: str = None,
        identity_credential_type: str = None,
        identity_credential_url: str = None,
        instance_id: str = None,
        request_id: str = None,
        submission_date: str = None,
    ):
        self.domain_name = domain_name
        self.identity_credential = identity_credential
        self.identity_credential_no = identity_credential_no
        self.identity_credential_type = identity_credential_type
        self.identity_credential_url = identity_credential_url
        self.instance_id = instance_id
        self.request_id = request_id
        self.submission_date = submission_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.identity_credential is not None:
            result['IdentityCredential'] = self.identity_credential

        if self.identity_credential_no is not None:
            result['IdentityCredentialNo'] = self.identity_credential_no

        if self.identity_credential_type is not None:
            result['IdentityCredentialType'] = self.identity_credential_type

        if self.identity_credential_url is not None:
            result['IdentityCredentialUrl'] = self.identity_credential_url

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.submission_date is not None:
            result['SubmissionDate'] = self.submission_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('IdentityCredential') is not None:
            self.identity_credential = m.get('IdentityCredential')

        if m.get('IdentityCredentialNo') is not None:
            self.identity_credential_no = m.get('IdentityCredentialNo')

        if m.get('IdentityCredentialType') is not None:
            self.identity_credential_type = m.get('IdentityCredentialType')

        if m.get('IdentityCredentialUrl') is not None:
            self.identity_credential_url = m.get('IdentityCredentialUrl')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SubmissionDate') is not None:
            self.submission_date = m.get('SubmissionDate')

        return self

