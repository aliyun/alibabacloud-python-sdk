# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_kms20160120 import models as main_models
from darabonba.model import DaraModel

class GetKmsInstanceQuotaInfosResponseBody(DaraModel):
    def __init__(
        self,
        kms_instance_id: str = None,
        kms_instance_quota_infos: List[main_models.GetKmsInstanceQuotaInfosResponseBodyKmsInstanceQuotaInfos] = None,
        request_id: str = None,
    ):
        # The ID of the KMS instance.
        self.kms_instance_id = kms_instance_id
        # An array of quota details for the instance.
        self.kms_instance_quota_infos = kms_instance_quota_infos
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.kms_instance_quota_infos:
            for v1 in self.kms_instance_quota_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kms_instance_id is not None:
            result['KmsInstanceId'] = self.kms_instance_id

        result['KmsInstanceQuotaInfos'] = []
        if self.kms_instance_quota_infos is not None:
            for k1 in self.kms_instance_quota_infos:
                result['KmsInstanceQuotaInfos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KmsInstanceId') is not None:
            self.kms_instance_id = m.get('KmsInstanceId')

        self.kms_instance_quota_infos = []
        if m.get('KmsInstanceQuotaInfos') is not None:
            for k1 in m.get('KmsInstanceQuotaInfos'):
                temp_model = main_models.GetKmsInstanceQuotaInfosResponseBodyKmsInstanceQuotaInfos()
                self.kms_instance_quota_infos.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetKmsInstanceQuotaInfosResponseBodyKmsInstanceQuotaInfos(DaraModel):
    def __init__(
        self,
        resource_quota: int = None,
        resource_type: str = None,
        used_quantity: int = None,
    ):
        # The quota.
        self.resource_quota = resource_quota
        # The resource type.
        self.resource_type = resource_type
        # The quota usage.
        self.used_quantity = used_quantity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_quota is not None:
            result['ResourceQuota'] = self.resource_quota

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.used_quantity is not None:
            result['UsedQuantity'] = self.used_quantity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceQuota') is not None:
            self.resource_quota = m.get('ResourceQuota')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('UsedQuantity') is not None:
            self.used_quantity = m.get('UsedQuantity')

        return self

