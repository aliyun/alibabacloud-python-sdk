# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyBundleRequest(DaraModel):
    def __init__(
        self,
        bundle_id: str = None,
        bundle_name: str = None,
        description: str = None,
        image_id: str = None,
        language: str = None,
        region_id: str = None,
    ):
        # The cloud computer template ID.
        # 
        # This parameter is required.
        self.bundle_id = bundle_id
        # The new cloud computer template name.
        self.bundle_name = bundle_name
        # The new cloud computer template description.
        self.description = description
        # The new image ID. The new image must meet the following conditions:
        # 
        # - The new image must be in the Available state.
        # 
        # - The new image must have the same operating system as the original image.
        # 
        # - The disk size required by the new image cannot be larger than that of the original image.
        # 
        # - The GPU type of the new image must be the same as that of the original image.
        self.image_id = image_id
        # The operating system language. Currently, only system images are supported.
        self.language = language
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to query the regions supported by Elastic Desktop Service.
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
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id

        if self.bundle_name is not None:
            result['BundleName'] = self.bundle_name

        if self.description is not None:
            result['Description'] = self.description

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.language is not None:
            result['Language'] = self.language

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')

        if m.get('BundleName') is not None:
            self.bundle_name = m.get('BundleName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

