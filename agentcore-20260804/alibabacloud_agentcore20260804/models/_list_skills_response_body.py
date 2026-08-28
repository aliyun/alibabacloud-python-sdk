# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class ListSkillsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListSkillsResponseBodyData = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The maximum number of entries to return per page.
        self.max_results = max_results
        # The pagination token for the next page.
        self.next_token = next_token
        # The request ID.
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
            result['data'] = self.data.to_map()

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ListSkillsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListSkillsResponseBodyData(DaraModel):
    def __init__(
        self,
        page_items: List[main_models.ListSkillsResponseBodyDataPageItems] = None,
        page_number: int = None,
        pages_available: int = None,
        total_count: int = None,
    ):
        # The data on the current page.
        self.page_items = page_items
        # The current page number.
        self.page_number = page_number
        # The total number of pages.
        self.pages_available = pages_available
        # The total number of records.
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
        result['pageItems'] = []
        if self.page_items is not None:
            for k1 in self.page_items:
                result['pageItems'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.pages_available is not None:
            result['pagesAvailable'] = self.pages_available

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.page_items = []
        if m.get('pageItems') is not None:
            for k1 in m.get('pageItems'):
                temp_model = main_models.ListSkillsResponseBodyDataPageItems()
                self.page_items.append(temp_model.from_map(k1))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pagesAvailable') is not None:
            self.pages_available = m.get('pagesAvailable')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

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
        online_cnt: int = None,
        owner: str = None,
        reviewing_version: str = None,
        scope: str = None,
        update_time: int = None,
        workspace_id: str = None,
        writeable: bool = None,
    ):
        # The business tags as a JSON array string.
        self.biz_tags = biz_tags
        # The description.
        self.description = description
        # The total number of downloads.
        self.download_count = download_count
        # The version that is being edited.
        self.editing_version = editing_version
        # Indicates whether the Skill is enabled.
        self.enable = enable
        # The source tag.
        self.from_ = from_
        # The label mapping.
        self.labels = labels
        # The name.
        self.name = name
        # The number of online versions.
        self.online_cnt = online_cnt
        # The resource owner.
        self.owner = owner
        # The version that is under review.
        self.reviewing_version = reviewing_version
        # The visibility scope.
        self.scope = scope
        # The update time. This value is a UNIX timestamp in milliseconds.
        self.update_time = update_time
        # The workspace ID.
        self.workspace_id = workspace_id
        # Indicates whether the current user has write permissions.
        self.writeable = writeable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_tags is not None:
            result['bizTags'] = self.biz_tags

        if self.description is not None:
            result['description'] = self.description

        if self.download_count is not None:
            result['downloadCount'] = self.download_count

        if self.editing_version is not None:
            result['editingVersion'] = self.editing_version

        if self.enable is not None:
            result['enable'] = self.enable

        if self.from_ is not None:
            result['from'] = self.from_

        if self.labels is not None:
            result['labels'] = self.labels

        if self.name is not None:
            result['name'] = self.name

        if self.online_cnt is not None:
            result['onlineCnt'] = self.online_cnt

        if self.owner is not None:
            result['owner'] = self.owner

        if self.reviewing_version is not None:
            result['reviewingVersion'] = self.reviewing_version

        if self.scope is not None:
            result['scope'] = self.scope

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        if self.writeable is not None:
            result['writeable'] = self.writeable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizTags') is not None:
            self.biz_tags = m.get('bizTags')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('downloadCount') is not None:
            self.download_count = m.get('downloadCount')

        if m.get('editingVersion') is not None:
            self.editing_version = m.get('editingVersion')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('from') is not None:
            self.from_ = m.get('from')

        if m.get('labels') is not None:
            self.labels = m.get('labels')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('onlineCnt') is not None:
            self.online_cnt = m.get('onlineCnt')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('reviewingVersion') is not None:
            self.reviewing_version = m.get('reviewingVersion')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        if m.get('writeable') is not None:
            self.writeable = m.get('writeable')

        return self

