# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class BatchAbolishApisRequest(DaraModel):
    def __init__(
        self,
        api: List[main_models.BatchAbolishApisRequestApi] = None,
        security_token: str = None,
    ):
        # The APIs that you want to operate.
        # 
        # This parameter is required.
        self.api = api
        self.security_token = security_token

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

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api = []
        if m.get('Api') is not None:
            for k1 in m.get('Api'):
                temp_model = main_models.BatchAbolishApisRequestApi()
                self.api.append(temp_model.from_map(k1))

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self

class BatchAbolishApisRequestApi(DaraModel):
    def __init__(
        self,
        api_uid: str = None,
        group_id: str = None,
        stage_id: str = None,
        stage_name: str = None,
    ):
        # The ID of the API.
        # 
        # This parameter is required.
        self.api_uid = api_uid
        # The ID of the API group.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the environment.
        self.stage_id = stage_id
        # The name of the environment.
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_uid is not None:
            result['ApiUid'] = self.api_uid

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.stage_id is not None:
            result['StageId'] = self.stage_id

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiUid') is not None:
            self.api_uid = m.get('ApiUid')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        return self

