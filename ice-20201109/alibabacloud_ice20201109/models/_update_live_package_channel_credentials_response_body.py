# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class UpdateLivePackageChannelCredentialsResponseBody(DaraModel):
    def __init__(
        self,
        ingest_endpoints: List[main_models.UpdateLivePackageChannelCredentialsResponseBodyIngestEndpoints] = None,
        request_id: str = None,
    ):
        # The information about the ingest endpoint.
        self.ingest_endpoints = ingest_endpoints
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.ingest_endpoints:
            for v1 in self.ingest_endpoints:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IngestEndpoints'] = []
        if self.ingest_endpoints is not None:
            for k1 in self.ingest_endpoints:
                result['IngestEndpoints'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ingest_endpoints = []
        if m.get('IngestEndpoints') is not None:
            for k1 in m.get('IngestEndpoints'):
                temp_model = main_models.UpdateLivePackageChannelCredentialsResponseBodyIngestEndpoints()
                self.ingest_endpoints.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class UpdateLivePackageChannelCredentialsResponseBodyIngestEndpoints(DaraModel):
    def __init__(
        self,
        id: str = None,
        password: str = None,
        url: str = None,
        username: str = None,
    ):
        # The ingest endpoint ID. `input1` indicates primary and `input2` indicates secondary.
        self.id = id
        # The password.
        self.password = password
        # The ingest endpoint URL.
        self.url = url
        # The username.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.password is not None:
            result['Password'] = self.password

        if self.url is not None:
            result['Url'] = self.url

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

