# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CheckMfdServiceOpenResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckMfdServiceOpenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckMfdServiceOpenResponseBody = None,
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
            temp_model = CheckMfdServiceOpenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOssBucketScanTaskRequest(TeaModel):
    def __init__(
        self,
        all_key_prefix: str = None,
        bucket_name_list: List[str] = None,
        decompress_max_file_count: int = None,
        decompress_max_layer: int = None,
        decryption_list: List[str] = None,
        exclude_key_suffix_list: List[str] = None,
        key_prefix_list: List[str] = None,
        key_suffix_list: List[str] = None,
        last_modified_start_time: int = None,
        scan_mode: int = None,
    ):
        self.all_key_prefix = all_key_prefix
        # This parameter is required.
        self.bucket_name_list = bucket_name_list
        self.decompress_max_file_count = decompress_max_file_count
        self.decompress_max_layer = decompress_max_layer
        self.decryption_list = decryption_list
        self.exclude_key_suffix_list = exclude_key_suffix_list
        self.key_prefix_list = key_prefix_list
        self.key_suffix_list = key_suffix_list
        self.last_modified_start_time = last_modified_start_time
        # This parameter is required.
        self.scan_mode = scan_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_key_prefix is not None:
            result['AllKeyPrefix'] = self.all_key_prefix
        if self.bucket_name_list is not None:
            result['BucketNameList'] = self.bucket_name_list
        if self.decompress_max_file_count is not None:
            result['DecompressMaxFileCount'] = self.decompress_max_file_count
        if self.decompress_max_layer is not None:
            result['DecompressMaxLayer'] = self.decompress_max_layer
        if self.decryption_list is not None:
            result['DecryptionList'] = self.decryption_list
        if self.exclude_key_suffix_list is not None:
            result['ExcludeKeySuffixList'] = self.exclude_key_suffix_list
        if self.key_prefix_list is not None:
            result['KeyPrefixList'] = self.key_prefix_list
        if self.key_suffix_list is not None:
            result['KeySuffixList'] = self.key_suffix_list
        if self.last_modified_start_time is not None:
            result['LastModifiedStartTime'] = self.last_modified_start_time
        if self.scan_mode is not None:
            result['ScanMode'] = self.scan_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllKeyPrefix') is not None:
            self.all_key_prefix = m.get('AllKeyPrefix')
        if m.get('BucketNameList') is not None:
            self.bucket_name_list = m.get('BucketNameList')
        if m.get('DecompressMaxFileCount') is not None:
            self.decompress_max_file_count = m.get('DecompressMaxFileCount')
        if m.get('DecompressMaxLayer') is not None:
            self.decompress_max_layer = m.get('DecompressMaxLayer')
        if m.get('DecryptionList') is not None:
            self.decryption_list = m.get('DecryptionList')
        if m.get('ExcludeKeySuffixList') is not None:
            self.exclude_key_suffix_list = m.get('ExcludeKeySuffixList')
        if m.get('KeyPrefixList') is not None:
            self.key_prefix_list = m.get('KeyPrefixList')
        if m.get('KeySuffixList') is not None:
            self.key_suffix_list = m.get('KeySuffixList')
        if m.get('LastModifiedStartTime') is not None:
            self.last_modified_start_time = m.get('LastModifiedStartTime')
        if m.get('ScanMode') is not None:
            self.scan_mode = m.get('ScanMode')
        return self


class CreateOssBucketScanTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateOssBucketScanTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateOssBucketScanTaskResponseBody = None,
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
            temp_model = CreateOssBucketScanTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOssScanConfigRequest(TeaModel):
    def __init__(
        self,
        all_key_prefix: str = None,
        bucket_name: str = None,
        decompress_max_file_count: int = None,
        decompress_max_layer: int = None,
        decryption_list: List[str] = None,
        enable: int = None,
        end_time: str = None,
        key_prefix_list: List[str] = None,
        key_suffix_list: List[str] = None,
        last_modified_start_time: int = None,
        name: str = None,
        real_time_incr: bool = None,
        scan_day_list: List[int] = None,
        start_time: str = None,
    ):
        self.all_key_prefix = all_key_prefix
        # This parameter is required.
        self.bucket_name = bucket_name
        self.decompress_max_file_count = decompress_max_file_count
        self.decompress_max_layer = decompress_max_layer
        self.decryption_list = decryption_list
        # This parameter is required.
        self.enable = enable
        self.end_time = end_time
        self.key_prefix_list = key_prefix_list
        self.key_suffix_list = key_suffix_list
        self.last_modified_start_time = last_modified_start_time
        self.name = name
        self.real_time_incr = real_time_incr
        self.scan_day_list = scan_day_list
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_key_prefix is not None:
            result['AllKeyPrefix'] = self.all_key_prefix
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.decompress_max_file_count is not None:
            result['DecompressMaxFileCount'] = self.decompress_max_file_count
        if self.decompress_max_layer is not None:
            result['DecompressMaxLayer'] = self.decompress_max_layer
        if self.decryption_list is not None:
            result['DecryptionList'] = self.decryption_list
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.key_prefix_list is not None:
            result['KeyPrefixList'] = self.key_prefix_list
        if self.key_suffix_list is not None:
            result['KeySuffixList'] = self.key_suffix_list
        if self.last_modified_start_time is not None:
            result['LastModifiedStartTime'] = self.last_modified_start_time
        if self.name is not None:
            result['Name'] = self.name
        if self.real_time_incr is not None:
            result['RealTimeIncr'] = self.real_time_incr
        if self.scan_day_list is not None:
            result['ScanDayList'] = self.scan_day_list
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllKeyPrefix') is not None:
            self.all_key_prefix = m.get('AllKeyPrefix')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('DecompressMaxFileCount') is not None:
            self.decompress_max_file_count = m.get('DecompressMaxFileCount')
        if m.get('DecompressMaxLayer') is not None:
            self.decompress_max_layer = m.get('DecompressMaxLayer')
        if m.get('DecryptionList') is not None:
            self.decryption_list = m.get('DecryptionList')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('KeyPrefixList') is not None:
            self.key_prefix_list = m.get('KeyPrefixList')
        if m.get('KeySuffixList') is not None:
            self.key_suffix_list = m.get('KeySuffixList')
        if m.get('LastModifiedStartTime') is not None:
            self.last_modified_start_time = m.get('LastModifiedStartTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RealTimeIncr') is not None:
            self.real_time_incr = m.get('RealTimeIncr')
        if m.get('ScanDayList') is not None:
            self.scan_day_list = m.get('ScanDayList')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreateOssScanConfigResponseBody(TeaModel):
    def __init__(
        self,
        id: int = None,
        request_id: str = None,
    ):
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateOssScanConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateOssScanConfigResponseBody = None,
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
            temp_model = CreateOssScanConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExportInfoRequest(TeaModel):
    def __init__(
        self,
        export_id: int = None,
    ):
        # This parameter is required.
        self.export_id = export_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_id is not None:
            result['ExportId'] = self.export_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportId') is not None:
            self.export_id = m.get('ExportId')
        return self


