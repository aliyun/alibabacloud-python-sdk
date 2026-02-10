# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListSasContainerWebDefenseRuleResponseBody(DaraModel):
    def __init__(
        self,
        container_web_defense_rule_list: List[main_models.ListSasContainerWebDefenseRuleResponseBodyContainerWebDefenseRuleList] = None,
        page_info: main_models.ListSasContainerWebDefenseRuleResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The rules for container tamper-proofing.
        self.container_web_defense_rule_list = container_web_defense_rule_list
        # The pagination information.
        self.page_info = page_info
        # The request ID, which is used to query logs and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.container_web_defense_rule_list:
            for v1 in self.container_web_defense_rule_list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ContainerWebDefenseRuleList'] = []
        if self.container_web_defense_rule_list is not None:
            for k1 in self.container_web_defense_rule_list:
                result['ContainerWebDefenseRuleList'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.container_web_defense_rule_list = []
        if m.get('ContainerWebDefenseRuleList') is not None:
            for k1 in m.get('ContainerWebDefenseRuleList'):
                temp_model = main_models.ListSasContainerWebDefenseRuleResponseBodyContainerWebDefenseRuleList()
                self.container_web_defense_rule_list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListSasContainerWebDefenseRuleResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListSasContainerWebDefenseRuleResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSasContainerWebDefenseRuleResponseBodyContainerWebDefenseRuleList(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        apptotal_count: int = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        path_conf_dtolist: List[main_models.ListSasContainerWebDefenseRuleResponseBodyContainerWebDefenseRuleListPathConfDTOList] = None,
        rule_name: str = None,
        rule_status: int = None,
    ):
        # The user ID.
        self.ali_uid = ali_uid
        # The number of the applications.
        self.apptotal_count = apptotal_count
        # The creation time. Unit: milliseconds.
        self.gmt_create = gmt_create
        # The timestamp when the alert event was last modified. Unit: milliseconds.
        self.gmt_modified = gmt_modified
        # The ID of the rule.
        self.id = id
        # The paths that are protected.
        self.path_conf_dtolist = path_conf_dtolist
        # The name of the rule.
        self.rule_name = rule_name
        # The status of the rule. Valid values:
        # 
        # *   **1**: enabled
        # *   **0**: disabled
        self.rule_status = rule_status

    def validate(self):
        if self.path_conf_dtolist:
            for v1 in self.path_conf_dtolist:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.apptotal_count is not None:
            result['ApptotalCount'] = self.apptotal_count

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        result['PathConfDTOList'] = []
        if self.path_conf_dtolist is not None:
            for k1 in self.path_conf_dtolist:
                result['PathConfDTOList'].append(k1.to_map() if k1 else None)

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_status is not None:
            result['RuleStatus'] = self.rule_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('ApptotalCount') is not None:
            self.apptotal_count = m.get('ApptotalCount')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        self.path_conf_dtolist = []
        if m.get('PathConfDTOList') is not None:
            for k1 in m.get('PathConfDTOList'):
                temp_model = main_models.ListSasContainerWebDefenseRuleResponseBodyContainerWebDefenseRuleListPathConfDTOList()
                self.path_conf_dtolist.append(temp_model.from_map(k1))

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleStatus') is not None:
            self.rule_status = m.get('RuleStatus')

        return self

class ListSasContainerWebDefenseRuleResponseBodyContainerWebDefenseRuleListPathConfDTOList(DaraModel):
    def __init__(
        self,
        backup_path: str = None,
        defense_mode: str = None,
        defense_path: str = None,
        exclude_file: str = None,
        exclude_file_path: str = None,
        exclude_file_type: str = None,
        guard_type: int = None,
        include_file: str = None,
        include_file_type: str = None,
        process_path_list: List[str] = None,
    ):
        # The backup paths.
        self.backup_path = backup_path
        # The prevention mode. Valid values:
        # 
        # *   **block**
        # *   **audit**
        self.defense_mode = defense_mode
        # The protected path.
        self.defense_path = defense_path
        # The file that is excluded.
        self.exclude_file = exclude_file
        # The path to the file that is excluded.
        self.exclude_file_path = exclude_file_path
        # The type of the file that is excluded.
        self.exclude_file_type = exclude_file_type
        # The protection mode. Valid values:
        # 
        # *   **0**: basic mode (whitelist)
        # *   **1**: complex mode (blacklist)
        self.guard_type = guard_type
        # The file that is included.
        self.include_file = include_file
        # The type of the file that is included.
        self.include_file_type = include_file_type
        # The processes that are added to the whitelist.
        self.process_path_list = process_path_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_path is not None:
            result['BackupPath'] = self.backup_path

        if self.defense_mode is not None:
            result['DefenseMode'] = self.defense_mode

        if self.defense_path is not None:
            result['DefensePath'] = self.defense_path

        if self.exclude_file is not None:
            result['ExcludeFile'] = self.exclude_file

        if self.exclude_file_path is not None:
            result['ExcludeFilePath'] = self.exclude_file_path

        if self.exclude_file_type is not None:
            result['ExcludeFileType'] = self.exclude_file_type

        if self.guard_type is not None:
            result['GuardType'] = self.guard_type

        if self.include_file is not None:
            result['IncludeFile'] = self.include_file

        if self.include_file_type is not None:
            result['IncludeFileType'] = self.include_file_type

        if self.process_path_list is not None:
            result['ProcessPathList'] = self.process_path_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupPath') is not None:
            self.backup_path = m.get('BackupPath')

        if m.get('DefenseMode') is not None:
            self.defense_mode = m.get('DefenseMode')

        if m.get('DefensePath') is not None:
            self.defense_path = m.get('DefensePath')

        if m.get('ExcludeFile') is not None:
            self.exclude_file = m.get('ExcludeFile')

        if m.get('ExcludeFilePath') is not None:
            self.exclude_file_path = m.get('ExcludeFilePath')

        if m.get('ExcludeFileType') is not None:
            self.exclude_file_type = m.get('ExcludeFileType')

        if m.get('GuardType') is not None:
            self.guard_type = m.get('GuardType')

        if m.get('IncludeFile') is not None:
            self.include_file = m.get('IncludeFile')

        if m.get('IncludeFileType') is not None:
            self.include_file_type = m.get('IncludeFileType')

        if m.get('ProcessPathList') is not None:
            self.process_path_list = m.get('ProcessPathList')

        return self

