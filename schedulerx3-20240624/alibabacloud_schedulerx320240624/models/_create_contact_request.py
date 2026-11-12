# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateContactRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        contact_name: str = None,
        type: str = None,
    ):
        # The JSON character string for channel parameter settings. Example for the IM type: {"channels":[{"channelType":"dingtalk","clientId":"xxx","clientSecret":"xxx","targetType":"group","targetId":"xxx","robotCode":"xxx"}]}
        # 
        # This parameter is required.
        self.config = config
        # The name of the alert contact.
        # 
        # This parameter is required.
        self.contact_name = contact_name
        # The contact type.
        # - IM: Configures an IM channel notification contact.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

