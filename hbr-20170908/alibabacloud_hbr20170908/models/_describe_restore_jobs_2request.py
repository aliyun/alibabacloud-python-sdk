# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class DescribeRestoreJobs2Request(DaraModel):
    def __init__(
        self,
        edition: str = None,
        filters: List[main_models.DescribeRestoreJobs2RequestFilters] = None,
        page_number: int = None,
        page_size: int = None,
        restore_type: str = None,
    ):
        self.edition = edition
        # The keys in the filter.
        self.filters = filters
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: Elastic Compute Service (ECS) files
        # *   **OSS**: Object Storage Service (OSS) buckets
        # *   **NAS**: Apsara File Storage NAS file systems
        # *   **OTS_TABLE**: Tablestore instances
        # *   **UDM_ECS_ROLLBACK**: ECS instances
        self.restore_type = restore_type

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

        if self.restore_type is not None:
            result['RestoreType'] = self.restore_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')

        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.DescribeRestoreJobs2RequestFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RestoreType') is not None:
            self.restore_type = m.get('RestoreType')

        return self

class DescribeRestoreJobs2RequestFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # The key in the filter. Valid values:
        # 
        # *   **RegionId**: the region ID
        # *   **PlanId**: the ID of a backup plan
        # *   **JobId**: the ID of a backup job
        # *   **VaultId**: the ID of a backup vault
        # *   **InstanceId**: the ID of an ECS instance
        # *   **Bucket**: the name of an OSS bucket
        # *   **FileSystemId**: the ID of a file system
        # *   **Status**: the status of a backup job
        # *   **CompleteTime**: the end time of a backup job
        self.key = key
        # The matching method. Default value: IN. This parameter specifies the operator that you want to use to match a key and a value in the filter. Valid values:
        # 
        # *   **EQUAL**: equal to
        # *   **NOT_EQUAL**: not equal to
        # *   **GREATER_THAN**: greater than
        # *   **GREATER_THAN_OR_EQUAL**: greater than or equal to
        # *   **LESS_THAN**: less than
        # *   **LESS_THAN_OR_EQUAL**: less than or equal to
        # *   **BETWEEN**: specifies a JSON array as a range. The results must fall within the range in the `[Minimum value,Maximum value]` format.
        # *   **IN**: specifies an array as a collection. The results must fall within the collection.
        # 
        # > If you specify the **CompleteTime** parameter as a key to query backup jobs, you cannot use the IN operator to perform a match.
        self.operator = operator
        # The values that you want to match in the filter.
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

