# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveZooKeeperSaslUserShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        instance_id: str = None,
        reload: bool = None,
        user_names_shrink: str = None,
    ):
        # The language of the returned results. Valid values: zh (default): Chinese, en: English.
        self.accept_language = accept_language
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether the changes take effect immediately.
        self.reload = reload
        # The list of usernames to remove.
        # 
        # This parameter is required.
        self.user_names_shrink = user_names_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.reload is not None:
            result['Reload'] = self.reload

        if self.user_names_shrink is not None:
            result['UserNames'] = self.user_names_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Reload') is not None:
            self.reload = m.get('Reload')

        if m.get('UserNames') is not None:
            self.user_names_shrink = m.get('UserNames')

        return self

