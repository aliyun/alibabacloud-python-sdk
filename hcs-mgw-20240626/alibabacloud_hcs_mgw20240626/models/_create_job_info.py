# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hcs_mgw20240626 import models as main_models
from darabonba.model import DaraModel

class CreateJobInfo(DaraModel):
    def __init__(
        self,
        appendable_to_normal: bool = None,
        audit: main_models.Audit = None,
        convert_symlink_target: bool = None,
        create_report: bool = None,
        dest_address: str = None,
        enable_multi_versioning: bool = None,
        filter_rule: main_models.FilterRule = None,
        import_qos: main_models.ImportQos = None,
        name: str = None,
        overwrite_mode: str = None,
        parent_version: str = None,
        schedule_rule: main_models.ScheduleRule = None,
        src_address: str = None,
        tags: str = None,
        target_storage_class: str = None,
        transfer_mode: str = None,
        with_last_modify_time: bool = None,
        with_storage_class: bool = None,
    ):
        self.appendable_to_normal = appendable_to_normal
        self.audit = audit
        self.convert_symlink_target = convert_symlink_target
        self.create_report = create_report
        # This parameter is required.
        self.dest_address = dest_address
        self.enable_multi_versioning = enable_multi_versioning
        self.filter_rule = filter_rule
        self.import_qos = import_qos
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.overwrite_mode = overwrite_mode
        self.parent_version = parent_version
        self.schedule_rule = schedule_rule
        # This parameter is required.
        self.src_address = src_address
        self.tags = tags
        self.target_storage_class = target_storage_class
        # This parameter is required.
        self.transfer_mode = transfer_mode
        self.with_last_modify_time = with_last_modify_time
        self.with_storage_class = with_storage_class

    def validate(self):
        if self.audit:
            self.audit.validate()
        if self.filter_rule:
            self.filter_rule.validate()
        if self.import_qos:
            self.import_qos.validate()
        if self.schedule_rule:
            self.schedule_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.appendable_to_normal is not None:
            result['AppendableToNormal'] = self.appendable_to_normal

        if self.audit is not None:
            result['Audit'] = self.audit.to_map()

        if self.convert_symlink_target is not None:
            result['ConvertSymlinkTarget'] = self.convert_symlink_target

        if self.create_report is not None:
            result['CreateReport'] = self.create_report

        if self.dest_address is not None:
            result['DestAddress'] = self.dest_address

        if self.enable_multi_versioning is not None:
            result['EnableMultiVersioning'] = self.enable_multi_versioning

        if self.filter_rule is not None:
            result['FilterRule'] = self.filter_rule.to_map()

        if self.import_qos is not None:
            result['ImportQos'] = self.import_qos.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.overwrite_mode is not None:
            result['OverwriteMode'] = self.overwrite_mode

        if self.parent_version is not None:
            result['ParentVersion'] = self.parent_version

        if self.schedule_rule is not None:
            result['ScheduleRule'] = self.schedule_rule.to_map()

        if self.src_address is not None:
            result['SrcAddress'] = self.src_address

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.target_storage_class is not None:
            result['TargetStorageClass'] = self.target_storage_class

        if self.transfer_mode is not None:
            result['TransferMode'] = self.transfer_mode

        if self.with_last_modify_time is not None:
            result['WithLastModifyTime'] = self.with_last_modify_time

        if self.with_storage_class is not None:
            result['WithStorageClass'] = self.with_storage_class

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppendableToNormal') is not None:
            self.appendable_to_normal = m.get('AppendableToNormal')

        if m.get('Audit') is not None:
            temp_model = main_models.Audit()
            self.audit = temp_model.from_map(m.get('Audit'))

        if m.get('ConvertSymlinkTarget') is not None:
            self.convert_symlink_target = m.get('ConvertSymlinkTarget')

        if m.get('CreateReport') is not None:
            self.create_report = m.get('CreateReport')

        if m.get('DestAddress') is not None:
            self.dest_address = m.get('DestAddress')

        if m.get('EnableMultiVersioning') is not None:
            self.enable_multi_versioning = m.get('EnableMultiVersioning')

        if m.get('FilterRule') is not None:
            temp_model = main_models.FilterRule()
            self.filter_rule = temp_model.from_map(m.get('FilterRule'))

        if m.get('ImportQos') is not None:
            temp_model = main_models.ImportQos()
            self.import_qos = temp_model.from_map(m.get('ImportQos'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OverwriteMode') is not None:
            self.overwrite_mode = m.get('OverwriteMode')

        if m.get('ParentVersion') is not None:
            self.parent_version = m.get('ParentVersion')

        if m.get('ScheduleRule') is not None:
            temp_model = main_models.ScheduleRule()
            self.schedule_rule = temp_model.from_map(m.get('ScheduleRule'))

        if m.get('SrcAddress') is not None:
            self.src_address = m.get('SrcAddress')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TargetStorageClass') is not None:
            self.target_storage_class = m.get('TargetStorageClass')

        if m.get('TransferMode') is not None:
            self.transfer_mode = m.get('TransferMode')

        if m.get('WithLastModifyTime') is not None:
            self.with_last_modify_time = m.get('WithLastModifyTime')

        if m.get('WithStorageClass') is not None:
            self.with_storage_class = m.get('WithStorageClass')

        return self

