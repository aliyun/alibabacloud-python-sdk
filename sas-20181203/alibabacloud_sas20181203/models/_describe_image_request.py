# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeImageRequest(DaraModel):
    def __init__(
        self,
        image_instance_id: str = None,
        image_region_id: str = None,
        image_repo_id: str = None,
        image_tag: str = None,
    ):
        # The instance ID of the image.
        # 
        # >  You can call the [DescribeImageInstances](~~DescribeImageInstances~~) operation to query the IDs of instances.
        # 
        # This parameter is required.
        self.image_instance_id = image_instance_id
        # The region ID of the image.
        # 
        # >  You can call the [DescribeImageInstances](~~DescribeImageInstances~~) operation to query the IDs of regions.
        # 
        # This parameter is required.
        self.image_region_id = image_region_id
        # The ID of the image repository.
        # 
        # >  You can call the [DescribeImageInstances](~~DescribeImageInstances~~) operation to query the IDs of image repositories.
        # 
        # This parameter is required.
        self.image_repo_id = image_repo_id
        # The tag that is added to the image.
        # 
        # >  You can call the [DescribeImageInstances](~~DescribeImageInstances~~) operation to query tags.
        # 
        # This parameter is required.
        self.image_tag = image_tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_instance_id is not None:
            result['ImageInstanceId'] = self.image_instance_id

        if self.image_region_id is not None:
            result['ImageRegionId'] = self.image_region_id

        if self.image_repo_id is not None:
            result['ImageRepoId'] = self.image_repo_id

        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageInstanceId') is not None:
            self.image_instance_id = m.get('ImageInstanceId')

        if m.get('ImageRegionId') is not None:
            self.image_region_id = m.get('ImageRegionId')

        if m.get('ImageRepoId') is not None:
            self.image_repo_id = m.get('ImageRepoId')

        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')

        return self

