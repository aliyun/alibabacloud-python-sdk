# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TransformToEcsRequest(DaraModel):
    def __init__(
        self,
        auto_renew: str = None,
        auto_renew_period: int = None,
        charge_type: str = None,
        dry_run: bool = None,
        effective_time: str = None,
        engine_version: str = None,
        instance_class: str = None,
        instance_id: str = None,
        is_across_zone: bool = None,
        iz_no: str = None,
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        secondary_iz_no: str = None,
        shard_count: int = None,
        v_switch_id: str = None,
    ):
        # Specifies whether to enable auto-renewal. Valid values:
        # 
        # * **true**: enabled.
        # * **false**: disabled.
        self.auto_renew = auto_renew
        # The auto-renewal period. Unit: months. Valid values: **1**, **2**, **3**, **6**, and **12**.
        # 
        # > This parameter is required when **AutoRenew** is set to **true**.
        self.auto_renew_period = auto_renew_period
        # The billing method to convert to. Valid values:
        # * **PostPaid**: pay-as-you-go.
        # * **PrePaid**: subscription. If you set this parameter to PrePaid, you must also specify the **Period** parameter.
        self.charge_type = charge_type
        # Specifies whether to perform a dry run for this operation. Valid values:
        # * **true**: performs a dry run without creating the cloud-native instance. The system checks items such as the request parameters, request format, service limits, and available inventory. If the check fails, the corresponding error is returned. If the check succeeds, the error code `DryRunOperation` is returned.
        # * **false** (default): sends the request. If the check succeeds, the instance is created.
        self.dry_run = dry_run
        # The time when the database switchover is performed after data migration. Valid values: 
        # * **Immediately**: The switchover is performed immediately after the migration is complete.
        # * **MaintainTime**: The switchover is performed during the maintenance window.
        # 
        # > Default value: **Immediately**.
        self.effective_time = effective_time
        # The Redis-compatible engine version of the instance. Valid values: **5.0**, **6.0**, and **7.0**.
        # 
        # This parameter is required.
        self.engine_version = engine_version
        # The instance type of the target cloud-native instance. For more information, see [Overview of instance specifications](https://help.aliyun.com/document_detail/26350.html).
        # 
        # > This is the description content.
        # > - For cluster instances, specify the corresponding cloud-native cluster instance type with .proxy, and specify the ShardCount parameter for the number of shards.
        # 
        # This parameter is required.
        self.instance_class = instance_class
        # The ID of the classic architecture instance to convert.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.is_across_zone = is_across_zone
        self.iz_no = iz_no
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The subscription duration. Unit: months. Valid values: **1** to **9**, **12**, **24**, and **36**.
        # > This parameter is available and required only when **ChargeType** is set to **PrePaid**.
        self.period = period
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.secondary_iz_no = secondary_iz_no
        # The number of data shard nodes in the cloud-native cluster instance.
        self.shard_count = shard_count
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_across_zone is not None:
            result['IsAcrossZone'] = self.is_across_zone

        if self.iz_no is not None:
            result['IzNo'] = self.iz_no

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.period is not None:
            result['Period'] = self.period

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.secondary_iz_no is not None:
            result['SecondaryIzNo'] = self.secondary_iz_no

        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsAcrossZone') is not None:
            self.is_across_zone = m.get('IsAcrossZone')

        if m.get('IzNo') is not None:
            self.iz_no = m.get('IzNo')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SecondaryIzNo') is not None:
            self.secondary_iz_no = m.get('SecondaryIzNo')

        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

