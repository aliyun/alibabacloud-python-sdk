# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetOssBucketScanStatisticRequest(DaraModel):
    def __init__(
        self,
        bucket_name_list: List[str] = None,
    ):
        self.bucket_name_list = bucket_name_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name_list is not None:
            result['BucketNameList'] = self.bucket_name_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketNameList') is not None:
            self.bucket_name_list = m.get('BucketNameList')

        return self

