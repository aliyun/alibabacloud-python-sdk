# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_brain_industrial20200920 import models as main_models
from darabonba.model import DaraModel

class GetLicenseResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.GetLicenseResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetLicenseResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetLicenseResponseBodyData(DaraModel):
    def __init__(
        self,
        activate_record: List[main_models.GetLicenseResponseBodyDataActivateRecord] = None,
        activate_time: str = None,
        adaptive_machine: str = None,
        all_duration: str = None,
        applicable_specs: str = None,
        buy_time: str = None,
        cpu_limit: int = None,
        description: str = None,
        duration: str = None,
        effect_time: str = None,
        expire_time: str = None,
        fingerprint: str = None,
        id: int = None,
        instance_id: str = None,
        license_code: str = None,
        license_spec_code: str = None,
        license_spec_name: str = None,
        license_spec_type: str = None,
        memory_limit: int = None,
        proposal: str = None,
        status: str = None,
        un_activate_all_duration: str = None,
    ):
        self.activate_record = activate_record
        # 代表资源一级ID的资源属性字段
        self.activate_time = activate_time
        self.adaptive_machine = adaptive_machine
        self.all_duration = all_duration
        self.applicable_specs = applicable_specs
        # 代表资源名称的资源属性字段
        self.buy_time = buy_time
        self.cpu_limit = cpu_limit
        self.description = description
        self.duration = duration
        self.effect_time = effect_time
        self.expire_time = expire_time
        # 代表创建时间的资源属性字段
        self.fingerprint = fingerprint
        # ID
        self.id = id
        self.instance_id = instance_id
        self.license_code = license_code
        self.license_spec_code = license_spec_code
        # 代表资源组的资源属性字段
        self.license_spec_name = license_spec_name
        self.license_spec_type = license_spec_type
        self.memory_limit = memory_limit
        self.proposal = proposal
        self.status = status
        self.un_activate_all_duration = un_activate_all_duration

    def validate(self):
        if self.activate_record:
            for v1 in self.activate_record:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ActivateRecord'] = []
        if self.activate_record is not None:
            for k1 in self.activate_record:
                result['ActivateRecord'].append(k1.to_map() if k1 else None)

        if self.activate_time is not None:
            result['ActivateTime'] = self.activate_time

        if self.adaptive_machine is not None:
            result['AdaptiveMachine'] = self.adaptive_machine

        if self.all_duration is not None:
            result['AllDuration'] = self.all_duration

        if self.applicable_specs is not None:
            result['ApplicableSpecs'] = self.applicable_specs

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

        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.license_code is not None:
            result['LicenseCode'] = self.license_code

        if self.license_spec_code is not None:
            result['LicenseSpecCode'] = self.license_spec_code

        if self.license_spec_name is not None:
            result['LicenseSpecName'] = self.license_spec_name

        if self.license_spec_type is not None:
            result['LicenseSpecType'] = self.license_spec_type

        if self.memory_limit is not None:
            result['MemoryLimit'] = self.memory_limit

        if self.proposal is not None:
            result['Proposal'] = self.proposal

        if self.status is not None:
            result['Status'] = self.status

        if self.un_activate_all_duration is not None:
            result['UnActivateAllDuration'] = self.un_activate_all_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.activate_record = []
        if m.get('ActivateRecord') is not None:
            for k1 in m.get('ActivateRecord'):
                temp_model = main_models.GetLicenseResponseBodyDataActivateRecord()
                self.activate_record.append(temp_model.from_map(k1))

        if m.get('ActivateTime') is not None:
            self.activate_time = m.get('ActivateTime')

        if m.get('AdaptiveMachine') is not None:
            self.adaptive_machine = m.get('AdaptiveMachine')

        if m.get('AllDuration') is not None:
            self.all_duration = m.get('AllDuration')

        if m.get('ApplicableSpecs') is not None:
            self.applicable_specs = m.get('ApplicableSpecs')

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

        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')

        if m.get('LicenseSpecCode') is not None:
            self.license_spec_code = m.get('LicenseSpecCode')

        if m.get('LicenseSpecName') is not None:
            self.license_spec_name = m.get('LicenseSpecName')

        if m.get('LicenseSpecType') is not None:
            self.license_spec_type = m.get('LicenseSpecType')

        if m.get('MemoryLimit') is not None:
            self.memory_limit = m.get('MemoryLimit')

        if m.get('Proposal') is not None:
            self.proposal = m.get('Proposal')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UnActivateAllDuration') is not None:
            self.un_activate_all_duration = m.get('UnActivateAllDuration')

        return self

class GetLicenseResponseBodyDataActivateRecord(DaraModel):
    def __init__(
        self,
        activate_time: str = None,
        buy_time: str = None,
        duration: str = None,
        expire_time: str = None,
        license_code: str = None,
        order_id: str = None,
        status: str = None,
    ):
        self.activate_time = activate_time
        self.buy_time = buy_time
        self.duration = duration
        self.expire_time = expire_time
        self.license_code = license_code
        self.order_id = order_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activate_time is not None:
            result['ActivateTime'] = self.activate_time

        if self.buy_time is not None:
            result['BuyTime'] = self.buy_time

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.license_code is not None:
            result['LicenseCode'] = self.license_code

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivateTime') is not None:
            self.activate_time = m.get('ActivateTime')

        if m.get('BuyTime') is not None:
            self.buy_time = m.get('BuyTime')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

