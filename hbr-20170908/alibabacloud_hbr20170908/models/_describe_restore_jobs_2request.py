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
        # The edition. Valid values: `BASIC` and `STANDARD`. Default value: `STANDARD`.
        self.edition = edition
        # The filter conditions.
        self.filters = filters
        # The page number. Pages start from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The data source type. Valid values:
        # 
        # - **ECS_FILE**: Restores ECS files.
        # 
        # - **OSS**: Restores OSS objects.
        # 
        # - **NAS**: Restores NAS files.
        # 
        # - **COMMON_FILE_SYSTEM**: Restores data to a CPFS file system.
        # 
        # - **OTS_TABLE**: Restores an OTS table.
        # 
        # - **UDM_ECS_ROLLBACK**: Restores an entire ECS instance.
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
        # The filter key. Valid values:
        # 
        # - **RegionId**: region ID
        # 
        # - **PlanId**: backup plan ID
        # 
        # - **JobId**: backup job ID
        # 
        # - **VaultId**: vault ID
        # 
        # - **InstanceId**: ECS instance ID
        # 
        # - **Bucket**: OSS bucket name
        # 
        # - **FileSystemId**: file system ID
        # 
        # - **Status**: job status
        # 
        # - **CompleteTime**: completion time
        self.key = key
        # The matching method. The default value is IN. Valid values:
        # 
        # - **EQUAL**: Equal to
        # 
        # - **NOT_EQUAL**: Not equal to
        # 
        # - **GREATER_THAN**: Greater than
        # 
        # - **GREATER_THAN_OR_EQUAL**: Greater than or equal to
        # 
        # - **LESS_THAN**: Less than
        # 
        # - **LESS_THAN_OR_EQUAL**: Less than or equal to
        # 
        # - **BETWEEN**: The value is within a specified range. The `Values` parameter must be a JSON array in the `[min, max]` format.
        # 
        # - **IN**: The value is in a specified set. The `Values` parameter must be an array.
        # 
        # > The IN operator is not supported when `Key` is **CompleteTime**.
        self.operator = operator
        # An array of values for the specified filter key.
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

