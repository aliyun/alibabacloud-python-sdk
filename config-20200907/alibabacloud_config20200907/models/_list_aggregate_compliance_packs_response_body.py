# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class ListAggregateCompliancePacksResponseBody(DaraModel):
    def __init__(
        self,
        compliance_packs_result: main_models.ListAggregateCompliancePacksResponseBodyCompliancePacksResult = None,
        request_id: str = None,
    ):
        # The compliance packages returned.
        self.compliance_packs_result = compliance_packs_result
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.compliance_packs_result:
            self.compliance_packs_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_packs_result is not None:
            result['CompliancePacksResult'] = self.compliance_packs_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePacksResult') is not None:
            temp_model = main_models.ListAggregateCompliancePacksResponseBodyCompliancePacksResult()
            self.compliance_packs_result = temp_model.from_map(m.get('CompliancePacksResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAggregateCompliancePacksResponseBodyCompliancePacksResult(DaraModel):
    def __init__(
        self,
        compliance_packs: List[main_models.ListAggregateCompliancePacksResponseBodyCompliancePacksResultCompliancePacks] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The compliance packages.
        self.compliance_packs = compliance_packs
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of compliance packages returned.
        self.total_count = total_count

    def validate(self):
        if self.compliance_packs:
            for v1 in self.compliance_packs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CompliancePacks'] = []
        if self.compliance_packs is not None:
            for k1 in self.compliance_packs:
                result['CompliancePacks'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.compliance_packs = []
        if m.get('CompliancePacks') is not None:
            for k1 in m.get('CompliancePacks'):
                temp_model = main_models.ListAggregateCompliancePacksResponseBodyCompliancePacksResultCompliancePacks()
                self.compliance_packs.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAggregateCompliancePacksResponseBodyCompliancePacksResultCompliancePacks(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        aggregator_id: str = None,
        compliance_pack_id: str = None,
        compliance_pack_name: str = None,
        compliance_pack_template_id: str = None,
        create_timestamp: int = None,
        description: str = None,
        risk_level: int = None,
        status: str = None,
        tags: List[main_models.ListAggregateCompliancePacksResponseBodyCompliancePacksResultCompliancePacksTags] = None,
    ):
        # The ID of the management account to which the compliance package belongs.
        self.account_id = account_id
        # The ID of the account group.
        self.aggregator_id = aggregator_id
        # The ID of the compliance package.
        self.compliance_pack_id = compliance_pack_id
        # The name of the compliance package.
        self.compliance_pack_name = compliance_pack_name
        # The ID of the compliance package template.
        self.compliance_pack_template_id = compliance_pack_template_id
        # The timestamp when the compliance package was created. Unit: milliseconds.
        self.create_timestamp = create_timestamp
        # The description of the compliance package.
        self.description = description
        # The risk level of the resources that are not compliant with the managed rules in the compliance package. Valid values:
        # 
        # *   1: high risk level.
        # *   2: medium risk level.
        # *   3: low risk level.
        self.risk_level = risk_level
        # The status of the compliance package. Valid values:
        # 
        # *   ACTIVE: The compliance package is available for use.
        # *   CREATING: The compliance package is being created.
        self.status = status
        # The tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id

        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name

        if self.compliance_pack_template_id is not None:
            result['CompliancePackTemplateId'] = self.compliance_pack_template_id

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.description is not None:
            result['Description'] = self.description

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')

        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')

        if m.get('CompliancePackTemplateId') is not None:
            self.compliance_pack_template_id = m.get('CompliancePackTemplateId')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListAggregateCompliancePacksResponseBodyCompliancePacksResultCompliancePacksTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListAggregateCompliancePacksResponseBodyCompliancePacksResultCompliancePacksTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

