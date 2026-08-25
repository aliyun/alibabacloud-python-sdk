# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class ListSCIMServerCredentialsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        scimserver_credentials: List[main_models.ListSCIMServerCredentialsResponseBodySCIMServerCredentials] = None,
        total_counts: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The SCIM credentials.
        self.scimserver_credentials = scimserver_credentials
        # The total number of entries returned.
        self.total_counts = total_counts

    def validate(self):
        if self.scimserver_credentials:
            for v1 in self.scimserver_credentials:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SCIMServerCredentials'] = []
        if self.scimserver_credentials is not None:
            for k1 in self.scimserver_credentials:
                result['SCIMServerCredentials'].append(k1.to_map() if k1 else None)

        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.scimserver_credentials = []
        if m.get('SCIMServerCredentials') is not None:
            for k1 in m.get('SCIMServerCredentials'):
                temp_model = main_models.ListSCIMServerCredentialsResponseBodySCIMServerCredentials()
                self.scimserver_credentials.append(temp_model.from_map(k1))

        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')

        return self

class ListSCIMServerCredentialsResponseBodySCIMServerCredentials(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        credential_id: str = None,
        credential_type: str = None,
        directory_id: str = None,
        expire_time: str = None,
        status: str = None,
    ):
        # The time when the SCIM credential was created.
        self.create_time = create_time
        # The ID of the SCIM credential.
        self.credential_id = credential_id
        # The type of the SCIM credential.
        self.credential_type = credential_type
        # The ID of the directory.
        self.directory_id = directory_id
        # The time when the SCIM credential expires.
        self.expire_time = expire_time
        # The status of the SCIM credential. Valid values:
        # 
        # *   Enabled
        # *   Disabled
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.credential_id is not None:
            result['CredentialId'] = self.credential_id

        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CredentialId') is not None:
            self.credential_id = m.get('CredentialId')

        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

