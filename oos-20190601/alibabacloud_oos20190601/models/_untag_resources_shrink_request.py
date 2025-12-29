# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UntagResourcesShrinkRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_ids_shrink: str = None,
        resource_type: str = None,
        tag_keys_shrink: str = None,
    ):
        # Specifies whether to remove all tags. This parameter takes effect only if TagKeys is left empty. Valid values: true and false. Default value: false. TagKeys is required if this parameter is set to false.
        self.all = all
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
        # The tag keys. The number of keys ranges from 1 to 20.
        self.tag_keys_shrink = tag_keys_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all is not None:
            result['All'] = self.all

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_ids_shrink is not None:
            result['ResourceIds'] = self.resource_ids_shrink

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tag_keys_shrink is not None:
            result['TagKeys'] = self.tag_keys_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceIds') is not None:
            self.resource_ids_shrink = m.get('ResourceIds')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKeys') is not None:
            self.tag_keys_shrink = m.get('TagKeys')

        return self

