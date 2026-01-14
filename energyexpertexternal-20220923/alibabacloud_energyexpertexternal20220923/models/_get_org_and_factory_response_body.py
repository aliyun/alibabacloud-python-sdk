# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class GetOrgAndFactoryResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetOrgAndFactoryResponseBodyData] = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The code returned for the request.
        self.code = code
        # data
        self.data = data
        # The HTTP status code.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.GetOrgAndFactoryResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetOrgAndFactoryResponseBodyData(DaraModel):
    def __init__(
        self,
        aliyun_pk: str = None,
        factory_list: List[main_models.GetOrgAndFactoryResponseBodyDataFactoryList] = None,
        organization_id: str = None,
        organization_name: str = None,
    ):
        # The Alibaba Cloud account ID.
        self.aliyun_pk = aliyun_pk
        # The sites.
        self.factory_list = factory_list
        # The enterprise ID.
        self.organization_id = organization_id
        # The enterprise name.
        self.organization_name = organization_name

    def validate(self):
        if self.factory_list:
            for v1 in self.factory_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_pk is not None:
            result['aliyunPk'] = self.aliyun_pk

        result['factoryList'] = []
        if self.factory_list is not None:
            for k1 in self.factory_list:
                result['factoryList'].append(k1.to_map() if k1 else None)

        if self.organization_id is not None:
            result['organizationId'] = self.organization_id

        if self.organization_name is not None:
            result['organizationName'] = self.organization_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliyunPk') is not None:
            self.aliyun_pk = m.get('aliyunPk')

        self.factory_list = []
        if m.get('factoryList') is not None:
            for k1 in m.get('factoryList'):
                temp_model = main_models.GetOrgAndFactoryResponseBodyDataFactoryList()
                self.factory_list.append(temp_model.from_map(k1))

        if m.get('organizationId') is not None:
            self.organization_id = m.get('organizationId')

        if m.get('organizationName') is not None:
            self.organization_name = m.get('organizationName')

        return self

class GetOrgAndFactoryResponseBodyDataFactoryList(DaraModel):
    def __init__(
        self,
        factory_id: str = None,
        factory_name: str = None,
    ):
        # The site ID.
        self.factory_id = factory_id
        # The site name.
        self.factory_name = factory_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.factory_id is not None:
            result['factoryId'] = self.factory_id

        if self.factory_name is not None:
            result['factoryName'] = self.factory_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('factoryId') is not None:
            self.factory_id = m.get('factoryId')

        if m.get('factoryName') is not None:
            self.factory_name = m.get('factoryName')

        return self

