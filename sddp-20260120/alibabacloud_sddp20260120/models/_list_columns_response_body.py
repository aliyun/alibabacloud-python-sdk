# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20260120 import models as main_models
from darabonba.model import DaraModel

class ListColumnsResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.ListColumnsResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned data.
        self.current_page = current_page
        # The list of records returned by the current query.
        self.items = items
        # The number of entries returned per page in the current query.
        self.page_size = page_size
        # The request ID, which can be used to locate the current API call.
        self.request_id = request_id
        # The total number of entries that meet the current statistics or query scope.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListColumnsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListColumnsResponseBodyItems(DaraModel):
    def __init__(
        self,
        creation_time: int = None,
        data_asset_source_id: str = None,
        data_source_name: str = None,
        data_type: str = None,
        engine_type: str = None,
        instance_name: str = None,
        masking_status: int = None,
        name: str = None,
        product_code: str = None,
        region_id: str = None,
        revision_id: int = None,
        revision_status: int = None,
        risk_level_id: int = None,
        risk_level_name: str = None,
        rule_id: int = None,
        rule_name: str = None,
        schema_name: str = None,
        sensitive: bool = None,
        table_name: str = None,
    ):
        # The creation time of the data object. The value is a UNIX timestamp in milliseconds since 1970-01-01 00:00:00 UTC.
        self.creation_time = creation_time
        # The cloud instance identity.
        self.data_asset_source_id = data_asset_source_id
        # The name of the database.
        self.data_source_name = data_source_name
        # The data type of the database column.
        self.data_type = data_type
        # The type of the database engine.
        self.engine_type = engine_type
        # The instance identity of the cloud instance to which the column belongs. This is a compatible field.
        self.instance_name = instance_name
        # The compatibility field for the column encryption status. To query column encryption results, call ListDataMaskingColumns.
        self.masking_status = masking_status
        # The name of the data column.
        self.name = name
        # The code of the cloud service.
        self.product_code = product_code
        # The ID of the region where the asset is located.
        self.region_id = region_id
        # The identifier of the detection result correction record.
        self.revision_id = revision_id
        # The correction status of the detection result. Valid values: 0: Not corrected. 1: Corrected.
        self.revision_status = revision_status
        # The identifier of the sensitivity level.
        self.risk_level_id = risk_level_id
        # The name of the sensitivity level.
        self.risk_level_name = risk_level_name
        # The identifier of the matched detection rule.
        self.rule_id = rule_id
        # The name of the matched detection rule.
        self.rule_name = rule_name
        # The name of the database schema.
        self.schema_name = schema_name
        # Indicates whether the data is detected as sensitive data.
        self.sensitive = sensitive
        # The name of the data table.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.data_asset_source_id is not None:
            result['DataAssetSourceId'] = self.data_asset_source_id

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.masking_status is not None:
            result['MaskingStatus'] = self.masking_status

        if self.name is not None:
            result['Name'] = self.name

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.revision_id is not None:
            result['RevisionId'] = self.revision_id

        if self.revision_status is not None:
            result['RevisionStatus'] = self.revision_status

        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id

        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.sensitive is not None:
            result['Sensitive'] = self.sensitive

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DataAssetSourceId') is not None:
            self.data_asset_source_id = m.get('DataAssetSourceId')

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('MaskingStatus') is not None:
            self.masking_status = m.get('MaskingStatus')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RevisionId') is not None:
            self.revision_id = m.get('RevisionId')

        if m.get('RevisionStatus') is not None:
            self.revision_status = m.get('RevisionStatus')

        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')

        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('Sensitive') is not None:
            self.sensitive = m.get('Sensitive')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

