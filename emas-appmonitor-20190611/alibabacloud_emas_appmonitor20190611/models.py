# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Any, Dict


class EventFilter(TeaModel):
    def __init__(
        self,
        key: str = None,
        op: str = None,
        sub_filters: List['EventFilter'] = None,
        values: List[str] = None,
    ):
        self.key = key
        # This parameter is required.
        self.op = op
        self.sub_filters = sub_filters
        self.values = values

    def validate(self):
        if self.sub_filters:
            for k in self.sub_filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.op is not None:
            result['Op'] = self.op
        result['SubFilters'] = []
        if self.sub_filters is not None:
            for k in self.sub_filters:
                result['SubFilters'].append(k.to_map() if k else None)
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Op') is not None:
            self.op = m.get('Op')
        self.sub_filters = []
        if m.get('SubFilters') is not None:
            for k in m.get('SubFilters'):
                temp_model = EventFilter()
                self.sub_filters.append(temp_model.from_map(k))
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class ConditionalRule(TeaModel):
    def __init__(
        self,
        filter: EventFilter = None,
        modify_time: str = None,
        name: str = None,
        operator: str = None,
        sample_rate: float = None,
    ):
        self.filter = filter
        self.modify_time = modify_time
        self.name = name
        self.operator = operator
        self.sample_rate = sample_rate

    def validate(self):
        if self.filter:
            self.filter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter is not None:
            result['Filter'] = self.filter.to_map()
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            temp_model = EventFilter()
            self.filter = temp_model.from_map(m['Filter'])
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        return self


class EventRule(TeaModel):
    def __init__(
        self,
        conditional: List[ConditionalRule] = None,
        enable: bool = None,
        event_id: str = None,
        modify_time: str = None,
        operator: str = None,
        sample_rate: float = None,
    ):
        self.conditional = conditional
        self.enable = enable
        self.event_id = event_id
        self.modify_time = modify_time
        self.operator = operator
        self.sample_rate = sample_rate

    def validate(self):
        if self.conditional:
            for k in self.conditional:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Conditional'] = []
        if self.conditional is not None:
            for k in self.conditional:
                result['Conditional'].append(k.to_map() if k else None)
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditional = []
        if m.get('Conditional') is not None:
            for k in m.get('Conditional'):
                temp_model = ConditionalRule()
                self.conditional.append(temp_model.from_map(k))
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        return self


class Filter(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        sub_filters: List['Filter'] = None,
        values: Any = None,
    ):
        self.key = key
        self.operator = operator
        self.sub_filters = sub_filters
        self.values = values

    def validate(self):
        if self.sub_filters:
            for k in self.sub_filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        result['SubFilters'] = []
        if self.sub_filters is not None:
            for k in self.sub_filters:
                result['SubFilters'].append(k.to_map() if k else None)
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        self.sub_filters = []
        if m.get('SubFilters') is not None:
            for k in m.get('SubFilters'):
                temp_model = Filter()
                self.sub_filters.append(temp_model.from_map(k))
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class FullSampleItem(TeaModel):
    def __init__(
        self,
        id: str = None,
        modify_time: str = None,
        operator: str = None,
    ):
        self.id = id
        self.modify_time = modify_time
        self.operator = operator

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.operator is not None:
            result['Operator'] = self.operator
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        return self


class SampleBase(TeaModel):
    def __init__(
        self,
        full_sample_device_ids: List[FullSampleItem] = None,
        full_sample_users: List[FullSampleItem] = None,
        sample_method: str = None,
        sample_rate: float = None,
    ):
        self.full_sample_device_ids = full_sample_device_ids
        self.full_sample_users = full_sample_users
        self.sample_method = sample_method
        self.sample_rate = sample_rate

    def validate(self):
        if self.full_sample_device_ids:
            for k in self.full_sample_device_ids:
                if k:
                    k.validate()
        if self.full_sample_users:
            for k in self.full_sample_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FullSampleDeviceIds'] = []
        if self.full_sample_device_ids is not None:
            for k in self.full_sample_device_ids:
                result['FullSampleDeviceIds'].append(k.to_map() if k else None)
        result['FullSampleUsers'] = []
        if self.full_sample_users is not None:
            for k in self.full_sample_users:
                result['FullSampleUsers'].append(k.to_map() if k else None)
        if self.sample_method is not None:
            result['SampleMethod'] = self.sample_method
        if self.sample_rate is not None:
            result['SampleRate'] = self.sample_rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.full_sample_device_ids = []
        if m.get('FullSampleDeviceIds') is not None:
            for k in m.get('FullSampleDeviceIds'):
                temp_model = FullSampleItem()
                self.full_sample_device_ids.append(temp_model.from_map(k))
        self.full_sample_users = []
        if m.get('FullSampleUsers') is not None:
            for k in m.get('FullSampleUsers'):
                temp_model = FullSampleItem()
                self.full_sample_users.append(temp_model.from_map(k))
        if m.get('SampleMethod') is not None:
            self.sample_method = m.get('SampleMethod')
        if m.get('SampleRate') is not None:
            self.sample_rate = m.get('SampleRate')
        return self


class GetErrorRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        biz_module: str = None,
        client_time: int = None,
        did: str = None,
        digest_hash: str = None,
        force: bool = None,
        os: str = None,
        uuid: str = None,
    ):
        # appKey
        # 
        # This parameter is required.
        self.app_key = app_key
        self.biz_module = biz_module
        # This parameter is required.
        self.client_time = client_time
        self.did = did
        self.digest_hash = digest_hash
        self.force = force
        self.os = os
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.biz_module is not None:
            result['BizModule'] = self.biz_module
        if self.client_time is not None:
            result['ClientTime'] = self.client_time
        if self.did is not None:
            result['Did'] = self.did
        if self.digest_hash is not None:
            result['DigestHash'] = self.digest_hash
        if self.force is not None:
            result['Force'] = self.force
        if self.os is not None:
            result['Os'] = self.os
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('BizModule') is not None:
            self.biz_module = m.get('BizModule')
        if m.get('ClientTime') is not None:
            self.client_time = m.get('ClientTime')
        if m.get('Did') is not None:
            self.did = m.get('Did')
        if m.get('DigestHash') is not None:
            self.digest_hash = m.get('DigestHash')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetErrorResponseBodyModel(TeaModel):
    def __init__(
        self,
        access: str = None,
        access_sub_type: str = None,
        additional_callback_info: str = None,
        additional_cross_platform_crash_info: str = None,
        additional_custom_info: str = None,
        android_vm: str = None,
        app_id: str = None,
        app_key: int = None,
        app_version: str = None,
        arg_hash: int = None,
        args: str = None,
        backtrace: str = None,
        banner: str = None,
        binary_uuids: str = None,
        brand: str = None,
        browser_name: str = None,
        browser_version: str = None,
        build: str = None,
        business_country: str = None,
        business_error_ext_data: str = None,
        business_log_type: str = None,
        carrier: str = None,
        channel: str = None,
        city: str = None,
        client_ip: str = None,
        client_time: int = None,
        col_no: str = None,
        country: str = None,
        cpu_model: str = None,
        crux_module: str = None,
        crux_stack: str = None,
        crux_stack_hash: int = None,
        crux_stack_trace: str = None,
        crux_stack_trace_hash: int = None,
        custom_exception_type: str = None,
        custom_info: str = None,
        data_directory: str = None,
        device_id: str = None,
        device_model: str = None,
        did: str = None,
        digest: str = None,
        digest_hash: str = None,
        dom_score: str = None,
        download_cache_directory: str = None,
        error_name: str = None,
        error_type: str = None,
        event_id: int = None,
        event_log: str = None,
        exception_arg_1: str = None,
        exception_arg_2: str = None,
        exception_arg_3: str = None,
        exception_code: str = None,
        exception_codes: str = None,
        exception_detail: str = None,
        exception_id: str = None,
        exception_msg: str = None,
        exception_subtype: str = None,
        exception_type: str = None,
        exception_version: str = None,
        export_status: str = None,
        external_storage_directory: str = None,
        feature_scene: str = None,
        file_name: str = None,
        file_path: str = None,
        filename: str = None,
        flutter_route: str = None,
        force_ground: int = None,
        fore_ground: int = None,
        h_5full_url: str = None,
        h_5short_url: str = None,
        has_open_multi_process_mode: int = None,
        has_sd_card: int = None,
        has_sg_security_config_key: int = None,
        imei: str = None,
        imsi: str = None,
        in_main_process: int = None,
        install_sd_card: int = None,
        is_back_trace: int = None,
        is_speed_version: int = None,
        isp: str = None,
        js_backtrace: str = None,
        language: str = None,
        launched_time: str = None,
        line_no: str = None,
        log_hash: int = None,
        main_log: str = None,
        memory_map: str = None,
        more_info_1: str = None,
        more_info_2: str = None,
        more_info_3: str = None,
        native_all_thread_dump: str = None,
        native_maps: str = None,
        need_re_cluster: int = None,
        opened_file_count: int = None,
        operations: str = None,
        origin_data: str = None,
        origin_uri: str = None,
        os: str = None,
        os_version: str = None,
        page: str = None,
        parent_process_name: str = None,
        pid: int = None,
        platform: str = None,
        process_name: str = None,
        province: str = None,
        reason: str = None,
        report_content: str = None,
        report_type: str = None,
        resolution: str = None,
        root_directory: str = None,
        runtime_ext_data: str = None,
        scene_value: str = None,
        sdk_type: str = None,
        sdk_version: str = None,
        seq: str = None,
        server_time: int = None,
        session_id: str = None,
        simple_report_content: str = None,
        so_lib_build: str = None,
        speed_flags: str = None,
        stack: str = None,
        status: str = None,
        structured_stack: str = None,
        summary: str = None,
        symbolic_file_type: str = None,
        sys_log: str = None,
        thread_name: str = None,
        threads: str = None,
        tid: int = None,
        track: str = None,
        triggered_time: str = None,
        upload_time: int = None,
        uri: str = None,
        user: str = None,
        user_id: str = None,
        user_nick: str = None,
        utdid: str = None,
        uuid: str = None,
        view: str = None,
        weex_full_url: str = None,
        weex_short_url: str = None,
        write_limit: int = None,
    ):
        self.access = access
        self.access_sub_type = access_sub_type
        self.additional_callback_info = additional_callback_info
        self.additional_cross_platform_crash_info = additional_cross_platform_crash_info
        self.additional_custom_info = additional_custom_info
        self.android_vm = android_vm
        self.app_id = app_id
        # appKey
        self.app_key = app_key
        self.app_version = app_version
        self.arg_hash = arg_hash
        self.args = args
        self.backtrace = backtrace
        # banner
        self.banner = banner
        self.binary_uuids = binary_uuids
        self.brand = brand
        self.browser_name = browser_name
        self.browser_version = browser_version
        self.build = build
        self.business_country = business_country
        self.business_error_ext_data = business_error_ext_data
        self.business_log_type = business_log_type
        # carrier
        self.carrier = carrier
        self.channel = channel
        self.city = city
        self.client_ip = client_ip
        self.client_time = client_time
        self.col_no = col_no
        self.country = country
        self.cpu_model = cpu_model
        self.crux_module = crux_module
        self.crux_stack = crux_stack
        self.crux_stack_hash = crux_stack_hash
        # CruxStackTrace
        self.crux_stack_trace = crux_stack_trace
        self.crux_stack_trace_hash = crux_stack_trace_hash
        self.custom_exception_type = custom_exception_type
        self.custom_info = custom_info
        self.data_directory = data_directory
        self.device_id = device_id
        self.device_model = device_model
        self.did = did
        self.digest = digest
        self.digest_hash = digest_hash
        self.dom_score = dom_score
        self.download_cache_directory = download_cache_directory
        self.error_name = error_name
        self.error_type = error_type
        self.event_id = event_id
        self.event_log = event_log
        self.exception_arg_1 = exception_arg_1
        self.exception_arg_2 = exception_arg_2
        self.exception_arg_3 = exception_arg_3
        self.exception_code = exception_code
        self.exception_codes = exception_codes
        self.exception_detail = exception_detail
        self.exception_id = exception_id
        self.exception_msg = exception_msg
        self.exception_subtype = exception_subtype
        self.exception_type = exception_type
        self.exception_version = exception_version
        self.export_status = export_status
        self.external_storage_directory = external_storage_directory
        self.feature_scene = feature_scene
        self.file_name = file_name
        self.file_path = file_path
        self.filename = filename
        self.flutter_route = flutter_route
        self.force_ground = force_ground
        self.fore_ground = fore_ground
        self.h_5full_url = h_5full_url
        self.h_5short_url = h_5short_url
        self.has_open_multi_process_mode = has_open_multi_process_mode
        self.has_sd_card = has_sd_card
        self.has_sg_security_config_key = has_sg_security_config_key
        # IMEI
        self.imei = imei
        # IMSI
        self.imsi = imsi
        self.in_main_process = in_main_process
        self.install_sd_card = install_sd_card
        self.is_back_trace = is_back_trace
        self.is_speed_version = is_speed_version
        # ISP
        self.isp = isp
        self.js_backtrace = js_backtrace
        self.language = language
        self.launched_time = launched_time
        self.line_no = line_no
        self.log_hash = log_hash
        self.main_log = main_log
        self.memory_map = memory_map
        self.more_info_1 = more_info_1
        self.more_info_2 = more_info_2
        self.more_info_3 = more_info_3
        self.native_all_thread_dump = native_all_thread_dump
        # Native map
        self.native_maps = native_maps
        self.need_re_cluster = need_re_cluster
        self.opened_file_count = opened_file_count
        self.operations = operations
        self.origin_data = origin_data
        self.origin_uri = origin_uri
        self.os = os
        self.os_version = os_version
        self.page = page
        self.parent_process_name = parent_process_name
        self.pid = pid
        self.platform = platform
        self.process_name = process_name
        self.province = province
        self.reason = reason
        self.report_content = report_content
        self.report_type = report_type
        self.resolution = resolution
        self.root_directory = root_directory
        self.runtime_ext_data = runtime_ext_data
        self.scene_value = scene_value
        self.sdk_type = sdk_type
        self.sdk_version = sdk_version
        self.seq = seq
        self.server_time = server_time
        self.session_id = session_id
        self.simple_report_content = simple_report_content
        self.so_lib_build = so_lib_build
        # SpeedFlags
        self.speed_flags = speed_flags
        self.stack = stack
        self.status = status
        self.structured_stack = structured_stack
        self.summary = summary
        self.symbolic_file_type = symbolic_file_type
        self.sys_log = sys_log
        self.thread_name = thread_name
        self.threads = threads
        self.tid = tid
        self.track = track
        self.triggered_time = triggered_time
        self.upload_time = upload_time
        # URI
        self.uri = uri
        self.user = user
        self.user_id = user_id
        self.user_nick = user_nick
        # utdid
        self.utdid = utdid
        # uuid
        self.uuid = uuid
        # view
        self.view = view
        self.weex_full_url = weex_full_url
        self.weex_short_url = weex_short_url
        self.write_limit = write_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access is not None:
            result['Access'] = self.access
        if self.access_sub_type is not None:
            result['AccessSubType'] = self.access_sub_type
        if self.additional_callback_info is not None:
            result['AdditionalCallbackInfo'] = self.additional_callback_info
        if self.additional_cross_platform_crash_info is not None:
            result['AdditionalCrossPlatformCrashInfo'] = self.additional_cross_platform_crash_info
        if self.additional_custom_info is not None:
            result['AdditionalCustomInfo'] = self.additional_custom_info
        if self.android_vm is not None:
            result['AndroidVm'] = self.android_vm
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.arg_hash is not None:
            result['ArgHash'] = self.arg_hash
        if self.args is not None:
            result['Args'] = self.args
        if self.backtrace is not None:
            result['Backtrace'] = self.backtrace
        if self.banner is not None:
            result['Banner'] = self.banner
        if self.binary_uuids is not None:
            result['BinaryUuids'] = self.binary_uuids
        if self.brand is not None:
            result['Brand'] = self.brand
        if self.browser_name is not None:
            result['BrowserName'] = self.browser_name
        if self.browser_version is not None:
            result['BrowserVersion'] = self.browser_version
        if self.build is not None:
            result['Build'] = self.build
        if self.business_country is not None:
            result['BusinessCountry'] = self.business_country
        if self.business_error_ext_data is not None:
            result['BusinessErrorExtData'] = self.business_error_ext_data
        if self.business_log_type is not None:
            result['BusinessLogType'] = self.business_log_type
        if self.carrier is not None:
            result['Carrier'] = self.carrier
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.city is not None:
            result['City'] = self.city
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_time is not None:
            result['ClientTime'] = self.client_time
        if self.col_no is not None:
            result['ColNo'] = self.col_no
        if self.country is not None:
            result['Country'] = self.country
        if self.cpu_model is not None:
            result['CpuModel'] = self.cpu_model
        if self.crux_module is not None:
            result['CruxModule'] = self.crux_module
        if self.crux_stack is not None:
            result['CruxStack'] = self.crux_stack
        if self.crux_stack_hash is not None:
            result['CruxStackHash'] = self.crux_stack_hash
        if self.crux_stack_trace is not None:
            result['CruxStackTrace'] = self.crux_stack_trace
        if self.crux_stack_trace_hash is not None:
            result['CruxStackTraceHash'] = self.crux_stack_trace_hash
        if self.custom_exception_type is not None:
            result['CustomExceptionType'] = self.custom_exception_type
        if self.custom_info is not None:
            result['CustomInfo'] = self.custom_info
        if self.data_directory is not None:
            result['DataDirectory'] = self.data_directory
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_model is not None:
            result['DeviceModel'] = self.device_model
        if self.did is not None:
            result['Did'] = self.did
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.digest_hash is not None:
            result['DigestHash'] = self.digest_hash
        if self.dom_score is not None:
            result['DomScore'] = self.dom_score
        if self.download_cache_directory is not None:
            result['DownloadCacheDirectory'] = self.download_cache_directory
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.error_type is not None:
            result['ErrorType'] = self.error_type
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_log is not None:
            result['EventLog'] = self.event_log
        if self.exception_arg_1 is not None:
            result['ExceptionArg1'] = self.exception_arg_1
        if self.exception_arg_2 is not None:
            result['ExceptionArg2'] = self.exception_arg_2
        if self.exception_arg_3 is not None:
            result['ExceptionArg3'] = self.exception_arg_3
        if self.exception_code is not None:
            result['ExceptionCode'] = self.exception_code
        if self.exception_codes is not None:
            result['ExceptionCodes'] = self.exception_codes
        if self.exception_detail is not None:
            result['ExceptionDetail'] = self.exception_detail
        if self.exception_id is not None:
            result['ExceptionId'] = self.exception_id
        if self.exception_msg is not None:
            result['ExceptionMsg'] = self.exception_msg
        if self.exception_subtype is not None:
            result['ExceptionSubtype'] = self.exception_subtype
        if self.exception_type is not None:
            result['ExceptionType'] = self.exception_type
        if self.exception_version is not None:
            result['ExceptionVersion'] = self.exception_version
        if self.export_status is not None:
            result['ExportStatus'] = self.export_status
        if self.external_storage_directory is not None:
            result['ExternalStorageDirectory'] = self.external_storage_directory
        if self.feature_scene is not None:
            result['FeatureScene'] = self.feature_scene
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.flutter_route is not None:
            result['FlutterRoute'] = self.flutter_route
        if self.force_ground is not None:
            result['ForceGround'] = self.force_ground
        if self.fore_ground is not None:
            result['ForeGround'] = self.fore_ground
        if self.h_5full_url is not None:
            result['H5FullUrl'] = self.h_5full_url
        if self.h_5short_url is not None:
            result['H5ShortUrl'] = self.h_5short_url
        if self.has_open_multi_process_mode is not None:
            result['HasOpenMultiProcessMode'] = self.has_open_multi_process_mode
        if self.has_sd_card is not None:
            result['HasSdCard'] = self.has_sd_card
        if self.has_sg_security_config_key is not None:
            result['HasSgSecurityConfigKey'] = self.has_sg_security_config_key
        if self.imei is not None:
            result['Imei'] = self.imei
        if self.imsi is not None:
            result['Imsi'] = self.imsi
        if self.in_main_process is not None:
            result['InMainProcess'] = self.in_main_process
        if self.install_sd_card is not None:
            result['InstallSdCard'] = self.install_sd_card
        if self.is_back_trace is not None:
            result['IsBackTrace'] = self.is_back_trace
        if self.is_speed_version is not None:
            result['IsSpeedVersion'] = self.is_speed_version
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.js_backtrace is not None:
            result['JsBacktrace'] = self.js_backtrace
        if self.language is not None:
            result['Language'] = self.language
        if self.launched_time is not None:
            result['LaunchedTime'] = self.launched_time
        if self.line_no is not None:
            result['LineNo'] = self.line_no
        if self.log_hash is not None:
            result['LogHash'] = self.log_hash
        if self.main_log is not None:
            result['MainLog'] = self.main_log
        if self.memory_map is not None:
            result['MemoryMap'] = self.memory_map
        if self.more_info_1 is not None:
            result['MoreInfo1'] = self.more_info_1
        if self.more_info_2 is not None:
            result['MoreInfo2'] = self.more_info_2
        if self.more_info_3 is not None:
            result['MoreInfo3'] = self.more_info_3
        if self.native_all_thread_dump is not None:
            result['NativeAllThreadDump'] = self.native_all_thread_dump
        if self.native_maps is not None:
            result['NativeMaps'] = self.native_maps
        if self.need_re_cluster is not None:
            result['NeedReCluster'] = self.need_re_cluster
        if self.opened_file_count is not None:
            result['OpenedFileCount'] = self.opened_file_count
        if self.operations is not None:
            result['Operations'] = self.operations
        if self.origin_data is not None:
            result['OriginData'] = self.origin_data
        if self.origin_uri is not None:
            result['OriginUri'] = self.origin_uri
        if self.os is not None:
            result['Os'] = self.os
        if self.os_version is not None:
            result['OsVersion'] = self.os_version
        if self.page is not None:
            result['Page'] = self.page
        if self.parent_process_name is not None:
            result['ParentProcessName'] = self.parent_process_name
        if self.pid is not None:
            result['Pid'] = self.pid
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.process_name is not None:
            result['ProcessName'] = self.process_name
        if self.province is not None:
            result['Province'] = self.province
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.report_content is not None:
            result['ReportContent'] = self.report_content
        if self.report_type is not None:
            result['ReportType'] = self.report_type
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.root_directory is not None:
            result['RootDirectory'] = self.root_directory
        if self.runtime_ext_data is not None:
            result['RuntimeExtData'] = self.runtime_ext_data
        if self.scene_value is not None:
            result['SceneValue'] = self.scene_value
        if self.sdk_type is not None:
            result['SdkType'] = self.sdk_type
        if self.sdk_version is not None:
            result['SdkVersion'] = self.sdk_version
        if self.seq is not None:
            result['Seq'] = self.seq
        if self.server_time is not None:
            result['ServerTime'] = self.server_time
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.simple_report_content is not None:
            result['SimpleReportContent'] = self.simple_report_content
        if self.so_lib_build is not None:
            result['SoLibBuild'] = self.so_lib_build
        if self.speed_flags is not None:
            result['SpeedFlags'] = self.speed_flags
        if self.stack is not None:
            result['Stack'] = self.stack
        if self.status is not None:
            result['Status'] = self.status
        if self.structured_stack is not None:
            result['StructuredStack'] = self.structured_stack
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.symbolic_file_type is not None:
            result['SymbolicFileType'] = self.symbolic_file_type
        if self.sys_log is not None:
            result['SysLog'] = self.sys_log
        if self.thread_name is not None:
            result['ThreadName'] = self.thread_name
        if self.threads is not None:
            result['Threads'] = self.threads
        if self.tid is not None:
            result['Tid'] = self.tid
        if self.track is not None:
            result['Track'] = self.track
        if self.triggered_time is not None:
            result['TriggeredTime'] = self.triggered_time
        if self.upload_time is not None:
            result['UploadTime'] = self.upload_time
        if self.uri is not None:
            result['Uri'] = self.uri
        if self.user is not None:
            result['User'] = self.user
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_nick is not None:
            result['UserNick'] = self.user_nick
        if self.utdid is not None:
            result['Utdid'] = self.utdid
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.view is not None:
            result['View'] = self.view
        if self.weex_full_url is not None:
            result['WeexFullUrl'] = self.weex_full_url
        if self.weex_short_url is not None:
            result['WeexShortUrl'] = self.weex_short_url
        if self.write_limit is not None:
            result['WriteLimit'] = self.write_limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Access') is not None:
            self.access = m.get('Access')
        if m.get('AccessSubType') is not None:
            self.access_sub_type = m.get('AccessSubType')
        if m.get('AdditionalCallbackInfo') is not None:
            self.additional_callback_info = m.get('AdditionalCallbackInfo')
        if m.get('AdditionalCrossPlatformCrashInfo') is not None:
            self.additional_cross_platform_crash_info = m.get('AdditionalCrossPlatformCrashInfo')
        if m.get('AdditionalCustomInfo') is not None:
            self.additional_custom_info = m.get('AdditionalCustomInfo')
        if m.get('AndroidVm') is not None:
            self.android_vm = m.get('AndroidVm')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('ArgHash') is not None:
            self.arg_hash = m.get('ArgHash')
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('Backtrace') is not None:
            self.backtrace = m.get('Backtrace')
        if m.get('Banner') is not None:
            self.banner = m.get('Banner')
        if m.get('BinaryUuids') is not None:
            self.binary_uuids = m.get('BinaryUuids')
        if m.get('Brand') is not None:
            self.brand = m.get('Brand')
        if m.get('BrowserName') is not None:
            self.browser_name = m.get('BrowserName')
        if m.get('BrowserVersion') is not None:
            self.browser_version = m.get('BrowserVersion')
        if m.get('Build') is not None:
            self.build = m.get('Build')
        if m.get('BusinessCountry') is not None:
            self.business_country = m.get('BusinessCountry')
        if m.get('BusinessErrorExtData') is not None:
            self.business_error_ext_data = m.get('BusinessErrorExtData')
        if m.get('BusinessLogType') is not None:
            self.business_log_type = m.get('BusinessLogType')
        if m.get('Carrier') is not None:
            self.carrier = m.get('Carrier')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientTime') is not None:
            self.client_time = m.get('ClientTime')
        if m.get('ColNo') is not None:
            self.col_no = m.get('ColNo')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('CpuModel') is not None:
            self.cpu_model = m.get('CpuModel')
        if m.get('CruxModule') is not None:
            self.crux_module = m.get('CruxModule')
        if m.get('CruxStack') is not None:
            self.crux_stack = m.get('CruxStack')
        if m.get('CruxStackHash') is not None:
            self.crux_stack_hash = m.get('CruxStackHash')
        if m.get('CruxStackTrace') is not None:
            self.crux_stack_trace = m.get('CruxStackTrace')
        if m.get('CruxStackTraceHash') is not None:
            self.crux_stack_trace_hash = m.get('CruxStackTraceHash')
        if m.get('CustomExceptionType') is not None:
            self.custom_exception_type = m.get('CustomExceptionType')
        if m.get('CustomInfo') is not None:
            self.custom_info = m.get('CustomInfo')
        if m.get('DataDirectory') is not None:
            self.data_directory = m.get('DataDirectory')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')
        if m.get('Did') is not None:
            self.did = m.get('Did')
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('DigestHash') is not None:
            self.digest_hash = m.get('DigestHash')
        if m.get('DomScore') is not None:
            self.dom_score = m.get('DomScore')
        if m.get('DownloadCacheDirectory') is not None:
            self.download_cache_directory = m.get('DownloadCacheDirectory')
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('ErrorType') is not None:
            self.error_type = m.get('ErrorType')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventLog') is not None:
            self.event_log = m.get('EventLog')
        if m.get('ExceptionArg1') is not None:
            self.exception_arg_1 = m.get('ExceptionArg1')
        if m.get('ExceptionArg2') is not None:
            self.exception_arg_2 = m.get('ExceptionArg2')
        if m.get('ExceptionArg3') is not None:
            self.exception_arg_3 = m.get('ExceptionArg3')
        if m.get('ExceptionCode') is not None:
            self.exception_code = m.get('ExceptionCode')
        if m.get('ExceptionCodes') is not None:
            self.exception_codes = m.get('ExceptionCodes')
        if m.get('ExceptionDetail') is not None:
            self.exception_detail = m.get('ExceptionDetail')
        if m.get('ExceptionId') is not None:
            self.exception_id = m.get('ExceptionId')
        if m.get('ExceptionMsg') is not None:
            self.exception_msg = m.get('ExceptionMsg')
        if m.get('ExceptionSubtype') is not None:
            self.exception_subtype = m.get('ExceptionSubtype')
        if m.get('ExceptionType') is not None:
            self.exception_type = m.get('ExceptionType')
        if m.get('ExceptionVersion') is not None:
            self.exception_version = m.get('ExceptionVersion')
        if m.get('ExportStatus') is not None:
            self.export_status = m.get('ExportStatus')
        if m.get('ExternalStorageDirectory') is not None:
            self.external_storage_directory = m.get('ExternalStorageDirectory')
        if m.get('FeatureScene') is not None:
            self.feature_scene = m.get('FeatureScene')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('FlutterRoute') is not None:
            self.flutter_route = m.get('FlutterRoute')
        if m.get('ForceGround') is not None:
            self.force_ground = m.get('ForceGround')
        if m.get('ForeGround') is not None:
            self.fore_ground = m.get('ForeGround')
        if m.get('H5FullUrl') is not None:
            self.h_5full_url = m.get('H5FullUrl')
        if m.get('H5ShortUrl') is not None:
            self.h_5short_url = m.get('H5ShortUrl')
        if m.get('HasOpenMultiProcessMode') is not None:
            self.has_open_multi_process_mode = m.get('HasOpenMultiProcessMode')
        if m.get('HasSdCard') is not None:
            self.has_sd_card = m.get('HasSdCard')
        if m.get('HasSgSecurityConfigKey') is not None:
            self.has_sg_security_config_key = m.get('HasSgSecurityConfigKey')
        if m.get('Imei') is not None:
            self.imei = m.get('Imei')
        if m.get('Imsi') is not None:
            self.imsi = m.get('Imsi')
        if m.get('InMainProcess') is not None:
            self.in_main_process = m.get('InMainProcess')
        if m.get('InstallSdCard') is not None:
            self.install_sd_card = m.get('InstallSdCard')
        if m.get('IsBackTrace') is not None:
            self.is_back_trace = m.get('IsBackTrace')
        if m.get('IsSpeedVersion') is not None:
            self.is_speed_version = m.get('IsSpeedVersion')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('JsBacktrace') is not None:
            self.js_backtrace = m.get('JsBacktrace')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LaunchedTime') is not None:
            self.launched_time = m.get('LaunchedTime')
        if m.get('LineNo') is not None:
            self.line_no = m.get('LineNo')
        if m.get('LogHash') is not None:
            self.log_hash = m.get('LogHash')
        if m.get('MainLog') is not None:
            self.main_log = m.get('MainLog')
        if m.get('MemoryMap') is not None:
            self.memory_map = m.get('MemoryMap')
        if m.get('MoreInfo1') is not None:
            self.more_info_1 = m.get('MoreInfo1')
        if m.get('MoreInfo2') is not None:
            self.more_info_2 = m.get('MoreInfo2')
        if m.get('MoreInfo3') is not None:
            self.more_info_3 = m.get('MoreInfo3')
        if m.get('NativeAllThreadDump') is not None:
            self.native_all_thread_dump = m.get('NativeAllThreadDump')
        if m.get('NativeMaps') is not None:
            self.native_maps = m.get('NativeMaps')
        if m.get('NeedReCluster') is not None:
            self.need_re_cluster = m.get('NeedReCluster')
        if m.get('OpenedFileCount') is not None:
            self.opened_file_count = m.get('OpenedFileCount')
        if m.get('Operations') is not None:
            self.operations = m.get('Operations')
        if m.get('OriginData') is not None:
            self.origin_data = m.get('OriginData')
        if m.get('OriginUri') is not None:
            self.origin_uri = m.get('OriginUri')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('OsVersion') is not None:
            self.os_version = m.get('OsVersion')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('ParentProcessName') is not None:
            self.parent_process_name = m.get('ParentProcessName')
        if m.get('Pid') is not None:
            self.pid = m.get('Pid')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('ReportContent') is not None:
            self.report_content = m.get('ReportContent')
        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('RootDirectory') is not None:
            self.root_directory = m.get('RootDirectory')
        if m.get('RuntimeExtData') is not None:
            self.runtime_ext_data = m.get('RuntimeExtData')
        if m.get('SceneValue') is not None:
            self.scene_value = m.get('SceneValue')
        if m.get('SdkType') is not None:
            self.sdk_type = m.get('SdkType')
        if m.get('SdkVersion') is not None:
            self.sdk_version = m.get('SdkVersion')
        if m.get('Seq') is not None:
            self.seq = m.get('Seq')
        if m.get('ServerTime') is not None:
            self.server_time = m.get('ServerTime')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SimpleReportContent') is not None:
            self.simple_report_content = m.get('SimpleReportContent')
        if m.get('SoLibBuild') is not None:
            self.so_lib_build = m.get('SoLibBuild')
        if m.get('SpeedFlags') is not None:
            self.speed_flags = m.get('SpeedFlags')
        if m.get('Stack') is not None:
            self.stack = m.get('Stack')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StructuredStack') is not None:
            self.structured_stack = m.get('StructuredStack')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('SymbolicFileType') is not None:
            self.symbolic_file_type = m.get('SymbolicFileType')
        if m.get('SysLog') is not None:
            self.sys_log = m.get('SysLog')
        if m.get('ThreadName') is not None:
            self.thread_name = m.get('ThreadName')
        if m.get('Threads') is not None:
            self.threads = m.get('Threads')
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')
        if m.get('Track') is not None:
            self.track = m.get('Track')
        if m.get('TriggeredTime') is not None:
            self.triggered_time = m.get('TriggeredTime')
        if m.get('UploadTime') is not None:
            self.upload_time = m.get('UploadTime')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        if m.get('User') is not None:
            self.user = m.get('User')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')
        if m.get('Utdid') is not None:
            self.utdid = m.get('Utdid')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('View') is not None:
            self.view = m.get('View')
        if m.get('WeexFullUrl') is not None:
            self.weex_full_url = m.get('WeexFullUrl')
        if m.get('WeexShortUrl') is not None:
            self.weex_short_url = m.get('WeexShortUrl')
        if m.get('WriteLimit') is not None:
            self.write_limit = m.get('WriteLimit')
        return self


