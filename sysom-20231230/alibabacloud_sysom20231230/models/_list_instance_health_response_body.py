# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sysom20231230 import models as main_models
from darabonba.model import DaraModel

class ListInstanceHealthResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListInstanceHealthResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        total: int = None,
    ):
        # The status code.
        # - If `code == Success`, the authorization is successful.
        # - Other status codes indicate authorization failed. Check the `message` field for the detailed fault information.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        # - If `code == Success`, this field is empty.
        # - Otherwise, this field contains the request error information.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The total number of query results.
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
                temp_model = main_models.ListInstanceHealthResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListInstanceHealthResponseBodyData(DaraModel):
    def __init__(
        self,
        images: List[str] = None,
        instance: str = None,
        namespace: str = None,
        pod: str = None,
        region_id: str = None,
        score: float = None,
        status: str = None,
    ):
        # The list of container image names in the Pod.
        self.images = images
        # The instance ID.
        self.instance = instance
        # The namespace of the Pod.
        self.namespace = namespace
        # The Pod name.
        self.pod = pod
        # The region ID.
        self.region_id = region_id
        # The health score.
        self.score = score
        # The running status of the instance. Valid values:
        # - **Running**: running.
        # - **Offline**: offline.
        # 
        # 
        # 
        # > An instance in the Offline status indicates that the heartbeat between the node and the SysOM server is lost. It does not mean that the corresponding ECS instance is not running.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.images is not None:
            result['images'] = self.images

        if self.instance is not None:
            result['instance'] = self.instance

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.pod is not None:
            result['pod'] = self.pod

        if self.region_id is not None:
            result['region_id'] = self.region_id

        if self.score is not None:
            result['score'] = self.score

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('images') is not None:
            self.images = m.get('images')

        if m.get('instance') is not None:
            self.instance = m.get('instance')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('pod') is not None:
            self.pod = m.get('pod')

        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')

        if m.get('score') is not None:
            self.score = m.get('score')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

