# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateContactRequest(DaraModel):
    def __init__(
        self,
        config: str = None,
        contact_name: str = None,
        enabled: bool = None,
        type: str = None,
    ):
        # The JSON character string for channel parameter settings. This parameter is optional. If specified, the settings are updated.
        self.config = config
        # The name of the contact to update.
        # 
        # This parameter is required.
        self.contact_name = contact_name
        # Specifies whether to enable or disable the notification channel for the contact.
        self.enabled = enabled
        # The type of the contact.
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

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

