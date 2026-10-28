# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_kvcachestore20260617 import models as main_models
from darabonba.model import DaraModel

class ListKVCacheStoreAvailableVscsRequest(DaraModel):
    def __init__(
        self,
        arns: List[main_models.ListKVCacheStoreAvailableVscsRequestArns] = None,
        instance_id: str = None,
        instance_type: str = None,
        kvcs_id: str = None,
        region_id: str = None,
    ):
        # The cross-account authorization role chain, used for cross-account VSC queries in ECS or EFLO scenarios.
        self.arns = arns
        # The compute instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The compute instance type. Valid values:
        # - ECS
        # - EFLO
        # 
        # This parameter is required.
        self.instance_type = instance_type
        # The KVCacheStore instance ID.
        # 
        # This parameter is required.
        self.kvcs_id = kvcs_id
        # The region ID, such as cn-hangzhou.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.arns:
            for v1 in self.arns:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Arns'] = []
        if self.arns is not None:
            for k1 in self.arns:
                result['Arns'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.kvcs_id is not None:
            result['KvcsId'] = self.kvcs_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.arns = []
        if m.get('Arns') is not None:
            for k1 in m.get('Arns'):
                temp_model = main_models.ListKVCacheStoreAvailableVscsRequestArns()
                self.arns.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('KvcsId') is not None:
            self.kvcs_id = m.get('KvcsId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class ListKVCacheStoreAvailableVscsRequestArns(DaraModel):
    def __init__(
        self,
        assume_role_for: str = None,
        role_arn: str = None,
        role_type: str = None,
    ):
        # The target UID for role assumption.
        # 
        # This parameter is required.
        self.assume_role_for = assume_role_for
        # The ARN of the RAM role.
        # 
        # This parameter is required.
        self.role_arn = role_arn
        # The role type. Valid values:
        # - service
        # - user
        # 
        # This parameter is required.
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assume_role_for is not None:
            result['AssumeRoleFor'] = self.assume_role_for

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeRoleFor') is not None:
            self.assume_role_for = m.get('AssumeRoleFor')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

