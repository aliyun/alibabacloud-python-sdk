# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AddressDetail(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        access_secret: str = None,
        address_type: str = None,
        agent_list: str = None,
        bucket: str = None,
        domain: str = None,
        inv_access_id: str = None,
        inv_access_secret: str = None,
        inv_bucket: str = None,
        inv_domain: str = None,
        inv_location: str = None,
        inv_path: str = None,
        inv_region_id: str = None,
        inv_role: str = None,
        prefix: str = None,
        region_id: str = None,
        role: str = None,
    ):
        # This parameter is required.
        self.access_id = access_id
        # This parameter is required.
        self.access_secret = access_secret
        # This parameter is required.
        self.address_type = address_type
        self.agent_list = agent_list
        # This parameter is required.
        self.bucket = bucket
        # This parameter is required.
        self.domain = domain
        self.inv_access_id = inv_access_id
        self.inv_access_secret = inv_access_secret
        self.inv_bucket = inv_bucket
        self.inv_domain = inv_domain
        self.inv_location = inv_location
        self.inv_path = inv_path
        self.inv_region_id = inv_region_id
        self.inv_role = inv_role
        self.prefix = prefix
        self.region_id = region_id
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.access_secret is not None:
            result['AccessSecret'] = self.access_secret
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.agent_list is not None:
            result['AgentList'] = self.agent_list
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.inv_access_id is not None:
            result['InvAccessId'] = self.inv_access_id
        if self.inv_access_secret is not None:
            result['InvAccessSecret'] = self.inv_access_secret
        if self.inv_bucket is not None:
            result['InvBucket'] = self.inv_bucket
        if self.inv_domain is not None:
            result['InvDomain'] = self.inv_domain
        if self.inv_location is not None:
            result['InvLocation'] = self.inv_location
        if self.inv_path is not None:
            result['InvPath'] = self.inv_path
        if self.inv_region_id is not None:
            result['InvRegionId'] = self.inv_region_id
        if self.inv_role is not None:
            result['InvRole'] = self.inv_role
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('AccessSecret') is not None:
            self.access_secret = m.get('AccessSecret')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('AgentList') is not None:
            self.agent_list = m.get('AgentList')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('InvAccessId') is not None:
            self.inv_access_id = m.get('InvAccessId')
        if m.get('InvAccessSecret') is not None:
            self.inv_access_secret = m.get('InvAccessSecret')
        if m.get('InvBucket') is not None:
            self.inv_bucket = m.get('InvBucket')
        if m.get('InvDomain') is not None:
            self.inv_domain = m.get('InvDomain')
        if m.get('InvLocation') is not None:
            self.inv_location = m.get('InvLocation')
        if m.get('InvPath') is not None:
            self.inv_path = m.get('InvPath')
        if m.get('InvRegionId') is not None:
            self.inv_region_id = m.get('InvRegionId')
        if m.get('InvRole') is not None:
            self.inv_role = m.get('InvRole')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class Audit(TeaModel):
    def __init__(
        self,
        log_mode: str = None,
    ):
        self.log_mode = log_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_mode is not None:
            result['LogMode'] = self.log_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogMode') is not None:
            self.log_mode = m.get('LogMode')
        return self