class DescribeExportInfoResponseBody(TeaModel):
    def __init__(
        self,
        current_count: int = None,
        export_status: str = None,
        file_name: str = None,
        id: int = None,
        link: str = None,
        message: str = None,
        progress: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_count = current_count
        self.export_status = export_status
        self.file_name = file_name
        self.id = id
        self.link = link
        self.message = message
        self.progress = progress
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_count is not None:
            result['CurrentCount'] = self.current_count
        if self.export_status is not None:
            result['ExportStatus'] = self.export_status
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.id is not None:
            result['Id'] = self.id
        if self.link is not None:
            result['Link'] = self.link
        if self.message is not None:
            result['Message'] = self.message
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentCount') is not None:
            self.current_count = m.get('CurrentCount')
        if m.get('ExportStatus') is not None:
            self.export_status = m.get('ExportStatus')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Link') is not None:
            self.link = m.get('Link')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeExportInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeExportInfoResponseBody = None,
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
            temp_model = DescribeExportInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceLinkedRoleStatusRequest(TeaModel):
    def __init__(
        self,
        service_linked_role: str = None,
    ):
        self.service_linked_role = service_linked_role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_linked_role is not None:
            result['ServiceLinkedRole'] = self.service_linked_role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceLinkedRole') is not None:
            self.service_linked_role = m.get('ServiceLinkedRole')
        return self


class DescribeServiceLinkedRoleStatusResponseBodyRoleStatus(TeaModel):
    def __init__(
        self,
        status: bool = None,
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


class DescribeServiceLinkedRoleStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        role_status: DescribeServiceLinkedRoleStatusResponseBodyRoleStatus = None,
    ):
        self.request_id = request_id
        self.role_status = role_status

    def validate(self):
        if self.role_status:
            self.role_status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role_status is not None:
            result['RoleStatus'] = self.role_status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RoleStatus') is not None:
            temp_model = DescribeServiceLinkedRoleStatusResponseBodyRoleStatus()
            self.role_status = temp_model.from_map(m['RoleStatus'])
        return self


class DescribeServiceLinkedRoleStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeServiceLinkedRoleStatusResponseBody = None,
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
            temp_model = DescribeServiceLinkedRoleStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportRecordRequest(TeaModel):
    def __init__(
        self,
        export_type: str = None,
        lang: str = None,
        params: str = None,
    ):
        # This parameter is required.
        self.export_type = export_type
        self.lang = lang
        self.params = params

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_type is not None:
            result['ExportType'] = self.export_type
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.params is not None:
            result['Params'] = self.params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        return self


class ExportRecordResponseBody(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        id: int = None,
        request_id: str = None,
    ):
        self.file_name = file_name
        self.id = id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.id is not None:
            result['Id'] = self.id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExportRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportRecordResponseBody = None,
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
            temp_model = ExportRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileDetectReportRequest(TeaModel):
    def __init__(
        self,
        event_id: int = None,
        field: str = None,
        file_hash: str = None,
        lang: str = None,
        source_type: str = None,
    ):
        self.event_id = event_id
        self.field = field
        self.file_hash = file_hash
        self.lang = lang
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.field is not None:
            result['Field'] = self.field
        if self.file_hash is not None:
            result['FileHash'] = self.file_hash
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('Field') is not None:
            self.field = m.get('Field')
        if m.get('FileHash') is not None:
            self.file_hash = m.get('FileHash')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class GetFileDetectReportResponseBodyData(TeaModel):
    def __init__(
        self,
        basic: str = None,
        file_hash: str = None,
        filename: str = None,
        has_data: bool = None,
        intelligences: str = None,
        sandbox: str = None,
        show_tab: bool = None,
        threat_level: int = None,
        threat_types: str = None,
    ):
        self.basic = basic
        self.file_hash = file_hash
        self.filename = filename
        self.has_data = has_data
        self.intelligences = intelligences
        self.sandbox = sandbox
        self.show_tab = show_tab
        self.threat_level = threat_level
        self.threat_types = threat_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.basic is not None:
            result['Basic'] = self.basic
        if self.file_hash is not None:
            result['FileHash'] = self.file_hash
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.has_data is not None:
            result['HasData'] = self.has_data
        if self.intelligences is not None:
            result['Intelligences'] = self.intelligences
        if self.sandbox is not None:
            result['Sandbox'] = self.sandbox
        if self.show_tab is not None:
            result['ShowTab'] = self.show_tab
        if self.threat_level is not None:
            result['ThreatLevel'] = self.threat_level
        if self.threat_types is not None:
            result['ThreatTypes'] = self.threat_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Basic') is not None:
            self.basic = m.get('Basic')
        if m.get('FileHash') is not None:
            self.file_hash = m.get('FileHash')
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('HasData') is not None:
            self.has_data = m.get('HasData')
        if m.get('Intelligences') is not None:
            self.intelligences = m.get('Intelligences')
        if m.get('Sandbox') is not None:
            self.sandbox = m.get('Sandbox')
        if m.get('ShowTab') is not None:
            self.show_tab = m.get('ShowTab')
        if m.get('ThreatLevel') is not None:
            self.threat_level = m.get('ThreatLevel')
        if m.get('ThreatTypes') is not None:
            self.threat_types = m.get('ThreatTypes')
        return self


class GetFileDetectReportResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetFileDetectReportResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetFileDetectReportResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetFileDetectReportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetFileDetectReportResponseBody = None,
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
            temp_model = GetFileDetectReportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOssBucketScanStatisticRequest(TeaModel):
    def __init__(
        self,
        bucket_name_list: List[str] = None,
    ):
        self.bucket_name_list = bucket_name_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name_list is not None:
            result['BucketNameList'] = self.bucket_name_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketNameList') is not None:
            self.bucket_name_list = m.get('BucketNameList')
        return self


class GetOssBucketScanStatisticResponseBodyData(TeaModel):
    def __init__(
        self,
        expire_time: int = None,
        high_risk: int = None,
        low_risk: int = None,
        medium_risk: int = None,
        no_scan_bucket: int = None,
        remain_auth: int = None,
        risk_bucket: int = None,
        scan_object: int = None,
        total_bucket: int = None,
        total_object: int = None,
    ):
        self.expire_time = expire_time
        self.high_risk = high_risk
        self.low_risk = low_risk
        self.medium_risk = medium_risk
        self.no_scan_bucket = no_scan_bucket
        self.remain_auth = remain_auth
        self.risk_bucket = risk_bucket
        self.scan_object = scan_object
        self.total_bucket = total_bucket
        self.total_object = total_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.high_risk is not None:
            result['HighRisk'] = self.high_risk
        if self.low_risk is not None:
            result['LowRisk'] = self.low_risk
        if self.medium_risk is not None:
            result['MediumRisk'] = self.medium_risk
        if self.no_scan_bucket is not None:
            result['NoScanBucket'] = self.no_scan_bucket
        if self.remain_auth is not None:
            result['RemainAuth'] = self.remain_auth
        if self.risk_bucket is not None:
            result['RiskBucket'] = self.risk_bucket
        if self.scan_object is not None:
            result['ScanObject'] = self.scan_object
        if self.total_bucket is not None:
            result['TotalBucket'] = self.total_bucket
        if self.total_object is not None:
            result['TotalObject'] = self.total_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('HighRisk') is not None:
            self.high_risk = m.get('HighRisk')
        if m.get('LowRisk') is not None:
            self.low_risk = m.get('LowRisk')
        if m.get('MediumRisk') is not None:
            self.medium_risk = m.get('MediumRisk')
        if m.get('NoScanBucket') is not None:
            self.no_scan_bucket = m.get('NoScanBucket')
        if m.get('RemainAuth') is not None:
            self.remain_auth = m.get('RemainAuth')
        if m.get('RiskBucket') is not None:
            self.risk_bucket = m.get('RiskBucket')
        if m.get('ScanObject') is not None:
            self.scan_object = m.get('ScanObject')
        if m.get('TotalBucket') is not None:
            self.total_bucket = m.get('TotalBucket')
        if m.get('TotalObject') is not None:
            self.total_object = m.get('TotalObject')
        return self


class GetOssBucketScanStatisticResponseBody(TeaModel):
    def __init__(
        self,
        data: GetOssBucketScanStatisticResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetOssBucketScanStatisticResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetOssBucketScanStatisticResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOssBucketScanStatisticResponseBody = None,
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
            temp_model = GetOssBucketScanStatisticResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOssScanConfigRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
    ):
        # This parameter is required.
        self.bucket_name = bucket_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        return self


class GetOssScanConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        all_key_prefix: bool = None,
        bucket_count: int = None,
        bucket_name: str = None,
        decompress_max_file_count: int = None,
        decompress_max_layer: int = None,
        decryption_list: List[str] = None,
        enable: int = None,
        end_time: str = None,
        id: str = None,
        key_prefix_list: List[str] = None,
        key_suffix_list: List[str] = None,
        last_modified_start_time: int = None,
        last_update_time: int = None,
        name: str = None,
        real_time_incr: bool = None,
        scan_day_list: List[int] = None,
        start_time: str = None,
    ):
        self.all_key_prefix = all_key_prefix
        self.bucket_count = bucket_count
        self.bucket_name = bucket_name
        self.decompress_max_file_count = decompress_max_file_count
        self.decompress_max_layer = decompress_max_layer
        self.decryption_list = decryption_list
        self.enable = enable
        self.end_time = end_time
        self.id = id
        self.key_prefix_list = key_prefix_list
        self.key_suffix_list = key_suffix_list
        self.last_modified_start_time = last_modified_start_time
        self.last_update_time = last_update_time
        self.name = name
        self.real_time_incr = real_time_incr
        self.scan_day_list = scan_day_list
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_key_prefix is not None:
            result['AllKeyPrefix'] = self.all_key_prefix
        if self.bucket_count is not None:
            result['BucketCount'] = self.bucket_count
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.decompress_max_file_count is not None:
            result['DecompressMaxFileCount'] = self.decompress_max_file_count
        if self.decompress_max_layer is not None:
            result['DecompressMaxLayer'] = self.decompress_max_layer
        if self.decryption_list is not None:
            result['DecryptionList'] = self.decryption_list
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.key_prefix_list is not None:
            result['KeyPrefixList'] = self.key_prefix_list
        if self.key_suffix_list is not None:
            result['KeySuffixList'] = self.key_suffix_list
        if self.last_modified_start_time is not None:
            result['LastModifiedStartTime'] = self.last_modified_start_time
        if self.last_update_time is not None:
            result['LastUpdateTime'] = self.last_update_time
        if self.name is not None:
            result['Name'] = self.name
        if self.real_time_incr is not None:
            result['RealTimeIncr'] = self.real_time_incr
        if self.scan_day_list is not None:
            result['ScanDayList'] = self.scan_day_list
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllKeyPrefix') is not None:
            self.all_key_prefix = m.get('AllKeyPrefix')
        if m.get('BucketCount') is not None:
            self.bucket_count = m.get('BucketCount')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('DecompressMaxFileCount') is not None:
            self.decompress_max_file_count = m.get('DecompressMaxFileCount')
        if m.get('DecompressMaxLayer') is not None:
            self.decompress_max_layer = m.get('DecompressMaxLayer')
        if m.get('DecryptionList') is not None:
            self.decryption_list = m.get('DecryptionList')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('KeyPrefixList') is not None:
            self.key_prefix_list = m.get('KeyPrefixList')
        if m.get('KeySuffixList') is not None:
            self.key_suffix_list = m.get('KeySuffixList')
        if m.get('LastModifiedStartTime') is not None:
            self.last_modified_start_time = m.get('LastModifiedStartTime')
        if m.get('LastUpdateTime') is not None:
            self.last_update_time = m.get('LastUpdateTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RealTimeIncr') is not None:
            self.real_time_incr = m.get('RealTimeIncr')
        if m.get('ScanDayList') is not None:
            self.scan_day_list = m.get('ScanDayList')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetOssScanConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: GetOssScanConfigResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetOssScanConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetOssScanConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetOssScanConfigResponseBody = None,
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
            temp_model = GetOssScanConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListObjectScanEventRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        current_page: int = None,
        event_name: str = None,
        lang: str = None,
        md_5: str = None,
        oss_key: str = None,
        page_size: int = None,
        parent_event_id: int = None,
        risk_level: str = None,
        source: str = None,
        time_end: int = None,
        time_start: int = None,
    ):
        self.bucket_name = bucket_name
        # This parameter is required.
        self.current_page = current_page
        self.event_name = event_name
        self.lang = lang
        self.md_5 = md_5
        self.oss_key = oss_key
        # This parameter is required.
        self.page_size = page_size
        self.parent_event_id = parent_event_id
        self.risk_level = risk_level
        self.source = source
        self.time_end = time_end
        self.time_start = time_start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.parent_event_id is not None:
            result['ParentEventId'] = self.parent_event_id
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.source is not None:
            result['Source'] = self.source
        if self.time_end is not None:
            result['TimeEnd'] = self.time_end
        if self.time_start is not None:
            result['TimeStart'] = self.time_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ParentEventId') is not None:
            self.parent_event_id = m.get('ParentEventId')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TimeEnd') is not None:
            self.time_end = m.get('TimeEnd')
        if m.get('TimeStart') is not None:
            self.time_start = m.get('TimeStart')
        return self


