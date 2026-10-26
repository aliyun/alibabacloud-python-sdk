# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20260120 import models as main_models
from darabonba.model import DaraModel

class ListTablesResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.ListTablesResponseBodyItems] = None,
        marker: str = None,
        next_marker: str = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        truncated: str = None,
    ):
        # The page number of the returned data.
        self.current_page = current_page
        # The list of records returned by the query.
        self.items = items
        # The pagination cursor used for the current query.
        self.marker = marker
        # The cursor used to query the next page.
        self.next_marker = next_marker
        # The number of entries returned per page for the current query.
        self.page_size = page_size
        # The ID of the request. You can use the ID to locate the API call.
        self.request_id = request_id
        # The total number of entries that meet the current statistical or query scope.
        self.total_count = total_count
        # Indicates whether more pages exist. A value of true indicates that more data exists. A value of false indicates that no more data exists.
        self.truncated = truncated

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

        if self.marker is not None:
            result['Marker'] = self.marker

        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.truncated is not None:
            result['Truncated'] = self.truncated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListTablesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('Marker') is not None:
            self.marker = m.get('Marker')

        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('Truncated') is not None:
            self.truncated = m.get('Truncated')

        return self

class ListTablesResponseBodyItems(DaraModel):
    def __init__(
        self,
        comment: str = None,
        creation_time: int = None,
        data_asset_source_id: str = None,
        data_source_name: str = None,
        instance_description: str = None,
        name: str = None,
        owner: str = None,
        product_code: str = None,
        risk_level_id: int = None,
        risk_level_name: str = None,
        rule_list: List[main_models.ListTablesResponseBodyItemsRuleList] = None,
        sensitive: bool = None,
        sensitive_count: int = None,
        sensitive_ratio: str = None,
        tenant_name: str = None,
        total_count: int = None,
    ):
        # The description of the database table.
        self.comment = comment
        # The time when the data object was created. The value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.creation_time = creation_time
        # The instance identity of the cloud instance.
        self.data_asset_source_id = data_asset_source_id
        # The name of the database.
        self.data_source_name = data_source_name
        # The description of the database instance.
        self.instance_description = instance_description
        # The name of the database table. Some engines return the name in the schema.table format.
        self.name = name
        # The ID of the Alibaba Cloud account that owns the database table.
        self.owner = owner
        # The code of the cloud service.
        self.product_code = product_code
        # The ID of the sensitivity level.
        self.risk_level_id = risk_level_id
        # The name of the sensitivity level.
        self.risk_level_name = risk_level_name
        # The list of detection models or rules.
        self.rule_list = rule_list
        # Indicates whether the data is detected as sensitive data.
        self.sensitive = sensitive
        # The number of sensitive data entries within the current statistical scope.
        self.sensitive_count = sensitive_count
        # The proportion of sensitive data.
        self.sensitive_ratio = sensitive_ratio
        # The name of the tenant to which the data asset belongs.
        self.tenant_name = tenant_name
        # The total number of entries that meet the current statistical or query scope.
        self.total_count = total_count

    def validate(self):
        if self.rule_list:
            for v1 in self.rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.data_asset_source_id is not None:
            result['DataAssetSourceId'] = self.data_asset_source_id

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id

        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name

        result['RuleList'] = []
        if self.rule_list is not None:
            for k1 in self.rule_list:
                result['RuleList'].append(k1.to_map() if k1 else None)

        if self.sensitive is not None:
            result['Sensitive'] = self.sensitive

        if self.sensitive_count is not None:
            result['SensitiveCount'] = self.sensitive_count

        if self.sensitive_ratio is not None:
            result['SensitiveRatio'] = self.sensitive_ratio

        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DataAssetSourceId') is not None:
            self.data_asset_source_id = m.get('DataAssetSourceId')

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')

        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')

        self.rule_list = []
        if m.get('RuleList') is not None:
            for k1 in m.get('RuleList'):
                temp_model = main_models.ListTablesResponseBodyItemsRuleList()
                self.rule_list.append(temp_model.from_map(k1))

        if m.get('Sensitive') is not None:
            self.sensitive = m.get('Sensitive')

        if m.get('SensitiveCount') is not None:
            self.sensitive_count = m.get('SensitiveCount')

        if m.get('SensitiveRatio') is not None:
            self.sensitive_ratio = m.get('SensitiveRatio')

        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTablesResponseBodyItemsRuleList(DaraModel):
    def __init__(
        self,
        count: int = None,
        name: str = None,
        risk_level_id: int = None,
    ):
        # The number of hits for the detection rule.
        self.count = count
        # The name of the detection model or rule.
        self.name = name
        # The ID of the sensitivity level.
        self.risk_level_id = risk_level_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.name is not None:
            result['Name'] = self.name

        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')

        return self

