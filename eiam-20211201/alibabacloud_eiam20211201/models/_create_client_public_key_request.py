# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateClientPublicKeyRequest(DaraModel):
    def __init__(
        self,
        algorithm_type: str = None,
        application_id: str = None,
        client_token: str = None,
        instance_id: str = None,
        public_key: str = None,
    ):
        # The algorithm type.
        # 
        # This parameter is required.
        self.algorithm_type = algorithm_type
        # The application ID.
        # 
        # This parameter is required.
        self.application_id = application_id
        # A client token used to ensure the idempotence of the request. Generate a unique value from your client for this parameter. The ClientToken value can contain only ASCII characters and must be no more than 64 characters long. For more information, see [How to ensure idempotence](https://www.alibabacloud.com/help/en/ecs/developer-reference/how-to-ensure-idempotence).
        # 
        # This parameter is required.
        self.client_token = client_token
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The public key in the Subject Public Key Info (SPKI) type of the Privacy-Enhanced Mail (PEM) format. The key must start with -----BEGIN PUBLIC KEY----- and end with -----END PUBLIC KEY-----.
        # 
        # This parameter is required.
        self.public_key = public_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm_type is not None:
            result['AlgorithmType'] = self.algorithm_type

        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.public_key is not None:
            result['PublicKey'] = self.public_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmType') is not None:
            self.algorithm_type = m.get('AlgorithmType')

        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')

        return self