class ListObjectScanEventResponseBodyDataDetails(TeaModel):
    def __init__(
        self,
        name: str = None,
        name_display: str = None,
        type: str = None,
        value: str = None,
        value_display: str = None,
    ):
        self.name = name
        self.name_display = name_display
        self.type = type
        self.value = value
        self.value_display = value_display

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.name_display is not None:
            result['NameDisplay'] = self.name_display
        if self.type is not None:
            result['Type'] = self.type
        if self.value is not None:
            result['Value'] = self.value
        if self.value_display is not None:
            result['ValueDisplay'] = self.value_display
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NameDisplay') is not None:
            self.name_display = m.get('NameDisplay')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('ValueDisplay') is not None:
            self.value_display = m.get('ValueDisplay')
        return self


class ListObjectScanEventResponseBodyData(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        details: List[ListObjectScanEventResponseBodyDataDetails] = None,
        display_sandbox_result: str = None,
        event_id: int = None,
        event_name: str = None,
        file_path: str = None,
        first_time: int = None,
        has_sub_event: bool = None,
        last_time: int = None,
        md_5: str = None,
        oss_key: str = None,
        risk_level: str = None,
        sha_1: str = None,
        sha_256: str = None,
        source: str = None,
    ):
        self.bucket_name = bucket_name
        self.details = details
        self.display_sandbox_result = display_sandbox_result
        self.event_id = event_id
        self.event_name = event_name
        self.file_path = file_path
        self.first_time = first_time
        self.has_sub_event = has_sub_event
        self.last_time = last_time
        self.md_5 = md_5
        self.oss_key = oss_key
        self.risk_level = risk_level
        self.sha_1 = sha_1
        self.sha_256 = sha_256
        self.source = source

    def validate(self):
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        result['Details'] = []
        if self.details is not None:
            for k in self.details:
                result['Details'].append(k.to_map() if k else None)
        if self.display_sandbox_result is not None:
            result['DisplaySandboxResult'] = self.display_sandbox_result
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_name is not None:
            result['EventName'] = self.event_name
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.first_time is not None:
            result['FirstTime'] = self.first_time
        if self.has_sub_event is not None:
            result['HasSubEvent'] = self.has_sub_event
        if self.last_time is not None:
            result['LastTime'] = self.last_time
        if self.md_5 is not None:
            result['Md5'] = self.md_5
        if self.oss_key is not None:
            result['OssKey'] = self.oss_key
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level
        if self.sha_1 is not None:
            result['Sha1'] = self.sha_1
        if self.sha_256 is not None:
            result['Sha256'] = self.sha_256
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        self.details = []
        if m.get('Details') is not None:
            for k in m.get('Details'):
                temp_model = ListObjectScanEventResponseBodyDataDetails()
                self.details.append(temp_model.from_map(k))
        if m.get('DisplaySandboxResult') is not None:
            self.display_sandbox_result = m.get('DisplaySandboxResult')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('FirstTime') is not None:
            self.first_time = m.get('FirstTime')
        if m.get('HasSubEvent') is not None:
            self.has_sub_event = m.get('HasSubEvent')
        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')
        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')
        if m.get('OssKey') is not None:
            self.oss_key = m.get('OssKey')
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')
        if m.get('Sha1') is not None:
            self.sha_1 = m.get('Sha1')
        if m.get('Sha256') is not None:
            self.sha_256 = m.get('Sha256')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListObjectScanEventResponseBodyPageInfo(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListObjectScanEventResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListObjectScanEventResponseBodyData] = None,
        page_info: ListObjectScanEventResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.data = data
        self.page_info = page_info
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListObjectScanEventResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageInfo') is not None:
            temp_model = ListObjectScanEventResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListObjectScanEventResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListObjectScanEventResponseBody = None,
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
            temp_model = ListObjectScanEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOssBucketRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        lang: str = None,
    ):
        self.bucket_name = bucket_name
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class ListOssBucketResponseBodyData(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        message: str = None,
        region_id: str = None,
        storage_class: str = None,
        support: bool = None,
    ):
        self.bucket_name = bucket_name
        self.message = message
        self.region_id = region_id
        self.storage_class = storage_class
        self.support = support

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.message is not None:
            result['Message'] = self.message
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        if self.support is not None:
            result['Support'] = self.support
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        if m.get('Support') is not None:
            self.support = m.get('Support')
        return self


class ListOssBucketResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListOssBucketResponseBodyData] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListOssBucketResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListOssBucketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOssBucketResponseBody = None,
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
            temp_model = ListOssBucketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOssBucketScanInfoRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        current_page: int = None,
        fuzz_bucket_name: str = None,
        has_risk: int = None,
        lang: str = None,
        page_size: int = None,
        status: int = None,
    ):
        self.bucket_name = bucket_name
        # This parameter is required.
        self.current_page = current_page
        self.fuzz_bucket_name = fuzz_bucket_name
        self.has_risk = has_risk
        self.lang = lang
        # This parameter is required.
        self.page_size = page_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.fuzz_bucket_name is not None:
            result['FuzzBucketName'] = self.fuzz_bucket_name
        if self.has_risk is not None:
            result['HasRisk'] = self.has_risk
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('FuzzBucketName') is not None:
            self.fuzz_bucket_name = m.get('FuzzBucketName')
        if m.get('HasRisk') is not None:
            self.has_risk = m.get('HasRisk')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListOssBucketScanInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        config_status: int = None,
        decompress_status: int = None,
        high_risk: int = None,
        last_scan_end_time: int = None,
        last_scan_time: int = None,
        low_risk: int = None,
        medium_risk: int = None,
        message: str = None,
        region_id: str = None,
        scan_object: int = None,
        scanned: bool = None,
        status: int = None,
        storage_class: str = None,
        support: bool = None,
        total_object: int = None,
    ):
        self.bucket_name = bucket_name
        self.config_status = config_status
        self.decompress_status = decompress_status
        self.high_risk = high_risk
        self.last_scan_end_time = last_scan_end_time
        self.last_scan_time = last_scan_time
        self.low_risk = low_risk
        self.medium_risk = medium_risk
        self.message = message
        self.region_id = region_id
        self.scan_object = scan_object
        self.scanned = scanned
        self.status = status
        self.storage_class = storage_class
        self.support = support
        self.total_object = total_object

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.config_status is not None:
            result['ConfigStatus'] = self.config_status
        if self.decompress_status is not None:
            result['DecompressStatus'] = self.decompress_status
        if self.high_risk is not None:
            result['HighRisk'] = self.high_risk
        if self.last_scan_end_time is not None:
            result['LastScanEndTime'] = self.last_scan_end_time
        if self.last_scan_time is not None:
            result['LastScanTime'] = self.last_scan_time
        if self.low_risk is not None:
            result['LowRisk'] = self.low_risk
        if self.medium_risk is not None:
            result['MediumRisk'] = self.medium_risk
        if self.message is not None:
            result['Message'] = self.message
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scan_object is not None:
            result['ScanObject'] = self.scan_object
        if self.scanned is not None:
            result['Scanned'] = self.scanned
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_class is not None:
            result['StorageClass'] = self.storage_class
        if self.support is not None:
            result['Support'] = self.support
        if self.total_object is not None:
            result['TotalObject'] = self.total_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('ConfigStatus') is not None:
            self.config_status = m.get('ConfigStatus')
        if m.get('DecompressStatus') is not None:
            self.decompress_status = m.get('DecompressStatus')
        if m.get('HighRisk') is not None:
            self.high_risk = m.get('HighRisk')
        if m.get('LastScanEndTime') is not None:
            self.last_scan_end_time = m.get('LastScanEndTime')
        if m.get('LastScanTime') is not None:
            self.last_scan_time = m.get('LastScanTime')
        if m.get('LowRisk') is not None:
            self.low_risk = m.get('LowRisk')
        if m.get('MediumRisk') is not None:
            self.medium_risk = m.get('MediumRisk')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ScanObject') is not None:
            self.scan_object = m.get('ScanObject')
        if m.get('Scanned') is not None:
            self.scanned = m.get('Scanned')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageClass') is not None:
            self.storage_class = m.get('StorageClass')
        if m.get('Support') is not None:
            self.support = m.get('Support')
        if m.get('TotalObject') is not None:
            self.total_object = m.get('TotalObject')
        return self


