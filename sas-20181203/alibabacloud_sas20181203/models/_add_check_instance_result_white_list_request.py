# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class AddCheckInstanceResultWhiteListRequest(DaraModel):
    def __init__(
        self,
        check_group_id: str = None,
        check_id: int = None,
        client_token: str = None,
        instance_ids: List[str] = None,
        instance_list: List[main_models.AddCheckInstanceResultWhiteListRequestInstanceList] = None,
        remark: str = None,
        rule_type: str = None,
    ):
        # The ID of the check group to which the check item belongs.
        self.check_group_id = check_group_id
        # The ID of the check item.
        # > Call the [ListCheckResult](~~ListCheckResult~~) operation to obtain this parameter.
        self.check_id = check_id
        # The client token that is used to ensure the idempotence of the request. Different requests should use different tokens. The token supports only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The collection of asset instance IDs.
        self.instance_ids = instance_ids
        # The collection of asset instance information.
        self.instance_list = instance_list
        # The remarks. Maximum length: 65535 bytes.
        self.remark = remark
        # The rule type. Default value: **WHITE**. Valid values:
        # - WHITE: whitelist
        self.rule_type = rule_type

    def validate(self):
        if self.instance_list:
            for v1 in self.instance_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_group_id is not None:
            result['CheckGroupId'] = self.check_group_id

        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        result['InstanceList'] = []
        if self.instance_list is not None:
            for k1 in self.instance_list:
                result['InstanceList'].append(k1.to_map() if k1 else None)

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckGroupId') is not None:
            self.check_group_id = m.get('CheckGroupId')

        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k1 in m.get('InstanceList'):
                temp_model = main_models.AddCheckInstanceResultWhiteListRequestInstanceList()
                self.instance_list.append(temp_model.from_map(k1))

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        return self

class AddCheckInstanceResultWhiteListRequestInstanceList(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        # The asset instance ID.
        # > Call the [ListCheckInstanceResult](~~ListCheckInstanceResult~~) operation to obtain this parameter.
        self.instance_id = instance_id
        # The region where the asset resides.
        # > Call the [ListCheckInstanceResult](~~ListCheckInstanceResult~~) operation to obtain this parameter.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

