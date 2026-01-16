# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class DescribePipelineManagementConfigResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.DescribePipelineManagementConfigResponseBodyResult = None,
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
            temp_model = main_models.DescribePipelineManagementConfigResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class DescribePipelineManagementConfigResponseBodyResult(DaraModel):
    def __init__(
        self,
        endpoints: str = None,
        es_instance_id: str = None,
        pipeline_ids: List[str] = None,
        pipeline_management_type: str = None,
        user_name: str = None,
    ):
        # The access addresses of the Elasticsearch cluster. Specify each address in the `http://Endpoint of the Elasticsearch cluster:Port number` format.
        self.endpoints = endpoints
        # The ID of the Elasticsearch cluster.
        self.es_instance_id = es_instance_id
        self.pipeline_ids = pipeline_ids
        # The pipeline management method. Valid values: Kibana and MULTIPLE_PIPELINE.
        self.pipeline_management_type = pipeline_management_type
        # The username that is used to access the Elasticsearch cluster.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoints is not None:
            result['endpoints'] = self.endpoints

        if self.es_instance_id is not None:
            result['esInstanceId'] = self.es_instance_id

        if self.pipeline_ids is not None:
            result['pipelineIds'] = self.pipeline_ids

        if self.pipeline_management_type is not None:
            result['pipelineManagementType'] = self.pipeline_management_type

        if self.user_name is not None:
            result['userName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpoints') is not None:
            self.endpoints = m.get('endpoints')

        if m.get('esInstanceId') is not None:
            self.es_instance_id = m.get('esInstanceId')

        if m.get('pipelineIds') is not None:
            self.pipeline_ids = m.get('pipelineIds')

        if m.get('pipelineManagementType') is not None:
            self.pipeline_management_type = m.get('pipelineManagementType')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        return self

