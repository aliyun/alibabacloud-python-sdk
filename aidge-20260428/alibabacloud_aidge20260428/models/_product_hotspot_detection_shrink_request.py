# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ProductHotspotDetectionShrinkRequest(DaraModel):
    def __init__(
        self,
        reference_image_urls_shrink: str = None,
        req_id: str = None,
        target_image_url: str = None,
    ):
        # The HTTPS URLs of reference images that define the SKU whitelist. A maximum of 20 images are supported.
        # 
        # This parameter is required.
        self.reference_image_urls_shrink = reference_image_urls_shrink
        # The unique business ID for this single-scene call.
        self.req_id = req_id
        # The HTTPS OSS or CDN URL of the target image to be annotated with bounding boxes.
        # 
        # This parameter is required.
        self.target_image_url = target_image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reference_image_urls_shrink is not None:
            result['ReferenceImageUrls'] = self.reference_image_urls_shrink

        if self.req_id is not None:
            result['ReqId'] = self.req_id

        if self.target_image_url is not None:
            result['TargetImageUrl'] = self.target_image_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReferenceImageUrls') is not None:
            self.reference_image_urls_shrink = m.get('ReferenceImageUrls')

        if m.get('ReqId') is not None:
            self.req_id = m.get('ReqId')

        if m.get('TargetImageUrl') is not None:
            self.target_image_url = m.get('TargetImageUrl')

        return self

