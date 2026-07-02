# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPublicKeyResponseBody(DaraModel):
    def __init__(
        self,
        key_id: str = None,
        key_version_id: str = None,
        public_key: str = None,
        request_id: str = None,
    ):
        # The globally unique identifier of the CMK.
        # 
        # > If you specify an alias of the CMK for the KeyId parameter in the request, the ID of the CMK to which the alias is bound is returned.
        self.key_id = key_id
        # The globally unique identifier of the key version.
        self.key_version_id = key_version_id
        # The public key in the PEM format.
        self.public_key = public_key
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.key_version_id is not None:
            result['KeyVersionId'] = self.key_version_id

        if self.public_key is not None:
            result['PublicKey'] = self.public_key

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('KeyVersionId') is not None:
            self.key_version_id = m.get('KeyVersionId')

        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

