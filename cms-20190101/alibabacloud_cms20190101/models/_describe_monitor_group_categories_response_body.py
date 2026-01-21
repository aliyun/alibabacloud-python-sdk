# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeMonitorGroupCategoriesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        monitor_group_categories: main_models.DescribeMonitorGroupCategoriesResponseBodyMonitorGroupCategories = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The error message returned.
        self.message = message
        # The cloud services to which the resources in the application group belong and the number of resources that belong to the cloud service.
        self.monitor_group_categories = monitor_group_categories
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.monitor_group_categories:
            self.monitor_group_categories.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.monitor_group_categories is not None:
            result['MonitorGroupCategories'] = self.monitor_group_categories.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('MonitorGroupCategories') is not None:
            temp_model = main_models.DescribeMonitorGroupCategoriesResponseBodyMonitorGroupCategories()
            self.monitor_group_categories = temp_model.from_map(m.get('MonitorGroupCategories'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeMonitorGroupCategoriesResponseBodyMonitorGroupCategories(DaraModel):
    def __init__(
        self,
        group_id: int = None,
        monitor_group_category: main_models.DescribeMonitorGroupCategoriesResponseBodyMonitorGroupCategoriesMonitorGroupCategory = None,
    ):
        # The ID of the application group.
        self.group_id = group_id
        # The cloud services to which the resources in the application group belong and the number of resources that belong to the cloud service.
        self.monitor_group_category = monitor_group_category

    def validate(self):
        if self.monitor_group_category:
            self.monitor_group_category.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.monitor_group_category is not None:
            result['MonitorGroupCategory'] = self.monitor_group_category.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('MonitorGroupCategory') is not None:
            temp_model = main_models.DescribeMonitorGroupCategoriesResponseBodyMonitorGroupCategoriesMonitorGroupCategory()
            self.monitor_group_category = temp_model.from_map(m.get('MonitorGroupCategory'))

        return self

class DescribeMonitorGroupCategoriesResponseBodyMonitorGroupCategoriesMonitorGroupCategory(DaraModel):
    def __init__(
        self,
        category_item: List[main_models.DescribeMonitorGroupCategoriesResponseBodyMonitorGroupCategoriesMonitorGroupCategoryCategoryItem] = None,
    ):
        self.category_item = category_item

    def validate(self):
        if self.category_item:
            for v1 in self.category_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CategoryItem'] = []
        if self.category_item is not None:
            for k1 in self.category_item:
                result['CategoryItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.category_item = []
        if m.get('CategoryItem') is not None:
            for k1 in m.get('CategoryItem'):
                temp_model = main_models.DescribeMonitorGroupCategoriesResponseBodyMonitorGroupCategoriesMonitorGroupCategoryCategoryItem()
                self.category_item.append(temp_model.from_map(k1))

        return self

class DescribeMonitorGroupCategoriesResponseBodyMonitorGroupCategoriesMonitorGroupCategoryCategoryItem(DaraModel):
    def __init__(
        self,
        category: str = None,
        count: int = None,
    ):
        # The abbreviation of the cloud service name.
        # 
        # >  For more information about how to obtain the abbreviation of a cloud service name, see `metricCategory` in the response parameter `Labels` of the [DescribeProjectMeta](https://help.aliyun.com/document_detail/114916.html) operation.
        self.category = category
        # The number of resources that belong to the cloud service.
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.count is not None:
            result['Count'] = self.count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        return self

