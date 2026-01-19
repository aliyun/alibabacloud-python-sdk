# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class RemoveVpcAccessResponseBody(DaraModel):
    def __init__(
        self,
        apis: main_models.RemoveVpcAccessResponseBodyApis = None,
        request_id: str = None,
    ):
        # API operations
        self.apis = apis
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.apis:
            self.apis.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apis is not None:
            result['Apis'] = self.apis.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Apis') is not None:
            temp_model = main_models.RemoveVpcAccessResponseBodyApis()
            self.apis = temp_model.from_map(m.get('Apis'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class RemoveVpcAccessResponseBodyApis(DaraModel):
    def __init__(
        self,
        api: List[main_models.RemoveVpcAccessResponseBodyApisApi] = None,
    ):
        self.api = api

    def validate(self):
        if self.api:
            for v1 in self.api:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Api'] = []
        if self.api is not None:
            for k1 in self.api:
                result['Api'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api = []
        if m.get('Api') is not None:
            for k1 in m.get('Api'):
                temp_model = main_models.RemoveVpcAccessResponseBodyApisApi()
                self.api.append(temp_model.from_map(k1))

        return self

class RemoveVpcAccessResponseBodyApisApi(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        group_id: str = None,
        stage_id: str = None,
    ):
        # API Id
        self.api_id = api_id
        # The ID of the API group.
        self.group_id = group_id
        # The ID of the runtime environment.
        self.stage_id = stage_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.stage_id is not None:
            result['StageId'] = self.stage_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')

        return self

