# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UntagResourcesRequest(DaraModel):
    def __init__(
        self,
        delete_all: bool = None,
        resource_ids: str = None,
        resource_region_id: str = None,
        resource_type: str = None,
        tag_keys: str = None,
    ):
        # Specifies whether to remove all existing tags from the specified resources. Default value: false. Valid values:
        # 
        # - **true**: removes all existing tags from the specified resources.
        # 
        # - **false**: does not remove all existing tags from the specified resources.
        # 
        # > All existing tags of a resource are removed only if the **tagKeys** parameter is left empty and the **DeleteAll** parameter is set to true.
        self.delete_all = delete_all
        # The IDs of the resources from which you want to remove tags. You can specify up to 20 IDs.
        # 
        # This parameter is required.
        self.resource_ids = resource_ids
        # The region in which the resource resides.
        # 
        # This parameter is required.
        self.resource_region_id = resource_region_id
        # The type of the resource. Valid values:
        # 
        # - **application**: Enterprise Distributed Application Service (EDAS) application
        # 
        # - **cluster**: EDAS cluster
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags that you want to remove. You can specify up to 20 tags. Set this parameter to a JSON array.
        self.tag_keys = tag_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_all is not None:
            result['DeleteAll'] = self.delete_all

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteAll') is not None:
            self.delete_all = m.get('DeleteAll')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')

        return self

