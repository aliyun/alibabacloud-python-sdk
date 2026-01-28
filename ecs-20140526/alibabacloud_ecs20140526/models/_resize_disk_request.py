# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResizeDiskRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        disk_id: str = None,
        new_size: int = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        type: str = None,
    ):
        # The new disk capacity. Unit: GiB. Valid values:
        # 
        # *   For a system disk:
        # 
        #     *   Basic disk (cloud): 20 to 500.
        # 
        #     *   ESSD (cloud_essd): The valid values vary based on the performance level of the ESSD.
        # 
        #         *   PL0 ESSD: 1 to 2048.
        #         *   PL1 ESSD: 20 to 2048.
        #         *   PL2 ESSD: 461 to 2048.
        #         *   PL3 ESSD: 1261 to 2048.
        # 
        #     *   ESSD AutoPL disk: 1 to 2048.
        # 
        #     *   Other disk categories: 20 to 2048.
        # 
        # *   For a data disk:
        # 
        #     *   Ultra disk (cloud_efficiency): 20 to 32768.
        # 
        #     *   Standard SSD (cloud_ssd): 20 to 32768.
        # 
        #     *   ESSD (cloud_essd): The valid values vary based on the performance level of the ESSD.`` To query the performance level of an ESSD, call the [DescribeDisks](https://help.aliyun.com/document_detail/25514.html) operation to query disk information and check the `PerformanceLevel` value in the response.
        # 
        #         *   PL0 ESSD: 1 to 65536.
        #         *   PL1 ESSD: 20 to 65536.
        #         *   PL2 ESSD: 461 to 65536.
        #         *   PL3 ESSD: 1261 to 65536.
        # 
        #     *   Basic disk (cloud): 5 to 2000.
        # 
        #     *   ESSD AutoPL disk (cloud_auto): 1 to 65536.
        # 
        #     *   Standard elastic ephemeral disk (elastic_ephemeral_disk_standard): 64 to 8192.
        # 
        #     *   Premium elastic ephemeral disk (elastic_ephemeral_disk_premium): 64 to 8192.
        # 
        # >  The new disk capacity must be larger than the original disk capacity. Otherwise, an error is reported.
        self.client_token = client_token
        # The ID of the disk. You can call the [DescribeDisks](https://help.aliyun.com/document_detail/25514.html) operation to query available disk IDs.
        # 
        # This parameter is required.
        self.disk_id = disk_id
        # The new disk capacity. Unit: GiB. Valid values:
        # 
        # *   System disk:
        # 
        #     *   Basic disk (cloud): 20 to 500.
        # 
        #     *   ESSD (cloud_essd): The valid values vary based on the performance level of the ESSD.
        # 
        #         *   Valid values when SystemDisk.PerformanceLevel is set to PL0: 1 to 2048.
        #         *   Valid values when SystemDisk.PerformanceLevel is set to PL1: 20 to 2048.
        #         *   Valid values when SystemDisk.PerformanceLevel is set to PL2: 461 to 2048.
        #         *   Valid values when SystemDisk.PerformanceLevel is set to PL3: 1261 to 2048.
        # 
        #     *   ESSD AutoPL disk: 1 to 2048.
        # 
        #     *   Other disk categories: 20 to 2048.
        # 
        # *   Data disk:
        # 
        #     *   Ultra disk (cloud_efficiency): 20 to 32768.
        # 
        #     *   Standard SSD (cloud_ssd): 20 to 32768.
        # 
        #     *   ESSD (cloud_essd): The valid values vary based on the performance level of the ESSD.`` To query the performance level of an ESSD, call the [DescribeDisks](https://help.aliyun.com/document_detail/25514.html) operation to query disk information and check the `PerformanceLevel` value in the response.
        # 
        #         *   PL0 ESSD: 1 to 65536.
        #         *   PL1 ESSD: 20 to 65536.
        #         *   PL2 ESSD: 461 to 65536.
        #         *   PL3 ESSD: 1261 to 65536.
        # 
        #     *   Basic disk (cloud): 5 to 2000.
        # 
        #     *   ESSD AutoPL disk (cloud_auto): 1 to 65536.
        # 
        #     *   Standard elastic ephemeral disk (elastic_ephemeral_disk_standard): 64 to 8192.
        # 
        #     *   Premium elastic ephemeral disk (elastic_ephemeral_disk_premium): 64 to 8192.
        # 
        # >  The new disk capacity must be larger than the original disk capacity. Otherwise, an error is reported.
        # 
        # This parameter is required.
        self.new_size = new_size
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The method that you want to use to resize the disk. Valid values:
        # 
        # *   offline (default): resizes the disk offline. After resizing a disk offline, you must [restart the instance](https://help.aliyun.com/document_detail/25440.html) in the console or call an API operation [RebootInstance](https://help.aliyun.com/document_detail/25502.html) make the operation take effect.
        # *   online: resizes the disk online without the need to restart the instance. You can resize ultra disks, standard SSDs, ESSDs, and elastic ephemeral disks online.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.new_size is not None:
            result['NewSize'] = self.new_size

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('NewSize') is not None:
            self.new_size = m.get('NewSize')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

