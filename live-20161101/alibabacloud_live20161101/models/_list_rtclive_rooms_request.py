# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRTCLiveRoomsRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        # The application ID. You can view your application IDs by navigating to **ApsaraVideo Live > Live+ > ApsaraVideo Real-time Communication > Application Management**.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The current page number, starting from 1.
        self.page_no = page_no
        # The page size. Valid values: 10 to 100. Default value: 50.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

