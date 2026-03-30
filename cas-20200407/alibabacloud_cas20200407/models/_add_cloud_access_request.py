# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddCloudAccessRequest(DaraModel):
    def __init__(
        self,
        cloud_name: str = None,
        secret_id: str = None,
        secret_key: str = None,
    ):
        self.cloud_name = cloud_name
        self.secret_id = secret_id
        self.secret_key = secret_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_name is not None:
            result['CloudName'] = self.cloud_name

        if self.secret_id is not None:
            result['SecretId'] = self.secret_id

        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudName') is not None:
            self.cloud_name = m.get('CloudName')

        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')

        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')

        return self

