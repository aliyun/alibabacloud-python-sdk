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
        owner_account: str = None,
        owner_id: int = None,
        period: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        shard_count: int = None,
    ):
        # Specifies whether to enable the auto-renewal feature. Valid values:
        # 
        # *   **true**: enables auto-renewal.
        # *   **false**: does not enable auto-renewal.
        self.auto_renew = auto_renew
        # The subscription duration that is supported by auto-renewal. Unit: month. Valid values: **1**, **2**, **3**, **6**, and **12**.
        # 
        # > This parameter is required if the **AutoRenew** parameter is set to **true**.
        self.auto_renew_period = auto_renew_period
        # The new billing method. Valid values:
        # 
        # *   **PostPaid:** pay-as-you-go
        # *   **PrePaid**: subscription. If you set this parameter to PrePaid, you must also specify the **Period** parameter.
        self.charge_type = charge_type
        # Specifies whether to perform a precheck before the system creates the instance. Valid values:
        # 
        # *   **true**: The system performs a dry run and does not create the cloud-native instance. The system prechecks the request parameters, request format, service limits, and available resources. If the request fails to pass the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false**: performs a dry run and sends the request. If the request passes the dry run, the instance is created.
        self.dry_run = dry_run
        # The time when a database switchover is performed after data is migrated. Valid values:
        # 
        # *   **Immediately**: A database switchover is performed immediately after data is migrated.
        # *   **MaintainTime**: A database switchover is performed during the maintenance window.
        # 
        # > Default value: Immediately.
        self.effective_time = effective_time
        # The database engine version of the instance. Valid values: **5.0**, **6.0**, and **7.0**.
        # 
        # This parameter is required.
        self.engine_version = engine_version
        # The instance specification of the cloud-native instance. For more information, see [Overview](https://help.aliyun.com/document_detail/26350.html).
        # 
        # This parameter is required.
        self.instance_class = instance_class
        # The ID of the instance that you want to convert.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The subscription duration of the instance. Unit: months. Valid values: **1**, 2, 3, 4, 5, 6, 7, 8, **9**, **12**, **24**, **36**.
        # 
        # > This parameter is available and required only if the **ChargeType** parameter is set to **PrePaid**.
        self.period = period
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The number of data shards in the cloud-native cluster instance.
        self.shard_count = shard_count

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

        if self.shard_count is not None:
            result['ShardCount'] = self.shard_count

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

        if m.get('ShardCount') is not None:
            self.shard_count = m.get('ShardCount')

        return self

