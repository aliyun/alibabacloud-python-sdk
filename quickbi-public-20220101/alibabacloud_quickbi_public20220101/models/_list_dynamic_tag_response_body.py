# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class ListDynamicTagResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListDynamicTagResponseBodyResult] = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result = result
        self.success = success

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

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListDynamicTagResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDynamicTagResponseBodyResult(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        config_id: str = None,
        config_name: str = None,
        ds_id: str = None,
        organization_id: str = None,
        related_attribute: int = None,
        table_name: str = None,
    ):
        self.column_name = column_name
        self.config_id = config_id
        self.config_name = config_name
        self.ds_id = ds_id
        self.organization_id = organization_id
        self.related_attribute = related_attribute
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.config_name is not None:
            result['ConfigName'] = self.config_name

        if self.ds_id is not None:
            result['DsId'] = self.ds_id

        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id

        if self.related_attribute is not None:
            result['RelatedAttribute'] = self.related_attribute

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')

        if m.get('DsId') is not None:
            self.ds_id = m.get('DsId')

        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')

        if m.get('RelatedAttribute') is not None:
            self.related_attribute = m.get('RelatedAttribute')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

