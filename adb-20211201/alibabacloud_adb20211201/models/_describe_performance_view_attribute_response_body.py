# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribePerformanceViewAttributeResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        create_from_view_type: str = None,
        dbcluster_id: str = None,
        fill_origin_view_keys: bool = None,
        request_id: str = None,
        view_detail: main_models.DescribePerformanceViewAttributeResponseBodyViewDetail = None,
        view_name: str = None,
    ):
        # The details about the access denial.
        # 
        # >  This parameter is returned only if Resource Access Management (RAM) permission verification failed.
        self.access_denied_detail = access_denied_detail
        # The type of the view.
        self.create_from_view_type = create_from_view_type
        # The cluster ID.
        # 
        # >  You can call the [DescribeDBClusters](https://help.aliyun.com/document_detail/129857.html) operation to query the information about all AnalyticDB for MySQL clusters within a region, including cluster IDs.
        self.dbcluster_id = dbcluster_id
        # Specifies whether to populate the names of the metrics in the original monitoring view when you view the monitoring view. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.fill_origin_view_keys = fill_origin_view_keys
        # The request ID.
        self.request_id = request_id
        # The information about the monitoring view.
        self.view_detail = view_detail
        # The name of the view.
        self.view_name = view_name

    def validate(self):
        if self.view_detail:
            self.view_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.create_from_view_type is not None:
            result['CreateFromViewType'] = self.create_from_view_type

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.fill_origin_view_keys is not None:
            result['FillOriginViewKeys'] = self.fill_origin_view_keys

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.view_detail is not None:
            result['ViewDetail'] = self.view_detail.to_map()

        if self.view_name is not None:
            result['ViewName'] = self.view_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('CreateFromViewType') is not None:
            self.create_from_view_type = m.get('CreateFromViewType')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('FillOriginViewKeys') is not None:
            self.fill_origin_view_keys = m.get('FillOriginViewKeys')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ViewDetail') is not None:
            temp_model = main_models.DescribePerformanceViewAttributeResponseBodyViewDetail()
            self.view_detail = temp_model.from_map(m.get('ViewDetail'))

        if m.get('ViewName') is not None:
            self.view_name = m.get('ViewName')

        return self

class DescribePerformanceViewAttributeResponseBodyViewDetail(DaraModel):
    def __init__(
        self,
        categories: List[main_models.DescribePerformanceViewAttributeResponseBodyViewDetailCategories] = None,
        chart_linked: bool = None,
        charts_per_line: int = None,
    ):
        # The metric category.
        self.categories = categories
        # Specifies whether to enable the filter interaction feature. Valid values:
        # 
        # *   **true**
        # *   **false**
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
                temp_model = main_models.DescribePerformanceViewAttributeResponseBodyViewDetailCategories()
                self.categories.append(temp_model.from_map(k1))

        if m.get('ChartLinked') is not None:
            self.chart_linked = m.get('ChartLinked')

        if m.get('ChartsPerLine') is not None:
            self.charts_per_line = m.get('ChartsPerLine')

        return self

class DescribePerformanceViewAttributeResponseBodyViewDetailCategories(DaraModel):
    def __init__(
        self,
        category: str = None,
        keys: List[main_models.DescribePerformanceViewAttributeResponseBodyViewDetailCategoriesKeys] = None,
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
                temp_model = main_models.DescribePerformanceViewAttributeResponseBodyViewDetailCategoriesKeys()
                self.keys.append(temp_model.from_map(k1))

        return self

class DescribePerformanceViewAttributeResponseBodyViewDetailCategoriesKeys(DaraModel):
    def __init__(
        self,
        enable_auto_mc: bool = None,
        engine: List[str] = None,
        group_type: List[str] = None,
        key_name: str = None,
        selected: bool = None,
    ):
        # Indicates whether the multi-cluster feature is enabled. Valid values:
        # 
        # - true
        # 
        # - false
        self.enable_auto_mc = enable_auto_mc
        # The database engine of the cluster. Valid values:
        # 
        # *  AnalyticDB
        self.engine = engine
        # The type of the resource group. Valid values:
        # 
        # *   **Interactive**
        # *   **Job**
        # 
        # >  For more information about resource groups, see [Resource group overview](https://help.aliyun.com/document_detail/428610.html).
        self.group_type = group_type
        # The name of the metric.
        self.key_name = key_name
        # Specifies whether to select the metric. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.selected = selected

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_auto_mc is not None:
            result['EnableAutoMc'] = self.enable_auto_mc

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.key_name is not None:
            result['KeyName'] = self.key_name

        if self.selected is not None:
            result['Selected'] = self.selected

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableAutoMc') is not None:
            self.enable_auto_mc = m.get('EnableAutoMc')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')

        if m.get('Selected') is not None:
            self.selected = m.get('Selected')

        return self

