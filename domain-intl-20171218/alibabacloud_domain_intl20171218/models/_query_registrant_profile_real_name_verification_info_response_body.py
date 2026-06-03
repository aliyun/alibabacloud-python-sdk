# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryRegistrantProfileRealNameVerificationInfoResponseBody(DaraModel):
    def __init__(
        self,
        identity_credential: str = None,
        identity_credential_no: str = None,
        identity_credential_type: str = None,
        identity_credential_url: str = None,
        modification_date: str = None,
        registrant_profile_id: int = None,
        request_id: str = None,
        submission_date: str = None,
    ):
        self.identity_credential = identity_credential
        self.identity_credential_no = identity_credential_no
        self.identity_credential_type = identity_credential_type
        self.identity_credential_url = identity_credential_url
        self.modification_date = modification_date
        self.registrant_profile_id = registrant_profile_id
        self.request_id = request_id
        self.submission_date = submission_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identity_credential is not None:
            result['IdentityCredential'] = self.identity_credential

        if self.identity_credential_no is not None:
            result['IdentityCredentialNo'] = self.identity_credential_no

        if self.identity_credential_type is not None:
            result['IdentityCredentialType'] = self.identity_credential_type

        if self.identity_credential_url is not None:
            result['IdentityCredentialUrl'] = self.identity_credential_url

        if self.modification_date is not None:
            result['ModificationDate'] = self.modification_date

        if self.registrant_profile_id is not None:
            result['RegistrantProfileId'] = self.registrant_profile_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.submission_date is not None:
            result['SubmissionDate'] = self.submission_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdentityCredential') is not None:
            self.identity_credential = m.get('IdentityCredential')

        if m.get('IdentityCredentialNo') is not None:
            self.identity_credential_no = m.get('IdentityCredentialNo')

        if m.get('IdentityCredentialType') is not None:
            self.identity_credential_type = m.get('IdentityCredentialType')

        if m.get('IdentityCredentialUrl') is not None:
            self.identity_credential_url = m.get('IdentityCredentialUrl')

        if m.get('ModificationDate') is not None:
            self.modification_date = m.get('ModificationDate')

        if m.get('RegistrantProfileId') is not None:
            self.registrant_profile_id = m.get('RegistrantProfileId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SubmissionDate') is not None:
            self.submission_date = m.get('SubmissionDate')

        return self

