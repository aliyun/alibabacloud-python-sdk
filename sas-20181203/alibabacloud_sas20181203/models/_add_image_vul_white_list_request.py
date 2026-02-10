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
        # The language of the content within the request and response. Default value: zh. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The reason why you add the vulnerability to the whitelist.
        self.reason = reason
        # The source of the whitelist. Valid values:
        # - **image**
        # - **agentless**
        self.source = source
        # The object on which you want to perform the operation. The value of this parameter is in the JSON format and contains the following fields:
        # 
        # *   **type**: the object type. The value is fixed to repo.
        # *   **target**: the object content. The value is in the Namespace/Image repository format.
        self.target = target
        # The type of the vulnerability. Valid values:
        # 
        # *   **cve**: system vulnerability
        # *   **sca**: application vulnerability
        self.type = type
        # The whitelist. The value of this parameter is in the JSON format and contains the following fields:
        # 
        # *   **Type**: the vulnerability type. Valid values: cve and sca.
        # *   **Name**: the name of the vulnerability that is specified in Common Vulnerabilities and Exposures (CVE).
        # *   **AliasName**: the alias of the vulnerability that is specified in CVE.
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

