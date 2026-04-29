# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListUnknownThreatDetectMachineResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListUnknownThreatDetectMachineResponseBodyData] = None,
        page_info: main_models.ListUnknownThreatDetectMachineResponseBodyPageInfo = None,
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
                temp_model = main_models.ListUnknownThreatDetectMachineResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListUnknownThreatDetectMachineResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListUnknownThreatDetectMachineResponseBodyPageInfo(DaraModel):
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

class ListUnknownThreatDetectMachineResponseBodyData(DaraModel):
    def __init__(
        self,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        process_count: int = None,
        status: str = None,
        study_mode: str = None,
        study_start_time: int = None,
        uuid: str = None,
    ):
        self.instance_name = instance_name
        self.internet_ip = internet_ip
        self.intranet_ip = intranet_ip
        self.process_count = process_count
        self.status = status
        self.study_mode = study_mode
        self.study_start_time = study_start_time
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.process_count is not None:
            result['ProcessCount'] = self.process_count

        if self.status is not None:
            result['Status'] = self.status

        if self.study_mode is not None:
            result['StudyMode'] = self.study_mode

        if self.study_start_time is not None:
            result['StudyStartTime'] = self.study_start_time

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('ProcessCount') is not None:
            self.process_count = m.get('ProcessCount')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StudyMode') is not None:
            self.study_mode = m.get('StudyMode')

        if m.get('StudyStartTime') is not None:
            self.study_start_time = m.get('StudyStartTime')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

