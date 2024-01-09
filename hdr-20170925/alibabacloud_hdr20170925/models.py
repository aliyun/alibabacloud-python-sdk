# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class ChangeRecoveryPointRequest(TeaModel):
    def __init__(
        self,
        eip_address_id: str = None,
        recovery_cpu: int = None,
        recovery_essd_performance_level: str = None,
        recovery_instance_name: str = None,
        recovery_instance_type: str = None,
        recovery_ip_address: str = None,
        recovery_memory: int = None,
        recovery_network: str = None,
        recovery_point_id: str = None,
        recovery_point_time: int = None,
        recovery_post_script_content: str = None,
        recovery_post_script_type: str = None,
        recovery_reserve_ip: bool = None,
        recovery_use_dhcp: bool = None,
        recovery_use_essd: bool = None,
        recovery_use_ssd: bool = None,
        security_token: str = None,
        server_id: str = None,
    ):
        self.eip_address_id = eip_address_id
        self.recovery_cpu = recovery_cpu
        self.recovery_essd_performance_level = recovery_essd_performance_level
        self.recovery_instance_name = recovery_instance_name
        self.recovery_instance_type = recovery_instance_type
        self.recovery_ip_address = recovery_ip_address
        self.recovery_memory = recovery_memory
        self.recovery_network = recovery_network
        self.recovery_point_id = recovery_point_id
        self.recovery_point_time = recovery_point_time
        self.recovery_post_script_content = recovery_post_script_content
        self.recovery_post_script_type = recovery_post_script_type
        self.recovery_reserve_ip = recovery_reserve_ip
        self.recovery_use_dhcp = recovery_use_dhcp
        self.recovery_use_essd = recovery_use_essd
        self.recovery_use_ssd = recovery_use_ssd
        self.security_token = security_token
        self.server_id = server_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eip_address_id is not None:
            result['EipAddressId'] = self.eip_address_id
        if self.recovery_cpu is not None:
            result['RecoveryCpu'] = self.recovery_cpu
        if self.recovery_essd_performance_level is not None:
            result['RecoveryEssdPerformanceLevel'] = self.recovery_essd_performance_level
        if self.recovery_instance_name is not None:
            result['RecoveryInstanceName'] = self.recovery_instance_name
        if self.recovery_instance_type is not None:
            result['RecoveryInstanceType'] = self.recovery_instance_type
        if self.recovery_ip_address is not None:
            result['RecoveryIpAddress'] = self.recovery_ip_address
        if self.recovery_memory is not None:
            result['RecoveryMemory'] = self.recovery_memory
        if self.recovery_network is not None:
            result['RecoveryNetwork'] = self.recovery_network
        if self.recovery_point_id is not None:
            result['RecoveryPointId'] = self.recovery_point_id
        if self.recovery_point_time is not None:
            result['RecoveryPointTime'] = self.recovery_point_time
        if self.recovery_post_script_content is not None:
            result['RecoveryPostScriptContent'] = self.recovery_post_script_content
        if self.recovery_post_script_type is not None:
            result['RecoveryPostScriptType'] = self.recovery_post_script_type
        if self.recovery_reserve_ip is not None:
            result['RecoveryReserveIp'] = self.recovery_reserve_ip
        if self.recovery_use_dhcp is not None:
            result['RecoveryUseDhcp'] = self.recovery_use_dhcp
        if self.recovery_use_essd is not None:
            result['RecoveryUseEssd'] = self.recovery_use_essd
        if self.recovery_use_ssd is not None:
            result['RecoveryUseSsd'] = self.recovery_use_ssd
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipAddressId') is not None:
            self.eip_address_id = m.get('EipAddressId')
        if m.get('RecoveryCpu') is not None:
            self.recovery_cpu = m.get('RecoveryCpu')
        if m.get('RecoveryEssdPerformanceLevel') is not None:
            self.recovery_essd_performance_level = m.get('RecoveryEssdPerformanceLevel')
        if m.get('RecoveryInstanceName') is not None:
            self.recovery_instance_name = m.get('RecoveryInstanceName')
        if m.get('RecoveryInstanceType') is not None:
            self.recovery_instance_type = m.get('RecoveryInstanceType')
        if m.get('RecoveryIpAddress') is not None:
            self.recovery_ip_address = m.get('RecoveryIpAddress')
        if m.get('RecoveryMemory') is not None:
            self.recovery_memory = m.get('RecoveryMemory')
        if m.get('RecoveryNetwork') is not None:
            self.recovery_network = m.get('RecoveryNetwork')
        if m.get('RecoveryPointId') is not None:
            self.recovery_point_id = m.get('RecoveryPointId')
        if m.get('RecoveryPointTime') is not None:
            self.recovery_point_time = m.get('RecoveryPointTime')
        if m.get('RecoveryPostScriptContent') is not None:
            self.recovery_post_script_content = m.get('RecoveryPostScriptContent')
        if m.get('RecoveryPostScriptType') is not None:
            self.recovery_post_script_type = m.get('RecoveryPostScriptType')
        if m.get('RecoveryReserveIp') is not None:
            self.recovery_reserve_ip = m.get('RecoveryReserveIp')
        if m.get('RecoveryUseDhcp') is not None:
            self.recovery_use_dhcp = m.get('RecoveryUseDhcp')
        if m.get('RecoveryUseEssd') is not None:
            self.recovery_use_essd = m.get('RecoveryUseEssd')
        if m.get('RecoveryUseSsd') is not None:
            self.recovery_use_ssd = m.get('RecoveryUseSsd')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        return self


class ChangeRecoveryPointResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ChangeRecoveryPointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeRecoveryPointResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ChangeRecoveryPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CommitFailoverRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        server_id: str = None,
    ):
        self.security_token = security_token
        self.server_id = server_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        return self


class CommitFailoverResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CommitFailoverResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CommitFailoverResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CommitFailoverResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRecoveryPlanRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        direction: str = None,
        name: str = None,
        site_pair_id: str = None,
    ):
        self.content = content
        self.direction = direction
        self.name = name
        self.site_pair_id = site_pair_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.name is not None:
            result['Name'] = self.name
        if self.site_pair_id is not None:
            result['SitePairId'] = self.site_pair_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SitePairId') is not None:
            self.site_pair_id = m.get('SitePairId')
        return self


class CreateRecoveryPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateRecoveryPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRecoveryPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateRecoveryPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSitePairRequest(TeaModel):
    def __init__(
        self,
        primary_site_name: str = None,
        primary_site_region_id: str = None,
        primary_site_type: str = None,
        primary_site_vpc_id: str = None,
        primary_site_zone_id: str = None,
        secondary_site_name: str = None,
        secondary_site_region_id: str = None,
        secondary_site_type: str = None,
        secondary_site_vpc_id: str = None,
        secondary_site_zone_id: str = None,
        security_token: str = None,
        site_pair_type: str = None,
    ):
        self.primary_site_name = primary_site_name
        self.primary_site_region_id = primary_site_region_id
        self.primary_site_type = primary_site_type
        self.primary_site_vpc_id = primary_site_vpc_id
        self.primary_site_zone_id = primary_site_zone_id
        self.secondary_site_name = secondary_site_name
        self.secondary_site_region_id = secondary_site_region_id
        self.secondary_site_type = secondary_site_type
        self.secondary_site_vpc_id = secondary_site_vpc_id
        self.secondary_site_zone_id = secondary_site_zone_id
        self.security_token = security_token
        self.site_pair_type = site_pair_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.primary_site_name is not None:
            result['PrimarySiteName'] = self.primary_site_name
        if self.primary_site_region_id is not None:
            result['PrimarySiteRegionId'] = self.primary_site_region_id
        if self.primary_site_type is not None:
            result['PrimarySiteType'] = self.primary_site_type
        if self.primary_site_vpc_id is not None:
            result['PrimarySiteVpcId'] = self.primary_site_vpc_id
        if self.primary_site_zone_id is not None:
            result['PrimarySiteZoneId'] = self.primary_site_zone_id
        if self.secondary_site_name is not None:
            result['SecondarySiteName'] = self.secondary_site_name
        if self.secondary_site_region_id is not None:
            result['SecondarySiteRegionId'] = self.secondary_site_region_id
        if self.secondary_site_type is not None:
            result['SecondarySiteType'] = self.secondary_site_type
        if self.secondary_site_vpc_id is not None:
            result['SecondarySiteVpcId'] = self.secondary_site_vpc_id
        if self.secondary_site_zone_id is not None:
            result['SecondarySiteZoneId'] = self.secondary_site_zone_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.site_pair_type is not None:
            result['SitePairType'] = self.site_pair_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrimarySiteName') is not None:
            self.primary_site_name = m.get('PrimarySiteName')
        if m.get('PrimarySiteRegionId') is not None:
            self.primary_site_region_id = m.get('PrimarySiteRegionId')
        if m.get('PrimarySiteType') is not None:
            self.primary_site_type = m.get('PrimarySiteType')
        if m.get('PrimarySiteVpcId') is not None:
            self.primary_site_vpc_id = m.get('PrimarySiteVpcId')
        if m.get('PrimarySiteZoneId') is not None:
            self.primary_site_zone_id = m.get('PrimarySiteZoneId')
        if m.get('SecondarySiteName') is not None:
            self.secondary_site_name = m.get('SecondarySiteName')
        if m.get('SecondarySiteRegionId') is not None:
            self.secondary_site_region_id = m.get('SecondarySiteRegionId')
        if m.get('SecondarySiteType') is not None:
            self.secondary_site_type = m.get('SecondarySiteType')
        if m.get('SecondarySiteVpcId') is not None:
            self.secondary_site_vpc_id = m.get('SecondarySiteVpcId')
        if m.get('SecondarySiteZoneId') is not None:
            self.secondary_site_zone_id = m.get('SecondarySiteZoneId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SitePairType') is not None:
            self.site_pair_type = m.get('SitePairType')
        return self


class CreateSitePairResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        primary_site_id: str = None,
        request_id: str = None,
        secondary_site_id: str = None,
        site_pair_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.primary_site_id = primary_site_id
        self.request_id = request_id
        self.secondary_site_id = secondary_site_id
        self.site_pair_id = site_pair_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.primary_site_id is not None:
            result['PrimarySiteId'] = self.primary_site_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secondary_site_id is not None:
            result['SecondarySiteId'] = self.secondary_site_id
        if self.site_pair_id is not None:
            result['SitePairId'] = self.site_pair_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PrimarySiteId') is not None:
            self.primary_site_id = m.get('PrimarySiteId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecondarySiteId') is not None:
            self.secondary_site_id = m.get('SecondarySiteId')
        if m.get('SitePairId') is not None:
            self.site_pair_id = m.get('SitePairId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSitePairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSitePairResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = CreateSitePairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRecoveryPlanRequest(TeaModel):
    def __init__(
        self,
        recovery_plan_id: str = None,
    ):
        self.recovery_plan_id = recovery_plan_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recovery_plan_id is not None:
            result['RecoveryPlanId'] = self.recovery_plan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecoveryPlanId') is not None:
            self.recovery_plan_id = m.get('RecoveryPlanId')
        return self


class DeleteRecoveryPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteRecoveryPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRecoveryPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteRecoveryPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSitePairRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        site_pair_id: str = None,
    ):
        self.security_token = security_token
        self.site_pair_id = site_pair_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.site_pair_id is not None:
            result['SitePairId'] = self.site_pair_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SitePairId') is not None:
            self.site_pair_id = m.get('SitePairId')
        return self


class DeleteSitePairResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteSitePairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSitePairResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DeleteSitePairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableInstanceTypesRequest(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        disk_type: str = None,
        filter: str = None,
        io_optimized: bool = None,
        network: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        region: str = None,
        security_token: str = None,
        sort_by: str = None,
        user_client: bool = None,
        zone_id: str = None,
    ):
        self.charge_type = charge_type
        self.disk_type = disk_type
        # -\
        self.filter = filter
        self.io_optimized = io_optimized
        self.network = network
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.region = region
        self.security_token = security_token
        self.sort_by = sort_by
        self.user_client = user_client
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized
        if self.network is not None:
            result['Network'] = self.network
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region is not None:
            result['Region'] = self.region
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.user_client is not None:
            result['UserClient'] = self.user_client
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('UserClient') is not None:
            self.user_client = m.get('UserClient')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeAvailableInstanceTypesResponseBodyInstanceTypes(TeaModel):
    def __init__(
        self,
        instance_type: List[str] = None,
    ):
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        return self


class DescribeAvailableInstanceTypesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        instance_types: DescribeAvailableInstanceTypesResponseBodyInstanceTypes = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.instance_types = instance_types
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.instance_types:
            self.instance_types.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceTypes') is not None:
            temp_model = DescribeAvailableInstanceTypesResponseBodyInstanceTypes()
            self.instance_types = temp_model.from_map(m['InstanceTypes'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAvailableInstanceTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAvailableInstanceTypesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeAvailableInstanceTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInfrastructuresRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        site_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class DescribeInfrastructuresResponseBodyInfrastructuresInfrastructure(TeaModel):
    def __init__(
        self,
        errno: str = None,
        infrastructure_id: str = None,
        ip_address: str = None,
        name: str = None,
        status: str = None,
        type: str = None,
    ):
        self.errno = errno
        self.infrastructure_id = infrastructure_id
        self.ip_address = ip_address
        self.name = name
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.errno is not None:
            result['Errno'] = self.errno
        if self.infrastructure_id is not None:
            result['InfrastructureId'] = self.infrastructure_id
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Errno') is not None:
            self.errno = m.get('Errno')
        if m.get('InfrastructureId') is not None:
            self.infrastructure_id = m.get('InfrastructureId')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeInfrastructuresResponseBodyInfrastructures(TeaModel):
    def __init__(
        self,
        infrastructure: List[DescribeInfrastructuresResponseBodyInfrastructuresInfrastructure] = None,
    ):
        self.infrastructure = infrastructure

    def validate(self):
        if self.infrastructure:
            for k in self.infrastructure:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['infrastructure'] = []
        if self.infrastructure is not None:
            for k in self.infrastructure:
                result['infrastructure'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.infrastructure = []
        if m.get('infrastructure') is not None:
            for k in m.get('infrastructure'):
                temp_model = DescribeInfrastructuresResponseBodyInfrastructuresInfrastructure()
                self.infrastructure.append(temp_model.from_map(k))
        return self


class DescribeInfrastructuresResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        infrastructures: DescribeInfrastructuresResponseBodyInfrastructures = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.infrastructures = infrastructures
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.infrastructures:
            self.infrastructures.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.infrastructures is not None:
            result['Infrastructures'] = self.infrastructures.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Infrastructures') is not None:
            temp_model = DescribeInfrastructuresResponseBodyInfrastructures()
            self.infrastructures = temp_model.from_map(m['Infrastructures'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInfrastructuresResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInfrastructuresResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeInfrastructuresResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRecoveryPlanRequest(TeaModel):
    def __init__(
        self,
        recovery_plan_id: str = None,
    ):
        self.recovery_plan_id = recovery_plan_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recovery_plan_id is not None:
            result['RecoveryPlanId'] = self.recovery_plan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecoveryPlanId') is not None:
            self.recovery_plan_id = m.get('RecoveryPlanId')
        return self


class DescribeRecoveryPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        content: str = None,
        direction: str = None,
        message: str = None,
        name: str = None,
        recovery_plan_id: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        self.code = code
        self.content = content
        self.direction = direction
        self.message = message
        self.name = name
        self.recovery_plan_id = recovery_plan_id
        self.request_id = request_id
        self.status = status
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.recovery_plan_id is not None:
            result['RecoveryPlanId'] = self.recovery_plan_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RecoveryPlanId') is not None:
            self.recovery_plan_id = m.get('RecoveryPlanId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeRecoveryPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRecoveryPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeRecoveryPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRecoveryPlansRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        site_pair_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.site_pair_id = site_pair_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.site_pair_id is not None:
            result['SitePairId'] = self.site_pair_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SitePairId') is not None:
            self.site_pair_id = m.get('SitePairId')
        return self


class DescribeRecoveryPlansResponseBodyRecoveryPlansRecoveryPlan(TeaModel):
    def __init__(
        self,
        direction: str = None,
        name: str = None,
        recovery_plan_id: str = None,
        status: str = None,
    ):
        self.direction = direction
        self.name = name
        self.recovery_plan_id = recovery_plan_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.name is not None:
            result['Name'] = self.name
        if self.recovery_plan_id is not None:
            result['RecoveryPlanId'] = self.recovery_plan_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RecoveryPlanId') is not None:
            self.recovery_plan_id = m.get('RecoveryPlanId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeRecoveryPlansResponseBodyRecoveryPlans(TeaModel):
    def __init__(
        self,
        recovery_plan: List[DescribeRecoveryPlansResponseBodyRecoveryPlansRecoveryPlan] = None,
    ):
        self.recovery_plan = recovery_plan

    def validate(self):
        if self.recovery_plan:
            for k in self.recovery_plan:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['recoveryPlan'] = []
        if self.recovery_plan is not None:
            for k in self.recovery_plan:
                result['recoveryPlan'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.recovery_plan = []
        if m.get('recoveryPlan') is not None:
            for k in m.get('recoveryPlan'):
                temp_model = DescribeRecoveryPlansResponseBodyRecoveryPlansRecoveryPlan()
                self.recovery_plan.append(temp_model.from_map(k))
        return self


class DescribeRecoveryPlansResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        recovery_plans: DescribeRecoveryPlansResponseBodyRecoveryPlans = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.recovery_plans = recovery_plans
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.recovery_plans:
            self.recovery_plans.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.recovery_plans is not None:
            result['RecoveryPlans'] = self.recovery_plans.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RecoveryPlans') is not None:
            temp_model = DescribeRecoveryPlansResponseBodyRecoveryPlans()
            self.recovery_plans = temp_model.from_map(m['RecoveryPlans'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeRecoveryPlansResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRecoveryPlansResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeRecoveryPlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRecoveryPointsRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        server_id: str = None,
        start_time: int = None,
    ):
        self.security_token = security_token
        self.server_id = server_id
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeRecoveryPointsResponseBodyRecoveryPointsRecoveryPoint(TeaModel):
    def __init__(
        self,
        application_consistent: bool = None,
        disable_reason: str = None,
        disabled: bool = None,
        recovery_point_id: str = None,
        recovery_point_time: int = None,
        used: bool = None,
    ):
        self.application_consistent = application_consistent
        self.disable_reason = disable_reason
        self.disabled = disabled
        self.recovery_point_id = recovery_point_id
        self.recovery_point_time = recovery_point_time
        self.used = used

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application_consistent is not None:
            result['ApplicationConsistent'] = self.application_consistent
        if self.disable_reason is not None:
            result['DisableReason'] = self.disable_reason
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.recovery_point_id is not None:
            result['RecoveryPointId'] = self.recovery_point_id
        if self.recovery_point_time is not None:
            result['RecoveryPointTime'] = self.recovery_point_time
        if self.used is not None:
            result['Used'] = self.used
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationConsistent') is not None:
            self.application_consistent = m.get('ApplicationConsistent')
        if m.get('DisableReason') is not None:
            self.disable_reason = m.get('DisableReason')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('RecoveryPointId') is not None:
            self.recovery_point_id = m.get('RecoveryPointId')
        if m.get('RecoveryPointTime') is not None:
            self.recovery_point_time = m.get('RecoveryPointTime')
        if m.get('Used') is not None:
            self.used = m.get('Used')
        return self


class DescribeRecoveryPointsResponseBodyRecoveryPoints(TeaModel):
    def __init__(
        self,
        recovery_point: List[DescribeRecoveryPointsResponseBodyRecoveryPointsRecoveryPoint] = None,
    ):
        self.recovery_point = recovery_point

    def validate(self):
        if self.recovery_point:
            for k in self.recovery_point:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['recoveryPoint'] = []
        if self.recovery_point is not None:
            for k in self.recovery_point:
                result['recoveryPoint'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.recovery_point = []
        if m.get('recoveryPoint') is not None:
            for k in m.get('recoveryPoint'):
                temp_model = DescribeRecoveryPointsResponseBodyRecoveryPointsRecoveryPoint()
                self.recovery_point.append(temp_model.from_map(k))
        return self


class DescribeRecoveryPointsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        recovery_points: DescribeRecoveryPointsResponseBodyRecoveryPoints = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.message = message
        self.recovery_points = recovery_points
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.recovery_points:
            self.recovery_points.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.recovery_points is not None:
            result['RecoveryPoints'] = self.recovery_points.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RecoveryPoints') is not None:
            temp_model = DescribeRecoveryPointsResponseBodyRecoveryPoints()
            self.recovery_points = temp_model.from_map(m['RecoveryPoints'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeRecoveryPointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRecoveryPointsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeRecoveryPointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServerRequest(TeaModel):
    def __init__(
        self,
        server_id: str = None,
    ):
        self.server_id = server_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        return self


class DescribeServerResponseBody(TeaModel):
    def __init__(
        self,
        agent_port: int = None,
        agent_version: str = None,
        alias: str = None,
        code: str = None,
        connection_status: str = None,
        consistent: bool = None,
        cpu: int = None,
        crash_consistent_point_policy: str = None,
        disks: str = None,
        errno: str = None,
        full_sync_current_size: int = None,
        full_sync_progress: int = None,
        full_sync_start_time: int = None,
        full_sync_total_size: int = None,
        hostname: str = None,
        incremental_sync_start_time: int = None,
        ip_address: str = None,
        latest_recovery_point_time: str = None,
        memory: int = None,
        message: str = None,
        operations: str = None,
        original_instance_id: str = None,
        os_detail: str = None,
        os_type: str = None,
        primary_site_id: str = None,
        recovered_instance_id: str = None,
        recovered_ip_address: str = None,
        recovery_cpu: int = None,
        recovery_essd_performance_level: str = None,
        recovery_instance_name: str = None,
        recovery_instance_type: str = None,
        recovery_ip_address: str = None,
        recovery_memory: int = None,
        recovery_network: str = None,
        recovery_post_script_content: str = None,
        recovery_post_script_type: str = None,
        recovery_reserve_ip: bool = None,
        recovery_use_dhcp: bool = None,
        recovery_use_essd: bool = None,
        recovery_use_ssd: bool = None,
        replication_infrastructure_id: str = None,
        replication_infrastructure_type: str = None,
        replication_network: str = None,
        replication_use_dhcp: bool = None,
        replication_use_essd: bool = None,
        replication_use_original_instance: bool = None,
        replication_use_ssd: bool = None,
        request_id: str = None,
        rpo: int = None,
        secondary_site_id: str = None,
        server_id: str = None,
        source_gateway_version: str = None,
        status: str = None,
        success: bool = None,
        target_gateway_version: str = None,
        task_id: str = None,
        test_failover_status: str = None,
        test_recovered_instance_id: str = None,
        test_recovered_instance_name: str = None,
        test_recovered_ip_address: str = None,
    ):
        self.agent_port = agent_port
        self.agent_version = agent_version
        self.alias = alias
        self.code = code
        self.connection_status = connection_status
        self.consistent = consistent
        self.cpu = cpu
        self.crash_consistent_point_policy = crash_consistent_point_policy
        self.disks = disks
        self.errno = errno
        self.full_sync_current_size = full_sync_current_size
        self.full_sync_progress = full_sync_progress
        self.full_sync_start_time = full_sync_start_time
        self.full_sync_total_size = full_sync_total_size
        self.hostname = hostname
        self.incremental_sync_start_time = incremental_sync_start_time
        self.ip_address = ip_address
        self.latest_recovery_point_time = latest_recovery_point_time
        self.memory = memory
        self.message = message
        self.operations = operations
        self.original_instance_id = original_instance_id
        self.os_detail = os_detail
        self.os_type = os_type
        self.primary_site_id = primary_site_id
        self.recovered_instance_id = recovered_instance_id
        self.recovered_ip_address = recovered_ip_address
        self.recovery_cpu = recovery_cpu
        self.recovery_essd_performance_level = recovery_essd_performance_level
        self.recovery_instance_name = recovery_instance_name
        self.recovery_instance_type = recovery_instance_type
        self.recovery_ip_address = recovery_ip_address
        self.recovery_memory = recovery_memory
        self.recovery_network = recovery_network
        self.recovery_post_script_content = recovery_post_script_content
        self.recovery_post_script_type = recovery_post_script_type
        self.recovery_reserve_ip = recovery_reserve_ip
        self.recovery_use_dhcp = recovery_use_dhcp
        self.recovery_use_essd = recovery_use_essd
        self.recovery_use_ssd = recovery_use_ssd
        self.replication_infrastructure_id = replication_infrastructure_id
        self.replication_infrastructure_type = replication_infrastructure_type
        self.replication_network = replication_network
        # -\
        self.replication_use_dhcp = replication_use_dhcp
        self.replication_use_essd = replication_use_essd
        self.replication_use_original_instance = replication_use_original_instance
        self.replication_use_ssd = replication_use_ssd
        self.request_id = request_id
        self.rpo = rpo
        self.secondary_site_id = secondary_site_id
        self.server_id = server_id
        self.source_gateway_version = source_gateway_version
        self.status = status
        self.success = success
        self.target_gateway_version = target_gateway_version
        self.task_id = task_id
        self.test_failover_status = test_failover_status
        self.test_recovered_instance_id = test_recovered_instance_id
        self.test_recovered_instance_name = test_recovered_instance_name
        self.test_recovered_ip_address = test_recovered_ip_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_port is not None:
            result['AgentPort'] = self.agent_port
        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.code is not None:
            result['Code'] = self.code
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.consistent is not None:
            result['Consistent'] = self.consistent
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.crash_consistent_point_policy is not None:
            result['CrashConsistentPointPolicy'] = self.crash_consistent_point_policy
        if self.disks is not None:
            result['Disks'] = self.disks
        if self.errno is not None:
            result['Errno'] = self.errno
        if self.full_sync_current_size is not None:
            result['FullSyncCurrentSize'] = self.full_sync_current_size
        if self.full_sync_progress is not None:
            result['FullSyncProgress'] = self.full_sync_progress
        if self.full_sync_start_time is not None:
            result['FullSyncStartTime'] = self.full_sync_start_time
        if self.full_sync_total_size is not None:
            result['FullSyncTotalSize'] = self.full_sync_total_size
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.incremental_sync_start_time is not None:
            result['IncrementalSyncStartTime'] = self.incremental_sync_start_time
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.latest_recovery_point_time is not None:
            result['LatestRecoveryPointTime'] = self.latest_recovery_point_time
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.message is not None:
            result['Message'] = self.message
        if self.operations is not None:
            result['Operations'] = self.operations
        if self.original_instance_id is not None:
            result['OriginalInstanceId'] = self.original_instance_id
        if self.os_detail is not None:
            result['OsDetail'] = self.os_detail
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.primary_site_id is not None:
            result['PrimarySiteId'] = self.primary_site_id
        if self.recovered_instance_id is not None:
            result['RecoveredInstanceId'] = self.recovered_instance_id
        if self.recovered_ip_address is not None:
            result['RecoveredIpAddress'] = self.recovered_ip_address
        if self.recovery_cpu is not None:
            result['RecoveryCpu'] = self.recovery_cpu
        if self.recovery_essd_performance_level is not None:
            result['RecoveryEssdPerformanceLevel'] = self.recovery_essd_performance_level
        if self.recovery_instance_name is not None:
            result['RecoveryInstanceName'] = self.recovery_instance_name
        if self.recovery_instance_type is not None:
            result['RecoveryInstanceType'] = self.recovery_instance_type
        if self.recovery_ip_address is not None:
            result['RecoveryIpAddress'] = self.recovery_ip_address
        if self.recovery_memory is not None:
            result['RecoveryMemory'] = self.recovery_memory
        if self.recovery_network is not None:
            result['RecoveryNetwork'] = self.recovery_network
        if self.recovery_post_script_content is not None:
            result['RecoveryPostScriptContent'] = self.recovery_post_script_content
        if self.recovery_post_script_type is not None:
            result['RecoveryPostScriptType'] = self.recovery_post_script_type
        if self.recovery_reserve_ip is not None:
            result['RecoveryReserveIp'] = self.recovery_reserve_ip
        if self.recovery_use_dhcp is not None:
            result['RecoveryUseDhcp'] = self.recovery_use_dhcp
        if self.recovery_use_essd is not None:
            result['RecoveryUseEssd'] = self.recovery_use_essd
        if self.recovery_use_ssd is not None:
            result['RecoveryUseSsd'] = self.recovery_use_ssd
        if self.replication_infrastructure_id is not None:
            result['ReplicationInfrastructureId'] = self.replication_infrastructure_id
        if self.replication_infrastructure_type is not None:
            result['ReplicationInfrastructureType'] = self.replication_infrastructure_type
        if self.replication_network is not None:
            result['ReplicationNetwork'] = self.replication_network
        if self.replication_use_dhcp is not None:
            result['ReplicationUseDhcp'] = self.replication_use_dhcp
        if self.replication_use_essd is not None:
            result['ReplicationUseEssd'] = self.replication_use_essd
        if self.replication_use_original_instance is not None:
            result['ReplicationUseOriginalInstance'] = self.replication_use_original_instance
        if self.replication_use_ssd is not None:
            result['ReplicationUseSsd'] = self.replication_use_ssd
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rpo is not None:
            result['Rpo'] = self.rpo
        if self.secondary_site_id is not None:
            result['SecondarySiteId'] = self.secondary_site_id
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.source_gateway_version is not None:
            result['SourceGatewayVersion'] = self.source_gateway_version
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        if self.target_gateway_version is not None:
            result['TargetGatewayVersion'] = self.target_gateway_version
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.test_failover_status is not None:
            result['TestFailoverStatus'] = self.test_failover_status
        if self.test_recovered_instance_id is not None:
            result['TestRecoveredInstanceId'] = self.test_recovered_instance_id
        if self.test_recovered_instance_name is not None:
            result['TestRecoveredInstanceName'] = self.test_recovered_instance_name
        if self.test_recovered_ip_address is not None:
            result['TestRecoveredIpAddress'] = self.test_recovered_ip_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentPort') is not None:
            self.agent_port = m.get('AgentPort')
        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('Consistent') is not None:
            self.consistent = m.get('Consistent')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CrashConsistentPointPolicy') is not None:
            self.crash_consistent_point_policy = m.get('CrashConsistentPointPolicy')
        if m.get('Disks') is not None:
            self.disks = m.get('Disks')
        if m.get('Errno') is not None:
            self.errno = m.get('Errno')
        if m.get('FullSyncCurrentSize') is not None:
            self.full_sync_current_size = m.get('FullSyncCurrentSize')
        if m.get('FullSyncProgress') is not None:
            self.full_sync_progress = m.get('FullSyncProgress')
        if m.get('FullSyncStartTime') is not None:
            self.full_sync_start_time = m.get('FullSyncStartTime')
        if m.get('FullSyncTotalSize') is not None:
            self.full_sync_total_size = m.get('FullSyncTotalSize')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('IncrementalSyncStartTime') is not None:
            self.incremental_sync_start_time = m.get('IncrementalSyncStartTime')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('LatestRecoveryPointTime') is not None:
            self.latest_recovery_point_time = m.get('LatestRecoveryPointTime')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Operations') is not None:
            self.operations = m.get('Operations')
        if m.get('OriginalInstanceId') is not None:
            self.original_instance_id = m.get('OriginalInstanceId')
        if m.get('OsDetail') is not None:
            self.os_detail = m.get('OsDetail')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('PrimarySiteId') is not None:
            self.primary_site_id = m.get('PrimarySiteId')
        if m.get('RecoveredInstanceId') is not None:
            self.recovered_instance_id = m.get('RecoveredInstanceId')
        if m.get('RecoveredIpAddress') is not None:
            self.recovered_ip_address = m.get('RecoveredIpAddress')
        if m.get('RecoveryCpu') is not None:
            self.recovery_cpu = m.get('RecoveryCpu')
        if m.get('RecoveryEssdPerformanceLevel') is not None:
            self.recovery_essd_performance_level = m.get('RecoveryEssdPerformanceLevel')
        if m.get('RecoveryInstanceName') is not None:
            self.recovery_instance_name = m.get('RecoveryInstanceName')
        if m.get('RecoveryInstanceType') is not None:
            self.recovery_instance_type = m.get('RecoveryInstanceType')
        if m.get('RecoveryIpAddress') is not None:
            self.recovery_ip_address = m.get('RecoveryIpAddress')
        if m.get('RecoveryMemory') is not None:
            self.recovery_memory = m.get('RecoveryMemory')
        if m.get('RecoveryNetwork') is not None:
            self.recovery_network = m.get('RecoveryNetwork')
        if m.get('RecoveryPostScriptContent') is not None:
            self.recovery_post_script_content = m.get('RecoveryPostScriptContent')
        if m.get('RecoveryPostScriptType') is not None:
            self.recovery_post_script_type = m.get('RecoveryPostScriptType')
        if m.get('RecoveryReserveIp') is not None:
            self.recovery_reserve_ip = m.get('RecoveryReserveIp')
        if m.get('RecoveryUseDhcp') is not None:
            self.recovery_use_dhcp = m.get('RecoveryUseDhcp')
        if m.get('RecoveryUseEssd') is not None:
            self.recovery_use_essd = m.get('RecoveryUseEssd')
        if m.get('RecoveryUseSsd') is not None:
            self.recovery_use_ssd = m.get('RecoveryUseSsd')
        if m.get('ReplicationInfrastructureId') is not None:
            self.replication_infrastructure_id = m.get('ReplicationInfrastructureId')
        if m.get('ReplicationInfrastructureType') is not None:
            self.replication_infrastructure_type = m.get('ReplicationInfrastructureType')
        if m.get('ReplicationNetwork') is not None:
            self.replication_network = m.get('ReplicationNetwork')
        if m.get('ReplicationUseDhcp') is not None:
            self.replication_use_dhcp = m.get('ReplicationUseDhcp')
        if m.get('ReplicationUseEssd') is not None:
            self.replication_use_essd = m.get('ReplicationUseEssd')
        if m.get('ReplicationUseOriginalInstance') is not None:
            self.replication_use_original_instance = m.get('ReplicationUseOriginalInstance')
        if m.get('ReplicationUseSsd') is not None:
            self.replication_use_ssd = m.get('ReplicationUseSsd')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rpo') is not None:
            self.rpo = m.get('Rpo')
        if m.get('SecondarySiteId') is not None:
            self.secondary_site_id = m.get('SecondarySiteId')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('SourceGatewayVersion') is not None:
            self.source_gateway_version = m.get('SourceGatewayVersion')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TargetGatewayVersion') is not None:
            self.target_gateway_version = m.get('TargetGatewayVersion')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TestFailoverStatus') is not None:
            self.test_failover_status = m.get('TestFailoverStatus')
        if m.get('TestRecoveredInstanceId') is not None:
            self.test_recovered_instance_id = m.get('TestRecoveredInstanceId')
        if m.get('TestRecoveredInstanceName') is not None:
            self.test_recovered_instance_name = m.get('TestRecoveredInstanceName')
        if m.get('TestRecoveredIpAddress') is not None:
            self.test_recovered_ip_address = m.get('TestRecoveredIpAddress')
        return self


class DescribeServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeServerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServersRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        server_ids: str = None,
        site_pair_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token
        self.server_ids = server_ids
        self.site_pair_id = site_pair_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.server_ids is not None:
            result['ServerIds'] = self.server_ids
        if self.site_pair_id is not None:
            result['SitePairId'] = self.site_pair_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ServerIds') is not None:
            self.server_ids = m.get('ServerIds')
        if m.get('SitePairId') is not None:
            self.site_pair_id = m.get('SitePairId')
        return self


class DescribeServersResponseBodyServersServer(TeaModel):
    def __init__(
        self,
        agent_port: int = None,
        agent_version: str = None,
        alias: str = None,
        connection_status: str = None,
        consistent: bool = None,
        cpu: int = None,
        crash_consistent_point_policy: str = None,
        disks: str = None,
        errno: str = None,
        full_sync_current_size: int = None,
        full_sync_progress: int = None,
        full_sync_start_time: int = None,
        full_sync_total_size: int = None,
        hostname: str = None,
        incremental_sync_start_time: int = None,
        instance_id: str = None,
        ip_address: str = None,
        latest_recovery_point_time: int = None,
        memory: int = None,
        operations: str = None,
        original_instance_id: str = None,
        os_detail: str = None,
        os_type: str = None,
        primary_site_id: str = None,
        recovered_instance_id: str = None,
        recovered_instance_name: str = None,
        recovered_ip_address: str = None,
        recovery_cpu: int = None,
        recovery_essd_performance_level: str = None,
        recovery_instance_name: str = None,
        recovery_instance_type: str = None,
        recovery_ip_address: str = None,
        recovery_memory: int = None,
        recovery_network: str = None,
        recovery_post_script_content: str = None,
        recovery_post_script_type: str = None,
        recovery_reserve_ip: bool = None,
        recovery_use_dhcp: bool = None,
        recovery_use_essd: bool = None,
        recovery_use_ssd: bool = None,
        replication_infrastructure_id: str = None,
        replication_infrastructure_type: str = None,
        replication_network: str = None,
        replication_use_dhcp: bool = None,
        replication_use_essd: bool = None,
        replication_use_original_instance: bool = None,
        replication_use_ssd: bool = None,
        rpo: int = None,
        secondary_site_id: str = None,
        server_id: str = None,
        source_gateway_version: str = None,
        status: str = None,
        target_gateway_version: str = None,
        task_id: str = None,
        test_failover_status: str = None,
        test_recovered_instance_id: str = None,
        test_recovered_instance_name: str = None,
        test_recovered_ip_address: str = None,
    ):
        self.agent_port = agent_port
        self.agent_version = agent_version
        self.alias = alias
        self.connection_status = connection_status
        self.consistent = consistent
        self.cpu = cpu
        self.crash_consistent_point_policy = crash_consistent_point_policy
        self.disks = disks
        self.errno = errno
        self.full_sync_current_size = full_sync_current_size
        self.full_sync_progress = full_sync_progress
        self.full_sync_start_time = full_sync_start_time
        self.full_sync_total_size = full_sync_total_size
        self.hostname = hostname
        self.incremental_sync_start_time = incremental_sync_start_time
        self.instance_id = instance_id
        self.ip_address = ip_address
        self.latest_recovery_point_time = latest_recovery_point_time
        self.memory = memory
        self.operations = operations
        self.original_instance_id = original_instance_id
        self.os_detail = os_detail
        self.os_type = os_type
        self.primary_site_id = primary_site_id
        self.recovered_instance_id = recovered_instance_id
        # -\
        self.recovered_instance_name = recovered_instance_name
        self.recovered_ip_address = recovered_ip_address
        self.recovery_cpu = recovery_cpu
        self.recovery_essd_performance_level = recovery_essd_performance_level
        self.recovery_instance_name = recovery_instance_name
        self.recovery_instance_type = recovery_instance_type
        self.recovery_ip_address = recovery_ip_address
        self.recovery_memory = recovery_memory
        self.recovery_network = recovery_network
        self.recovery_post_script_content = recovery_post_script_content
        self.recovery_post_script_type = recovery_post_script_type
        self.recovery_reserve_ip = recovery_reserve_ip
        self.recovery_use_dhcp = recovery_use_dhcp
        self.recovery_use_essd = recovery_use_essd
        self.recovery_use_ssd = recovery_use_ssd
        self.replication_infrastructure_id = replication_infrastructure_id
        self.replication_infrastructure_type = replication_infrastructure_type
        self.replication_network = replication_network
        self.replication_use_dhcp = replication_use_dhcp
        self.replication_use_essd = replication_use_essd
        self.replication_use_original_instance = replication_use_original_instance
        self.replication_use_ssd = replication_use_ssd
        self.rpo = rpo
        self.secondary_site_id = secondary_site_id
        self.server_id = server_id
        self.source_gateway_version = source_gateway_version
        self.status = status
        self.target_gateway_version = target_gateway_version
        self.task_id = task_id
        self.test_failover_status = test_failover_status
        self.test_recovered_instance_id = test_recovered_instance_id
        self.test_recovered_instance_name = test_recovered_instance_name
        self.test_recovered_ip_address = test_recovered_ip_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_port is not None:
            result['AgentPort'] = self.agent_port
        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.consistent is not None:
            result['Consistent'] = self.consistent
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.crash_consistent_point_policy is not None:
            result['CrashConsistentPointPolicy'] = self.crash_consistent_point_policy
        if self.disks is not None:
            result['Disks'] = self.disks
        if self.errno is not None:
            result['Errno'] = self.errno
        if self.full_sync_current_size is not None:
            result['FullSyncCurrentSize'] = self.full_sync_current_size
        if self.full_sync_progress is not None:
            result['FullSyncProgress'] = self.full_sync_progress
        if self.full_sync_start_time is not None:
            result['FullSyncStartTime'] = self.full_sync_start_time
        if self.full_sync_total_size is not None:
            result['FullSyncTotalSize'] = self.full_sync_total_size
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.incremental_sync_start_time is not None:
            result['IncrementalSyncStartTime'] = self.incremental_sync_start_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.latest_recovery_point_time is not None:
            result['LatestRecoveryPointTime'] = self.latest_recovery_point_time
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.operations is not None:
            result['Operations'] = self.operations
        if self.original_instance_id is not None:
            result['OriginalInstanceId'] = self.original_instance_id
        if self.os_detail is not None:
            result['OsDetail'] = self.os_detail
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.primary_site_id is not None:
            result['PrimarySiteId'] = self.primary_site_id
        if self.recovered_instance_id is not None:
            result['RecoveredInstanceId'] = self.recovered_instance_id
        if self.recovered_instance_name is not None:
            result['RecoveredInstanceName'] = self.recovered_instance_name
        if self.recovered_ip_address is not None:
            result['RecoveredIpAddress'] = self.recovered_ip_address
        if self.recovery_cpu is not None:
            result['RecoveryCpu'] = self.recovery_cpu
        if self.recovery_essd_performance_level is not None:
            result['RecoveryEssdPerformanceLevel'] = self.recovery_essd_performance_level
        if self.recovery_instance_name is not None:
            result['RecoveryInstanceName'] = self.recovery_instance_name
        if self.recovery_instance_type is not None:
            result['RecoveryInstanceType'] = self.recovery_instance_type
        if self.recovery_ip_address is not None:
            result['RecoveryIpAddress'] = self.recovery_ip_address
        if self.recovery_memory is not None:
            result['RecoveryMemory'] = self.recovery_memory
        if self.recovery_network is not None:
            result['RecoveryNetwork'] = self.recovery_network
        if self.recovery_post_script_content is not None:
            result['RecoveryPostScriptContent'] = self.recovery_post_script_content
        if self.recovery_post_script_type is not None:
            result['RecoveryPostScriptType'] = self.recovery_post_script_type
        if self.recovery_reserve_ip is not None:
            result['RecoveryReserveIp'] = self.recovery_reserve_ip
        if self.recovery_use_dhcp is not None:
            result['RecoveryUseDhcp'] = self.recovery_use_dhcp
        if self.recovery_use_essd is not None:
            result['RecoveryUseEssd'] = self.recovery_use_essd
        if self.recovery_use_ssd is not None:
            result['RecoveryUseSsd'] = self.recovery_use_ssd
        if self.replication_infrastructure_id is not None:
            result['ReplicationInfrastructureId'] = self.replication_infrastructure_id
        if self.replication_infrastructure_type is not None:
            result['ReplicationInfrastructureType'] = self.replication_infrastructure_type
        if self.replication_network is not None:
            result['ReplicationNetwork'] = self.replication_network
        if self.replication_use_dhcp is not None:
            result['ReplicationUseDhcp'] = self.replication_use_dhcp
        if self.replication_use_essd is not None:
            result['ReplicationUseEssd'] = self.replication_use_essd
        if self.replication_use_original_instance is not None:
            result['ReplicationUseOriginalInstance'] = self.replication_use_original_instance
        if self.replication_use_ssd is not None:
            result['ReplicationUseSsd'] = self.replication_use_ssd
        if self.rpo is not None:
            result['Rpo'] = self.rpo
        if self.secondary_site_id is not None:
            result['SecondarySiteId'] = self.secondary_site_id
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.source_gateway_version is not None:
            result['SourceGatewayVersion'] = self.source_gateway_version
        if self.status is not None:
            result['Status'] = self.status
        if self.target_gateway_version is not None:
            result['TargetGatewayVersion'] = self.target_gateway_version
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.test_failover_status is not None:
            result['TestFailoverStatus'] = self.test_failover_status
        if self.test_recovered_instance_id is not None:
            result['TestRecoveredInstanceId'] = self.test_recovered_instance_id
        if self.test_recovered_instance_name is not None:
            result['TestRecoveredInstanceName'] = self.test_recovered_instance_name
        if self.test_recovered_ip_address is not None:
            result['TestRecoveredIpAddress'] = self.test_recovered_ip_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentPort') is not None:
            self.agent_port = m.get('AgentPort')
        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('Consistent') is not None:
            self.consistent = m.get('Consistent')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CrashConsistentPointPolicy') is not None:
            self.crash_consistent_point_policy = m.get('CrashConsistentPointPolicy')
        if m.get('Disks') is not None:
            self.disks = m.get('Disks')
        if m.get('Errno') is not None:
            self.errno = m.get('Errno')
        if m.get('FullSyncCurrentSize') is not None:
            self.full_sync_current_size = m.get('FullSyncCurrentSize')
        if m.get('FullSyncProgress') is not None:
            self.full_sync_progress = m.get('FullSyncProgress')
        if m.get('FullSyncStartTime') is not None:
            self.full_sync_start_time = m.get('FullSyncStartTime')
        if m.get('FullSyncTotalSize') is not None:
            self.full_sync_total_size = m.get('FullSyncTotalSize')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('IncrementalSyncStartTime') is not None:
            self.incremental_sync_start_time = m.get('IncrementalSyncStartTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('LatestRecoveryPointTime') is not None:
            self.latest_recovery_point_time = m.get('LatestRecoveryPointTime')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Operations') is not None:
            self.operations = m.get('Operations')
        if m.get('OriginalInstanceId') is not None:
            self.original_instance_id = m.get('OriginalInstanceId')
        if m.get('OsDetail') is not None:
            self.os_detail = m.get('OsDetail')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('PrimarySiteId') is not None:
            self.primary_site_id = m.get('PrimarySiteId')
        if m.get('RecoveredInstanceId') is not None:
            self.recovered_instance_id = m.get('RecoveredInstanceId')
        if m.get('RecoveredInstanceName') is not None:
            self.recovered_instance_name = m.get('RecoveredInstanceName')
        if m.get('RecoveredIpAddress') is not None:
            self.recovered_ip_address = m.get('RecoveredIpAddress')
        if m.get('RecoveryCpu') is not None:
            self.recovery_cpu = m.get('RecoveryCpu')
        if m.get('RecoveryEssdPerformanceLevel') is not None:
            self.recovery_essd_performance_level = m.get('RecoveryEssdPerformanceLevel')
        if m.get('RecoveryInstanceName') is not None:
            self.recovery_instance_name = m.get('RecoveryInstanceName')
        if m.get('RecoveryInstanceType') is not None:
            self.recovery_instance_type = m.get('RecoveryInstanceType')
        if m.get('RecoveryIpAddress') is not None:
            self.recovery_ip_address = m.get('RecoveryIpAddress')
        if m.get('RecoveryMemory') is not None:
            self.recovery_memory = m.get('RecoveryMemory')
        if m.get('RecoveryNetwork') is not None:
            self.recovery_network = m.get('RecoveryNetwork')
        if m.get('RecoveryPostScriptContent') is not None:
            self.recovery_post_script_content = m.get('RecoveryPostScriptContent')
        if m.get('RecoveryPostScriptType') is not None:
            self.recovery_post_script_type = m.get('RecoveryPostScriptType')
        if m.get('RecoveryReserveIp') is not None:
            self.recovery_reserve_ip = m.get('RecoveryReserveIp')
        if m.get('RecoveryUseDhcp') is not None:
            self.recovery_use_dhcp = m.get('RecoveryUseDhcp')
        if m.get('RecoveryUseEssd') is not None:
            self.recovery_use_essd = m.get('RecoveryUseEssd')
        if m.get('RecoveryUseSsd') is not None:
            self.recovery_use_ssd = m.get('RecoveryUseSsd')
        if m.get('ReplicationInfrastructureId') is not None:
            self.replication_infrastructure_id = m.get('ReplicationInfrastructureId')
        if m.get('ReplicationInfrastructureType') is not None:
            self.replication_infrastructure_type = m.get('ReplicationInfrastructureType')
        if m.get('ReplicationNetwork') is not None:
            self.replication_network = m.get('ReplicationNetwork')
        if m.get('ReplicationUseDhcp') is not None:
            self.replication_use_dhcp = m.get('ReplicationUseDhcp')
        if m.get('ReplicationUseEssd') is not None:
            self.replication_use_essd = m.get('ReplicationUseEssd')
        if m.get('ReplicationUseOriginalInstance') is not None:
            self.replication_use_original_instance = m.get('ReplicationUseOriginalInstance')
        if m.get('ReplicationUseSsd') is not None:
            self.replication_use_ssd = m.get('ReplicationUseSsd')
        if m.get('Rpo') is not None:
            self.rpo = m.get('Rpo')
        if m.get('SecondarySiteId') is not None:
            self.secondary_site_id = m.get('SecondarySiteId')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('SourceGatewayVersion') is not None:
            self.source_gateway_version = m.get('SourceGatewayVersion')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TargetGatewayVersion') is not None:
            self.target_gateway_version = m.get('TargetGatewayVersion')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TestFailoverStatus') is not None:
            self.test_failover_status = m.get('TestFailoverStatus')
        if m.get('TestRecoveredInstanceId') is not None:
            self.test_recovered_instance_id = m.get('TestRecoveredInstanceId')
        if m.get('TestRecoveredInstanceName') is not None:
            self.test_recovered_instance_name = m.get('TestRecoveredInstanceName')
        if m.get('TestRecoveredIpAddress') is not None:
            self.test_recovered_ip_address = m.get('TestRecoveredIpAddress')
        return self


class DescribeServersResponseBodyServers(TeaModel):
    def __init__(
        self,
        server: List[DescribeServersResponseBodyServersServer] = None,
    ):
        self.server = server

    def validate(self):
        if self.server:
            for k in self.server:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['server'] = []
        if self.server is not None:
            for k in self.server:
                result['server'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.server = []
        if m.get('server') is not None:
            for k in m.get('server'):
                temp_model = DescribeServersResponseBodyServersServer()
                self.server.append(temp_model.from_map(k))
        return self


class DescribeServersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        servers: DescribeServersResponseBodyServers = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.servers = servers
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.servers:
            self.servers.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.servers is not None:
            result['Servers'] = self.servers.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Servers') is not None:
            temp_model = DescribeServersResponseBodyServers()
            self.servers = temp_model.from_map(m['Servers'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeServersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeServersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeServersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSiteRequest(TeaModel):
    def __init__(
        self,
        site_id: str = None,
    ):
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        return self


class DescribeSiteResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        name: str = None,
        region_id: str = None,
        request_id: str = None,
        site_id: str = None,
        success: bool = None,
        type: str = None,
        user_security_group_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.code = code
        self.message = message
        self.name = name
        self.region_id = region_id
        self.request_id = request_id
        self.site_id = site_id
        self.success = success
        self.type = type
        self.user_security_group_id = user_security_group_id
        self.vpc_id = vpc_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.success is not None:
            result['Success'] = self.success
        if self.type is not None:
            result['Type'] = self.type
        if self.user_security_group_id is not None:
            result['UserSecurityGroupId'] = self.user_security_group_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserSecurityGroupId') is not None:
            self.user_security_group_id = m.get('UserSecurityGroupId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeSiteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSiteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeSiteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSitePairRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        site_pair_id: str = None,
    ):
        self.security_token = security_token
        self.site_pair_id = site_pair_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.site_pair_id is not None:
            result['SitePairId'] = self.site_pair_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SitePairId') is not None:
            self.site_pair_id = m.get('SitePairId')
        return self


class DescribeSitePairResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        created_time: int = None,
        message: str = None,
        primary_site_id: str = None,
        primary_site_name: str = None,
        request_id: str = None,
        secondary_site_id: str = None,
        secondary_site_name: str = None,
        site_pair_id: str = None,
        site_pair_type: str = None,
        success: bool = None,
        version: str = None,
    ):
        self.code = code
        self.created_time = created_time
        self.message = message
        self.primary_site_id = primary_site_id
        self.primary_site_name = primary_site_name
        self.request_id = request_id
        self.secondary_site_id = secondary_site_id
        self.secondary_site_name = secondary_site_name
        self.site_pair_id = site_pair_id
        self.site_pair_type = site_pair_type
        self.success = success
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.message is not None:
            result['Message'] = self.message
        if self.primary_site_id is not None:
            result['PrimarySiteId'] = self.primary_site_id
        if self.primary_site_name is not None:
            result['PrimarySiteName'] = self.primary_site_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secondary_site_id is not None:
            result['SecondarySiteId'] = self.secondary_site_id
        if self.secondary_site_name is not None:
            result['SecondarySiteName'] = self.secondary_site_name
        if self.site_pair_id is not None:
            result['SitePairId'] = self.site_pair_id
        if self.site_pair_type is not None:
            result['SitePairType'] = self.site_pair_type
        if self.success is not None:
            result['Success'] = self.success
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PrimarySiteId') is not None:
            self.primary_site_id = m.get('PrimarySiteId')
        if m.get('PrimarySiteName') is not None:
            self.primary_site_name = m.get('PrimarySiteName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecondarySiteId') is not None:
            self.secondary_site_id = m.get('SecondarySiteId')
        if m.get('SecondarySiteName') is not None:
            self.secondary_site_name = m.get('SecondarySiteName')
        if m.get('SitePairId') is not None:
            self.site_pair_id = m.get('SitePairId')
        if m.get('SitePairType') is not None:
            self.site_pair_type = m.get('SitePairType')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeSitePairResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSitePairResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeSitePairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSitePairStatisticsRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        site_pair_id: str = None,
    ):
        self.security_token = security_token
        self.site_pair_id = site_pair_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.site_pair_id is not None:
            result['SitePairId'] = self.site_pair_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SitePairId') is not None:
            self.site_pair_id = m.get('SitePairId')
        return self


class DescribeSitePairStatisticsResponseBodyPrimarySiteGatewayInfo(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        heartbeated_time: int = None,
        status: str = None,
        version: str = None,
    ):
        self.gateway_id = gateway_id
        self.heartbeated_time = heartbeated_time
        self.status = status
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.heartbeated_time is not None:
            result['HeartbeatedTime'] = self.heartbeated_time
        if self.status is not None:
            result['Status'] = self.status
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('HeartbeatedTime') is not None:
            self.heartbeated_time = m.get('HeartbeatedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeSitePairStatisticsResponseBodyPrimarySiteServersServer(TeaModel):
    def __init__(
        self,
        agent_version: str = None,
        connection_status: str = None,
        ip_address: str = None,
        server_id: str = None,
    ):
        self.agent_version = agent_version
        self.connection_status = connection_status
        self.ip_address = ip_address
        self.server_id = server_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        return self


class DescribeSitePairStatisticsResponseBodyPrimarySiteServers(TeaModel):
    def __init__(
        self,
        server: List[DescribeSitePairStatisticsResponseBodyPrimarySiteServersServer] = None,
    ):
        self.server = server

    def validate(self):
        if self.server:
            for k in self.server:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['server'] = []
        if self.server is not None:
            for k in self.server:
                result['server'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.server = []
        if m.get('server') is not None:
            for k in m.get('server'):
                temp_model = DescribeSitePairStatisticsResponseBodyPrimarySiteServersServer()
                self.server.append(temp_model.from_map(k))
        return self


class DescribeSitePairStatisticsResponseBodySecondarySiteGatewayInfo(TeaModel):
    def __init__(
        self,
        gateway_id: str = None,
        heartbeated_time: int = None,
        status: str = None,
        version: str = None,
    ):
        self.gateway_id = gateway_id
        self.heartbeated_time = heartbeated_time
        self.status = status
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id
        if self.heartbeated_time is not None:
            result['HeartbeatedTime'] = self.heartbeated_time
        if self.status is not None:
            result['Status'] = self.status
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')
        if m.get('HeartbeatedTime') is not None:
            self.heartbeated_time = m.get('HeartbeatedTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeSitePairStatisticsResponseBodySecondarySiteServersServer(TeaModel):
    def __init__(
        self,
        agent_version: str = None,
        connection_status: str = None,
        ip_address: str = None,
        server_id: str = None,
    ):
        self.agent_version = agent_version
        self.connection_status = connection_status
        self.ip_address = ip_address
        self.server_id = server_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        return self


class DescribeSitePairStatisticsResponseBodySecondarySiteServers(TeaModel):
    def __init__(
        self,
        server: List[DescribeSitePairStatisticsResponseBodySecondarySiteServersServer] = None,
    ):
        self.server = server

    def validate(self):
        if self.server:
            for k in self.server:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['server'] = []
        if self.server is not None:
            for k in self.server:
                result['server'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.server = []
        if m.get('server') is not None:
            for k in m.get('server'):
                temp_model = DescribeSitePairStatisticsResponseBodySecondarySiteServersServer()
                self.server.append(temp_model.from_map(k))
        return self


class DescribeSitePairStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        primary_site_gateway_info: DescribeSitePairStatisticsResponseBodyPrimarySiteGatewayInfo = None,
        primary_site_servers: DescribeSitePairStatisticsResponseBodyPrimarySiteServers = None,
        request_id: str = None,
        secondary_site_gateway_info: DescribeSitePairStatisticsResponseBodySecondarySiteGatewayInfo = None,
        secondary_site_servers: DescribeSitePairStatisticsResponseBodySecondarySiteServers = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.primary_site_gateway_info = primary_site_gateway_info
        self.primary_site_servers = primary_site_servers
        self.request_id = request_id
        self.secondary_site_gateway_info = secondary_site_gateway_info
        self.secondary_site_servers = secondary_site_servers
        self.success = success

    def validate(self):
        if self.primary_site_gateway_info:
            self.primary_site_gateway_info.validate()
        if self.primary_site_servers:
            self.primary_site_servers.validate()
        if self.secondary_site_gateway_info:
            self.secondary_site_gateway_info.validate()
        if self.secondary_site_servers:
            self.secondary_site_servers.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.primary_site_gateway_info is not None:
            result['PrimarySiteGatewayInfo'] = self.primary_site_gateway_info.to_map()
        if self.primary_site_servers is not None:
            result['PrimarySiteServers'] = self.primary_site_servers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secondary_site_gateway_info is not None:
            result['SecondarySiteGatewayInfo'] = self.secondary_site_gateway_info.to_map()
        if self.secondary_site_servers is not None:
            result['SecondarySiteServers'] = self.secondary_site_servers.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PrimarySiteGatewayInfo') is not None:
            temp_model = DescribeSitePairStatisticsResponseBodyPrimarySiteGatewayInfo()
            self.primary_site_gateway_info = temp_model.from_map(m['PrimarySiteGatewayInfo'])
        if m.get('PrimarySiteServers') is not None:
            temp_model = DescribeSitePairStatisticsResponseBodyPrimarySiteServers()
            self.primary_site_servers = temp_model.from_map(m['PrimarySiteServers'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecondarySiteGatewayInfo') is not None:
            temp_model = DescribeSitePairStatisticsResponseBodySecondarySiteGatewayInfo()
            self.secondary_site_gateway_info = temp_model.from_map(m['SecondarySiteGatewayInfo'])
        if m.get('SecondarySiteServers') is not None:
            temp_model = DescribeSitePairStatisticsResponseBodySecondarySiteServers()
            self.secondary_site_servers = temp_model.from_map(m['SecondarySiteServers'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSitePairStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSitePairStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeSitePairStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSitePairsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        site_pair_type: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.site_pair_type = site_pair_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.site_pair_type is not None:
            result['SitePairType'] = self.site_pair_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SitePairType') is not None:
            self.site_pair_type = m.get('SitePairType')
        return self


class DescribeSitePairsResponseBodySitePairsSitePairReplicationStatistics(TeaModel):
    def __init__(
        self,
        critical: int = None,
        healthy: int = None,
        not_applicable: int = None,
        warning: int = None,
    ):
        self.critical = critical
        self.healthy = healthy
        self.not_applicable = not_applicable
        self.warning = warning

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.critical is not None:
            result['Critical'] = self.critical
        if self.healthy is not None:
            result['Healthy'] = self.healthy
        if self.not_applicable is not None:
            result['NotApplicable'] = self.not_applicable
        if self.warning is not None:
            result['Warning'] = self.warning
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Critical') is not None:
            self.critical = m.get('Critical')
        if m.get('Healthy') is not None:
            self.healthy = m.get('Healthy')
        if m.get('NotApplicable') is not None:
            self.not_applicable = m.get('NotApplicable')
        if m.get('Warning') is not None:
            self.warning = m.get('Warning')
        return self


class DescribeSitePairsResponseBodySitePairsSitePair(TeaModel):
    def __init__(
        self,
        cloud_site_name: str = None,
        created_time: int = None,
        local_site_name: str = None,
        primary_site_id: str = None,
        primary_site_name: str = None,
        replication_statistics: DescribeSitePairsResponseBodySitePairsSitePairReplicationStatistics = None,
        secondary_site_id: str = None,
        secondary_site_name: str = None,
        server_count: int = None,
        site_pair_id: str = None,
        site_pair_type: str = None,
        version: str = None,
    ):
        self.cloud_site_name = cloud_site_name
        self.created_time = created_time
        self.local_site_name = local_site_name
        self.primary_site_id = primary_site_id
        self.primary_site_name = primary_site_name
        self.replication_statistics = replication_statistics
        self.secondary_site_id = secondary_site_id
        self.secondary_site_name = secondary_site_name
        self.server_count = server_count
        self.site_pair_id = site_pair_id
        self.site_pair_type = site_pair_type
        self.version = version

    def validate(self):
        if self.replication_statistics:
            self.replication_statistics.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_site_name is not None:
            result['CloudSiteName'] = self.cloud_site_name
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.local_site_name is not None:
            result['LocalSiteName'] = self.local_site_name
        if self.primary_site_id is not None:
            result['PrimarySiteId'] = self.primary_site_id
        if self.primary_site_name is not None:
            result['PrimarySiteName'] = self.primary_site_name
        if self.replication_statistics is not None:
            result['ReplicationStatistics'] = self.replication_statistics.to_map()
        if self.secondary_site_id is not None:
            result['SecondarySiteId'] = self.secondary_site_id
        if self.secondary_site_name is not None:
            result['SecondarySiteName'] = self.secondary_site_name
        if self.server_count is not None:
            result['ServerCount'] = self.server_count
        if self.site_pair_id is not None:
            result['SitePairId'] = self.site_pair_id
        if self.site_pair_type is not None:
            result['SitePairType'] = self.site_pair_type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudSiteName') is not None:
            self.cloud_site_name = m.get('CloudSiteName')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('LocalSiteName') is not None:
            self.local_site_name = m.get('LocalSiteName')
        if m.get('PrimarySiteId') is not None:
            self.primary_site_id = m.get('PrimarySiteId')
        if m.get('PrimarySiteName') is not None:
            self.primary_site_name = m.get('PrimarySiteName')
        if m.get('ReplicationStatistics') is not None:
            temp_model = DescribeSitePairsResponseBodySitePairsSitePairReplicationStatistics()
            self.replication_statistics = temp_model.from_map(m['ReplicationStatistics'])
        if m.get('SecondarySiteId') is not None:
            self.secondary_site_id = m.get('SecondarySiteId')
        if m.get('SecondarySiteName') is not None:
            self.secondary_site_name = m.get('SecondarySiteName')
        if m.get('ServerCount') is not None:
            self.server_count = m.get('ServerCount')
        if m.get('SitePairId') is not None:
            self.site_pair_id = m.get('SitePairId')
        if m.get('SitePairType') is not None:
            self.site_pair_type = m.get('SitePairType')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeSitePairsResponseBodySitePairs(TeaModel):
    def __init__(
        self,
        site_pair: List[DescribeSitePairsResponseBodySitePairsSitePair] = None,
    ):
        self.site_pair = site_pair

    def validate(self):
        if self.site_pair:
            for k in self.site_pair:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['sitePair'] = []
        if self.site_pair is not None:
            for k in self.site_pair:
                result['sitePair'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.site_pair = []
        if m.get('sitePair') is not None:
            for k in m.get('sitePair'):
                temp_model = DescribeSitePairsResponseBodySitePairsSitePair()
                self.site_pair.append(temp_model.from_map(k))
        return self


class DescribeSitePairsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        site_pairs: DescribeSitePairsResponseBodySitePairs = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.site_pairs = site_pairs
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.site_pairs:
            self.site_pairs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.site_pairs is not None:
            result['SitePairs'] = self.site_pairs.to_map()
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SitePairs') is not None:
            temp_model = DescribeSitePairsResponseBodySitePairs()
            self.site_pairs = temp_model.from_map(m['SitePairs'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSitePairsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSitePairsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeSitePairsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSummaryRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
    ):
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeSummaryResponseBodyReplicationDetailsCriticalServersCriticalServer(TeaModel):
    def __init__(
        self,
        connection_status: str = None,
        instance_id: str = None,
        rpo: int = None,
        server_id: str = None,
        site_pair_id: str = None,
        status: str = None,
    ):
        self.connection_status = connection_status
        self.instance_id = instance_id
        # RPO
        self.rpo = rpo
        self.server_id = server_id
        self.site_pair_id = site_pair_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rpo is not None:
            result['Rpo'] = self.rpo
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.site_pair_id is not None:
            result['SitePairId'] = self.site_pair_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Rpo') is not None:
            self.rpo = m.get('Rpo')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('SitePairId') is not None:
            self.site_pair_id = m.get('SitePairId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSummaryResponseBodyReplicationDetailsCriticalServers(TeaModel):
    def __init__(
        self,
        critical_server: List[DescribeSummaryResponseBodyReplicationDetailsCriticalServersCriticalServer] = None,
    ):
        self.critical_server = critical_server

    def validate(self):
        if self.critical_server:
            for k in self.critical_server:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['criticalServer'] = []
        if self.critical_server is not None:
            for k in self.critical_server:
                result['criticalServer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.critical_server = []
        if m.get('criticalServer') is not None:
            for k in m.get('criticalServer'):
                temp_model = DescribeSummaryResponseBodyReplicationDetailsCriticalServersCriticalServer()
                self.critical_server.append(temp_model.from_map(k))
        return self


class DescribeSummaryResponseBodyReplicationDetailsNotApplicableServersNotApplicableServer(TeaModel):
    def __init__(
        self,
        connection_status: str = None,
        instance_id: str = None,
        rpo: int = None,
        server_id: str = None,
        site_pair_id: str = None,
        status: str = None,
    ):
        self.connection_status = connection_status
        self.instance_id = instance_id
        # RPO
        self.rpo = rpo
        self.server_id = server_id
        self.site_pair_id = site_pair_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rpo is not None:
            result['Rpo'] = self.rpo
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.site_pair_id is not None:
            result['SitePairId'] = self.site_pair_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Rpo') is not None:
            self.rpo = m.get('Rpo')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('SitePairId') is not None:
            self.site_pair_id = m.get('SitePairId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSummaryResponseBodyReplicationDetailsNotApplicableServers(TeaModel):
    def __init__(
        self,
        not_applicable_server: List[DescribeSummaryResponseBodyReplicationDetailsNotApplicableServersNotApplicableServer] = None,
    ):
        self.not_applicable_server = not_applicable_server

    def validate(self):
        if self.not_applicable_server:
            for k in self.not_applicable_server:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['notApplicableServer'] = []
        if self.not_applicable_server is not None:
            for k in self.not_applicable_server:
                result['notApplicableServer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.not_applicable_server = []
        if m.get('notApplicableServer') is not None:
            for k in m.get('notApplicableServer'):
                temp_model = DescribeSummaryResponseBodyReplicationDetailsNotApplicableServersNotApplicableServer()
                self.not_applicable_server.append(temp_model.from_map(k))
        return self


class DescribeSummaryResponseBodyReplicationDetailsWarningServersWarningServer(TeaModel):
    def __init__(
        self,
        connection_status: str = None,
        instance_id: str = None,
        rpo: int = None,
        server_id: str = None,
        site_pair_id: str = None,
        status: str = None,
    ):
        self.connection_status = connection_status
        self.instance_id = instance_id
        # RPO
        self.rpo = rpo
        self.server_id = server_id
        self.site_pair_id = site_pair_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rpo is not None:
            result['Rpo'] = self.rpo
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.site_pair_id is not None:
            result['SitePairId'] = self.site_pair_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Rpo') is not None:
            self.rpo = m.get('Rpo')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('SitePairId') is not None:
            self.site_pair_id = m.get('SitePairId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeSummaryResponseBodyReplicationDetailsWarningServers(TeaModel):
    def __init__(
        self,
        warning_server: List[DescribeSummaryResponseBodyReplicationDetailsWarningServersWarningServer] = None,
    ):
        self.warning_server = warning_server

    def validate(self):
        if self.warning_server:
            for k in self.warning_server:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['warningServer'] = []
        if self.warning_server is not None:
            for k in self.warning_server:
                result['warningServer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.warning_server = []
        if m.get('warningServer') is not None:
            for k in m.get('warningServer'):
                temp_model = DescribeSummaryResponseBodyReplicationDetailsWarningServersWarningServer()
                self.warning_server.append(temp_model.from_map(k))
        return self


class DescribeSummaryResponseBodyReplicationDetails(TeaModel):
    def __init__(
        self,
        critical_servers: DescribeSummaryResponseBodyReplicationDetailsCriticalServers = None,
        not_applicable_servers: DescribeSummaryResponseBodyReplicationDetailsNotApplicableServers = None,
        warning_servers: DescribeSummaryResponseBodyReplicationDetailsWarningServers = None,
    ):
        self.critical_servers = critical_servers
        self.not_applicable_servers = not_applicable_servers
        self.warning_servers = warning_servers

    def validate(self):
        if self.critical_servers:
            self.critical_servers.validate()
        if self.not_applicable_servers:
            self.not_applicable_servers.validate()
        if self.warning_servers:
            self.warning_servers.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.critical_servers is not None:
            result['CriticalServers'] = self.critical_servers.to_map()
        if self.not_applicable_servers is not None:
            result['NotApplicableServers'] = self.not_applicable_servers.to_map()
        if self.warning_servers is not None:
            result['WarningServers'] = self.warning_servers.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CriticalServers') is not None:
            temp_model = DescribeSummaryResponseBodyReplicationDetailsCriticalServers()
            self.critical_servers = temp_model.from_map(m['CriticalServers'])
        if m.get('NotApplicableServers') is not None:
            temp_model = DescribeSummaryResponseBodyReplicationDetailsNotApplicableServers()
            self.not_applicable_servers = temp_model.from_map(m['NotApplicableServers'])
        if m.get('WarningServers') is not None:
            temp_model = DescribeSummaryResponseBodyReplicationDetailsWarningServers()
            self.warning_servers = temp_model.from_map(m['WarningServers'])
        return self


class DescribeSummaryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        db_server_count: int = None,
        message: str = None,
        replication_details: DescribeSummaryResponseBodyReplicationDetails = None,
        request_id: str = None,
        server_count: int = None,
        site_count: int = None,
        success: bool = None,
        total_size: int = None,
    ):
        self.code = code
        # -\
        self.db_server_count = db_server_count
        self.message = message
        self.replication_details = replication_details
        self.request_id = request_id
        self.server_count = server_count
        self.site_count = site_count
        self.success = success
        self.total_size = total_size

    def validate(self):
        if self.replication_details:
            self.replication_details.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.db_server_count is not None:
            result['DbServerCount'] = self.db_server_count
        if self.message is not None:
            result['Message'] = self.message
        if self.replication_details is not None:
            result['ReplicationDetails'] = self.replication_details.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_count is not None:
            result['ServerCount'] = self.server_count
        if self.site_count is not None:
            result['SiteCount'] = self.site_count
        if self.success is not None:
            result['Success'] = self.success
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DbServerCount') is not None:
            self.db_server_count = m.get('DbServerCount')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ReplicationDetails') is not None:
            temp_model = DescribeSummaryResponseBodyReplicationDetails()
            self.replication_details = temp_model.from_map(m['ReplicationDetails'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerCount') is not None:
            self.server_count = m.get('ServerCount')
        if m.get('SiteCount') is not None:
            self.site_count = m.get('SiteCount')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class DescribeSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSummaryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        content: str = None,
        created_time: int = None,
        message: str = None,
        name: str = None,
        progress: int = None,
        request_id: str = None,
        status_code: str = None,
        success: bool = None,
        task_id: str = None,
        updated_time: int = None,
    ):
        self.code = code
        self.content = content
        self.created_time = created_time
        self.message = message
        self.name = name
        self.progress = progress
        self.request_id = request_id
        self.status_code = status_code
        self.success = success
        self.task_id = task_id
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class DescribeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTasksRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        security_token: str = None,
        site_pair_id: str = None,
        sort_by: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.security_token = security_token
        self.site_pair_id = site_pair_id
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.site_pair_id is not None:
            result['SitePairId'] = self.site_pair_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SitePairId') is not None:
            self.site_pair_id = m.get('SitePairId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        return self


class DescribeTasksResponseBodyTasksTask(TeaModel):
    def __init__(
        self,
        created_time: int = None,
        name: str = None,
        progress: int = None,
        status_code: str = None,
        target_name: str = None,
        task_id: str = None,
        updated_time: int = None,
    ):
        self.created_time = created_time
        self.name = name
        self.progress = progress
        self.status_code = status_code
        self.target_name = target_name
        self.task_id = task_id
        self.updated_time = updated_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.name is not None:
            result['Name'] = self.name
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        if self.target_name is not None:
            result['TargetName'] = self.target_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')
        return self


class DescribeTasksResponseBodyTasks(TeaModel):
    def __init__(
        self,
        task: List[DescribeTasksResponseBodyTasksTask] = None,
    ):
        self.task = task

    def validate(self):
        if self.task:
            for k in self.task:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['task'] = []
        if self.task is not None:
            for k in self.task:
                result['task'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task = []
        if m.get('task') is not None:
            for k in m.get('task'):
                temp_model = DescribeTasksResponseBodyTasksTask()
                self.task.append(temp_model.from_map(k))
        return self


class DescribeTasksResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        tasks: DescribeTasksResponseBodyTasks = None,
        total_count: int = None,
    ):
        self.code = code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.tasks = tasks
        self.total_count = total_count

    def validate(self):
        if self.tasks:
            self.tasks.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.tasks is not None:
            result['Tasks'] = self.tasks.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Tasks') is not None:
            temp_model = DescribeTasksResponseBodyTasks()
            self.tasks = temp_model.from_map(m['Tasks'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DescribeTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableReplicationRequest(TeaModel):
    def __init__(
        self,
        server_id: str = None,
    ):
        self.server_id = server_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        return self


class DisableReplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DisableReplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableReplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = DisableReplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableReplicationRequest(TeaModel):
    def __init__(
        self,
        crash_consistent_point_policy: str = None,
        recovery_network: str = None,
        replication_network: str = None,
        replication_use_essd: bool = None,
        replication_use_ssd: bool = None,
        server_id: str = None,
    ):
        self.crash_consistent_point_policy = crash_consistent_point_policy
        self.recovery_network = recovery_network
        self.replication_network = replication_network
        self.replication_use_essd = replication_use_essd
        self.replication_use_ssd = replication_use_ssd
        self.server_id = server_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crash_consistent_point_policy is not None:
            result['CrashConsistentPointPolicy'] = self.crash_consistent_point_policy
        if self.recovery_network is not None:
            result['RecoveryNetwork'] = self.recovery_network
        if self.replication_network is not None:
            result['ReplicationNetwork'] = self.replication_network
        if self.replication_use_essd is not None:
            result['ReplicationUseEssd'] = self.replication_use_essd
        if self.replication_use_ssd is not None:
            result['ReplicationUseSsd'] = self.replication_use_ssd
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CrashConsistentPointPolicy') is not None:
            self.crash_consistent_point_policy = m.get('CrashConsistentPointPolicy')
        if m.get('RecoveryNetwork') is not None:
            self.recovery_network = m.get('RecoveryNetwork')
        if m.get('ReplicationNetwork') is not None:
            self.replication_network = m.get('ReplicationNetwork')
        if m.get('ReplicationUseEssd') is not None:
            self.replication_use_essd = m.get('ReplicationUseEssd')
        if m.get('ReplicationUseSsd') is not None:
            self.replication_use_ssd = m.get('ReplicationUseSsd')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        return self


class EnableReplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableReplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableReplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = EnableReplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FailbackRequest(TeaModel):
    def __init__(
        self,
        recovery_cpu: int = None,
        recovery_infrastructure_id: str = None,
        recovery_instance_name: str = None,
        recovery_instance_type: str = None,
        recovery_ip_address: str = None,
        recovery_memory: int = None,
        recovery_network: str = None,
        recovery_point_id: str = None,
        recovery_post_script_content: str = None,
        recovery_post_script_type: str = None,
        recovery_reserve_ip: bool = None,
        recovery_use_dhcp: bool = None,
        security_token: str = None,
        server_id: str = None,
    ):
        self.recovery_cpu = recovery_cpu
        self.recovery_infrastructure_id = recovery_infrastructure_id
        self.recovery_instance_name = recovery_instance_name
        self.recovery_instance_type = recovery_instance_type
        self.recovery_ip_address = recovery_ip_address
        self.recovery_memory = recovery_memory
        self.recovery_network = recovery_network
        self.recovery_point_id = recovery_point_id
        self.recovery_post_script_content = recovery_post_script_content
        self.recovery_post_script_type = recovery_post_script_type
        self.recovery_reserve_ip = recovery_reserve_ip
        self.recovery_use_dhcp = recovery_use_dhcp
        self.security_token = security_token
        self.server_id = server_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recovery_cpu is not None:
            result['RecoveryCpu'] = self.recovery_cpu
        if self.recovery_infrastructure_id is not None:
            result['RecoveryInfrastructureId'] = self.recovery_infrastructure_id
        if self.recovery_instance_name is not None:
            result['RecoveryInstanceName'] = self.recovery_instance_name
        if self.recovery_instance_type is not None:
            result['RecoveryInstanceType'] = self.recovery_instance_type
        if self.recovery_ip_address is not None:
            result['RecoveryIpAddress'] = self.recovery_ip_address
        if self.recovery_memory is not None:
            result['RecoveryMemory'] = self.recovery_memory
        if self.recovery_network is not None:
            result['RecoveryNetwork'] = self.recovery_network
        if self.recovery_point_id is not None:
            result['RecoveryPointId'] = self.recovery_point_id
        if self.recovery_post_script_content is not None:
            result['RecoveryPostScriptContent'] = self.recovery_post_script_content
        if self.recovery_post_script_type is not None:
            result['RecoveryPostScriptType'] = self.recovery_post_script_type
        if self.recovery_reserve_ip is not None:
            result['RecoveryReserveIp'] = self.recovery_reserve_ip
        if self.recovery_use_dhcp is not None:
            result['RecoveryUseDhcp'] = self.recovery_use_dhcp
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RecoveryCpu') is not None:
            self.recovery_cpu = m.get('RecoveryCpu')
        if m.get('RecoveryInfrastructureId') is not None:
            self.recovery_infrastructure_id = m.get('RecoveryInfrastructureId')
        if m.get('RecoveryInstanceName') is not None:
            self.recovery_instance_name = m.get('RecoveryInstanceName')
        if m.get('RecoveryInstanceType') is not None:
            self.recovery_instance_type = m.get('RecoveryInstanceType')
        if m.get('RecoveryIpAddress') is not None:
            self.recovery_ip_address = m.get('RecoveryIpAddress')
        if m.get('RecoveryMemory') is not None:
            self.recovery_memory = m.get('RecoveryMemory')
        if m.get('RecoveryNetwork') is not None:
            self.recovery_network = m.get('RecoveryNetwork')
        if m.get('RecoveryPointId') is not None:
            self.recovery_point_id = m.get('RecoveryPointId')
        if m.get('RecoveryPostScriptContent') is not None:
            self.recovery_post_script_content = m.get('RecoveryPostScriptContent')
        if m.get('RecoveryPostScriptType') is not None:
            self.recovery_post_script_type = m.get('RecoveryPostScriptType')
        if m.get('RecoveryReserveIp') is not None:
            self.recovery_reserve_ip = m.get('RecoveryReserveIp')
        if m.get('RecoveryUseDhcp') is not None:
            self.recovery_use_dhcp = m.get('RecoveryUseDhcp')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        return self


class FailbackResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class FailbackResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FailbackResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = FailbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ForcedFailoverRequest(TeaModel):
    def __init__(
        self,
        eip_address_id: str = None,
        recovery_cpu: int = None,
        recovery_essd_performance_level: str = None,
        recovery_instance_name: str = None,
        recovery_instance_type: str = None,
        recovery_ip_address: str = None,
        recovery_memory: int = None,
        recovery_network: str = None,
        recovery_point_id: str = None,
        recovery_point_time: int = None,
        recovery_post_script_content: str = None,
        recovery_post_script_type: str = None,
        recovery_reserve_ip: bool = None,
        recovery_use_dhcp: bool = None,
        recovery_use_essd: bool = None,
        recovery_use_ssd: bool = None,
        security_token: str = None,
        server_id: str = None,
    ):
        self.eip_address_id = eip_address_id
        self.recovery_cpu = recovery_cpu
        self.recovery_essd_performance_level = recovery_essd_performance_level
        self.recovery_instance_name = recovery_instance_name
        self.recovery_instance_type = recovery_instance_type
        self.recovery_ip_address = recovery_ip_address
        self.recovery_memory = recovery_memory
        self.recovery_network = recovery_network
        self.recovery_point_id = recovery_point_id
        self.recovery_point_time = recovery_point_time
        self.recovery_post_script_content = recovery_post_script_content
        self.recovery_post_script_type = recovery_post_script_type
        self.recovery_reserve_ip = recovery_reserve_ip
        self.recovery_use_dhcp = recovery_use_dhcp
        self.recovery_use_essd = recovery_use_essd
        self.recovery_use_ssd = recovery_use_ssd
        self.security_token = security_token
        self.server_id = server_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eip_address_id is not None:
            result['EipAddressId'] = self.eip_address_id
        if self.recovery_cpu is not None:
            result['RecoveryCpu'] = self.recovery_cpu
        if self.recovery_essd_performance_level is not None:
            result['RecoveryEssdPerformanceLevel'] = self.recovery_essd_performance_level
        if self.recovery_instance_name is not None:
            result['RecoveryInstanceName'] = self.recovery_instance_name
        if self.recovery_instance_type is not None:
            result['RecoveryInstanceType'] = self.recovery_instance_type
        if self.recovery_ip_address is not None:
            result['RecoveryIpAddress'] = self.recovery_ip_address
        if self.recovery_memory is not None:
            result['RecoveryMemory'] = self.recovery_memory
        if self.recovery_network is not None:
            result['RecoveryNetwork'] = self.recovery_network
        if self.recovery_point_id is not None:
            result['RecoveryPointId'] = self.recovery_point_id
        if self.recovery_point_time is not None:
            result['RecoveryPointTime'] = self.recovery_point_time
        if self.recovery_post_script_content is not None:
            result['RecoveryPostScriptContent'] = self.recovery_post_script_content
        if self.recovery_post_script_type is not None:
            result['RecoveryPostScriptType'] = self.recovery_post_script_type
        if self.recovery_reserve_ip is not None:
            result['RecoveryReserveIp'] = self.recovery_reserve_ip
        if self.recovery_use_dhcp is not None:
            result['RecoveryUseDhcp'] = self.recovery_use_dhcp
        if self.recovery_use_essd is not None:
            result['RecoveryUseEssd'] = self.recovery_use_essd
        if self.recovery_use_ssd is not None:
            result['RecoveryUseSsd'] = self.recovery_use_ssd
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipAddressId') is not None:
            self.eip_address_id = m.get('EipAddressId')
        if m.get('RecoveryCpu') is not None:
            self.recovery_cpu = m.get('RecoveryCpu')
        if m.get('RecoveryEssdPerformanceLevel') is not None:
            self.recovery_essd_performance_level = m.get('RecoveryEssdPerformanceLevel')
        if m.get('RecoveryInstanceName') is not None:
            self.recovery_instance_name = m.get('RecoveryInstanceName')
        if m.get('RecoveryInstanceType') is not None:
            self.recovery_instance_type = m.get('RecoveryInstanceType')
        if m.get('RecoveryIpAddress') is not None:
            self.recovery_ip_address = m.get('RecoveryIpAddress')
        if m.get('RecoveryMemory') is not None:
            self.recovery_memory = m.get('RecoveryMemory')
        if m.get('RecoveryNetwork') is not None:
            self.recovery_network = m.get('RecoveryNetwork')
        if m.get('RecoveryPointId') is not None:
            self.recovery_point_id = m.get('RecoveryPointId')
        if m.get('RecoveryPointTime') is not None:
            self.recovery_point_time = m.get('RecoveryPointTime')
        if m.get('RecoveryPostScriptContent') is not None:
            self.recovery_post_script_content = m.get('RecoveryPostScriptContent')
        if m.get('RecoveryPostScriptType') is not None:
            self.recovery_post_script_type = m.get('RecoveryPostScriptType')
        if m.get('RecoveryReserveIp') is not None:
            self.recovery_reserve_ip = m.get('RecoveryReserveIp')
        if m.get('RecoveryUseDhcp') is not None:
            self.recovery_use_dhcp = m.get('RecoveryUseDhcp')
        if m.get('RecoveryUseEssd') is not None:
            self.recovery_use_essd = m.get('RecoveryUseEssd')
        if m.get('RecoveryUseSsd') is not None:
            self.recovery_use_ssd = m.get('RecoveryUseSsd')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        return self


class ForcedFailoverResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ForcedFailoverResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ForcedFailoverResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ForcedFailoverResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterServersRequest(TeaModel):
    def __init__(
        self,
        agent_port: int = None,
        server_instances_info: str = None,
        site_pair_id: str = None,
    ):
        self.agent_port = agent_port
        self.server_instances_info = server_instances_info
        self.site_pair_id = site_pair_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_port is not None:
            result['AgentPort'] = self.agent_port
        if self.server_instances_info is not None:
            result['ServerInstancesInfo'] = self.server_instances_info
        if self.site_pair_id is not None:
            result['SitePairId'] = self.site_pair_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentPort') is not None:
            self.agent_port = m.get('AgentPort')
        if m.get('ServerInstancesInfo') is not None:
            self.server_instances_info = m.get('ServerInstancesInfo')
        if m.get('SitePairId') is not None:
            self.site_pair_id = m.get('SitePairId')
        return self


class RegisterServersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class RegisterServersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RegisterServersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = RegisterServersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReversedDisableReplicationRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        server_id: str = None,
    ):
        self.security_token = security_token
        self.server_id = server_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        return self


class ReversedDisableReplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReversedDisableReplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReversedDisableReplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ReversedDisableReplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReversedEnableReplicationRequest(TeaModel):
    def __init__(
        self,
        app_consistent_point_policy: str = None,
        crash_consistent_point_policy: str = None,
        recovery_network: str = None,
        replication_compute_resource: str = None,
        replication_datastore: str = None,
        replication_dns: str = None,
        replication_gateway: str = None,
        replication_infrastructure_id: str = None,
        replication_ip_address: str = None,
        replication_location: str = None,
        replication_net_mask: str = None,
        replication_network: str = None,
        replication_use_dhcp: bool = None,
        replication_use_original_instance: bool = None,
        security_token: str = None,
        server_id: str = None,
        shadow_instance_type: str = None,
    ):
        # -\
        self.app_consistent_point_policy = app_consistent_point_policy
        # -\
        self.crash_consistent_point_policy = crash_consistent_point_policy
        self.recovery_network = recovery_network
        # -\
        self.replication_compute_resource = replication_compute_resource
        # -\
        self.replication_datastore = replication_datastore
        # -\
        self.replication_dns = replication_dns
        # -\
        self.replication_gateway = replication_gateway
        self.replication_infrastructure_id = replication_infrastructure_id
        # -\
        self.replication_ip_address = replication_ip_address
        # -\
        self.replication_location = replication_location
        # -\
        self.replication_net_mask = replication_net_mask
        self.replication_network = replication_network
        # -\
        self.replication_use_dhcp = replication_use_dhcp
        self.replication_use_original_instance = replication_use_original_instance
        self.security_token = security_token
        self.server_id = server_id
        # -\
        self.shadow_instance_type = shadow_instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_consistent_point_policy is not None:
            result['AppConsistentPointPolicy'] = self.app_consistent_point_policy
        if self.crash_consistent_point_policy is not None:
            result['CrashConsistentPointPolicy'] = self.crash_consistent_point_policy
        if self.recovery_network is not None:
            result['RecoveryNetwork'] = self.recovery_network
        if self.replication_compute_resource is not None:
            result['ReplicationComputeResource'] = self.replication_compute_resource
        if self.replication_datastore is not None:
            result['ReplicationDatastore'] = self.replication_datastore
        if self.replication_dns is not None:
            result['ReplicationDns'] = self.replication_dns
        if self.replication_gateway is not None:
            result['ReplicationGateway'] = self.replication_gateway
        if self.replication_infrastructure_id is not None:
            result['ReplicationInfrastructureId'] = self.replication_infrastructure_id
        if self.replication_ip_address is not None:
            result['ReplicationIpAddress'] = self.replication_ip_address
        if self.replication_location is not None:
            result['ReplicationLocation'] = self.replication_location
        if self.replication_net_mask is not None:
            result['ReplicationNetMask'] = self.replication_net_mask
        if self.replication_network is not None:
            result['ReplicationNetwork'] = self.replication_network
        if self.replication_use_dhcp is not None:
            result['ReplicationUseDhcp'] = self.replication_use_dhcp
        if self.replication_use_original_instance is not None:
            result['ReplicationUseOriginalInstance'] = self.replication_use_original_instance
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.shadow_instance_type is not None:
            result['ShadowInstanceType'] = self.shadow_instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppConsistentPointPolicy') is not None:
            self.app_consistent_point_policy = m.get('AppConsistentPointPolicy')
        if m.get('CrashConsistentPointPolicy') is not None:
            self.crash_consistent_point_policy = m.get('CrashConsistentPointPolicy')
        if m.get('RecoveryNetwork') is not None:
            self.recovery_network = m.get('RecoveryNetwork')
        if m.get('ReplicationComputeResource') is not None:
            self.replication_compute_resource = m.get('ReplicationComputeResource')
        if m.get('ReplicationDatastore') is not None:
            self.replication_datastore = m.get('ReplicationDatastore')
        if m.get('ReplicationDns') is not None:
            self.replication_dns = m.get('ReplicationDns')
        if m.get('ReplicationGateway') is not None:
            self.replication_gateway = m.get('ReplicationGateway')
        if m.get('ReplicationInfrastructureId') is not None:
            self.replication_infrastructure_id = m.get('ReplicationInfrastructureId')
        if m.get('ReplicationIpAddress') is not None:
            self.replication_ip_address = m.get('ReplicationIpAddress')
        if m.get('ReplicationLocation') is not None:
            self.replication_location = m.get('ReplicationLocation')
        if m.get('ReplicationNetMask') is not None:
            self.replication_net_mask = m.get('ReplicationNetMask')
        if m.get('ReplicationNetwork') is not None:
            self.replication_network = m.get('ReplicationNetwork')
        if m.get('ReplicationUseDhcp') is not None:
            self.replication_use_dhcp = m.get('ReplicationUseDhcp')
        if m.get('ReplicationUseOriginalInstance') is not None:
            self.replication_use_original_instance = m.get('ReplicationUseOriginalInstance')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('ShadowInstanceType') is not None:
            self.shadow_instance_type = m.get('ShadowInstanceType')
        return self


class ReversedEnableReplicationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ReversedEnableReplicationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReversedEnableReplicationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = ReversedEnableReplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TestCleanupRequest(TeaModel):
    def __init__(
        self,
        server_id: str = None,
    ):
        self.server_id = server_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        return self


class TestCleanupResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class TestCleanupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TestCleanupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = TestCleanupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TestFailoverRequest(TeaModel):
    def __init__(
        self,
        eip_address_id: str = None,
        recovery_cpu: int = None,
        recovery_essd_performance_level: str = None,
        recovery_instance_name: str = None,
        recovery_instance_type: str = None,
        recovery_ip_address: str = None,
        recovery_memory: int = None,
        recovery_network: str = None,
        recovery_point_id: str = None,
        recovery_point_time: int = None,
        recovery_post_script_content: str = None,
        recovery_post_script_type: str = None,
        recovery_reserve_ip: bool = None,
        recovery_use_dhcp: bool = None,
        recovery_use_essd: bool = None,
        recovery_use_ssd: bool = None,
        security_token: str = None,
        server_id: str = None,
    ):
        self.eip_address_id = eip_address_id
        self.recovery_cpu = recovery_cpu
        self.recovery_essd_performance_level = recovery_essd_performance_level
        self.recovery_instance_name = recovery_instance_name
        self.recovery_instance_type = recovery_instance_type
        self.recovery_ip_address = recovery_ip_address
        self.recovery_memory = recovery_memory
        self.recovery_network = recovery_network
        self.recovery_point_id = recovery_point_id
        self.recovery_point_time = recovery_point_time
        self.recovery_post_script_content = recovery_post_script_content
        self.recovery_post_script_type = recovery_post_script_type
        self.recovery_reserve_ip = recovery_reserve_ip
        self.recovery_use_dhcp = recovery_use_dhcp
        self.recovery_use_essd = recovery_use_essd
        self.recovery_use_ssd = recovery_use_ssd
        self.security_token = security_token
        self.server_id = server_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eip_address_id is not None:
            result['EipAddressId'] = self.eip_address_id
        if self.recovery_cpu is not None:
            result['RecoveryCpu'] = self.recovery_cpu
        if self.recovery_essd_performance_level is not None:
            result['RecoveryEssdPerformanceLevel'] = self.recovery_essd_performance_level
        if self.recovery_instance_name is not None:
            result['RecoveryInstanceName'] = self.recovery_instance_name
        if self.recovery_instance_type is not None:
            result['RecoveryInstanceType'] = self.recovery_instance_type
        if self.recovery_ip_address is not None:
            result['RecoveryIpAddress'] = self.recovery_ip_address
        if self.recovery_memory is not None:
            result['RecoveryMemory'] = self.recovery_memory
        if self.recovery_network is not None:
            result['RecoveryNetwork'] = self.recovery_network
        if self.recovery_point_id is not None:
            result['RecoveryPointId'] = self.recovery_point_id
        if self.recovery_point_time is not None:
            result['RecoveryPointTime'] = self.recovery_point_time
        if self.recovery_post_script_content is not None:
            result['RecoveryPostScriptContent'] = self.recovery_post_script_content
        if self.recovery_post_script_type is not None:
            result['RecoveryPostScriptType'] = self.recovery_post_script_type
        if self.recovery_reserve_ip is not None:
            result['RecoveryReserveIp'] = self.recovery_reserve_ip
        if self.recovery_use_dhcp is not None:
            result['RecoveryUseDhcp'] = self.recovery_use_dhcp
        if self.recovery_use_essd is not None:
            result['RecoveryUseEssd'] = self.recovery_use_essd
        if self.recovery_use_ssd is not None:
            result['RecoveryUseSsd'] = self.recovery_use_ssd
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipAddressId') is not None:
            self.eip_address_id = m.get('EipAddressId')
        if m.get('RecoveryCpu') is not None:
            self.recovery_cpu = m.get('RecoveryCpu')
        if m.get('RecoveryEssdPerformanceLevel') is not None:
            self.recovery_essd_performance_level = m.get('RecoveryEssdPerformanceLevel')
        if m.get('RecoveryInstanceName') is not None:
            self.recovery_instance_name = m.get('RecoveryInstanceName')
        if m.get('RecoveryInstanceType') is not None:
            self.recovery_instance_type = m.get('RecoveryInstanceType')
        if m.get('RecoveryIpAddress') is not None:
            self.recovery_ip_address = m.get('RecoveryIpAddress')
        if m.get('RecoveryMemory') is not None:
            self.recovery_memory = m.get('RecoveryMemory')
        if m.get('RecoveryNetwork') is not None:
            self.recovery_network = m.get('RecoveryNetwork')
        if m.get('RecoveryPointId') is not None:
            self.recovery_point_id = m.get('RecoveryPointId')
        if m.get('RecoveryPointTime') is not None:
            self.recovery_point_time = m.get('RecoveryPointTime')
        if m.get('RecoveryPostScriptContent') is not None:
            self.recovery_post_script_content = m.get('RecoveryPostScriptContent')
        if m.get('RecoveryPostScriptType') is not None:
            self.recovery_post_script_type = m.get('RecoveryPostScriptType')
        if m.get('RecoveryReserveIp') is not None:
            self.recovery_reserve_ip = m.get('RecoveryReserveIp')
        if m.get('RecoveryUseDhcp') is not None:
            self.recovery_use_dhcp = m.get('RecoveryUseDhcp')
        if m.get('RecoveryUseEssd') is not None:
            self.recovery_use_essd = m.get('RecoveryUseEssd')
        if m.get('RecoveryUseSsd') is not None:
            self.recovery_use_ssd = m.get('RecoveryUseSsd')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        return self


class TestFailoverResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class TestFailoverResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TestFailoverResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = TestFailoverResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TriggerReversedRegisterRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        server_id: str = None,
    ):
        self.security_token = security_token
        self.server_id = server_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        return self


class TriggerReversedRegisterResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class TriggerReversedRegisterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TriggerReversedRegisterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = TriggerReversedRegisterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnregisterServerRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        server_id: str = None,
    ):
        self.security_token = security_token
        self.server_id = server_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        return self


class UnregisterServerResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnregisterServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnregisterServerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UnregisterServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRecoveryPlanRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        name: str = None,
        recovery_plan_id: str = None,
    ):
        self.content = content
        self.name = name
        self.recovery_plan_id = recovery_plan_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.name is not None:
            result['Name'] = self.name
        if self.recovery_plan_id is not None:
            result['RecoveryPlanId'] = self.recovery_plan_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RecoveryPlanId') is not None:
            self.recovery_plan_id = m.get('RecoveryPlanId')
        return self


class UpdateRecoveryPlanResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class UpdateRecoveryPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRecoveryPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
            temp_model = UpdateRecoveryPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


