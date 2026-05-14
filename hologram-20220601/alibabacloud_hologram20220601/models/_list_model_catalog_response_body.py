# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hologram20220601 import models as main_models
from darabonba.model import DaraModel

class ListModelCatalogResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        model_list: List[main_models.ListModelCatalogResponseBodyModelList] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # maxResults
        self.max_results = max_results
        self.model_list = model_list
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.model_list:
            for v1 in self.model_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        result['modelList'] = []
        if self.model_list is not None:
            for k1 in self.model_list:
                result['modelList'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        self.model_list = []
        if m.get('modelList') is not None:
            for k1 in m.get('modelList'):
                temp_model = main_models.ListModelCatalogResponseBodyModelList()
                self.model_list.append(temp_model.from_map(k1))

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListModelCatalogResponseBodyModelList(DaraModel):
    def __init__(
        self,
        default_params: str = None,
        extra: str = None,
        model_type: str = None,
        params_example: str = None,
        provider: str = None,
        service_deploy_region: str = None,
        task_type: str = None,
    ):
        self.default_params = default_params
        self.extra = extra
        self.model_type = model_type
        self.params_example = params_example
        self.provider = provider
        self.service_deploy_region = service_deploy_region
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_params is not None:
            result['defaultParams'] = self.default_params

        if self.extra is not None:
            result['extra'] = self.extra

        if self.model_type is not None:
            result['modelType'] = self.model_type

        if self.params_example is not None:
            result['paramsExample'] = self.params_example

        if self.provider is not None:
            result['provider'] = self.provider

        if self.service_deploy_region is not None:
            result['serviceDeployRegion'] = self.service_deploy_region

        if self.task_type is not None:
            result['taskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultParams') is not None:
            self.default_params = m.get('defaultParams')

        if m.get('extra') is not None:
            self.extra = m.get('extra')

        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')

        if m.get('paramsExample') is not None:
            self.params_example = m.get('paramsExample')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        if m.get('serviceDeployRegion') is not None:
            self.service_deploy_region = m.get('serviceDeployRegion')

        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')

        return self

