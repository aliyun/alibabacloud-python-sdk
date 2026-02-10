# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeAgentlessSensitiveFileByKeyResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.DescribeAgentlessSensitiveFileByKeyResponseBodyPageInfo = None,
        request_id: str = None,
        sensitive_file_list: List[main_models.DescribeAgentlessSensitiveFileByKeyResponseBodySensitiveFileList] = None,
        success: bool = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id
        # The information about the sensitive files that are detected by using the agentless detection feature.
        self.sensitive_file_list = sensitive_file_list
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.sensitive_file_list:
            for v1 in self.sensitive_file_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SensitiveFileList'] = []
        if self.sensitive_file_list is not None:
            for k1 in self.sensitive_file_list:
                result['SensitiveFileList'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeAgentlessSensitiveFileByKeyResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.sensitive_file_list = []
        if m.get('SensitiveFileList') is not None:
            for k1 in m.get('SensitiveFileList'):
                temp_model = main_models.DescribeAgentlessSensitiveFileByKeyResponseBodySensitiveFileList()
                self.sensitive_file_list.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeAgentlessSensitiveFileByKeyResponseBodySensitiveFileList(DaraModel):
    def __init__(
        self,
        file_path: str = None,
        first_scan_time: int = None,
        id: int = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        last_scan_time: int = None,
        md_5: str = None,
        prompt: str = None,
        risk_level: str = None,
        sensitive_file_key: str = None,
        status: int = None,
        target_name: str = None,
        uuid: str = None,
    ):
        # The path to the sensitive file.
        self.file_path = file_path
        # The timestamp when the first scan was performed. Unit: milliseconds.
        self.first_scan_time = first_scan_time
        # The ID of the alert for the sensitive file.
        self.id = id
        # The instance name of the asset.
        self.instance_name = instance_name
        # The public IP address of the asset.
        self.internet_ip = internet_ip
        # The private IP address of the asset.
        self.intranet_ip = intranet_ip
        # The timestamp when the last scan was performed. Unit: milliseconds.
        self.last_scan_time = last_scan_time
        # The MD5 hash value of the sensitive file.
        self.md_5 = md_5
        # The content of the sensitive file.
        self.prompt = prompt
        # The risk level. Valid values:
        # 
        # *   **high**
        # *   **medium**
        # *   **low**
        self.risk_level = risk_level
        # The type of the sensitive file.
        self.sensitive_file_key = sensitive_file_key
        # The status of the sensitive file. Valid values:
        # 
        # *   **0**: unhandled.
        # *   **1**: ignored.
        # *   **2**: false positive.
        self.status = status
        # The name of the asset.
        self.target_name = target_name
        # The UUID of the asset.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.first_scan_time is not None:
            result['FirstScanTime'] = self.first_scan_time

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.last_scan_time is not None:
            result['LastScanTime'] = self.last_scan_time

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.sensitive_file_key is not None:
            result['SensitiveFileKey'] = self.sensitive_file_key

        if self.status is not None:
            result['Status'] = self.status

        if self.target_name is not None:
            result['TargetName'] = self.target_name

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('FirstScanTime') is not None:
            self.first_scan_time = m.get('FirstScanTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('LastScanTime') is not None:
            self.last_scan_time = m.get('LastScanTime')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('SensitiveFileKey') is not None:
            self.sensitive_file_key = m.get('SensitiveFileKey')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class DescribeAgentlessSensitiveFileByKeyResponseBodyPageInfo(DaraModel):
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

