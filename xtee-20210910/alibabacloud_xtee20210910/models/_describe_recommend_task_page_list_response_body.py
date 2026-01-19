# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeRecommendTaskPageListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        current_page: int = None,
        page_size: int = None,
        result_object: List[main_models.DescribeRecommendTaskPageListResponseBodyResultObject] = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # Request ID
        self.request_id = request_id
        # Current page number
        self.current_page = current_page
        # Page size, with a default value of 10
        self.page_size = page_size
        # Returned object
        self.result_object = result_object
        # Total number of items
        self.total_item = total_item
        # Total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        result['resultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['resultObject'].append(k1.to_map() if k1 else None)

        if self.total_item is not None:
            result['totalItem'] = self.total_item

        if self.total_page is not None:
            result['totalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        self.result_object = []
        if m.get('resultObject') is not None:
            for k1 in m.get('resultObject'):
                temp_model = main_models.DescribeRecommendTaskPageListResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('totalItem') is not None:
            self.total_item = m.get('totalItem')

        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')

        return self

class DescribeRecommendTaskPageListResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        expect_velocities: List[str] = None,
        gmt_create: int = None,
        normal_count: int = None,
        normal_size: int = None,
        risk_count: int = None,
        risk_size: int = None,
        sample_name: str = None,
        sample_scene: str = None,
        task_id: int = None,
        task_name: str = None,
        task_status: str = None,
    ):
        # Impact indicators
        self.expect_velocities = expect_velocities
        # Creation time.
        self.gmt_create = gmt_create
        # Number of samples
        self.normal_count = normal_count
        # Number of normal samples
        self.normal_size = normal_size
        # Number of records displayed on the current page.
        self.risk_count = risk_count
        # Number of risk samples
        self.risk_size = risk_size
        # Sample name
        self.sample_name = sample_name
        # Sample scenario
        self.sample_scene = sample_scene
        # Task ID.
        self.task_id = task_id
        # Task name.
        self.task_name = task_name
        # Task status.
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expect_velocities is not None:
            result['expectVelocities'] = self.expect_velocities

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.normal_count is not None:
            result['normalCount'] = self.normal_count

        if self.normal_size is not None:
            result['normalSize'] = self.normal_size

        if self.risk_count is not None:
            result['riskCount'] = self.risk_count

        if self.risk_size is not None:
            result['riskSize'] = self.risk_size

        if self.sample_name is not None:
            result['sampleName'] = self.sample_name

        if self.sample_scene is not None:
            result['sampleScene'] = self.sample_scene

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.task_name is not None:
            result['taskName'] = self.task_name

        if self.task_status is not None:
            result['taskStatus'] = self.task_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expectVelocities') is not None:
            self.expect_velocities = m.get('expectVelocities')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('normalCount') is not None:
            self.normal_count = m.get('normalCount')

        if m.get('normalSize') is not None:
            self.normal_size = m.get('normalSize')

        if m.get('riskCount') is not None:
            self.risk_count = m.get('riskCount')

        if m.get('riskSize') is not None:
            self.risk_size = m.get('riskSize')

        if m.get('sampleName') is not None:
            self.sample_name = m.get('sampleName')

        if m.get('sampleScene') is not None:
            self.sample_scene = m.get('sampleScene')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')

        return self

