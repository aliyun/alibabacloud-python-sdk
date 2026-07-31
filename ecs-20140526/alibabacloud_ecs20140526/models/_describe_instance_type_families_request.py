# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInstanceTypeFamiliesRequest(DaraModel):
    def __init__(
        self,
        generation: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The generation of instance families. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html). Valid values:
        # 
        # - ecs-1: Series I instance family. These were among the first to go online and are cost-effective.
        # 
        # - ecs-2: Series II instance family. This family features a second hardware and software upgrade with enhanced instance performance.
        # 
        # - ecs-3: Series III instance family. This family delivers excellent performance and can handle various workload requirements.
        # 
        # - ecs-4: Series IV instance family. This family includes common enterprise-level instance types (such as g5, c5, and r5), ECS Bare Metal instance types (such as ebmc5s, ebmg5s, and ebmr5s), and burstable instance types (such as t5). They provide strong scenario adaptability, can handle massive popular workloads, and deliver lower latency.
        # 
        # - ecs-5: Series V instance family. This family includes common enterprise-level instance types (such as g6, c6, and r6), ECS Bare Metal instance types (such as ebmg6, ebmg6e, and ebmc6), and storage-enhanced instance family types (such as g6e). They deliver faster response times and superior performance.
        # 
        # - ecs-6: Series VI instance family. This family includes enterprise-level instance types (such as hfc7, hfg7, and hfr7) and ECS Bare Metal instance types (such as ebmhfg7). This series of instance families is in invitational preview.
        self.generation = generation
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.generation is not None:
            result['Generation'] = self.generation

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Generation') is not None:
            self.generation = m.get('Generation')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

