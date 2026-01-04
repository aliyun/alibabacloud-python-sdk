# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeNCInformationResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        data: List[main_models.DescribeNCInformationResponseBodyData] = None,
        desc: str = None,
        msg: str = None,
        pager: main_models.DescribeNCInformationResponseBodyPager = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.data = data
        self.desc = desc
        self.msg = msg
        self.pager = pager
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.pager:
            self.pager.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.pager is not None:
            result['Pager'] = self.pager.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeNCInformationResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('Pager') is not None:
            temp_model = main_models.DescribeNCInformationResponseBodyPager()
            self.pager = temp_model.from_map(m.get('Pager'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeNCInformationResponseBodyPager(DaraModel):
    def __init__(
        self,
        page: int = None,
        size: int = None,
        total: int = None,
    ):
        self.page = page
        self.size = size
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page is not None:
            result['Page'] = self.page

        if self.size is not None:
            result['Size'] = self.size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class DescribeNCInformationResponseBodyData(DaraModel):
    def __init__(
        self,
        cpu: main_models.DescribeNCInformationResponseBodyDataCpu = None,
        gpu: main_models.DescribeNCInformationResponseBodyDataGpu = None,
        hdd: main_models.DescribeNCInformationResponseBodyDataHdd = None,
        info: main_models.DescribeNCInformationResponseBodyDataInfo = None,
        memory: main_models.DescribeNCInformationResponseBodyDataMemory = None,
        nvme: main_models.DescribeNCInformationResponseBodyDataNvme = None,
        online: bool = None,
        region: str = None,
        ssd: main_models.DescribeNCInformationResponseBodyDataSsd = None,
        virtual: str = None,
    ):
        self.cpu = cpu
        self.gpu = gpu
        self.hdd = hdd
        self.info = info
        self.memory = memory
        self.nvme = nvme
        self.online = online
        self.region = region
        self.ssd = ssd
        self.virtual = virtual

    def validate(self):
        if self.cpu:
            self.cpu.validate()
        if self.gpu:
            self.gpu.validate()
        if self.hdd:
            self.hdd.validate()
        if self.info:
            self.info.validate()
        if self.memory:
            self.memory.validate()
        if self.nvme:
            self.nvme.validate()
        if self.ssd:
            self.ssd.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu.to_map()

        if self.gpu is not None:
            result['Gpu'] = self.gpu.to_map()

        if self.hdd is not None:
            result['Hdd'] = self.hdd.to_map()

        if self.info is not None:
            result['Info'] = self.info.to_map()

        if self.memory is not None:
            result['Memory'] = self.memory.to_map()

        if self.nvme is not None:
            result['Nvme'] = self.nvme.to_map()

        if self.online is not None:
            result['Online'] = self.online

        if self.region is not None:
            result['Region'] = self.region

        if self.ssd is not None:
            result['Ssd'] = self.ssd.to_map()

        if self.virtual is not None:
            result['Virtual'] = self.virtual

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            temp_model = main_models.DescribeNCInformationResponseBodyDataCpu()
            self.cpu = temp_model.from_map(m.get('Cpu'))

        if m.get('Gpu') is not None:
            temp_model = main_models.DescribeNCInformationResponseBodyDataGpu()
            self.gpu = temp_model.from_map(m.get('Gpu'))

        if m.get('Hdd') is not None:
            temp_model = main_models.DescribeNCInformationResponseBodyDataHdd()
            self.hdd = temp_model.from_map(m.get('Hdd'))

        if m.get('Info') is not None:
            temp_model = main_models.DescribeNCInformationResponseBodyDataInfo()
            self.info = temp_model.from_map(m.get('Info'))

        if m.get('Memory') is not None:
            temp_model = main_models.DescribeNCInformationResponseBodyDataMemory()
            self.memory = temp_model.from_map(m.get('Memory'))

        if m.get('Nvme') is not None:
            temp_model = main_models.DescribeNCInformationResponseBodyDataNvme()
            self.nvme = temp_model.from_map(m.get('Nvme'))

        if m.get('Online') is not None:
            self.online = m.get('Online')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Ssd') is not None:
            temp_model = main_models.DescribeNCInformationResponseBodyDataSsd()
            self.ssd = temp_model.from_map(m.get('Ssd'))

        if m.get('Virtual') is not None:
            self.virtual = m.get('Virtual')

        return self

class DescribeNCInformationResponseBodyDataSsd(DaraModel):
    def __init__(
        self,
        display: bool = None,
        oversell_ratio: int = None,
        remain: int = None,
        reserve_disable: bool = None,
        reserve_disable_total: int = None,
        reserved: int = None,
        status_disable: bool = None,
        status_disable_total: int = None,
        total: int = None,
        type: str = None,
        used: int = None,
        used_ratio: int = None,
    ):
        self.display = display
        self.oversell_ratio = oversell_ratio
        self.remain = remain
        self.reserve_disable = reserve_disable
        self.reserve_disable_total = reserve_disable_total
        self.reserved = reserved
        self.status_disable = status_disable
        self.status_disable_total = status_disable_total
        self.total = total
        self.type = type
        self.used = used
        self.used_ratio = used_ratio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display is not None:
            result['Display'] = self.display

        if self.oversell_ratio is not None:
            result['OversellRatio'] = self.oversell_ratio

        if self.remain is not None:
            result['Remain'] = self.remain

        if self.reserve_disable is not None:
            result['ReserveDisable'] = self.reserve_disable

        if self.reserve_disable_total is not None:
            result['ReserveDisableTotal'] = self.reserve_disable_total

        if self.reserved is not None:
            result['Reserved'] = self.reserved

        if self.status_disable is not None:
            result['StatusDisable'] = self.status_disable

        if self.status_disable_total is not None:
            result['StatusDisableTotal'] = self.status_disable_total

        if self.total is not None:
            result['Total'] = self.total

        if self.type is not None:
            result['Type'] = self.type

        if self.used is not None:
            result['Used'] = self.used

        if self.used_ratio is not None:
            result['UsedRatio'] = self.used_ratio

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('OversellRatio') is not None:
            self.oversell_ratio = m.get('OversellRatio')

        if m.get('Remain') is not None:
            self.remain = m.get('Remain')

        if m.get('ReserveDisable') is not None:
            self.reserve_disable = m.get('ReserveDisable')

        if m.get('ReserveDisableTotal') is not None:
            self.reserve_disable_total = m.get('ReserveDisableTotal')

        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')

        if m.get('StatusDisable') is not None:
            self.status_disable = m.get('StatusDisable')

        if m.get('StatusDisableTotal') is not None:
            self.status_disable_total = m.get('StatusDisableTotal')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Used') is not None:
            self.used = m.get('Used')

        if m.get('UsedRatio') is not None:
            self.used_ratio = m.get('UsedRatio')

        return self

class DescribeNCInformationResponseBodyDataNvme(DaraModel):
    def __init__(
        self,
        display: bool = None,
        oversell_ratio: int = None,
        remain: int = None,
        reserve_disable: bool = None,
        reserve_disable_total: int = None,
        reserved: int = None,
        status_disable: bool = None,
        status_disable_total: int = None,
        total: int = None,
        type: str = None,
        used: int = None,
        used_ratio: int = None,
    ):
        self.display = display
        self.oversell_ratio = oversell_ratio
        self.remain = remain
        self.reserve_disable = reserve_disable
        self.reserve_disable_total = reserve_disable_total
        self.reserved = reserved
        self.status_disable = status_disable
        self.status_disable_total = status_disable_total
        self.total = total
        self.type = type
        self.used = used
        self.used_ratio = used_ratio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display is not None:
            result['Display'] = self.display

        if self.oversell_ratio is not None:
            result['OversellRatio'] = self.oversell_ratio

        if self.remain is not None:
            result['Remain'] = self.remain

        if self.reserve_disable is not None:
            result['ReserveDisable'] = self.reserve_disable

        if self.reserve_disable_total is not None:
            result['ReserveDisableTotal'] = self.reserve_disable_total

        if self.reserved is not None:
            result['Reserved'] = self.reserved

        if self.status_disable is not None:
            result['StatusDisable'] = self.status_disable

        if self.status_disable_total is not None:
            result['StatusDisableTotal'] = self.status_disable_total

        if self.total is not None:
            result['Total'] = self.total

        if self.type is not None:
            result['Type'] = self.type

        if self.used is not None:
            result['Used'] = self.used

        if self.used_ratio is not None:
            result['UsedRatio'] = self.used_ratio

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('OversellRatio') is not None:
            self.oversell_ratio = m.get('OversellRatio')

        if m.get('Remain') is not None:
            self.remain = m.get('Remain')

        if m.get('ReserveDisable') is not None:
            self.reserve_disable = m.get('ReserveDisable')

        if m.get('ReserveDisableTotal') is not None:
            self.reserve_disable_total = m.get('ReserveDisableTotal')

        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')

        if m.get('StatusDisable') is not None:
            self.status_disable = m.get('StatusDisable')

        if m.get('StatusDisableTotal') is not None:
            self.status_disable_total = m.get('StatusDisableTotal')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Used') is not None:
            self.used = m.get('Used')

        if m.get('UsedRatio') is not None:
            self.used_ratio = m.get('UsedRatio')

        return self

class DescribeNCInformationResponseBodyDataMemory(DaraModel):
    def __init__(
        self,
        display: bool = None,
        oversell_ratio: int = None,
        remain: int = None,
        reserve_disable: bool = None,
        reserve_disable_total: int = None,
        reserved: int = None,
        status_disable: bool = None,
        status_disable_total: int = None,
        total: int = None,
        type: str = None,
        used: int = None,
        used_ratio: int = None,
    ):
        self.display = display
        self.oversell_ratio = oversell_ratio
        self.remain = remain
        self.reserve_disable = reserve_disable
        self.reserve_disable_total = reserve_disable_total
        self.reserved = reserved
        self.status_disable = status_disable
        self.status_disable_total = status_disable_total
        self.total = total
        self.type = type
        self.used = used
        self.used_ratio = used_ratio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display is not None:
            result['Display'] = self.display

        if self.oversell_ratio is not None:
            result['OversellRatio'] = self.oversell_ratio

        if self.remain is not None:
            result['Remain'] = self.remain

        if self.reserve_disable is not None:
            result['ReserveDisable'] = self.reserve_disable

        if self.reserve_disable_total is not None:
            result['ReserveDisableTotal'] = self.reserve_disable_total

        if self.reserved is not None:
            result['Reserved'] = self.reserved

        if self.status_disable is not None:
            result['StatusDisable'] = self.status_disable

        if self.status_disable_total is not None:
            result['StatusDisableTotal'] = self.status_disable_total

        if self.total is not None:
            result['Total'] = self.total

        if self.type is not None:
            result['Type'] = self.type

        if self.used is not None:
            result['Used'] = self.used

        if self.used_ratio is not None:
            result['UsedRatio'] = self.used_ratio

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('OversellRatio') is not None:
            self.oversell_ratio = m.get('OversellRatio')

        if m.get('Remain') is not None:
            self.remain = m.get('Remain')

        if m.get('ReserveDisable') is not None:
            self.reserve_disable = m.get('ReserveDisable')

        if m.get('ReserveDisableTotal') is not None:
            self.reserve_disable_total = m.get('ReserveDisableTotal')

        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')

        if m.get('StatusDisable') is not None:
            self.status_disable = m.get('StatusDisable')

        if m.get('StatusDisableTotal') is not None:
            self.status_disable_total = m.get('StatusDisableTotal')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Used') is not None:
            self.used = m.get('Used')

        if m.get('UsedRatio') is not None:
            self.used_ratio = m.get('UsedRatio')

        return self

class DescribeNCInformationResponseBodyDataInfo(DaraModel):
    def __init__(
        self,
        ip: str = None,
        name: str = None,
        tag: List[str] = None,
        uuid: str = None,
    ):
        self.ip = ip
        self.name = name
        self.tag = tag
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['Ip'] = self.ip

        if self.name is not None:
            result['Name'] = self.name

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class DescribeNCInformationResponseBodyDataHdd(DaraModel):
    def __init__(
        self,
        display: bool = None,
        oversell_ratio: int = None,
        remain: int = None,
        reserve_disable: bool = None,
        reserve_disable_total: int = None,
        reserved: int = None,
        status_disable: bool = None,
        status_disable_total: int = None,
        total: int = None,
        type: str = None,
        used: int = None,
        used_ratio: int = None,
    ):
        self.display = display
        self.oversell_ratio = oversell_ratio
        self.remain = remain
        self.reserve_disable = reserve_disable
        self.reserve_disable_total = reserve_disable_total
        self.reserved = reserved
        self.status_disable = status_disable
        self.status_disable_total = status_disable_total
        self.total = total
        self.type = type
        self.used = used
        self.used_ratio = used_ratio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display is not None:
            result['Display'] = self.display

        if self.oversell_ratio is not None:
            result['OversellRatio'] = self.oversell_ratio

        if self.remain is not None:
            result['Remain'] = self.remain

        if self.reserve_disable is not None:
            result['ReserveDisable'] = self.reserve_disable

        if self.reserve_disable_total is not None:
            result['ReserveDisableTotal'] = self.reserve_disable_total

        if self.reserved is not None:
            result['Reserved'] = self.reserved

        if self.status_disable is not None:
            result['StatusDisable'] = self.status_disable

        if self.status_disable_total is not None:
            result['StatusDisableTotal'] = self.status_disable_total

        if self.total is not None:
            result['Total'] = self.total

        if self.type is not None:
            result['Type'] = self.type

        if self.used is not None:
            result['Used'] = self.used

        if self.used_ratio is not None:
            result['UsedRatio'] = self.used_ratio

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('OversellRatio') is not None:
            self.oversell_ratio = m.get('OversellRatio')

        if m.get('Remain') is not None:
            self.remain = m.get('Remain')

        if m.get('ReserveDisable') is not None:
            self.reserve_disable = m.get('ReserveDisable')

        if m.get('ReserveDisableTotal') is not None:
            self.reserve_disable_total = m.get('ReserveDisableTotal')

        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')

        if m.get('StatusDisable') is not None:
            self.status_disable = m.get('StatusDisable')

        if m.get('StatusDisableTotal') is not None:
            self.status_disable_total = m.get('StatusDisableTotal')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Used') is not None:
            self.used = m.get('Used')

        if m.get('UsedRatio') is not None:
            self.used_ratio = m.get('UsedRatio')

        return self

class DescribeNCInformationResponseBodyDataGpu(DaraModel):
    def __init__(
        self,
        display: bool = None,
        oversell_ratio: int = None,
        remain: int = None,
        reserve_disable: bool = None,
        reserve_disable_total: int = None,
        reserved: int = None,
        status_disable: bool = None,
        status_disable_total: int = None,
        total: int = None,
        type: str = None,
        used: int = None,
        used_ratio: int = None,
    ):
        self.display = display
        self.oversell_ratio = oversell_ratio
        self.remain = remain
        self.reserve_disable = reserve_disable
        self.reserve_disable_total = reserve_disable_total
        self.reserved = reserved
        self.status_disable = status_disable
        self.status_disable_total = status_disable_total
        self.total = total
        self.type = type
        self.used = used
        self.used_ratio = used_ratio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display is not None:
            result['Display'] = self.display

        if self.oversell_ratio is not None:
            result['OversellRatio'] = self.oversell_ratio

        if self.remain is not None:
            result['Remain'] = self.remain

        if self.reserve_disable is not None:
            result['ReserveDisable'] = self.reserve_disable

        if self.reserve_disable_total is not None:
            result['ReserveDisableTotal'] = self.reserve_disable_total

        if self.reserved is not None:
            result['Reserved'] = self.reserved

        if self.status_disable is not None:
            result['StatusDisable'] = self.status_disable

        if self.status_disable_total is not None:
            result['StatusDisableTotal'] = self.status_disable_total

        if self.total is not None:
            result['Total'] = self.total

        if self.type is not None:
            result['Type'] = self.type

        if self.used is not None:
            result['Used'] = self.used

        if self.used_ratio is not None:
            result['UsedRatio'] = self.used_ratio

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('OversellRatio') is not None:
            self.oversell_ratio = m.get('OversellRatio')

        if m.get('Remain') is not None:
            self.remain = m.get('Remain')

        if m.get('ReserveDisable') is not None:
            self.reserve_disable = m.get('ReserveDisable')

        if m.get('ReserveDisableTotal') is not None:
            self.reserve_disable_total = m.get('ReserveDisableTotal')

        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')

        if m.get('StatusDisable') is not None:
            self.status_disable = m.get('StatusDisable')

        if m.get('StatusDisableTotal') is not None:
            self.status_disable_total = m.get('StatusDisableTotal')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Used') is not None:
            self.used = m.get('Used')

        if m.get('UsedRatio') is not None:
            self.used_ratio = m.get('UsedRatio')

        return self

class DescribeNCInformationResponseBodyDataCpu(DaraModel):
    def __init__(
        self,
        display: bool = None,
        oversell_ratio: int = None,
        remain: int = None,
        reserve_disable: bool = None,
        reserve_disable_total: int = None,
        reserved: int = None,
        status_disable: bool = None,
        status_disable_total: int = None,
        total: int = None,
        type: str = None,
        used: int = None,
        used_ratio: int = None,
    ):
        self.display = display
        self.oversell_ratio = oversell_ratio
        self.remain = remain
        self.reserve_disable = reserve_disable
        self.reserve_disable_total = reserve_disable_total
        self.reserved = reserved
        self.status_disable = status_disable
        self.status_disable_total = status_disable_total
        self.total = total
        self.type = type
        self.used = used
        self.used_ratio = used_ratio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display is not None:
            result['Display'] = self.display

        if self.oversell_ratio is not None:
            result['OversellRatio'] = self.oversell_ratio

        if self.remain is not None:
            result['Remain'] = self.remain

        if self.reserve_disable is not None:
            result['ReserveDisable'] = self.reserve_disable

        if self.reserve_disable_total is not None:
            result['ReserveDisableTotal'] = self.reserve_disable_total

        if self.reserved is not None:
            result['Reserved'] = self.reserved

        if self.status_disable is not None:
            result['StatusDisable'] = self.status_disable

        if self.status_disable_total is not None:
            result['StatusDisableTotal'] = self.status_disable_total

        if self.total is not None:
            result['Total'] = self.total

        if self.type is not None:
            result['Type'] = self.type

        if self.used is not None:
            result['Used'] = self.used

        if self.used_ratio is not None:
            result['UsedRatio'] = self.used_ratio

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('OversellRatio') is not None:
            self.oversell_ratio = m.get('OversellRatio')

        if m.get('Remain') is not None:
            self.remain = m.get('Remain')

        if m.get('ReserveDisable') is not None:
            self.reserve_disable = m.get('ReserveDisable')

        if m.get('ReserveDisableTotal') is not None:
            self.reserve_disable_total = m.get('ReserveDisableTotal')

        if m.get('Reserved') is not None:
            self.reserved = m.get('Reserved')

        if m.get('StatusDisable') is not None:
            self.status_disable = m.get('StatusDisable')

        if m.get('StatusDisableTotal') is not None:
            self.status_disable_total = m.get('StatusDisableTotal')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Used') is not None:
            self.used = m.get('Used')

        if m.get('UsedRatio') is not None:
            self.used_ratio = m.get('UsedRatio')

        return self

