# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeRegionResourceResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeRegionResourceResponseBodyData] = None,
        desc: str = None,
        msg: str = None,
        pager: main_models.DescribeRegionResourceResponseBodyPager = None,
        request_id: str = None,
    ):
        self.data = data
        self.desc = desc
        self.msg = msg
        self.pager = pager
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeRegionResourceResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('Pager') is not None:
            temp_model = main_models.DescribeRegionResourceResponseBodyPager()
            self.pager = temp_model.from_map(m.get('Pager'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRegionResourceResponseBodyPager(DaraModel):
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

class DescribeRegionResourceResponseBodyData(DaraModel):
    def __init__(
        self,
        area_code: str = None,
        area_name: str = None,
        arm_card: main_models.DescribeRegionResourceResponseBodyDataArmCard = None,
        attributes: List[str] = None,
        bandwidth: main_models.DescribeRegionResourceResponseBodyDataBandwidth = None,
        block_storage: main_models.DescribeRegionResourceResponseBodyDataBlockStorage = None,
        country_code: str = None,
        country_name: str = None,
        cpu: main_models.DescribeRegionResourceResponseBodyDataCpu = None,
        gpu: main_models.DescribeRegionResourceResponseBodyDataGpu = None,
        hdd: main_models.DescribeRegionResourceResponseBodyDataHdd = None,
        house_id: str = None,
        ipv_4s: List[main_models.DescribeRegionResourceResponseBodyDataIpv4s] = None,
        ipv_6s: List[main_models.DescribeRegionResourceResponseBodyDataIpv6s] = None,
        isp_types: List[str] = None,
        memory: main_models.DescribeRegionResourceResponseBodyDataMemory = None,
        name: str = None,
        nvme: main_models.DescribeRegionResourceResponseBodyDataNvme = None,
        oss_storage: main_models.DescribeRegionResourceResponseBodyDataOssStorage = None,
        pangu: main_models.DescribeRegionResourceResponseBodyDataPangu = None,
        pcfarm_num: main_models.DescribeRegionResourceResponseBodyDataPcfarmNum = None,
        poc: bool = None,
        province_code: str = None,
        province_name: str = None,
        reserve_disable: bool = None,
        ssd: main_models.DescribeRegionResourceResponseBodyDataSsd = None,
        status_disable: bool = None,
        type: str = None,
        uuid: str = None,
        virtual: str = None,
    ):
        self.area_code = area_code
        self.area_name = area_name
        self.arm_card = arm_card
        self.attributes = attributes
        self.bandwidth = bandwidth
        self.block_storage = block_storage
        self.country_code = country_code
        self.country_name = country_name
        self.cpu = cpu
        self.gpu = gpu
        self.hdd = hdd
        self.house_id = house_id
        self.ipv_4s = ipv_4s
        self.ipv_6s = ipv_6s
        self.isp_types = isp_types
        self.memory = memory
        self.name = name
        self.nvme = nvme
        self.oss_storage = oss_storage
        self.pangu = pangu
        self.pcfarm_num = pcfarm_num
        self.poc = poc
        self.province_code = province_code
        self.province_name = province_name
        self.reserve_disable = reserve_disable
        self.ssd = ssd
        self.status_disable = status_disable
        self.type = type
        self.uuid = uuid
        self.virtual = virtual

    def validate(self):
        if self.arm_card:
            self.arm_card.validate()
        if self.bandwidth:
            self.bandwidth.validate()
        if self.block_storage:
            self.block_storage.validate()
        if self.cpu:
            self.cpu.validate()
        if self.gpu:
            self.gpu.validate()
        if self.hdd:
            self.hdd.validate()
        if self.ipv_4s:
            for v1 in self.ipv_4s:
                 if v1:
                    v1.validate()
        if self.ipv_6s:
            for v1 in self.ipv_6s:
                 if v1:
                    v1.validate()
        if self.memory:
            self.memory.validate()
        if self.nvme:
            self.nvme.validate()
        if self.oss_storage:
            self.oss_storage.validate()
        if self.pangu:
            self.pangu.validate()
        if self.pcfarm_num:
            self.pcfarm_num.validate()
        if self.ssd:
            self.ssd.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area_code is not None:
            result['AreaCode'] = self.area_code

        if self.area_name is not None:
            result['AreaName'] = self.area_name

        if self.arm_card is not None:
            result['ArmCard'] = self.arm_card.to_map()

        if self.attributes is not None:
            result['Attributes'] = self.attributes

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth.to_map()

        if self.block_storage is not None:
            result['BlockStorage'] = self.block_storage.to_map()

        if self.country_code is not None:
            result['CountryCode'] = self.country_code

        if self.country_name is not None:
            result['CountryName'] = self.country_name

        if self.cpu is not None:
            result['Cpu'] = self.cpu.to_map()

        if self.gpu is not None:
            result['Gpu'] = self.gpu.to_map()

        if self.hdd is not None:
            result['Hdd'] = self.hdd.to_map()

        if self.house_id is not None:
            result['HouseId'] = self.house_id

        result['Ipv4s'] = []
        if self.ipv_4s is not None:
            for k1 in self.ipv_4s:
                result['Ipv4s'].append(k1.to_map() if k1 else None)

        result['Ipv6s'] = []
        if self.ipv_6s is not None:
            for k1 in self.ipv_6s:
                result['Ipv6s'].append(k1.to_map() if k1 else None)

        if self.isp_types is not None:
            result['IspTypes'] = self.isp_types

        if self.memory is not None:
            result['Memory'] = self.memory.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.nvme is not None:
            result['Nvme'] = self.nvme.to_map()

        if self.oss_storage is not None:
            result['OssStorage'] = self.oss_storage.to_map()

        if self.pangu is not None:
            result['Pangu'] = self.pangu.to_map()

        if self.pcfarm_num is not None:
            result['PcfarmNum'] = self.pcfarm_num.to_map()

        if self.poc is not None:
            result['Poc'] = self.poc

        if self.province_code is not None:
            result['ProvinceCode'] = self.province_code

        if self.province_name is not None:
            result['ProvinceName'] = self.province_name

        if self.reserve_disable is not None:
            result['ReserveDisable'] = self.reserve_disable

        if self.ssd is not None:
            result['Ssd'] = self.ssd.to_map()

        if self.status_disable is not None:
            result['StatusDisable'] = self.status_disable

        if self.type is not None:
            result['Type'] = self.type

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.virtual is not None:
            result['Virtual'] = self.virtual

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaCode') is not None:
            self.area_code = m.get('AreaCode')

        if m.get('AreaName') is not None:
            self.area_name = m.get('AreaName')

        if m.get('ArmCard') is not None:
            temp_model = main_models.DescribeRegionResourceResponseBodyDataArmCard()
            self.arm_card = temp_model.from_map(m.get('ArmCard'))

        if m.get('Attributes') is not None:
            self.attributes = m.get('Attributes')

        if m.get('Bandwidth') is not None:
            temp_model = main_models.DescribeRegionResourceResponseBodyDataBandwidth()
            self.bandwidth = temp_model.from_map(m.get('Bandwidth'))

        if m.get('BlockStorage') is not None:
            temp_model = main_models.DescribeRegionResourceResponseBodyDataBlockStorage()
            self.block_storage = temp_model.from_map(m.get('BlockStorage'))

        if m.get('CountryCode') is not None:
            self.country_code = m.get('CountryCode')

        if m.get('CountryName') is not None:
            self.country_name = m.get('CountryName')

        if m.get('Cpu') is not None:
            temp_model = main_models.DescribeRegionResourceResponseBodyDataCpu()
            self.cpu = temp_model.from_map(m.get('Cpu'))

        if m.get('Gpu') is not None:
            temp_model = main_models.DescribeRegionResourceResponseBodyDataGpu()
            self.gpu = temp_model.from_map(m.get('Gpu'))

        if m.get('Hdd') is not None:
            temp_model = main_models.DescribeRegionResourceResponseBodyDataHdd()
            self.hdd = temp_model.from_map(m.get('Hdd'))

        if m.get('HouseId') is not None:
            self.house_id = m.get('HouseId')

        self.ipv_4s = []
        if m.get('Ipv4s') is not None:
            for k1 in m.get('Ipv4s'):
                temp_model = main_models.DescribeRegionResourceResponseBodyDataIpv4s()
                self.ipv_4s.append(temp_model.from_map(k1))

        self.ipv_6s = []
        if m.get('Ipv6s') is not None:
            for k1 in m.get('Ipv6s'):
                temp_model = main_models.DescribeRegionResourceResponseBodyDataIpv6s()
                self.ipv_6s.append(temp_model.from_map(k1))

        if m.get('IspTypes') is not None:
            self.isp_types = m.get('IspTypes')

        if m.get('Memory') is not None:
            temp_model = main_models.DescribeRegionResourceResponseBodyDataMemory()
            self.memory = temp_model.from_map(m.get('Memory'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Nvme') is not None:
            temp_model = main_models.DescribeRegionResourceResponseBodyDataNvme()
            self.nvme = temp_model.from_map(m.get('Nvme'))

        if m.get('OssStorage') is not None:
            temp_model = main_models.DescribeRegionResourceResponseBodyDataOssStorage()
            self.oss_storage = temp_model.from_map(m.get('OssStorage'))

        if m.get('Pangu') is not None:
            temp_model = main_models.DescribeRegionResourceResponseBodyDataPangu()
            self.pangu = temp_model.from_map(m.get('Pangu'))

        if m.get('PcfarmNum') is not None:
            temp_model = main_models.DescribeRegionResourceResponseBodyDataPcfarmNum()
            self.pcfarm_num = temp_model.from_map(m.get('PcfarmNum'))

        if m.get('Poc') is not None:
            self.poc = m.get('Poc')

        if m.get('ProvinceCode') is not None:
            self.province_code = m.get('ProvinceCode')

        if m.get('ProvinceName') is not None:
            self.province_name = m.get('ProvinceName')

        if m.get('ReserveDisable') is not None:
            self.reserve_disable = m.get('ReserveDisable')

        if m.get('Ssd') is not None:
            temp_model = main_models.DescribeRegionResourceResponseBodyDataSsd()
            self.ssd = temp_model.from_map(m.get('Ssd'))

        if m.get('StatusDisable') is not None:
            self.status_disable = m.get('StatusDisable')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('Virtual') is not None:
            self.virtual = m.get('Virtual')

        return self

class DescribeRegionResourceResponseBodyDataSsd(DaraModel):
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

class DescribeRegionResourceResponseBodyDataPcfarmNum(DaraModel):
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

class DescribeRegionResourceResponseBodyDataPangu(DaraModel):
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

class DescribeRegionResourceResponseBodyDataOssStorage(DaraModel):
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

class DescribeRegionResourceResponseBodyDataNvme(DaraModel):
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

class DescribeRegionResourceResponseBodyDataMemory(DaraModel):
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

class DescribeRegionResourceResponseBodyDataIpv6s(DaraModel):
    def __init__(
        self,
        display: str = None,
        isp: str = None,
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
        vlan: str = None,
    ):
        self.display = display
        self.isp = isp
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
        self.vlan = vlan

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display is not None:
            result['Display'] = self.display

        if self.isp is not None:
            result['Isp'] = self.isp

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

        if self.vlan is not None:
            result['Vlan'] = self.vlan

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

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

        if m.get('Vlan') is not None:
            self.vlan = m.get('Vlan')

        return self

class DescribeRegionResourceResponseBodyDataIpv4s(DaraModel):
    def __init__(
        self,
        display: str = None,
        isp: str = None,
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
        vlan: str = None,
    ):
        self.display = display
        self.isp = isp
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
        self.vlan = vlan

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display is not None:
            result['Display'] = self.display

        if self.isp is not None:
            result['Isp'] = self.isp

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

        if self.vlan is not None:
            result['Vlan'] = self.vlan

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

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

        if m.get('Vlan') is not None:
            self.vlan = m.get('Vlan')

        return self

class DescribeRegionResourceResponseBodyDataHdd(DaraModel):
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

class DescribeRegionResourceResponseBodyDataGpu(DaraModel):
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

class DescribeRegionResourceResponseBodyDataCpu(DaraModel):
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

class DescribeRegionResourceResponseBodyDataBlockStorage(DaraModel):
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

class DescribeRegionResourceResponseBodyDataBandwidth(DaraModel):
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

class DescribeRegionResourceResponseBodyDataArmCard(DaraModel):
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

