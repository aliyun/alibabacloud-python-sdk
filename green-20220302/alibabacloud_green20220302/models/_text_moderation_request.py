# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TextModerationRequest(DaraModel):
    def __init__(
        self,
        service: str = None,
        service_parameters: str = None,
    ):
        # The type of the moderation service. Valid values: nickname_detection: user nickname chat_detection: chat interactions comment_detection: dynamic comments pgc_detection: professionally-generated content (PGC) teaching materials
        # 
        # Valid values:
        # 
        # *   pgc_detection: moderation of PGC teaching materials
        # *   nickname_detection: user nickname moderation
        # *   comment_multilingual_pro: multi-language moderation in international business scenarios
        # *   chat_detection: moderation of interactive content of private chats
        # *   ad_compliance_detection: advertising law compliance identification
        # *   comment_detection: moderation of comment content of public chats
        # *   ai_art_detection: AI-generated text identfication
        self.service = service
        # The parameters required by the moderation service. The value is a JSON string.
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

