# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListKeyPairsRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        key_pair_name: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. Generate a unique value for this parameter from your client to ensure that different requests use unique values. ClientToken supports only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The name of the key pair. The name must be 2 to 64 characters in length and can contain letters and Chinese characters. It must start with an uppercase or lowercase letter or a Chinese character, and cannot start with http:// or https://. It can contain digits, colons (:), underscores (_), or hyphens (-).
        self.key_pair_name = key_pair_name
        # The page number of the key pair list. Minimum value: 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The region ID. You can call [ListRegions](https://help.aliyun.com/document_detail/189315.html) to query available regions.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

