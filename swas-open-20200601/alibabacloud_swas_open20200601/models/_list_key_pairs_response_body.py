# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class ListKeyPairsResponseBody(DaraModel):
    def __init__(
        self,
        key_pairs: List[main_models.ListKeyPairsResponseBodyKeyPairs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The collection of key pair information.
        self.key_pairs = key_pairs
        # The current page number.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of key pairs.
        self.total_count = total_count

    def validate(self):
        if self.key_pairs:
            for v1 in self.key_pairs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KeyPairs'] = []
        if self.key_pairs is not None:
            for k1 in self.key_pairs:
                result['KeyPairs'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.key_pairs = []
        if m.get('KeyPairs') is not None:
            for k1 in m.get('KeyPairs'):
                temp_model = main_models.ListKeyPairsResponseBodyKeyPairs()
                self.key_pairs.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListKeyPairsResponseBodyKeyPairs(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        instance_ids: List[str] = None,
        key_pair_name: str = None,
        public_key: str = None,
    ):
        # The time when the key pair was created. The time follows the UTC (Z) time zone and is in the YYYY-MM-DDThh:mmZ format.
        self.creation_time = creation_time
        # The IDs of the simple application server instances. A maximum of 50 instance IDs are supported.
        self.instance_ids = instance_ids
        # The name of the key pair. The name must be 2 to 64 characters in length and can contain letters and Chinese characters. It must start with an uppercase or lowercase letter or a Chinese character, and cannot start with http:// or https://. It can contain digits, colons (:), underscores (_), or hyphens (-).
        self.key_pair_name = key_pair_name
        # The content of the public key.
        self.public_key = public_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.public_key is not None:
            result['PublicKey'] = self.public_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')

        return self

