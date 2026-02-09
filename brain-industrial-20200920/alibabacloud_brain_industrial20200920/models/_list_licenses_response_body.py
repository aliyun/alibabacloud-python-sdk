# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_brain_industrial20200920 import models as main_models
from darabonba.model import DaraModel

class ListLicensesResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        current_page: int = None,
        http_status_code: int = None,
        license_list: List[main_models.ListLicensesResponseBodyLicenseList] = None,
        message: str = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        total_page: str = None,
        total_page_count: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.current_page = current_page
        self.http_status_code = http_status_code
        self.license_list = license_list
        self.message = message
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count
        self.total_page = total_page
        self.total_page_count = total_page_count

    def validate(self):
        if self.license_list:
            for v1 in self.license_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['LicenseList'] = []
        if self.license_list is not None:
            for k1 in self.license_list:
                result['LicenseList'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        if self.total_page_count is not None:
            result['TotalPageCount'] = self.total_page_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.license_list = []
        if m.get('LicenseList') is not None:
            for k1 in m.get('LicenseList'):
                temp_model = main_models.ListLicensesResponseBodyLicenseList()
                self.license_list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        if m.get('TotalPageCount') is not None:
            self.total_page_count = m.get('TotalPageCount')

        return self

class ListLicensesResponseBodyLicenseList(DaraModel):
    def __init__(
        self,
        activate_time: str = None,
        adaptive_machine: int = None,
        all_duration: str = None,
        buy_time: str = None,
        cpu_limit: int = None,
        description: str = None,
        duration: str = None,
        effect_time: str = None,
        expire_time: str = None,
        id: str = None,
        instance_id: str = None,
        license_spec_code: str = None,
        license_spec_name: str = None,
        license_spec_type: str = None,
        memory_limit: int = None,
        status: str = None,
        un_activate_all_duration: str = None,
    ):
        self.activate_time = activate_time
        self.adaptive_machine = adaptive_machine
        self.all_duration = all_duration
        self.buy_time = buy_time
        self.cpu_limit = cpu_limit
        self.description = description
        self.duration = duration
        self.effect_time = effect_time
        self.expire_time = expire_time
        self.id = id
        self.instance_id = instance_id
        self.license_spec_code = license_spec_code
        self.license_spec_name = license_spec_name
        self.license_spec_type = license_spec_type
        self.memory_limit = memory_limit
        self.status = status
        self.un_activate_all_duration = un_activate_all_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activate_time is not None:
            result['ActivateTime'] = self.activate_time

        if self.adaptive_machine is not None:
            result['AdaptiveMachine'] = self.adaptive_machine

        if self.all_duration is not None:
            result['AllDuration'] = self.all_duration

        if self.buy_time is not None:
            result['BuyTime'] = self.buy_time

        if self.cpu_limit is not None:
            result['CpuLimit'] = self.cpu_limit

        if self.description is not None:
            result['Description'] = self.description

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.effect_time is not None:
            result['EffectTime'] = self.effect_time

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.license_spec_code is not None:
            result['LicenseSpecCode'] = self.license_spec_code

        if self.license_spec_name is not None:
            result['LicenseSpecName'] = self.license_spec_name

        if self.license_spec_type is not None:
            result['LicenseSpecType'] = self.license_spec_type

        if self.memory_limit is not None:
            result['MemoryLimit'] = self.memory_limit

        if self.status is not None:
            result['Status'] = self.status

        if self.un_activate_all_duration is not None:
            result['UnActivateAllDuration'] = self.un_activate_all_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivateTime') is not None:
            self.activate_time = m.get('ActivateTime')

        if m.get('AdaptiveMachine') is not None:
            self.adaptive_machine = m.get('AdaptiveMachine')

        if m.get('AllDuration') is not None:
            self.all_duration = m.get('AllDuration')

        if m.get('BuyTime') is not None:
            self.buy_time = m.get('BuyTime')

        if m.get('CpuLimit') is not None:
            self.cpu_limit = m.get('CpuLimit')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EffectTime') is not None:
            self.effect_time = m.get('EffectTime')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LicenseSpecCode') is not None:
            self.license_spec_code = m.get('LicenseSpecCode')

        if m.get('LicenseSpecName') is not None:
            self.license_spec_name = m.get('LicenseSpecName')

        if m.get('LicenseSpecType') is not None:
            self.license_spec_type = m.get('LicenseSpecType')

        if m.get('MemoryLimit') is not None:
            self.memory_limit = m.get('MemoryLimit')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UnActivateAllDuration') is not None:
            self.un_activate_all_duration = m.get('UnActivateAllDuration')

        return self

