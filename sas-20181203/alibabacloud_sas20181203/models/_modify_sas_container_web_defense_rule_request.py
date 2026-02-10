# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ModifySasContainerWebDefenseRuleRequest(DaraModel):
    def __init__(
        self,
        path_conf_dtolist: List[main_models.ModifySasContainerWebDefenseRuleRequestPathConfDTOList] = None,
        rule_id: int = None,
        rule_name: str = None,
    ):
        # The paths that are protected.
        self.path_conf_dtolist = path_conf_dtolist
        # The ID of the rule.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The name of the rule.
        self.rule_name = rule_name

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
        result['PathConfDTOList'] = []
        if self.path_conf_dtolist is not None:
            for k1 in self.path_conf_dtolist:
                result['PathConfDTOList'].append(k1.to_map() if k1 else None)

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.path_conf_dtolist = []
        if m.get('PathConfDTOList') is not None:
            for k1 in m.get('PathConfDTOList'):
                temp_model = main_models.ModifySasContainerWebDefenseRuleRequestPathConfDTOList()
                self.path_conf_dtolist.append(temp_model.from_map(k1))

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

class ModifySasContainerWebDefenseRuleRequestPathConfDTOList(DaraModel):
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
        path_conf_id: int = None,
        process_path_list: List[str] = None,
    ):
        # The backup paths.
        self.backup_path = backup_path
        # The prevention mode. Valid values:
        # 
        # *   **block**
        # *   **audit**
        # 
        # This parameter is required.
        self.defense_mode = defense_mode
        # The path that is protected.
        # 
        # This parameter is required.
        self.defense_path = defense_path
        # The files that are excluded.
        self.exclude_file = exclude_file
        # The paths to the files that are excluded.
        self.exclude_file_path = exclude_file_path
        # The types of the files that are excluded.
        self.exclude_file_type = exclude_file_type
        # The protection mode. Valid values:
        # 
        # *   **0**: basic mode (whitelist)
        # *   **1**: complex mode (blacklist)
        # 
        # This parameter is required.
        self.guard_type = guard_type
        # The files that are included.
        self.include_file = include_file
        # The type of the files that are included.
        self.include_file_type = include_file_type
        # The path ID.
        self.path_conf_id = path_conf_id
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

        if self.path_conf_id is not None:
            result['PathConfId'] = self.path_conf_id

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

        if m.get('PathConfId') is not None:
            self.path_conf_id = m.get('PathConfId')

        if m.get('ProcessPathList') is not None:
            self.process_path_list = m.get('ProcessPathList')

        return self

