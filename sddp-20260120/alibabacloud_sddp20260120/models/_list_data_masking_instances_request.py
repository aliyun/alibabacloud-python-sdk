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
        # The column name filter condition.
        self.column_name = column_name
        # The page number of the current query. Pages start from 1.
        self.current_page = current_page
        # The name of the database.
        self.db_name = db_name
        # The database engine type. The value must match the EngineType of the target instance, such as MySQL or PostgreSQL.
        self.engine_type = engine_type
        # The instance identity of the database instance. You can obtain the value from Items[].InstanceId in the response of ListDataMaskingInstances.
        self.instance_id = instance_id
        # The language of the response description. Valid values:
        # - zh: Chinese.
        # - en: English.
        self.lang = lang
        # The column encryption status used for filtering. Valid values:
        # - NotEncrypted: Not encrypted.
        # - Success: Encryption succeeded.
        # - Failed: Encryption failed.
        self.masking_status = masking_status
        # The ID of the model tag. This parameter is used to limit the data to those that match the specified model tag.
        self.model_tag_id = model_tag_id
        # The number of records per page. Keep other filter conditions consistent when querying the next page.
        self.page_size = page_size
        # The code of the cloud product. Column encryption supports RDS, POLARDB, and PolarDBX2. If you also specify ProductId, the two values must correspond to each other.
        self.product_code = product_code
        # The ID of the cloud product type. Valid values: 5 (RDS), 8 (POLARDB), and 27 (PolarDBX2). If you specify both ProductId and ProductCode, the values must correspond to each other.
        self.product_id = product_id
        # The list of cloud product type IDs. Separate multiple values with commas (,). Valid values for column encryption: 5 (RDS), 8 (POLARDB), and 27 (PolarDBX2).
        self.product_ids = product_ids
        # The ID of the sensitivity level. You can obtain the value from the response of ListRiskLevels.
        self.risk_level_id = risk_level_id
        # The list of sensitivity level IDs. Separate multiple values with commas (,). Select values from the response of ListRiskLevels that corresponds to the same TemplateId.
        self.risk_level_ids = risk_level_ids
        # The name of the table. For PostgreSQL or Oracle scenarios, retain the schema.table format obtained from the table list.
        self.table_name = table_name
        # The ID of the classification and grading template. You can obtain the value from Items[].Id in the response of ListTemplates. The value must be consistent with the selected sensitivity level and detection model.
        self.template_id = template_id
        # The list of detection model IDs. Separate multiple values with commas (,). Select values from the response of ListIdentifyModels that corresponds to the same TemplateId.
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

