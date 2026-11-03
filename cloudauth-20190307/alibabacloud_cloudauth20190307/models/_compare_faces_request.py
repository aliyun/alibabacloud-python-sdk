# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CompareFacesRequest(DaraModel):
    def __init__(
        self,
        source_image_type: str = None,
        source_image_value: str = None,
        target_image_type: str = None,
        target_image_value: str = None,
    ):
        # The type of the first image. Valid values:
        # 
        # - **FacePic**: A face photo of the user.
        # - **IDPic**: A portrait photo from the chip of a second-generation Chinese ID card. This photo is typically read and decoded by a second-generation ID card reader.
        self.source_image_type = source_image_type
        # The URL of the first image. For more information, see the instructions on uploading image URLs.
        self.source_image_value = source_image_value
        # The type of the second image. Valid values:
        # 
        # - **FacePic**: A face photo of the user.
        # - **IDPic**: A portrait photo from the chip of a second-generation Chinese ID card. This photo is typically read and decoded by a second-generation ID card reader.
        self.target_image_type = target_image_type
        # The URL of the second image. For more information, see the instructions on uploading image URLs.
        self.target_image_value = target_image_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_image_type is not None:
            result['SourceImageType'] = self.source_image_type

        if self.source_image_value is not None:
            result['SourceImageValue'] = self.source_image_value

        if self.target_image_type is not None:
            result['TargetImageType'] = self.target_image_type

        if self.target_image_value is not None:
            result['TargetImageValue'] = self.target_image_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceImageType') is not None:
            self.source_image_type = m.get('SourceImageType')

        if m.get('SourceImageValue') is not None:
            self.source_image_value = m.get('SourceImageValue')

        if m.get('TargetImageType') is not None:
            self.target_image_type = m.get('TargetImageType')

        if m.get('TargetImageValue') is not None:
            self.target_image_value = m.get('TargetImageValue')

        return self

