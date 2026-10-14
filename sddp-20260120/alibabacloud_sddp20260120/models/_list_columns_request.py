# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListColumnsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        data_asset_source_id: str = None,
        data_source_name: str = None,
        engine_type: str = None,
        instance_name: str = None,
        lang: str = None,
        name: str = None,
        page_size: int = None,
        product_code: str = None,
        risk_level_id: int = None,
        rule_id: int = None,
        table_name: str = None,
        template_id: int = None,
    ):
        # The current page number, starting from 1.
        self.current_page = current_page
        # The cloud database instance identity. Set this parameter to the InstanceId from the instance list.
        self.data_asset_source_id = data_asset_source_id
        # The database name. Set this parameter to the DbName returned by ListDataSources.
        self.data_source_name = data_source_name
        # The database engine type. This value must match the EngineType of the target instance, such as MySQL or PostgreSQL.
        self.engine_type = engine_type
        # The compatible parameter for the instance identity. DataAssetSourceId takes precedence. If both are specified, DataAssetSourceId is used.
        self.instance_name = instance_name
        # The language of the response description. Valid values:
        # - zh: Chinese.
        # - en: English.
        self.lang = lang
        # The column name filter condition.
        self.name = name
        # The number of records per page. Keep other filter conditions consistent when querying the next page.
        self.page_size = page_size
        # The cloud product code. Column encryption supports RDS, POLARDB, and PolarDBX2. If ProductId is also specified, the two values must correspond to each other.
        self.product_code = product_code
        # The sensitivity level ID. You can obtain this value from the list returned by ListRiskLevels.
        self.risk_level_id = risk_level_id
        # The ID of the detection rule or model. Set this parameter to the ID of the corresponding detection rule in the target template.
        self.rule_id = rule_id
        # The name of the data table. For PostgreSQL or Oracle scenarios, retain the schema.table format obtained from the table list.
        self.table_name = table_name
        # The ID of the classification and grading template. You can obtain this value from Items[].Id returned by ListTemplates. Ensure consistency with the selected sensitivity level and detection model.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.data_asset_source_id is not None:
            result['DataAssetSourceId'] = self.data_asset_source_id

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.name is not None:
            result['Name'] = self.name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DataAssetSourceId') is not None:
            self.data_asset_source_id = m.get('DataAssetSourceId')

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

