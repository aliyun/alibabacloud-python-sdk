# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetParametersForImportRequest(DaraModel):
    def __init__(
        self,
        key_id: str = None,
        wrapping_algorithm: str = None,
        wrapping_key_spec: str = None,
    ):
        # The globally unique ID of the CMK.
        # 
        # >  You can import key material only for CMKs whose Origin parameter is set to EXTERNAL.
        # 
        # This parameter is required.
        self.key_id = key_id
        # The algorithm that is used to encrypt key material.
        # 
        # This parameter is required.
        self.wrapping_algorithm = wrapping_algorithm
        # The type of the public key that is used to encrypt key material.
        # 
        # This parameter is required.
        self.wrapping_key_spec = wrapping_key_spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.wrapping_algorithm is not None:
            result['WrappingAlgorithm'] = self.wrapping_algorithm

        if self.wrapping_key_spec is not None:
            result['WrappingKeySpec'] = self.wrapping_key_spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('WrappingAlgorithm') is not None:
            self.wrapping_algorithm = m.get('WrappingAlgorithm')

        if m.get('WrappingKeySpec') is not None:
            self.wrapping_key_spec = m.get('WrappingKeySpec')

        return self

