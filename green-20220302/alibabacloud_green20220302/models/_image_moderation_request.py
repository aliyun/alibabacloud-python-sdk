# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImageModerationRequest(DaraModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
    ):
        # The detection types supported by Image Moderation Enhanced Edition. Valid values:
        # - baselineCheck: general baseline check
        # - baselineCheck_pro: general baseline check (Professional Edition)
        # - baselineCheck_cb: general baseline check (Overseas Edition)
        # - tonalityImprove: content governance detection
        # - aigcCheck: AIGC image detection
        # - aigcViolationDetection: AIGC image infringement detection
        # - aigcDetector: AIGC image generation determination
        # - profilePhotoCheck: profile picture detection
        # - postImageCheck: post and comment image detection
        # - advertisingCheck: marketing material detection
        # - liveStreamCheck: video or live stream screenshot detection
        # - generalOcr: general image and text OCR
        # - generalRecognition: universal image recognition
        # - postImageCheckByVL: image moderation service with large and small model fusion
        # - postImageCheckByVL_cb: image moderation service with large and small model fusion (Overseas Edition)
        # - baselineCheckByVL: general image moderation large model service
        self.service = service
        # The parameter set for the content moderation object. The value is a JSON string.
        # - imageUrl: the URL of the object to be moderated. Required.
        # - dataId: the data ID corresponding to the moderation object. Optional.
        # - referer: the Referer request header, used for scenarios such as hotlink protection. Optional.
        self.service_parameters = service_parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service is not None:
            result['Service'] = self.service

        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')

        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')

        return self

