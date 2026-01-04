# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeKeyPairsRequest(DaraModel):
    def __init__(
        self,
        key_pair_id: str = None,
        key_pair_name: str = None,
        page_number: str = None,
        page_size: str = None,
    ):
        # The ID of the key pair.
        self.key_pair_id = key_pair_id
        # The name of the key pair that you want to bind to the simple application server. The name must be 2 to 128 characters in length. The name must start with a letter but cannot start with `http://` or `https://`. The name can contain the following characters:
        # 
        # *   Numbers.
        # *   :
        # *   _
        # *   .
        # 
        # You can specify only one name. By default, all key pairs are queried.
        self.key_pair_name = key_pair_name
        # The page number of the returned page. Valid values: integers that are greater than 0. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: integers that are greater than 0. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

