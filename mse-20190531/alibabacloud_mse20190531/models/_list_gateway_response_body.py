# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListGatewayResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListGatewayResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The return value.
        self.code = code
        # The data returned.
        self.data = data
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListGatewayResponseBodyData()
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

class ListGatewayResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        result: List[main_models.ListGatewayResponseBodyDataResult] = None,
        total_size: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The data returned.
        self.result = result
        # The total number of entries returned.
        self.total_size = total_size

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListGatewayResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class ListGatewayResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        ahas_on: bool = None,
        app_version: str = None,
        arms_on: bool = None,
        charge_type: str = None,
        current_version: str = None,
        elastic: bool = None,
        elastic_instance_id: str = None,
        elastic_policy: main_models.ListGatewayResponseBodyDataResultElasticPolicy = None,
        elastic_replica: int = None,
        elastic_type: str = None,
        end_date: str = None,
        gateway_entry: List[main_models.ListGatewayResponseBodyDataResultGatewayEntry] = None,
        gateway_type: str = None,
        gateway_unique_id: str = None,
        gateway_version: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        init_config: main_models.ListGatewayResponseBodyDataResultInitConfig = None,
        instance_id: str = None,
        internet_slb: List[main_models.ListGatewayResponseBodyDataResultInternetSlb] = None,
        latest_version: str = None,
        maintenance_period: main_models.ListGatewayResponseBodyDataResultMaintenancePeriod = None,
        mse_tag: str = None,
        mse_version: str = None,
        must_upgrade: bool = None,
        name: str = None,
        primary_user: str = None,
        region: str = None,
        replica: int = None,
        resource_group_id: str = None,
        roll_back: bool = None,
        slb: List[main_models.ListGatewayResponseBodyDataResultSlb] = None,
        spec: str = None,
        status: int = None,
        status_desc: str = None,
        support_wasm: bool = None,
        tag: str = None,
        total_replica: int = None,
        upgrade: bool = None,
        version_lifecycle: str = None,
        vpc_id: str = None,
        vswitch_2: str = None,
    ):
        # Indicates whether Application High Availability Service (AHAS) is activated.
        self.ahas_on = ahas_on
        # The version of the application.
        self.app_version = app_version
        # Indicates whether Application Real-Time Monitoring Service (ARMS) is activated.
        self.arms_on = arms_on
        # The billing method.
        self.charge_type = charge_type
        # The current version of the gateway.
        self.current_version = current_version
        # Indicates whether auto scale-out is enabled.
        self.elastic = elastic
        # The ID of the elastic gateway. This parameter is returned if auto scale-out is used.
        self.elastic_instance_id = elastic_instance_id
        # The auto scale-out policy.
        self.elastic_policy = elastic_policy
        # The number of replicas that are automatically scaled out.
        self.elastic_replica = elastic_replica
        # The type of auto scale-out. Valid value:
        # 
        # *   CronHPA: scale-out by time
        self.elastic_type = elastic_type
        # The time when the instance expires.
        self.end_date = end_date
        self.gateway_entry = gateway_entry
        # The gateway type.
        self.gateway_type = gateway_type
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The version of the gateway.
        self.gateway_version = gateway_version
        # The time when the gateway was created.
        self.gmt_create = gmt_create
        # The time when the gateway was modified.
        self.gmt_modified = gmt_modified
        # The gateway ID.
        self.id = id
        # The configurations.
        self.init_config = init_config
        # The instance ID.
        self.instance_id = instance_id
        # The details of the Internet-facing SLB instances.
        self.internet_slb = internet_slb
        # The latest version of the gateway.
        self.latest_version = latest_version
        self.maintenance_period = maintenance_period
        # The resource tag.
        self.mse_tag = mse_tag
        self.mse_version = mse_version
        # Indicates whether the instance was forcefully upgraded.
        self.must_upgrade = must_upgrade
        # The gateway name.
        self.name = name
        # The user information.
        self.primary_user = primary_user
        # The region ID.
        self.region = region
        # The number of replicas.
        self.replica = replica
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # Indicates whether rollbacks are allowed.
        self.roll_back = roll_back
        # The details of Server Load Balancer (SLB) instances.
        self.slb = slb
        # The specifications of the gateway.
        self.spec = spec
        # The gateway state. Valid values:
        # 
        # *   0: The gateway is being created.
        # *   1: The gateway failed to be created.
        # *   2: The gateway is running.
        # *   3: The gateway is being changed.
        # *   4: The gateway is scaling in.
        # *   6: The gateway is scaling out.
        # *   8: The gateway is being deleted.
        # *   9: The gateway is suspended and is to be released.
        # *   10: The gateway is restarting.
        # *   11: The gateway is being rebuilt.
        # *   12: The gateway is being upgraded.
        # *   13: The gateway failed to be upgraded.
        self.status = status
        # The description of the gateway state.
        self.status_desc = status_desc
        # Indicates whether WebAssembly (Wasm) is supported.
        self.support_wasm = support_wasm
        # The tag.
        self.tag = tag
        # The total number of replicas, including the number of replicas that are automatically scaled out.
        self.total_replica = total_replica
        # Indicates whether the instance was upgraded.
        self.upgrade = upgrade
        self.version_lifecycle = version_lifecycle
        # The ID of the virtual private cloud (VPC) to which the gateway belongs.
        self.vpc_id = vpc_id
        # The ID of the secondary vSwitch.
        self.vswitch_2 = vswitch_2

    def validate(self):
        if self.elastic_policy:
            self.elastic_policy.validate()
        if self.gateway_entry:
            for v1 in self.gateway_entry:
                 if v1:
                    v1.validate()
        if self.init_config:
            self.init_config.validate()
        if self.internet_slb:
            for v1 in self.internet_slb:
                 if v1:
                    v1.validate()
        if self.maintenance_period:
            self.maintenance_period.validate()
        if self.slb:
            for v1 in self.slb:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ahas_on is not None:
            result['AhasOn'] = self.ahas_on

        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.arms_on is not None:
            result['ArmsOn'] = self.arms_on

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version

        if self.elastic is not None:
            result['Elastic'] = self.elastic

        if self.elastic_instance_id is not None:
            result['ElasticInstanceId'] = self.elastic_instance_id

        if self.elastic_policy is not None:
            result['ElasticPolicy'] = self.elastic_policy.to_map()

        if self.elastic_replica is not None:
            result['ElasticReplica'] = self.elastic_replica

        if self.elastic_type is not None:
            result['ElasticType'] = self.elastic_type

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        result['GatewayEntry'] = []
        if self.gateway_entry is not None:
            for k1 in self.gateway_entry:
                result['GatewayEntry'].append(k1.to_map() if k1 else None)

        if self.gateway_type is not None:
            result['GatewayType'] = self.gateway_type

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.gateway_version is not None:
            result['GatewayVersion'] = self.gateway_version

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.init_config is not None:
            result['InitConfig'] = self.init_config.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['InternetSlb'] = []
        if self.internet_slb is not None:
            for k1 in self.internet_slb:
                result['InternetSlb'].append(k1.to_map() if k1 else None)

        if self.latest_version is not None:
            result['LatestVersion'] = self.latest_version

        if self.maintenance_period is not None:
            result['MaintenancePeriod'] = self.maintenance_period.to_map()

        if self.mse_tag is not None:
            result['MseTag'] = self.mse_tag

        if self.mse_version is not None:
            result['MseVersion'] = self.mse_version

        if self.must_upgrade is not None:
            result['MustUpgrade'] = self.must_upgrade

        if self.name is not None:
            result['Name'] = self.name

        if self.primary_user is not None:
            result['PrimaryUser'] = self.primary_user

        if self.region is not None:
            result['Region'] = self.region

        if self.replica is not None:
            result['Replica'] = self.replica

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.roll_back is not None:
            result['RollBack'] = self.roll_back

        result['Slb'] = []
        if self.slb is not None:
            for k1 in self.slb:
                result['Slb'].append(k1.to_map() if k1 else None)

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.status is not None:
            result['Status'] = self.status

        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc

        if self.support_wasm is not None:
            result['SupportWasm'] = self.support_wasm

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.total_replica is not None:
            result['TotalReplica'] = self.total_replica

        if self.upgrade is not None:
            result['Upgrade'] = self.upgrade

        if self.version_lifecycle is not None:
            result['VersionLifecycle'] = self.version_lifecycle

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vswitch_2 is not None:
            result['Vswitch2'] = self.vswitch_2

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AhasOn') is not None:
            self.ahas_on = m.get('AhasOn')

        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('ArmsOn') is not None:
            self.arms_on = m.get('ArmsOn')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')

        if m.get('Elastic') is not None:
            self.elastic = m.get('Elastic')

        if m.get('ElasticInstanceId') is not None:
            self.elastic_instance_id = m.get('ElasticInstanceId')

        if m.get('ElasticPolicy') is not None:
            temp_model = main_models.ListGatewayResponseBodyDataResultElasticPolicy()
            self.elastic_policy = temp_model.from_map(m.get('ElasticPolicy'))

        if m.get('ElasticReplica') is not None:
            self.elastic_replica = m.get('ElasticReplica')

        if m.get('ElasticType') is not None:
            self.elastic_type = m.get('ElasticType')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        self.gateway_entry = []
        if m.get('GatewayEntry') is not None:
            for k1 in m.get('GatewayEntry'):
                temp_model = main_models.ListGatewayResponseBodyDataResultGatewayEntry()
                self.gateway_entry.append(temp_model.from_map(k1))

        if m.get('GatewayType') is not None:
            self.gateway_type = m.get('GatewayType')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('GatewayVersion') is not None:
            self.gateway_version = m.get('GatewayVersion')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InitConfig') is not None:
            temp_model = main_models.ListGatewayResponseBodyDataResultInitConfig()
            self.init_config = temp_model.from_map(m.get('InitConfig'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.internet_slb = []
        if m.get('InternetSlb') is not None:
            for k1 in m.get('InternetSlb'):
                temp_model = main_models.ListGatewayResponseBodyDataResultInternetSlb()
                self.internet_slb.append(temp_model.from_map(k1))

        if m.get('LatestVersion') is not None:
            self.latest_version = m.get('LatestVersion')

        if m.get('MaintenancePeriod') is not None:
            temp_model = main_models.ListGatewayResponseBodyDataResultMaintenancePeriod()
            self.maintenance_period = temp_model.from_map(m.get('MaintenancePeriod'))

        if m.get('MseTag') is not None:
            self.mse_tag = m.get('MseTag')

        if m.get('MseVersion') is not None:
            self.mse_version = m.get('MseVersion')

        if m.get('MustUpgrade') is not None:
            self.must_upgrade = m.get('MustUpgrade')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PrimaryUser') is not None:
            self.primary_user = m.get('PrimaryUser')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Replica') is not None:
            self.replica = m.get('Replica')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RollBack') is not None:
            self.roll_back = m.get('RollBack')

        self.slb = []
        if m.get('Slb') is not None:
            for k1 in m.get('Slb'):
                temp_model = main_models.ListGatewayResponseBodyDataResultSlb()
                self.slb.append(temp_model.from_map(k1))

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')

        if m.get('SupportWasm') is not None:
            self.support_wasm = m.get('SupportWasm')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('TotalReplica') is not None:
            self.total_replica = m.get('TotalReplica')

        if m.get('Upgrade') is not None:
            self.upgrade = m.get('Upgrade')

        if m.get('VersionLifecycle') is not None:
            self.version_lifecycle = m.get('VersionLifecycle')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('Vswitch2') is not None:
            self.vswitch_2 = m.get('Vswitch2')

        return self

class ListGatewayResponseBodyDataResultSlb(DaraModel):
    def __init__(
        self,
        gateway_slb_mode: str = None,
        gateway_slb_status: str = None,
        slb_id: str = None,
        slb_ip: str = None,
        slb_port: str = None,
        slb_spec: str = None,
        status_desc: str = None,
        type: str = None,
    ):
        # The mode of the SLB instance.
        self.gateway_slb_mode = gateway_slb_mode
        # The state of the SLB instance.
        self.gateway_slb_status = gateway_slb_status
        # The ID of the SLB instance.
        self.slb_id = slb_id
        # The IP address of the SLB instance.
        self.slb_ip = slb_ip
        # The port number of the SLB instance.
        self.slb_port = slb_port
        # The specifications of the SLB instance.
        self.slb_spec = slb_spec
        # The description of the state.
        self.status_desc = status_desc
        # The network type. Valid values:
        # 
        # *   PUB_NET
        # *   PRIVATE_NET
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_slb_mode is not None:
            result['GatewaySlbMode'] = self.gateway_slb_mode

        if self.gateway_slb_status is not None:
            result['GatewaySlbStatus'] = self.gateway_slb_status

        if self.slb_id is not None:
            result['SlbId'] = self.slb_id

        if self.slb_ip is not None:
            result['SlbIp'] = self.slb_ip

        if self.slb_port is not None:
            result['SlbPort'] = self.slb_port

        if self.slb_spec is not None:
            result['SlbSpec'] = self.slb_spec

        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewaySlbMode') is not None:
            self.gateway_slb_mode = m.get('GatewaySlbMode')

        if m.get('GatewaySlbStatus') is not None:
            self.gateway_slb_status = m.get('GatewaySlbStatus')

        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')

        if m.get('SlbIp') is not None:
            self.slb_ip = m.get('SlbIp')

        if m.get('SlbPort') is not None:
            self.slb_port = m.get('SlbPort')

        if m.get('SlbSpec') is not None:
            self.slb_spec = m.get('SlbSpec')

        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListGatewayResponseBodyDataResultMaintenancePeriod(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        time_zone: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        return self

class ListGatewayResponseBodyDataResultInternetSlb(DaraModel):
    def __init__(
        self,
        gateway_slb_mode: str = None,
        gateway_slb_status: str = None,
        internet_network_flow: str = None,
        slb_id: str = None,
        slb_ip: str = None,
        slb_port: str = None,
        slb_spec: str = None,
        status_desc: str = None,
        type: str = None,
    ):
        # The mode of the SLB instance.
        self.gateway_slb_mode = gateway_slb_mode
        # The state of the SLB instance.
        self.gateway_slb_status = gateway_slb_status
        # The traffic of the gateway.
        self.internet_network_flow = internet_network_flow
        # The ID of the SLB instance.
        self.slb_id = slb_id
        # The IP address of the SLB instance.
        self.slb_ip = slb_ip
        # The port number of the SLB instance.
        self.slb_port = slb_port
        # The specifications of the SLB instance.
        self.slb_spec = slb_spec
        # The description of the state.
        self.status_desc = status_desc
        # The type of the SLB instance.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_slb_mode is not None:
            result['GatewaySlbMode'] = self.gateway_slb_mode

        if self.gateway_slb_status is not None:
            result['GatewaySlbStatus'] = self.gateway_slb_status

        if self.internet_network_flow is not None:
            result['InternetNetworkFlow'] = self.internet_network_flow

        if self.slb_id is not None:
            result['SlbId'] = self.slb_id

        if self.slb_ip is not None:
            result['SlbIp'] = self.slb_ip

        if self.slb_port is not None:
            result['SlbPort'] = self.slb_port

        if self.slb_spec is not None:
            result['SlbSpec'] = self.slb_spec

        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GatewaySlbMode') is not None:
            self.gateway_slb_mode = m.get('GatewaySlbMode')

        if m.get('GatewaySlbStatus') is not None:
            self.gateway_slb_status = m.get('GatewaySlbStatus')

        if m.get('InternetNetworkFlow') is not None:
            self.internet_network_flow = m.get('InternetNetworkFlow')

        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')

        if m.get('SlbIp') is not None:
            self.slb_ip = m.get('SlbIp')

        if m.get('SlbPort') is not None:
            self.slb_port = m.get('SlbPort')

        if m.get('SlbSpec') is not None:
            self.slb_spec = m.get('SlbSpec')

        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListGatewayResponseBodyDataResultInitConfig(DaraModel):
    def __init__(
        self,
        enable_waf: bool = None,
        support_waf: bool = None,
    ):
        # Indicates whether Web Application Firewall (WAF) is enabled.
        self.enable_waf = enable_waf
        # Indicates whether WAF is supported.
        self.support_waf = support_waf

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_waf is not None:
            result['EnableWaf'] = self.enable_waf

        if self.support_waf is not None:
            result['SupportWaf'] = self.support_waf

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableWaf') is not None:
            self.enable_waf = m.get('EnableWaf')

        if m.get('SupportWaf') is not None:
            self.support_waf = m.get('SupportWaf')

        return self

class ListGatewayResponseBodyDataResultGatewayEntry(DaraModel):
    def __init__(
        self,
        entry_domain: str = None,
        http_ports: List[int] = None,
        https_ports: List[int] = None,
        ip_list: List[str] = None,
        ipv_6list: List[str] = None,
        net_type: str = None,
        status: str = None,
    ):
        self.entry_domain = entry_domain
        self.http_ports = http_ports
        self.https_ports = https_ports
        self.ip_list = ip_list
        self.ipv_6list = ipv_6list
        self.net_type = net_type
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entry_domain is not None:
            result['EntryDomain'] = self.entry_domain

        if self.http_ports is not None:
            result['HttpPorts'] = self.http_ports

        if self.https_ports is not None:
            result['HttpsPorts'] = self.https_ports

        if self.ip_list is not None:
            result['IpList'] = self.ip_list

        if self.ipv_6list is not None:
            result['Ipv6List'] = self.ipv_6list

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntryDomain') is not None:
            self.entry_domain = m.get('EntryDomain')

        if m.get('HttpPorts') is not None:
            self.http_ports = m.get('HttpPorts')

        if m.get('HttpsPorts') is not None:
            self.https_ports = m.get('HttpsPorts')

        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')

        if m.get('Ipv6List') is not None:
            self.ipv_6list = m.get('Ipv6List')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListGatewayResponseBodyDataResultElasticPolicy(DaraModel):
    def __init__(
        self,
        elastic: bool = None,
        elastic_type: str = None,
        enable_scale_time_policy_list: List[main_models.ListGatewayResponseBodyDataResultElasticPolicyEnableScaleTimePolicyList] = None,
        load_warning_threshold: bool = None,
        max_replica: int = None,
        time_policy_list: List[main_models.ListGatewayResponseBodyDataResultElasticPolicyTimePolicyList] = None,
    ):
        # Indicates whether auto scale-out is enabled.
        self.elastic = elastic
        # The type of auto scale-out. Valid value:
        # 
        # *   CronHPA: scale-out by time
        self.elastic_type = elastic_type
        self.enable_scale_time_policy_list = enable_scale_time_policy_list
        self.load_warning_threshold = load_warning_threshold
        # The maximum number of instances that are automatically scaled out. This parameter is used for horizontal scale-out.
        self.max_replica = max_replica
        # The time policy list for auto scale-out.
        self.time_policy_list = time_policy_list

    def validate(self):
        if self.enable_scale_time_policy_list:
            for v1 in self.enable_scale_time_policy_list:
                 if v1:
                    v1.validate()
        if self.time_policy_list:
            for v1 in self.time_policy_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic is not None:
            result['Elastic'] = self.elastic

        if self.elastic_type is not None:
            result['ElasticType'] = self.elastic_type

        result['EnableScaleTimePolicyList'] = []
        if self.enable_scale_time_policy_list is not None:
            for k1 in self.enable_scale_time_policy_list:
                result['EnableScaleTimePolicyList'].append(k1.to_map() if k1 else None)

        if self.load_warning_threshold is not None:
            result['LoadWarningThreshold'] = self.load_warning_threshold

        if self.max_replica is not None:
            result['MaxReplica'] = self.max_replica

        result['TimePolicyList'] = []
        if self.time_policy_list is not None:
            for k1 in self.time_policy_list:
                result['TimePolicyList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Elastic') is not None:
            self.elastic = m.get('Elastic')

        if m.get('ElasticType') is not None:
            self.elastic_type = m.get('ElasticType')

        self.enable_scale_time_policy_list = []
        if m.get('EnableScaleTimePolicyList') is not None:
            for k1 in m.get('EnableScaleTimePolicyList'):
                temp_model = main_models.ListGatewayResponseBodyDataResultElasticPolicyEnableScaleTimePolicyList()
                self.enable_scale_time_policy_list.append(temp_model.from_map(k1))

        if m.get('LoadWarningThreshold') is not None:
            self.load_warning_threshold = m.get('LoadWarningThreshold')

        if m.get('MaxReplica') is not None:
            self.max_replica = m.get('MaxReplica')

        self.time_policy_list = []
        if m.get('TimePolicyList') is not None:
            for k1 in m.get('TimePolicyList'):
                temp_model = main_models.ListGatewayResponseBodyDataResultElasticPolicyTimePolicyList()
                self.time_policy_list.append(temp_model.from_map(k1))

        return self

class ListGatewayResponseBodyDataResultElasticPolicyTimePolicyList(DaraModel):
    def __init__(
        self,
        desired_replica: int = None,
        end_time: str = None,
        start_time: str = None,
    ):
        # The expected number of replicas for auto scale-out.
        self.desired_replica = desired_replica
        # The end time of auto scale-out.
        self.end_time = end_time
        # The start time of auto scale-out.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desired_replica is not None:
            result['DesiredReplica'] = self.desired_replica

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesiredReplica') is not None:
            self.desired_replica = m.get('DesiredReplica')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class ListGatewayResponseBodyDataResultElasticPolicyEnableScaleTimePolicyList(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

