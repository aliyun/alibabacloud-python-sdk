# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateFormationCrawlerRequest(DaraModel):
    def __init__(
        self,
        crawler_info: str = None,
        crawler_task_id: str = None,
        dbcluster_id: str = None,
        region_id: str = None,
    ):
        # The JSON string that contains the complete configuration of the crawler. This is the most important parameter. For more information about the internal JSON structure, see the CrawlerInfo structure definition section.
        # 
        # This parameter is required.
        self.crawler_info = crawler_info
        # The task ID.
        self.crawler_task_id = crawler_task_id
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The region ID.
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to query the regions and zones supported by AnalyticDB for MySQL, including region IDs.
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
        if self.crawler_info is not None:
            result['CrawlerInfo'] = self.crawler_info

        if self.crawler_task_id is not None:
            result['CrawlerTaskId'] = self.crawler_task_id

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrawlerInfo') is not None:
            self.crawler_info = m.get('CrawlerInfo')

        if m.get('CrawlerTaskId') is not None:
            self.crawler_task_id = m.get('CrawlerTaskId')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

