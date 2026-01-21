# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHybridMonitorNamespaceListRequest(DaraModel):
    def __init__(
        self,
        keyword: str = None,
        namespace: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        show_task_statistic: bool = None,
    ):
        # The search keyword.
        self.keyword = keyword
        # The name of the namespace.
        # 
        # The name can contain letters, digits, and hyphens (-).
        self.namespace = namespace
        # The page number.
        # 
        # Page numbers start from 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Page numbers start from 1. Default value: 10.
        self.page_size = page_size
        self.region_id = region_id
        # Specifies whether to return the configuration details of metric import tasks for Alibaba Cloud services and the number of metric import tasks for third-party services. Valid values:
        # 
        # *   true
        # *   false (default)
        self.show_task_statistic = show_task_statistic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.show_task_statistic is not None:
            result['ShowTaskStatistic'] = self.show_task_statistic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ShowTaskStatistic') is not None:
            self.show_task_statistic = m.get('ShowTaskStatistic')

        return self

