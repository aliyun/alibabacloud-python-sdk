# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetClientKeyResponseBody(DaraModel):
    def __init__(
        self,
        aap_name: str = None,
        client_key_id: str = None,
        create_time: str = None,
        key_algorithm: str = None,
        key_origin: str = None,
        not_after: str = None,
        not_before: str = None,
        public_key_data: str = None,
        request_id: str = None,
    ):
        # The name of the application access point (AAP).
        self.aap_name = aap_name
        # The ID of the client key.
        self.client_key_id = client_key_id
        # The time when the client key was created.
        self.create_time = create_time
        # The algorithm of the private key for the client key.
        self.key_algorithm = key_algorithm
        # The creator of the client key.
        # 
        # Currently, client keys are generated only by KMS. The value is \\`KMS_PROVIDED\\`.
        self.key_origin = key_origin
        # The time when the client key expires.
        self.not_after = not_after
        # The time when the validity period of the client key starts.
        self.not_before = not_before
        # The content of the public key for the client key.
        self.public_key_data = public_key_data
        # The ID of the request. Alibaba Cloud generates this unique ID for each request. Use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aap_name is not None:
            result['AapName'] = self.aap_name

        if self.client_key_id is not None:
            result['ClientKeyId'] = self.client_key_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.key_algorithm is not None:
            result['KeyAlgorithm'] = self.key_algorithm

        if self.key_origin is not None:
            result['KeyOrigin'] = self.key_origin

        if self.not_after is not None:
            result['NotAfter'] = self.not_after

        if self.not_before is not None:
            result['NotBefore'] = self.not_before

        if self.public_key_data is not None:
            result['PublicKeyData'] = self.public_key_data

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AapName') is not None:
            self.aap_name = m.get('AapName')

        if m.get('ClientKeyId') is not None:
            self.client_key_id = m.get('ClientKeyId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('KeyAlgorithm') is not None:
            self.key_algorithm = m.get('KeyAlgorithm')

        if m.get('KeyOrigin') is not None:
            self.key_origin = m.get('KeyOrigin')

        if m.get('NotAfter') is not None:
            self.not_after = m.get('NotAfter')

        if m.get('NotBefore') is not None:
            self.not_before = m.get('NotBefore')

        if m.get('PublicKeyData') is not None:
            self.public_key_data = m.get('PublicKeyData')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

