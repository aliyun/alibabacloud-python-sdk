# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupJobs2Request(DaraModel):
    def __init__(
        self,
        edition: str = None,
        filters: List[main_models.DescribeBackupJobs2RequestFilters] = None,
        page_number: int = None,
        page_size: int = None,
        sort_direction: str = None,
        source_type: str = None,
    ):
        # The edition. Valid values: BASIC and STANDARD. The default value is STANDARD.
        self.edition = edition
        # The key-value pairs of the filter.
        self.filters = filters
        # The page number. Pages start from page 1. The default value is 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. The default value is 10.
        self.page_size = page_size
        # The sort direction. Valid values:
        # 
        # - **ASCEND**: Ascending order.
        # 
        # - **DESCEND** (Default): Descending order.
        self.sort_direction = sort_direction
        # The type of the data source. Valid values:
        # 
        # - **ECS_FILE**: Backs up Elastic Compute Service (ECS) files.
        # 
        # - **OSS**: Backs up Alibaba Cloud Object Storage Service (OSS) buckets.
        # 
        # - **NAS**: Backs up Alibaba Cloud Apsara File Storage NAS (NAS) file systems.
        # 
        # - **OTS**: Backs up Alibaba Cloud Tablestore instances.
        # 
        # - **UDM_ECS**: Backs up entire ECS instances.
        # 
        # - **UDM_ECS_DISK**: A sub-task for disk backup in an ECS instance backup job.
        # 
        # - **COMMON_NAS**: A generic NAS data source. This includes archive NAS and on-premises NAS data sources. Use the Values parameter of Filters to specify the data source type.
        # 
        # - **File**: Backs up on-premises files.
        # 
        # - **SYNC**: Data synchronization.
        self.source_type = source_type

    def validate(self):
        if self.filters:
            for v1 in self.filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edition is not None:
            result['Edition'] = self.edition

        result['Filters'] = []
        if self.filters is not None:
            for k1 in self.filters:
                result['Filters'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_direction is not None:
            result['SortDirection'] = self.sort_direction

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.DescribeBackupJobs2RequestFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortDirection') is not None:
            self.sort_direction = m.get('SortDirection')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

class DescribeBackupJobs2RequestFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # The key of the filter. Valid values:
        # 
        # - **RegionId**: The region ID.
        # 
        # - **PlanId**: The backup plan ID.
        # 
        # - **JobId**: The backup job ID.
        # 
        # - **VaultId**: The repository ID.
        # 
        # - **InstanceId**: The ECS instance ID.
        # 
        # - **Bucket**: The name of the OSS bucket.
        # 
        # - **FileSystemId**: The file system ID.
        # 
        # - **Status**: The job status.
        # 
        # - **CreatedTime**: The start time of the job.
        # 
        # - **CompleteTime**: The end time of the job.
        # 
        # - **InstanceName**: The name of the Tablestore instance.
        # 
        # - **BackupType**: The backup job. This parameter is required only when SourceType is set to COMMON_NAS.
        # 
        # - **ParentId**: The ID of the parent job. This parameter is required when you query sub-tasks. For example, if you set SourceType to UDM_ECS_DISK, you must specify the ID of the UDM_ECS job.
        self.key = key
        # The matching operator. The default value is IN. This parameter specifies the operator to use for matching the Key and Value. Valid values:
        # 
        # - **EQUAL**: Equal to.
        # 
        # - **NOT_EQUAL**: Not equal to.
        # 
        # - **GREATER_THAN**: Greater than.
        # 
        # - **GREATER_THAN_OR_EQUAL**: Greater than or equal to.
        # 
        # - **LESS_THAN**: Less than.
        # 
        # - **LESS_THAN_OR_EQUAL**: Less than or equal to.
        # 
        # - **BETWEEN**: The value is a JSON array in the format of `[start,end]`.
        # 
        # - **IN**: The value is an array.
        # 
        # > The IN operator is not supported when you use **CompleteTime** as the key for a query.
        self.operator = operator
        # The value of the filter.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

