# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChatShrinkRequest(DaraModel):
    def __init__(
        self,
        authorization: str = None,
        external_user_id: str = None,
        input_shrink: str = None,
        routing_key: str = None,
        session_id: str = None,
        settings_shrink: str = None,
        stream_options_shrink: str = None,
        template_id: str = None,
    ):
        self.authorization = authorization
        self.external_user_id = external_user_id
        self.input_shrink = input_shrink
        self.routing_key = routing_key
        self.session_id = session_id
        self.settings_shrink = settings_shrink
        self.stream_options_shrink = stream_options_shrink
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorization is not None:
            result['Authorization'] = self.authorization

        if self.external_user_id is not None:
            result['ExternalUserId'] = self.external_user_id

        if self.input_shrink is not None:
            result['Input'] = self.input_shrink

        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.settings_shrink is not None:
            result['Settings'] = self.settings_shrink

        if self.stream_options_shrink is not None:
            result['StreamOptions'] = self.stream_options_shrink

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')

        if m.get('ExternalUserId') is not None:
            self.external_user_id = m.get('ExternalUserId')

        if m.get('Input') is not None:
            self.input_shrink = m.get('Input')

        if m.get('RoutingKey') is not None:
            self.routing_key = m.get('RoutingKey')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Settings') is not None:
            self.settings_shrink = m.get('Settings')

        if m.get('StreamOptions') is not None:
            self.stream_options_shrink = m.get('StreamOptions')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

