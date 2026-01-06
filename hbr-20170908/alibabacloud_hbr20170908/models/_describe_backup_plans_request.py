# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupPlansRequest(DaraModel):
    def __init__(
        self,
        edition: str = None,
        filters: List[main_models.DescribeBackupPlansRequestFilters] = None,
        page_number: int = None,
        page_size: int = None,
        source_type: str = None,
    ):
        self.edition = edition
        # The filters.
        self.filters = filters
        # The page number. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: Elastic Compute Service (ECS) files
        # *   **OSS**: Object Storage Service (OSS) buckets
        # *   **NAS**: File Storage NAS (NAS) file systems
        # *   **OTS**: Tablestore instances
        # *   **UDM_ECS**: ECS instances
        # *   **SYNC**: data synchronization
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
                temp_model = main_models.DescribeBackupPlansRequestFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

class DescribeBackupPlansRequestFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        # The keys in the filter. Valid values:
        # 
        # *   **regionId**: the ID of a region
        # *   **planId**: the ID of a backup plan
        # *   **sourceType**: the type of a data source
        # *   **vaultId**: the ID of a backup vault
        # *   **instanceName**: the name of an instance
        # *   **instanceId**: the ID of an instance
        # *   **planName**: the name of a backup plan
        self.key = key
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

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

