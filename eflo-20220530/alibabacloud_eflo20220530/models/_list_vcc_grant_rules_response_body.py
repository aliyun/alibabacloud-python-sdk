# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo20220530 import models as main_models
from darabonba.model import DaraModel

class ListVccGrantRulesResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: int = None,
        content: main_models.ListVccGrantRulesResponseBodyContent = None,
        message: str = None,
        request_id: str = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The response status code.
        self.code = code
        # The response parameters.
        self.content = content
        # The returned message.
        self.message = message
        # Request ID of the current request
        self.request_id = request_id

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Content') is not None:
            temp_model = main_models.ListVccGrantRulesResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListVccGrantRulesResponseBodyContent(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListVccGrantRulesResponseBodyContentData] = None,
        total: int = None,
    ):
        # List of cross-account authorization information of Lingjun connection
        self.data = data
        # The total number of entries returned.
        self.total = total

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListVccGrantRulesResponseBodyContentData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListVccGrantRulesResponseBodyContentData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        er_id: str = None,
        grant_rule_id: str = None,
        grant_tenant_id: str = None,
        instance_id: str = None,
        instance_name: str = None,
        product: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tenant_id: str = None,
        used: bool = None,
    ):
        # The time when the data address was created.
        self.create_time = create_time
        # Lingjun HUB ID
        self.er_id = er_id
        # Cross-account authorization information Instance ID
        self.grant_rule_id = grant_rule_id
        # Authorized Tenant ID
        self.grant_tenant_id = grant_tenant_id
        # Network Instance ID
        self.instance_id = instance_id
        # The name of the ECU.
        self.instance_name = instance_name
        # The type of the authorized product. Valid values:
        # 
        # *   **VPD**: indicates a VPD instance of the Lingjun network segment.
        # *   **VCC**: indicates that Lingjun connects to the VCC instance.
        self.product = product
        # The region ID.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # The ID of the tenant.
        self.tenant_id = tenant_id
        # Whether the current cross-account resource has been bound to the cross-account Lingjun HUB. Valid values:
        # 
        # *   **true**: Used
        # *   **false**: Not used
        self.used = used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.er_id is not None:
            result['ErId'] = self.er_id

        if self.grant_rule_id is not None:
            result['GrantRuleId'] = self.grant_rule_id

        if self.grant_tenant_id is not None:
            result['GrantTenantId'] = self.grant_tenant_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.product is not None:
            result['Product'] = self.product

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.used is not None:
            result['Used'] = self.used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')

        if m.get('GrantRuleId') is not None:
            self.grant_rule_id = m.get('GrantRuleId')

        if m.get('GrantTenantId') is not None:
            self.grant_tenant_id = m.get('GrantTenantId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('Used') is not None:
            self.used = m.get('Used')

        return self

