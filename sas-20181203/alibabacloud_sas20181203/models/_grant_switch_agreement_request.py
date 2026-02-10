# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrantSwitchAgreementRequest(DaraModel):
    def __init__(
        self,
        is_agree: bool = None,
        is_confirmed: bool = None,
        is_immediate: bool = None,
        lang: str = None,
        type: str = None,
    ):
        # Indicates whether to agree to migrate the client connections from overseas servers to the Singapore center.
        self.is_agree = is_agree
        # Has the user confirmed the migration of Hong Kong region data to Singapore data center
        # 
        # - **true:** The user has confirmed that Hong Kong region data has been migrated to the Singapore data center. No notification popup needs to be displayed subsequently.
        # 
        # - **false**:The user has not confirmed that Hong Kong region data has been migrated to the Singapore data center. Notification popup still needs to be displayed subsequently.
        self.is_confirmed = is_confirmed
        # Whether to schedule the migration of data from the Hong Kong region to the Singapore data center within 24 hours. Values:
        # - **true**: Schedule the switch within 24 hours.
        # - **false**: Do not schedule. Users with cloud products in the Hong Kong region will be automatically migrated on March 5, 2026; users without cloud products in the Hong Kong region will be automatically migrated on November 17, 2025.
        self.is_immediate = is_immediate
        # The language type for requests and responses. The default value is **zh**. Possible values:
        # 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Switching type. Possible values:
        # 
        # - **sg_switch**: Migrate client connections from overseas servers to Singapore
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_agree is not None:
            result['IsAgree'] = self.is_agree

        if self.is_confirmed is not None:
            result['IsConfirmed'] = self.is_confirmed

        if self.is_immediate is not None:
            result['IsImmediate'] = self.is_immediate

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsAgree') is not None:
            self.is_agree = m.get('IsAgree')

        if m.get('IsConfirmed') is not None:
            self.is_confirmed = m.get('IsConfirmed')

        if m.get('IsImmediate') is not None:
            self.is_immediate = m.get('IsImmediate')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

