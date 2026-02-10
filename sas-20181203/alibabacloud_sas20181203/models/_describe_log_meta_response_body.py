# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeLogMetaResponseBody(DaraModel):
    def __init__(
        self,
        log_meta_list: List[main_models.DescribeLogMetaResponseBodyLogMetaList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of the configurations of the log analysis feature.
        self.log_meta_list = log_meta_list
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.log_meta_list:
            for v1 in self.log_meta_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LogMetaList'] = []
        if self.log_meta_list is not None:
            for k1 in self.log_meta_list:
                result['LogMetaList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.log_meta_list = []
        if m.get('LogMetaList') is not None:
            for k1 in m.get('LogMetaList'):
                temp_model = main_models.DescribeLogMetaResponseBodyLogMetaList()
                self.log_meta_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeLogMetaResponseBodyLogMetaList(DaraModel):
    def __init__(
        self,
        category: str = None,
        hot_ttl: int = None,
        log_desc: str = None,
        log_store: str = None,
        project: str = None,
        status: str = None,
        topic: str = None,
        ttl: int = None,
        user_log_store: str = None,
        user_project: str = None,
        user_region: str = None,
    ):
        # The category of logs. Valid values:
        # 
        # *   **host**
        # *   **security**
        self.category = category
        # The time period after which logs in hot storage are moved to cold storage. Unit: days.
        # 
        # >  If the value is -1, logs that are stored in hot storage are not moved to cold storage.
        self.hot_ttl = hot_ttl
        # The name of the log type.
        self.log_desc = log_desc
        # The name of the dedicated Logstore in which logs are stored.
        self.log_store = log_store
        # The name of the project.
        self.project = project
        # The status of the log analysis feature. Valid values:
        # 
        # *   **disabled**
        # *   **enabled**
        self.status = status
        # The topic of logs that are delivered.
        self.topic = topic
        # The number of days during which logs can be retained.
        self.ttl = ttl
        # The name of the dedicated Logstore in which user logs are stored.
        self.user_log_store = user_log_store
        # The name of the dedicated project in which logs are stored.
        self.user_project = user_project
        # The ID of the region.
        self.user_region = user_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.hot_ttl is not None:
            result['HotTtl'] = self.hot_ttl

        if self.log_desc is not None:
            result['LogDesc'] = self.log_desc

        if self.log_store is not None:
            result['LogStore'] = self.log_store

        if self.project is not None:
            result['Project'] = self.project

        if self.status is not None:
            result['Status'] = self.status

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.user_log_store is not None:
            result['UserLogStore'] = self.user_log_store

        if self.user_project is not None:
            result['UserProject'] = self.user_project

        if self.user_region is not None:
            result['UserRegion'] = self.user_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('HotTtl') is not None:
            self.hot_ttl = m.get('HotTtl')

        if m.get('LogDesc') is not None:
            self.log_desc = m.get('LogDesc')

        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('UserLogStore') is not None:
            self.user_log_store = m.get('UserLogStore')

        if m.get('UserProject') is not None:
            self.user_project = m.get('UserProject')

        if m.get('UserRegion') is not None:
            self.user_region = m.get('UserRegion')

        return self

