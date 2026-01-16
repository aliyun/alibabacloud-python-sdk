# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListAvailableEsInstanceIdsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListAvailableEsInstanceIdsResponseBodyResult] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListAvailableEsInstanceIdsResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListAvailableEsInstanceIdsResponseBodyResult(DaraModel):
    def __init__(
        self,
        description: str = None,
        endpoint: str = None,
        es_instance_id: str = None,
        kibana_endpoint: str = None,
    ):
        # The name of the Elasticsearch cluster.
        self.description = description
        # The address that is used to access the Elasticsearch cluster over the Internet.
        self.endpoint = endpoint
        # The ID of the Elasticsearch cluster.
        self.es_instance_id = es_instance_id
        # The address that is used to access the Kibana console of the Elasticsearch cluster over the Internet.
        self.kibana_endpoint = kibana_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.es_instance_id is not None:
            result['esInstanceId'] = self.es_instance_id

        if self.kibana_endpoint is not None:
            result['kibanaEndpoint'] = self.kibana_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('esInstanceId') is not None:
            self.es_instance_id = m.get('esInstanceId')

        if m.get('kibanaEndpoint') is not None:
            self.kibana_endpoint = m.get('kibanaEndpoint')

        return self

