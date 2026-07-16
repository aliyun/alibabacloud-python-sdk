# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateMacResponseBody(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        key_id: str = None,
        mac: str = None,
        request_id: str = None,
    ):
        # The algorithm that is used to generate the message authentication code. Valid values vary based on the key specification:  
        # 
        # - HMAC_SM3
        # 
        # - HMAC_SHA_224
        # 
        # - HMAC_SHA_256
        # 
        # - HMAC_SHA_384
        # 
        # - HMAC_SHA_512
        self.algorithm = algorithm
        # The globally unique identifier of the customer master key (CMK).
        # 
        # > If the KeyId parameter in the request uses a CMK alias, the response returns the CMK identifier that corresponds to the alias.
        self.key_id = key_id
        # The Base64-encoded message authenticate code.
        self.mac = mac
        # The ID of the request. Alibaba Cloud generates a unique identifier for each request. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

