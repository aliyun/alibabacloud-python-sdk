# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class StartTaskForDistributeImageRequest(DaraModel):
    def __init__(
        self,
        destination_region_list: List[str] = None,
        image_id: str = None,
        product_type: str = None,
        retry_type: str = None,
        source_region: str = None,
        version_id: str = None,
    ):
        # The regions to which you want to replicate the image.
        self.destination_region_list = destination_region_list
        # The image ID.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The product type.
        # 
        # Valid values:
        # 
        # *   CloudDesktop: Elastic Desktop Service
        # *   CloudApp: App Streaming
        # *   WuyingServer: Workstation
        self.product_type = product_type
        # This parameter is not publicly available.
        self.retry_type = retry_type
        # The region where the source image is located. If you leave this parameter empty, a random region is selected.
        self.source_region = source_region
        # The ID of the image version. If you do not specify this parameter, the latest image version is used by default.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_region_list is not None:
            result['DestinationRegionList'] = self.destination_region_list

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.retry_type is not None:
            result['RetryType'] = self.retry_type

        if self.source_region is not None:
            result['SourceRegion'] = self.source_region

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationRegionList') is not None:
            self.destination_region_list = m.get('DestinationRegionList')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RetryType') is not None:
            self.retry_type = m.get('RetryType')

        if m.get('SourceRegion') is not None:
            self.source_region = m.get('SourceRegion')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

