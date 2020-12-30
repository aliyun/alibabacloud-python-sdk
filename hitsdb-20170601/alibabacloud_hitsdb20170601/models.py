# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateHiTSDBInstanceRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        region_id: str = None,
        app_key: str = None,
        zone_id: str = None,
        instance_name: str = None,
        instance_alias: str = None,
        instance_class: str = None,
        instance_storage: str = None,
        pay_type: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        max_timeline_limit: str = None,
        instance_tps: str = None,
        engine_type: str = None,
        max_series_per_database: str = None,
        max_database_limit: str = None,
        pricing_cycle: str = None,
        duration: str = None,
        tsdbversion: str = None,
        disk_category: str = None,
        client_token: str = None,
    ):
        self.security_token = security_token
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.region_id = region_id
        self.app_key = app_key
        self.zone_id = zone_id
        self.instance_name = instance_name
        self.instance_alias = instance_alias
        self.instance_class = instance_class
        self.instance_storage = instance_storage
        self.pay_type = pay_type
        self.vpcid = vpcid
        self.v_switch_id = v_switch_id
        self.max_timeline_limit = max_timeline_limit
        self.instance_tps = instance_tps
        self.engine_type = engine_type
        self.max_series_per_database = max_series_per_database
        self.max_database_limit = max_database_limit
        self.pricing_cycle = pricing_cycle
        self.duration = duration
        self.tsdbversion = tsdbversion
        self.disk_category = disk_category
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_storage is not None:
            result['InstanceStorage'] = self.instance_storage
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.max_timeline_limit is not None:
            result['MaxTimelineLimit'] = self.max_timeline_limit
        if self.instance_tps is not None:
            result['InstanceTps'] = self.instance_tps
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.max_series_per_database is not None:
            result['MaxSeriesPerDatabase'] = self.max_series_per_database
        if self.max_database_limit is not None:
            result['MaxDatabaseLimit'] = self.max_database_limit
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.tsdbversion is not None:
            result['TSDBVersion'] = self.tsdbversion
        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceStorage') is not None:
            self.instance_storage = m.get('InstanceStorage')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('MaxTimelineLimit') is not None:
            self.max_timeline_limit = m.get('MaxTimelineLimit')
        if m.get('InstanceTps') is not None:
            self.instance_tps = m.get('InstanceTps')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('MaxSeriesPerDatabase') is not None:
            self.max_series_per_database = m.get('MaxSeriesPerDatabase')
        if m.get('MaxDatabaseLimit') is not None:
            self.max_database_limit = m.get('MaxDatabaseLimit')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('TSDBVersion') is not None:
            self.tsdbversion = m.get('TSDBVersion')
        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateHiTSDBInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_id: str = None,
        order_id: int = None,
    ):
        self.request_id = request_id
        self.instance_id = instance_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateHiTSDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateHiTSDBInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateHiTSDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHiTSDBInstanceRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        app_key: str = None,
        instance_id: str = None,
    ):
        self.security_token = security_token
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.app_key = app_key
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteHiTSDBInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteHiTSDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteHiTSDBInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteHiTSDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHiTSDBInstanceRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        app_key: str = None,
        instance_id: str = None,
    ):
        self.security_token = security_token
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.app_key = app_key
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeHiTSDBInstanceResponseBodySecurityIpList(TeaModel):
    def __init__(
        self,
        ip: str = None,
    ):
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeHiTSDBInstanceResponseBody(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        gmt_created: str = None,
        cpu_number: str = None,
        mem_size: str = None,
        network_type: str = None,
        gmt_expire: str = None,
        instance_alias: str = None,
        instance_status: str = None,
        expired_time: int = None,
        payment_type: str = None,
        max_timeline_limit: str = None,
        public_connection_string: str = None,
        engine_type: str = None,
        instance_tps: str = None,
        status: str = None,
        instance_storage: str = None,
        request_id: str = None,
        zone_id: str = None,
        instance_id: str = None,
        create_time: int = None,
        disk_category: str = None,
        instance_class: str = None,
        vswitch_id: str = None,
        series: int = None,
        vpc_id: str = None,
        charge_type: str = None,
        security_ip_list: List[DescribeHiTSDBInstanceResponseBodySecurityIpList] = None,
        instance_description: str = None,
        region_id: str = None,
        connection_string: str = None,
    ):
        self.auto_renew = auto_renew
        self.gmt_created = gmt_created
        self.cpu_number = cpu_number
        self.mem_size = mem_size
        self.network_type = network_type
        self.gmt_expire = gmt_expire
        self.instance_alias = instance_alias
        self.instance_status = instance_status
        self.expired_time = expired_time
        self.payment_type = payment_type
        self.max_timeline_limit = max_timeline_limit
        self.public_connection_string = public_connection_string
        self.engine_type = engine_type
        self.instance_tps = instance_tps
        self.status = status
        self.instance_storage = instance_storage
        self.request_id = request_id
        self.zone_id = zone_id
        self.instance_id = instance_id
        self.create_time = create_time
        self.disk_category = disk_category
        self.instance_class = instance_class
        self.vswitch_id = vswitch_id
        self.series = series
        self.vpc_id = vpc_id
        self.charge_type = charge_type
        self.security_ip_list = security_ip_list
        self.instance_description = instance_description
        self.region_id = region_id
        self.connection_string = connection_string

    def validate(self):
        if self.security_ip_list:
            for k in self.security_ip_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.cpu_number is not None:
            result['CpuNumber'] = self.cpu_number
        if self.mem_size is not None:
            result['MemSize'] = self.mem_size
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.gmt_expire is not None:
            result['GmtExpire'] = self.gmt_expire
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.max_timeline_limit is not None:
            result['MaxTimelineLimit'] = self.max_timeline_limit
        if self.public_connection_string is not None:
            result['PublicConnectionString'] = self.public_connection_string
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.instance_tps is not None:
            result['InstanceTps'] = self.instance_tps
        if self.status is not None:
            result['Status'] = self.status
        if self.instance_storage is not None:
            result['InstanceStorage'] = self.instance_storage
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.series is not None:
            result['Series'] = self.series
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        result['SecurityIpList'] = []
        if self.security_ip_list is not None:
            for k in self.security_ip_list:
                result['SecurityIpList'].append(k.to_map() if k else None)
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('CpuNumber') is not None:
            self.cpu_number = m.get('CpuNumber')
        if m.get('MemSize') is not None:
            self.mem_size = m.get('MemSize')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('GmtExpire') is not None:
            self.gmt_expire = m.get('GmtExpire')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('MaxTimelineLimit') is not None:
            self.max_timeline_limit = m.get('MaxTimelineLimit')
        if m.get('PublicConnectionString') is not None:
            self.public_connection_string = m.get('PublicConnectionString')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('InstanceTps') is not None:
            self.instance_tps = m.get('InstanceTps')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('InstanceStorage') is not None:
            self.instance_storage = m.get('InstanceStorage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('Series') is not None:
            self.series = m.get('Series')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        self.security_ip_list = []
        if m.get('SecurityIpList') is not None:
            for k in m.get('SecurityIpList'):
                temp_model = DescribeHiTSDBInstanceResponseBodySecurityIpList()
                self.security_ip_list.append(temp_model.from_map(k))
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        return self


class DescribeHiTSDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeHiTSDBInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeHiTSDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHiTSDBInstanceListRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        app_key: str = None,
        query_str: str = None,
        status_list: str = None,
        page_number: int = None,
        page_size: int = None,
        engine_type: str = None,
    ):
        self.security_token = security_token
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.app_key = app_key
        self.query_str = query_str
        self.status_list = status_list
        self.page_number = page_number
        self.page_size = page_size
        self.engine_type = engine_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.query_str is not None:
            result['QueryStr'] = self.query_str
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('QueryStr') is not None:
            self.query_str = m.get('QueryStr')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        return self


