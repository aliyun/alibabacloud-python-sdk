# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateOriginProtectionRequest(DaraModel):
    def __init__(
        self,
        auto_confirm_iplist: str = None,
        origin_converge: str = None,
        site_id: int = None,
    ):
        self.auto_confirm_iplist = auto_confirm_iplist
        # The IP convergence status.
        # 
        # *   on
        # *   off
        # 
        # This parameter is required.
        self.origin_converge = origin_converge
        # The website ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_confirm_iplist is not None:
            result['AutoConfirmIPList'] = self.auto_confirm_iplist

        if self.origin_converge is not None:
            result['OriginConverge'] = self.origin_converge

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoConfirmIPList') is not None:
            self.auto_confirm_iplist = m.get('AutoConfirmIPList')

        if m.get('OriginConverge') is not None:
            self.origin_converge = m.get('OriginConverge')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

