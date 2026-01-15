# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetSecretResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetSecretResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetSecretResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetSecretResponseBodyData(DaraModel):
    def __init__(
        self,
        create_timestamp: int = None,
        gateway_type: str = None,
        kms_config: main_models.KMSConfig = None,
        name: str = None,
        reference_count: int = None,
        secret_id: str = None,
        secret_source: str = None,
        status: str = None,
        update_timestamp: int = None,
    ):
        self.create_timestamp = create_timestamp
        self.gateway_type = gateway_type
        self.kms_config = kms_config
        self.name = name
        self.reference_count = reference_count
        self.secret_id = secret_id
        self.secret_source = secret_source
        self.status = status
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.kms_config:
            self.kms_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_timestamp is not None:
            result['createTimestamp'] = self.create_timestamp

        if self.gateway_type is not None:
            result['gatewayType'] = self.gateway_type

        if self.kms_config is not None:
            result['kmsConfig'] = self.kms_config.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.reference_count is not None:
            result['referenceCount'] = self.reference_count

        if self.secret_id is not None:
            result['secretId'] = self.secret_id

        if self.secret_source is not None:
            result['secretSource'] = self.secret_source

        if self.status is not None:
            result['status'] = self.status

        if self.update_timestamp is not None:
            result['updateTimestamp'] = self.update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTimestamp') is not None:
            self.create_timestamp = m.get('createTimestamp')

        if m.get('gatewayType') is not None:
            self.gateway_type = m.get('gatewayType')

        if m.get('kmsConfig') is not None:
            temp_model = main_models.KMSConfig()
            self.kms_config = temp_model.from_map(m.get('kmsConfig'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('referenceCount') is not None:
            self.reference_count = m.get('referenceCount')

        if m.get('secretId') is not None:
            self.secret_id = m.get('secretId')

        if m.get('secretSource') is not None:
            self.secret_source = m.get('secretSource')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updateTimestamp') is not None:
            self.update_timestamp = m.get('updateTimestamp')

        return self

