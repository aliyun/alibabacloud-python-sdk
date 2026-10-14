# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTablesRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        data_asset_source_id: str = None,
        data_source_name: str = None,
        lang: str = None,
        marker: int = None,
        name: str = None,
        page_size: int = None,
        product_code: str = None,
        product_id: int = None,
        risk_level_id: int = None,
        rule_id: int = None,
        template_id: int = None,
    ):
        # The current page number, starting from 1.
        self.current_page = current_page
        # The cloud database instance identity. Set this to the InstanceId value from the instance list.
        self.data_asset_source_id = data_asset_source_id
        # The database name. Set this to the DbName value returned by ListDataSources.
        self.data_source_name = data_source_name
        # The language of the response description. Valid values:
        # 
        # - zh: Chinese.
        # - en: English.
        self.lang = lang
        # The start position for cursor-based pagination. Use the NextMarker value returned from the previous request. Keep the original filter conditions consistent.
        self.marker = marker
        # The name filter condition.
        self.name = name
        # The number of records per page. Keep other filter conditions consistent when querying the next page.
        self.page_size = page_size
        # The cloud product code. Column encryption supports RDS, POLARDB, and PolarDBX2. If you also specify ProductId, the two values must correspond to each other.
        self.product_code = product_code
        # The cloud product type ID. Valid values:
        # 
        # - 5: ApsaraDB RDS.
        # - 8: PolarDB.
        # - 27: PolarDB-X 2.0.
        # 
        # If you specify both ProductId and ProductCode, the values must correspond to each other.
        self.product_id = product_id
        # The sensitivity level ID. You can obtain this value from the list returned by ListRiskLevels.
        self.risk_level_id = risk_level_id
        # The detection rule or model ID. Set this to the Id of the corresponding detection rule within the target template.
        self.rule_id = rule_id
        # The classification and grading template ID. You can obtain this value from Items[].Id returned by ListTemplates. Keep this value consistent with the selected sensitivity level and detection model.
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

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.marker is not None:
            result['Marker'] = self.marker

        if self.name is not None:
            result['Name'] = self.name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

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

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Marker') is not None:
            self.marker = m.get('Marker')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

