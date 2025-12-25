# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class KMSConfig(DaraModel):
    def __init__(
        self,
        kms_instance_id: str = None,
        kms_key_id: str = None,
    ):
        self.kms_instance_id = kms_instance_id
        self.kms_key_id = kms_key_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kms_instance_id is not None:
            result['kmsInstanceId'] = self.kms_instance_id

        if self.kms_key_id is not None:
            result['kmsKeyId'] = self.kms_key_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kmsInstanceId') is not None:
            self.kms_instance_id = m.get('kmsInstanceId')

        if m.get('kmsKeyId') is not None:
            self.kms_key_id = m.get('kmsKeyId')

        return self

