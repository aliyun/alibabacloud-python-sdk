# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListBaselineCheckWhiteRecordResponseBody(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListBaselineCheckWhiteRecordResponseBodyList] = None,
        page_info: main_models.ListBaselineCheckWhiteRecordResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The whitelist rules.
        self.list = list
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListBaselineCheckWhiteRecordResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListBaselineCheckWhiteRecordResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListBaselineCheckWhiteRecordResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListBaselineCheckWhiteRecordResponseBodyList(DaraModel):
    def __init__(
        self,
        check_id: int = None,
        check_item: str = None,
        check_type: str = None,
        check_type_dis_name: str = None,
        container_items: List[main_models.ListBaselineCheckWhiteRecordResponseBodyListContainerItems] = None,
        lang: str = None,
        reason: str = None,
        record_id: int = None,
        source: str = None,
        target: str = None,
        target_type: str = None,
    ):
        # The ID of the check item.
        self.check_id = check_id
        # The description of the check item.
        self.check_item = check_item
        # The type of the check item.
        self.check_type = check_type
        # The display name of the check item type.
        self.check_type_dis_name = check_type_dis_name
        # List of whitelisted container names in the check item.
        self.container_items = container_items
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The reason why the check item is added to the whitelist.
        self.reason = reason
        # The ID of the whitelist rule.
        self.record_id = record_id
        # The data source. Valid values:
        # 
        # *   **default**: server
        # *   **agentless**: agentless detection
        self.source = source
        # The object that is added to the whitelist.
        self.target = target
        # The type of the assets on which the whitelist rule takes effect. Valid values:
        # 
        # *   **all_instance**: all servers
        # *   **instance**: specific servers
        self.target_type = target_type

    def validate(self):
        if self.container_items:
            for v1 in self.container_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.check_item is not None:
            result['CheckItem'] = self.check_item

        if self.check_type is not None:
            result['CheckType'] = self.check_type

        if self.check_type_dis_name is not None:
            result['CheckTypeDisName'] = self.check_type_dis_name

        result['ContainerItems'] = []
        if self.container_items is not None:
            for k1 in self.container_items:
                result['ContainerItems'].append(k1.to_map() if k1 else None)

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.source is not None:
            result['Source'] = self.source

        if self.target is not None:
            result['Target'] = self.target

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('CheckItem') is not None:
            self.check_item = m.get('CheckItem')

        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')

        if m.get('CheckTypeDisName') is not None:
            self.check_type_dis_name = m.get('CheckTypeDisName')

        self.container_items = []
        if m.get('ContainerItems') is not None:
            for k1 in m.get('ContainerItems'):
                temp_model = main_models.ListBaselineCheckWhiteRecordResponseBodyListContainerItems()
                self.container_items.append(temp_model.from_map(k1))

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

class ListBaselineCheckWhiteRecordResponseBodyListContainerItems(DaraModel):
    def __init__(
        self,
        container_names: str = None,
        uuid: str = None,
    ):
        # Names of the whitelisted containers for the current asset, separated by English commas.
        self.container_names = container_names
        # Server UUID.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container_names is not None:
            result['ContainerNames'] = self.container_names

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContainerNames') is not None:
            self.container_names = m.get('ContainerNames')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

