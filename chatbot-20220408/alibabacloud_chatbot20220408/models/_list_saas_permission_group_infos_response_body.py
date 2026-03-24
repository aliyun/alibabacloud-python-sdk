# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_chatbot20220408 import models as main_models
from darabonba.model import DaraModel

class ListSaasPermissionGroupInfosResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListSaasPermissionGroupInfosResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListSaasPermissionGroupInfosResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListSaasPermissionGroupInfosResponseBodyData(DaraModel):
    def __init__(
        self,
        en_name: str = None,
        name: str = None,
        pg_infos: List[main_models.ListSaasPermissionGroupInfosResponseBodyDataPgInfos] = None,
        saas_code: str = None,
    ):
        self.en_name = en_name
        self.name = name
        self.pg_infos = pg_infos
        self.saas_code = saas_code

    def validate(self):
        if self.pg_infos:
            for v1 in self.pg_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.en_name is not None:
            result['EnName'] = self.en_name

        if self.name is not None:
            result['Name'] = self.name

        result['PgInfos'] = []
        if self.pg_infos is not None:
            for k1 in self.pg_infos:
                result['PgInfos'].append(k1.to_map() if k1 else None)

        if self.saas_code is not None:
            result['SaasCode'] = self.saas_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnName') is not None:
            self.en_name = m.get('EnName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.pg_infos = []
        if m.get('PgInfos') is not None:
            for k1 in m.get('PgInfos'):
                temp_model = main_models.ListSaasPermissionGroupInfosResponseBodyDataPgInfos()
                self.pg_infos.append(temp_model.from_map(k1))

        if m.get('SaasCode') is not None:
            self.saas_code = m.get('SaasCode')

        return self

class ListSaasPermissionGroupInfosResponseBodyDataPgInfos(DaraModel):
    def __init__(
        self,
        pg_code: str = None,
        pg_en_name: str = None,
        pg_name: str = None,
    ):
        self.pg_code = pg_code
        self.pg_en_name = pg_en_name
        self.pg_name = pg_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pg_code is not None:
            result['PgCode'] = self.pg_code

        if self.pg_en_name is not None:
            result['PgEnName'] = self.pg_en_name

        if self.pg_name is not None:
            result['PgName'] = self.pg_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PgCode') is not None:
            self.pg_code = m.get('PgCode')

        if m.get('PgEnName') is not None:
            self.pg_en_name = m.get('PgEnName')

        if m.get('PgName') is not None:
            self.pg_name = m.get('PgName')

        return self

