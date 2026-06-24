# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdatePipelineManagementConfigRequest(DaraModel):
    def __init__(
        self,
        endpoints: List[str] = None,
        es_instance_id: str = None,
        password: str = None,
        pipeline_ids: List[str] = None,
        pipeline_management_type: str = None,
        user_name: str = None,
        client_token: str = None,
    ):
        # The list of access addresses of the Elasticsearch instance where Kibana resides after Kibana pipeline management is enabled.
        self.endpoints = endpoints
        self.es_instance_id = es_instance_id
        # The password used to log on to Kibana.
        self.password = password
        # The list of pipelines managed by Kibana.
        self.pipeline_ids = pipeline_ids
        # The pipeline management method. Valid values:
        # 
        # - ES: Kibana pipeline management.
        # - MULTIPLE_PIPELINE: configuration file management.
        self.pipeline_management_type = pipeline_management_type
        # The username used to log on to Kibana.
        self.user_name = user_name
        # A unique token used to ensure idempotence of the request. The client generates this value. The value must be unique across different requests and can contain up to 64 ASCII characters.
        self.client_token = client_token

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

        if self.password is not None:
            result['password'] = self.password

        if self.pipeline_ids is not None:
            result['pipelineIds'] = self.pipeline_ids

        if self.pipeline_management_type is not None:
            result['pipelineManagementType'] = self.pipeline_management_type

        if self.user_name is not None:
            result['userName'] = self.user_name

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpoints') is not None:
            self.endpoints = m.get('endpoints')

        if m.get('esInstanceId') is not None:
            self.es_instance_id = m.get('esInstanceId')

        if m.get('password') is not None:
            self.password = m.get('password')

        if m.get('pipelineIds') is not None:
            self.pipeline_ids = m.get('pipelineIds')

        if m.get('pipelineManagementType') is not None:
            self.pipeline_management_type = m.get('pipelineManagementType')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        return self

