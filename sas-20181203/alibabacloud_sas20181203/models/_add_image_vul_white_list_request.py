# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddImageVulWhiteListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        reason: str = None,
        source: str = None,
        target: str = None,
        type: str = None,
        whitelist: str = None,
    ):
        # The language of the request and response. Default value: zh. Valid values:
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # The reason for adding the whitelist.
        self.reason = reason
        # The source of the whitelist. Valid values:
        # - **image**: image
        # - **agentless**: agentless
        self.source = source
        # The operation target. This parameter is in JSON format and contains the following fields:
        # 
        # - **type**: the target type. Set the value to repo.
        # - **target**: the target content. Format: namespace/image repository.
        self.target = target
        # The vulnerability type. Valid values:
        # - **cve**: system vulnerability
        # - **sca**: application vulnerability
        self.type = type
        # The whitelist. This parameter is in JSON format and contains the following fields:
        # 
        # - **Type**: the vulnerability type. Valid values: cve and sca.
        # - **Name**: the name in the vulnerability advisory.
        # - **AliasName**: the alias in the vulnerability advisory.
        self.whitelist = whitelist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.source is not None:
            result['Source'] = self.source

        if self.target is not None:
            result['Target'] = self.target

        if self.type is not None:
            result['Type'] = self.type

        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')

        return self

