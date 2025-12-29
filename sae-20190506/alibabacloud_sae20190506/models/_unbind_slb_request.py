# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnbindSlbRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        internet: bool = None,
        intranet: bool = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # Specifies whether to disassociate the Internet-facing SLB instance. Valid values:
        # 
        # *   **true**: dissociates the Internet-facing SLB instance.
        # *   **false**: does not dissociate the Internet-facing SLB instance.
        self.internet = internet
        # Specifies whether to disassociate the internal-facing SLB instance. Valid values:
        # 
        # *   **true**: dissociates the internal-facing SLB instance.
        # *   **false**: does not dissociate the internal-facing SLB instance.
        self.intranet = intranet

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.internet is not None:
            result['Internet'] = self.internet

        if self.intranet is not None:
            result['Intranet'] = self.intranet

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Internet') is not None:
            self.internet = m.get('Internet')

        if m.get('Intranet') is not None:
            self.intranet = m.get('Intranet')

        return self

