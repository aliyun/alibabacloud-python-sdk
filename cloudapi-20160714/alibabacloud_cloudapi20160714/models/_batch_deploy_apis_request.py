# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class BatchDeployApisRequest(DaraModel):
    def __init__(
        self,
        api: List[main_models.BatchDeployApisRequestApi] = None,
        description: str = None,
        security_token: str = None,
        stage_name: str = None,
    ):
        # The APIs that you want to publish.
        self.api = api
        # The description.
        # 
        # This parameter is required.
        self.description = description
        self.security_token = security_token
        # The name of the runtime environment. Valid values:
        # 
        # *   **RELEASE**
        # *   **TEST**
        # *   PRE: the pre-release environment
        # 
        # This parameter is required.
        self.stage_name = stage_name

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

        if self.description is not None:
            result['Description'] = self.description

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api = []
        if m.get('Api') is not None:
            for k1 in m.get('Api'):
                temp_model = main_models.BatchDeployApisRequestApi()
                self.api.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        return self

class BatchDeployApisRequestApi(DaraModel):
    def __init__(
        self,
        api_uid: str = None,
        group_id: str = None,
    ):
        # The API ID.
        # 
        # This parameter is required.
        self.api_uid = api_uid
        # The API group ID.
        # 
        # This parameter is required.
        self.group_id = group_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiUid') is not None:
            self.api_uid = m.get('ApiUid')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        return self

