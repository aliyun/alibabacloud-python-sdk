# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeWebLockBindListRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        remark: str = None,
        source_ip: str = None,
        status: str = None,
        uuid: str = None,
    ):
        # The page number of the current page in a paging query. Minimum value: 1. Default value: 1.
        self.current_page = current_page
        # The language of the request and response. Valid values:
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The maximum number of entries per page in a paging query. Default value: 20.
        self.page_size = page_size
        # The fuzzy match field for the server. The value can be a server name or IP address.
        self.remark = remark
        # The IP address of the access source.
        self.source_ip = source_ip
        # The protection status of the servers that you want to query. Valid values:
        # - **on**: Protection is enabled.
        # - **off**: Protection is disabled.
        self.status = status
        # The UUID of the asset that you want to query.
        # > Call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to obtain this parameter.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.status is not None:
            result['Status'] = self.status

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

