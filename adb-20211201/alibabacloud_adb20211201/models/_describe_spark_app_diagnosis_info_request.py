# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSparkAppDiagnosisInfoRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        dbcluster_id: str = None,
        language: str = None,
        region_id: str = None,
    ):
        # The application ID.
        # 
        # >  You can call the [ListSparkApps](https://help.aliyun.com/document_detail/455888.html) operation to query all application IDs.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The cluster ID.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/98094.html) operation to query the information about all AnalyticDB for MySQL clusters within a region, including cluster IDs.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The language in which you want to display the results. Valid values:
        # 
        # *   en: English.
        # *   zh (default): Chinese.
        # 
        # This parameter is required.
        self.language = language
        # The region ID.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to query the most recent region list.
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
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.language is not None:
            result['Language'] = self.language

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

