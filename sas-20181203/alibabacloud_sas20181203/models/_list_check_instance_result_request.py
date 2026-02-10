# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListCheckInstanceResultRequest(DaraModel):
    def __init__(
        self,
        check_id: int = None,
        current_page: int = None,
        instance_id_key: str = None,
        instance_ids: List[str] = None,
        instance_name_key: str = None,
        lang: str = None,
        page_size: int = None,
        region_id_key: str = None,
        sort_types: List[str] = None,
        statuses: List[str] = None,
    ):
        # The ID of the check item.
        # 
        # This parameter is required.
        self.check_id = check_id
        # The number of the page to return.
        self.current_page = current_page
        # The ID of the instance.
        self.instance_id_key = instance_id_key
        # The instance IDs of cloud services.
        self.instance_ids = instance_ids
        # The name of the instance.
        self.instance_name_key = instance_name_key
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries per page. Maximum value: 100.
        self.page_size = page_size
        # The region ID of the instance.
        self.region_id_key = region_id_key
        # The types of the conditions based on which the check items are sorted.
        self.sort_types = sort_types
        # The statuses of check items.
        self.statuses = statuses

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.instance_id_key is not None:
            result['InstanceIdKey'] = self.instance_id_key

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.instance_name_key is not None:
            result['InstanceNameKey'] = self.instance_name_key

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id_key is not None:
            result['RegionIdKey'] = self.region_id_key

        if self.sort_types is not None:
            result['SortTypes'] = self.sort_types

        if self.statuses is not None:
            result['Statuses'] = self.statuses

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('InstanceIdKey') is not None:
            self.instance_id_key = m.get('InstanceIdKey')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('InstanceNameKey') is not None:
            self.instance_name_key = m.get('InstanceNameKey')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionIdKey') is not None:
            self.region_id_key = m.get('RegionIdKey')

        if m.get('SortTypes') is not None:
            self.sort_types = m.get('SortTypes')

        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')

        return self

