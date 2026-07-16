# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHotlineRecordDetailRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        close_time_end: int = None,
        close_time_start: int = None,
        current_page: int = None,
        instance_id: str = None,
        page_size: int = None,
    ):
        # A unique ID for the customer request. Used for idempotency validation and can be generated using UUID.
        self.client_token = client_token
        # The start time when the hotline call ends. The value is a UNIX timestamp in milliseconds.
        self.close_time_end = close_time_end
        # The end time when the hotline call ends. The value is a UNIX timestamp in milliseconds.
        self.close_time_start = close_time_start
        # Current page number. Default value: **1**.
        self.current_page = current_page
        # Artificial Intelligence Cloud Call Service (AICCS) instance ID. You can obtain it from the Artificial Intelligence Cloud Call Service console.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Page size. Default value: **100**.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.close_time_end is not None:
            result['CloseTimeEnd'] = self.close_time_end

        if self.close_time_start is not None:
            result['CloseTimeStart'] = self.close_time_start

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CloseTimeEnd') is not None:
            self.close_time_end = m.get('CloseTimeEnd')

        if m.get('CloseTimeStart') is not None:
            self.close_time_start = m.get('CloseTimeStart')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

