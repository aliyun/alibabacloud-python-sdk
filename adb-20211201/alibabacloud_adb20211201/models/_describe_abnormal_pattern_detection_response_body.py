# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeAbnormalPatternDetectionResponseBody(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        detection_items: List[main_models.DescribeAbnormalPatternDetectionResponseBodyDetectionItems] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The cluster ID.
        self.dbcluster_id = dbcluster_id
        # The queried detection items and detection results.
        self.detection_items = detection_items
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.detection_items:
            for v1 in self.detection_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        result['DetectionItems'] = []
        if self.detection_items is not None:
            for k1 in self.detection_items:
                result['DetectionItems'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        self.detection_items = []
        if m.get('DetectionItems') is not None:
            for k1 in m.get('DetectionItems'):
                temp_model = main_models.DescribeAbnormalPatternDetectionResponseBodyDetectionItems()
                self.detection_items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAbnormalPatternDetectionResponseBodyDetectionItems(DaraModel):
    def __init__(
        self,
        name: str = None,
        results: List[main_models.DescribeAbnormalPatternDetectionResponseBodyDetectionItemsResults] = None,
    ):
        # The name of the detection item.
        self.name = name
        # The detection result items.
        self.results = results

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.DescribeAbnormalPatternDetectionResponseBodyDetectionItemsResults()
                self.results.append(temp_model.from_map(k1))

        return self

class DescribeAbnormalPatternDetectionResponseBodyDetectionItemsResults(DaraModel):
    def __init__(
        self,
        access_ip: str = None,
        detail: str = None,
        failed_count: int = None,
        pattern_id: str = None,
        query_count: int = None,
        related_metrics: str = None,
        sqlpattern: str = None,
        tables: str = None,
        user: str = None,
    ):
        # The IP address of the SQL client that submits the SQL pattern.
        self.access_ip = access_ip
        # The description of the detection result.
        self.detail = detail
        # The number of failed SQL patterns within the time range.
        self.failed_count = failed_count
        # The SQL pattern ID.
        self.pattern_id = pattern_id
        # The number of queries.
        self.query_count = query_count
        # The metrics related to the SQL pattern.
        self.related_metrics = related_metrics
        # The SQL statement that represents the SQL pattern.
        self.sqlpattern = sqlpattern
        # The names of tables.
        self.tables = tables
        # The name of the database account that is used to submit the query.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_ip is not None:
            result['AccessIp'] = self.access_ip

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count

        if self.pattern_id is not None:
            result['PatternId'] = self.pattern_id

        if self.query_count is not None:
            result['QueryCount'] = self.query_count

        if self.related_metrics is not None:
            result['RelatedMetrics'] = self.related_metrics

        if self.sqlpattern is not None:
            result['SQLPattern'] = self.sqlpattern

        if self.tables is not None:
            result['Tables'] = self.tables

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessIp') is not None:
            self.access_ip = m.get('AccessIp')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')

        if m.get('PatternId') is not None:
            self.pattern_id = m.get('PatternId')

        if m.get('QueryCount') is not None:
            self.query_count = m.get('QueryCount')

        if m.get('RelatedMetrics') is not None:
            self.related_metrics = m.get('RelatedMetrics')

        if m.get('SQLPattern') is not None:
            self.sqlpattern = m.get('SQLPattern')

        if m.get('Tables') is not None:
            self.tables = m.get('Tables')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

