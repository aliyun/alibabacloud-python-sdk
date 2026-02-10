# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetCheckSummaryRequest(DaraModel):
    def __init__(
        self,
        is_item_statistic: bool = None,
        lang: str = None,
        resource_directory_account_id: str = None,
        task_sources: List[str] = None,
        vendors: List[str] = None,
    ):
        # Specifies whether to return the statistics of the check items, including the number of check items supported by the system and the number of check items available to you. Default value: **false**. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_item_statistic = is_item_statistic
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The Alibaba Cloud account ID of the member in the resource directory.
        # 
        # >  You can call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to query the IDs of Alibaba Cloud accounts.
        self.resource_directory_account_id = resource_directory_account_id
        # List of task sources.
        self.task_sources = task_sources
        # The cloud service providers.
        self.vendors = vendors

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_item_statistic is not None:
            result['IsItemStatistic'] = self.is_item_statistic

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.task_sources is not None:
            result['TaskSources'] = self.task_sources

        if self.vendors is not None:
            result['Vendors'] = self.vendors

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsItemStatistic') is not None:
            self.is_item_statistic = m.get('IsItemStatistic')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('TaskSources') is not None:
            self.task_sources = m.get('TaskSources')

        if m.get('Vendors') is not None:
            self.vendors = m.get('Vendors')

        return self

