# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class DescribePatternTypesResponseBody(DaraModel):
    def __init__(
        self,
        pattern_types: List[main_models.DescribePatternTypesResponseBodyPatternTypes] = None,
        request_id: str = None,
    ):
        # The instance types that meet the specified requirements.
        self.pattern_types = pattern_types
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.pattern_types:
            for v1 in self.pattern_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PatternTypes'] = []
        if self.pattern_types is not None:
            for k1 in self.pattern_types:
                result['PatternTypes'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pattern_types = []
        if m.get('PatternTypes') is not None:
            for k1 in m.get('PatternTypes'):
                temp_model = main_models.DescribePatternTypesResponseBodyPatternTypes()
                self.pattern_types.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePatternTypesResponseBodyPatternTypes(DaraModel):
    def __init__(
        self,
        cores: int = None,
        instance_family_level: str = None,
        instance_type: str = None,
        instance_type_family: str = None,
        memory: float = None,
    ):
        # The number of vCPUs that are assigned to the instance type.
        self.cores = cores
        # The level of the instance family.
        # 
        # *   EntryLevel: entry level (shared instance types) Instance types of this level are the most cost-effective but may not provide stable computing performance. Instance types of this level are suitable for business scenarios in which the CPU utilization is low. For more information, see [Shared instance families](https://help.aliyun.com/document_detail/108489.html).
        # *   EnterpriseLevel: enterprise level. Instance types of this level provide stable performance and dedicated resources and are suitable for scenarios that require high stability. For more information, see [Overview of instance families](https://help.aliyun.com/document_detail/25378.html).
        # *   CreditEntryLevel: credit-based entry level (burstable instance types). CPU credits are used to ensure computing performance. Instance types of this level are suitable for scenarios in which the CPU utilization is low but may fluctuate in specific cases. For more information, see [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html).
        self.instance_family_level = instance_family_level
        # The name of the instance type.
        self.instance_type = instance_type
        # The instance family.
        self.instance_type_family = instance_type_family
        # The memory size that are assigned to the instance type. Unit: GiB.
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cores is not None:
            result['Cores'] = self.cores

        if self.instance_family_level is not None:
            result['InstanceFamilyLevel'] = self.instance_family_level

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.instance_type_family is not None:
            result['InstanceTypeFamily'] = self.instance_type_family

        if self.memory is not None:
            result['Memory'] = self.memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')

        if m.get('InstanceFamilyLevel') is not None:
            self.instance_family_level = m.get('InstanceFamilyLevel')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InstanceTypeFamily') is not None:
            self.instance_type_family = m.get('InstanceTypeFamily')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        return self

