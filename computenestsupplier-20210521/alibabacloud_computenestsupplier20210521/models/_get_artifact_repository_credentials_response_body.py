# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class GetArtifactRepositoryCredentialsResponseBody(DaraModel):
    def __init__(
        self,
        available_resources: List[main_models.GetArtifactRepositoryCredentialsResponseBodyAvailableResources] = None,
        credentials: main_models.GetArtifactRepositoryCredentialsResponseBodyCredentials = None,
        expire_date: str = None,
        request_id: str = None,
    ):
        # The information about the resources that can be uploaded.
        self.available_resources = available_resources
        # The credentials.
        self.credentials = credentials
        # The time when the credentials expired.
        self.expire_date = expire_date
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.available_resources:
            for v1 in self.available_resources:
                 if v1:
                    v1.validate()
        if self.credentials:
            self.credentials.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableResources'] = []
        if self.available_resources is not None:
            for k1 in self.available_resources:
                result['AvailableResources'].append(k1.to_map() if k1 else None)

        if self.credentials is not None:
            result['Credentials'] = self.credentials.to_map()

        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_resources = []
        if m.get('AvailableResources') is not None:
            for k1 in m.get('AvailableResources'):
                temp_model = main_models.GetArtifactRepositoryCredentialsResponseBodyAvailableResources()
                self.available_resources.append(temp_model.from_map(k1))

        if m.get('Credentials') is not None:
            temp_model = main_models.GetArtifactRepositoryCredentialsResponseBodyCredentials()
            self.credentials = temp_model.from_map(m.get('Credentials'))

        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetArtifactRepositoryCredentialsResponseBodyCredentials(DaraModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        password: str = None,
        security_token: str = None,
        username: str = None,
    ):
        # The AccessKey ID.
        self.access_key_id = access_key_id
        # The AccessKey secret.
        self.access_key_secret = access_key_secret
        # The password.
        self.password = password
        # The Security Token Service (STS) token.
        self.security_token = security_token
        # The username.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id

        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret

        if self.password is not None:
            result['Password'] = self.password

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')

        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

class GetArtifactRepositoryCredentialsResponseBodyAvailableResources(DaraModel):
    def __init__(
        self,
        path: str = None,
        region_id: str = None,
        repository_name: str = None,
    ):
        # The path.
        self.path = path
        # The region ID.
        self.region_id = region_id
        # The repository name.
        self.repository_name = repository_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.path is not None:
            result['Path'] = self.path

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.repository_name is not None:
            result['RepositoryName'] = self.repository_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RepositoryName') is not None:
            self.repository_name = m.get('RepositoryName')

        return self

