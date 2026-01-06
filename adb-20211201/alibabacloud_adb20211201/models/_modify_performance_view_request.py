# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class ModifyPerformanceViewRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        view_detail: main_models.ModifyPerformanceViewRequestViewDetail = None,
        view_name: str = None,
    ):
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition cluster.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/612397.html) operation to query the IDs of all AnalyticDB for MySQL clusters within a region.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/143074.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The new information about the monitoring view.
        # 
        # This parameter is required.
        self.view_detail = view_detail
        # The name of the monitoring view.
        # 
        # This parameter is required.
        self.view_name = view_name

    def validate(self):
        if self.view_detail:
            self.view_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.view_detail is not None:
            result['ViewDetail'] = self.view_detail.to_map()

        if self.view_name is not None:
            result['ViewName'] = self.view_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ViewDetail') is not None:
            temp_model = main_models.ModifyPerformanceViewRequestViewDetail()
            self.view_detail = temp_model.from_map(m.get('ViewDetail'))

        if m.get('ViewName') is not None:
            self.view_name = m.get('ViewName')

        return self

class ModifyPerformanceViewRequestViewDetail(DaraModel):
    def __init__(
        self,
        categories: List[main_models.ModifyPerformanceViewRequestViewDetailCategories] = None,
        chart_linked: bool = None,
        charts_per_line: int = None,
    ):
        # The metric categories.
        self.categories = categories
        # Specifies whether to enable the filter interaction feature. Valid values:
        # 
        # *   true
        # *   false
        self.chart_linked = chart_linked
        # The number of charts to display in each row.
        self.charts_per_line = charts_per_line

    def validate(self):
        if self.categories:
            for v1 in self.categories:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Categories'] = []
        if self.categories is not None:
            for k1 in self.categories:
                result['Categories'].append(k1.to_map() if k1 else None)

        if self.chart_linked is not None:
            result['ChartLinked'] = self.chart_linked

        if self.charts_per_line is not None:
            result['ChartsPerLine'] = self.charts_per_line

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.categories = []
        if m.get('Categories') is not None:
            for k1 in m.get('Categories'):
                temp_model = main_models.ModifyPerformanceViewRequestViewDetailCategories()
                self.categories.append(temp_model.from_map(k1))

        if m.get('ChartLinked') is not None:
            self.chart_linked = m.get('ChartLinked')

        if m.get('ChartsPerLine') is not None:
            self.charts_per_line = m.get('ChartsPerLine')

        return self

class ModifyPerformanceViewRequestViewDetailCategories(DaraModel):
    def __init__(
        self,
        category: str = None,
        keys: List[main_models.ModifyPerformanceViewRequestViewDetailCategoriesKeys] = None,
    ):
        # The name of the metric category. Valid values:
        # 
        # *   **Node**
        # *   **DiskData**
        # *   **WorkLoad**
        # *   **ResourceGroup**
        self.category = category
        # The metrics.
        self.keys = keys

    def validate(self):
        if self.keys:
            for v1 in self.keys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        result['Keys'] = []
        if self.keys is not None:
            for k1 in self.keys:
                result['Keys'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        self.keys = []
        if m.get('Keys') is not None:
            for k1 in m.get('Keys'):
                temp_model = main_models.ModifyPerformanceViewRequestViewDetailCategoriesKeys()
                self.keys.append(temp_model.from_map(k1))

        return self

class ModifyPerformanceViewRequestViewDetailCategoriesKeys(DaraModel):
    def __init__(
        self,
        key_name: str = None,
        selected: bool = None,
    ):
        # The name of the metric.
        self.key_name = key_name
        # Specifies whether to select the metric. Valid values:
        # 
        # *   true
        # *   false
        self.selected = selected

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_name is not None:
            result['KeyName'] = self.key_name

        if self.selected is not None:
            result['Selected'] = self.selected

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')

        if m.get('Selected') is not None:
            self.selected = m.get('Selected')

        return self

