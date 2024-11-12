# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateHiTSDBInstanceRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        disk_category: str = None,
        duration: str = None,
        instance_alias: str = None,
        instance_class: str = None,
        instance_storage: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pay_type: str = None,
        pricing_cycle: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        vpcid: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        # The ID of the zone in which you want to create the instance.
        self.app_key = app_key
        # The ID of the request.
        self.disk_category = disk_category
        # The disk type of TSDB for InfluxDB️®️.
        # 
        # *   cloud_efficiency: ultra disk
        # *   cloud_ssd: standard SSD.
        # *   cloud_essd: ESSD cloud_auto: ESSD AutoPL disk
        self.duration = duration
        # The type of the instance.
        self.instance_alias = instance_alias
        # The storage capacity of the instance. Unit: GB.
        # 
        # This parameter is required.
        self.instance_class = instance_class
        # The billing method of the instance. Valid values:
        # 
        # *   PREPAY: subscription
        # *   POSTPAY: pay-as-you-go
        # 
        # This parameter is required.
        self.instance_storage = instance_storage
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the VPC in which the instances reside.
        # 
        # This parameter is required.
        self.pay_type = pay_type
        # The subscription duration of the instance.
        # 
        # *   If PricingCycle is set to Month, set this parameter to an integer that ranges from 1 to 9.
        # *   If PricingCycle is set to Year, set this parameter to an integer that ranges from 1 to 3.
        self.pricing_cycle = pricing_cycle
        # A reserved parameter.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The ID of the vSwitch to which the instance connects to.
        # 
        # This parameter is required.
        self.vpcid = vpcid
        # The unit of the subscription duration of the instance. Valid values:
        # 
        # *   Month
        # *   Year
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The name of the instance .
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_storage is not None:
            result['InstanceStorage'] = self.instance_storage
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.vpcid is not None:
            result['VPCId'] = self.vpcid
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceStorage') is not None:
            self.instance_storage = m.get('InstanceStorage')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('VPCId') is not None:
            self.vpcid = m.get('VPCId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateHiTSDBInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        order_id: int = None,
        request_id: str = None,
    ):
        # The ID of the order.
        self.instance_id = instance_id
        # Creates a Time Series Database (TSDB) instance.
        self.order_id = order_id
        # The ID of the instance.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateHiTSDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateHiTSDBInstanceResponseBody = None,
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
            temp_model = CreateHiTSDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHiTSDBInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DeleteHiTSDBInstanceResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteHiTSDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteHiTSDBInstanceResponseBody = None,
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
            temp_model = DeleteHiTSDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHiTSDBInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeHiTSDBInstanceResponseBodySecurityIpList(TeaModel):
    def __init__(
        self,
        ip: str = None,
    ):
        # The IP address in the whitelist of the instance.
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        access_denied_detail: str = None,
        auto_renew: str = None,
        charge_type: str = None,
        connection_string: str = None,
        cpu_number: str = None,
        create_time: int = None,
        disk_category: str = None,
        engine_type: str = None,
        expired_time: int = None,
        gmt_created: str = None,
        gmt_expire: str = None,
        instance_alias: str = None,
        instance_class: str = None,
        instance_description: str = None,
        instance_id: str = None,
        instance_status: str = None,
        instance_storage: str = None,
        instance_tps: str = None,
        max_timeline_limit: str = None,
        mem_size: str = None,
        network_type: str = None,
        payment_type: str = None,
        public_connection_string: str = None,
        region_id: str = None,
        request_id: str = None,
        security_ip_list: List[DescribeHiTSDBInstanceResponseBodySecurityIpList] = None,
        series: int = None,
        status: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # Indicates whether auto-renewal is enabled for the instance that uses the subscription billing method.
        self.auto_renew = auto_renew
        # The billing method of the instance. Valid values: PREPAY and POSTPAY. The PREPAY value indicates the subscription billing method. The POSTPAY value indicates the pay-as-you-go billing method.
        self.charge_type = charge_type
        # The endpoint of the database.
        self.connection_string = connection_string
        # The number of CPU cores of the instance.
        self.cpu_number = cpu_number
        # The timestamp when the instance is created.
        self.create_time = create_time
        # The disk type of the instance. For a TSDB for InfluxDB®️ instance, the valid values are cloud_efficiency and cloud_ssd. The cloud_efficiency value indicates ultra disks. The cloud_ssd value indicates standard SSDs.
        self.disk_category = disk_category
        # The engine type of the instance. Valid values: tsdb_tsdb, tsdb_influxdb, and tsdb1.5. The tsdb_tsdb value indicates the OpenTSDB engine. The tsdb_influxdb value indicates the InfluxDB®️ engine. The tsdb1.5 value indicates the tsdb1.5 engine.
        self.engine_type = engine_type
        # The timestamp when the instance expires. This parameter is returned only when the instance uses the subscription billing method.
        self.expired_time = expired_time
        # The time when the instance is created. The time is in the yyyy-MM-dd HH:mm:ss format.
        self.gmt_created = gmt_created
        # The time when the instance expires. This parameter is returned only when the instance uses the subscription billing method. The time is in the yyyy-MM-dd HH:mm:ss format.
        self.gmt_expire = gmt_expire
        # The name of the instance.
        self.instance_alias = instance_alias
        # The type of the instance.
        self.instance_class = instance_class
        # The description of the instance.
        self.instance_description = instance_description
        # The ID of the instance.
        self.instance_id = instance_id
        # The status of the instance. Valid values: ACTIVATION, CREATING, NET_CREATING, CLASS_CHANGING, LOCKED, and DELETED. ACTIVATION indicates that the instance is running. CREATING indicates that the instance is being created. NET_CREATING indicates that a network connection to the instance is being created. CLASS_CHANGING indicates that the configuration of the instance is being modified. LOCKED indicates that the instance is locked. DELETED indicates that the instance is deleted.
        self.instance_status = instance_status
        # The storage capacity of the instance. Unit: GB.
        self.instance_storage = instance_storage
        # The transactions per second (TPS) of the instance. Unit: TPS.
        self.instance_tps = instance_tps
        # The number of time series supported by the instance. This parameter is returned only if the instance is a TSDB instance.
        self.max_timeline_limit = max_timeline_limit
        # The memory size of the instance. This parameter is returned only if the instance is a TSDB for InfluxDB®️ instance.
        self.mem_size = mem_size
        # The network type of the instance.
        self.network_type = network_type
        # The billing method of the instance. Valid values: PREPAY and POSTPAY. The PREPAY value indicates the subscription billing method. The POSTPAY value indicates the pay-as-you-go billing method.
        self.payment_type = payment_type
        # The public endpoint of the instance. You can use the public endpoint to access the instance over the Internet.
        self.public_connection_string = public_connection_string
        # The ID of the region in which the instance is located.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # The IP address whitelist of the instance.
        self.security_ip_list = security_ip_list
        # The edition of the TSDB for InfluxDB®️ instance. Valid values: 0 and 1. The 0 value indicates the Standard Edition. The 1 value indicates the High-availability Edition.
        self.series = series
        # The status of the instance. Valid values: ACTIVATION, CREATING, NET_CREATING, CLASS_CHANGING, LOCKED, and DELETED. ACTIVATION indicates that the instance is running. CREATING indicates that the instance is being created. NET_CREATING indicates that a network connection to the instance is being created. CLASS_CHANGING indicates that the configuration of the instance is being modified. LOCKED indicates that the instance is locked. DELETED indicates that the instance is deleted.
        self.status = status
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The ID of the vSwitch to which the instance connects.
        self.vswitch_id = vswitch_id
        # The ID of the zone in which the instance is deployed.
        self.zone_id = zone_id

    def validate(self):
        if self.security_ip_list:
            for k in self.security_ip_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.cpu_number is not None:
            result['CpuNumber'] = self.cpu_number
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_expire is not None:
            result['GmtExpire'] = self.gmt_expire
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_storage is not None:
            result['InstanceStorage'] = self.instance_storage
        if self.instance_tps is not None:
            result['InstanceTps'] = self.instance_tps
        if self.max_timeline_limit is not None:
            result['MaxTimelineLimit'] = self.max_timeline_limit
        if self.mem_size is not None:
            result['MemSize'] = self.mem_size
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.public_connection_string is not None:
            result['PublicConnectionString'] = self.public_connection_string
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecurityIpList'] = []
        if self.security_ip_list is not None:
            for k in self.security_ip_list:
                result['SecurityIpList'].append(k.to_map() if k else None)
        if self.series is not None:
            result['Series'] = self.series
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('CpuNumber') is not None:
            self.cpu_number = m.get('CpuNumber')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtExpire') is not None:
            self.gmt_expire = m.get('GmtExpire')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceStorage') is not None:
            self.instance_storage = m.get('InstanceStorage')
        if m.get('InstanceTps') is not None:
            self.instance_tps = m.get('InstanceTps')
        if m.get('MaxTimelineLimit') is not None:
            self.max_timeline_limit = m.get('MaxTimelineLimit')
        if m.get('MemSize') is not None:
            self.mem_size = m.get('MemSize')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('PublicConnectionString') is not None:
            self.public_connection_string = m.get('PublicConnectionString')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.security_ip_list = []
        if m.get('SecurityIpList') is not None:
            for k in m.get('SecurityIpList'):
                temp_model = DescribeHiTSDBInstanceResponseBodySecurityIpList()
                self.security_ip_list.append(temp_model.from_map(k))
        if m.get('Series') is not None:
            self.series = m.get('Series')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeHiTSDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeHiTSDBInstanceResponseBody = None,
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
            temp_model = DescribeHiTSDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHiTSDBInstanceListRequest(TeaModel):
    def __init__(
        self,
        engine_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        query_str: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        status_list: str = None,
    ):
        # The ID of the request.
        self.engine_type = engine_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The number of instances to return on each page.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The engine type of the instances that you want to query. Valid values: tsdb_tsdb and tsdb_influxdb. The tsdb_tsdb value indicates the OpenTSDB engine. The tsdb_influxdb value indicates the InfluxDB®️ engine.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The states of the instances you want to query. Specify this parameter in the JSON format. The InstanceStatus parameter enumerates the instances of the specified states.
        self.query_str = query_str
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # The number of the page to return.
        self.status_list = status_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_str is not None:
            result['QueryStr'] = self.query_str
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryStr') is not None:
            self.query_str = m.get('QueryStr')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        return self


