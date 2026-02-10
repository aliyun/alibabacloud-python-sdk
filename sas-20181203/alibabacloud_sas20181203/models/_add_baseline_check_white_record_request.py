# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddBaselineCheckWhiteRecordRequest(DaraModel):
    def __init__(
        self,
        check_id: int = None,
        lang: str = None,
        reason: str = None,
        source: str = None,
        target_type: str = None,
    ):
        # The ID of the check item.
        # 
        # >  You can call the [ListCheckItemWarningSummary](~~ListCheckItemWarningSummary~~) operation to query the IDs of check items.
        self.check_id = check_id
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The reason why the check item is added to the whitelist.
        self.reason = reason
        # The data source. If you leave this parameter empty, the default value is used. Valid values:
        # 
        # *   **default**: server
        # *   **agentless**: agentless detection
        self.source = source
        # The type of the assets on which the whitelist rule takes effect. Valid values:
        # 
        # *   **all_instance**: all servers
        # *   **instance**: specific servers
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.source is not None:
            result['Source'] = self.source

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

