# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeSuspEventQuaraFilesResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        quara_files: List[main_models.DescribeSuspEventQuaraFilesResponseBodyQuaraFiles] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # An array that consists of the quarantined files.
        self.quara_files = quara_files
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.quara_files:
            for v1 in self.quara_files:
                 if v1:
                    v1.validate()

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

        result['QuaraFiles'] = []
        if self.quara_files is not None:
            for k1 in self.quara_files:
                result['QuaraFiles'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        self.quara_files = []
        if m.get('QuaraFiles') is not None:
            for k1 in m.get('QuaraFiles'):
                temp_model = main_models.DescribeSuspEventQuaraFilesResponseBodyQuaraFiles()
                self.quara_files.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSuspEventQuaraFilesResponseBodyQuaraFiles(DaraModel):
    def __init__(
        self,
        event_name: str = None,
        event_type: str = None,
        id: int = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        ip: str = None,
        link: str = None,
        md_5: str = None,
        modify_time: str = None,
        path: str = None,
        status: str = None,
        tag: str = None,
        uuid: str = None,
    ):
        # The name of the event.
        self.event_name = event_name
        # The type of the event.
        self.event_type = event_type
        # The ID of the quarantined file.
        self.id = id
        # The instance ID of the asset.
        self.instance_id = instance_id
        # The name of the server on which the quarantined file is located.
        self.instance_name = instance_name
        # The public IP address of the server on which the quarantined file is located.
        self.internet_ip = internet_ip
        # The private IP address of the server on which the quarantined file is located.
        self.intranet_ip = intranet_ip
        # The public IP address of the server on which the quarantined file is located.
        self.ip = ip
        # The download link of the quarantined file.
        self.link = link
        # The MD5 hash value of the quarantined file.
        self.md_5 = md_5
        # The time when the quarantined file was last modified.
        self.modify_time = modify_time
        # The path to the quarantined file on the server.
        self.path = path
        # The status of the quarantined file. Valid values:
        # 
        # *   **quaraFailed**: The file fails to be quarantined.
        # *   **quaraDone**: The file is quarantined.
        # *   **quaraing**: The file is being quarantined.
        # *   **rollbackFailed**: The system fails to cancel quarantining the file.
        # *   **rollbackDone**: The system cancelled quarantining the file.
        # *   **rollbacking**: The system is cancelling quarantining the file.
        self.status = status
        # The unique ID of the event.
        self.tag = tag
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.link is not None:
            result['Link'] = self.link

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.path is not None:
            result['Path'] = self.path

        if self.status is not None:
            result['Status'] = self.status

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Link') is not None:
            self.link = m.get('Link')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