class GetErrorResponseBody(TeaModel):
    def __init__(
        self,
        args: Dict[str, Any] = None,
        error_code: int = None,
        message: str = None,
        model: GetErrorResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.args = args
        self.error_code = error_code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['Args'] = self.args
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = GetErrorResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetErrorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetErrorResponseBody = None,
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
            temp_model = GetErrorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetErrorsRequestFilter(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        sub_filters: List[str] = None,
        values: List[Any] = None,
    ):
        self.key = key
        self.operator = operator
        self.sub_filters = sub_filters
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.sub_filters is not None:
            result['SubFilters'] = self.sub_filters
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('SubFilters') is not None:
            self.sub_filters = m.get('SubFilters')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class GetErrorsRequestTimeRange(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
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


class GetErrorsRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        biz_module: str = None,
        digest_hash: str = None,
        filter: GetErrorsRequestFilter = None,
        os: str = None,
        page_index: int = None,
        page_size: int = None,
        time_range: GetErrorsRequestTimeRange = None,
        utdid: str = None,
    ):
        # appKey
        # 
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.biz_module = biz_module
        self.digest_hash = digest_hash
        self.filter = filter
        self.os = os
        # This parameter is required.
        self.page_index = page_index
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.time_range = time_range
        # utdid
        self.utdid = utdid

    def validate(self):
        if self.filter:
            self.filter.validate()
        if self.time_range:
            self.time_range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.biz_module is not None:
            result['BizModule'] = self.biz_module
        if self.digest_hash is not None:
            result['DigestHash'] = self.digest_hash
        if self.filter is not None:
            result['Filter'] = self.filter.to_map()
        if self.os is not None:
            result['Os'] = self.os
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.time_range is not None:
            result['TimeRange'] = self.time_range.to_map()
        if self.utdid is not None:
            result['Utdid'] = self.utdid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('BizModule') is not None:
            self.biz_module = m.get('BizModule')
        if m.get('DigestHash') is not None:
            self.digest_hash = m.get('DigestHash')
        if m.get('Filter') is not None:
            temp_model = GetErrorsRequestFilter()
            self.filter = temp_model.from_map(m['Filter'])
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TimeRange') is not None:
            temp_model = GetErrorsRequestTimeRange()
            self.time_range = temp_model.from_map(m['TimeRange'])
        if m.get('Utdid') is not None:
            self.utdid = m.get('Utdid')
        return self


class GetErrorsShrinkRequestTimeRange(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
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


class GetErrorsShrinkRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        biz_module: str = None,
        digest_hash: str = None,
        filter_shrink: str = None,
        os: str = None,
        page_index: int = None,
        page_size: int = None,
        time_range: GetErrorsShrinkRequestTimeRange = None,
        utdid: str = None,
    ):
        # appKey
        # 
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.biz_module = biz_module
        self.digest_hash = digest_hash
        self.filter_shrink = filter_shrink
        self.os = os
        # This parameter is required.
        self.page_index = page_index
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.time_range = time_range
        # utdid
        self.utdid = utdid

    def validate(self):
        if self.time_range:
            self.time_range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.biz_module is not None:
            result['BizModule'] = self.biz_module
        if self.digest_hash is not None:
            result['DigestHash'] = self.digest_hash
        if self.filter_shrink is not None:
            result['Filter'] = self.filter_shrink
        if self.os is not None:
            result['Os'] = self.os
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.time_range is not None:
            result['TimeRange'] = self.time_range.to_map()
        if self.utdid is not None:
            result['Utdid'] = self.utdid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('BizModule') is not None:
            self.biz_module = m.get('BizModule')
        if m.get('DigestHash') is not None:
            self.digest_hash = m.get('DigestHash')
        if m.get('Filter') is not None:
            self.filter_shrink = m.get('Filter')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TimeRange') is not None:
            temp_model = GetErrorsShrinkRequestTimeRange()
            self.time_range = temp_model.from_map(m['TimeRange'])
        if m.get('Utdid') is not None:
            self.utdid = m.get('Utdid')
        return self


class GetErrorsResponseBodyModelItems(TeaModel):
    def __init__(
        self,
        client_time: int = None,
        did: str = None,
        digest_hash: str = None,
        utdid: str = None,
        uuid: str = None,
    ):
        self.client_time = client_time
        self.did = did
        self.digest_hash = digest_hash
        # Utdid
        self.utdid = utdid
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_time is not None:
            result['ClientTime'] = self.client_time
        if self.did is not None:
            result['Did'] = self.did
        if self.digest_hash is not None:
            result['DigestHash'] = self.digest_hash
        if self.utdid is not None:
            result['Utdid'] = self.utdid
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientTime') is not None:
            self.client_time = m.get('ClientTime')
        if m.get('Did') is not None:
            self.did = m.get('Did')
        if m.get('DigestHash') is not None:
            self.digest_hash = m.get('DigestHash')
        if m.get('Utdid') is not None:
            self.utdid = m.get('Utdid')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetErrorsResponseBodyModel(TeaModel):
    def __init__(
        self,
        items: List[GetErrorsResponseBodyModelItems] = None,
        page_num: int = None,
        page_size: int = None,
        pages: int = None,
        total: int = None,
    ):
        self.items = items
        self.page_num = page_num
        self.page_size = page_size
        self.pages = pages
        self.total = total

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = GetErrorsResponseBodyModelItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetErrorsResponseBody(TeaModel):
    def __init__(
        self,
        args: Dict[str, Any] = None,
        error_code: int = None,
        message: str = None,
        model: GetErrorsResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Args
        self.args = args
        self.error_code = error_code
        self.message = message
        self.model = model
        # RequestId
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['Args'] = self.args
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = GetErrorsResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetErrorsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetErrorsResponseBody = None,
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
            temp_model = GetErrorsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIssueRequestFilter(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        sub_filters: List[str] = None,
        values: List[Any] = None,
    ):
        self.key = key
        self.operator = operator
        self.sub_filters = sub_filters
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.sub_filters is not None:
            result['SubFilters'] = self.sub_filters
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('SubFilters') is not None:
            self.sub_filters = m.get('SubFilters')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class GetIssueRequestTimeRange(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        granularity: int = None,
        granularity_unit: str = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.granularity = granularity
        self.granularity_unit = granularity_unit
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
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.granularity_unit is not None:
            result['GranularityUnit'] = self.granularity_unit
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('GranularityUnit') is not None:
            self.granularity_unit = m.get('GranularityUnit')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetIssueRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        biz_module: str = None,
        digest_hash: str = None,
        filter: GetIssueRequestFilter = None,
        os: str = None,
        time_range: GetIssueRequestTimeRange = None,
    ):
        # AppKey
        # 
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.biz_module = biz_module
        self.digest_hash = digest_hash
        self.filter = filter
        # This parameter is required.
        self.os = os
        # This parameter is required.
        self.time_range = time_range

    def validate(self):
        if self.filter:
            self.filter.validate()
        if self.time_range:
            self.time_range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.biz_module is not None:
            result['BizModule'] = self.biz_module
        if self.digest_hash is not None:
            result['DigestHash'] = self.digest_hash
        if self.filter is not None:
            result['Filter'] = self.filter.to_map()
        if self.os is not None:
            result['Os'] = self.os
        if self.time_range is not None:
            result['TimeRange'] = self.time_range.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('BizModule') is not None:
            self.biz_module = m.get('BizModule')
        if m.get('DigestHash') is not None:
            self.digest_hash = m.get('DigestHash')
        if m.get('Filter') is not None:
            temp_model = GetIssueRequestFilter()
            self.filter = temp_model.from_map(m['Filter'])
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('TimeRange') is not None:
            temp_model = GetIssueRequestTimeRange()
            self.time_range = temp_model.from_map(m['TimeRange'])
        return self


class GetIssueShrinkRequestTimeRange(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        granularity: int = None,
        granularity_unit: str = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.granularity = granularity
        self.granularity_unit = granularity_unit
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
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.granularity_unit is not None:
            result['GranularityUnit'] = self.granularity_unit
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('GranularityUnit') is not None:
            self.granularity_unit = m.get('GranularityUnit')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetIssueShrinkRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        biz_module: str = None,
        digest_hash: str = None,
        filter_shrink: str = None,
        os: str = None,
        time_range: GetIssueShrinkRequestTimeRange = None,
    ):
        # AppKey
        # 
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.biz_module = biz_module
        self.digest_hash = digest_hash
        self.filter_shrink = filter_shrink
        # This parameter is required.
        self.os = os
        # This parameter is required.
        self.time_range = time_range

    def validate(self):
        if self.time_range:
            self.time_range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.biz_module is not None:
            result['BizModule'] = self.biz_module
        if self.digest_hash is not None:
            result['DigestHash'] = self.digest_hash
        if self.filter_shrink is not None:
            result['Filter'] = self.filter_shrink
        if self.os is not None:
            result['Os'] = self.os
        if self.time_range is not None:
            result['TimeRange'] = self.time_range.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('BizModule') is not None:
            self.biz_module = m.get('BizModule')
        if m.get('DigestHash') is not None:
            self.digest_hash = m.get('DigestHash')
        if m.get('Filter') is not None:
            self.filter_shrink = m.get('Filter')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('TimeRange') is not None:
            temp_model = GetIssueShrinkRequestTimeRange()
            self.time_range = temp_model.from_map(m['TimeRange'])
        return self


class GetIssueResponseBodyModel(TeaModel):
    def __init__(
        self,
        affected_versions: List[str] = None,
        alloc_size_max: int = None,
        alloc_size_pct_50: int = None,
        alloc_size_pct_70: int = None,
        alloc_size_pct_90: int = None,
        crux_stack: str = None,
        digest_hash: str = None,
        error_column: int = None,
        error_count: int = None,
        error_count_growth_rate: float = None,
        error_device_count: int = None,
        error_device_count_growth_rate: float = None,
        error_device_rate: float = None,
        error_device_rate_growth_rate: float = None,
        error_file_name: str = None,
        error_line: str = None,
        error_name: str = None,
        error_rate: float = None,
        error_rate_growth_rate: float = None,
        error_type: str = None,
        event_time: int = None,
        first_version: str = None,
        gmt_create: int = None,
        gmt_latest: int = None,
        key_line: int = None,
        name: str = None,
        stack: str = None,
        status: int = None,
        summary: str = None,
        symbolic_status: bool = None,
        tags: List[str] = None,
    ):
        self.affected_versions = affected_versions
        self.alloc_size_max = alloc_size_max
        self.alloc_size_pct_50 = alloc_size_pct_50
        self.alloc_size_pct_70 = alloc_size_pct_70
        self.alloc_size_pct_90 = alloc_size_pct_90
        self.crux_stack = crux_stack
        self.digest_hash = digest_hash
        self.error_column = error_column
        self.error_count = error_count
        self.error_count_growth_rate = error_count_growth_rate
        self.error_device_count = error_device_count
        self.error_device_count_growth_rate = error_device_count_growth_rate
        self.error_device_rate = error_device_rate
        self.error_device_rate_growth_rate = error_device_rate_growth_rate
        self.error_file_name = error_file_name
        self.error_line = error_line
        self.error_name = error_name
        self.error_rate = error_rate
        self.error_rate_growth_rate = error_rate_growth_rate
        self.error_type = error_type
        self.event_time = event_time
        self.first_version = first_version
        self.gmt_create = gmt_create
        self.gmt_latest = gmt_latest
        self.key_line = key_line
        self.name = name
        self.stack = stack
        self.status = status
        self.summary = summary
        self.symbolic_status = symbolic_status
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affected_versions is not None:
            result['AffectedVersions'] = self.affected_versions
        if self.alloc_size_max is not None:
            result['AllocSizeMax'] = self.alloc_size_max
        if self.alloc_size_pct_50 is not None:
            result['AllocSizePct50'] = self.alloc_size_pct_50
        if self.alloc_size_pct_70 is not None:
            result['AllocSizePct70'] = self.alloc_size_pct_70
        if self.alloc_size_pct_90 is not None:
            result['AllocSizePct90'] = self.alloc_size_pct_90
        if self.crux_stack is not None:
            result['CruxStack'] = self.crux_stack
        if self.digest_hash is not None:
            result['DigestHash'] = self.digest_hash
        if self.error_column is not None:
            result['ErrorColumn'] = self.error_column
        if self.error_count is not None:
            result['ErrorCount'] = self.error_count
        if self.error_count_growth_rate is not None:
            result['ErrorCountGrowthRate'] = self.error_count_growth_rate
        if self.error_device_count is not None:
            result['ErrorDeviceCount'] = self.error_device_count
        if self.error_device_count_growth_rate is not None:
            result['ErrorDeviceCountGrowthRate'] = self.error_device_count_growth_rate
        if self.error_device_rate is not None:
            result['ErrorDeviceRate'] = self.error_device_rate
        if self.error_device_rate_growth_rate is not None:
            result['ErrorDeviceRateGrowthRate'] = self.error_device_rate_growth_rate
        if self.error_file_name is not None:
            result['ErrorFileName'] = self.error_file_name
        if self.error_line is not None:
            result['ErrorLine'] = self.error_line
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.error_rate is not None:
            result['ErrorRate'] = self.error_rate
        if self.error_rate_growth_rate is not None:
            result['ErrorRateGrowthRate'] = self.error_rate_growth_rate
        if self.error_type is not None:
            result['ErrorType'] = self.error_type
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.first_version is not None:
            result['FirstVersion'] = self.first_version
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_latest is not None:
            result['GmtLatest'] = self.gmt_latest
        if self.key_line is not None:
            result['KeyLine'] = self.key_line
        if self.name is not None:
            result['Name'] = self.name
        if self.stack is not None:
            result['Stack'] = self.stack
        if self.status is not None:
            result['Status'] = self.status
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.symbolic_status is not None:
            result['SymbolicStatus'] = self.symbolic_status
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectedVersions') is not None:
            self.affected_versions = m.get('AffectedVersions')
        if m.get('AllocSizeMax') is not None:
            self.alloc_size_max = m.get('AllocSizeMax')
        if m.get('AllocSizePct50') is not None:
            self.alloc_size_pct_50 = m.get('AllocSizePct50')
        if m.get('AllocSizePct70') is not None:
            self.alloc_size_pct_70 = m.get('AllocSizePct70')
        if m.get('AllocSizePct90') is not None:
            self.alloc_size_pct_90 = m.get('AllocSizePct90')
        if m.get('CruxStack') is not None:
            self.crux_stack = m.get('CruxStack')
        if m.get('DigestHash') is not None:
            self.digest_hash = m.get('DigestHash')
        if m.get('ErrorColumn') is not None:
            self.error_column = m.get('ErrorColumn')
        if m.get('ErrorCount') is not None:
            self.error_count = m.get('ErrorCount')
        if m.get('ErrorCountGrowthRate') is not None:
            self.error_count_growth_rate = m.get('ErrorCountGrowthRate')
        if m.get('ErrorDeviceCount') is not None:
            self.error_device_count = m.get('ErrorDeviceCount')
        if m.get('ErrorDeviceCountGrowthRate') is not None:
            self.error_device_count_growth_rate = m.get('ErrorDeviceCountGrowthRate')
        if m.get('ErrorDeviceRate') is not None:
            self.error_device_rate = m.get('ErrorDeviceRate')
        if m.get('ErrorDeviceRateGrowthRate') is not None:
            self.error_device_rate_growth_rate = m.get('ErrorDeviceRateGrowthRate')
        if m.get('ErrorFileName') is not None:
            self.error_file_name = m.get('ErrorFileName')
        if m.get('ErrorLine') is not None:
            self.error_line = m.get('ErrorLine')
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('ErrorRate') is not None:
            self.error_rate = m.get('ErrorRate')
        if m.get('ErrorRateGrowthRate') is not None:
            self.error_rate_growth_rate = m.get('ErrorRateGrowthRate')
        if m.get('ErrorType') is not None:
            self.error_type = m.get('ErrorType')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('FirstVersion') is not None:
            self.first_version = m.get('FirstVersion')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtLatest') is not None:
            self.gmt_latest = m.get('GmtLatest')
        if m.get('KeyLine') is not None:
            self.key_line = m.get('KeyLine')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Stack') is not None:
            self.stack = m.get('Stack')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('SymbolicStatus') is not None:
            self.symbolic_status = m.get('SymbolicStatus')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class GetIssueResponseBody(TeaModel):
    def __init__(
        self,
        args: Dict[str, Any] = None,
        error_code: int = None,
        message: str = None,
        model: GetIssueResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Args
        self.args = args
        self.error_code = error_code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['Args'] = self.args
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = GetIssueResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetIssueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetIssueResponseBody = None,
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
            temp_model = GetIssueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIssuesRequestFilter(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        sub_filters: List[str] = None,
        values: List[Any] = None,
    ):
        self.key = key
        self.operator = operator
        self.sub_filters = sub_filters
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.sub_filters is not None:
            result['SubFilters'] = self.sub_filters
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('SubFilters') is not None:
            self.sub_filters = m.get('SubFilters')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class GetIssuesRequestTimeRange(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        granularity: int = None,
        granularity_unit: str = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.granularity = granularity
        self.granularity_unit = granularity_unit
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
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.granularity_unit is not None:
            result['GranularityUnit'] = self.granularity_unit
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('GranularityUnit') is not None:
            self.granularity_unit = m.get('GranularityUnit')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetIssuesRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        biz_module: str = None,
        filter: GetIssuesRequestFilter = None,
        name: str = None,
        order_by: str = None,
        order_type: str = None,
        os: str = None,
        page_index: int = None,
        page_size: int = None,
        status: int = None,
        time_range: GetIssuesRequestTimeRange = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.biz_module = biz_module
        self.filter = filter
        self.name = name
        self.order_by = order_by
        self.order_type = order_type
        self.os = os
        self.page_index = page_index
        self.page_size = page_size
        self.status = status
        # This parameter is required.
        self.time_range = time_range

    def validate(self):
        if self.filter:
            self.filter.validate()
        if self.time_range:
            self.time_range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.biz_module is not None:
            result['BizModule'] = self.biz_module
        if self.filter is not None:
            result['Filter'] = self.filter.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.os is not None:
            result['Os'] = self.os
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.time_range is not None:
            result['TimeRange'] = self.time_range.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('BizModule') is not None:
            self.biz_module = m.get('BizModule')
        if m.get('Filter') is not None:
            temp_model = GetIssuesRequestFilter()
            self.filter = temp_model.from_map(m['Filter'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeRange') is not None:
            temp_model = GetIssuesRequestTimeRange()
            self.time_range = temp_model.from_map(m['TimeRange'])
        return self


class GetIssuesShrinkRequestTimeRange(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        granularity: int = None,
        granularity_unit: str = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.granularity = granularity
        self.granularity_unit = granularity_unit
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
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.granularity_unit is not None:
            result['GranularityUnit'] = self.granularity_unit
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('GranularityUnit') is not None:
            self.granularity_unit = m.get('GranularityUnit')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetIssuesShrinkRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        biz_module: str = None,
        filter_shrink: str = None,
        name: str = None,
        order_by: str = None,
        order_type: str = None,
        os: str = None,
        page_index: int = None,
        page_size: int = None,
        status: int = None,
        time_range: GetIssuesShrinkRequestTimeRange = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.biz_module = biz_module
        self.filter_shrink = filter_shrink
        self.name = name
        self.order_by = order_by
        self.order_type = order_type
        self.os = os
        self.page_index = page_index
        self.page_size = page_size
        self.status = status
        # This parameter is required.
        self.time_range = time_range

    def validate(self):
        if self.time_range:
            self.time_range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.biz_module is not None:
            result['BizModule'] = self.biz_module
        if self.filter_shrink is not None:
            result['Filter'] = self.filter_shrink
        if self.name is not None:
            result['Name'] = self.name
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.os is not None:
            result['Os'] = self.os
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.time_range is not None:
            result['TimeRange'] = self.time_range.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('BizModule') is not None:
            self.biz_module = m.get('BizModule')
        if m.get('Filter') is not None:
            self.filter_shrink = m.get('Filter')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimeRange') is not None:
            temp_model = GetIssuesShrinkRequestTimeRange()
            self.time_range = temp_model.from_map(m['TimeRange'])
        return self


class GetIssuesResponseBodyModelItems(TeaModel):
    def __init__(
        self,
        affected_user_count: int = None,
        alloc_size_max: int = None,
        alloc_size_pct_50: int = None,
        alloc_size_pct_70: int = None,
        alloc_size_pct_90: int = None,
        digest_hash: str = None,
        dom_score: str = None,
        error_column: int = None,
        error_count: int = None,
        error_device_count: int = None,
        error_device_rate: float = None,
        error_file_name: str = None,
        error_line: int = None,
        error_name: str = None,
        error_rate: float = None,
        error_type: str = None,
        event_time: str = None,
        first_version: str = None,
        name: str = None,
        stack: str = None,
        status: int = None,
    ):
        self.affected_user_count = affected_user_count
        self.alloc_size_max = alloc_size_max
        self.alloc_size_pct_50 = alloc_size_pct_50
        self.alloc_size_pct_70 = alloc_size_pct_70
        self.alloc_size_pct_90 = alloc_size_pct_90
        self.digest_hash = digest_hash
        self.dom_score = dom_score
        self.error_column = error_column
        self.error_count = error_count
        self.error_device_count = error_device_count
        self.error_device_rate = error_device_rate
        self.error_file_name = error_file_name
        self.error_line = error_line
        self.error_name = error_name
        self.error_rate = error_rate
        self.error_type = error_type
        self.event_time = event_time
        self.first_version = first_version
        self.name = name
        self.stack = stack
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.affected_user_count is not None:
            result['AffectedUserCount'] = self.affected_user_count
        if self.alloc_size_max is not None:
            result['AllocSizeMax'] = self.alloc_size_max
        if self.alloc_size_pct_50 is not None:
            result['AllocSizePct50'] = self.alloc_size_pct_50
        if self.alloc_size_pct_70 is not None:
            result['AllocSizePct70'] = self.alloc_size_pct_70
        if self.alloc_size_pct_90 is not None:
            result['AllocSizePct90'] = self.alloc_size_pct_90
        if self.digest_hash is not None:
            result['DigestHash'] = self.digest_hash
        if self.dom_score is not None:
            result['DomScore'] = self.dom_score
        if self.error_column is not None:
            result['ErrorColumn'] = self.error_column
        if self.error_count is not None:
            result['ErrorCount'] = self.error_count
        if self.error_device_count is not None:
            result['ErrorDeviceCount'] = self.error_device_count
        if self.error_device_rate is not None:
            result['ErrorDeviceRate'] = self.error_device_rate
        if self.error_file_name is not None:
            result['ErrorFileName'] = self.error_file_name
        if self.error_line is not None:
            result['ErrorLine'] = self.error_line
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.error_rate is not None:
            result['ErrorRate'] = self.error_rate
        if self.error_type is not None:
            result['ErrorType'] = self.error_type
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.first_version is not None:
            result['FirstVersion'] = self.first_version
        if self.name is not None:
            result['Name'] = self.name
        if self.stack is not None:
            result['Stack'] = self.stack
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectedUserCount') is not None:
            self.affected_user_count = m.get('AffectedUserCount')
        if m.get('AllocSizeMax') is not None:
            self.alloc_size_max = m.get('AllocSizeMax')
        if m.get('AllocSizePct50') is not None:
            self.alloc_size_pct_50 = m.get('AllocSizePct50')
        if m.get('AllocSizePct70') is not None:
            self.alloc_size_pct_70 = m.get('AllocSizePct70')
        if m.get('AllocSizePct90') is not None:
            self.alloc_size_pct_90 = m.get('AllocSizePct90')
        if m.get('DigestHash') is not None:
            self.digest_hash = m.get('DigestHash')
        if m.get('DomScore') is not None:
            self.dom_score = m.get('DomScore')
        if m.get('ErrorColumn') is not None:
            self.error_column = m.get('ErrorColumn')
        if m.get('ErrorCount') is not None:
            self.error_count = m.get('ErrorCount')
        if m.get('ErrorDeviceCount') is not None:
            self.error_device_count = m.get('ErrorDeviceCount')
        if m.get('ErrorDeviceRate') is not None:
            self.error_device_rate = m.get('ErrorDeviceRate')
        if m.get('ErrorFileName') is not None:
            self.error_file_name = m.get('ErrorFileName')
        if m.get('ErrorLine') is not None:
            self.error_line = m.get('ErrorLine')
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('ErrorRate') is not None:
            self.error_rate = m.get('ErrorRate')
        if m.get('ErrorType') is not None:
            self.error_type = m.get('ErrorType')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('FirstVersion') is not None:
            self.first_version = m.get('FirstVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Stack') is not None:
            self.stack = m.get('Stack')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetIssuesResponseBodyModel(TeaModel):
    def __init__(
        self,
        items: List[GetIssuesResponseBodyModelItems] = None,
        page_num: int = None,
        page_size: int = None,
        pages: int = None,
        total: int = None,
    ):
        self.items = items
        self.page_num = page_num
        self.page_size = page_size
        self.pages = pages
        self.total = total

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = GetIssuesResponseBodyModelItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetIssuesResponseBody(TeaModel):
    def __init__(
        self,
        args: Dict[str, Any] = None,
        error_code: int = None,
        message: str = None,
        model: GetIssuesResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Args
        self.args = args
        self.error_code = error_code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['Args'] = self.args
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = GetIssuesResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetIssuesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetIssuesResponseBody = None,
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
            temp_model = GetIssuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSymbolicFilesRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        app_version: str = None,
        build_id: str = None,
        end_time: int = None,
        export_status: str = None,
        file_name: str = None,
        file_type: str = None,
        os: str = None,
        page_index: int = None,
        page_size: int = None,
        start_time: int = None,
        uuid: str = None,
    ):
        # appKey
        # 
        # This parameter is required.
        self.app_key = app_key
        self.app_version = app_version
        self.build_id = build_id
        self.end_time = end_time
        self.export_status = export_status
        self.file_name = file_name
        # This parameter is required.
        self.file_type = file_type
        # This parameter is required.
        self.os = os
        # This parameter is required.
        self.page_index = page_index
        # This parameter is required.
        self.page_size = page_size
        self.start_time = start_time
        # uuid
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.build_id is not None:
            result['BuildId'] = self.build_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.export_status is not None:
            result['ExportStatus'] = self.export_status
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.os is not None:
            result['Os'] = self.os
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('BuildId') is not None:
            self.build_id = m.get('BuildId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExportStatus') is not None:
            self.export_status = m.get('ExportStatus')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetSymbolicFilesResponseBodyModelItems(TeaModel):
    def __init__(
        self,
        app_version: str = None,
        build_id: str = None,
        export_status: str = None,
        file_name: str = None,
        file_path: str = None,
        file_type: str = None,
        gmt_create: int = None,
        id: int = None,
        status: str = None,
        uuid: str = None,
    ):
        self.app_version = app_version
        self.build_id = build_id
        self.export_status = export_status
        self.file_name = file_name
        self.file_path = file_path
        self.file_type = file_type
        self.gmt_create = gmt_create
        self.id = id
        self.status = status
        # uuid
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.build_id is not None:
            result['BuildId'] = self.build_id
        if self.export_status is not None:
            result['ExportStatus'] = self.export_status
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.status is not None:
            result['Status'] = self.status
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('BuildId') is not None:
            self.build_id = m.get('BuildId')
        if m.get('ExportStatus') is not None:
            self.export_status = m.get('ExportStatus')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetSymbolicFilesResponseBodyModel(TeaModel):
    def __init__(
        self,
        items: List[GetSymbolicFilesResponseBodyModelItems] = None,
        page_num: int = None,
        page_size: int = None,
        pages: int = None,
        total: int = None,
    ):
        self.items = items
        self.page_num = page_num
        self.page_size = page_size
        self.pages = pages
        self.total = total

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pages is not None:
            result['Pages'] = self.pages
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = GetSymbolicFilesResponseBodyModelItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetSymbolicFilesResponseBody(TeaModel):
    def __init__(
        self,
        args: Dict[str, Any] = None,
        error_code: int = None,
        message: str = None,
        model: GetSymbolicFilesResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Args
        self.args = args
        self.error_code = error_code
        self.message = message
        self.model = model
        # requestId
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['Args'] = self.args
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = GetSymbolicFilesResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSymbolicFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSymbolicFilesResponseBody = None,
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
            temp_model = GetSymbolicFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RequestUploadTokenRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        os: str = None,
    ):
        # appKey
        # 
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.os = os

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.os is not None:
            result['Os'] = self.os
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        return self


class RequestUploadTokenResponseBodyModel(TeaModel):
    def __init__(
        self,
        access_key_id: str = None,
        access_key_secret: str = None,
        endpoint: str = None,
        security_token: str = None,
        upload_bucket: str = None,
        upload_dir: str = None,
    ):
        # OSS AccessKeyId
        self.access_key_id = access_key_id
        # OSS AccessKeySecret
        self.access_key_secret = access_key_secret
        self.endpoint = endpoint
        self.security_token = security_token
        self.upload_bucket = upload_bucket
        self.upload_dir = upload_dir

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.upload_bucket is not None:
            result['UploadBucket'] = self.upload_bucket
        if self.upload_dir is not None:
            result['UploadDir'] = self.upload_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('UploadBucket') is not None:
            self.upload_bucket = m.get('UploadBucket')
        if m.get('UploadDir') is not None:
            self.upload_dir = m.get('UploadDir')
        return self


class RequestUploadTokenResponseBody(TeaModel):
    def __init__(
        self,
        args: Dict[str, Any] = None,
        error_code: int = None,
        message: str = None,
        model: RequestUploadTokenResponseBodyModel = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Args
        self.args = args
        self.error_code = error_code
        self.message = message
        self.model = model
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['Args'] = self.args
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = RequestUploadTokenResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RequestUploadTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RequestUploadTokenResponseBody = None,
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
            temp_model = RequestUploadTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitSymbolicRequest(TeaModel):
    def __init__(
        self,
        app_key: int = None,
        app_version: str = None,
        build_id: str = None,
        file_name: str = None,
        file_path: str = None,
        file_type: str = None,
        os: str = None,
        uuid: str = None,
    ):
        # appKey
        # 
        # This parameter is required.
        self.app_key = app_key
        self.app_version = app_version
        self.build_id = build_id
        # This parameter is required.
        self.file_name = file_name
        # This parameter is required.
        self.file_path = file_path
        # This parameter is required.
        self.file_type = file_type
        # This parameter is required.
        self.os = os
        # uuid
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.build_id is not None:
            result['BuildId'] = self.build_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.os is not None:
            result['Os'] = self.os
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('BuildId') is not None:
            self.build_id = m.get('BuildId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Os') is not None:
            self.os = m.get('Os')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class SubmitSymbolicResponseBody(TeaModel):
    def __init__(
        self,
        args: Dict[str, Any] = None,
        error_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # args
        self.args = args
        self.error_code = error_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['Args'] = self.args
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitSymbolicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitSymbolicResponseBody = None,
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
            temp_model = SubmitSymbolicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


