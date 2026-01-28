# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_domain20180129 import models as main_models
from darabonba.model import DaraModel

class QueryQualificationDetailResponseBody(DaraModel):
    def __init__(
        self,
        audit_status: int = None,
        credentials: main_models.QueryQualificationDetailResponseBodyCredentials = None,
        request_id: str = None,
        track_id: str = None,
    ):
        self.audit_status = audit_status
        self.credentials = credentials
        self.request_id = request_id
        self.track_id = track_id

    def validate(self):
        if self.credentials:
            self.credentials.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status

        if self.credentials is not None:
            result['Credentials'] = self.credentials.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.track_id is not None:
            result['TrackId'] = self.track_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')

        if m.get('Credentials') is not None:
            temp_model = main_models.QueryQualificationDetailResponseBodyCredentials()
            self.credentials = temp_model.from_map(m.get('Credentials'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TrackId') is not None:
            self.track_id = m.get('TrackId')

        return self

class QueryQualificationDetailResponseBodyCredentials(DaraModel):
    def __init__(
        self,
        qualification_credential: List[main_models.QueryQualificationDetailResponseBodyCredentialsQualificationCredential] = None,
    ):
        self.qualification_credential = qualification_credential

    def validate(self):
        if self.qualification_credential:
            for v1 in self.qualification_credential:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['QualificationCredential'] = []
        if self.qualification_credential is not None:
            for k1 in self.qualification_credential:
                result['QualificationCredential'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.qualification_credential = []
        if m.get('QualificationCredential') is not None:
            for k1 in m.get('QualificationCredential'):
                temp_model = main_models.QueryQualificationDetailResponseBodyCredentialsQualificationCredential()
                self.qualification_credential.append(temp_model.from_map(k1))

        return self

class QueryQualificationDetailResponseBodyCredentialsQualificationCredential(DaraModel):
    def __init__(
        self,
        credential_no: str = None,
        credential_type: str = None,
        credential_url: str = None,
    ):
        self.credential_no = credential_no
        self.credential_type = credential_type
        self.credential_url = credential_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credential_no is not None:
            result['CredentialNo'] = self.credential_no

        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type

        if self.credential_url is not None:
            result['CredentialUrl'] = self.credential_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CredentialNo') is not None:
            self.credential_no = m.get('CredentialNo')

        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')

        if m.get('CredentialUrl') is not None:
            self.credential_url = m.get('CredentialUrl')

        return self

