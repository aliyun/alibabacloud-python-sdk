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
        # The moderation services supported by Image Moderation 2.0. Valid values:
        # 
        # *   baselineCheck: common baseline moderation
        # *   baselineCheck_pro: common baseline moderation_Professional
        # *   baselineCheck_cb: common baseline moderation_For regions outside the Chinese mainland
        # *   tonalityImprove: content governance moderation
        # *   aigcCheck: AI-generated image identification
        # *   profilePhotoCheck: avatar image moderation
        # *   advertisingCheck: marketing material identification
        # *   liveStreamCheck: moderation of screenshots of videos and live streams
        # 
        # Valid values:
        # 
        # *   liveStreamCheck: moderation of screenshots of videos and live streams
        # *   baselineCheck: common baseline moderation
        # *   aigcCheck: AI-generated image identification
        # *   baselineCheck_pro: common baseline moderation_Professional
        # *   advertisingCheck: marketing material identification
        # *   baselineCheck_cb: common baseline moderation_For regions outside the Chinese mainland
        # *   tonalityImprove: content governance moderation
        # *   profilePhotoCheck: avatar image moderation
        self.service = service
        # The parameters required by the moderation service. The value is a JSON string.
        # 
        # *   imageUrl: the URL of the object that you want to moderate. This parameter is required.
        # *   dataId: the ID of the object that you want to moderate. This parameter is optional.
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

