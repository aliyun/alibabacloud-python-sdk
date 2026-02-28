# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_rtc20180111 import models as main_models
from darabonba.model import DaraModel

class DescribeEndPointMetricDataResponseBody(DaraModel):
    def __init__(
        self,
        pub_metrics: List[main_models.DescribeEndPointMetricDataResponseBodyPubMetrics] = None,
        request_id: str = None,
        sub_metrics: List[main_models.DescribeEndPointMetricDataResponseBodySubMetrics] = None,
    ):
        self.pub_metrics = pub_metrics
        self.request_id = request_id
        self.sub_metrics = sub_metrics

    def validate(self):
        if self.pub_metrics:
            for v1 in self.pub_metrics:
                 if v1:
                    v1.validate()
        if self.sub_metrics:
            for v1 in self.sub_metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PubMetrics'] = []
        if self.pub_metrics is not None:
            for k1 in self.pub_metrics:
                result['PubMetrics'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SubMetrics'] = []
        if self.sub_metrics is not None:
            for k1 in self.sub_metrics:
                result['SubMetrics'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pub_metrics = []
        if m.get('PubMetrics') is not None:
            for k1 in m.get('PubMetrics'):
                temp_model = main_models.DescribeEndPointMetricDataResponseBodyPubMetrics()
                self.pub_metrics.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sub_metrics = []
        if m.get('SubMetrics') is not None:
            for k1 in m.get('SubMetrics'):
                temp_model = main_models.DescribeEndPointMetricDataResponseBodySubMetrics()
                self.sub_metrics.append(temp_model.from_map(k1))

        return self

class DescribeEndPointMetricDataResponseBodySubMetrics(DaraModel):
    def __init__(
        self,
        nodes: List[main_models.DescribeEndPointMetricDataResponseBodySubMetricsNodes] = None,
        type: str = None,
        user_id: str = None,
    ):
        self.nodes = nodes
        self.type = type
        self.user_id = user_id

    def validate(self):
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.DescribeEndPointMetricDataResponseBodySubMetricsNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class DescribeEndPointMetricDataResponseBodySubMetricsNodes(DaraModel):
    def __init__(
        self,
        ext: Dict[str, Any] = None,
        x: str = None,
        y: str = None,
    ):
        self.ext = ext
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ext is not None:
            result['Ext'] = self.ext

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

class DescribeEndPointMetricDataResponseBodyPubMetrics(DaraModel):
    def __init__(
        self,
        nodes: List[main_models.DescribeEndPointMetricDataResponseBodyPubMetricsNodes] = None,
        type: str = None,
        user_id: str = None,
    ):
        self.nodes = nodes
        self.type = type
        self.user_id = user_id

    def validate(self):
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.DescribeEndPointMetricDataResponseBodyPubMetricsNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class DescribeEndPointMetricDataResponseBodyPubMetricsNodes(DaraModel):
    def __init__(
        self,
        ext: Dict[str, Any] = None,
        x: str = None,
        y: str = None,
    ):
        self.ext = ext
        self.x = x
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ext is not None:
            result['Ext'] = self.ext

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        return self

