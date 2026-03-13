# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sophonsoar20220728 import models as main_models
from darabonba.model import DaraModel

class DescribeNodeParamTagsResponseBody(DaraModel):
    def __init__(
        self,
        param_referred_paths: List[main_models.DescribeNodeParamTagsResponseBodyParamReferredPaths] = None,
        request_id: str = None,
    ):
        # The configuration of the recommended path.
        self.param_referred_paths = param_referred_paths
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.param_referred_paths:
            for v1 in self.param_referred_paths:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ParamReferredPaths'] = []
        if self.param_referred_paths is not None:
            for k1 in self.param_referred_paths:
                result['ParamReferredPaths'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.param_referred_paths = []
        if m.get('ParamReferredPaths') is not None:
            for k1 in m.get('ParamReferredPaths'):
                temp_model = main_models.DescribeNodeParamTagsResponseBodyParamReferredPaths()
                self.param_referred_paths.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeNodeParamTagsResponseBodyParamReferredPaths(DaraModel):
    def __init__(
        self,
        param_name: str = None,
        referred_path: List[str] = None,
    ):
        # The name of the upstream node.
        self.param_name = param_name
        # The paths.
        self.referred_path = referred_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.param_name is not None:
            result['ParamName'] = self.param_name

        if self.referred_path is not None:
            result['ReferredPath'] = self.referred_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')

        if m.get('ReferredPath') is not None:
            self.referred_path = m.get('ReferredPath')

        return self

