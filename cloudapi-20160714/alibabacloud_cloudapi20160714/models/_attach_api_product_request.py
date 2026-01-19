# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class AttachApiProductRequest(DaraModel):
    def __init__(
        self,
        api_product_id: str = None,
        apis: List[main_models.AttachApiProductRequestApis] = None,
        security_token: str = None,
    ):
        # The ID of the API product.
        # 
        # This parameter is required.
        self.api_product_id = api_product_id
        # The APIs to be attached.
        # 
        # This parameter is required.
        self.apis = apis
        self.security_token = security_token

    def validate(self):
        if self.apis:
            for v1 in self.apis:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_product_id is not None:
            result['ApiProductId'] = self.api_product_id

        result['Apis'] = []
        if self.apis is not None:
            for k1 in self.apis:
                result['Apis'].append(k1.to_map() if k1 else None)

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiProductId') is not None:
            self.api_product_id = m.get('ApiProductId')

        self.apis = []
        if m.get('Apis') is not None:
            for k1 in m.get('Apis'):
                temp_model = main_models.AttachApiProductRequestApis()
                self.apis.append(temp_model.from_map(k1))

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        return self



class AttachApiProductRequestApis(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        stage_name: str = None,
    ):
        # The API ID.
        # 
        # This parameter is required.
        self.api_id = api_id
        # The environment. Valid values:
        # 
        # *   **RELEASE**: the production environment
        # *   **PRE**: the staging environment
        # *   **TEST**: the test environment
        # 
        # This parameter is required.
        self.stage_name = stage_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        return self

