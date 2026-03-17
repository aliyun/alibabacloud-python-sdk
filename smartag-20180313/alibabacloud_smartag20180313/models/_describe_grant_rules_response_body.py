# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeGrantRulesResponseBody(DaraModel):
    def __init__(
        self,
        grant_rules: main_models.DescribeGrantRulesResponseBodyGrantRules = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.grant_rules = grant_rules
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned on each page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.grant_rules:
            self.grant_rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.grant_rules is not None:
            result['GrantRules'] = self.grant_rules.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GrantRules') is not None:
            temp_model = main_models.DescribeGrantRulesResponseBodyGrantRules()
            self.grant_rules = temp_model.from_map(m.get('GrantRules'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeGrantRulesResponseBodyGrantRules(DaraModel):
    def __init__(
        self,
        grant_rule: List[main_models.DescribeGrantRulesResponseBodyGrantRulesGrantRule] = None,
    ):
        self.grant_rule = grant_rule

    def validate(self):
        if self.grant_rule:
            for v1 in self.grant_rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GrantRule'] = []
        if self.grant_rule is not None:
            for k1 in self.grant_rule:
                result['GrantRule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.grant_rule = []
        if m.get('GrantRule') is not None:
            for k1 in m.get('GrantRule'):
                temp_model = main_models.DescribeGrantRulesResponseBodyGrantRulesGrantRule()
                self.grant_rule.append(temp_model.from_map(k1))

        return self

class DescribeGrantRulesResponseBodyGrantRulesGrantRule(DaraModel):
    def __init__(
        self,
        ccn_instance_id: str = None,
        ccn_uid: int = None,
        cen_instance_id: str = None,
        cen_uid: int = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        grant_rule_id: str = None,
        grant_traffic_service: bool = None,
        region_id: str = None,
    ):
        self.ccn_instance_id = ccn_instance_id
        self.ccn_uid = ccn_uid
        self.cen_instance_id = cen_instance_id
        self.cen_uid = cen_uid
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.grant_rule_id = grant_rule_id
        self.grant_traffic_service = grant_traffic_service
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ccn_instance_id is not None:
            result['CcnInstanceId'] = self.ccn_instance_id

        if self.ccn_uid is not None:
            result['CcnUid'] = self.ccn_uid

        if self.cen_instance_id is not None:
            result['CenInstanceId'] = self.cen_instance_id

        if self.cen_uid is not None:
            result['CenUid'] = self.cen_uid

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.grant_rule_id is not None:
            result['GrantRuleId'] = self.grant_rule_id

        if self.grant_traffic_service is not None:
            result['GrantTrafficService'] = self.grant_traffic_service

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CcnInstanceId') is not None:
            self.ccn_instance_id = m.get('CcnInstanceId')

        if m.get('CcnUid') is not None:
            self.ccn_uid = m.get('CcnUid')

        if m.get('CenInstanceId') is not None:
            self.cen_instance_id = m.get('CenInstanceId')

        if m.get('CenUid') is not None:
            self.cen_uid = m.get('CenUid')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GrantRuleId') is not None:
            self.grant_rule_id = m.get('GrantRuleId')

        if m.get('GrantTrafficService') is not None:
            self.grant_traffic_service = m.get('GrantTrafficService')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

