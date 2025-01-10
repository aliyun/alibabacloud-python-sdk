# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class ActivateLicenseRequest(TeaModel):
    def __init__(
        self,
        fingerprint: str = None,
        id: str = None,
        instance_id: str = None,
        order_id: str = None,
    ):
        self.fingerprint = fingerprint
        self.id = id
        self.instance_id = instance_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ActivateLicenseResponseBodyDataActivateRecord(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ActivateLicenseResponseBodyData(TeaModel):
    def __init__(
        self,
        activate_record: List[ActivateLicenseResponseBodyDataActivateRecord] = None,
        activate_time: str = None,
        all_duration: str = None,
        applicable_specs: str = None,
        buy_time: str = None,
        cpu_limit: int = None,
        description: str = None,
        duration: str = None,
        effect_time: str = None,
        expire_time: str = None,
        fingerprint: str = None,
        id: str = None,
        instance_id: str = None,
        license_code: str = None,
        license_spec_name: str = None,
        memory_limit: int = None,
        status: str = None,
        un_activate_all_duration: str = None,
    ):
        self.activate_record = activate_record
        self.activate_time = activate_time
        self.all_duration = all_duration
        self.applicable_specs = applicable_specs
        self.buy_time = buy_time
        self.cpu_limit = cpu_limit
        self.description = description
        self.duration = duration
        self.effect_time = effect_time
        self.expire_time = expire_time
        self.fingerprint = fingerprint
        self.id = id
        self.instance_id = instance_id
        self.license_code = license_code
        self.license_spec_name = license_spec_name
        self.memory_limit = memory_limit
        self.status = status
        self.un_activate_all_duration = un_activate_all_duration

    def validate(self):
        if self.activate_record:
            for k in self.activate_record:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ActivateRecord'] = []
        if self.activate_record is not None:
            for k in self.activate_record:
                result['ActivateRecord'].append(k.to_map() if k else None)
        if self.activate_time is not None:
            result['ActivateTime'] = self.activate_time
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
        if self.license_spec_name is not None:
            result['LicenseSpecName'] = self.license_spec_name
        if self.memory_limit is not None:
            result['MemoryLimit'] = self.memory_limit
        if self.status is not None:
            result['Status'] = self.status
        if self.un_activate_all_duration is not None:
            result['UnActivateAllDuration'] = self.un_activate_all_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.activate_record = []
        if m.get('ActivateRecord') is not None:
            for k in m.get('ActivateRecord'):
                temp_model = ActivateLicenseResponseBodyDataActivateRecord()
                self.activate_record.append(temp_model.from_map(k))
        if m.get('ActivateTime') is not None:
            self.activate_time = m.get('ActivateTime')
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
        if m.get('LicenseSpecName') is not None:
            self.license_spec_name = m.get('LicenseSpecName')
        if m.get('MemoryLimit') is not None:
            self.memory_limit = m.get('MemoryLimit')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UnActivateAllDuration') is not None:
            self.un_activate_all_duration = m.get('UnActivateAllDuration')
        return self


class ActivateLicenseResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: ActivateLicenseResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ActivateLicenseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ActivateLicenseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ActivateLicenseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ActivateLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLicenseRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        instance_id: str = None,
    ):
        self.id = id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetLicenseResponseBodyDataActivateRecord(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class GetLicenseResponseBodyData(TeaModel):
    def __init__(
        self,
        activate_record: List[GetLicenseResponseBodyDataActivateRecord] = None,
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
            for k in self.activate_record:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ActivateRecord'] = []
        if self.activate_record is not None:
            for k in self.activate_record:
                result['ActivateRecord'].append(k.to_map() if k else None)
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
            for k in m.get('ActivateRecord'):
                temp_model = GetLicenseResponseBodyDataActivateRecord()
                self.activate_record.append(temp_model.from_map(k))
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


class GetLicenseResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: GetLicenseResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = GetLicenseResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetLicenseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLicenseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetLicenseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLicensesRequest(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        query_str: str = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.query_str = query_str

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_str is not None:
            result['QueryStr'] = self.query_str
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryStr') is not None:
            self.query_str = m.get('QueryStr')
        return self


class ListLicensesResponseBodyLicenseList(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListLicensesResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        current_page: int = None,
        http_status_code: int = None,
        license_list: List[ListLicensesResponseBodyLicenseList] = None,
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
            for k in self.license_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.license_list:
                result['LicenseList'].append(k.to_map() if k else None)
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
            for k in m.get('LicenseList'):
                temp_model = ListLicensesResponseBodyLicenseList()
                self.license_list.append(temp_model.from_map(k))
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


class ListLicensesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLicensesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLicensesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserResourcesRequest(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
    ):
        self.commodity_code = commodity_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        return self


class ListUserResourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        commodity_code: str = None,
        end_date: str = None,
        instance_id: str = None,
        region: str = None,
        start_date: str = None,
        status: str = None,
        status_msg: str = None,
    ):
        self.charge_type = charge_type
        self.commodity_code = commodity_code
        self.end_date = end_date
        self.instance_id = instance_id
        self.region = region
        self.start_date = start_date
        self.status = status
        self.status_msg = status_msg

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.region is not None:
            result['region'] = self.region
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.status is not None:
            result['status'] = self.status
        if self.status_msg is not None:
            result['statusMsg'] = self.status_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusMsg') is not None:
            self.status_msg = m.get('statusMsg')
        return self


class ListUserResourcesResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: List[ListUserResourcesResponseBodyData] = None,
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
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListUserResourcesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListUserResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUserResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLicenseDescriptionRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
    ):
        self.description = description
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateLicenseDescriptionResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateLicenseDescriptionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateLicenseDescriptionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateLicenseDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


