# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetKmsInstanceQuotaInfosRequest(DaraModel):
    def __init__(
        self,
        kms_instance_id: str = None,
        resource_type: str = None,
    ):
        # The ID of the KMS instance to query.
        self.kms_instance_id = kms_instance_id
        # The resource type. Valid values:
        # 
        # - `key`: key quota
        # 
        # - `secret`: secret quota
        # 
        # - `qps`: queries per second (QPS) quota
        # 
        # - `vpc`: Virtual Private Cloud (VPC) quota
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kms_instance_id is not None:
            result['KmsInstanceId'] = self.kms_instance_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KmsInstanceId') is not None:
            self.kms_instance_id = m.get('KmsInstanceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

