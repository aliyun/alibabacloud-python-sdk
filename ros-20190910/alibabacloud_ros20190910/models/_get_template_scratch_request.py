# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTemplateScratchRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        show_data_option: str = None,
        template_scratch_id: str = None,
    ):
        # The region ID of the resource scenario.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The data display option. Valid values:
        # 
        # *   Sources: displays only the data of source nodes. This setting takes effect only when TemplateScratchType is set to ArchitectureDetection.
        # *   Source: displays only the data of the source node. This setting takes effect only when TemplateScratchType is not set to ArchitectureDetection.
        # *   Provisions: displays only the data of new nodes. This setting takes effect only when TemplateScratchType is not set to ArchitectureDetection.
        # *   All: displays all data.
        # 
        # For more information about source nodes and new nodes, see [Overview](https://help.aliyun.com/document_detail/352074.html).
        # 
        # >  If you do not specify this parameter, the node data is not displayed.
        self.show_data_option = show_data_option
        # The ID of the resource scenario.
        self.template_scratch_id = template_scratch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.show_data_option is not None:
            result['ShowDataOption'] = self.show_data_option

        if self.template_scratch_id is not None:
            result['TemplateScratchId'] = self.template_scratch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ShowDataOption') is not None:
            self.show_data_option = m.get('ShowDataOption')

        if m.get('TemplateScratchId') is not None:
            self.template_scratch_id = m.get('TemplateScratchId')

        return self