class ListOssBucketScanInfoResponseBodyPageInfo(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListOssBucketScanInfoResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListOssBucketScanInfoResponseBodyData] = None,
        page_info: ListOssBucketScanInfoResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.data = data
        self.page_info = page_info
        self.request_id = request_id

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListOssBucketScanInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageInfo') is not None:
            temp_model = ListOssBucketScanInfoResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['PageInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListOssBucketScanInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOssBucketScanInfoResponseBody = None,
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
            temp_model = ListOssBucketScanInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSupportObjectSuffixResponseBody(TeaModel):
    def __init__(
        self,
        data: List[str] = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListSupportObjectSuffixResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSupportObjectSuffixResponseBody = None,
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
            temp_model = ListSupportObjectSuffixResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateBucketScanTaskRequest(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        operate_code: int = None,
    ):
        self.bucket_name = bucket_name
        self.operate_code = operate_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.operate_code is not None:
            result['OperateCode'] = self.operate_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('OperateCode') is not None:
            self.operate_code = m.get('OperateCode')
        return self


class OperateBucketScanTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OperateBucketScanTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OperateBucketScanTaskResponseBody = None,
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
            temp_model = OperateBucketScanTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateOssScanConfigRequest(TeaModel):
    def __init__(
        self,
        all_key_prefix: str = None,
        bucket_name: str = None,
        decompress_max_file_count: int = None,
        decompress_max_layer: int = None,
        decryption_list: List[str] = None,
        enable: int = None,
        end_time: str = None,
        id: str = None,
        key_prefix_list: List[str] = None,
        key_suffix_list: List[str] = None,
        last_modified_start_time: int = None,
        name: str = None,
        real_time_incr: bool = None,
        scan_day_list: List[int] = None,
        start_time: str = None,
    ):
        self.all_key_prefix = all_key_prefix
        self.bucket_name = bucket_name
        self.decompress_max_file_count = decompress_max_file_count
        self.decompress_max_layer = decompress_max_layer
        self.decryption_list = decryption_list
        self.enable = enable
        self.end_time = end_time
        self.id = id
        self.key_prefix_list = key_prefix_list
        self.key_suffix_list = key_suffix_list
        self.last_modified_start_time = last_modified_start_time
        self.name = name
        self.real_time_incr = real_time_incr
        self.scan_day_list = scan_day_list
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_key_prefix is not None:
            result['AllKeyPrefix'] = self.all_key_prefix
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.decompress_max_file_count is not None:
            result['DecompressMaxFileCount'] = self.decompress_max_file_count
        if self.decompress_max_layer is not None:
            result['DecompressMaxLayer'] = self.decompress_max_layer
        if self.decryption_list is not None:
            result['DecryptionList'] = self.decryption_list
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.id is not None:
            result['Id'] = self.id
        if self.key_prefix_list is not None:
            result['KeyPrefixList'] = self.key_prefix_list
        if self.key_suffix_list is not None:
            result['KeySuffixList'] = self.key_suffix_list
        if self.last_modified_start_time is not None:
            result['LastModifiedStartTime'] = self.last_modified_start_time
        if self.name is not None:
            result['Name'] = self.name
        if self.real_time_incr is not None:
            result['RealTimeIncr'] = self.real_time_incr
        if self.scan_day_list is not None:
            result['ScanDayList'] = self.scan_day_list
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllKeyPrefix') is not None:
            self.all_key_prefix = m.get('AllKeyPrefix')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('DecompressMaxFileCount') is not None:
            self.decompress_max_file_count = m.get('DecompressMaxFileCount')
        if m.get('DecompressMaxLayer') is not None:
            self.decompress_max_layer = m.get('DecompressMaxLayer')
        if m.get('DecryptionList') is not None:
            self.decryption_list = m.get('DecryptionList')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('KeyPrefixList') is not None:
            self.key_prefix_list = m.get('KeyPrefixList')
        if m.get('KeySuffixList') is not None:
            self.key_suffix_list = m.get('KeySuffixList')
        if m.get('LastModifiedStartTime') is not None:
            self.last_modified_start_time = m.get('LastModifiedStartTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RealTimeIncr') is not None:
            self.real_time_incr = m.get('RealTimeIncr')
        if m.get('ScanDayList') is not None:
            self.scan_day_list = m.get('ScanDayList')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class UpdateOssScanConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateOssScanConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateOssScanConfigResponseBody = None,
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
            temp_model = UpdateOssScanConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


