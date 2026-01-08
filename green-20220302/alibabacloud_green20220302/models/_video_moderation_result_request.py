# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class VideoModerationResultRequest(DaraModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
    ):
        # The type of the moderation service.
        # 
        # Valid values:
        # 
        # *   liveStreamDetection: live stream moderation
        # *   videoDetection: video file moderation
        # *   liveStreamDetection_cb: live stream moderation_For regions outside the Chinese mainland
        # *   videoDetection_cb: video file moderation_For regions outside the Chinese mainland.
        self.service = service
        # The parameters required by the moderation service. The ID of the task that you want to query. You can specify one task ID at a time.
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

