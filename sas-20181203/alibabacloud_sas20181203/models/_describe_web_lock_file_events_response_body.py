# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeWebLockFileEventsResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        list: List[main_models.DescribeWebLockFileEventsResponseBodyList] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # An array that consists of events on web tamper proofing returned.
        self.list = list
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of events on web tamper proofing returned.
        self.total_count = total_count

    def validate(self):
        if self.list:
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.DescribeWebLockFileEventsResponseBodyList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeWebLockFileEventsResponseBodyList(DaraModel):
    def __init__(
        self,
        count: int = None,
        ds: int = None,
        event_name: str = None,
        event_status: str = None,
        event_type: str = None,
        gmt_event: int = None,
        id: int = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        ip: str = None,
        level: str = None,
        path: str = None,
        process_name: str = None,
        process_path: str = None,
        status: str = None,
        uuid: str = None,
    ):
        # The number of attempts.
        self.count = count
        # The timestamp at which the event on web tamper proofing was first detected.
        self.ds = ds
        # The name of the event on web tamper proofing.
        self.event_name = event_name
        # The status of the event on web tamper proofing. Valid values:
        # 
        # *   **1**: unhandled
        # *   **2**: ignored
        # *   **4**: deprecated
        # *   **8**: marked as false positive
        # *   **10**: added to the whitelist
        # *   **16**: handling
        # *   **32**: defended
        # *   **64**: invalid
        # *   **128**: deleted
        # *   **512**: automatically handled
        self.event_status = event_status
        # The prevention mode. Valid values:
        # 
        # *   **audit**: Interception Mode
        # *   **web_lock**: Alert Mode
        self.event_type = event_type
        # The timestamp at which the event on web tamper proofing was last detected.
        self.gmt_event = gmt_event
        # The ID of the event on web tamper proofing.
        self.id = id
        # The name of the asset.
        self.instance_name = instance_name
        # The public IP address of the affected asset.
        self.internet_ip = internet_ip
        # The private IP address of the asset.
        self.intranet_ip = intranet_ip
        # The IP address of the asset.
        self.ip = ip
        # The severity of the event on web tamper proofing. Valid values: **medium**
        self.level = level
        # The file path.
        self.path = path
        # The name of the process.
        self.process_name = process_name
        # The path to the process.
        self.process_path = process_path
        # The status of the event on web tamper proofing. Valid values:
        # 
        # *   **1**: unhandled
        # *   **2**: ignored
        # *   **4**: deprecated
        # *   **8**: marked as false positive
        # *   **10**: added to the whitelist
        # *   **16**: handling
        # *   **32**: defended
        # *   **64**: invalid
        # *   **128**: deleted
        # *   **512**: automatically handled
        self.status = status
        # The UUID of the asset.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.ds is not None:
            result['Ds'] = self.ds

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.event_status is not None:
            result['EventStatus'] = self.event_status

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.gmt_event is not None:
            result['GmtEvent'] = self.gmt_event

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.level is not None:
            result['Level'] = self.level

        if self.path is not None:
            result['Path'] = self.path

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        if self.process_path is not None:
            result['ProcessPath'] = self.process_path

        if self.status is not None:
            result['Status'] = self.status

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Ds') is not None:
            self.ds = m.get('Ds')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('EventStatus') is not None:
            self.event_status = m.get('EventStatus')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('GmtEvent') is not None:
            self.gmt_event = m.get('GmtEvent')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        if m.get('ProcessPath') is not None:
            self.process_path = m.get('ProcessPath')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

