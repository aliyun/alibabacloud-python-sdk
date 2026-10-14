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
        # The type of the cloud disk. Valid values:
        # 
        # This parameter is required.
        self.category = category
        # The name of the cloud disk.
        self.disk_name = disk_name
        # Specifies whether to encrypt the cloud disk. Valid values:
        self.encrypted = encrypted
        # The edge zone ID.
        # 
        # This parameter is required.
        self.ens_region_id = ens_region_id
        # The billing cycle of the instance. Valid values: Hour, Day, Month.
        self.instance_billing_cycle = instance_billing_cycle
        # The billing method of the instance. Currently, only **PostPaid** (pay-as-you-go) is supported.
        # 
        # This parameter is required.
        self.instance_charge_type = instance_charge_type
        # The ID of the KMS key used by the cloud disk.
        self.kmskey_id = kmskey_id
        # The size of the cloud disk. Unit: GiB.
        self.size = size
        # The snapshot used to create the cloud disk.
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
        # The tag key of the instance. Valid values of N: **1** to **20**.
        self.key = key
        # The tag value of the topic. **Key** and **Value** must be specified or left empty at the same time. If both are specified, topics are filtered by the tag. If neither is specified, all topics are queried.
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

