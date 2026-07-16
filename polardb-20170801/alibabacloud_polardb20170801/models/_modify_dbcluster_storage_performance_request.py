# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBClusterStoragePerformanceRequest(DaraModel):
    def __init__(
        self,
        auto_use_coupon: bool = None,
        bursting_enabled: str = None,
        client_token: str = None,
        dbcluster_id: str = None,
        modify_type: str = None,
        promotion_code: str = None,
        provisioned_iops: int = None,
        resource_owner_id: int = None,
        storage_type: str = None,
    ):
        self.auto_use_coupon = auto_use_coupon
        # Specifies if the I/O performance burst feature is enabled for an ESSD AutoPL disk. Valid values:
        # 
        # - **true**: Enabled
        # 
        # - **false**: Disabled (Default)
        # 
        # > This parameter applies only when StorageType is set to ESSDAUTOPL.
        self.bursting_enabled = bursting_enabled
        # A client-generated token that ensures request idempotence. The token must be unique for each request. It is case-sensitive and can be up to 64 ASCII characters long.
        self.client_token = client_token
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The modification type. Valid values:
        # 
        # - **Upgrade**: Upgrades the storage performance.
        # 
        # - **Downgrade**: Downgrades the storage performance.
        self.modify_type = modify_type
        self.promotion_code = promotion_code
        # <props="china">
        # 
        # Valid values: 0 to min{50,000, 1000 \\* capacity - baseline performance}.
        # 
        # 
        # 
        # <props="china">
        # 
        # Baseline performance = min{1,800 + 50 \\* capacity, 50,000}.
        # 
        # 
        # 
        # <props="china">
        # 
        # > This parameter applies only when StorageType is set to ESSDAUTOPL.
        self.provisioned_iops = provisioned_iops
        self.resource_owner_id = resource_owner_id
        # The target storage type. Valid values for Enterprise Edition:
        # 
        # - **PSL5**
        # 
        # - **PSL4**
        # 
        # Valid values for Standard Edition:
        # 
        # - **ESSDPL0**
        # 
        # - **ESSDPL1**
        # 
        # - **ESSDPL2**
        # 
        # - **ESSDPL3**
        # 
        # - **ESSDAUTOPL**
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_use_coupon is not None:
            result['AutoUseCoupon'] = self.auto_use_coupon

        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type

        if self.promotion_code is not None:
            result['PromotionCode'] = self.promotion_code

        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoUseCoupon') is not None:
            self.auto_use_coupon = m.get('AutoUseCoupon')

        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')

        if m.get('PromotionCode') is not None:
            self.promotion_code = m.get('PromotionCode')

        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