class CreateAddressInfo(TeaModel):
    def __init__(
        self,
        address_detail: AddressDetail = None,
        name: str = None,
        tags: str = None,
    ):
        # This parameter is required.
        self.address_detail = address_detail
        # This parameter is required.
        self.name = name
        self.tags = tags

    def validate(self):
        if self.address_detail:
            self.address_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_detail is not None:
            result['AddressDetail'] = self.address_detail.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressDetail') is not None:
            temp_model = AddressDetail()
            self.address_detail = temp_model.from_map(m['AddressDetail'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class CreateAgentInfo(TeaModel):
    def __init__(
        self,
        agent_endpoint: str = None,
        deploy_method: str = None,
        name: str = None,
        tags: str = None,
        tunnel_id: str = None,
    ):
        # This parameter is required.
        self.agent_endpoint = agent_endpoint
        # This parameter is required.
        self.deploy_method = deploy_method
        # This parameter is required.
        self.name = name
        self.tags = tags
        # This parameter is required.
        self.tunnel_id = tunnel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_endpoint is not None:
            result['AgentEndpoint'] = self.agent_endpoint
        if self.deploy_method is not None:
            result['DeployMethod'] = self.deploy_method
        if self.name is not None:
            result['Name'] = self.name
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.tunnel_id is not None:
            result['TunnelId'] = self.tunnel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentEndpoint') is not None:
            self.agent_endpoint = m.get('AgentEndpoint')
        if m.get('DeployMethod') is not None:
            self.deploy_method = m.get('DeployMethod')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TunnelId') is not None:
            self.tunnel_id = m.get('TunnelId')
        return self


class FileTypeFilters(TeaModel):
    def __init__(
        self,
        exclude_dir: bool = None,
        exclude_symlink: bool = None,
    ):
        self.exclude_dir = exclude_dir
        self.exclude_symlink = exclude_symlink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_dir is not None:
            result['ExcludeDir'] = self.exclude_dir
        if self.exclude_symlink is not None:
            result['ExcludeSymlink'] = self.exclude_symlink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeDir') is not None:
            self.exclude_dir = m.get('ExcludeDir')
        if m.get('ExcludeSymlink') is not None:
            self.exclude_symlink = m.get('ExcludeSymlink')
        return self


class KeyFilterItem(TeaModel):
    def __init__(
        self,
        regex: List[str] = None,
    ):
        self.regex = regex

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regex is not None:
            result['Regex'] = self.regex
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Regex') is not None:
            self.regex = m.get('Regex')
        return self


class KeyFilters(TeaModel):
    def __init__(
        self,
        excludes: KeyFilterItem = None,
        includes: KeyFilterItem = None,
    ):
        self.excludes = excludes
        self.includes = includes

    def validate(self):
        if self.excludes:
            self.excludes.validate()
        if self.includes:
            self.includes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.excludes is not None:
            result['Excludes'] = self.excludes.to_map()
        if self.includes is not None:
            result['Includes'] = self.includes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Excludes') is not None:
            temp_model = KeyFilterItem()
            self.excludes = temp_model.from_map(m['Excludes'])
        if m.get('Includes') is not None:
            temp_model = KeyFilterItem()
            self.includes = temp_model.from_map(m['Includes'])
        return self


class TimeFilter(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class LastModifyFilterItem(TeaModel):
    def __init__(
        self,
        time_filter: List[TimeFilter] = None,
    ):
        self.time_filter = time_filter

    def validate(self):
        if self.time_filter:
            for k in self.time_filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TimeFilter'] = []
        if self.time_filter is not None:
            for k in self.time_filter:
                result['TimeFilter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.time_filter = []
        if m.get('TimeFilter') is not None:
            for k in m.get('TimeFilter'):
                temp_model = TimeFilter()
                self.time_filter.append(temp_model.from_map(k))
        return self


class LastModifiedFilters(TeaModel):
    def __init__(
        self,
        excludes: LastModifyFilterItem = None,
        includes: LastModifyFilterItem = None,
    ):
        self.excludes = excludes
        self.includes = includes

    def validate(self):
        if self.excludes:
            self.excludes.validate()
        if self.includes:
            self.includes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.excludes is not None:
            result['Excludes'] = self.excludes.to_map()
        if self.includes is not None:
            result['Includes'] = self.includes.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Excludes') is not None:
            temp_model = LastModifyFilterItem()
            self.excludes = temp_model.from_map(m['Excludes'])
        if m.get('Includes') is not None:
            temp_model = LastModifyFilterItem()
            self.includes = temp_model.from_map(m['Includes'])
        return self


class FilterRule(TeaModel):
    def __init__(
        self,
        file_type_filters: FileTypeFilters = None,
        key_filters: KeyFilters = None,
        last_modified_filters: LastModifiedFilters = None,
    ):
        self.file_type_filters = file_type_filters
        self.key_filters = key_filters
        self.last_modified_filters = last_modified_filters

    def validate(self):
        if self.file_type_filters:
            self.file_type_filters.validate()
        if self.key_filters:
            self.key_filters.validate()
        if self.last_modified_filters:
            self.last_modified_filters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_type_filters is not None:
            result['FileTypeFilters'] = self.file_type_filters.to_map()
        if self.key_filters is not None:
            result['KeyFilters'] = self.key_filters.to_map()
        if self.last_modified_filters is not None:
            result['LastModifiedFilters'] = self.last_modified_filters.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileTypeFilters') is not None:
            temp_model = FileTypeFilters()
            self.file_type_filters = temp_model.from_map(m['FileTypeFilters'])
        if m.get('KeyFilters') is not None:
            temp_model = KeyFilters()
            self.key_filters = temp_model.from_map(m['KeyFilters'])
        if m.get('LastModifiedFilters') is not None:
            temp_model = LastModifiedFilters()
            self.last_modified_filters = temp_model.from_map(m['LastModifiedFilters'])
        return self


class ImportQos(TeaModel):
    def __init__(
        self,
        max_band_width: int = None,
        max_import_task_qps: int = None,
    ):
        self.max_band_width = max_band_width
        self.max_import_task_qps = max_import_task_qps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_band_width is not None:
            result['MaxBandWidth'] = self.max_band_width
        if self.max_import_task_qps is not None:
            result['MaxImportTaskQps'] = self.max_import_task_qps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxBandWidth') is not None:
            self.max_band_width = m.get('MaxBandWidth')
        if m.get('MaxImportTaskQps') is not None:
            self.max_import_task_qps = m.get('MaxImportTaskQps')
        return self


class ScheduleRule(TeaModel):
    def __init__(
        self,
        max_schedule_count: int = None,
        start_cron_expression: str = None,
        suspend_cron_expression: str = None,
    ):
        self.max_schedule_count = max_schedule_count
        self.start_cron_expression = start_cron_expression
        self.suspend_cron_expression = suspend_cron_expression

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_schedule_count is not None:
            result['MaxScheduleCount'] = self.max_schedule_count
        if self.start_cron_expression is not None:
            result['StartCronExpression'] = self.start_cron_expression
        if self.suspend_cron_expression is not None:
            result['SuspendCronExpression'] = self.suspend_cron_expression
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxScheduleCount') is not None:
            self.max_schedule_count = m.get('MaxScheduleCount')
        if m.get('StartCronExpression') is not None:
            self.start_cron_expression = m.get('StartCronExpression')
        if m.get('SuspendCronExpression') is not None:
            self.suspend_cron_expression = m.get('SuspendCronExpression')
        return self


class CreateJobInfo(TeaModel):
    def __init__(
        self,
        audit: Audit = None,
        convert_symlink_target: bool = None,
        create_report: bool = None,
        dest_address: str = None,
        enable_multi_versioning: bool = None,
        filter_rule: FilterRule = None,
        import_qos: ImportQos = None,
        name: str = None,
        overwrite_mode: str = None,
        parent_version: str = None,
        schedule_rule: ScheduleRule = None,
        src_address: str = None,
        tags: str = None,
        transfer_mode: str = None,
    ):
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
        # This parameter is required.
        self.transfer_mode = transfer_mode

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.transfer_mode is not None:
            result['TransferMode'] = self.transfer_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audit') is not None:
            temp_model = Audit()
            self.audit = temp_model.from_map(m['Audit'])
        if m.get('ConvertSymlinkTarget') is not None:
            self.convert_symlink_target = m.get('ConvertSymlinkTarget')
        if m.get('CreateReport') is not None:
            self.create_report = m.get('CreateReport')
        if m.get('DestAddress') is not None:
            self.dest_address = m.get('DestAddress')
        if m.get('EnableMultiVersioning') is not None:
            self.enable_multi_versioning = m.get('EnableMultiVersioning')
        if m.get('FilterRule') is not None:
            temp_model = FilterRule()
            self.filter_rule = temp_model.from_map(m['FilterRule'])
        if m.get('ImportQos') is not None:
            temp_model = ImportQos()
            self.import_qos = temp_model.from_map(m['ImportQos'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OverwriteMode') is not None:
            self.overwrite_mode = m.get('OverwriteMode')
        if m.get('ParentVersion') is not None:
            self.parent_version = m.get('ParentVersion')
        if m.get('ScheduleRule') is not None:
            temp_model = ScheduleRule()
            self.schedule_rule = temp_model.from_map(m['ScheduleRule'])
        if m.get('SrcAddress') is not None:
            self.src_address = m.get('SrcAddress')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TransferMode') is not None:
            self.transfer_mode = m.get('TransferMode')
        return self


class CreateReportInfo(TeaModel):
    def __init__(
        self,
        job_name: str = None,
        runtime_id: int = None,
        version: str = None,
    ):
        self.job_name = job_name
        self.runtime_id = runtime_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_name is not None:
            result['JobName'] = self.job_name
        if self.runtime_id is not None:
            result['RuntimeId'] = self.runtime_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        if m.get('RuntimeId') is not None:
            self.runtime_id = m.get('RuntimeId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class TunnelQos(TeaModel):
    def __init__(
        self,
        max_bandwidth: int = None,
        max_qps: int = None,
    ):
        self.max_bandwidth = max_bandwidth
        self.max_qps = max_qps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_bandwidth is not None:
            result['MaxBandwidth'] = self.max_bandwidth
        if self.max_qps is not None:
            result['MaxQps'] = self.max_qps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxBandwidth') is not None:
            self.max_bandwidth = m.get('MaxBandwidth')
        if m.get('MaxQps') is not None:
            self.max_qps = m.get('MaxQps')
        return self


class CreateTunnelInfo(TeaModel):
    def __init__(
        self,
        tags: str = None,
        tunnel_qos: TunnelQos = None,
    ):
        self.tags = tags
        self.tunnel_qos = tunnel_qos

    def validate(self):
        if self.tunnel_qos:
            self.tunnel_qos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.tunnel_qos is not None:
            result['TunnelQos'] = self.tunnel_qos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TunnelQos') is not None:
            temp_model = TunnelQos()
            self.tunnel_qos = temp_model.from_map(m['TunnelQos'])
        return self


class VerifyResp(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        http_code: str = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.http_code = http_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.http_code is not None:
            result['HttpCode'] = self.http_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')
        return self


class GetAddressResp(TeaModel):
    def __init__(
        self,
        address_detail: AddressDetail = None,
        create_time: str = None,
        modify_time: str = None,
        name: str = None,
        owner: str = None,
        status: str = None,
        tags: str = None,
        verify_result: VerifyResp = None,
        verify_time: str = None,
        version: str = None,
    ):
        self.address_detail = address_detail
        self.create_time = create_time
        self.modify_time = modify_time
        self.name = name
        self.owner = owner
        self.status = status
        self.tags = tags
        self.verify_result = verify_result
        self.verify_time = verify_time
        self.version = version

    def validate(self):
        if self.address_detail:
            self.address_detail.validate()
        if self.verify_result:
            self.verify_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_detail is not None:
            result['AddressDetail'] = self.address_detail.to_map()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.status is not None:
            result['Status'] = self.status
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.verify_result is not None:
            result['VerifyResult'] = self.verify_result.to_map()
        if self.verify_time is not None:
            result['VerifyTime'] = self.verify_time
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressDetail') is not None:
            temp_model = AddressDetail()
            self.address_detail = temp_model.from_map(m['AddressDetail'])
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('VerifyResult') is not None:
            temp_model = VerifyResp()
            self.verify_result = temp_model.from_map(m['VerifyResult'])
        if m.get('VerifyTime') is not None:
            self.verify_time = m.get('VerifyTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetAgentResp(TeaModel):
    def __init__(
        self,
        activation_key: str = None,
        agent_endpoint: str = None,
        create_time: str = None,
        deploy_method: str = None,
        modify_time: str = None,
        name: str = None,
        owner: str = None,
        tags: str = None,
        tunnel_id: str = None,
        version: str = None,
    ):
        self.activation_key = activation_key
        self.agent_endpoint = agent_endpoint
        self.create_time = create_time
        self.deploy_method = deploy_method
        self.modify_time = modify_time
        self.name = name
        self.owner = owner
        self.tags = tags
        self.tunnel_id = tunnel_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activation_key is not None:
            result['ActivationKey'] = self.activation_key
        if self.agent_endpoint is not None:
            result['AgentEndpoint'] = self.agent_endpoint
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.deploy_method is not None:
            result['DeployMethod'] = self.deploy_method
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.tunnel_id is not None:
            result['TunnelId'] = self.tunnel_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivationKey') is not None:
            self.activation_key = m.get('ActivationKey')
        if m.get('AgentEndpoint') is not None:
            self.agent_endpoint = m.get('AgentEndpoint')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeployMethod') is not None:
            self.deploy_method = m.get('DeployMethod')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TunnelId') is not None:
            self.tunnel_id = m.get('TunnelId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetAgentStatusResp(TeaModel):
    def __init__(
        self,
        status: str = None,
    ):
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetJobResp(TeaModel):
    def __init__(
        self,
        audit: Audit = None,
        convert_symlink_target: bool = None,
        create_report: bool = None,
        create_time: str = None,
        dest_address: str = None,
        enable_multi_versioning: bool = None,
        filter_rule: FilterRule = None,
        import_qos: ImportQos = None,
        modify_time: str = None,
        name: str = None,
        overwrite_mode: str = None,
        owner: str = None,
        parent_name: str = None,
        parent_version: str = None,
        schedule_rule: ScheduleRule = None,
        src_address: str = None,
        status: str = None,
        tags: str = None,
        transfer_mode: str = None,
        version: str = None,
    ):
        self.audit = audit
        self.convert_symlink_target = convert_symlink_target
        self.create_report = create_report
        self.create_time = create_time
        self.dest_address = dest_address
        self.enable_multi_versioning = enable_multi_versioning
        self.filter_rule = filter_rule
        self.import_qos = import_qos
        self.modify_time = modify_time
        self.name = name
        self.overwrite_mode = overwrite_mode
        self.owner = owner
        self.parent_name = parent_name
        self.parent_version = parent_version
        self.schedule_rule = schedule_rule
        self.src_address = src_address
        self.status = status
        self.tags = tags
        self.transfer_mode = transfer_mode
        self.version = version

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.transfer_mode is not None:
            result['TransferMode'] = self.transfer_mode
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Audit') is not None:
            temp_model = Audit()
            self.audit = temp_model.from_map(m['Audit'])
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
            temp_model = FilterRule()
            self.filter_rule = temp_model.from_map(m['FilterRule'])
        if m.get('ImportQos') is not None:
            temp_model = ImportQos()
            self.import_qos = temp_model.from_map(m['ImportQos'])
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
            temp_model = ScheduleRule()
            self.schedule_rule = temp_model.from_map(m['ScheduleRule'])
        if m.get('SrcAddress') is not None:
            self.src_address = m.get('SrcAddress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TransferMode') is not None:
            self.transfer_mode = m.get('TransferMode')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetJobResultResp(TeaModel):
    def __init__(
        self,
        address_type: str = None,
        copied_object_count: int = None,
        copied_object_size: int = None,
        failed_object_count: int = None,
        inv_access_id: str = None,
        inv_access_secret: str = None,
        inv_bucket: str = None,
        inv_domain: str = None,
        inv_location: str = None,
        inv_path: str = None,
        inv_region_id: str = None,
        ready_retry: str = None,
        total_object_count: int = None,
        total_object_size: int = None,
        version: str = None,
    ):
        self.address_type = address_type
        self.copied_object_count = copied_object_count
        self.copied_object_size = copied_object_size
        self.failed_object_count = failed_object_count
        self.inv_access_id = inv_access_id
        self.inv_access_secret = inv_access_secret
        self.inv_bucket = inv_bucket
        self.inv_domain = inv_domain
        self.inv_location = inv_location
        self.inv_path = inv_path
        self.inv_region_id = inv_region_id
        self.ready_retry = ready_retry
        self.total_object_count = total_object_count
        self.total_object_size = total_object_size
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.copied_object_count is not None:
            result['CopiedObjectCount'] = self.copied_object_count
        if self.copied_object_size is not None:
            result['CopiedObjectSize'] = self.copied_object_size
        if self.failed_object_count is not None:
            result['FailedObjectCount'] = self.failed_object_count
        if self.inv_access_id is not None:
            result['InvAccessId'] = self.inv_access_id
        if self.inv_access_secret is not None:
            result['InvAccessSecret'] = self.inv_access_secret
        if self.inv_bucket is not None:
            result['InvBucket'] = self.inv_bucket
        if self.inv_domain is not None:
            result['InvDomain'] = self.inv_domain
        if self.inv_location is not None:
            result['InvLocation'] = self.inv_location
        if self.inv_path is not None:
            result['InvPath'] = self.inv_path
        if self.inv_region_id is not None:
            result['InvRegionId'] = self.inv_region_id
        if self.ready_retry is not None:
            result['ReadyRetry'] = self.ready_retry
        if self.total_object_count is not None:
            result['TotalObjectCount'] = self.total_object_count
        if self.total_object_size is not None:
            result['TotalObjectSize'] = self.total_object_size
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('CopiedObjectCount') is not None:
            self.copied_object_count = m.get('CopiedObjectCount')
        if m.get('CopiedObjectSize') is not None:
            self.copied_object_size = m.get('CopiedObjectSize')
        if m.get('FailedObjectCount') is not None:
            self.failed_object_count = m.get('FailedObjectCount')
        if m.get('InvAccessId') is not None:
            self.inv_access_id = m.get('InvAccessId')
        if m.get('InvAccessSecret') is not None:
            self.inv_access_secret = m.get('InvAccessSecret')
        if m.get('InvBucket') is not None:
            self.inv_bucket = m.get('InvBucket')
        if m.get('InvDomain') is not None:
            self.inv_domain = m.get('InvDomain')
        if m.get('InvLocation') is not None:
            self.inv_location = m.get('InvLocation')
        if m.get('InvPath') is not None:
            self.inv_path = m.get('InvPath')
        if m.get('InvRegionId') is not None:
            self.inv_region_id = m.get('InvRegionId')
        if m.get('ReadyRetry') is not None:
            self.ready_retry = m.get('ReadyRetry')
        if m.get('TotalObjectCount') is not None:
            self.total_object_count = m.get('TotalObjectCount')
        if m.get('TotalObjectSize') is not None:
            self.total_object_size = m.get('TotalObjectSize')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetReportResp(TeaModel):
    def __init__(
        self,
        copied_count: int = None,
        error_message: str = None,
        failed_count: int = None,
        failed_list_prefix: str = None,
        job_create_time: str = None,
        job_end_time: str = None,
        job_execute_time: str = None,
        report_create_time: str = None,
        report_end_time: str = None,
        skipped_count: int = None,
        skipped_list_prefix: str = None,
        status: str = None,
        total_count: int = None,
        total_list_prefix: str = None,
    ):
        self.copied_count = copied_count
        self.error_message = error_message
        self.failed_count = failed_count
        self.failed_list_prefix = failed_list_prefix
        self.job_create_time = job_create_time
        self.job_end_time = job_end_time
        self.job_execute_time = job_execute_time
        self.report_create_time = report_create_time
        self.report_end_time = report_end_time
        self.skipped_count = skipped_count
        self.skipped_list_prefix = skipped_list_prefix
        self.status = status
        self.total_count = total_count
        self.total_list_prefix = total_list_prefix

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.copied_count is not None:
            result['CopiedCount'] = self.copied_count
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count
        if self.failed_list_prefix is not None:
            result['FailedListPrefix'] = self.failed_list_prefix
        if self.job_create_time is not None:
            result['JobCreateTime'] = self.job_create_time
        if self.job_end_time is not None:
            result['JobEndTime'] = self.job_end_time
        if self.job_execute_time is not None:
            result['JobExecuteTime'] = self.job_execute_time
        if self.report_create_time is not None:
            result['ReportCreateTime'] = self.report_create_time
        if self.report_end_time is not None:
            result['ReportEndTime'] = self.report_end_time
        if self.skipped_count is not None:
            result['SkippedCount'] = self.skipped_count
        if self.skipped_list_prefix is not None:
            result['SkippedListPrefix'] = self.skipped_list_prefix
        if self.status is not None:
            result['Status'] = self.status
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_list_prefix is not None:
            result['TotalListPrefix'] = self.total_list_prefix
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CopiedCount') is not None:
            self.copied_count = m.get('CopiedCount')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')
        if m.get('FailedListPrefix') is not None:
            self.failed_list_prefix = m.get('FailedListPrefix')
        if m.get('JobCreateTime') is not None:
            self.job_create_time = m.get('JobCreateTime')
        if m.get('JobEndTime') is not None:
            self.job_end_time = m.get('JobEndTime')
        if m.get('JobExecuteTime') is not None:
            self.job_execute_time = m.get('JobExecuteTime')
        if m.get('ReportCreateTime') is not None:
            self.report_create_time = m.get('ReportCreateTime')
        if m.get('ReportEndTime') is not None:
            self.report_end_time = m.get('ReportEndTime')
        if m.get('SkippedCount') is not None:
            self.skipped_count = m.get('SkippedCount')
        if m.get('SkippedListPrefix') is not None:
            self.skipped_list_prefix = m.get('SkippedListPrefix')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalListPrefix') is not None:
            self.total_list_prefix = m.get('TotalListPrefix')
        return self


class GetTunnelResp(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        modify_time: str = None,
        owner: str = None,
        tags: str = None,
        tunnel_id: str = None,
        tunnel_qos: TunnelQos = None,
    ):
        self.create_time = create_time
        self.modify_time = modify_time
        self.owner = owner
        self.tags = tags
        self.tunnel_id = tunnel_id
        self.tunnel_qos = tunnel_qos

    def validate(self):
        if self.tunnel_qos:
            self.tunnel_qos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.tunnel_id is not None:
            result['TunnelId'] = self.tunnel_id
        if self.tunnel_qos is not None:
            result['TunnelQos'] = self.tunnel_qos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TunnelId') is not None:
            self.tunnel_id = m.get('TunnelId')
        if m.get('TunnelQos') is not None:
            temp_model = TunnelQos()
            self.tunnel_qos = temp_model.from_map(m['TunnelQos'])
        return self


class JobHistory(TeaModel):
    def __init__(
        self,
        commit_id: str = None,
        copied_count: int = None,
        copied_size: int = None,
        end_time: str = None,
        failed_count: int = None,
        job_version: str = None,
        list_status: str = None,
        message: str = None,
        name: str = None,
        operator: str = None,
        runtime_id: str = None,
        runtime_state: str = None,
        start_time: str = None,
        status: str = None,
        total_count: int = None,
        total_size: int = None,
    ):
        self.commit_id = commit_id
        self.copied_count = copied_count
        self.copied_size = copied_size
        self.end_time = end_time
        self.failed_count = failed_count
        self.job_version = job_version
        self.list_status = list_status
        self.message = message
        self.name = name
        self.operator = operator
        self.runtime_id = runtime_id
        self.runtime_state = runtime_state
        self.start_time = start_time
        self.status = status
        self.total_count = total_count
        self.total_size = total_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commit_id is not None:
            result['CommitId'] = self.commit_id
        if self.copied_count is not None:
            result['CopiedCount'] = self.copied_count
        if self.copied_size is not None:
            result['CopiedSize'] = self.copied_size
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count
        if self.job_version is not None:
            result['JobVersion'] = self.job_version
        if self.list_status is not None:
            result['ListStatus'] = self.list_status
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.runtime_id is not None:
            result['RuntimeId'] = self.runtime_id
        if self.runtime_state is not None:
            result['RuntimeState'] = self.runtime_state
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')
        if m.get('CopiedCount') is not None:
            self.copied_count = m.get('CopiedCount')
        if m.get('CopiedSize') is not None:
            self.copied_size = m.get('CopiedSize')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')
        if m.get('JobVersion') is not None:
            self.job_version = m.get('JobVersion')
        if m.get('ListStatus') is not None:
            self.list_status = m.get('ListStatus')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('RuntimeId') is not None:
            self.runtime_id = m.get('RuntimeId')
        if m.get('RuntimeState') is not None:
            self.runtime_state = m.get('RuntimeState')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListAddressResp(TeaModel):
    def __init__(
        self,
        import_address: List[GetAddressResp] = None,
        next_marker: str = None,
        truncated: bool = None,
    ):
        self.import_address = import_address
        self.next_marker = next_marker
        self.truncated = truncated

    def validate(self):
        if self.import_address:
            for k in self.import_address:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ImportAddress'] = []
        if self.import_address is not None:
            for k in self.import_address:
                result['ImportAddress'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.truncated is not None:
            result['Truncated'] = self.truncated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.import_address = []
        if m.get('ImportAddress') is not None:
            for k in m.get('ImportAddress'):
                temp_model = GetAddressResp()
                self.import_address.append(temp_model.from_map(k))
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('Truncated') is not None:
            self.truncated = m.get('Truncated')
        return self


class ListAgentResp(TeaModel):
    def __init__(
        self,
        import_agent: List[GetAgentResp] = None,
        next_marker: str = None,
        truncated: bool = None,
    ):
        self.import_agent = import_agent
        self.next_marker = next_marker
        self.truncated = truncated

    def validate(self):
        if self.import_agent:
            for k in self.import_agent:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ImportAgent'] = []
        if self.import_agent is not None:
            for k in self.import_agent:
                result['ImportAgent'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.truncated is not None:
            result['Truncated'] = self.truncated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.import_agent = []
        if m.get('ImportAgent') is not None:
            for k in m.get('ImportAgent'):
                temp_model = GetAgentResp()
                self.import_agent.append(temp_model.from_map(k))
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('Truncated') is not None:
            self.truncated = m.get('Truncated')
        return self


class ListJobHistoryResp(TeaModel):
    def __init__(
        self,
        job_history: List[JobHistory] = None,
        next_marker: str = None,
        truncated: str = None,
    ):
        self.job_history = job_history
        self.next_marker = next_marker
        self.truncated = truncated

    def validate(self):
        if self.job_history:
            for k in self.job_history:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['JobHistory'] = []
        if self.job_history is not None:
            for k in self.job_history:
                result['JobHistory'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.truncated is not None:
            result['Truncated'] = self.truncated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_history = []
        if m.get('JobHistory') is not None:
            for k in m.get('JobHistory'):
                temp_model = JobHistory()
                self.job_history.append(temp_model.from_map(k))
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('Truncated') is not None:
            self.truncated = m.get('Truncated')
        return self


class ListJobInfo(TeaModel):
    def __init__(
        self,
        import_job: List[CreateJobInfo] = None,
        next_marker: str = None,
        truncated: bool = None,
    ):
        self.import_job = import_job
        self.next_marker = next_marker
        self.truncated = truncated

    def validate(self):
        if self.import_job:
            for k in self.import_job:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ImportJob'] = []
        if self.import_job is not None:
            for k in self.import_job:
                result['ImportJob'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.truncated is not None:
            result['Truncated'] = self.truncated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.import_job = []
        if m.get('ImportJob') is not None:
            for k in m.get('ImportJob'):
                temp_model = CreateJobInfo()
                self.import_job.append(temp_model.from_map(k))
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('Truncated') is not None:
            self.truncated = m.get('Truncated')
        return self


class ListJobResp(TeaModel):
    def __init__(
        self,
        import_job: List[GetJobResp] = None,
        next_marker: str = None,
        truncated: bool = None,
    ):
        self.import_job = import_job
        self.next_marker = next_marker
        self.truncated = truncated

    def validate(self):
        if self.import_job:
            for k in self.import_job:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ImportJob'] = []
        if self.import_job is not None:
            for k in self.import_job:
                result['ImportJob'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.truncated is not None:
            result['Truncated'] = self.truncated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.import_job = []
        if m.get('ImportJob') is not None:
            for k in m.get('ImportJob'):
                temp_model = GetJobResp()
                self.import_job.append(temp_model.from_map(k))
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('Truncated') is not None:
            self.truncated = m.get('Truncated')
        return self


class ListTunnelResp(TeaModel):
    def __init__(
        self,
        import_tunnel: List[GetTunnelResp] = None,
        next_marker: str = None,
        truncated: bool = None,
    ):
        self.import_tunnel = import_tunnel
        self.next_marker = next_marker
        self.truncated = truncated

    def validate(self):
        if self.import_tunnel:
            for k in self.import_tunnel:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ImportTunnel'] = []
        if self.import_tunnel is not None:
            for k in self.import_tunnel:
                result['ImportTunnel'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.truncated is not None:
            result['Truncated'] = self.truncated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.import_tunnel = []
        if m.get('ImportTunnel') is not None:
            for k in m.get('ImportTunnel'):
                temp_model = GetTunnelResp()
                self.import_tunnel.append(temp_model.from_map(k))
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('Truncated') is not None:
            self.truncated = m.get('Truncated')
        return self


class UpdateAddressInfo(TeaModel):
    def __init__(
        self,
        agent_list: str = None,
    ):
        self.agent_list = agent_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_list is not None:
            result['AgentList'] = self.agent_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentList') is not None:
            self.agent_list = m.get('AgentList')
        return self


class UpdateJobInfo(TeaModel):
    def __init__(
        self,
        import_qos: ImportQos = None,
        status: str = None,
    ):
        self.import_qos = import_qos
        self.status = status

    def validate(self):
        if self.import_qos:
            self.import_qos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.import_qos is not None:
            result['ImportQos'] = self.import_qos.to_map()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportQos') is not None:
            temp_model = ImportQos()
            self.import_qos = temp_model.from_map(m['ImportQos'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateTunnelInfo(TeaModel):
    def __init__(
        self,
        tags: str = None,
        tunnel_qos: TunnelQos = None,
    ):
        self.tags = tags
        self.tunnel_qos = tunnel_qos

    def validate(self):
        if self.tunnel_qos:
            self.tunnel_qos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.tunnel_qos is not None:
            result['TunnelQos'] = self.tunnel_qos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TunnelQos') is not None:
            temp_model = TunnelQos()
            self.tunnel_qos = temp_model.from_map(m['TunnelQos'])
        return self


class VerifyAddressResp(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        status: str = None,
        verify_time: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.status = status
        self.verify_time = verify_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.status is not None:
            result['Status'] = self.status
        if self.verify_time is not None:
            result['VerifyTime'] = self.verify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VerifyTime') is not None:
            self.verify_time = m.get('VerifyTime')
        return self


class CreateAddressRequest(TeaModel):
    def __init__(
        self,
        import_address: CreateAddressInfo = None,
    ):
        # The details for creating the data address.
        self.import_address = import_address

    def validate(self):
        if self.import_address:
            self.import_address.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.import_address is not None:
            result['ImportAddress'] = self.import_address.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportAddress') is not None:
            temp_model = CreateAddressInfo()
            self.import_address = temp_model.from_map(m['ImportAddress'])
        return self


class CreateAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateAgentRequest(TeaModel):
    def __init__(
        self,
        import_agent: CreateAgentInfo = None,
    ):
        # The details for creating the agent.
        self.import_agent = import_agent

    def validate(self):
        if self.import_agent:
            self.import_agent.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.import_agent is not None:
            result['ImportAgent'] = self.import_agent.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportAgent') is not None:
            temp_model = CreateAgentInfo()
            self.import_agent = temp_model.from_map(m['ImportAgent'])
        return self


class CreateAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateJobRequest(TeaModel):
    def __init__(
        self,
        import_job: CreateJobInfo = None,
    ):
        # The details for creating the migration task.
        # 
        # This parameter is required.
        self.import_job = import_job

    def validate(self):
        if self.import_job:
            self.import_job.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.import_job is not None:
            result['ImportJob'] = self.import_job.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportJob') is not None:
            temp_model = CreateJobInfo()
            self.import_job = temp_model.from_map(m['ImportJob'])
        return self


class CreateJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateReportRequest(TeaModel):
    def __init__(
        self,
        create_report: CreateReportInfo = None,
    ):
        # The details for creating the migration report.
        self.create_report = create_report

    def validate(self):
        if self.create_report:
            self.create_report.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_report is not None:
            result['CreateReport'] = self.create_report.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateReport') is not None:
            temp_model = CreateReportInfo()
            self.create_report = temp_model.from_map(m['CreateReport'])
        return self


class CreateReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateTunnelRequest(TeaModel):
    def __init__(
        self,
        import_tunnel: CreateTunnelInfo = None,
    ):
        # The details for creating the tunnel.
        self.import_tunnel = import_tunnel

    def validate(self):
        if self.import_tunnel:
            self.import_tunnel.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.import_tunnel is not None:
            result['ImportTunnel'] = self.import_tunnel.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportTunnel') is not None:
            temp_model = CreateTunnelInfo()
            self.import_tunnel = temp_model.from_map(m['ImportTunnel'])
        return self


class CreateTunnelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteJobRequest(TeaModel):
    def __init__(
        self,
        force_delete: bool = None,
    ):
        # Specifies whether to force delete the subtask. If the task has subtasks and you set this parameter to true, the task and its subtasks are forcibly deleted. If this parameter is set to false, the task and its subtasks fail to be deleted.
        self.force_delete = force_delete

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force_delete is not None:
            result['forceDelete'] = self.force_delete
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('forceDelete') is not None:
            self.force_delete = m.get('forceDelete')
        return self


class DeleteJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteTunnelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class GetAddressResponseBody(TeaModel):
    def __init__(
        self,
        import_address: GetAddressResp = None,
    ):
        # The details for obtaining the data address.
        # 
        # Valid values:
        # 
        # *   1:1
        self.import_address = import_address

    def validate(self):
        if self.import_address:
            self.import_address.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.import_address is not None:
            result['ImportAddress'] = self.import_address.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportAddress') is not None:
            temp_model = GetAddressResp()
            self.import_address = temp_model.from_map(m['ImportAddress'])
        return self


class GetAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAddressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentResponseBody(TeaModel):
    def __init__(
        self,
        import_agent: GetAgentResp = None,
    ):
        # The details for obtaining the details of the agent.
        self.import_agent = import_agent

    def validate(self):
        if self.import_agent:
            self.import_agent.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.import_agent is not None:
            result['ImportAgent'] = self.import_agent.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportAgent') is not None:
            temp_model = GetAgentResp()
            self.import_agent = temp_model.from_map(m['ImportAgent'])
        return self


class GetAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAgentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentStatusResponseBody(TeaModel):
    def __init__(
        self,
        import_agent_status: GetAgentStatusResp = None,
    ):
        # The details for obtaining the status of the agent.
        self.import_agent_status = import_agent_status

    def validate(self):
        if self.import_agent_status:
            self.import_agent_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.import_agent_status is not None:
            result['ImportAgentStatus'] = self.import_agent_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportAgentStatus') is not None:
            temp_model = GetAgentStatusResp()
            self.import_agent_status = temp_model.from_map(m['ImportAgentStatus'])
        return self


class GetAgentStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAgentStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAgentStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobRequest(TeaModel):
    def __init__(
        self,
        by_version: str = None,
    ):
        # Specifies whether to obtain the details of the migration task by using the task ID.
        self.by_version = by_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.by_version is not None:
            result['byVersion'] = self.by_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('byVersion') is not None:
            self.by_version = m.get('byVersion')
        return self


class GetJobResponseBody(TeaModel):
    def __init__(
        self,
        import_job: GetJobResp = None,
    ):
        # The details for obtaining the details of the migration task.
        self.import_job = import_job

    def validate(self):
        if self.import_job:
            self.import_job.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.import_job is not None:
            result['ImportJob'] = self.import_job.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportJob') is not None:
            temp_model = GetJobResp()
            self.import_job = temp_model.from_map(m['ImportJob'])
        return self


class GetJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobResultRequest(TeaModel):
    def __init__(
        self,
        runtime_id: int = None,
    ):
        # The execution ID of the task.
        # 
        # This parameter is required.
        self.runtime_id = runtime_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.runtime_id is not None:
            result['runtimeId'] = self.runtime_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('runtimeId') is not None:
            self.runtime_id = m.get('runtimeId')
        return self


class GetJobResultResponseBody(TeaModel):
    def __init__(
        self,
        import_job_result: GetJobResultResp = None,
    ):
        # The details for obtaining the retries of the migration task.
        self.import_job_result = import_job_result

    def validate(self):
        if self.import_job_result:
            self.import_job_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.import_job_result is not None:
            result['ImportJobResult'] = self.import_job_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportJobResult') is not None:
            temp_model = GetJobResultResp()
            self.import_job_result = temp_model.from_map(m['ImportJobResult'])
        return self


class GetJobResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetJobResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetReportRequest(TeaModel):
    def __init__(
        self,
        runtime_id: int = None,
        version: str = None,
    ):
        # The execution ID of the migration task.
        self.runtime_id = runtime_id
        # The ID of the migration task.
        # 
        # This parameter is required.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.runtime_id is not None:
            result['runtimeId'] = self.runtime_id
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('runtimeId') is not None:
            self.runtime_id = m.get('runtimeId')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetReportResponseBody(TeaModel):
    def __init__(
        self,
        get_report_response: GetReportResp = None,
    ):
        # The details for obtaining the migration report.
        self.get_report_response = get_report_response

    def validate(self):
        if self.get_report_response:
            self.get_report_response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.get_report_response is not None:
            result['GetReportResponse'] = self.get_report_response.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GetReportResponse') is not None:
            temp_model = GetReportResp()
            self.get_report_response = temp_model.from_map(m['GetReportResponse'])
        return self


class GetReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetReportResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTunnelResponseBody(TeaModel):
    def __init__(
        self,
        import_tunnel: GetTunnelResp = None,
    ):
        # The details for obtaining the details of the tunnel.
        self.import_tunnel = import_tunnel

    def validate(self):
        if self.import_tunnel:
            self.import_tunnel.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.import_tunnel is not None:
            result['ImportTunnel'] = self.import_tunnel.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportTunnel') is not None:
            temp_model = GetTunnelResp()
            self.import_tunnel = temp_model.from_map(m['ImportTunnel'])
        return self


class GetTunnelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTunnelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTunnelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAddressRequest(TeaModel):
    def __init__(
        self,
        count: int = None,
        marker: str = None,
    ):
        # Specifies the number of migration addresses to be returned.\\
        # Valid values: 0 - 1000 (excluding 0).\\
        # Default value: 1000.
        self.count = count
        # The marker after which the migration addresses are listed.\\
        # By default, this parameter is left empty.
        self.marker = marker

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self


class ListAddressResponseBody(TeaModel):
    def __init__(
        self,
        import_address_list: ListAddressResp = None,
    ):
        # The details of migration addresses.
        self.import_address_list = import_address_list

    def validate(self):
        if self.import_address_list:
            self.import_address_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.import_address_list is not None:
            result['ImportAddressList'] = self.import_address_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportAddressList') is not None:
            temp_model = ListAddressResp()
            self.import_address_list = temp_model.from_map(m['ImportAddressList'])
        return self


class ListAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAddressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAgentRequest(TeaModel):
    def __init__(
        self,
        count: int = None,
        marker: str = None,
    ):
        # Specifies the number of agents to be returned.\\
        # Valid values: 0 - 1000.\\
        # Default value: 1000.
        self.count = count
        # The marker after which the agents are listed.\\
        # By default, this parameter is left empty.
        self.marker = marker

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self


class ListAgentResponseBody(TeaModel):
    def __init__(
        self,
        import_agent_list: ListAgentResp = None,
    ):
        # The details of the agents.
        self.import_agent_list = import_agent_list

    def validate(self):
        if self.import_agent_list:
            self.import_agent_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.import_agent_list is not None:
            result['ImportAgentList'] = self.import_agent_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportAgentList') is not None:
            temp_model = ListAgentResp()
            self.import_agent_list = temp_model.from_map(m['ImportAgentList'])
        return self


class ListAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAgentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        count: int = None,
        marker: str = None,
        parent_name: str = None,
    ):
        # Specifies whether to return subtasks.\\
        # Valid values: true and false.
        self.all = all
        # Specifies the number of migration tasks to be returned.\\
        # Valid values: 0 - 1000 (excluding 0).\\
        # Default value: 1000.
        self.count = count
        # The marker after which the migration tasks are listed.\\
        # By default, this parameter is left empty.
        self.marker = marker
        # The name of the parent task. If this parameter is specified, all subtasks of the parent task are returned.
        self.parent_name = parent_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['all'] = self.all
        if self.count is not None:
            result['count'] = self.count
        if self.marker is not None:
            result['marker'] = self.marker
        if self.parent_name is not None:
            result['parentName'] = self.parent_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all') is not None:
            self.all = m.get('all')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('parentName') is not None:
            self.parent_name = m.get('parentName')
        return self


class ListJobResponseBody(TeaModel):
    def __init__(
        self,
        import_job_list: ListJobResp = None,
    ):
        # The queried migration tasks.
        self.import_job_list = import_job_list

    def validate(self):
        if self.import_job_list:
            self.import_job_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.import_job_list is not None:
            result['ImportJobList'] = self.import_job_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportJobList') is not None:
            temp_model = ListJobResp()
            self.import_job_list = temp_model.from_map(m['ImportJobList'])
        return self


class ListJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobHistoryRequest(TeaModel):
    def __init__(
        self,
        count: int = None,
        marker: str = None,
        runtime_id: int = None,
    ):
        # Specifies the number of running records of the migration task to be returned.\\
        # Valid values: 0 - 1000.\\
        # Default value: 1000.
        self.count = count
        # The marker after which the running history of the task is listed.\\
        # By default, this parameter is left empty.
        self.marker = marker
        # The execution ID of the task. If you specify an execution ID, only the running history related to the execution ID is listed.
        self.runtime_id = runtime_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.marker is not None:
            result['marker'] = self.marker
        if self.runtime_id is not None:
            result['runtimeId'] = self.runtime_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('runtimeId') is not None:
            self.runtime_id = m.get('runtimeId')
        return self


class ListJobHistoryResponseBody(TeaModel):
    def __init__(
        self,
        job_history_list: ListJobHistoryResp = None,
    ):
        # The running history of the migration task.
        self.job_history_list = job_history_list

    def validate(self):
        if self.job_history_list:
            self.job_history_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_history_list is not None:
            result['JobHistoryList'] = self.job_history_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobHistoryList') is not None:
            temp_model = ListJobHistoryResp()
            self.job_history_list = temp_model.from_map(m['JobHistoryList'])
        return self


class ListJobHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListJobHistoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListJobHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTunnelRequest(TeaModel):
    def __init__(
        self,
        count: int = None,
        marker: str = None,
    ):
        # Specifies the number of tunnels to be returned.\\
        # Valid values: 0 - 1000.\\
        # Default value: 1000.
        self.count = count
        # The marker after which tunnels are listed.\\
        # By default, this parameter is left empty.
        self.marker = marker

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self


class ListTunnelResponseBody(TeaModel):
    def __init__(
        self,
        import_tunnel_list: ListTunnelResp = None,
    ):
        # The details of the tunnels.
        self.import_tunnel_list = import_tunnel_list

    def validate(self):
        if self.import_tunnel_list:
            self.import_tunnel_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.import_tunnel_list is not None:
            result['ImportTunnelList'] = self.import_tunnel_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportTunnelList') is not None:
            temp_model = ListTunnelResp()
            self.import_tunnel_list = temp_model.from_map(m['ImportTunnelList'])
        return self


class ListTunnelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTunnelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTunnelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAddressRequest(TeaModel):
    def __init__(
        self,
        import_address: UpdateAddressInfo = None,
    ):
        # The details for updating the data address.
        self.import_address = import_address

    def validate(self):
        if self.import_address:
            self.import_address.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.import_address is not None:
            result['ImportAddress'] = self.import_address.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportAddress') is not None:
            temp_model = UpdateAddressInfo()
            self.import_address = temp_model.from_map(m['ImportAddress'])
        return self


class UpdateAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateJobRequest(TeaModel):
    def __init__(
        self,
        import_job: UpdateJobInfo = None,
    ):
        # The details for updating the task.
        self.import_job = import_job

    def validate(self):
        if self.import_job:
            self.import_job.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.import_job is not None:
            result['ImportJob'] = self.import_job.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportJob') is not None:
            temp_model = UpdateJobInfo()
            self.import_job = temp_model.from_map(m['ImportJob'])
        return self


class UpdateJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateTunnelRequest(TeaModel):
    def __init__(
        self,
        import_tunnel: UpdateTunnelInfo = None,
    ):
        # The details for updating the tunnel.
        self.import_tunnel = import_tunnel

    def validate(self):
        if self.import_tunnel:
            self.import_tunnel.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.import_tunnel is not None:
            result['ImportTunnel'] = self.import_tunnel.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImportTunnel') is not None:
            temp_model = UpdateTunnelInfo()
            self.import_tunnel = temp_model.from_map(m['ImportTunnel'])
        return self


class UpdateTunnelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class VerifyAddressResponseBody(TeaModel):
    def __init__(
        self,
        verify_address_response: VerifyAddressResp = None,
    ):
        # 校验数据地址详情。
        self.verify_address_response = verify_address_response

    def validate(self):
        if self.verify_address_response:
            self.verify_address_response.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.verify_address_response is not None:
            result['VerifyAddressResponse'] = self.verify_address_response.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VerifyAddressResponse') is not None:
            temp_model = VerifyAddressResp()
            self.verify_address_response = temp_model.from_map(m['VerifyAddressResponse'])
        return self


class VerifyAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: VerifyAddressResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = VerifyAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


