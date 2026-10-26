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
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The ID of the cloud disk. You can call the [DescribeDisks](https://help.aliyun.com/document_detail/25514.html) operation to query the ID of the cloud disk.
        # 
        # This parameter is required.
        self.disk_id = disk_id
        # The new capacity of the cloud disk. Unit: GiB. Valid values:
        # - System cloud disk:
        #   - Basic cloud disk: 20 to 500.
        #   - ESSD:
        #     - PL0: 1 to 2048.
        #     - PL1: 20 to 2048.
        #     - PL2: 461 to 2048.
        #     - PL3: 1261 to 2048.
        #   - ESSD AutoPL disk: 1 to 2048.
        #   - Other cloud disk types: 20 to 2048.
        # 
        # - Data cloud disk:
        #     - Ultra cloud disk (cloud_efficiency): 20 to 32768.
        #     - Standard SSD (cloud_ssd): 20 to 32768.
        #     - ESSD (cloud_essd): The valid values vary based on the `PerformanceLevel` parameter. You can call the [DescribeDisks](https://help.aliyun.com/document_detail/25514.html) operation to query the cloud disk information and check the valid values based on the `PerformanceLevel` parameter in the response.
        #         - PL0: 1 to 65536.
        #         - PL1: 20 to 65536.
        #         - PL2: 461 to 65536.
        #         - PL3: 1261 to 65536.
        #     - Basic cloud disk (cloud): 5 to 2000.
        #     - ESSD AutoPL disk (cloud_auto): 1 to 65536.
        # <props="china">
        #     - ESSD Entry disk (cloud_essd_entry): 10 to 32768.
        # 
        #   - Standard elastic ephemeral disk (elastic_ephemeral_disk_standard): 64 to 8192.
        #   - Premium elastic ephemeral disk (elastic_ephemeral_disk_premium): 64 to 8192.
        # 
        # > The new capacity must be greater than the original capacity. Otherwise, an error is returned when you call this operation.
        # 
        # This parameter is required.
        self.new_size = new_size
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The method used to resize the cloud disk. Valid values:
        # 
        # - offline: offline resizing. This is the default value. After the cloud disk is resized, you must [restart the instance](https://help.aliyun.com/document_detail/25440.html) in the console or call the [RebootInstance](https://help.aliyun.com/document_detail/25502.html) operation for the resize to take effect.
        #  
        # - online: online resizing. The cloud disk is resized without the need to restart the instance. This value supports ultra cloud disks, standard SSDs, ESSDs, and elastic ephemeral disks.
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

