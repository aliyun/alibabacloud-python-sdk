# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribePerformanceViewsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        request_id: str = None,
        views: List[main_models.DescribePerformanceViewsResponseBodyViews] = None,
    ):
        # The details about the access denial.
        # 
        # >  This parameter is returned only if Resource Access Management (RAM) permission verification failed.
        self.access_denied_detail = access_denied_detail
        # The request ID.
        self.request_id = request_id
        # the list of view.
        self.views = views

    def validate(self):
        if self.views:
            for v1 in self.views:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Views'] = []
        if self.views is not None:
            for k1 in self.views:
                result['Views'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.views = []
        if m.get('Views') is not None:
            for k1 in m.get('Views'):
                temp_model = main_models.DescribePerformanceViewsResponseBodyViews()
                self.views.append(temp_model.from_map(k1))

        return self

class DescribePerformanceViewsResponseBodyViews(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        update_time: str = None,
        view_name: str = None,
    ):
        # The time when created.
        self.create_time = create_time
        # The time when updated.
        self.update_time = update_time
        # The name of the view.
        self.view_name = view_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.view_name is not None:
            result['ViewName'] = self.view_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('ViewName') is not None:
            self.view_name = m.get('ViewName')

        return self

