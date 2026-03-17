# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDpiConfigErrorRequest(DaraModel):
    def __init__(
        self,
        dpi_config_type: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        rule_instance_id: str = None,
        smart_agid: str = None,
    ):
        # The type of the instance for which the DPI feature is configured. Valid values:
        # 
        # *   **acl**
        # *   **qos**
        # 
        # This parameter is required.
        self.dpi_config_type = dpi_config_type
        # The maximum number of entries to return on each page.
        # 
        # Valid values: **1** to **100**.
        # 
        # Default value: **10**.
        self.max_results = max_results
        # The token that is used to query the next page.
        self.next_token = next_token
        # The region ID of the SAG instance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/69813.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the instance for which the DPI feature is configured.
        self.rule_instance_id = rule_instance_id
        # The ID of the SAG instance.
        self.smart_agid = smart_agid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dpi_config_type is not None:
            result['DpiConfigType'] = self.dpi_config_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rule_instance_id is not None:
            result['RuleInstanceId'] = self.rule_instance_id

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DpiConfigType') is not None:
            self.dpi_config_type = m.get('DpiConfigType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RuleInstanceId') is not None:
            self.rule_instance_id = m.get('RuleInstanceId')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        return self

