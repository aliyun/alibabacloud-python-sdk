# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class ListAbnormalyEventsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListAbnormalyEventsResponseBodyData] = None,
        message: str = None,
        total: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListAbnormalyEventsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListAbnormalyEventsResponseBodyData(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        description: str = None,
        diag_status: int = None,
        end_at: int = None,
        instance: str = None,
        item: str = None,
        level: str = None,
        namespace: str = None,
        opts: List[main_models.ListAbnormalyEventsResponseBodyDataOpts] = None,
        pod: str = None,
        raw_metrics: main_models.ListAbnormalyEventsResponseBodyDataRawMetrics = None,
        region_id: str = None,
        type: str = None,
        uuid: str = None,
    ):
        self.created_at = created_at
        self.description = description
        self.diag_status = diag_status
        self.end_at = end_at
        self.instance = instance
        self.item = item
        self.level = level
        self.namespace = namespace
        self.opts = opts
        self.pod = pod
        self.raw_metrics = raw_metrics
        self.region_id = region_id
        self.type = type
        self.uuid = uuid

    def validate(self):
        if self.opts:
            for v1 in self.opts:
                 if v1:
                    v1.validate()
        if self.raw_metrics:
            self.raw_metrics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.diag_status is not None:
            result['diag_status'] = self.diag_status

        if self.end_at is not None:
            result['end_at'] = self.end_at

        if self.instance is not None:
            result['instance'] = self.instance

        if self.item is not None:
            result['item'] = self.item

        if self.level is not None:
            result['level'] = self.level

        if self.namespace is not None:
            result['namespace'] = self.namespace

        result['opts'] = []
        if self.opts is not None:
            for k1 in self.opts:
                result['opts'].append(k1.to_map() if k1 else None)

        if self.pod is not None:
            result['pod'] = self.pod

        if self.raw_metrics is not None:
            result['raw_metrics'] = self.raw_metrics.to_map()

        if self.region_id is not None:
            result['region_id'] = self.region_id

        if self.type is not None:
            result['type'] = self.type

        if self.uuid is not None:
            result['uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('diag_status') is not None:
            self.diag_status = m.get('diag_status')

        if m.get('end_at') is not None:
            self.end_at = m.get('end_at')

        if m.get('instance') is not None:
            self.instance = m.get('instance')

        if m.get('item') is not None:
            self.item = m.get('item')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        self.opts = []
        if m.get('opts') is not None:
            for k1 in m.get('opts'):
                temp_model = main_models.ListAbnormalyEventsResponseBodyDataOpts()
                self.opts.append(temp_model.from_map(k1))

        if m.get('pod') is not None:
            self.pod = m.get('pod')

        if m.get('raw_metrics') is not None:
            temp_model = main_models.ListAbnormalyEventsResponseBodyDataRawMetrics()
            self.raw_metrics = temp_model.from_map(m.get('raw_metrics'))

        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')

        return self

class ListAbnormalyEventsResponseBodyDataRawMetrics(DaraModel):
    def __init__(
        self,
        end_time: float = None,
        metrics: List[str] = None,
        start_time: float = None,
    ):
        self.end_time = end_time
        self.metrics = metrics
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['end_time'] = self.end_time

        if self.metrics is not None:
            result['metrics'] = self.metrics

        if self.start_time is not None:
            result['start_time'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')

        if m.get('metrics') is not None:
            self.metrics = m.get('metrics')

        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')

        return self

class ListAbnormalyEventsResponseBodyDataOpts(DaraModel):
    def __init__(
        self,
        label: str = None,
        result: main_models.ListAbnormalyEventsResponseBodyDataOptsResult = None,
        type: str = None,
    ):
        self.label = label
        self.result = result
        self.type = type

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.label is not None:
            result['label'] = self.label

        if self.result is not None:
            result['result'] = self.result.to_map()

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('label') is not None:
            self.label = m.get('label')

        if m.get('result') is not None:
            temp_model = main_models.ListAbnormalyEventsResponseBodyDataOptsResult()
            self.result = temp_model.from_map(m.get('result'))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListAbnormalyEventsResponseBodyDataOptsResult(DaraModel):
    def __init__(
        self,
        status: str = None,
        url: str = None,
    ):
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['status'] = self.status

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

