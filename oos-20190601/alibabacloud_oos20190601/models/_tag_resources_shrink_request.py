# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TagResourcesShrinkRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        resource_ids_shrink: str = None,
        resource_type: str = None,
        tags_shrink: str = None,
    ):
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IDs of the resources for which you want to modify the resource group. The number of resource IDs is 1 to 50.
        # 
        # *   If you set ResourceType to template, specify ResourceIds in the ["TemplateName1","TemplateName2"] format.
        # *   If you set ResourceType to parameter, specify ResourceIds in the ["Name1","Name2"] format.
        # *   If you set ResourceType to secretparameter, specify ResourceIds in the ["Name1","Name2"] format.
        # *   If you set ResourceType to stateconfiguration, specify ResourceIds in the ["StateConfigurationId 1","StateConfigurationId 2"] format.
        # *   If you set ResourceType to application, specify ResourceIds in the ["Name1","Name2"] format.
        # 
        # This parameter is required.
        self.resource_ids_shrink = resource_ids_shrink
        # The type of the resource for which you want to modify the resource group. Valid values:
        # 
        # *   template: template.
        # *   parameter: parameter.
        # *   secretparameter: encryption parameter.
        # *   stateconfiguration: desired-state configuration.
        # *   application: application.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag keys and values. The number of key-value pairs ranges from 1 to 20.
        # 
        # This parameter is required.
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_ids_shrink is not None:
            result['ResourceIds'] = self.resource_ids_shrink

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceIds') is not None:
            self.resource_ids_shrink = m.get('ResourceIds')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        return self

