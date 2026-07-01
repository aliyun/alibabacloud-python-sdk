# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMediaResourceIdRequest(DaraModel):
    def __init__(
        self,
        extend_info: str = None,
        file_size: int = None,
        memo: str = None,
        oss_key: str = None,
        resource_type: int = None,
    ):
        # The extended field.
        # 
        # > Required when the resource type is **image**.
        self.extend_info = extend_info
        # The file size. Unit: bytes.
        # 
        # This parameter is required.
        self.file_size = file_size
        # The description of the uploaded resource.
        self.memo = memo
        # The address of the resource to retrieve.
        # 
        # This parameter is required.
        self.oss_key = oss_key
        # The resource type.
        # 
        # - **1**: Text
        # - **2**: Image. Small images must not exceed 100 KB. Large images must not exceed 2 MB. Images must be clear. Supported formats: JPG, JPEG, PNG.
        # - **3**: Audio
        # - **4**: Video. Supported format: MP4.
        # > 
        # > - If the resource type is image, **img_rate** is required.
        # > - 1:1 ratio: oneToOne
        # > - 16:9 ratio: sixteenToNine
        # > - 3:1 ratio: threeToOne
        # > - 48:65 ratio: fortyEightToSixtyFiv.
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
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info

        if self.file_size is not None:
            result['FileSize'] = self.file_size

        if self.memo is not None:
            result['Memo'] = self.memo

        if self.oss_key is not None:
            result['OssKey'] = self.oss_key

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')

        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')

        if m.get('Memo') is not None:
            self.memo = m.get('Memo')

        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

