# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class DsgWhiteListAddOrUpdateRequest(DaraModel):
    def __init__(
        self,
        white_lists: List[main_models.DsgWhiteListAddOrUpdateRequestWhiteLists] = None,
    ):
        # A collection of whitelists.
        # 
        # This parameter is required.
        self.white_lists = white_lists

    def validate(self):
        if self.white_lists:
            for v1 in self.white_lists:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['WhiteLists'] = []
        if self.white_lists is not None:
            for k1 in self.white_lists:
                result['WhiteLists'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.white_lists = []
        if m.get('WhiteLists') is not None:
            for k1 in m.get('WhiteLists'):
                temp_model = main_models.DsgWhiteListAddOrUpdateRequestWhiteLists()
                self.white_lists.append(temp_model.from_map(k1))

        return self

class DsgWhiteListAddOrUpdateRequestWhiteLists(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        id: int = None,
        rule_id: int = None,
        start_time: str = None,
        user_group_ids: List[int] = None,
    ):
        # The end of the time range to query. If you enter null, the whitelist is valid permanently.
        self.end_time = end_time
        # The ID of the data masking whitelist.
        # 
        # *   If you do not configure this parameter, the current operation is to add a data masking whitelist.
        # *   If you configure this parameter, the current operation is to modify a data masking whitelist. You can call the [DsgWhiteListQueryList](https://help.aliyun.com/document_detail/2786508.html) operation to query the whitelist ID.
        self.id = id
        # The ID of the data masking rule. You can call the [DsgDesensPlanQueryList](https://help.aliyun.com/document_detail/2786578.html) operation to query the ID of the data masking rule.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The beginning of the time range to query.
        # 
        # This parameter is required.
        self.start_time = start_time
        # A collection of user group IDs.
        # 
        # This parameter is required.
        self.user_group_ids = user_group_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.id is not None:
            result['Id'] = self.id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        return self

