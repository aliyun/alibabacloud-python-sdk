# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddCheckResultWhiteListRequest(DaraModel):
    def __init__(
        self,
        check_ids: List[int] = None,
        client_token: str = None,
        instance_ids: List[str] = None,
        remark: str = None,
        rule_type: str = None,
    ):
        # The IDs of the check items.
        # > Call the [ListCheckResult](~~ListCheckResult~~) operation to obtain this parameter.
        self.check_ids = check_ids
        # The client token that is used to ensure the idempotence of the request. Different requests should use different tokens. The token supports only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The instance IDs of the cloud service instances to add to the whitelist. Separate multiple instance IDs with commas (,).
        self.instance_ids = instance_ids
        # The remarks. Maximum length: 65,535 bytes.
        self.remark = remark
        # The rule type. Default value: **WHITE**. Valid values:
        # - **WHITE**: adds to the whitelist.
        self.rule_type = rule_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_ids is not None:
            result['CheckIds'] = self.check_ids

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckIds') is not None:
            self.check_ids = m.get('CheckIds')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        return self

