# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class DescribeXpackMonitorConfigResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.DescribeXpackMonitorConfigResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.DescribeXpackMonitorConfigResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class DescribeXpackMonitorConfigResponseBodyResult(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        endpoints: List[str] = None,
        es_instance_id: str = None,
        pipeline_ids: List[str] = None,
        user_name: str = None,
    ):
        # Indicates whether the X-Pack Monitoring feature is enabled. Valid values:
        # 
        # *   true: enabled
        # *   false: disabled
        self.enable = enable
        self.endpoints = endpoints
        # The ID of the associated Elasticsearch cluster.
        self.es_instance_id = es_instance_id
        self.pipeline_ids = pipeline_ids
        # The username that is used to access the associated Elasticsearch cluster.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['enable'] = self.enable

        if self.endpoints is not None:
            result['endpoints'] = self.endpoints

        if self.es_instance_id is not None:
            result['esInstanceId'] = self.es_instance_id

        if self.pipeline_ids is not None:
            result['pipelineIds'] = self.pipeline_ids

        if self.user_name is not None:
            result['userName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('endpoints') is not None:
            self.endpoints = m.get('endpoints')

        if m.get('esInstanceId') is not None:
            self.es_instance_id = m.get('esInstanceId')

        if m.get('pipelineIds') is not None:
            self.pipeline_ids = m.get('pipelineIds')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        return self

