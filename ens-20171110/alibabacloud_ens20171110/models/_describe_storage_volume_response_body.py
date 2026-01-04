# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeStorageVolumeResponseBody(DaraModel):
    def __init__(
        self,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        storage_volumes: List[main_models.DescribeStorageVolumeResponseBodyStorageVolumes] = None,
        total_count: str = None,
    ):
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The list of returned results.
        self.storage_volumes = storage_volumes
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.storage_volumes:
            for v1 in self.storage_volumes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['StorageVolumes'] = []
        if self.storage_volumes is not None:
            for k1 in self.storage_volumes:
                result['StorageVolumes'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.storage_volumes = []
        if m.get('StorageVolumes') is not None:
            for k1 in m.get('StorageVolumes'):
                temp_model = main_models.DescribeStorageVolumeResponseBodyStorageVolumes()
                self.storage_volumes.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeStorageVolumeResponseBodyStorageVolumes(DaraModel):
    def __init__(
        self,
        auth_protocol: str = None,
        creation_time: str = None,
        description: str = None,
        ens_region_id: str = None,
        is_auth: int = None,
        is_enable: int = None,
        status: str = None,
        storage_gateway_id: str = None,
        storage_id: str = None,
        storage_volume_id: str = None,
        storage_volume_name: str = None,
        target_name: str = None,
    ):
        # The authentication protocol. The value is set to **CHAP**.
        self.auth_protocol = auth_protocol
        # The time when the volume was created. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the volume.
        self.description = description
        # The ID of the node.
        self.ens_region_id = ens_region_id
        # Indicates whether authentication is enabled. Valid values:
        # 
        # *   **1**: Authentication is enabled.
        # *   **0** (default): Authentication is disabled.
        self.is_auth = is_auth
        # Indicates whether the volume is enabled. Valid values:
        # 
        # *   **1** (default): The volume is enabled.
        # *   **0**: The volume is disabled.
        self.is_enable = is_enable
        # The status of the volume. Valid values:
        # 
        # *   creating
        # *   available
        # *   deleting
        # *   deleted
        self.status = status
        # The ID of the storage gateway.
        self.storage_gateway_id = storage_gateway_id
        # The ID of the storage medium.
        self.storage_id = storage_id
        # The ID of the volume.
        self.storage_volume_id = storage_volume_id
        # The name of the volume.
        self.storage_volume_name = storage_volume_name
        # The destination of the volume.
        self.target_name = target_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_protocol is not None:
            result['AuthProtocol'] = self.auth_protocol

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.is_auth is not None:
            result['IsAuth'] = self.is_auth

        if self.is_enable is not None:
            result['IsEnable'] = self.is_enable

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_gateway_id is not None:
            result['StorageGatewayId'] = self.storage_gateway_id

        if self.storage_id is not None:
            result['StorageId'] = self.storage_id

        if self.storage_volume_id is not None:
            result['StorageVolumeId'] = self.storage_volume_id

        if self.storage_volume_name is not None:
            result['StorageVolumeName'] = self.storage_volume_name

        if self.target_name is not None:
            result['TargetName'] = self.target_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthProtocol') is not None:
            self.auth_protocol = m.get('AuthProtocol')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('IsAuth') is not None:
            self.is_auth = m.get('IsAuth')

        if m.get('IsEnable') is not None:
            self.is_enable = m.get('IsEnable')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageGatewayId') is not None:
            self.storage_gateway_id = m.get('StorageGatewayId')

        if m.get('StorageId') is not None:
            self.storage_id = m.get('StorageId')

        if m.get('StorageVolumeId') is not None:
            self.storage_volume_id = m.get('StorageVolumeId')

        if m.get('StorageVolumeName') is not None:
            self.storage_volume_name = m.get('StorageVolumeName')

        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')

        return self

