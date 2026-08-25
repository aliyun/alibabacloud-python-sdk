# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class ListProtectedResourcesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        protected_resources: List[main_models.ListProtectedResourcesResponseBodyProtectedResources] = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The return code. A value of 200 indicates success.
        self.code = code
        # The number of results per query.
        # 
        # Valid values: 10 to 100. Default value: 10.
        self.max_results = max_results
        # The returned message. The value "successful" is returned for a successful request. An error message is returned for a failed request.
        self.message = message
        # The pagination token for the next page. If this parameter is empty, no more pages are available.
        self.next_token = next_token
        # The list of protected resources.
        self.protected_resources = protected_resources
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        # 
        # - true: The request was successful.
        # - false: The request failed.
        self.success = success
        # The total number of protected resources.
        self.total_count = total_count

    def validate(self):
        if self.protected_resources:
            for v1 in self.protected_resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['ProtectedResources'] = []
        if self.protected_resources is not None:
            for k1 in self.protected_resources:
                result['ProtectedResources'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.protected_resources = []
        if m.get('ProtectedResources') is not None:
            for k1 in m.get('ProtectedResources'):
                temp_model = main_models.ListProtectedResourcesResponseBodyProtectedResources()
                self.protected_resources.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListProtectedResourcesResponseBodyProtectedResources(DaraModel):
    def __init__(
        self,
        backup_plan_count: int = None,
        created_by_product: str = None,
        protected_data_size: int = None,
        protected_resource_id: str = None,
        resource_id: str = None,
        resource_owner_id: int = None,
        resource_region_id: str = None,
        snapshot_count: int = None,
        source_type: str = None,
    ):
        # The number of backup plans.
        self.backup_plan_count = backup_plan_count
        # The product capability to which the resource belongs. Valid values:
        # - **HBR**: Cloud Backup standard capability.
        # - **BASIC**: ECS File Backup Essential Edition.
        self.created_by_product = created_by_product
        # The amount of protected data, in bytes. Currently, only ECS File Backup Essential Edition is supported.
        # - **SourceType=ECS_FILE**: the backed-up block storage capacity.
        self.protected_data_size = protected_data_size
        # The ID of the protected resource.
        self.protected_resource_id = protected_resource_id
        # The resource ID.
        # - **SourceType=ECS_FILE**: the ECS instance ID.
        # - **SourceType=COMMON_FILE_SYSTEM**: the CPFS data source ID.
        # - **SourceType=COMMON_NAS**: the on-premises NAS data source ID.
        # - **SourceType=File**: the local service client ID.
        # - **SourceType=NAS**: the Alibaba Cloud NAS file system ID.
        # - **SourceType=OSS**: the OSS bucket.
        self.resource_id = resource_id
        # The UID of the user who owns the resource.
        self.resource_owner_id = resource_owner_id
        # The region ID of the resource.
        self.resource_region_id = resource_region_id
        # The number of backups.
        self.snapshot_count = snapshot_count
        # The backup feature type. Valid values:
        # - **ECS_FILE**: ECS file backup.
        # - **COMMON_FILE_SYSTEM**: Cloud Parallel File Storage (CPFS) backup.
        # - **COMMON_NAS**: on-premises NAS backup.
        # - **File**: on-premises file backup.
        # - **NAS**: Alibaba Cloud NAS backup.
        # - **OSS**: OSS backup.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_plan_count is not None:
            result['BackupPlanCount'] = self.backup_plan_count

        if self.created_by_product is not None:
            result['CreatedByProduct'] = self.created_by_product

        if self.protected_data_size is not None:
            result['ProtectedDataSize'] = self.protected_data_size

        if self.protected_resource_id is not None:
            result['ProtectedResourceId'] = self.protected_resource_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

        if self.snapshot_count is not None:
            result['SnapshotCount'] = self.snapshot_count

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPlanCount') is not None:
            self.backup_plan_count = m.get('BackupPlanCount')

        if m.get('CreatedByProduct') is not None:
            self.created_by_product = m.get('CreatedByProduct')

        if m.get('ProtectedDataSize') is not None:
            self.protected_data_size = m.get('ProtectedDataSize')

        if m.get('ProtectedResourceId') is not None:
            self.protected_resource_id = m.get('ProtectedResourceId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        if m.get('SnapshotCount') is not None:
            self.snapshot_count = m.get('SnapshotCount')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

