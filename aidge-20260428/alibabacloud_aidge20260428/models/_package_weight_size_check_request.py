# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PackageWeightSizeCheckRequest(DaraModel):
    def __init__(
        self,
        annotated_image_url: str = None,
        raw_image_url: str = None,
    ):
        # The URL of the annotated image with manual bounding box markings, which is the original image overlaid with blue or red rectangular bounding box lines. The URL must be publicly accessible. The image must not exceed 4000 × 4000 pixels or 10 MB in size. Supported formats: png, jpeg, and jpg.
        # 
        # This parameter is required.
        self.annotated_image_url = annotated_image_url
        # The URL of the raw image, which is the unannotated photo of the parcel on the scanning platform. The URL must be publicly accessible. The image must not exceed 4000 × 4000 pixels or 10 MB in size. Supported formats: png, jpeg, and jpg.
        # 
        # This parameter is required.
        self.raw_image_url = raw_image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotated_image_url is not None:
            result['AnnotatedImageUrl'] = self.annotated_image_url

        if self.raw_image_url is not None:
            result['RawImageUrl'] = self.raw_image_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnnotatedImageUrl') is not None:
            self.annotated_image_url = m.get('AnnotatedImageUrl')

        if m.get('RawImageUrl') is not None:
            self.raw_image_url = m.get('RawImageUrl')

        return self

