# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyWebCCGlobalSwitchRequest(DaraModel):
    def __init__(
        self,
        cc_global_switch: str = None,
        domain: str = None,
    ):
        # Specifies whether the HTTP flood mitigation feature is enabled. Valid values:
        # 
        # *   **open**
        # *   **close**
        # 
        # This parameter is required.
        self.cc_global_switch = cc_global_switch
        # The domain name of the website.
        # 
        # >  A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) operation to query all domain names.
        # 
        # This parameter is required.
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cc_global_switch is not None:
            result['CcGlobalSwitch'] = self.cc_global_switch

        if self.domain is not None:
            result['Domain'] = self.domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CcGlobalSwitch') is not None:
            self.cc_global_switch = m.get('CcGlobalSwitch')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        return self

