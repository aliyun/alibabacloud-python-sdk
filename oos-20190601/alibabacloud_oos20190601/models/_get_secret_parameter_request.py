# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSecretParameterRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        parameter_version: int = None,
        region_id: str = None,
        with_decryption: bool = None,
    ):
        # The name of the parameter. The name must be 1 to 180 characters in length, and can contain letters, digits, hyphens (-), and underscores (_). It cannot start with ALIYUN, ACS, ALIBABA, ALICLOUD, or OOS.
        # 
        # This parameter is required.
        self.name = name
        # The version number of the common parameter. Valid values: 1 to 100.
        self.parameter_version = parameter_version
        # The ID of the region.
        self.region_id = region_id
        # Specifies whether to decrypt the parameter value. The decrypted parameter value is returned only if this parameter is set to true. Otherwise, null is returned.
        self.with_decryption = with_decryption

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.with_decryption is not None:
            result['WithDecryption'] = self.with_decryption

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('WithDecryption') is not None:
            self.with_decryption = m.get('WithDecryption')

        return self

