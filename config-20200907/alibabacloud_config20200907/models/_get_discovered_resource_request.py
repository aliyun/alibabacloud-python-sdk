# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDiscoveredResourceRequest(DaraModel):
    def __init__(
        self,
        compliance_option: int = None,
        region: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # Specifies whether to query the compliance results of the resource. Valid values:
        # 
        # *   0 (default): does not query the compliance results of the resource.
        # *   1: queries the compliance results of the resource.
        self.compliance_option = compliance_option
        # The ID of the region in which the resource resides.
        # 
        # For more information about how to query the region ID of a resource, see [ListDiscoveredResources](https://help.aliyun.com/document_detail/411702.html).
        self.region = region
        # The resource ID.
        # 
        # For more information about how to obtain the ID of a resource, see [ListDiscoveredResources](https://help.aliyun.com/document_detail/411702.html).
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource.
        # 
        # For more information about how to obtain the type of a resource, see [ListDiscoveredResources](https://help.aliyun.com/document_detail/411702.html).
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_option is not None:
            result['ComplianceOption'] = self.compliance_option

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceOption') is not None:
            self.compliance_option = m.get('ComplianceOption')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

