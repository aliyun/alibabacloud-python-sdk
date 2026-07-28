# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AssociateMacSecKeyRequest(DaraModel):
    def __init__(
        self,
        cak: str = None,
        cipher_suite: str = None,
        ckn: str = None,
        physical_connection_id: str = None,
        region_id: str = None,
    ):
        # The passphrase. Only hexadecimal characters are supported. Lowercase characters are automatically transformed to uppercase. If the encryption algorithm type is GCM-AES-128 or GCM-AES-XPN-128, the length must be 32 hexadecimal characters. If the encryption algorithm type is GCM-AES-256 or GCM-AES-XPN-256, the length must be 64 hexadecimal characters.
        # 
        # This parameter is required.
        self.cak = cak
        # The encryption algorithm type. Valid values:
        # 
        # - GCM-AES-128
        # 
        # - GCM-AES-XPN-128
        # 
        # - GCM-AES-256
        # 
        # - GCM-AES-XPN-256
        # 
        # This parameter is required.
        self.cipher_suite = cipher_suite
        # The key name. Only hexadecimal characters are supported. Lowercase characters are automatically converted to uppercase. If the encryption algorithm type is GCM-AES-128 or GCM-AES-XPN-128, the length must be 32 hexadecimal characters. If the encryption algorithm type is GCM-AES-256 or GCM-AES-XPN-256, the length must be 64 hexadecimal characters.
        # 
        # This parameter is required.
        self.ckn = ckn
        # The ID of the Express Connect circuit.
        # 
        # This parameter is required.
        self.physical_connection_id = physical_connection_id
        # The region ID of the Express Connect circuit.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/448570.html) operation to query region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cak is not None:
            result['Cak'] = self.cak

        if self.cipher_suite is not None:
            result['CipherSuite'] = self.cipher_suite

        if self.ckn is not None:
            result['Ckn'] = self.ckn

        if self.physical_connection_id is not None:
            result['PhysicalConnectionId'] = self.physical_connection_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cak') is not None:
            self.cak = m.get('Cak')

        if m.get('CipherSuite') is not None:
            self.cipher_suite = m.get('CipherSuite')

        if m.get('Ckn') is not None:
            self.ckn = m.get('Ckn')

        if m.get('PhysicalConnectionId') is not None:
            self.physical_connection_id = m.get('PhysicalConnectionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

