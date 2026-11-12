# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class CreateDiskRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        disk_name: str = None,
        encrypted: bool = None,
        ens_region_id: str = None,
        instance_billing_cycle: str = None,
        instance_charge_type: str = None,
        kmskey_id: str = None,
        size: str = None,
        snapshot_id: str = None,
        tag: List[main_models.CreateDiskRequestTag] = None,
    ):
        # The category of the cloud disk. Valid values:
        # 
        # - cloud_efficiency: ultra disk
        # - cloud_ssd: all-flash disk
        # 
        # This parameter is required.
        self.category = category
        # The name of the cloud disk.
        self.disk_name = disk_name
        # Specifies whether to encrypt the cloud disk. Valid values:
        # 
        # - **true**: yes
        # 
        # - **false** (default): no
        self.encrypted = encrypted
        # The edge zone ID.
        # 
        # This parameter is required.
        self.ens_region_id = ens_region_id
        # The billing cycle of the instance. Valid values: Hour, Day, and Month.
        self.instance_billing_cycle = instance_billing_cycle
        # The billing method of the instance. Only **PostPaid** (pay-as-you-go) is supported.
        # 
        # This parameter is required.
        self.instance_charge_type = instance_charge_type
        # The ID of the Key Management Service (KMS) key used for the cloud disk.
        # 
        # > If **Encrypted** is set to **true** and **KMSKeyId** is left empty, the default service key is used.
        self.kmskey_id = kmskey_id
        # The size of the cloud disk. Unit: GiB.
        self.size = size
        # The ID of the snapshot used to create the cloud disk.
        # 
        # The **SnapshotId** and **Size** parameters are subject to the following limits:
        # 
        # - If snapshot size of the snapshot specified by **SnapshotId** is greater than the value of **Size**, snapshot size of the created cloud disk is equal to snapshot size of the snapshot.
        # 
        # - If snapshot size of the snapshot specified by **SnapshotId** is less than the value of **Size**, snapshot size of the created cloud disk is equal to the value of **Size**.
        self.snapshot_id = snapshot_id
        # The list of tags. You can add up to 20 tags in a single call.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.disk_name is not None:
            result['DiskName'] = self.disk_name

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.instance_billing_cycle is not None:
            result['InstanceBillingCycle'] = self.instance_billing_cycle

        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type

        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id

        if self.size is not None:
            result['Size'] = self.size

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('InstanceBillingCycle') is not None:
            self.instance_billing_cycle = m.get('InstanceBillingCycle')

        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')

        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateDiskRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateDiskRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N for the instance. Valid values of N: **1** to **20**.
        # 
        # - The key cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
        # - The key can be up to 64 characters in length.
        # - The key cannot be an empty string.
        self.key = key
        # The value of tag N for the topic. **Key** and **Value** must be both specified or both left empty. If both are specified, the system filters topics that match the tag. If neither is specified, the system queries all topics.
        # 
        # - Valid values of N: 1 to 20.
        # - The value can be an empty string.
        # - The value can be up to 128 characters in length, and cannot start with `aliyun` or `acs:`, or contain `http://` or `https://`.
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

