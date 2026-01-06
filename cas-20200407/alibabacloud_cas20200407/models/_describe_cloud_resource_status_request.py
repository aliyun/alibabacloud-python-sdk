# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCloudResourceStatusRequest(DaraModel):
    def __init__(
        self,
        secret_id: str = None,
    ):
        # The AccessKey secret used to access cloud resources.
        # 
        # >  You can call the [ListCloudAccess](https://help.aliyun.com/document_detail/2712219.html) operation to obtain the ID.
        self.secret_id = secret_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.secret_id is not None:
            result['SecretId'] = self.secret_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')

        return self

