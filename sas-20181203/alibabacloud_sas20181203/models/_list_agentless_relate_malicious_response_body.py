# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListAgentlessRelateMaliciousResponseBody(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListAgentlessRelateMaliciousResponseBodyList] = None,
        page_info: main_models.ListAgentlessRelateMaliciousResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The list of hosts that are associated with the risk.
        self.list = list
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.ListAgentlessRelateMaliciousResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListAgentlessRelateMaliciousResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAgentlessRelateMaliciousResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
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

class ListAgentlessRelateMaliciousResponseBodyList(DaraModel):
    def __init__(
        self,
        details: List[main_models.ListAgentlessRelateMaliciousResponseBodyListDetails] = None,
        download_url: str = None,
        file_path: str = None,
        first_scan_timestamp: int = None,
        high_light: str = None,
        id: int = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        latest_scan_timestamp: int = None,
        level: str = None,
        malicious_md_5: str = None,
        malicious_name: str = None,
        malicious_type: str = None,
        operate_result: str = None,
        operate_timestamp: str = None,
        partition: str = None,
        target_id: str = None,
        target_name: str = None,
        target_type: str = None,
        uuid: str = None,
    ):
        # The details of the alert events.
        self.details = details
        # The URL to download the malicious image sample.
        self.download_url = download_url
        # The file path.
        self.file_path = file_path
        # The timestamp when the first scan was performed. Unit: milliseconds.
        self.first_scan_timestamp = first_scan_timestamp
        # The highlighted JSON string.
        self.high_light = high_light
        # The event ID.
        self.id = id
        # The name of the asset.
        self.instance_name = instance_name
        # The public IP address of the server.
        self.internet_ip = internet_ip
        # The private IP address of the server.
        self.intranet_ip = intranet_ip
        # The timestamp when the last scan was performed. Unit: milliseconds.
        self.latest_scan_timestamp = latest_scan_timestamp
        # The severity of the malicious file. Valid values:
        # 
        # *   serious
        # *   suspicious
        # *   remind
        self.level = level
        # The MD5 hash value of the malicious file.
        self.malicious_md_5 = malicious_md_5
        # The name of the malicious file.
        self.malicious_name = malicious_name
        # The type of the virus.
        self.malicious_type = malicious_type
        # The handling result of the alert.
        self.operate_result = operate_result
        # The timestamp when the alert is handled. Unit: milliseconds.
        self.operate_timestamp = operate_timestamp
        # The partition of the disk.
        self.partition = partition
        # The ID of the task object.
        self.target_id = target_id
        # The name of the task object.
        self.target_name = target_name
        # The type of the task object. Valid values:
        # 
        # *   **1**: snapshot.
        # *   **2**: image.
        self.target_type = target_type
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        if self.details:
            for v1 in self.details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Details'] = []
        if self.details is not None:
            for k1 in self.details:
                result['Details'].append(k1.to_map() if k1 else None)

        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.first_scan_timestamp is not None:
            result['FirstScanTimestamp'] = self.first_scan_timestamp

        if self.high_light is not None:
            result['HighLight'] = self.high_light

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.latest_scan_timestamp is not None:
            result['LatestScanTimestamp'] = self.latest_scan_timestamp

        if self.level is not None:
            result['Level'] = self.level

        if self.malicious_md_5 is not None:
            result['MaliciousMd5'] = self.malicious_md_5

        if self.malicious_name is not None:
            result['MaliciousName'] = self.malicious_name

        if self.malicious_type is not None:
            result['MaliciousType'] = self.malicious_type

        if self.operate_result is not None:
            result['OperateResult'] = self.operate_result

        if self.operate_timestamp is not None:
            result['OperateTimestamp'] = self.operate_timestamp

        if self.partition is not None:
            result['Partition'] = self.partition

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_name is not None:
            result['TargetName'] = self.target_name

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.details = []
        if m.get('Details') is not None:
            for k1 in m.get('Details'):
                temp_model = main_models.ListAgentlessRelateMaliciousResponseBodyListDetails()
                self.details.append(temp_model.from_map(k1))

        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('FirstScanTimestamp') is not None:
            self.first_scan_timestamp = m.get('FirstScanTimestamp')

        if m.get('HighLight') is not None:
            self.high_light = m.get('HighLight')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('LatestScanTimestamp') is not None:
            self.latest_scan_timestamp = m.get('LatestScanTimestamp')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('MaliciousMd5') is not None:
            self.malicious_md_5 = m.get('MaliciousMd5')

        if m.get('MaliciousName') is not None:
            self.malicious_name = m.get('MaliciousName')

        if m.get('MaliciousType') is not None:
            self.malicious_type = m.get('MaliciousType')

        if m.get('OperateResult') is not None:
            self.operate_result = m.get('OperateResult')

        if m.get('OperateTimestamp') is not None:
            self.operate_timestamp = m.get('OperateTimestamp')

        if m.get('Partition') is not None:
            self.partition = m.get('Partition')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class ListAgentlessRelateMaliciousResponseBodyListDetails(DaraModel):
    def __init__(
        self,
        name: str = None,
        name_key: str = None,
        type: str = None,
        value: str = None,
    ):
        # The name of the detailed item.
        self.name = name
        # The name key of the detailed item.
        self.name_key = name_key
        # The type of the detailed item.
        self.type = type
        # The value of the detailed item.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.name_key is not None:
            result['NameKey'] = self.name_key

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NameKey') is not None:
            self.name_key = m.get('NameKey')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

