# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeKeyPairsResponseBody(DaraModel):
    def __init__(
        self,
        key_pairs: main_models.DescribeKeyPairsResponseBodyKeyPairs = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about the key pairs.
        self.key_pairs = key_pairs
        # The page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of key pairs.
        self.total_count = total_count

    def validate(self):
        if self.key_pairs:
            self.key_pairs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_pairs is not None:
            result['KeyPairs'] = self.key_pairs.to_map()

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
        if m.get('KeyPairs') is not None:
            temp_model = main_models.DescribeKeyPairsResponseBodyKeyPairs()
            self.key_pairs = temp_model.from_map(m.get('KeyPairs'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeKeyPairsResponseBodyKeyPairs(DaraModel):
    def __init__(
        self,
        key_pair: List[main_models.DescribeKeyPairsResponseBodyKeyPairsKeyPair] = None,
    ):
        self.key_pair = key_pair

    def validate(self):
        if self.key_pair:
            for v1 in self.key_pair:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KeyPair'] = []
        if self.key_pair is not None:
            for k1 in self.key_pair:
                result['KeyPair'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.key_pair = []
        if m.get('KeyPair') is not None:
            for k1 in m.get('KeyPair'):
                temp_model = main_models.DescribeKeyPairsResponseBodyKeyPairsKeyPair()
                self.key_pair.append(temp_model.from_map(k1))

        return self

class DescribeKeyPairsResponseBodyKeyPairsKeyPair(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        key_pair_finger_print: str = None,
        key_pair_id: str = None,
        key_pair_name: str = None,
    ):
        # The time when the key pair was created. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The fingerprint of the key pair.
        self.key_pair_finger_print = key_pair_finger_print
        # The ID of the key pair.
        self.key_pair_id = key_pair_id
        # The name of the SSH key pair.
        self.key_pair_name = key_pair_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.key_pair_finger_print is not None:
            result['KeyPairFingerPrint'] = self.key_pair_finger_print

        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('KeyPairFingerPrint') is not None:
            self.key_pair_finger_print = m.get('KeyPairFingerPrint')

        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        return self

