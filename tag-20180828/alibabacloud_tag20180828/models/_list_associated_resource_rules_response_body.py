# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_tag20180828 import models as main_models
from darabonba.model import DaraModel

class ListAssociatedResourceRulesResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        rules: List[main_models.ListAssociatedResourceRulesResponseBodyRules] = None,
    ):
        # You can use the `NextToken` parameter to determine whether there is a token that can be used to start the next query. Valid values:
        # 
        # - If `NextToken` is empty, no next query is performed.
        # 
        # - If a value is returned for `NextToken`, the value is the token that is used for the next query.
        # 
        # This parameter is required.
        self.next_token = next_token
        # The Request ID.
        self.request_id = request_id
        # A list of associated resource rules.
        self.rules = rules

    def validate(self):
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.ListAssociatedResourceRulesResponseBodyRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class ListAssociatedResourceRulesResponseBodyRules(DaraModel):
    def __init__(
        self,
        existing_status: str = None,
        setting_name: str = None,
        status: str = None,
        tag_keys: List[str] = None,
    ):
        self.existing_status = existing_status
        # The name of the associated resource rule.
        self.setting_name = setting_name
        # The status of the associated resource rule. Valid values: `Enable` and `Disable`.
        self.status = status
        # The Tag Keys to which the rule applies.
        self.tag_keys = tag_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.existing_status is not None:
            result['ExistingStatus'] = self.existing_status

        if self.setting_name is not None:
            result['SettingName'] = self.setting_name

        if self.status is not None:
            result['Status'] = self.status

        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExistingStatus') is not None:
            self.existing_status = m.get('ExistingStatus')

        if m.get('SettingName') is not None:
            self.setting_name = m.get('SettingName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')

        return self

