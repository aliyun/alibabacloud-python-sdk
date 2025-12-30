# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateCloudGtmGlobalAlertShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        alert_config_shrink: str = None,
        alert_group_shrink: str = None,
        client_token: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh-CN: Chinese
        # *   en-US: English
        self.accept_language = accept_language
        # The alert configurations.
        self.alert_config_shrink = alert_config_shrink
        # The alert contact groups.
        self.alert_group_shrink = alert_group_shrink
        # The client token that is used to ensure the idempotence of the request. You can specify a custom value for this parameter, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.alert_config_shrink is not None:
            result['AlertConfig'] = self.alert_config_shrink

        if self.alert_group_shrink is not None:
            result['AlertGroup'] = self.alert_group_shrink

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AlertConfig') is not None:
            self.alert_config_shrink = m.get('AlertConfig')

        if m.get('AlertGroup') is not None:
            self.alert_group_shrink = m.get('AlertGroup')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        return self

