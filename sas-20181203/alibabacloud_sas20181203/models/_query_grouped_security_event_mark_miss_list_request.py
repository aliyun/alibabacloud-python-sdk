# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryGroupedSecurityEventMarkMissListRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        disposal_way: str = None,
        event_name: str = None,
        from_: str = None,
        lang: str = None,
        page_size: int = None,
        remark: str = None,
        source_ip: str = None,
    ):
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The handling method. Valid values:
        # 
        # *   **1**: Automatically Added to Whitelist
        # *   **2**: Defense Without Notification
        self.disposal_way = disposal_way
        # The name of the alert event. The value indicates a subtype.
        self.event_name = event_name
        # The ID of the request source. Set the value to sas.
        self.from_ = from_
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries to return on each page. Default value: **20**.
        self.page_size = page_size
        # The condition that is used to query alert events by asset. You can specify a value of the following types:
        # 
        # *   The IP address of the asset.
        # *   The public IP address of the asset.
        # *   The private IP address of the asset.
        # *   The name of the asset.
        self.remark = remark
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.disposal_way is not None:
            result['DisposalWay'] = self.disposal_way

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.from_ is not None:
            result['From'] = self.from_

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DisposalWay') is not None:
            self.disposal_way = m.get('DisposalWay')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

