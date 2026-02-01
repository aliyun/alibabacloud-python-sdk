# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class ListInstancesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListInstancesResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        total: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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

        if self.request_id is not None:
            result['request_id'] = self.request_id

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
                temp_model = main_models.ListInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListInstancesResponseBodyData(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        instance: str = None,
        kernel_version: str = None,
        meta: Any = None,
        os_arch: str = None,
        os_health_score: str = None,
        os_name: str = None,
        os_name_id: str = None,
        os_version: str = None,
        os_version_id: str = None,
        region: str = None,
        status: str = None,
    ):
        self.cluster_id = cluster_id
        self.instance = instance
        self.kernel_version = kernel_version
        self.meta = meta
        self.os_arch = os_arch
        self.os_health_score = os_health_score
        self.os_name = os_name
        self.os_name_id = os_name_id
        self.os_version = os_version
        self.os_version_id = os_version_id
        self.region = region
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.instance is not None:
            result['instance'] = self.instance

        if self.kernel_version is not None:
            result['kernel_version'] = self.kernel_version

        if self.meta is not None:
            result['meta'] = self.meta

        if self.os_arch is not None:
            result['os_arch'] = self.os_arch

        if self.os_health_score is not None:
            result['os_health_score'] = self.os_health_score

        if self.os_name is not None:
            result['os_name'] = self.os_name

        if self.os_name_id is not None:
            result['os_name_id'] = self.os_name_id

        if self.os_version is not None:
            result['os_version'] = self.os_version

        if self.os_version_id is not None:
            result['os_version_id'] = self.os_version_id

        if self.region is not None:
            result['region'] = self.region

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('instance') is not None:
            self.instance = m.get('instance')

        if m.get('kernel_version') is not None:
            self.kernel_version = m.get('kernel_version')

        if m.get('meta') is not None:
            self.meta = m.get('meta')

        if m.get('os_arch') is not None:
            self.os_arch = m.get('os_arch')

        if m.get('os_health_score') is not None:
            self.os_health_score = m.get('os_health_score')

        if m.get('os_name') is not None:
            self.os_name = m.get('os_name')

        if m.get('os_name_id') is not None:
            self.os_name_id = m.get('os_name_id')

        if m.get('os_version') is not None:
            self.os_version = m.get('os_version')

        if m.get('os_version_id') is not None:
            self.os_version_id = m.get('os_version_id')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

