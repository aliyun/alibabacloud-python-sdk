# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeKmsKeysResponseBody(DaraModel):
    def __init__(
        self,
        authorize_status: str = None,
        keys: List[main_models.DescribeKmsKeysResponseBodyKeys] = None,
        kms_service_status: str = None,
        request_id: str = None,
    ):
        # The authorization status.
        # 
        # Valid value:
        # 
        # *   not_authorized
        # *   authorized
        self.authorize_status = authorize_status
        # Customer master key (CMK)
        self.keys = keys
        # Indicates whether KMS is activated.
        # 
        # Valid value:
        # 
        # *   disabled
        # *   enabled
        self.kms_service_status = kms_service_status
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.keys:
            for v1 in self.keys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorize_status is not None:
            result['AuthorizeStatus'] = self.authorize_status

        result['Keys'] = []
        if self.keys is not None:
            for k1 in self.keys:
                result['Keys'].append(k1.to_map() if k1 else None)

        if self.kms_service_status is not None:
            result['KmsServiceStatus'] = self.kms_service_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizeStatus') is not None:
            self.authorize_status = m.get('AuthorizeStatus')

        self.keys = []
        if m.get('Keys') is not None:
            for k1 in m.get('Keys'):
                temp_model = main_models.DescribeKmsKeysResponseBodyKeys()
                self.keys.append(temp_model.from_map(k1))

        if m.get('KmsServiceStatus') is not None:
            self.kms_service_status = m.get('KmsServiceStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeKmsKeysResponseBodyKeys(DaraModel):
    def __init__(
        self,
        alias: str = None,
        arn: str = None,
        key_id: str = None,
        type: str = None,
    ):
        # The alias of the key.
        self.alias = alias
        # The Alibaba Cloud Resource Name (ARN) of the key in KMS.
        self.arn = arn
        # The ID of the key.
        self.key_id = key_id
        # The type of the key.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.arn is not None:
            result['Arn'] = self.arn

        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

