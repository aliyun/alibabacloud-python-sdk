# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperateBucketScanTaskRequest(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        operate_code: int = None,
    ):
        self.bucket_name = bucket_name
        self.operate_code = operate_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.operate_code is not None:
            result['OperateCode'] = self.operate_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('OperateCode') is not None:
            self.operate_code = m.get('OperateCode')

        return self

