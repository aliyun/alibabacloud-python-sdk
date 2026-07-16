# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateTemplateByScratchRequest(DaraModel):
    def __init__(
        self,
        provision_region_id: str = None,
        region_id: str = None,
        template_scratch_id: str = None,
        template_type: str = None,
    ):
        # The region ID of the new node.
        self.provision_region_id = provision_region_id
        # The region ID of the resource scenario.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource scenario.
        # 
        # For more information about how to query the IDs of resource scenarios, see [ListTemplateScratches](https://help.aliyun.com/document_detail/363050.html).
        # 
        # This parameter is required.
        self.template_scratch_id = template_scratch_id
        # The type of the template that Resource Orchestration Service (ROS) generates. ROS can generate templates of the ROS and Terraform types. Default value: ROS.
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.provision_region_id is not None:
            result['ProvisionRegionId'] = self.provision_region_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.template_scratch_id is not None:
            result['TemplateScratchId'] = self.template_scratch_id

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProvisionRegionId') is not None:
            self.provision_region_id = m.get('ProvisionRegionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TemplateScratchId') is not None:
            self.template_scratch_id = m.get('TemplateScratchId')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        return self

