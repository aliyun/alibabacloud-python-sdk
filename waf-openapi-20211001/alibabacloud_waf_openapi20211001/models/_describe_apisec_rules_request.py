# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApisecRulesRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        lang: str = None,
        level: str = None,
        name: str = None,
        origin: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        status: int = None,
        type: str = None,
    ):
        # The ID of the WAF instance.
        # 
        # > You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the current WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The language of the returned rules. Valid values:
        # 
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The level of the rule.
        # 
        # For risk detection (risk) and security events (event), valid values:
        # - **high**: High risk.
        # - **medium**: Medium risk.
        # - **low**: Low risk.
        # 
        # For sensitive data (sensitive_word), valid values:
        # - **S1**: S1 level.
        # - **S2**: S2 level.
        # - **S3**: S3 level.
        # - **S4**: S4 level.
        self.level = level
        # The name of the rule.
        self.name = name
        # The source of the rule. Valid values:
        # - **custom**: Custom.
        # - **default**: Built-in.
        self.origin = origin
        # The page number to return in a paged query. Default value: **1**, which indicates the first page of paging.
        self.page_number = page_number
        # The number of entries to return on each page in a paged query. Default value: **10**, which indicates 10 entries per paging.
        self.page_size = page_size
        # The region where the WAF instance resides. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The enabling status of the rule. Valid values:
        # 
        # - **1**: Enabled.
        # 
        # - **0**: shutdown.
        self.status = status
        # The rule type. Valid values:
        # - **risk**: Risk detection.
        # - **event**: Security events.
        # - **sensitive_word**: Sensitive data.
        # - **auth_flag**: Authentication credentials.
        # - **api_tag**: Business purpose.
        # - **desensitization**: Data masking.
        # - **whitelist**: Whitelist.
        # - **recognition**: API identification.
        # - **offline_api**: Lifecycle management.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.level is not None:
            result['Level'] = self.level

        if self.name is not None:
            result['Name'] = self.name

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