class DescribeHiTSDBInstanceListResponseBodyInstanceList(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        create_time: int = None,
        engine_type: str = None,
        expired_time: int = None,
        gmt_created: str = None,
        gmt_expire: str = None,
        instance_alias: str = None,
        instance_class: str = None,
        instance_description: str = None,
        instance_id: str = None,
        instance_status: str = None,
        instance_storage: str = None,
        instance_tps: str = None,
        lock_mode: str = None,
        max_series_per_database: str = None,
        network_type: str = None,
        payment_type: str = None,
        region_id: str = None,
        status: str = None,
        user_id: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        zone_id: str = None,
    ):
        # The user ID.
        self.charge_type = charge_type
        # The billing method of the instance. Valid values: PREPAY and POSTPAY. The PREPAY value indicates the subscription billing method. The POSTPAY value indicates the pay-as-you-go billing method.
        self.create_time = create_time
        # The ID of the vSwitch.
        self.engine_type = engine_type
        # The ID of the zone in which the instance is deployed.
        self.expired_time = expired_time
        # The name of the instance.
        self.gmt_created = gmt_created
        # Queries the list of Time Series Database (TSDB) instances.
        self.gmt_expire = gmt_expire
        # The transactions per second (TPS) of the instance. Unit: TPS.
        self.instance_alias = instance_alias
        # The timestamp when the instance was created.
        self.instance_class = instance_class
        # The region ID of the instance.
        self.instance_description = instance_description
        # Indicates whether the instance is locked. Valid values: 0 and 1. The value 0 indicates that the instance is not locked. The value 1 indicates that the instance is locked.
        self.instance_id = instance_id
        # The time when the instance expires. This parameter is returned only when the instance uses the subscription billing method. The time is in the yyyy-MM-dd HH:mm:ss format.
        self.instance_status = instance_status
        # The network type of the instance. The VPC value indicates a virtual private cloud (VPC).
        self.instance_storage = instance_storage
        # The timestamp when the instance expires. This parameter is returned only when the instance uses the subscription billing method.
        self.instance_tps = instance_tps
        # The description of the instance.
        self.lock_mode = lock_mode
        # The engine type of the instance. Valid values: tsdb_tsdb and tsdb_influxdb. The tsdb_tsdb value indicates the OpenTSDB engine. The tsdb_influxdb value indicates the InfluxDB®️ engine.
        self.max_series_per_database = max_series_per_database
        # The ID of the instance.
        self.network_type = network_type
        # The maximum number of time series that can be stored in a database.
        self.payment_type = payment_type
        # The time when the instance was created. The time is in the yyyy-MM-dd HH:mm:ss format.
        self.region_id = region_id
        # The ID of the VPC.
        self.status = status
        # The storage capacity of the instance. Unit: GB.
        self.user_id = user_id
        # The billing method of the instance. Valid values: PREPAY and POSTPAY. The PREPAY value indicates the subscription billing method. The POSTPAY value indicates the pay-as-you-go billing method.
        self.vpc_id = vpc_id
        # The type of the instance.
        self.vswitch_id = vswitch_id
        # The state of the instance. The value of this parameter is an enumerated string.
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_expire is not None:
            result['GmtExpire'] = self.gmt_expire
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_storage is not None:
            result['InstanceStorage'] = self.instance_storage
        if self.instance_tps is not None:
            result['InstanceTps'] = self.instance_tps
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.max_series_per_database is not None:
            result['MaxSeriesPerDatabase'] = self.max_series_per_database
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtExpire') is not None:
            self.gmt_expire = m.get('GmtExpire')
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceStorage') is not None:
            self.instance_storage = m.get('InstanceStorage')
        if m.get('InstanceTps') is not None:
            self.instance_tps = m.get('InstanceTps')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('MaxSeriesPerDatabase') is not None:
            self.max_series_per_database = m.get('MaxSeriesPerDatabase')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeHiTSDBInstanceListResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        instance_list: List[DescribeHiTSDBInstanceListResponseBodyInstanceList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The status of the instance. Valid values: ACTIVATION, CREATING, NET_CREATING, CLASS_CHANGING, LOCKED, and DELETED. ACTIVATION: The instance is running. CREATING: The instance is being created. NET_CREATING: A network connection is being established. CLASS_CHANGING: The configuration of the instance is being modified. LOCKED: The instance is locked. DELETED: The instance is deleted.
        self.instance_list = instance_list
        # The number of instances returned on each page.
        self.page_number = page_number
        # The total number of returned instances.
        self.page_size = page_size
        # The page number of the returned page.
        self.request_id = request_id
        # The list of queried instances.
        self.total = total

    def validate(self):
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        result['InstanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['InstanceList'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k in m.get('InstanceList'):
                temp_model = DescribeHiTSDBInstanceListResponseBodyInstanceList()
                self.instance_list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeHiTSDBInstanceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeHiTSDBInstanceListResponseBody = None,
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
            temp_model = DescribeHiTSDBInstanceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHiTSDBInstanceSecurityIpListRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # The ID of the request.
        self.group_name = group_name
        # The name of the group to which the instance belongs. The group name can contain only letters, digits, and underscores (_).
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeHiTSDBInstanceSecurityIpListResponseBodySecurityIpList(TeaModel):
    def __init__(
        self,
        ip: str = None,
    ):
        # auditing
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        return self


class DescribeHiTSDBInstanceSecurityIpListResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        request_id: str = None,
        security_ip_list: List[DescribeHiTSDBInstanceSecurityIpListResponseBodySecurityIpList] = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The IP address whitelist of the instance.
        self.request_id = request_id
        # The IP address in the whitelist.
        self.security_ip_list = security_ip_list

    def validate(self):
        if self.security_ip_list:
            for k in self.security_ip_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecurityIpList'] = []
        if self.security_ip_list is not None:
            for k in self.security_ip_list:
                result['SecurityIpList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.security_ip_list = []
        if m.get('SecurityIpList') is not None:
            for k in m.get('SecurityIpList'):
                temp_model = DescribeHiTSDBInstanceSecurityIpListResponseBodySecurityIpList()
                self.security_ip_list.append(temp_model.from_map(k))
        return self


class DescribeHiTSDBInstanceSecurityIpListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeHiTSDBInstanceSecurityIpListResponseBody = None,
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
            temp_model = DescribeHiTSDBInstanceSecurityIpListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # The language of the values to return. Valid values:
        # 
        # *   zh-CN: Chinese
        # *   en-US: English
        # *   ja: Japanese
        # 
        # Default value: en-US
        self.accept_language = accept_language
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        # The name of the region.
        self.local_name = local_name
        # The endpoint of the region.
        self.region_endpoint = region_endpoint
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: DescribeRegionsResponseBodyRegions = None,
        request_id: str = None,
    ):
        # The collection of regions.
        self.regions = regions
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZonesRequest(TeaModel):
    def __init__(
        self,
        language: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # The ID of the request.
        self.language = language
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class DescribeZonesResponseBodyZoneListZoneModel(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        zone_id: str = None,
    ):
        # Shanghai Zone B
        self.local_name = local_name
        # The name of the zone
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeZonesResponseBodyZoneList(TeaModel):
    def __init__(
        self,
        zone_model: List[DescribeZonesResponseBodyZoneListZoneModel] = None,
    ):
        self.zone_model = zone_model

    def validate(self):
        if self.zone_model:
            for k in self.zone_model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ZoneModel'] = []
        if self.zone_model is not None:
            for k in self.zone_model:
                result['ZoneModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone_model = []
        if m.get('ZoneModel') is not None:
            for k in m.get('ZoneModel'):
                temp_model = DescribeZonesResponseBodyZoneListZoneModel()
                self.zone_model.append(temp_model.from_map(k))
        return self


class DescribeZonesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        zone_list: DescribeZonesResponseBodyZoneList = None,
    ):
        # The list of available zones.
        self.request_id = request_id
        # The ID of the zone.
        self.zone_list = zone_list

    def validate(self):
        if self.zone_list:
            self.zone_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.zone_list is not None:
            result['ZoneList'] = self.zone_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ZoneList') is not None:
            temp_model = DescribeZonesResponseBodyZoneList()
            self.zone_list = temp_model.from_map(m['ZoneList'])
        return self


class DescribeZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeZonesResponseBody = None,
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
            temp_model = DescribeZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHiTSDBInstanceClassRequest(TeaModel):
    def __init__(
        self,
        instance_class: str = None,
        instance_id: str = None,
        instance_storage: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # The storage capacity of the instance. Unit: GB.
        # 
        # This parameter is required.
        self.instance_class = instance_class
        # The type of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the request.
        # 
        # This parameter is required.
        self.instance_storage = instance_storage
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_storage is not None:
            result['InstanceStorage'] = self.instance_storage
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceStorage') is not None:
            self.instance_storage = m.get('InstanceStorage')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyHiTSDBInstanceClassResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # Modifies the type of a Time Series Database (TSDB) instance.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyHiTSDBInstanceClassResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyHiTSDBInstanceClassResponseBody = None,
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
            temp_model = ModifyHiTSDBInstanceClassResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHiTSDBInstanceSecurityIpListRequest(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_ip_list: str = None,
        security_token: str = None,
    ):
        # auditing
        self.group_name = group_name
        # The name of the group to which the instance belongs. The group name can contain only letters, digits, and underscores (_).
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the request.
        # 
        # This parameter is required.
        self.security_ip_list = security_ip_list
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_ip_list is not None:
            result['SecurityIpList'] = self.security_ip_list
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityIpList') is not None:
            self.security_ip_list = m.get('SecurityIpList')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class ModifyHiTSDBInstanceSecurityIpListResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # Configures the whitelist of a Time Series Database (TSDB) instance. The IP addresses in the whitelist are allowed to connect to the instance.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyHiTSDBInstanceSecurityIpListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyHiTSDBInstanceSecurityIpListResponseBody = None,
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
            temp_model = ModifyHiTSDBInstanceSecurityIpListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenameHiTSDBInstanceAliasRequest(TeaModel):
    def __init__(
        self,
        instance_alias: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # Instance Alias
        # 
        # This parameter is required.
        self.instance_alias = instance_alias
        # Instance ID
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_alias is not None:
            result['InstanceAlias'] = self.instance_alias
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceAlias') is not None:
            self.instance_alias = m.get('InstanceAlias')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class RenameHiTSDBInstanceAliasResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # Request ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenameHiTSDBInstanceAliasResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenameHiTSDBInstanceAliasResponseBody = None,
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
            temp_model = RenameHiTSDBInstanceAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewTSDBInstanceRequest(TeaModel):
    def __init__(
        self,
        duration: int = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pricing_cycle: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # The subscription duration of the instance. If you set PricingCycle to Month, set Duration to an integer that ranges from 1 to 9. If you set PricingCycle to Year, set Duration to an integer that ranges from 1 to 3.
        # 
        # This parameter is required.
        self.duration = duration
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The unit of the subscription duration. Valid values: Month and Year. This parameter is valid only for an instance that uses the subscription billing method.
        # 
        # This parameter is required.
        self.pricing_cycle = pricing_cycle
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class RenewTSDBInstanceResponseBody(TeaModel):
    def __init__(
        self,
        order_id: int = None,
        request_id: str = None,
    ):
        # The ID of the order.
        self.order_id = order_id
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenewTSDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RenewTSDBInstanceResponseBody = None,
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
            temp_model = RenewTSDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartHiTSDBInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class RestartHiTSDBInstanceResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RestartHiTSDBInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestartHiTSDBInstanceResponseBody = None,
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
            temp_model = RestartHiTSDBInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchHiTSDBInstancePublicNetRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        security_token: str = None,
        switch_action: int = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.security_token = security_token
        # *   **1**: enables access to the instance from the Internet.
        # *   **0**: disables access to the instance from the Internet.
        # 
        # This parameter is required.
        self.switch_action = switch_action

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.switch_action is not None:
            result['SwitchAction'] = self.switch_action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('SwitchAction') is not None:
            self.switch_action = m.get('SwitchAction')
        return self


class SwitchHiTSDBInstancePublicNetResponseBody(TeaModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SwitchHiTSDBInstancePublicNetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SwitchHiTSDBInstancePublicNetResponseBody = None,
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
            temp_model = SwitchHiTSDBInstancePublicNetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


