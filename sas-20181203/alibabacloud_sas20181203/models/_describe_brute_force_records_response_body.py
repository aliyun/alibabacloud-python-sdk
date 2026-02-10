# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeBruteForceRecordsResponseBody(DaraModel):
    def __init__(
        self,
        machine_list: List[main_models.DescribeBruteForceRecordsResponseBodyMachineList] = None,
        page_info: main_models.DescribeBruteForceRecordsResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The IP addresses.
        self.machine_list = machine_list
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.machine_list:
            for v1 in self.machine_list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MachineList'] = []
        if self.machine_list is not None:
            for k1 in self.machine_list:
                result['MachineList'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.machine_list = []
        if m.get('MachineList') is not None:
            for k1 in m.get('MachineList'):
                temp_model = main_models.DescribeBruteForceRecordsResponseBodyMachineList()
                self.machine_list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeBruteForceRecordsResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeBruteForceRecordsResponseBodyPageInfo(DaraModel):
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
        # The number of entries returned per page. Default value: **20**.
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

class DescribeBruteForceRecordsResponseBodyMachineList(DaraModel):
    def __init__(
        self,
        ali_net_online: bool = None,
        block_expire_date: int = None,
        block_ip: str = None,
        block_type: str = None,
        error_code: str = None,
        id: int = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        port: str = None,
        rule_name: str = None,
        source: str = None,
        status: int = None,
        uuid: str = None,
    ):
        # The status of the host network extension. Valid values:
        # 
        # *   **true**: online
        # *   **false**: offline
        self.ali_net_online = ali_net_online
        # The timestamp when the block action on the IP address becomes invalid.
        self.block_expire_date = block_expire_date
        # The IP address that is blocked.
        self.block_ip = block_ip
        # The blocking type. Valid values:
        # 
        # *   **group**: security group
        # *   **alinet**: host network extension
        self.block_type = block_type
        # The error code returned when the defense rule fails to block the IP address.
        self.error_code = error_code
        # The ID of the primary key that is recorded in the defense rule.
        self.id = id
        # The instance name of the server.
        self.instance_name = instance_name
        # The public IP address.
        self.internet_ip = internet_ip
        # The private IP address.
        self.intranet_ip = intranet_ip
        # The port that is attacked.
        self.port = port
        # The name of the defense rule.
        self.rule_name = rule_name
        # The type of the defense rule. Valid values:
        # 
        # *   **userRule**: custom rule
        # *   **blinkRule**: system rule
        self.source = source
        # The status of the defense rule. Valid values:
        # 
        # *   **0**: invalid
        # *   **1**: enabled
        # *   **2**: failed
        self.status = status
        # The UUID of the server on which the defense rule takes effect.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_net_online is not None:
            result['AliNetOnline'] = self.ali_net_online

        if self.block_expire_date is not None:
            result['BlockExpireDate'] = self.block_expire_date

        if self.block_ip is not None:
            result['BlockIp'] = self.block_ip

        if self.block_type is not None:
            result['BlockType'] = self.block_type

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.port is not None:
            result['Port'] = self.port

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliNetOnline') is not None:
            self.ali_net_online = m.get('AliNetOnline')

        if m.get('BlockExpireDate') is not None:
            self.block_expire_date = m.get('BlockExpireDate')

        if m.get('BlockIp') is not None:
            self.block_ip = m.get('BlockIp')

        if m.get('BlockType') is not None:
            self.block_type = m.get('BlockType')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

