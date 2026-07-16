# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetKmsInstanceRequest(DaraModel):
    def __init__(
        self,
        kms_instance_id: str = None,
    ):
        # The ID of the KMS instance to query.
        # 
        # This parameter is required.
        self.kms_instance_id = kms_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kms_instance_id is not None:
            result['KmsInstanceId'] = self.kms_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KmsInstanceId') is not None:
            self.kms_instance_id = m.get('KmsInstanceId')

        return self

