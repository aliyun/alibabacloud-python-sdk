# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_btripopen20220520 import models as main_models
from darabonba.model import DaraModel

class TripTaskQueryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        module: main_models.TripTaskQueryResponseBodyModule = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.code = code
        self.message = message
        # module。
        self.module = module
        self.request_id = request_id
        self.success = success
        # traceId
        self.trace_id = trace_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.module is not None:
            result['module'] = self.module.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.trace_id is not None:
            result['traceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('module') is not None:
            temp_model = main_models.TripTaskQueryResponseBodyModule()
            self.module = temp_model.from_map(m.get('module'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')

        return self

class TripTaskQueryResponseBodyModule(DaraModel):
    def __init__(
        self,
        need_refresh: bool = None,
        record_tasks: List[main_models.TripTaskQueryResponseBodyModuleRecordTasks] = None,
        running_tasks: List[main_models.TripTaskQueryResponseBodyModuleRunningTasks] = None,
    ):
        self.need_refresh = need_refresh
        self.record_tasks = record_tasks
        self.running_tasks = running_tasks

    def validate(self):
        if self.record_tasks:
            for v1 in self.record_tasks:
                 if v1:
                    v1.validate()
        if self.running_tasks:
            for v1 in self.running_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.need_refresh is not None:
            result['needRefresh'] = self.need_refresh

        result['record_tasks'] = []
        if self.record_tasks is not None:
            for k1 in self.record_tasks:
                result['record_tasks'].append(k1.to_map() if k1 else None)

        result['running_tasks'] = []
        if self.running_tasks is not None:
            for k1 in self.running_tasks:
                result['running_tasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('needRefresh') is not None:
            self.need_refresh = m.get('needRefresh')

        self.record_tasks = []
        if m.get('record_tasks') is not None:
            for k1 in m.get('record_tasks'):
                temp_model = main_models.TripTaskQueryResponseBodyModuleRecordTasks()
                self.record_tasks.append(temp_model.from_map(k1))

        self.running_tasks = []
        if m.get('running_tasks') is not None:
            for k1 in m.get('running_tasks'):
                temp_model = main_models.TripTaskQueryResponseBodyModuleRunningTasks()
                self.running_tasks.append(temp_model.from_map(k1))

        return self

class TripTaskQueryResponseBodyModuleRunningTasks(DaraModel):
    def __init__(
        self,
        actioner: str = None,
        attributes: str = None,
        gmt_create: int = None,
        gmt_finished: int = None,
        id: int = None,
        node_id: str = None,
        out_result: str = None,
        owner: str = None,
        status: str = None,
    ):
        self.actioner = actioner
        self.attributes = attributes
        self.gmt_create = gmt_create
        self.gmt_finished = gmt_finished
        self.id = id
        self.node_id = node_id
        self.out_result = out_result
        self.owner = owner
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actioner is not None:
            result['actioner'] = self.actioner

        if self.attributes is not None:
            result['attributes'] = self.attributes

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.gmt_finished is not None:
            result['gmt_finished'] = self.gmt_finished

        if self.id is not None:
            result['id'] = self.id

        if self.node_id is not None:
            result['node_id'] = self.node_id

        if self.out_result is not None:
            result['out_result'] = self.out_result

        if self.owner is not None:
            result['owner'] = self.owner

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actioner') is not None:
            self.actioner = m.get('actioner')

        if m.get('attributes') is not None:
            self.attributes = m.get('attributes')

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('gmt_finished') is not None:
            self.gmt_finished = m.get('gmt_finished')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('node_id') is not None:
            self.node_id = m.get('node_id')

        if m.get('out_result') is not None:
            self.out_result = m.get('out_result')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class TripTaskQueryResponseBodyModuleRecordTasks(DaraModel):
    def __init__(
        self,
        actioner: str = None,
        attributes: str = None,
        gmt_create: int = None,
        gmt_finished: int = None,
        id: int = None,
        node_id: str = None,
        out_result: str = None,
        owner: str = None,
        status: str = None,
    ):
        self.actioner = actioner
        self.attributes = attributes
        self.gmt_create = gmt_create
        self.gmt_finished = gmt_finished
        self.id = id
        self.node_id = node_id
        self.out_result = out_result
        self.owner = owner
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actioner is not None:
            result['actioner'] = self.actioner

        if self.attributes is not None:
            result['attributes'] = self.attributes

        if self.gmt_create is not None:
            result['gmt_create'] = self.gmt_create

        if self.gmt_finished is not None:
            result['gmt_finished'] = self.gmt_finished

        if self.id is not None:
            result['id'] = self.id

        if self.node_id is not None:
            result['node_id'] = self.node_id

        if self.out_result is not None:
            result['out_result'] = self.out_result

        if self.owner is not None:
            result['owner'] = self.owner

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actioner') is not None:
            self.actioner = m.get('actioner')

        if m.get('attributes') is not None:
            self.attributes = m.get('attributes')

        if m.get('gmt_create') is not None:
            self.gmt_create = m.get('gmt_create')

        if m.get('gmt_finished') is not None:
            self.gmt_finished = m.get('gmt_finished')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('node_id') is not None:
            self.node_id = m.get('node_id')

        if m.get('out_result') is not None:
            self.out_result = m.get('out_result')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

