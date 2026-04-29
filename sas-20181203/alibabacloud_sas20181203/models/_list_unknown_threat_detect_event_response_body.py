# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListUnknownThreatDetectEventResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListUnknownThreatDetectEventResponseBodyData] = None,
        page_info: main_models.ListUnknownThreatDetectEventResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.data = data
        self.page_info = page_info
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListUnknownThreatDetectEventResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListUnknownThreatDetectEventResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListUnknownThreatDetectEventResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.count = count
        self.current_page = current_page
        self.page_size = page_size
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

class ListUnknownThreatDetectEventResponseBodyData(DaraModel):
    def __init__(
        self,
        cmd_chain: str = None,
        cmdline: str = None,
        count: int = None,
        first_time: int = None,
        hash_key: str = None,
        id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        last_time: int = None,
        md_5: str = None,
        parent_cmdline: str = None,
        parent_pid: str = None,
        parent_process_path: str = None,
        pid: str = None,
        process_path: str = None,
        sha_256: str = None,
        status: int = None,
        uuid: str = None,
    ):
        self.cmd_chain = cmd_chain
        self.cmdline = cmdline
        self.count = count
        self.first_time = first_time
        self.hash_key = hash_key
        self.id = id
        self.instance_name = instance_name
        self.internet_ip = internet_ip
        self.intranet_ip = intranet_ip
        self.last_time = last_time
        self.md_5 = md_5
        self.parent_cmdline = parent_cmdline
        self.parent_pid = parent_pid
        self.parent_process_path = parent_process_path
        self.pid = pid
        self.process_path = process_path
        self.sha_256 = sha_256
        self.status = status
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cmd_chain is not None:
            result['CmdChain'] = self.cmd_chain

        if self.cmdline is not None:
            result['Cmdline'] = self.cmdline

        if self.count is not None:
            result['Count'] = self.count

        if self.first_time is not None:
            result['FirstTime'] = self.first_time

        if self.hash_key is not None:
            result['HashKey'] = self.hash_key

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.last_time is not None:
            result['LastTime'] = self.last_time

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.parent_cmdline is not None:
            result['ParentCmdline'] = self.parent_cmdline

        if self.parent_pid is not None:
            result['ParentPid'] = self.parent_pid

        if self.parent_process_path is not None:
            result['ParentProcessPath'] = self.parent_process_path

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.process_path is not None:
            result['ProcessPath'] = self.process_path

        if self.sha_256 is not None:
            result['Sha256'] = self.sha_256

        if self.status is not None:
            result['Status'] = self.status

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CmdChain') is not None:
            self.cmd_chain = m.get('CmdChain')

        if m.get('Cmdline') is not None:
            self.cmdline = m.get('Cmdline')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('FirstTime') is not None:
            self.first_time = m.get('FirstTime')

        if m.get('HashKey') is not None:
            self.hash_key = m.get('HashKey')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('ParentCmdline') is not None:
            self.parent_cmdline = m.get('ParentCmdline')

        if m.get('ParentPid') is not None:
            self.parent_pid = m.get('ParentPid')

        if m.get('ParentProcessPath') is not None:
            self.parent_process_path = m.get('ParentProcessPath')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('ProcessPath') is not None:
            self.process_path = m.get('ProcessPath')

        if m.get('Sha256') is not None:
            self.sha_256 = m.get('Sha256')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

