# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class ListTemplateScratchesRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[main_models.ListTemplateScratchesRequestTags] = None,
        template_scratch_id: str = None,
        template_scratch_type: str = None,
    ):
        # The number of the page to return.
        # 
        # Pages start from page 1.
        # 
        # Default value: 1
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Maximum value: 50.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the scenario.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The status of the scenario. Valid values:
        # 
        # *   GENERATE_IN_PROGRESS: The scenario is being created.
        # *   GENERATE_COMPLETE: The scenario is created.
        # *   GENERATE_FAILED: The scenario fails to be created.
        self.status = status
        # The tags of the scenario.
        self.tags = tags
        # The ID of the scenario.
        self.template_scratch_id = template_scratch_id
        # The type of the resource scenario. Valid values:
        # 
        # *   ArchitectureReplication: resource replication
        # *   ArchitectureDetection: resource detection
        # *   ResourceImport: resource management
        # *   ResourceMigration: resource migration
        self.template_scratch_type = template_scratch_type

    def validate(self):
        if self.tags:
            for v1 in self.tags:
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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.template_scratch_id is not None:
            result['TemplateScratchId'] = self.template_scratch_id

        if self.template_scratch_type is not None:
            result['TemplateScratchType'] = self.template_scratch_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListTemplateScratchesRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TemplateScratchId') is not None:
            self.template_scratch_id = m.get('TemplateScratchId')

        if m.get('TemplateScratchType') is not None:
            self.template_scratch_type = m.get('TemplateScratchType')

        return self

class ListTemplateScratchesRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the scenario.
        # 
        # > Tags is optional. If you want to specify Tags, you must specify Key.
        # 
        # This parameter is required.
        self.key = key
        # The tag value of the scenario.
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

