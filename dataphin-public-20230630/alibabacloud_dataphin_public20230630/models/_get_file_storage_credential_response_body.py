# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetFileStorageCredentialResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        storage_credential: main_models.GetFileStorageCredentialResponseBodyStorageCredential = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.storage_credential = storage_credential
        self.success = success

    def validate(self):
        if self.storage_credential:
            self.storage_credential.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.storage_credential is not None:
            result['StorageCredential'] = self.storage_credential.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StorageCredential') is not None:
            temp_model = main_models.GetFileStorageCredentialResponseBodyStorageCredential()
            self.storage_credential = temp_model.from_map(m.get('StorageCredential'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetFileStorageCredentialResponseBodyStorageCredential(DaraModel):
    def __init__(
        self,
        access_id: str = None,
        access_key: str = None,
        bucket: str = None,
        endpoint: str = None,
        expiration: int = None,
        object_name: str = None,
        region: str = None,
        security_token: str = None,
        storage_type: str = None,
    ):
        self.access_id = access_id
        self.access_key = access_key
        self.bucket = bucket
        self.endpoint = endpoint
        self.expiration = expiration
        self.object_name = object_name
        # region
        self.region = region
        self.security_token = security_token
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_id is not None:
            result['AccessId'] = self.access_id

        if self.access_key is not None:
            result['AccessKey'] = self.access_key

        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.expiration is not None:
            result['Expiration'] = self.expiration

        if self.object_name is not None:
            result['ObjectName'] = self.object_name

        if self.region is not None:
            result['Region'] = self.region

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')

        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')

        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')

        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

