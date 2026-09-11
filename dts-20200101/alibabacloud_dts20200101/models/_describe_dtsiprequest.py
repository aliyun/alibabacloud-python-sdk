# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDTSIPRequest(DaraModel):
    def __init__(
        self,
        destination_endpoint_region: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        source_endpoint_region: str = None,
    ):
        # The region ID of the destination instance. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        # > If the destination instance is a self-managed database that has a public IP address, you can specify **ap-southeast-1** or the region ID that is geographically closest to the self-managed database.
        self.destination_endpoint_region = destination_endpoint_region
        # The region in which the DTS task instance resides. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The region ID of the source instance. For more information, see [Supported regions](https://help.aliyun.com/document_detail/141033.html).
        # > If the source instance is a self-managed database that has a public IP address, you can specify **ap-southeast-1** or the region ID that is geographically closest to the self-managed database.
        # 
        # This parameter is required.
        self.source_endpoint_region = source_endpoint_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_endpoint_region is not None:
            result['DestinationEndpointRegion'] = self.destination_endpoint_region

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.source_endpoint_region is not None:
            result['SourceEndpointRegion'] = self.source_endpoint_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationEndpointRegion') is not None:
            self.destination_endpoint_region = m.get('DestinationEndpointRegion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SourceEndpointRegion') is not None:
            self.source_endpoint_region = m.get('SourceEndpointRegion')

        return self

