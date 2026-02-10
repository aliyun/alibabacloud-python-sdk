# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPublishBatchRequest(DaraModel):
    def __init__(
        self,
        batch_name: str = None,
        current_page: int = None,
        page_size: int = None,
        upgrade_version: str = None,
    ):
        # The name of the release batch.
        self.batch_name = batch_name
        # The page number.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The destination version of the Security Center agent.
        # 
        # This parameter is required.
        self.upgrade_version = upgrade_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_name is not None:
            result['BatchName'] = self.batch_name

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.upgrade_version is not None:
            result['UpgradeVersion'] = self.upgrade_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchName') is not None:
            self.batch_name = m.get('BatchName')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('UpgradeVersion') is not None:
            self.upgrade_version = m.get('UpgradeVersion')

        return self