class DescribeHiTSDBInstanceListResponseBodyInstanceList(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        status: str = None,
        max_series_per_database: str = None,
        payment_type: str = None,
        engine_type: str = None,
        vswitch_id: str = None,
        instance_class: str = None,
        create_time: int = None,
        user_id: str = None,
        charge_type: str = None,
        instance_storage: str = None,
        network_type: str = None,
        instance_id: str = None,
        lock_mode: str = None,
        instance_description: str = None,
        region_id: str = None,
        gmt_created: str = None,
        instance_alias: str = None,
        instance_tps: str = None,
        expired_time: int = None,
        zone_id: str = None,
        instance_status: str = None,
        gmt_expire: str = None,
    ):
        self.vpc_id = vpc_id
        self.status = status
        self.max_series_per_database = max_series_per_database
        self.payment_type = payment_type
        self.engine_type = engine_type
        self.vswitch_id = vswitch_id
        self.instance_class = instance_class
        self.create_time = create_time
        self.user_id = user_id
        self.charge_type = charge_type
        self.instance_storage = instance_storage
        self.network_type = network_type
        self.instance_id = instance_id
        self.lock_mode = lock_mode
        self.instance_description = instance_description
        self.region_id = region_id
        self.gmt_created = gmt_created
        self.instance_alias = instance_alias
        self.instance_tps = instance_tps
        self.expired_time = expired_time
        self.zone_id = zone_id
        self.instance_status = instance_status
        self.gmt_expire = gmt_expire

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.status is not None:
            result['Status'] = self.status
        if self.max_series_per_database is not None:
            result['MaxSeriesPerDatabase'] = self.max_series_per_database
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.instance_storage is not None:
            result['InstanceStorage'] = self.instance_storage
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.instance_tps is not None:
            result['InstanceTps'] = self.instance_tps
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.gmt_expire is not None:
            result['GmtExpire'] = self.gmt_expire
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('MaxSeriesPerDatabase') is not None:
            self.max_series_per_database = m.get('MaxSeriesPerDatabase')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('InstanceStorage') is not None:
            self.instance_storage = m.get('InstanceStorage')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('InstanceTps') is not None:
            self.instance_tps = m.get('InstanceTps')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('GmtExpire') is not None:
            self.gmt_expire = m.get('GmtExpire')
        return self


class DescribeHiTSDBInstanceListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        total: int = None,
        instance_list: List[DescribeHiTSDBInstanceListResponseBodyInstanceList] = None,
    ):
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
        self.total = total
        self.instance_list = instance_list

    def validate(self):
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total is not None:
            result['Total'] = self.total
        result['InstanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['InstanceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k in m.get('InstanceList'):
                temp_model = DescribeHiTSDBInstanceListResponseBodyInstanceList()
                self.instance_list.append(temp_model.from_map(k))
        return self


class DescribeHiTSDBInstanceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeHiTSDBInstanceListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeHiTSDBInstanceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHiTSDBInstanceClassRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        app_key: str = None,
        instance_id: str = None,
        instance_class: str = None,
        instance_storage: str = None,
    ):
        self.security_token = security_token
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.app_key = app_key
        self.instance_id = instance_id
        self.instance_class = instance_class
        self.instance_storage = instance_storage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_storage is not None:
            result['InstanceStorage'] = self.instance_storage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceStorage') is not None:
            self.instance_storage = m.get('InstanceStorage')
        return self


class ModifyHiTSDBInstanceClassResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyHiTSDBInstanceClassResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyHiTSDBInstanceClassResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyHiTSDBInstanceClassResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenameHiTSDBInstanceAliasRequest(TeaModel):
    def __init__(
        self,
        security_token: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        owner_account: str = None,
        app_key: str = None,
        instance_id: str = None,
        instance_alias: str = None,
    ):
        self.security_token = security_token
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.owner_account = owner_account
        self.app_key = app_key
        self.instance_id = instance_id
        self.instance_alias = instance_alias

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        return self


class RenameHiTSDBInstanceAliasResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenameHiTSDBInstanceAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenameHiTSDBInstanceAliasResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RenameHiTSDBInstanceAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


