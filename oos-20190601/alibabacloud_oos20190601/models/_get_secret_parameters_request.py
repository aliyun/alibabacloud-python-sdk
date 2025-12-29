# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSecretParametersRequest(DaraModel):
    def __init__(
        self,
        names: str = None,
        region_id: str = None,
        with_decryption: bool = None,
    ):
        # The name of the encryption parameter. Multiple encryption parameters can form a JSON array in the format of ["xxxxxxxxx", "yyyyyyyyy", … "zzzzzzzzz"]. Each JSON array can contain a maximum of 10 encryption parameters. Multiple encryption parameters in the array are separated by commas (,).
        # 
        # This parameter is required.
        self.names = names
        # The ID of the region.
        self.region_id = region_id
        # Specifies whether to decrypt the parameter value. Default value: false. Valid values:
        # 
        # *   true
        # *   false
        self.with_decryption = with_decryption

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.names is not None:
            result['Names'] = self.names

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.with_decryption is not None:
            result['WithDecryption'] = self.with_decryption

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Names') is not None:
            self.names = m.get('Names')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('WithDecryption') is not None:
            self.with_decryption = m.get('WithDecryption')

        return self

