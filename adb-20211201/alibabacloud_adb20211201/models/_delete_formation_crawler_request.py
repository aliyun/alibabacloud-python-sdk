# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteFormationCrawlerRequest(DaraModel):
    def __init__(
        self,
        crawler_task_id: int = None,
        crawler_task_name: str = None,
        dbcluster_id: str = None,
        region_id: str = None,
    ):
        # The task ID.
        # 
        # This parameter is required.
        self.crawler_task_id = crawler_task_id
        # The task name.
        # 
        # This parameter is required.
        self.crawler_task_name = crawler_task_name
        # The instance ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to query available region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.crawler_task_id is not None:
            result['CrawlerTaskId'] = self.crawler_task_id

        if self.crawler_task_name is not None:
            result['CrawlerTaskName'] = self.crawler_task_name

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrawlerTaskId') is not None:
            self.crawler_task_id = m.get('CrawlerTaskId')

        if m.get('CrawlerTaskName') is not None:
            self.crawler_task_name = m.get('CrawlerTaskName')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

