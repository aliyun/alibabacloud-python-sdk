# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddZooKeeperSaslUserShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        instance_id: str = None,
        reload: bool = None,
        sasl_user_shrink: str = None,
    ):
        # The language of the response. Valid values: zh (default): Chinese, en: English.
        self.accept_language = accept_language
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether to restart the cluster to immediately load the SASL users.
        self.reload = reload
        # The list of SASL users to add.
        # 
        # This parameter is required.
        self.sasl_user_shrink = sasl_user_shrink

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

        if self.sasl_user_shrink is not None:
            result['SaslUser'] = self.sasl_user_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Reload') is not None:
            self.reload = m.get('Reload')

        if m.get('SaslUser') is not None:
            self.sasl_user_shrink = m.get('SaslUser')

        return self

