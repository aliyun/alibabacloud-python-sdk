# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListDlpOutboundLogsResponseBody(DaraModel):
    def __init__(
        self,
        logs: List[main_models.ListDlpOutboundLogsResponseBodyLogs] = None,
        request_id: str = None,
        total_number: int = None,
    ):
        # The log objects.
        self.logs = logs
        # The request ID.
        self.request_id = request_id
        # The total number of records that match the query conditions.
        self.total_number = total_number

    def validate(self):
        if self.logs:
            for v1 in self.logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Logs'] = []
        if self.logs is not None:
            for k1 in self.logs:
                result['Logs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_number is not None:
            result['TotalNumber'] = self.total_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.logs = []
        if m.get('Logs') is not None:
            for k1 in m.get('Logs'):
                temp_model = main_models.ListDlpOutboundLogsResponseBodyLogs()
                self.logs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNumber') is not None:
            self.total_number = m.get('TotalNumber')

        return self

class ListDlpOutboundLogsResponseBodyLogs(DaraModel):
    def __init__(
        self,
        category: str = None,
        channel_id: str = None,
        channel_type: str = None,
        department: str = None,
        dev_file_path: str = None,
        device_tag: str = None,
        device_type: str = None,
        dlp_storage_config_id: str = None,
        dlp_storage_type: str = None,
        dst_addr: str = None,
        file_origin: str = None,
        file_origin_host: str = None,
        file_origin_referrer: str = None,
        file_preview: str = None,
        format: str = None,
        group_info: str = None,
        host_name: str = None,
        log_id: str = None,
        matched_dicts: main_models.ListDlpOutboundLogsResponseBodyLogsMatchedDicts = None,
        matched_policies: List[main_models.ListDlpOutboundLogsResponseBodyLogsMatchedPolicies] = None,
        oss_file_name: str = None,
        policy_action: str = None,
        policy_name: List[str] = None,
        process_name: str = None,
        process_name_desc: str = None,
        risk_level: str = None,
        scene: str = None,
        screen_file_path: str = None,
        size: str = None,
        src_file_name: str = None,
        src_ip: str = None,
        start_time: str = None,
        upload_time: str = None,
        user: str = None,
    ):
        # The file category.
        self.category = category
        # The primary channel ID.
        self.channel_id = channel_id
        # The primary channel.
        self.channel_type = channel_type
        # The department.
        self.department = department
        # The local path of the file on the device.
        self.dev_file_path = dev_file_path
        # The unique identifier of the device.
        self.device_tag = device_tag
        # The device type.
        self.device_type = device_type
        # The storage policy ID.
        self.dlp_storage_config_id = dlp_storage_config_id
        # The storage type.
        self.dlp_storage_type = dlp_storage_type
        # The outbound destination address or URL.
        self.dst_addr = dst_addr
        # The file source.
        self.file_origin = file_origin
        # The host of the file source.
        self.file_origin_host = file_origin_host
        # The referrer of the file source.
        self.file_origin_referrer = file_origin_referrer
        # The file content preview snippet.
        self.file_preview = file_preview
        # The file type.
        self.format = format
        # The organizational structure path.
        self.group_info = group_info
        # The hostname of the device.
        self.host_name = host_name
        # LogId
        self.log_id = log_id
        # The matched dictionary statistics.
        self.matched_dicts = matched_dicts
        # The list of matched policy details.
        self.matched_policies = matched_policies
        # The object path of the sensitive file in the storage bucket.
        self.oss_file_name = oss_file_name
        # The policy action.
        self.policy_action = policy_action
        # The list of matched policy names.
        self.policy_name = policy_name
        # The outbound process name.
        self.process_name = process_name
        # The secondary channel description.
        self.process_name_desc = process_name_desc
        # The risk level.
        self.risk_level = risk_level
        # The matched risk scenario.
        self.scene = scene
        # The storage path of the screenshot file.
        self.screen_file_path = screen_file_path
        # The file size.
        self.size = size
        # The original file name.
        self.src_file_name = src_file_name
        # The source IP address of the device.
        self.src_ip = src_ip
        # The time when the event occurred.
        self.start_time = start_time
        # The time when the log was reported.
        self.upload_time = upload_time
        # The username.
        self.user = user

    def validate(self):
        if self.matched_dicts:
            self.matched_dicts.validate()
        if self.matched_policies:
            for v1 in self.matched_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.channel_type is not None:
            result['ChannelType'] = self.channel_type

        if self.department is not None:
            result['Department'] = self.department

        if self.dev_file_path is not None:
            result['DevFilePath'] = self.dev_file_path

        if self.device_tag is not None:
            result['DeviceTag'] = self.device_tag

        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.dlp_storage_config_id is not None:
            result['DlpStorageConfigId'] = self.dlp_storage_config_id

        if self.dlp_storage_type is not None:
            result['DlpStorageType'] = self.dlp_storage_type

        if self.dst_addr is not None:
            result['DstAddr'] = self.dst_addr

        if self.file_origin is not None:
            result['FileOrigin'] = self.file_origin

        if self.file_origin_host is not None:
            result['FileOriginHost'] = self.file_origin_host

        if self.file_origin_referrer is not None:
            result['FileOriginReferrer'] = self.file_origin_referrer

        if self.file_preview is not None:
            result['FilePreview'] = self.file_preview

        if self.format is not None:
            result['Format'] = self.format

        if self.group_info is not None:
            result['GroupInfo'] = self.group_info

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.log_id is not None:
            result['LogId'] = self.log_id

        if self.matched_dicts is not None:
            result['MatchedDicts'] = self.matched_dicts.to_map()

        result['MatchedPolicies'] = []
        if self.matched_policies is not None:
            for k1 in self.matched_policies:
                result['MatchedPolicies'].append(k1.to_map() if k1 else None)

        if self.oss_file_name is not None:
            result['OssFileName'] = self.oss_file_name

        if self.policy_action is not None:
            result['PolicyAction'] = self.policy_action

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        if self.process_name_desc is not None:
            result['ProcessNameDesc'] = self.process_name_desc

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.screen_file_path is not None:
            result['ScreenFilePath'] = self.screen_file_path

        if self.size is not None:
            result['Size'] = self.size

        if self.src_file_name is not None:
            result['SrcFileName'] = self.src_file_name

        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.upload_time is not None:
            result['UploadTime'] = self.upload_time

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('ChannelType') is not None:
            self.channel_type = m.get('ChannelType')

        if m.get('Department') is not None:
            self.department = m.get('Department')

        if m.get('DevFilePath') is not None:
            self.dev_file_path = m.get('DevFilePath')

        if m.get('DeviceTag') is not None:
            self.device_tag = m.get('DeviceTag')

        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('DlpStorageConfigId') is not None:
            self.dlp_storage_config_id = m.get('DlpStorageConfigId')

        if m.get('DlpStorageType') is not None:
            self.dlp_storage_type = m.get('DlpStorageType')

        if m.get('DstAddr') is not None:
            self.dst_addr = m.get('DstAddr')

        if m.get('FileOrigin') is not None:
            self.file_origin = m.get('FileOrigin')

        if m.get('FileOriginHost') is not None:
            self.file_origin_host = m.get('FileOriginHost')

        if m.get('FileOriginReferrer') is not None:
            self.file_origin_referrer = m.get('FileOriginReferrer')

        if m.get('FilePreview') is not None:
            self.file_preview = m.get('FilePreview')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('GroupInfo') is not None:
            self.group_info = m.get('GroupInfo')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('LogId') is not None:
            self.log_id = m.get('LogId')

        if m.get('MatchedDicts') is not None:
            temp_model = main_models.ListDlpOutboundLogsResponseBodyLogsMatchedDicts()
            self.matched_dicts = temp_model.from_map(m.get('MatchedDicts'))

        self.matched_policies = []
        if m.get('MatchedPolicies') is not None:
            for k1 in m.get('MatchedPolicies'):
                temp_model = main_models.ListDlpOutboundLogsResponseBodyLogsMatchedPolicies()
                self.matched_policies.append(temp_model.from_map(k1))

        if m.get('OssFileName') is not None:
            self.oss_file_name = m.get('OssFileName')

        if m.get('PolicyAction') is not None:
            self.policy_action = m.get('PolicyAction')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        if m.get('ProcessNameDesc') is not None:
            self.process_name_desc = m.get('ProcessNameDesc')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('ScreenFilePath') is not None:
            self.screen_file_path = m.get('ScreenFilePath')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SrcFileName') is not None:
            self.src_file_name = m.get('SrcFileName')

        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UploadTime') is not None:
            self.upload_time = m.get('UploadTime')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

class ListDlpOutboundLogsResponseBodyLogsMatchedPolicies(DaraModel):
    def __init__(
        self,
        engine_data_level: str = None,
        engine_data_type: str = None,
        engine_name: str = None,
        policy_desc: str = None,
        policy_name: str = None,
    ):
        # The corresponding data level.
        self.engine_data_level = engine_data_level
        # The corresponding data type.
        self.engine_data_type = engine_data_type
        # The matched detection rule name.
        self.engine_name = engine_name
        # The policy description.
        self.policy_desc = policy_desc
        # The matched policy name.
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine_data_level is not None:
            result['EngineDataLevel'] = self.engine_data_level

        if self.engine_data_type is not None:
            result['EngineDataType'] = self.engine_data_type

        if self.engine_name is not None:
            result['EngineName'] = self.engine_name

        if self.policy_desc is not None:
            result['PolicyDesc'] = self.policy_desc

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EngineDataLevel') is not None:
            self.engine_data_level = m.get('EngineDataLevel')

        if m.get('EngineDataType') is not None:
            self.engine_data_type = m.get('EngineDataType')

        if m.get('EngineName') is not None:
            self.engine_name = m.get('EngineName')

        if m.get('PolicyDesc') is not None:
            self.policy_desc = m.get('PolicyDesc')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        return self

class ListDlpOutboundLogsResponseBodyLogsMatchedDicts(DaraModel):
    def __init__(
        self,
        inner_dicts: List[main_models.ListDlpOutboundLogsResponseBodyLogsMatchedDictsInnerDicts] = None,
        keywords: List[main_models.ListDlpOutboundLogsResponseBodyLogsMatchedDictsKeywords] = None,
        user_dicts: List[main_models.ListDlpOutboundLogsResponseBodyLogsMatchedDictsUserDicts] = None,
    ):
        # The matched built-in dictionaries.
        self.inner_dicts = inner_dicts
        # The matched keywords.
        self.keywords = keywords
        # The matched built-in dictionaries.
        self.user_dicts = user_dicts

    def validate(self):
        if self.inner_dicts:
            for v1 in self.inner_dicts:
                 if v1:
                    v1.validate()
        if self.keywords:
            for v1 in self.keywords:
                 if v1:
                    v1.validate()
        if self.user_dicts:
            for v1 in self.user_dicts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InnerDicts'] = []
        if self.inner_dicts is not None:
            for k1 in self.inner_dicts:
                result['InnerDicts'].append(k1.to_map() if k1 else None)

        result['Keywords'] = []
        if self.keywords is not None:
            for k1 in self.keywords:
                result['Keywords'].append(k1.to_map() if k1 else None)

        result['UserDicts'] = []
        if self.user_dicts is not None:
            for k1 in self.user_dicts:
                result['UserDicts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.inner_dicts = []
        if m.get('InnerDicts') is not None:
            for k1 in m.get('InnerDicts'):
                temp_model = main_models.ListDlpOutboundLogsResponseBodyLogsMatchedDictsInnerDicts()
                self.inner_dicts.append(temp_model.from_map(k1))

        self.keywords = []
        if m.get('Keywords') is not None:
            for k1 in m.get('Keywords'):
                temp_model = main_models.ListDlpOutboundLogsResponseBodyLogsMatchedDictsKeywords()
                self.keywords.append(temp_model.from_map(k1))

        self.user_dicts = []
        if m.get('UserDicts') is not None:
            for k1 in m.get('UserDicts'):
                temp_model = main_models.ListDlpOutboundLogsResponseBodyLogsMatchedDictsUserDicts()
                self.user_dicts.append(temp_model.from_map(k1))

        return self

class ListDlpOutboundLogsResponseBodyLogsMatchedDictsUserDicts(DaraModel):
    def __init__(
        self,
        count: int = None,
        name: str = None,
    ):
        # The number of matches.
        self.count = count
        # The dictionary name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class ListDlpOutboundLogsResponseBodyLogsMatchedDictsKeywords(DaraModel):
    def __init__(
        self,
        count: int = None,
        name: str = None,
    ):
        # The number of matches.
        self.count = count
        # The keyword name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class ListDlpOutboundLogsResponseBodyLogsMatchedDictsInnerDicts(DaraModel):
    def __init__(
        self,
        count: int = None,
        name: str = None,
    ):
        # The number of matches.
        self.count = count
        # The dictionary name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

