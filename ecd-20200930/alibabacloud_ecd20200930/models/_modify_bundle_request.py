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
        # The ID of the cloud computer template that you want to modify.
        # 
        # This parameter is required.
        self.bundle_id = bundle_id
        # The name of the new cloud computer template.
        self.bundle_name = bundle_name
        # The description of the new cloud computer template.
        self.description = description
        # The new image ID. The new image must meet the following conditions:
        # 
        # *   The new image must be in the Available state.
        # *   The operating system of the new image must be the same as that of the original image.
        # *   The required disk size for the new image cannot be greater than that for the original image.
        # *   The GPU type of the new image must be the same as that of the original image.
        self.image_id = image_id
        # The OS language. This parameter is available only for system images.
        # 
        # Valid values:
        # 
        # *   en-US: American English
        # *   zh-HK: Traditional Chinese (Hong Kong)
        # *   zh-CN: Simplified Chinese.
        # 
        # *   ja-JP: Japanese
        self.language = language
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

