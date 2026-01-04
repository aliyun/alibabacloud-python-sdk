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
        # The category of the disk. Valid values:
        # 
        # *   cloud_efficiency: ultra disk.
        # *   cloud_ssd: all-flash disk.
        # 
        # This parameter is required.
        self.category = category
        # The name of the disk.
        self.disk_name = disk_name
        # Specifies whether to encrypt the new system disk. Valid values:
        # 
        # *   **true**
        # *   **false** (default): no
        self.encrypted = encrypted
        # The ID of the edge node.
        # 
        # This parameter is required.
        self.ens_region_id = ens_region_id
        self.instance_billing_cycle = instance_billing_cycle
        # The billing method of the instance. Set the value to **PostPaid**.
        # 
        # This parameter is required.
        self.instance_charge_type = instance_charge_type
        # The ID of the Key Management Service (KMS) key that is used by the cloud disk.
        # 
        # >  If you set the **Encrypted** parameter to **true**, the default service key is used when the **KMSKeyId** parameter is empty.
        self.kmskey_id = kmskey_id
        # The size of the disk. Unit: GiB.
        self.size = size
        # The ID of the snapshot that you want to use to create the disk.
        # 
        # The following limits apply to the **SnapshotId** and **Size** parameters:
        # 
        # *   If the size of the snapshot specified by **SnapshotId** is greater than the specified **Size** value, the size of the created disk is equal to the specified snapshot size.
        # *   If the size of the snapshot specified by **SnapshotId** is smaller than the specified **Size** value, the size of the created disk is equal to the specified **Size** value.
        self.snapshot_id = snapshot_id
        # The tags of the instance. You can specify at most 20 tags in each call.
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
        # The key of the tag. Valid values of N: **1** to **20**.
        # 
        # *   The key cannot start with `aliyun`, `acs:`, `http://`, or `https://`.
        # *   The key must be up to 64 characters in length.
        # *   The tag key cannot be an empty string.
        self.key = key
        # The value of a tag that is attached to the topics you want to query. This parameter is not required. If you configure this parameter, you must also configure the **Key** parameter.**** If you include the Key and Value parameters in a request, this operation queries only the topics that use the specified tags. If you do not include these parameters in a request, this operation queries all topics that you can access.
        # 
        # *   Valid values: 1 to 20.
        # *   The value of this parameter can be an empty string.
        # *   The tag value can be up to 128 characters in length. It cannot start with aliyun or acs: and cannot contain http:// or https://.
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

