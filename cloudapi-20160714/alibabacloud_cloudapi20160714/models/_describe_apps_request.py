# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAppsRequest(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        app_owner: int = None,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
    ):
        # The ID of the app.
        self.app_id = app_id
        # The Alibaba Cloud account of the app owner. For more information, see [Account Management](https://account.console.aliyun.com/?spm=a2c4g.11186623.2.15.3a8c196eVWxvQB#/secure).
        self.app_owner = app_owner
        # The number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Maximum value: 100. Default value: 10.
        self.page_size = page_size
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_owner is not None:
            result['AppOwner'] = self.app_owner

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppOwner') is not None:
            self.app_owner = m.get('AppOwner')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

