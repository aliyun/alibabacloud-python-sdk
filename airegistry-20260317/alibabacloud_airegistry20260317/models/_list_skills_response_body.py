# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_airegistry20260317 import models as main_models
from darabonba.model import DaraModel

class ListSkillsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListSkillsResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListSkillsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListSkillsResponseBodyData(DaraModel):
    def __init__(
        self,
        page_items: List[main_models.ListSkillsResponseBodyDataPageItems] = None,
        page_number: int = None,
        pages_available: int = None,
        total_count: int = None,
    ):
        self.page_items = page_items
        self.page_number = page_number
        self.pages_available = pages_available
        self.total_count = total_count

    def validate(self):
        if self.page_items:
            for v1 in self.page_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PageItems'] = []
        if self.page_items is not None:
            for k1 in self.page_items:
                result['PageItems'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.pages_available is not None:
            result['PagesAvailable'] = self.pages_available

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.page_items = []
        if m.get('PageItems') is not None:
            for k1 in m.get('PageItems'):
                temp_model = main_models.ListSkillsResponseBodyDataPageItems()
                self.page_items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PagesAvailable') is not None:
            self.pages_available = m.get('PagesAvailable')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSkillsResponseBodyDataPageItems(DaraModel):
    def __init__(
        self,
        biz_tags: str = None,
        description: str = None,
        download_count: int = None,
        editing_version: str = None,
        enable: bool = None,
        from_: str = None,
        labels: Dict[str, str] = None,
        name: str = None,
        namespace_id: str = None,
        online_cnt: int = None,
        owner: str = None,
        reviewing_version: str = None,
        scope: str = None,
        update_time: int = None,
        writeable: bool = None,
    ):
        self.biz_tags = biz_tags
        self.description = description
        self.download_count = download_count
        self.editing_version = editing_version
        self.enable = enable
        self.from_ = from_
        self.labels = labels
        self.name = name
        self.namespace_id = namespace_id
        self.online_cnt = online_cnt
        self.owner = owner
        self.reviewing_version = reviewing_version
        self.scope = scope
        self.update_time = update_time
        self.writeable = writeable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_tags is not None:
            result['BizTags'] = self.biz_tags

        if self.description is not None:
            result['Description'] = self.description

        if self.download_count is not None:
            result['DownloadCount'] = self.download_count

        if self.editing_version is not None:
            result['EditingVersion'] = self.editing_version

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.from_ is not None:
            result['From'] = self.from_

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.online_cnt is not None:
            result['OnlineCnt'] = self.online_cnt

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.reviewing_version is not None:
            result['ReviewingVersion'] = self.reviewing_version

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.writeable is not None:
            result['Writeable'] = self.writeable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTags') is not None:
            self.biz_tags = m.get('BizTags')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DownloadCount') is not None:
            self.download_count = m.get('DownloadCount')

        if m.get('EditingVersion') is not None:
            self.editing_version = m.get('EditingVersion')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('OnlineCnt') is not None:
            self.online_cnt = m.get('OnlineCnt')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ReviewingVersion') is not None:
            self.reviewing_version = m.get('ReviewingVersion')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('Writeable') is not None:
            self.writeable = m.get('Writeable')

        return self

