# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CopyImageRequest(DaraModel):
    def __init__(
        self,
        destination_description: str = None,
        destination_image_name: str = None,
        destination_region_id: str = None,
        image_id: str = None,
        region_id: str = None,
    ):
        # The description of the new image in the destination region. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.destination_description = destination_description
        # The name of the new image. The name must be 2 to 128 characters in length. The name must start with a letter but cannot start with `http://` or `https://`. The name can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.destination_image_name = destination_image_name
        # The ID of the destination region. The ID must be different from the current region ID of the image. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.destination_region_id = destination_region_id
        # The ID of the image that is copied to the destination region.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_description is not None:
            result['DestinationDescription'] = self.destination_description

        if self.destination_image_name is not None:
            result['DestinationImageName'] = self.destination_image_name

        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationDescription') is not None:
            self.destination_description = m.get('DestinationDescription')

        if m.get('DestinationImageName') is not None:
            self.destination_image_name = m.get('DestinationImageName')

        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

