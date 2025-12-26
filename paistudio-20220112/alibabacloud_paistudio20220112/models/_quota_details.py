# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class QuotaDetails(DaraModel):
    def __init__(
        self,
        actual_min_quota: main_models.ResourceAmount = None,
        allocatable_quota: main_models.ResourceAmount = None,
        allocated_quota: main_models.ResourceAmount = None,
        ancestors_allocated_quota: main_models.ResourceAmount = None,
        descendants_allocated_quota: main_models.ResourceAmount = None,
        desired_min_quota: main_models.ResourceAmount = None,
        requested_quota: main_models.ResourceAmount = None,
        self_allocated_quota: main_models.ResourceAmount = None,
        self_submitted_quota: main_models.ResourceAmount = None,
        system_reserved_quota: main_models.ResourceAmount = None,
        used_quota: main_models.ResourceAmount = None,
    ):
        self.actual_min_quota = actual_min_quota
        self.allocatable_quota = allocatable_quota
        self.allocated_quota = allocated_quota
        self.ancestors_allocated_quota = ancestors_allocated_quota
        self.descendants_allocated_quota = descendants_allocated_quota
        self.desired_min_quota = desired_min_quota
        self.requested_quota = requested_quota
        self.self_allocated_quota = self_allocated_quota
        self.self_submitted_quota = self_submitted_quota
        self.system_reserved_quota = system_reserved_quota
        self.used_quota = used_quota

    def validate(self):
        if self.actual_min_quota:
            self.actual_min_quota.validate()
        if self.allocatable_quota:
            self.allocatable_quota.validate()
        if self.allocated_quota:
            self.allocated_quota.validate()
        if self.ancestors_allocated_quota:
            self.ancestors_allocated_quota.validate()
        if self.descendants_allocated_quota:
            self.descendants_allocated_quota.validate()
        if self.desired_min_quota:
            self.desired_min_quota.validate()
        if self.requested_quota:
            self.requested_quota.validate()
        if self.self_allocated_quota:
            self.self_allocated_quota.validate()
        if self.self_submitted_quota:
            self.self_submitted_quota.validate()
        if self.system_reserved_quota:
            self.system_reserved_quota.validate()
        if self.used_quota:
            self.used_quota.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_min_quota is not None:
            result['ActualMinQuota'] = self.actual_min_quota.to_map()

        if self.allocatable_quota is not None:
            result['AllocatableQuota'] = self.allocatable_quota.to_map()

        if self.allocated_quota is not None:
            result['AllocatedQuota'] = self.allocated_quota.to_map()

        if self.ancestors_allocated_quota is not None:
            result['AncestorsAllocatedQuota'] = self.ancestors_allocated_quota.to_map()

        if self.descendants_allocated_quota is not None:
            result['DescendantsAllocatedQuota'] = self.descendants_allocated_quota.to_map()

        if self.desired_min_quota is not None:
            result['DesiredMinQuota'] = self.desired_min_quota.to_map()

        if self.requested_quota is not None:
            result['RequestedQuota'] = self.requested_quota.to_map()

        if self.self_allocated_quota is not None:
            result['SelfAllocatedQuota'] = self.self_allocated_quota.to_map()

        if self.self_submitted_quota is not None:
            result['SelfSubmittedQuota'] = self.self_submitted_quota.to_map()

        if self.system_reserved_quota is not None:
            result['SystemReservedQuota'] = self.system_reserved_quota.to_map()

        if self.used_quota is not None:
            result['UsedQuota'] = self.used_quota.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualMinQuota') is not None:
            temp_model = main_models.ResourceAmount()
            self.actual_min_quota = temp_model.from_map(m.get('ActualMinQuota'))

        if m.get('AllocatableQuota') is not None:
            temp_model = main_models.ResourceAmount()
            self.allocatable_quota = temp_model.from_map(m.get('AllocatableQuota'))

        if m.get('AllocatedQuota') is not None:
            temp_model = main_models.ResourceAmount()
            self.allocated_quota = temp_model.from_map(m.get('AllocatedQuota'))

        if m.get('AncestorsAllocatedQuota') is not None:
            temp_model = main_models.ResourceAmount()
            self.ancestors_allocated_quota = temp_model.from_map(m.get('AncestorsAllocatedQuota'))

        if m.get('DescendantsAllocatedQuota') is not None:
            temp_model = main_models.ResourceAmount()
            self.descendants_allocated_quota = temp_model.from_map(m.get('DescendantsAllocatedQuota'))

        if m.get('DesiredMinQuota') is not None:
            temp_model = main_models.ResourceAmount()
            self.desired_min_quota = temp_model.from_map(m.get('DesiredMinQuota'))

        if m.get('RequestedQuota') is not None:
            temp_model = main_models.ResourceAmount()
            self.requested_quota = temp_model.from_map(m.get('RequestedQuota'))

        if m.get('SelfAllocatedQuota') is not None:
            temp_model = main_models.ResourceAmount()
            self.self_allocated_quota = temp_model.from_map(m.get('SelfAllocatedQuota'))

        if m.get('SelfSubmittedQuota') is not None:
            temp_model = main_models.ResourceAmount()
            self.self_submitted_quota = temp_model.from_map(m.get('SelfSubmittedQuota'))

        if m.get('SystemReservedQuota') is not None:
            temp_model = main_models.ResourceAmount()
            self.system_reserved_quota = temp_model.from_map(m.get('SystemReservedQuota'))

        if m.get('UsedQuota') is not None:
            temp_model = main_models.ResourceAmount()
            self.used_quota = temp_model.from_map(m.get('UsedQuota'))

        return self

