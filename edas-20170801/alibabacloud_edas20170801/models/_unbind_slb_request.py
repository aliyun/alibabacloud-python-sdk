# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UnbindSlbRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        delete_listener: str = None,
        slb_id: str = None,
        type: str = None,
    ):
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # Specifies whether to delete the listener.
        # 
        # - true: Delete the listener.
        # 
        # - false: Do not delete the listener.
        self.delete_listener = delete_listener
        # The ID of the SLB instance.
        # 
        # This parameter is required.
        self.slb_id = slb_id
        # The network type of the SLB instance.
        # 
        # - **internet**: an internet-facing instance.
        # 
        # - **intranet**: an internal-facing instance.
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
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.delete_listener is not None:
            result['DeleteListener'] = self.delete_listener

        if self.slb_id is not None:
            result['SlbId'] = self.slb_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DeleteListener') is not None:
            self.delete_listener = m.get('DeleteListener')

        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

