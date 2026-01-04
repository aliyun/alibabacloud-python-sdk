# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeGrantRulesToCenResponseBody(DaraModel):
    def __init__(
        self,
        cen_grant_rules: main_models.DescribeGrantRulesToCenResponseBodyCenGrantRules = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the authorization.
        self.cen_grant_rules = cen_grant_rules
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.cen_grant_rules:
            self.cen_grant_rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_grant_rules is not None:
            result['CenGrantRules'] = self.cen_grant_rules.to_map()

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
        if m.get('CenGrantRules') is not None:
            temp_model = main_models.DescribeGrantRulesToCenResponseBodyCenGrantRules()
            self.cen_grant_rules = temp_model.from_map(m.get('CenGrantRules'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeGrantRulesToCenResponseBodyCenGrantRules(DaraModel):
    def __init__(
        self,
        cbn_grant_rule: List[main_models.DescribeGrantRulesToCenResponseBodyCenGrantRulesCbnGrantRule] = None,
    ):
        self.cbn_grant_rule = cbn_grant_rule

    def validate(self):
        if self.cbn_grant_rule:
            for v1 in self.cbn_grant_rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CbnGrantRule'] = []
        if self.cbn_grant_rule is not None:
            for k1 in self.cbn_grant_rule:
                result['CbnGrantRule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cbn_grant_rule = []
        if m.get('CbnGrantRule') is not None:
            for k1 in m.get('CbnGrantRule'):
                temp_model = main_models.DescribeGrantRulesToCenResponseBodyCenGrantRulesCbnGrantRule()
                self.cbn_grant_rule.append(temp_model.from_map(k1))

        return self

class DescribeGrantRulesToCenResponseBodyCenGrantRulesCbnGrantRule(DaraModel):
    def __init__(
        self,
        cen_instance_id: str = None,
        cen_owner_id: int = None,
        creation_time: str = None,
    ):
        # The ID of the authorized CEN instance.
        self.cen_instance_id = cen_instance_id
        # The UID of the Alibaba Cloud account to which the authorized CEN instance belongs.
        self.cen_owner_id = cen_owner_id
        # The time when the instance was created.
        self.creation_time = creation_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_instance_id is not None:
            result['CenInstanceId'] = self.cen_instance_id

        if self.cen_owner_id is not None:
            result['CenOwnerId'] = self.cen_owner_id

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenInstanceId') is not None:
            self.cen_instance_id = m.get('CenInstanceId')

        if m.get('CenOwnerId') is not None:
            self.cen_owner_id = m.get('CenOwnerId')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        return self

