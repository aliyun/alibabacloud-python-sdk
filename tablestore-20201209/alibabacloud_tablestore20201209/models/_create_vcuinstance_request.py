# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_tablestore20201209 import models as main_models
from darabonba.model import DaraModel

class CreateVCUInstanceRequest(DaraModel):
    def __init__(
        self,
        alias_name: str = None,
        auto_renew_period_in_month: int = None,
        cluster_type: str = None,
        dry_run: bool = None,
        enable_auto_renew: bool = None,
        enable_elastic_vcu: bool = None,
        instance_description: str = None,
        period_in_month: int = None,
        resource_group_id: str = None,
        tags: List[main_models.CreateVCUInstanceRequestTags] = None,
        vcu: int = None,
    ):
        self.alias_name = alias_name
        self.auto_renew_period_in_month = auto_renew_period_in_month
        # cluster type
        # 
        # This parameter is required.
        self.cluster_type = cluster_type
        self.dry_run = dry_run
        self.enable_auto_renew = enable_auto_renew
        self.enable_elastic_vcu = enable_elastic_vcu
        self.instance_description = instance_description
        # This parameter is required.
        self.period_in_month = period_in_month
        # resource group id
        self.resource_group_id = resource_group_id
        # tag
        self.tags = tags
        # This parameter is required.
        self.vcu = vcu

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name

        if self.auto_renew_period_in_month is not None:
            result['AutoRenewPeriodInMonth'] = self.auto_renew_period_in_month

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.enable_auto_renew is not None:
            result['EnableAutoRenew'] = self.enable_auto_renew

        if self.enable_elastic_vcu is not None:
            result['EnableElasticVCU'] = self.enable_elastic_vcu

        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description

        if self.period_in_month is not None:
            result['PeriodInMonth'] = self.period_in_month

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.vcu is not None:
            result['VCU'] = self.vcu

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')

        if m.get('AutoRenewPeriodInMonth') is not None:
            self.auto_renew_period_in_month = m.get('AutoRenewPeriodInMonth')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EnableAutoRenew') is not None:
            self.enable_auto_renew = m.get('EnableAutoRenew')

        if m.get('EnableElasticVCU') is not None:
            self.enable_elastic_vcu = m.get('EnableElasticVCU')

        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')

        if m.get('PeriodInMonth') is not None:
            self.period_in_month = m.get('PeriodInMonth')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateVCUInstanceRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VCU') is not None:
            self.vcu = m.get('VCU')

        return self

class CreateVCUInstanceRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.key = key
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

