# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListFileProtectClientRuleResponseBody(DaraModel):
    def __init__(
        self,
        file_protect_list: List[main_models.ListFileProtectClientRuleResponseBodyFileProtectList] = None,
        page_info: main_models.ListFileProtectClientRuleResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.file_protect_list = file_protect_list
        self.page_info = page_info
        self.request_id = request_id

    def validate(self):
        if self.file_protect_list:
            for v1 in self.file_protect_list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FileProtectList'] = []
        if self.file_protect_list is not None:
            for k1 in self.file_protect_list:
                result['FileProtectList'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.file_protect_list = []
        if m.get('FileProtectList') is not None:
            for k1 in m.get('FileProtectList'):
                temp_model = main_models.ListFileProtectClientRuleResponseBodyFileProtectList()
                self.file_protect_list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListFileProtectClientRuleResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListFileProtectClientRuleResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListFileProtectClientRuleResponseBodyFileProtectList(DaraModel):
    def __init__(
        self,
        alert_level: int = None,
        effect_instance_count: int = None,
        exclude_users: List[str] = None,
        file_ops: List[str] = None,
        file_paths: List[str] = None,
        file_types: List[str] = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        platform: str = None,
        proc_paths: List[str] = None,
        rule_action: str = None,
        rule_name: str = None,
        status: int = None,
        switch_id: str = None,
    ):
        self.alert_level = alert_level
        self.effect_instance_count = effect_instance_count
        self.exclude_users = exclude_users
        self.file_ops = file_ops
        self.file_paths = file_paths
        self.file_types = file_types
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.platform = platform
        self.proc_paths = proc_paths
        self.rule_action = rule_action
        self.rule_name = rule_name
        self.status = status
        self.switch_id = switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_level is not None:
            result['AlertLevel'] = self.alert_level

        if self.effect_instance_count is not None:
            result['EffectInstanceCount'] = self.effect_instance_count

        if self.exclude_users is not None:
            result['ExcludeUsers'] = self.exclude_users

        if self.file_ops is not None:
            result['FileOps'] = self.file_ops

        if self.file_paths is not None:
            result['FilePaths'] = self.file_paths

        if self.file_types is not None:
            result['FileTypes'] = self.file_types

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.proc_paths is not None:
            result['ProcPaths'] = self.proc_paths

        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.status is not None:
            result['Status'] = self.status

        if self.switch_id is not None:
            result['SwitchId'] = self.switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertLevel') is not None:
            self.alert_level = m.get('AlertLevel')

        if m.get('EffectInstanceCount') is not None:
            self.effect_instance_count = m.get('EffectInstanceCount')

        if m.get('ExcludeUsers') is not None:
            self.exclude_users = m.get('ExcludeUsers')

        if m.get('FileOps') is not None:
            self.file_ops = m.get('FileOps')

        if m.get('FilePaths') is not None:
            self.file_paths = m.get('FilePaths')

        if m.get('FileTypes') is not None:
            self.file_types = m.get('FileTypes')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('ProcPaths') is not None:
            self.proc_paths = m.get('ProcPaths')

        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SwitchId') is not None:
            self.switch_id = m.get('SwitchId')

        return self

