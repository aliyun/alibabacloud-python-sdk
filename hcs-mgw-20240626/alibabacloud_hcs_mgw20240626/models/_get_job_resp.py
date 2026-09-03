# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hcs_mgw20240626 import models as main_models
from darabonba.model import DaraModel

class GetJobResp(DaraModel):
    def __init__(
        self,
        appendable_to_normal: bool = None,
        audit: main_models.Audit = None,
        convert_symlink_target: bool = None,
        create_report: bool = None,
        create_time: str = None,
        dest_address: str = None,
        enable_multi_versioning: bool = None,
        filter_rule: main_models.FilterRule = None,
        import_qos: main_models.ImportQos = None,
        modify_time: str = None,
        name: str = None,
        overwrite_mode: str = None,
        owner: str = None,
        parent_name: str = None,
        parent_version: str = None,
        schedule_rule: main_models.ScheduleRule = None,
        src_address: str = None,
        status: str = None,
        tags: str = None,
        target_storage_class: str = None,
        transfer_mode: str = None,
        version: str = None,
        with_last_modify_time: bool = None,
        with_storage_class: bool = None,
    ):
        # Specifies whether to migrate appendable files as normal or multipart files. The default value is false.
        self.appendable_to_normal = appendable_to_normal
        # The audit method.
        self.audit = audit
        # Indicates whether to convert the target of the symbolic link.
        self.convert_symlink_target = convert_symlink_target
        # Indicates whether to generate a migration report.
        self.create_report = create_report
        # The time when the job was created.
        self.create_time = create_time
        # The name of the destination data address.
        self.dest_address = dest_address
        # Indicates whether multi-versioning is enabled.
        self.enable_multi_versioning = enable_multi_versioning
        # The filter rule.
        self.filter_rule = filter_rule
        # The rate limiting rule for the job.
        self.import_qos = import_qos
        # The time when the job was last modified.
        self.modify_time = modify_time
        # The name of the job.
        self.name = name
        # The file overwrite mode.
        self.overwrite_mode = overwrite_mode
        # The owner.
        self.owner = owner
        # The name of the parent job.
        self.parent_name = parent_name
        # The ID of the parent job.
        self.parent_version = parent_version
        # The scheduling rule.
        self.schedule_rule = schedule_rule
        # The name of the source data address.
        self.src_address = src_address
        # The status of the job.
        # 
        # IMPORT_JOB_BEGIN: The job is created.
        # 
        # IMPORT_JOB_LAUNCHING: The job is starting.
        # 
        # IMPORT_JOB_PREPARING: The job is preparing.
        # 
        # IMPORT_JOB_DOING: The job is running.
        # 
        # IMPORT_JOB_SUSPEND: The job is paused.
        # 
        # IMPORT_JOB_CLOSING: The job is shutting down.
        # 
        # IMPORT_JOB_FINISHED: The job is finished.
        # 
        # IMPORT_JOB_INTERRUPTED: The job is abnormally interrupted.
        # 
        # IMPORT_JOB_CONFIRMED: The migration is complete, and the user has confirmed data integrity and consistency.
        # 
        # IMPORT_JOB_DELETING: The job is being deleted.
        self.status = status
        # The tags.
        self.tags = tags
        # Specifies the StorageClass of the destination file. The destination address must be an OSS address. Valid values: Standard, IA, Archive, ColdArchive, and DeepColdArchive.
        self.target_storage_class = target_storage_class
        # The file transfer mode.
        self.transfer_mode = transfer_mode
        # The ID of the job.
        self.version = version
        # Specifies whether to retain the lastModifyTime property. The default value is true.
        self.with_last_modify_time = with_last_modify_time
        # Specifies whether to migrate the StorageClass property. This is allowed only for migrations from OSS to OSS.
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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dest_address is not None:
            result['DestAddress'] = self.dest_address

        if self.enable_multi_versioning is not None:
            result['EnableMultiVersioning'] = self.enable_multi_versioning

        if self.filter_rule is not None:
            result['FilterRule'] = self.filter_rule.to_map()

        if self.import_qos is not None:
            result['ImportQos'] = self.import_qos.to_map()

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.overwrite_mode is not None:
            result['OverwriteMode'] = self.overwrite_mode

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.parent_name is not None:
            result['ParentName'] = self.parent_name

        if self.parent_version is not None:
            result['ParentVersion'] = self.parent_version

        if self.schedule_rule is not None:
            result['ScheduleRule'] = self.schedule_rule.to_map()

        if self.src_address is not None:
            result['SrcAddress'] = self.src_address

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.target_storage_class is not None:
            result['TargetStorageClass'] = self.target_storage_class

        if self.transfer_mode is not None:
            result['TransferMode'] = self.transfer_mode

        if self.version is not None:
            result['Version'] = self.version

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

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

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

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OverwriteMode') is not None:
            self.overwrite_mode = m.get('OverwriteMode')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ParentName') is not None:
            self.parent_name = m.get('ParentName')

        if m.get('ParentVersion') is not None:
            self.parent_version = m.get('ParentVersion')

        if m.get('ScheduleRule') is not None:
            temp_model = main_models.ScheduleRule()
            self.schedule_rule = temp_model.from_map(m.get('ScheduleRule'))

        if m.get('SrcAddress') is not None:
            self.src_address = m.get('SrcAddress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TargetStorageClass') is not None:
            self.target_storage_class = m.get('TargetStorageClass')

        if m.get('TransferMode') is not None:
            self.transfer_mode = m.get('TransferMode')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('WithLastModifyTime') is not None:
            self.with_last_modify_time = m.get('WithLastModifyTime')

        if m.get('WithStorageClass') is not None:
            self.with_storage_class = m.get('WithStorageClass')

        return self

