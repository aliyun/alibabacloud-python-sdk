# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class QuotaTopo(DaraModel):
    def __init__(
        self,
        depth: str = None,
        parent_quota_id: str = None,
        quota_details: main_models.QuotaDetails = None,
        quota_id: str = None,
        quota_name: str = None,
        resource_type: str = None,
        workload_details: main_models.WorkloadDetails = None,
    ):
        self.depth = depth
        self.parent_quota_id = parent_quota_id
        self.quota_details = quota_details
        self.quota_id = quota_id
        self.quota_name = quota_name
        self.resource_type = resource_type
        self.workload_details = workload_details

    def validate(self):
        if self.quota_details:
            self.quota_details.validate()
        if self.workload_details:
            self.workload_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.depth is not None:
            result['Depth'] = self.depth

        if self.parent_quota_id is not None:
            result['ParentQuotaId'] = self.parent_quota_id

        if self.quota_details is not None:
            result['QuotaDetails'] = self.quota_details.to_map()

        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id

        if self.quota_name is not None:
            result['QuotaName'] = self.quota_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.workload_details is not None:
            result['WorkloadDetails'] = self.workload_details.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Depth') is not None:
            self.depth = m.get('Depth')

        if m.get('ParentQuotaId') is not None:
            self.parent_quota_id = m.get('ParentQuotaId')

        if m.get('QuotaDetails') is not None:
            temp_model = main_models.QuotaDetails()
            self.quota_details = temp_model.from_map(m.get('QuotaDetails'))

        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')

        if m.get('QuotaName') is not None:
            self.quota_name = m.get('QuotaName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('WorkloadDetails') is not None:
            temp_model = main_models.WorkloadDetails()
            self.workload_details = temp_model.from_map(m.get('WorkloadDetails'))

        return self

