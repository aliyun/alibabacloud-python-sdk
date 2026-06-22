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
        # Specifies whether you agree to the data migration from the Hong Kong (China) region to the Singapore data center. Valid values:
        # 
        # - **true**: Agree.
        # 
        # - **false**: Disagree.
        self.is_agree = is_agree
        # Specifies whether the user confirms that the data migration from the Hong Kong (China) region to the Singapore data center has been completed.
        # 
        # - **true**: Confirmed. The user has confirmed that the data migration from the Hong Kong (China) region to the Singapore data center has been completed, and the notification pop-up window no longer needs to be displayed.
        # - **false**: Not confirmed. The user has not confirmed that the data migration from the Hong Kong (China) region to the Singapore data center has been completed, and the notification pop-up window still needs to be displayed.
        self.is_confirmed = is_confirmed
        # Specifies whether to schedule data migration of data from the Hong Kong (China) region to the Singapore data center within 24 hours. Valid values:
        # 
        # - **true**: Schedule the switch within 24 hours.
        # 
        # - **false**: Do not schedule. For users who have cloud services in the Hong Kong (China) region, data migration will be automatically completed on March 5, 2026. For users who do not have cloud services in the Hong Kong (China) region, data migration will be automatically completed on November 17, 2025.
        self.is_immediate = is_immediate
        # The language type for the request and response messages. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The switch type. Valid values:
        # 
        # - **sg_switch**: data migration from the Hong Kong (China) region to the Singapore data center.
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

