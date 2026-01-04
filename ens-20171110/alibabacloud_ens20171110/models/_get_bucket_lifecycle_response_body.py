# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class GetBucketLifecycleResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        rule: List[main_models.GetBucketLifecycleResponseBodyRule] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The detailed information about the rule.
        self.rule = rule

    def validate(self):
        if self.rule:
            for v1 in self.rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Rule'] = []
        if self.rule is not None:
            for k1 in self.rule:
                result['Rule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rule = []
        if m.get('Rule') is not None:
            for k1 in m.get('Rule'):
                temp_model = main_models.GetBucketLifecycleResponseBodyRule()
                self.rule.append(temp_model.from_map(k1))

        return self

class GetBucketLifecycleResponseBodyRule(DaraModel):
    def __init__(
        self,
        expiration: main_models.GetBucketLifecycleResponseBodyRuleExpiration = None,
        id: str = None,
        prefix: str = None,
        status: str = None,
    ):
        # The expiration time.
        self.expiration = expiration
        # The unique ID of the rule.
        self.id = id
        # The prefix that is applied to the rule.
        self.prefix = prefix
        # The status of the rule. Valid values:
        # 
        # *   **Enabled**: The rule is periodically executed.
        # *   **Disabled**: The rule is ignored.
        self.status = status

    def validate(self):
        if self.expiration:
            self.expiration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expiration is not None:
            result['Expiration'] = self.expiration.to_map()

        if self.id is not None:
            result['ID'] = self.id

        if self.prefix is not None:
            result['Prefix'] = self.prefix

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expiration') is not None:
            temp_model = main_models.GetBucketLifecycleResponseBodyRuleExpiration()
            self.expiration = temp_model.from_map(m.get('Expiration'))

        if m.get('ID') is not None:
            self.id = m.get('ID')

        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetBucketLifecycleResponseBodyRuleExpiration(DaraModel):
    def __init__(
        self,
        created_before_date: str = None,
        days: str = None,
    ):
        # The expiration date.
        self.created_before_date = created_before_date
        # The validity period, in days.
        self.days = days

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_before_date is not None:
            result['CreatedBeforeDate'] = self.created_before_date

        if self.days is not None:
            result['Days'] = self.days

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedBeforeDate') is not None:
            self.created_before_date = m.get('CreatedBeforeDate')

        if m.get('Days') is not None:
            self.days = m.get('Days')

        return self

