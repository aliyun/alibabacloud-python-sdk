# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20260120 import models as main_models
from darabonba.model import DaraModel

class DeleteDataMaskingRuleRequest(DaraModel):
    def __init__(
        self,
        engine_type: str = None,
        instance_id: str = None,
        lang: str = None,
        product_code: str = None,
        product_id: int = None,
        sub_rule_list: List[main_models.DeleteDataMaskingRuleRequestSubRuleList] = None,
    ):
        self.engine_type = engine_type
        self.instance_id = instance_id
        self.lang = lang
        self.product_code = product_code
        self.product_id = product_id
        self.sub_rule_list = sub_rule_list

    def validate(self):
        if self.sub_rule_list:
            for v1 in self.sub_rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        result['SubRuleList'] = []
        if self.sub_rule_list is not None:
            for k1 in self.sub_rule_list:
                result['SubRuleList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        self.sub_rule_list = []
        if m.get('SubRuleList') is not None:
            for k1 in m.get('SubRuleList'):
                temp_model = main_models.DeleteDataMaskingRuleRequestSubRuleList()
                self.sub_rule_list.append(temp_model.from_map(k1))

        return self

class DeleteDataMaskingRuleRequestSubRuleList(DaraModel):
    def __init__(
        self,
        columns: str = None,
        db_name: str = None,
        table_name: str = None,
    ):
        self.columns = columns
        self.db_name = db_name
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.columns is not None:
            result['Columns'] = self.columns

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Columns') is not None:
            self.columns = m.get('Columns')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

