# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListEscalationPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        page_bean: main_models.ListEscalationPoliciesResponseBodyPageBean = None,
        request_id: str = None,
    ):
        # The returned objects.
        self.page_bean = page_bean
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.page_bean:
            self.page_bean.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_bean is not None:
            result['PageBean'] = self.page_bean.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageBean') is not None:
            temp_model = main_models.ListEscalationPoliciesResponseBodyPageBean()
            self.page_bean = temp_model.from_map(m.get('PageBean'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListEscalationPoliciesResponseBodyPageBean(DaraModel):
    def __init__(
        self,
        escalation_policies: List[main_models.ListEscalationPoliciesResponseBodyPageBeanEscalationPolicies] = None,
        page: int = None,
        size: int = None,
        total: int = None,
    ):
        # The list of escalation policies.
        self.escalation_policies = escalation_policies
        # The page number of the returned page.
        self.page = page
        # The number of entries returned per page.
        self.size = size
        # The total number of returned entries.
        self.total = total

    def validate(self):
        if self.escalation_policies:
            for v1 in self.escalation_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EscalationPolicies'] = []
        if self.escalation_policies is not None:
            for k1 in self.escalation_policies:
                result['EscalationPolicies'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['Page'] = self.page

        if self.size is not None:
            result['Size'] = self.size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.escalation_policies = []
        if m.get('EscalationPolicies') is not None:
            for k1 in m.get('EscalationPolicies'):
                temp_model = main_models.ListEscalationPoliciesResponseBodyPageBeanEscalationPolicies()
                self.escalation_policies.append(temp_model.from_map(k1))

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListEscalationPoliciesResponseBodyPageBeanEscalationPolicies(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        # The ID of the escalation policy.
        self.id = id
        # The name of the escalation policy.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

