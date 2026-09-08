# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDataMaskingInstancesRequest(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        current_page: int = None,
        db_name: str = None,
        engine_type: str = None,
        instance_id: str = None,
        lang: str = None,
        masking_status: str = None,
        model_tag_id: str = None,
        page_size: int = None,
        product_code: str = None,
        product_id: int = None,
        product_ids: str = None,
        risk_level_id: int = None,
        risk_level_ids: str = None,
        table_name: str = None,
        template_id: int = None,
        template_rule_ids: str = None,
    ):
        self.column_name = column_name
        self.current_page = current_page
        self.db_name = db_name
        self.engine_type = engine_type
        self.instance_id = instance_id
        self.lang = lang
        self.masking_status = masking_status
        self.model_tag_id = model_tag_id
        self.page_size = page_size
        self.product_code = product_code
        self.product_id = product_id
        self.product_ids = product_ids
        self.risk_level_id = risk_level_id
        self.risk_level_ids = risk_level_ids
        self.table_name = table_name
        self.template_id = template_id
        self.template_rule_ids = template_rule_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.masking_status is not None:
            result['MaskingStatus'] = self.masking_status

        if self.model_tag_id is not None:
            result['ModelTagId'] = self.model_tag_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.product_ids is not None:
            result['ProductIds'] = self.product_ids

        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id

        if self.risk_level_ids is not None:
            result['RiskLevelIds'] = self.risk_level_ids

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_rule_ids is not None:
            result['TemplateRuleIds'] = self.template_rule_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MaskingStatus') is not None:
            self.masking_status = m.get('MaskingStatus')

        if m.get('ModelTagId') is not None:
            self.model_tag_id = m.get('ModelTagId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('ProductIds') is not None:
            self.product_ids = m.get('ProductIds')

        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')

        if m.get('RiskLevelIds') is not None:
            self.risk_level_ids = m.get('RiskLevelIds')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateRuleIds') is not None:
            self.template_rule_ids = m.get('TemplateRuleIds')

        return self

