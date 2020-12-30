# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AddUserHdfsInfoRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        ext_info: str = None,
        client_token: str = None,
    ):
        self.cluster_id = cluster_id
        self.ext_info = ext_info
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class AddUserHdfsInfoResponseBody(TeaModel):
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


class AddUserHdfsInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddUserHdfsInfoResponseBody = None,
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
            temp_model = AddUserHdfsInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AllocatePublicNetworkAddressRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        client_token: str = None,
    ):
        self.cluster_id = cluster_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class AllocatePublicNetworkAddressResponseBody(TeaModel):
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


class AllocatePublicNetworkAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AllocatePublicNetworkAddressResponseBody = None,
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
            temp_model = AllocatePublicNetworkAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckComponentsVersionRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        components: str = None,
    ):
        self.cluster_id = cluster_id
        self.components = components

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.components is not None:
            result['Components'] = self.components
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Components') is not None:
            self.components = m.get('Components')
        return self


class CheckComponentsVersionResponseBodyComponentsComponent(TeaModel):
    def __init__(
        self,
        is_latest_version: str = None,
        component: str = None,
    ):
        self.is_latest_version = is_latest_version
        self.component = component

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_latest_version is not None:
            result['IsLatestVersion'] = self.is_latest_version
        if self.component is not None:
            result['Component'] = self.component
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsLatestVersion') is not None:
            self.is_latest_version = m.get('IsLatestVersion')
        if m.get('Component') is not None:
            self.component = m.get('Component')
        return self


class CheckComponentsVersionResponseBodyComponents(TeaModel):
    def __init__(
        self,
        component: List[CheckComponentsVersionResponseBodyComponentsComponent] = None,
    ):
        self.component = component

    def validate(self):
        if self.component:
            for k in self.component:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Component'] = []
        if self.component is not None:
            for k in self.component:
                result['Component'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.component = []
        if m.get('Component') is not None:
            for k in m.get('Component'):
                temp_model = CheckComponentsVersionResponseBodyComponentsComponent()
                self.component.append(temp_model.from_map(k))
        return self


class CheckComponentsVersionResponseBody(TeaModel):
    def __init__(
        self,
        components: CheckComponentsVersionResponseBodyComponents = None,
        request_id: str = None,
    ):
        self.components = components
        self.request_id = request_id

    def validate(self):
        if self.components:
            self.components.validate()

    def to_map(self):
        result = dict()
        if self.components is not None:
            result['Components'] = self.components.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Components') is not None:
            temp_model = CheckComponentsVersionResponseBodyComponents()
            self.components = temp_model.from_map(m['Components'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckComponentsVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckComponentsVersionResponseBody = None,
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
            temp_model = CheckComponentsVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseBackupRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class CloseBackupResponseBody(TeaModel):
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


class CloseBackupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CloseBackupResponseBody = None,
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
            temp_model = CloseBackupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConvertInstanceRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        pricing_cycle: str = None,
        duration: int = None,
    ):
        self.cluster_id = cluster_id
        self.pricing_cycle = pricing_cycle
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class ConvertInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: int = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ConvertInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ConvertInstanceResponseBody = None,
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
            temp_model = ConvertInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBackupPlanRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class CreateBackupPlanResponseBody(TeaModel):
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


class CreateBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateBackupPlanResponseBody = None,
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
            temp_model = CreateBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        zone_id: str = None,
        cluster_name: str = None,
        vpc_id: str = None,
        v_switch_id: str = None,
        master_instance_type: str = None,
        core_instance_type: str = None,
        disk_type: str = None,
        disk_size: int = None,
        node_count: int = None,
        pay_type: str = None,
        engine: str = None,
        security_iplist: str = None,
        engine_version: str = None,
        cold_storage_size: int = None,
        period_unit: str = None,
        period: int = None,
        auto_renew_period: int = None,
        client_token: str = None,
        resource_group_id: str = None,
    ):
        self.region_id = region_id
        self.zone_id = zone_id
        self.cluster_name = cluster_name
        self.vpc_id = vpc_id
        self.v_switch_id = v_switch_id
        self.master_instance_type = master_instance_type
        self.core_instance_type = core_instance_type
        self.disk_type = disk_type
        self.disk_size = disk_size
        self.node_count = node_count
        self.pay_type = pay_type
        self.engine = engine
        self.security_iplist = security_iplist
        self.engine_version = engine_version
        self.cold_storage_size = cold_storage_size
        self.period_unit = period_unit
        self.period = period
        self.auto_renew_period = auto_renew_period
        self.client_token = client_token
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.master_instance_type is not None:
            result['MasterInstanceType'] = self.master_instance_type
        if self.core_instance_type is not None:
            result['CoreInstanceType'] = self.core_instance_type
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.cold_storage_size is not None:
            result['ColdStorageSize'] = self.cold_storage_size
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.period is not None:
            result['Period'] = self.period
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('MasterInstanceType') is not None:
            self.master_instance_type = m.get('MasterInstanceType')
        if m.get('CoreInstanceType') is not None:
            self.core_instance_type = m.get('CoreInstanceType')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ColdStorageSize') is not None:
            self.cold_storage_size = m.get('ColdStorageSize')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cluster_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.cluster_id = cluster_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateClusterResponseBody = None,
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
            temp_model = CreateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGlobalResourceRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        client_token: str = None,
    ):
        self.cluster_id = cluster_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateGlobalResourceResponseBody(TeaModel):
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


class CreateGlobalResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateGlobalResourceResponseBody = None,
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
            temp_model = CreateGlobalResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHbaseHaSlbRequest(TeaModel):
    def __init__(
        self,
        bds_id: str = None,
        ha_id: str = None,
        ha_types: str = None,
        hbase_type: str = None,
        client_token: str = None,
    ):
        self.bds_id = bds_id
        self.ha_id = ha_id
        self.ha_types = ha_types
        self.hbase_type = hbase_type
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.bds_id is not None:
            result['BdsId'] = self.bds_id
        if self.ha_id is not None:
            result['HaId'] = self.ha_id
        if self.ha_types is not None:
            result['HaTypes'] = self.ha_types
        if self.hbase_type is not None:
            result['HbaseType'] = self.hbase_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BdsId') is not None:
            self.bds_id = m.get('BdsId')
        if m.get('HaId') is not None:
            self.ha_id = m.get('HaId')
        if m.get('HaTypes') is not None:
            self.ha_types = m.get('HaTypes')
        if m.get('HbaseType') is not None:
            self.hbase_type = m.get('HbaseType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateHbaseHaSlbResponseBody(TeaModel):
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


class CreateHbaseHaSlbResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateHbaseHaSlbResponseBody = None,
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
            temp_model = CreateHbaseHaSlbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHBaseSlbServerRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        slb_server: str = None,
        client_token: str = None,
    ):
        self.cluster_id = cluster_id
        self.slb_server = slb_server
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.slb_server is not None:
            result['SlbServer'] = self.slb_server
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('SlbServer') is not None:
            self.slb_server = m.get('SlbServer')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateHBaseSlbServerResponseBody(TeaModel):
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


class CreateHBaseSlbServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateHBaseSlbServerResponseBody = None,
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
            temp_model = CreateHBaseSlbServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMultiZoneClusterRequest(TeaModel):
    def __init__(
        self,
        engine: str = None,
        engine_version: str = None,
        arch_version: str = None,
        cluster_name: str = None,
        region_id: str = None,
        vpc_id: str = None,
        multi_zone_combination: str = None,
        primary_zone_id: str = None,
        primary_vswitch_id: str = None,
        standby_zone_id: str = None,
        standby_vswitch_id: str = None,
        arbiter_zone_id: str = None,
        arbiter_vswitch_id: str = None,
        master_instance_type: str = None,
        core_instance_type: str = None,
        core_disk_type: str = None,
        core_disk_size: int = None,
        core_node_count: int = None,
        log_instance_type: str = None,
        log_disk_type: str = None,
        log_disk_size: int = None,
        log_node_count: int = None,
        security_iplist: str = None,
        pay_type: str = None,
        period_unit: str = None,
        period: int = None,
        auto_renew_period: int = None,
        client_token: str = None,
        resource_group_id: str = None,
    ):
        self.engine = engine
        self.engine_version = engine_version
        self.arch_version = arch_version
        self.cluster_name = cluster_name
        self.region_id = region_id
        self.vpc_id = vpc_id
        self.multi_zone_combination = multi_zone_combination
        self.primary_zone_id = primary_zone_id
        self.primary_vswitch_id = primary_vswitch_id
        self.standby_zone_id = standby_zone_id
        self.standby_vswitch_id = standby_vswitch_id
        self.arbiter_zone_id = arbiter_zone_id
        self.arbiter_vswitch_id = arbiter_vswitch_id
        self.master_instance_type = master_instance_type
        self.core_instance_type = core_instance_type
        self.core_disk_type = core_disk_type
        self.core_disk_size = core_disk_size
        self.core_node_count = core_node_count
        self.log_instance_type = log_instance_type
        self.log_disk_type = log_disk_type
        self.log_disk_size = log_disk_size
        self.log_node_count = log_node_count
        self.security_iplist = security_iplist
        self.pay_type = pay_type
        self.period_unit = period_unit
        self.period = period
        self.auto_renew_period = auto_renew_period
        self.client_token = client_token
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.arch_version is not None:
            result['ArchVersion'] = self.arch_version
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.multi_zone_combination is not None:
            result['MultiZoneCombination'] = self.multi_zone_combination
        if self.primary_zone_id is not None:
            result['PrimaryZoneId'] = self.primary_zone_id
        if self.primary_vswitch_id is not None:
            result['PrimaryVSwitchId'] = self.primary_vswitch_id
        if self.standby_zone_id is not None:
            result['StandbyZoneId'] = self.standby_zone_id
        if self.standby_vswitch_id is not None:
            result['StandbyVSwitchId'] = self.standby_vswitch_id
        if self.arbiter_zone_id is not None:
            result['ArbiterZoneId'] = self.arbiter_zone_id
        if self.arbiter_vswitch_id is not None:
            result['ArbiterVSwitchId'] = self.arbiter_vswitch_id
        if self.master_instance_type is not None:
            result['MasterInstanceType'] = self.master_instance_type
        if self.core_instance_type is not None:
            result['CoreInstanceType'] = self.core_instance_type
        if self.core_disk_type is not None:
            result['CoreDiskType'] = self.core_disk_type
        if self.core_disk_size is not None:
            result['CoreDiskSize'] = self.core_disk_size
        if self.core_node_count is not None:
            result['CoreNodeCount'] = self.core_node_count
        if self.log_instance_type is not None:
            result['LogInstanceType'] = self.log_instance_type
        if self.log_disk_type is not None:
            result['LogDiskType'] = self.log_disk_type
        if self.log_disk_size is not None:
            result['LogDiskSize'] = self.log_disk_size
        if self.log_node_count is not None:
            result['LogNodeCount'] = self.log_node_count
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.period is not None:
            result['Period'] = self.period
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ArchVersion') is not None:
            self.arch_version = m.get('ArchVersion')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('MultiZoneCombination') is not None:
            self.multi_zone_combination = m.get('MultiZoneCombination')
        if m.get('PrimaryZoneId') is not None:
            self.primary_zone_id = m.get('PrimaryZoneId')
        if m.get('PrimaryVSwitchId') is not None:
            self.primary_vswitch_id = m.get('PrimaryVSwitchId')
        if m.get('StandbyZoneId') is not None:
            self.standby_zone_id = m.get('StandbyZoneId')
        if m.get('StandbyVSwitchId') is not None:
            self.standby_vswitch_id = m.get('StandbyVSwitchId')
        if m.get('ArbiterZoneId') is not None:
            self.arbiter_zone_id = m.get('ArbiterZoneId')
        if m.get('ArbiterVSwitchId') is not None:
            self.arbiter_vswitch_id = m.get('ArbiterVSwitchId')
        if m.get('MasterInstanceType') is not None:
            self.master_instance_type = m.get('MasterInstanceType')
        if m.get('CoreInstanceType') is not None:
            self.core_instance_type = m.get('CoreInstanceType')
        if m.get('CoreDiskType') is not None:
            self.core_disk_type = m.get('CoreDiskType')
        if m.get('CoreDiskSize') is not None:
            self.core_disk_size = m.get('CoreDiskSize')
        if m.get('CoreNodeCount') is not None:
            self.core_node_count = m.get('CoreNodeCount')
        if m.get('LogInstanceType') is not None:
            self.log_instance_type = m.get('LogInstanceType')
        if m.get('LogDiskType') is not None:
            self.log_disk_type = m.get('LogDiskType')
        if m.get('LogDiskSize') is not None:
            self.log_disk_size = m.get('LogDiskSize')
        if m.get('LogNodeCount') is not None:
            self.log_node_count = m.get('LogNodeCount')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CreateMultiZoneClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cluster_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.cluster_id = cluster_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateMultiZoneClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateMultiZoneClusterResponseBody = None,
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
            temp_model = CreateMultiZoneClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRestorePlanRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        target_cluster_id: str = None,
        restore_all_table: bool = None,
        restore_by_copy: bool = None,
        restore_to_date: str = None,
        tables: str = None,
    ):
        self.cluster_id = cluster_id
        self.target_cluster_id = target_cluster_id
        self.restore_all_table = restore_all_table
        self.restore_by_copy = restore_by_copy
        self.restore_to_date = restore_to_date
        self.tables = tables

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.target_cluster_id is not None:
            result['TargetClusterId'] = self.target_cluster_id
        if self.restore_all_table is not None:
            result['RestoreAllTable'] = self.restore_all_table
        if self.restore_by_copy is not None:
            result['RestoreByCopy'] = self.restore_by_copy
        if self.restore_to_date is not None:
            result['RestoreToDate'] = self.restore_to_date
        if self.tables is not None:
            result['Tables'] = self.tables
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('TargetClusterId') is not None:
            self.target_cluster_id = m.get('TargetClusterId')
        if m.get('RestoreAllTable') is not None:
            self.restore_all_table = m.get('RestoreAllTable')
        if m.get('RestoreByCopy') is not None:
            self.restore_by_copy = m.get('RestoreByCopy')
        if m.get('RestoreToDate') is not None:
            self.restore_to_date = m.get('RestoreToDate')
        if m.get('Tables') is not None:
            self.tables = m.get('Tables')
        return self


class CreateRestorePlanResponseBody(TeaModel):
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


class CreateRestorePlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRestorePlanResponseBody = None,
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
            temp_model = CreateRestorePlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServerlessClusterRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        zone_id: str = None,
        cluster_name: str = None,
        vpc_id: str = None,
        v_switch_id: str = None,
        pay_type: str = None,
        period_unit: str = None,
        period: int = None,
        auto_renew_period: int = None,
        serverless_spec: str = None,
        serverless_capability: int = None,
        serverless_storage: int = None,
        engine: str = None,
        engine_version: str = None,
        client_token: str = None,
        client_type: str = None,
        resource_group_id: str = None,
    ):
        self.region_id = region_id
        self.zone_id = zone_id
        self.cluster_name = cluster_name
        self.vpc_id = vpc_id
        self.v_switch_id = v_switch_id
        self.pay_type = pay_type
        self.period_unit = period_unit
        self.period = period
        self.auto_renew_period = auto_renew_period
        self.serverless_spec = serverless_spec
        self.serverless_capability = serverless_capability
        self.serverless_storage = serverless_storage
        self.engine = engine
        self.engine_version = engine_version
        self.client_token = client_token
        self.client_type = client_type
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.period is not None:
            result['Period'] = self.period
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.serverless_spec is not None:
            result['ServerlessSpec'] = self.serverless_spec
        if self.serverless_capability is not None:
            result['ServerlessCapability'] = self.serverless_capability
        if self.serverless_storage is not None:
            result['ServerlessStorage'] = self.serverless_storage
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('ServerlessSpec') is not None:
            self.serverless_spec = m.get('ServerlessSpec')
        if m.get('ServerlessCapability') is not None:
            self.serverless_capability = m.get('ServerlessCapability')
        if m.get('ServerlessStorage') is not None:
            self.serverless_storage = m.get('ServerlessStorage')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CreateServerlessClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cluster_id: str = None,
        order_id: str = None,
        pass_word: str = None,
    ):
        self.request_id = request_id
        self.cluster_id = cluster_id
        self.order_id = order_id
        self.pass_word = pass_word

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.pass_word is not None:
            result['PassWord'] = self.pass_word
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PassWord') is not None:
            self.pass_word = m.get('PassWord')
        return self


class CreateServerlessClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateServerlessClusterResponseBody = None,
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
            temp_model = CreateServerlessClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGlobalResourceRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
    ):
        self.cluster_id = cluster_id
        self.resource_name = resource_name
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DeleteGlobalResourceResponseBody(TeaModel):
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


class DeleteGlobalResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteGlobalResourceResponseBody = None,
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
            temp_model = DeleteGlobalResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHBaseHaDBRequest(TeaModel):
    def __init__(
        self,
        bds_id: str = None,
        ha_id: str = None,
    ):
        self.bds_id = bds_id
        self.ha_id = ha_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.bds_id is not None:
            result['BdsId'] = self.bds_id
        if self.ha_id is not None:
            result['HaId'] = self.ha_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BdsId') is not None:
            self.bds_id = m.get('BdsId')
        if m.get('HaId') is not None:
            self.ha_id = m.get('HaId')
        return self


class DeleteHBaseHaDBResponseBody(TeaModel):
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


class DeleteHBaseHaDBResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteHBaseHaDBResponseBody = None,
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
            temp_model = DeleteHBaseHaDBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHbaseHaSlbRequest(TeaModel):
    def __init__(
        self,
        bds_id: str = None,
        ha_id: str = None,
        ha_types: str = None,
    ):
        self.bds_id = bds_id
        self.ha_id = ha_id
        self.ha_types = ha_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.bds_id is not None:
            result['BdsId'] = self.bds_id
        if self.ha_id is not None:
            result['HaId'] = self.ha_id
        if self.ha_types is not None:
            result['HaTypes'] = self.ha_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BdsId') is not None:
            self.bds_id = m.get('BdsId')
        if m.get('HaId') is not None:
            self.ha_id = m.get('HaId')
        if m.get('HaTypes') is not None:
            self.ha_types = m.get('HaTypes')
        return self


class DeleteHbaseHaSlbResponseBody(TeaModel):
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


class DeleteHbaseHaSlbResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteHbaseHaSlbResponseBody = None,
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
            temp_model = DeleteHbaseHaSlbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHBaseSlbServerRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        slb_server: str = None,
    ):
        self.cluster_id = cluster_id
        self.slb_server = slb_server

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.slb_server is not None:
            result['SlbServer'] = self.slb_server
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('SlbServer') is not None:
            self.slb_server = m.get('SlbServer')
        return self


class DeleteHBaseSlbServerResponseBody(TeaModel):
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


class DeleteHBaseSlbServerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteHBaseSlbServerResponseBody = None,
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
            temp_model = DeleteHBaseSlbServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        immediate_delete_flag: bool = None,
    ):
        self.cluster_id = cluster_id
        self.immediate_delete_flag = immediate_delete_flag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.immediate_delete_flag is not None:
            result['ImmediateDeleteFlag'] = self.immediate_delete_flag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ImmediateDeleteFlag') is not None:
            self.immediate_delete_flag = m.get('ImmediateDeleteFlag')
        return self


class DeleteInstanceResponseBody(TeaModel):
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


class DeleteInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteInstanceResponseBody = None,
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
            temp_model = DeleteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMultiZoneClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        immediate_delete_flag: bool = None,
    ):
        self.cluster_id = cluster_id
        self.immediate_delete_flag = immediate_delete_flag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.immediate_delete_flag is not None:
            result['ImmediateDeleteFlag'] = self.immediate_delete_flag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ImmediateDeleteFlag') is not None:
            self.immediate_delete_flag = m.get('ImmediateDeleteFlag')
        return self


class DeleteMultiZoneClusterResponseBody(TeaModel):
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


class DeleteMultiZoneClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteMultiZoneClusterResponseBody = None,
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
            temp_model = DeleteMultiZoneClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServerlessClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
        zone_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.region_id = region_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DeleteServerlessClusterResponseBody(TeaModel):
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


class DeleteServerlessClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteServerlessClusterResponseBody = None,
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
            temp_model = DeleteServerlessClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserHdfsInfoRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        name_service: str = None,
    ):
        self.cluster_id = cluster_id
        self.name_service = name_service

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.name_service is not None:
            result['NameService'] = self.name_service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('NameService') is not None:
            self.name_service = m.get('NameService')
        return self


class DeleteUserHdfsInfoResponseBody(TeaModel):
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


class DeleteUserHdfsInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteUserHdfsInfoResponseBody = None,
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
            temp_model = DeleteUserHdfsInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableResourceRequest(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        region_id: str = None,
        zone_id: str = None,
    ):
        self.charge_type = charge_type
        self.region_id = region_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceInstanceTypeDetail(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        mem: int = None,
    ):
        self.cpu = cpu
        self.mem = mem

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.mem is not None:
            result['Mem'] = self.mem
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Mem') is not None:
            self.mem = m.get('Mem')
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceDBInstanceStorageRange(TeaModel):
    def __init__(
        self,
        max_size: int = None,
        step_size: int = None,
        min_size: int = None,
    ):
        self.max_size = max_size
        self.step_size = step_size
        self.min_size = min_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.max_size is not None:
            result['MaxSize'] = self.max_size
        if self.step_size is not None:
            result['StepSize'] = self.step_size
        if self.min_size is not None:
            result['MinSize'] = self.min_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxSize') is not None:
            self.max_size = m.get('MaxSize')
        if m.get('StepSize') is not None:
            self.step_size = m.get('StepSize')
        if m.get('MinSize') is not None:
            self.min_size = m.get('MinSize')
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResource(TeaModel):
    def __init__(
        self,
        instance_type_detail: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceInstanceTypeDetail = None,
        dbinstance_storage_range: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceDBInstanceStorageRange = None,
        max_core_count: int = None,
        instance_type: str = None,
    ):
        self.instance_type_detail = instance_type_detail
        self.dbinstance_storage_range = dbinstance_storage_range
        self.max_core_count = max_core_count
        self.instance_type = instance_type

    def validate(self):
        if self.instance_type_detail:
            self.instance_type_detail.validate()
        if self.dbinstance_storage_range:
            self.dbinstance_storage_range.validate()

    def to_map(self):
        result = dict()
        if self.instance_type_detail is not None:
            result['InstanceTypeDetail'] = self.instance_type_detail.to_map()
        if self.dbinstance_storage_range is not None:
            result['DBInstanceStorageRange'] = self.dbinstance_storage_range.to_map()
        if self.max_core_count is not None:
            result['MaxCoreCount'] = self.max_core_count
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceTypeDetail') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceInstanceTypeDetail()
            self.instance_type_detail = temp_model.from_map(m['InstanceTypeDetail'])
        if m.get('DBInstanceStorageRange') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceDBInstanceStorageRange()
            self.dbinstance_storage_range = temp_model.from_map(m['DBInstanceStorageRange'])
        if m.get('MaxCoreCount') is not None:
            self.max_core_count = m.get('MaxCoreCount')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResources(TeaModel):
    def __init__(
        self,
        core_resource: List[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResource] = None,
    ):
        self.core_resource = core_resource

    def validate(self):
        if self.core_resource:
            for k in self.core_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['CoreResource'] = []
        if self.core_resource is not None:
            for k in self.core_resource:
                result['CoreResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.core_resource = []
        if m.get('CoreResource') is not None:
            for k in m.get('CoreResource'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResource()
                self.core_resource.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageType(TeaModel):
    def __init__(
        self,
        core_resources: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResources = None,
        storage_type: str = None,
    ):
        self.core_resources = core_resources
        self.storage_type = storage_type

    def validate(self):
        if self.core_resources:
            self.core_resources.validate()

    def to_map(self):
        result = dict()
        if self.core_resources is not None:
            result['CoreResources'] = self.core_resources.to_map()
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoreResources') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResources()
            self.core_resources = temp_model.from_map(m['CoreResources'])
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypes(TeaModel):
    def __init__(
        self,
        supported_storage_type: List[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageType] = None,
    ):
        self.supported_storage_type = supported_storage_type

    def validate(self):
        if self.supported_storage_type:
            for k in self.supported_storage_type:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SupportedStorageType'] = []
        if self.supported_storage_type is not None:
            for k in self.supported_storage_type:
                result['SupportedStorageType'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_storage_type = []
        if m.get('SupportedStorageType') is not None:
            for k in m.get('SupportedStorageType'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageType()
                self.supported_storage_type.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategories(TeaModel):
    def __init__(
        self,
        supported_storage_types: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypes = None,
        category: str = None,
    ):
        self.supported_storage_types = supported_storage_types
        self.category = category

    def validate(self):
        if self.supported_storage_types:
            self.supported_storage_types.validate()

    def to_map(self):
        result = dict()
        if self.supported_storage_types is not None:
            result['SupportedStorageTypes'] = self.supported_storage_types.to_map()
        if self.category is not None:
            result['Category'] = self.category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedStorageTypes') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypes()
            self.supported_storage_types = temp_model.from_map(m['SupportedStorageTypes'])
        if m.get('Category') is not None:
            self.category = m.get('Category')
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategories(TeaModel):
    def __init__(
        self,
        supported_categories: List[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategories] = None,
    ):
        self.supported_categories = supported_categories

    def validate(self):
        if self.supported_categories:
            for k in self.supported_categories:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SupportedCategories'] = []
        if self.supported_categories is not None:
            for k in self.supported_categories:
                result['SupportedCategories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_categories = []
        if m.get('SupportedCategories') is not None:
            for k in m.get('SupportedCategories'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategories()
                self.supported_categories.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersion(TeaModel):
    def __init__(
        self,
        version: str = None,
        supported_categories: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategories = None,
    ):
        self.version = version
        self.supported_categories = supported_categories

    def validate(self):
        if self.supported_categories:
            self.supported_categories.validate()

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.supported_categories is not None:
            result['SupportedCategories'] = self.supported_categories.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('SupportedCategories') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategories()
            self.supported_categories = temp_model.from_map(m['SupportedCategories'])
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersions(TeaModel):
    def __init__(
        self,
        supported_engine_version: List[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersion] = None,
    ):
        self.supported_engine_version = supported_engine_version

    def validate(self):
        if self.supported_engine_version:
            for k in self.supported_engine_version:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SupportedEngineVersion'] = []
        if self.supported_engine_version is not None:
            for k in self.supported_engine_version:
                result['SupportedEngineVersion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_engine_version = []
        if m.get('SupportedEngineVersion') is not None:
            for k in m.get('SupportedEngineVersion'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersion()
                self.supported_engine_version.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngine(TeaModel):
    def __init__(
        self,
        supported_engine_versions: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersions = None,
        engine: str = None,
    ):
        self.supported_engine_versions = supported_engine_versions
        self.engine = engine

    def validate(self):
        if self.supported_engine_versions:
            self.supported_engine_versions.validate()

    def to_map(self):
        result = dict()
        if self.supported_engine_versions is not None:
            result['SupportedEngineVersions'] = self.supported_engine_versions.to_map()
        if self.engine is not None:
            result['Engine'] = self.engine
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedEngineVersions') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersions()
            self.supported_engine_versions = temp_model.from_map(m['SupportedEngineVersions'])
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEngines(TeaModel):
    def __init__(
        self,
        supported_engine: List[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngine] = None,
    ):
        self.supported_engine = supported_engine

    def validate(self):
        if self.supported_engine:
            for k in self.supported_engine:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SupportedEngine'] = []
        if self.supported_engine is not None:
            for k in self.supported_engine:
                result['SupportedEngine'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_engine = []
        if m.get('SupportedEngine') is not None:
            for k in m.get('SupportedEngine'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngine()
                self.supported_engine.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResourceInstanceTypeDetail(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        mem: int = None,
    ):
        self.cpu = cpu
        self.mem = mem

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.mem is not None:
            result['Mem'] = self.mem
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Mem') is not None:
            self.mem = m.get('Mem')
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResource(TeaModel):
    def __init__(
        self,
        instance_type_detail: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResourceInstanceTypeDetail = None,
        instance_type: str = None,
    ):
        self.instance_type_detail = instance_type_detail
        self.instance_type = instance_type

    def validate(self):
        if self.instance_type_detail:
            self.instance_type_detail.validate()

    def to_map(self):
        result = dict()
        if self.instance_type_detail is not None:
            result['InstanceTypeDetail'] = self.instance_type_detail.to_map()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceTypeDetail') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResourceInstanceTypeDetail()
            self.instance_type_detail = temp_model.from_map(m['InstanceTypeDetail'])
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResources(TeaModel):
    def __init__(
        self,
        master_resource: List[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResource] = None,
    ):
        self.master_resource = master_resource

    def validate(self):
        if self.master_resource:
            for k in self.master_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['MasterResource'] = []
        if self.master_resource is not None:
            for k in self.master_resource:
                result['MasterResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.master_resource = []
        if m.get('MasterResource') is not None:
            for k in m.get('MasterResource'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResource()
                self.master_resource.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZone(TeaModel):
    def __init__(
        self,
        supported_engines: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEngines = None,
        zone_id: str = None,
        master_resources: DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResources = None,
        region_id: str = None,
    ):
        self.supported_engines = supported_engines
        self.zone_id = zone_id
        self.master_resources = master_resources
        self.region_id = region_id

    def validate(self):
        if self.supported_engines:
            self.supported_engines.validate()
        if self.master_resources:
            self.master_resources.validate()

    def to_map(self):
        result = dict()
        if self.supported_engines is not None:
            result['SupportedEngines'] = self.supported_engines.to_map()
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.master_resources is not None:
            result['MasterResources'] = self.master_resources.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedEngines') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEngines()
            self.supported_engines = temp_model.from_map(m['SupportedEngines'])
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('MasterResources') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResources()
            self.master_resources = temp_model.from_map(m['MasterResources'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAvailableResourceResponseBodyAvailableZones(TeaModel):
    def __init__(
        self,
        available_zone: List[DescribeAvailableResourceResponseBodyAvailableZonesAvailableZone] = None,
    ):
        self.available_zone = available_zone

    def validate(self):
        if self.available_zone:
            for k in self.available_zone:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AvailableZone'] = []
        if self.available_zone is not None:
            for k in self.available_zone:
                result['AvailableZone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_zone = []
        if m.get('AvailableZone') is not None:
            for k in m.get('AvailableZone'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableZonesAvailableZone()
                self.available_zone.append(temp_model.from_map(k))
        return self


class DescribeAvailableResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        available_zones: DescribeAvailableResourceResponseBodyAvailableZones = None,
    ):
        self.request_id = request_id
        self.available_zones = available_zones

    def validate(self):
        if self.available_zones:
            self.available_zones.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.available_zones is not None:
            result['AvailableZones'] = self.available_zones.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AvailableZones') is not None:
            temp_model = DescribeAvailableResourceResponseBodyAvailableZones()
            self.available_zones = temp_model.from_map(m['AvailableZones'])
        return self


class DescribeAvailableResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAvailableResourceResponseBody = None,
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
            temp_model = DescribeAvailableResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPlanConfigRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeBackupPlanConfigResponseBodyTables(TeaModel):
    def __init__(
        self,
        table: List[str] = None,
    ):
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class DescribeBackupPlanConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        full_backup_cycle: int = None,
        next_full_backup_date: str = None,
        tables: DescribeBackupPlanConfigResponseBodyTables = None,
        min_hfile_backup_count: int = None,
    ):
        self.request_id = request_id
        self.full_backup_cycle = full_backup_cycle
        self.next_full_backup_date = next_full_backup_date
        self.tables = tables
        self.min_hfile_backup_count = min_hfile_backup_count

    def validate(self):
        if self.tables:
            self.tables.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.full_backup_cycle is not None:
            result['FullBackupCycle'] = self.full_backup_cycle
        if self.next_full_backup_date is not None:
            result['NextFullBackupDate'] = self.next_full_backup_date
        if self.tables is not None:
            result['Tables'] = self.tables.to_map()
        if self.min_hfile_backup_count is not None:
            result['MinHFileBackupCount'] = self.min_hfile_backup_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FullBackupCycle') is not None:
            self.full_backup_cycle = m.get('FullBackupCycle')
        if m.get('NextFullBackupDate') is not None:
            self.next_full_backup_date = m.get('NextFullBackupDate')
        if m.get('Tables') is not None:
            temp_model = DescribeBackupPlanConfigResponseBodyTables()
            self.tables = temp_model.from_map(m['Tables'])
        if m.get('MinHFileBackupCount') is not None:
            self.min_hfile_backup_count = m.get('MinHFileBackupCount')
        return self


class DescribeBackupPlanConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBackupPlanConfigResponseBody = None,
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
            temp_model = DescribeBackupPlanConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPolicyRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeBackupPolicyResponseBody(TeaModel):
    def __init__(
        self,
        preferred_backup_period: str = None,
        preferred_backup_end_time_utc: str = None,
        preferred_backup_start_time_utc: str = None,
        request_id: str = None,
        preferred_backup_time: str = None,
        backup_retention_period: str = None,
    ):
        self.preferred_backup_period = preferred_backup_period
        self.preferred_backup_end_time_utc = preferred_backup_end_time_utc
        self.preferred_backup_start_time_utc = preferred_backup_start_time_utc
        self.request_id = request_id
        self.preferred_backup_time = preferred_backup_time
        self.backup_retention_period = backup_retention_period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.preferred_backup_end_time_utc is not None:
            result['PreferredBackupEndTimeUTC'] = self.preferred_backup_end_time_utc
        if self.preferred_backup_start_time_utc is not None:
            result['PreferredBackupStartTimeUTC'] = self.preferred_backup_start_time_utc
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.backup_retention_period is not None:
            result['BackupRetentionPeriod'] = self.backup_retention_period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('PreferredBackupEndTimeUTC') is not None:
            self.preferred_backup_end_time_utc = m.get('PreferredBackupEndTimeUTC')
        if m.get('PreferredBackupStartTimeUTC') is not None:
            self.preferred_backup_start_time_utc = m.get('PreferredBackupStartTimeUTC')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('BackupRetentionPeriod') is not None:
            self.backup_retention_period = m.get('BackupRetentionPeriod')
        return self


class DescribeBackupPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBackupPolicyResponseBody = None,
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
            temp_model = DescribeBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        backup_id: str = None,
        page_number: str = None,
        page_size: str = None,
        start_time: str = None,
        end_time: str = None,
        start_time_utc: str = None,
        end_time_utc: str = None,
    ):
        self.cluster_id = cluster_id
        self.backup_id = backup_id
        self.page_number = page_number
        self.page_size = page_size
        self.start_time = start_time
        self.end_time = end_time
        self.start_time_utc = start_time_utc
        self.end_time_utc = end_time_utc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time_utc is not None:
            result['StartTimeUTC'] = self.start_time_utc
        if self.end_time_utc is not None:
            result['EndTimeUTC'] = self.end_time_utc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTimeUTC') is not None:
            self.start_time_utc = m.get('StartTimeUTC')
        if m.get('EndTimeUTC') is not None:
            self.end_time_utc = m.get('EndTimeUTC')
        return self


class DescribeBackupsResponseBodyBackupsBackup(TeaModel):
    def __init__(
        self,
        backup_status: str = None,
        backup_type: str = None,
        backup_start_time: str = None,
        backup_download_url: str = None,
        backup_start_time_utc: str = None,
        backup_end_time: str = None,
        backup_id: int = None,
        backup_dbnames: str = None,
        backup_end_time_utc: str = None,
        backup_size: str = None,
        backup_mode: str = None,
        backup_method: str = None,
    ):
        self.backup_status = backup_status
        self.backup_type = backup_type
        self.backup_start_time = backup_start_time
        self.backup_download_url = backup_download_url
        self.backup_start_time_utc = backup_start_time_utc
        self.backup_end_time = backup_end_time
        self.backup_id = backup_id
        self.backup_dbnames = backup_dbnames
        self.backup_end_time_utc = backup_end_time_utc
        self.backup_size = backup_size
        self.backup_mode = backup_mode
        self.backup_method = backup_method

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.backup_start_time is not None:
            result['BackupStartTime'] = self.backup_start_time
        if self.backup_download_url is not None:
            result['BackupDownloadURL'] = self.backup_download_url
        if self.backup_start_time_utc is not None:
            result['BackupStartTimeUTC'] = self.backup_start_time_utc
        if self.backup_end_time is not None:
            result['BackupEndTime'] = self.backup_end_time
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_dbnames is not None:
            result['BackupDBNames'] = self.backup_dbnames
        if self.backup_end_time_utc is not None:
            result['BackupEndTimeUTC'] = self.backup_end_time_utc
        if self.backup_size is not None:
            result['BackupSize'] = self.backup_size
        if self.backup_mode is not None:
            result['BackupMode'] = self.backup_mode
        if self.backup_method is not None:
            result['BackupMethod'] = self.backup_method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BackupStartTime') is not None:
            self.backup_start_time = m.get('BackupStartTime')
        if m.get('BackupDownloadURL') is not None:
            self.backup_download_url = m.get('BackupDownloadURL')
        if m.get('BackupStartTimeUTC') is not None:
            self.backup_start_time_utc = m.get('BackupStartTimeUTC')
        if m.get('BackupEndTime') is not None:
            self.backup_end_time = m.get('BackupEndTime')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupDBNames') is not None:
            self.backup_dbnames = m.get('BackupDBNames')
        if m.get('BackupEndTimeUTC') is not None:
            self.backup_end_time_utc = m.get('BackupEndTimeUTC')
        if m.get('BackupSize') is not None:
            self.backup_size = m.get('BackupSize')
        if m.get('BackupMode') is not None:
            self.backup_mode = m.get('BackupMode')
        if m.get('BackupMethod') is not None:
            self.backup_method = m.get('BackupMethod')
        return self


class DescribeBackupsResponseBodyBackups(TeaModel):
    def __init__(
        self,
        backup: List[DescribeBackupsResponseBodyBackupsBackup] = None,
    ):
        self.backup = backup

    def validate(self):
        if self.backup:
            for k in self.backup:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Backup'] = []
        if self.backup is not None:
            for k in self.backup:
                result['Backup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup = []
        if m.get('Backup') is not None:
            for k in m.get('Backup'):
                temp_model = DescribeBackupsResponseBodyBackupsBackup()
                self.backup.append(temp_model.from_map(k))
        return self


class DescribeBackupsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        enable_status: str = None,
        backups: DescribeBackupsResponseBodyBackups = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.enable_status = enable_status
        self.backups = backups

    def validate(self):
        if self.backups:
            self.backups.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status
        if self.backups is not None:
            result['Backups'] = self.backups.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')
        if m.get('Backups') is not None:
            temp_model = DescribeBackupsResponseBodyBackups()
            self.backups = temp_model.from_map(m['Backups'])
        return self


class DescribeBackupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBackupsResponseBody = None,
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
            temp_model = DescribeBackupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupStatusRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeBackupStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        bds_cluster_id: str = None,
        cluster_id: str = None,
        backup_status: str = None,
    ):
        self.request_id = request_id
        self.bds_cluster_id = bds_cluster_id
        self.cluster_id = cluster_id
        self.backup_status = backup_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.bds_cluster_id is not None:
            result['BdsClusterId'] = self.bds_cluster_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BdsClusterId') is not None:
            self.bds_cluster_id = m.get('BdsClusterId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        return self


class DescribeBackupStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBackupStatusResponseBody = None,
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
            temp_model = DescribeBackupStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupSummaryRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.cluster_id = cluster_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeBackupSummaryResponseBodyIncr(TeaModel):
    def __init__(
        self,
        status: str = None,
        speed: str = None,
        pos: str = None,
        queue_log_num: str = None,
        backup_log_size: str = None,
        running_log_num: str = None,
    ):
        self.status = status
        self.speed = speed
        self.pos = pos
        self.queue_log_num = queue_log_num
        self.backup_log_size = backup_log_size
        self.running_log_num = running_log_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.pos is not None:
            result['Pos'] = self.pos
        if self.queue_log_num is not None:
            result['QueueLogNum'] = self.queue_log_num
        if self.backup_log_size is not None:
            result['BackupLogSize'] = self.backup_log_size
        if self.running_log_num is not None:
            result['RunningLogNum'] = self.running_log_num
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('Pos') is not None:
            self.pos = m.get('Pos')
        if m.get('QueueLogNum') is not None:
            self.queue_log_num = m.get('QueueLogNum')
        if m.get('BackupLogSize') is not None:
            self.backup_log_size = m.get('BackupLogSize')
        if m.get('RunningLogNum') is not None:
            self.running_log_num = m.get('RunningLogNum')
        return self


class DescribeBackupSummaryResponseBodyFullRecordsRecord(TeaModel):
    def __init__(
        self,
        status: str = None,
        finish_time: str = None,
        process: str = None,
        data_size: str = None,
        speed: str = None,
        record_id: str = None,
        create_time: str = None,
    ):
        self.status = status
        self.finish_time = finish_time
        self.process = process
        self.data_size = data_size
        self.speed = speed
        self.record_id = record_id
        self.create_time = create_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.process is not None:
            result['Process'] = self.process
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class DescribeBackupSummaryResponseBodyFullRecords(TeaModel):
    def __init__(
        self,
        record: List[DescribeBackupSummaryResponseBodyFullRecordsRecord] = None,
    ):
        self.record = record

    def validate(self):
        if self.record:
            for k in self.record:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Record'] = []
        if self.record is not None:
            for k in self.record:
                result['Record'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.record = []
        if m.get('Record') is not None:
            for k in m.get('Record'):
                temp_model = DescribeBackupSummaryResponseBodyFullRecordsRecord()
                self.record.append(temp_model.from_map(k))
        return self


class DescribeBackupSummaryResponseBodyFull(TeaModel):
    def __init__(
        self,
        next_full_backup_date: str = None,
        records: DescribeBackupSummaryResponseBodyFullRecords = None,
        has_more: str = None,
        page_size: int = None,
        page_number: int = None,
        total: int = None,
    ):
        self.next_full_backup_date = next_full_backup_date
        self.records = records
        self.has_more = has_more
        self.page_size = page_size
        self.page_number = page_number
        self.total = total

    def validate(self):
        if self.records:
            self.records.validate()

    def to_map(self):
        result = dict()
        if self.next_full_backup_date is not None:
            result['NextFullBackupDate'] = self.next_full_backup_date
        if self.records is not None:
            result['Records'] = self.records.to_map()
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextFullBackupDate') is not None:
            self.next_full_backup_date = m.get('NextFullBackupDate')
        if m.get('Records') is not None:
            temp_model = DescribeBackupSummaryResponseBodyFullRecords()
            self.records = temp_model.from_map(m['Records'])
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeBackupSummaryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        incr: DescribeBackupSummaryResponseBodyIncr = None,
        full: DescribeBackupSummaryResponseBodyFull = None,
    ):
        self.request_id = request_id
        self.incr = incr
        self.full = full

    def validate(self):
        if self.incr:
            self.incr.validate()
        if self.full:
            self.full.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.incr is not None:
            result['Incr'] = self.incr.to_map()
        if self.full is not None:
            result['Full'] = self.full.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Incr') is not None:
            temp_model = DescribeBackupSummaryResponseBodyIncr()
            self.incr = temp_model.from_map(m['Incr'])
        if m.get('Full') is not None:
            temp_model = DescribeBackupSummaryResponseBodyFull()
            self.full = temp_model.from_map(m['Full'])
        return self


class DescribeBackupSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBackupSummaryResponseBody = None,
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
            temp_model = DescribeBackupSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupTablesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        backup_record_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.cluster_id = cluster_id
        self.backup_record_id = backup_record_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.backup_record_id is not None:
            result['BackupRecordId'] = self.backup_record_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('BackupRecordId') is not None:
            self.backup_record_id = m.get('BackupRecordId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeBackupTablesResponseBodyBackupRecordsBackupRecord(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        process: str = None,
        data_size: str = None,
        speed: str = None,
        state: str = None,
        message: str = None,
        table: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.process = process
        self.data_size = data_size
        self.speed = speed
        self.state = state
        self.message = message
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.process is not None:
            result['Process'] = self.process
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.state is not None:
            result['State'] = self.state
        if self.message is not None:
            result['Message'] = self.message
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class DescribeBackupTablesResponseBodyBackupRecords(TeaModel):
    def __init__(
        self,
        backup_record: List[DescribeBackupTablesResponseBodyBackupRecordsBackupRecord] = None,
    ):
        self.backup_record = backup_record

    def validate(self):
        if self.backup_record:
            for k in self.backup_record:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['BackupRecord'] = []
        if self.backup_record is not None:
            for k in self.backup_record:
                result['BackupRecord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup_record = []
        if m.get('BackupRecord') is not None:
            for k in m.get('BackupRecord'):
                temp_model = DescribeBackupTablesResponseBodyBackupRecordsBackupRecord()
                self.backup_record.append(temp_model.from_map(k))
        return self


class DescribeBackupTablesResponseBodyTables(TeaModel):
    def __init__(
        self,
        table: List[str] = None,
    ):
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class DescribeBackupTablesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_size: int = None,
        backup_records: DescribeBackupTablesResponseBodyBackupRecords = None,
        page_number: int = None,
        total: int = None,
        tables: DescribeBackupTablesResponseBodyTables = None,
    ):
        self.request_id = request_id
        self.page_size = page_size
        self.backup_records = backup_records
        self.page_number = page_number
        self.total = total
        self.tables = tables

    def validate(self):
        if self.backup_records:
            self.backup_records.validate()
        if self.tables:
            self.tables.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.backup_records is not None:
            result['BackupRecords'] = self.backup_records.to_map()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total is not None:
            result['Total'] = self.total
        if self.tables is not None:
            result['Tables'] = self.tables.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('BackupRecords') is not None:
            temp_model = DescribeBackupTablesResponseBodyBackupRecords()
            self.backup_records = temp_model.from_map(m['BackupRecords'])
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('Tables') is not None:
            temp_model = DescribeBackupTablesResponseBodyTables()
            self.tables = temp_model.from_map(m['Tables'])
        return self


class DescribeBackupTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBackupTablesResponseBody = None,
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
            temp_model = DescribeBackupTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterConnectionRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        cluster_id: str = None,
    ):
        self.region_id = region_id
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeClusterConnectionResponseBodyUiProxyConnAddrInfo(TeaModel):
    def __init__(
        self,
        conn_addr_port: str = None,
        net_type: str = None,
        conn_addr: str = None,
    ):
        self.conn_addr_port = conn_addr_port
        self.net_type = net_type
        self.conn_addr = conn_addr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.conn_addr_port is not None:
            result['ConnAddrPort'] = self.conn_addr_port
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.conn_addr is not None:
            result['ConnAddr'] = self.conn_addr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnAddrPort') is not None:
            self.conn_addr_port = m.get('ConnAddrPort')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('ConnAddr') is not None:
            self.conn_addr = m.get('ConnAddr')
        return self


class DescribeClusterConnectionResponseBodyServiceConnAddrsServiceConnAddrConnAddrInfo(TeaModel):
    def __init__(
        self,
        conn_addr_port: str = None,
        net_type: str = None,
        conn_addr: str = None,
    ):
        self.conn_addr_port = conn_addr_port
        self.net_type = net_type
        self.conn_addr = conn_addr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.conn_addr_port is not None:
            result['ConnAddrPort'] = self.conn_addr_port
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.conn_addr is not None:
            result['ConnAddr'] = self.conn_addr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnAddrPort') is not None:
            self.conn_addr_port = m.get('ConnAddrPort')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('ConnAddr') is not None:
            self.conn_addr = m.get('ConnAddr')
        return self


class DescribeClusterConnectionResponseBodyServiceConnAddrsServiceConnAddr(TeaModel):
    def __init__(
        self,
        conn_addr_info: DescribeClusterConnectionResponseBodyServiceConnAddrsServiceConnAddrConnAddrInfo = None,
        conn_type: str = None,
    ):
        self.conn_addr_info = conn_addr_info
        self.conn_type = conn_type

    def validate(self):
        if self.conn_addr_info:
            self.conn_addr_info.validate()

    def to_map(self):
        result = dict()
        if self.conn_addr_info is not None:
            result['ConnAddrInfo'] = self.conn_addr_info.to_map()
        if self.conn_type is not None:
            result['ConnType'] = self.conn_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnAddrInfo') is not None:
            temp_model = DescribeClusterConnectionResponseBodyServiceConnAddrsServiceConnAddrConnAddrInfo()
            self.conn_addr_info = temp_model.from_map(m['ConnAddrInfo'])
        if m.get('ConnType') is not None:
            self.conn_type = m.get('ConnType')
        return self


class DescribeClusterConnectionResponseBodyServiceConnAddrs(TeaModel):
    def __init__(
        self,
        service_conn_addr: List[DescribeClusterConnectionResponseBodyServiceConnAddrsServiceConnAddr] = None,
    ):
        self.service_conn_addr = service_conn_addr

    def validate(self):
        if self.service_conn_addr:
            for k in self.service_conn_addr:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ServiceConnAddr'] = []
        if self.service_conn_addr is not None:
            for k in self.service_conn_addr:
                result['ServiceConnAddr'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.service_conn_addr = []
        if m.get('ServiceConnAddr') is not None:
            for k in m.get('ServiceConnAddr'):
                temp_model = DescribeClusterConnectionResponseBodyServiceConnAddrsServiceConnAddr()
                self.service_conn_addr.append(temp_model.from_map(k))
        return self


class DescribeClusterConnectionResponseBodyThriftConn(TeaModel):
    def __init__(
        self,
        conn_addr_port: str = None,
        net_type: str = None,
        conn_addr: str = None,
    ):
        self.conn_addr_port = conn_addr_port
        self.net_type = net_type
        self.conn_addr = conn_addr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.conn_addr_port is not None:
            result['ConnAddrPort'] = self.conn_addr_port
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.conn_addr is not None:
            result['ConnAddr'] = self.conn_addr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnAddrPort') is not None:
            self.conn_addr_port = m.get('ConnAddrPort')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('ConnAddr') is not None:
            self.conn_addr = m.get('ConnAddr')
        return self


class DescribeClusterConnectionResponseBodyZkConnAddrsZkConnAddr(TeaModel):
    def __init__(
        self,
        conn_addr_port: str = None,
        net_type: str = None,
        conn_addr: str = None,
    ):
        self.conn_addr_port = conn_addr_port
        self.net_type = net_type
        self.conn_addr = conn_addr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.conn_addr_port is not None:
            result['ConnAddrPort'] = self.conn_addr_port
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.conn_addr is not None:
            result['ConnAddr'] = self.conn_addr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnAddrPort') is not None:
            self.conn_addr_port = m.get('ConnAddrPort')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('ConnAddr') is not None:
            self.conn_addr = m.get('ConnAddr')
        return self


class DescribeClusterConnectionResponseBodyZkConnAddrs(TeaModel):
    def __init__(
        self,
        zk_conn_addr: List[DescribeClusterConnectionResponseBodyZkConnAddrsZkConnAddr] = None,
    ):
        self.zk_conn_addr = zk_conn_addr

    def validate(self):
        if self.zk_conn_addr:
            for k in self.zk_conn_addr:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ZkConnAddr'] = []
        if self.zk_conn_addr is not None:
            for k in self.zk_conn_addr:
                result['ZkConnAddr'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zk_conn_addr = []
        if m.get('ZkConnAddr') is not None:
            for k in m.get('ZkConnAddr'):
                temp_model = DescribeClusterConnectionResponseBodyZkConnAddrsZkConnAddr()
                self.zk_conn_addr.append(temp_model.from_map(k))
        return self


class DescribeClusterConnectionResponseBodySlbConnAddrsSlbConnAddrConnAddrInfo(TeaModel):
    def __init__(
        self,
        conn_addr_port: str = None,
        net_type: str = None,
        conn_addr: str = None,
    ):
        self.conn_addr_port = conn_addr_port
        self.net_type = net_type
        self.conn_addr = conn_addr

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.conn_addr_port is not None:
            result['ConnAddrPort'] = self.conn_addr_port
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.conn_addr is not None:
            result['ConnAddr'] = self.conn_addr
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnAddrPort') is not None:
            self.conn_addr_port = m.get('ConnAddrPort')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('ConnAddr') is not None:
            self.conn_addr = m.get('ConnAddr')
        return self


class DescribeClusterConnectionResponseBodySlbConnAddrsSlbConnAddr(TeaModel):
    def __init__(
        self,
        conn_addr_info: DescribeClusterConnectionResponseBodySlbConnAddrsSlbConnAddrConnAddrInfo = None,
        slb_type: str = None,
    ):
        self.conn_addr_info = conn_addr_info
        self.slb_type = slb_type

    def validate(self):
        if self.conn_addr_info:
            self.conn_addr_info.validate()

    def to_map(self):
        result = dict()
        if self.conn_addr_info is not None:
            result['ConnAddrInfo'] = self.conn_addr_info.to_map()
        if self.slb_type is not None:
            result['SlbType'] = self.slb_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnAddrInfo') is not None:
            temp_model = DescribeClusterConnectionResponseBodySlbConnAddrsSlbConnAddrConnAddrInfo()
            self.conn_addr_info = temp_model.from_map(m['ConnAddrInfo'])
        if m.get('SlbType') is not None:
            self.slb_type = m.get('SlbType')
        return self


class DescribeClusterConnectionResponseBodySlbConnAddrs(TeaModel):
    def __init__(
        self,
        slb_conn_addr: List[DescribeClusterConnectionResponseBodySlbConnAddrsSlbConnAddr] = None,
    ):
        self.slb_conn_addr = slb_conn_addr

    def validate(self):
        if self.slb_conn_addr:
            for k in self.slb_conn_addr:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SlbConnAddr'] = []
        if self.slb_conn_addr is not None:
            for k in self.slb_conn_addr:
                result['SlbConnAddr'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.slb_conn_addr = []
        if m.get('SlbConnAddr') is not None:
            for k in m.get('SlbConnAddr'):
                temp_model = DescribeClusterConnectionResponseBodySlbConnAddrsSlbConnAddr()
                self.slb_conn_addr.append(temp_model.from_map(k))
        return self


class DescribeClusterConnectionResponseBody(TeaModel):
    def __init__(
        self,
        is_multimod: str = None,
        vpc_id: str = None,
        request_id: str = None,
        ui_proxy_conn_addr_info: DescribeClusterConnectionResponseBodyUiProxyConnAddrInfo = None,
        v_switch_id: str = None,
        service_conn_addrs: DescribeClusterConnectionResponseBodyServiceConnAddrs = None,
        net_type: str = None,
        db_type: str = None,
        thrift_conn: DescribeClusterConnectionResponseBodyThriftConn = None,
        zk_conn_addrs: DescribeClusterConnectionResponseBodyZkConnAddrs = None,
        slb_conn_addrs: DescribeClusterConnectionResponseBodySlbConnAddrs = None,
    ):
        self.is_multimod = is_multimod
        self.vpc_id = vpc_id
        self.request_id = request_id
        self.ui_proxy_conn_addr_info = ui_proxy_conn_addr_info
        self.v_switch_id = v_switch_id
        self.service_conn_addrs = service_conn_addrs
        self.net_type = net_type
        self.db_type = db_type
        self.thrift_conn = thrift_conn
        self.zk_conn_addrs = zk_conn_addrs
        self.slb_conn_addrs = slb_conn_addrs

    def validate(self):
        if self.ui_proxy_conn_addr_info:
            self.ui_proxy_conn_addr_info.validate()
        if self.service_conn_addrs:
            self.service_conn_addrs.validate()
        if self.thrift_conn:
            self.thrift_conn.validate()
        if self.zk_conn_addrs:
            self.zk_conn_addrs.validate()
        if self.slb_conn_addrs:
            self.slb_conn_addrs.validate()

    def to_map(self):
        result = dict()
        if self.is_multimod is not None:
            result['IsMultimod'] = self.is_multimod
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ui_proxy_conn_addr_info is not None:
            result['UiProxyConnAddrInfo'] = self.ui_proxy_conn_addr_info.to_map()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.service_conn_addrs is not None:
            result['ServiceConnAddrs'] = self.service_conn_addrs.to_map()
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.thrift_conn is not None:
            result['ThriftConn'] = self.thrift_conn.to_map()
        if self.zk_conn_addrs is not None:
            result['ZkConnAddrs'] = self.zk_conn_addrs.to_map()
        if self.slb_conn_addrs is not None:
            result['SlbConnAddrs'] = self.slb_conn_addrs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsMultimod') is not None:
            self.is_multimod = m.get('IsMultimod')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UiProxyConnAddrInfo') is not None:
            temp_model = DescribeClusterConnectionResponseBodyUiProxyConnAddrInfo()
            self.ui_proxy_conn_addr_info = temp_model.from_map(m['UiProxyConnAddrInfo'])
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ServiceConnAddrs') is not None:
            temp_model = DescribeClusterConnectionResponseBodyServiceConnAddrs()
            self.service_conn_addrs = temp_model.from_map(m['ServiceConnAddrs'])
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('ThriftConn') is not None:
            temp_model = DescribeClusterConnectionResponseBodyThriftConn()
            self.thrift_conn = temp_model.from_map(m['ThriftConn'])
        if m.get('ZkConnAddrs') is not None:
            temp_model = DescribeClusterConnectionResponseBodyZkConnAddrs()
            self.zk_conn_addrs = temp_model.from_map(m['ZkConnAddrs'])
        if m.get('SlbConnAddrs') is not None:
            temp_model = DescribeClusterConnectionResponseBodySlbConnAddrs()
            self.slb_conn_addrs = temp_model.from_map(m['SlbConnAddrs'])
        return self


class DescribeClusterConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeClusterConnectionResponseBody = None,
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
            temp_model = DescribeClusterConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeColdStorageRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeColdStorageResponseBody(TeaModel):
    def __init__(
        self,
        cold_storage_use_percent: str = None,
        cold_storage_size: str = None,
        request_id: str = None,
        cluster_id: str = None,
        pay_type: str = None,
        open_status: str = None,
    ):
        self.cold_storage_use_percent = cold_storage_use_percent
        self.cold_storage_size = cold_storage_size
        self.request_id = request_id
        self.cluster_id = cluster_id
        self.pay_type = pay_type
        self.open_status = open_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cold_storage_use_percent is not None:
            result['ColdStorageUsePercent'] = self.cold_storage_use_percent
        if self.cold_storage_size is not None:
            result['ColdStorageSize'] = self.cold_storage_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.open_status is not None:
            result['OpenStatus'] = self.open_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColdStorageUsePercent') is not None:
            self.cold_storage_use_percent = m.get('ColdStorageUsePercent')
        if m.get('ColdStorageSize') is not None:
            self.cold_storage_size = m.get('ColdStorageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('OpenStatus') is not None:
            self.open_status = m.get('OpenStatus')
        return self


class DescribeColdStorageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeColdStorageResponseBody = None,
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
            temp_model = DescribeColdStorageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDBInstanceUsageRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeDBInstanceUsageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
    ):
        self.request_id = request_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DescribeDBInstanceUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDBInstanceUsageResponseBody = None,
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
            temp_model = DescribeDBInstanceUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeletedInstancesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeDeletedInstancesResponseBodyInstancesInstance(TeaModel):
    def __init__(
        self,
        status: str = None,
        instance_id: str = None,
        region_id: str = None,
        parent_id: str = None,
        cluster_type: str = None,
        instance_name: str = None,
        delete_time: str = None,
        zone_id: str = None,
        module_stack_version: str = None,
        engine: str = None,
        major_version: str = None,
        created_time: str = None,
    ):
        self.status = status
        self.instance_id = instance_id
        self.region_id = region_id
        self.parent_id = parent_id
        self.cluster_type = cluster_type
        self.instance_name = instance_name
        self.delete_time = delete_time
        self.zone_id = zone_id
        self.module_stack_version = module_stack_version
        self.engine = engine
        self.major_version = major_version
        self.created_time = created_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.delete_time is not None:
            result['DeleteTime'] = self.delete_time
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.module_stack_version is not None:
            result['ModuleStackVersion'] = self.module_stack_version
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('DeleteTime') is not None:
            self.delete_time = m.get('DeleteTime')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ModuleStackVersion') is not None:
            self.module_stack_version = m.get('ModuleStackVersion')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        return self


class DescribeDeletedInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        instance: List[DescribeDeletedInstancesResponseBodyInstancesInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = DescribeDeletedInstancesResponseBodyInstancesInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class DescribeDeletedInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: DescribeDeletedInstancesResponseBodyInstances = None,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
    ):
        self.instances = instances
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = dict()
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instances') is not None:
            temp_model = DescribeDeletedInstancesResponseBodyInstances()
            self.instances = temp_model.from_map(m['Instances'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeDeletedInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDeletedInstancesResponseBody = None,
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
            temp_model = DescribeDeletedInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiskWarningLineRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeDiskWarningLineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        warning_line: str = None,
    ):
        self.request_id = request_id
        self.warning_line = warning_line

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.warning_line is not None:
            result['WarningLine'] = self.warning_line
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('WarningLine') is not None:
            self.warning_line = m.get('WarningLine')
        return self


class DescribeDiskWarningLineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDiskWarningLineResponseBody = None,
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
            temp_model = DescribeDiskWarningLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEndpointsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeEndpointsResponseBodyConnAddrsConnAddrInfo(TeaModel):
    def __init__(
        self,
        conn_addr_port: str = None,
        net_type: str = None,
        conn_addr: str = None,
        conn_type: str = None,
    ):
        self.conn_addr_port = conn_addr_port
        self.net_type = net_type
        self.conn_addr = conn_addr
        self.conn_type = conn_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.conn_addr_port is not None:
            result['ConnAddrPort'] = self.conn_addr_port
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.conn_addr is not None:
            result['ConnAddr'] = self.conn_addr
        if self.conn_type is not None:
            result['ConnType'] = self.conn_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnAddrPort') is not None:
            self.conn_addr_port = m.get('ConnAddrPort')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('ConnAddr') is not None:
            self.conn_addr = m.get('ConnAddr')
        if m.get('ConnType') is not None:
            self.conn_type = m.get('ConnType')
        return self


class DescribeEndpointsResponseBodyConnAddrs(TeaModel):
    def __init__(
        self,
        conn_addr_info: List[DescribeEndpointsResponseBodyConnAddrsConnAddrInfo] = None,
    ):
        self.conn_addr_info = conn_addr_info

    def validate(self):
        if self.conn_addr_info:
            for k in self.conn_addr_info:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ConnAddrInfo'] = []
        if self.conn_addr_info is not None:
            for k in self.conn_addr_info:
                result['ConnAddrInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conn_addr_info = []
        if m.get('ConnAddrInfo') is not None:
            for k in m.get('ConnAddrInfo'):
                temp_model = DescribeEndpointsResponseBodyConnAddrsConnAddrInfo()
                self.conn_addr_info.append(temp_model.from_map(k))
        return self


class DescribeEndpointsResponseBody(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        request_id: str = None,
        conn_addrs: DescribeEndpointsResponseBodyConnAddrs = None,
        v_switch_id: str = None,
        net_type: str = None,
        engine: str = None,
    ):
        self.vpc_id = vpc_id
        self.request_id = request_id
        self.conn_addrs = conn_addrs
        self.v_switch_id = v_switch_id
        self.net_type = net_type
        self.engine = engine

    def validate(self):
        if self.conn_addrs:
            self.conn_addrs.validate()

    def to_map(self):
        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.conn_addrs is not None:
            result['ConnAddrs'] = self.conn_addrs.to_map()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.net_type is not None:
            result['NetType'] = self.net_type
        if self.engine is not None:
            result['Engine'] = self.engine
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ConnAddrs') is not None:
            temp_model = DescribeEndpointsResponseBodyConnAddrs()
            self.conn_addrs = temp_model.from_map(m['ConnAddrs'])
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        return self


class DescribeEndpointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeEndpointsResponseBody = None,
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
            temp_model = DescribeEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeInstanceResponseBodyTagsTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeInstanceResponseBodyTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeInstanceResponseBodyTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeInstanceResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        module_stack_version: str = None,
        is_ha: bool = None,
        created_time: str = None,
        resource_group_id: str = None,
        master_instance_type: str = None,
        is_deletion_protection: bool = None,
        module_id: int = None,
        is_latest_version: bool = None,
        maintain_end_time: str = None,
        network_type: str = None,
        core_instance_type: str = None,
        cluster_name: str = None,
        master_disk_type: str = None,
        maintain_start_time: str = None,
        engine: str = None,
        tags: DescribeInstanceResponseBodyTags = None,
        status: str = None,
        cold_storage_size: int = None,
        parent_id: str = None,
        major_version: str = None,
        core_disk_count: str = None,
        expire_time_utc: str = None,
        master_disk_size: int = None,
        request_id: str = None,
        zone_id: str = None,
        cluster_id: str = None,
        instance_id: str = None,
        core_node_count: int = None,
        cold_storage_status: str = None,
        created_time_utc: str = None,
        minor_version: str = None,
        duration: int = None,
        pay_type: str = None,
        is_multi_model: bool = None,
        cluster_type: str = None,
        vswitch_id: str = None,
        master_node_count: int = None,
        instance_name: str = None,
        vpc_id: str = None,
        auto_renewal: bool = None,
        core_disk_type: str = None,
        region_id: str = None,
        expire_time: str = None,
        backup_status: str = None,
        core_disk_size: int = None,
    ):
        self.module_stack_version = module_stack_version
        self.is_ha = is_ha
        self.created_time = created_time
        self.resource_group_id = resource_group_id
        self.master_instance_type = master_instance_type
        self.is_deletion_protection = is_deletion_protection
        self.module_id = module_id
        self.is_latest_version = is_latest_version
        self.maintain_end_time = maintain_end_time
        self.network_type = network_type
        self.core_instance_type = core_instance_type
        self.cluster_name = cluster_name
        self.master_disk_type = master_disk_type
        self.maintain_start_time = maintain_start_time
        self.engine = engine
        self.tags = tags
        self.status = status
        self.cold_storage_size = cold_storage_size
        self.parent_id = parent_id
        self.major_version = major_version
        self.core_disk_count = core_disk_count
        self.expire_time_utc = expire_time_utc
        self.master_disk_size = master_disk_size
        self.request_id = request_id
        self.zone_id = zone_id
        self.cluster_id = cluster_id
        self.instance_id = instance_id
        self.core_node_count = core_node_count
        self.cold_storage_status = cold_storage_status
        self.created_time_utc = created_time_utc
        self.minor_version = minor_version
        self.duration = duration
        self.pay_type = pay_type
        self.is_multi_model = is_multi_model
        self.cluster_type = cluster_type
        self.vswitch_id = vswitch_id
        self.master_node_count = master_node_count
        self.instance_name = instance_name
        self.vpc_id = vpc_id
        self.auto_renewal = auto_renewal
        self.core_disk_type = core_disk_type
        self.region_id = region_id
        self.expire_time = expire_time
        self.backup_status = backup_status
        self.core_disk_size = core_disk_size

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        if self.module_stack_version is not None:
            result['ModuleStackVersion'] = self.module_stack_version
        if self.is_ha is not None:
            result['IsHa'] = self.is_ha
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.master_instance_type is not None:
            result['MasterInstanceType'] = self.master_instance_type
        if self.is_deletion_protection is not None:
            result['IsDeletionProtection'] = self.is_deletion_protection
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.is_latest_version is not None:
            result['IsLatestVersion'] = self.is_latest_version
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.core_instance_type is not None:
            result['CoreInstanceType'] = self.core_instance_type
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.master_disk_type is not None:
            result['MasterDiskType'] = self.master_disk_type
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.cold_storage_size is not None:
            result['ColdStorageSize'] = self.cold_storage_size
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
        if self.core_disk_count is not None:
            result['CoreDiskCount'] = self.core_disk_count
        if self.expire_time_utc is not None:
            result['ExpireTimeUTC'] = self.expire_time_utc
        if self.master_disk_size is not None:
            result['MasterDiskSize'] = self.master_disk_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.core_node_count is not None:
            result['CoreNodeCount'] = self.core_node_count
        if self.cold_storage_status is not None:
            result['ColdStorageStatus'] = self.cold_storage_status
        if self.created_time_utc is not None:
            result['CreatedTimeUTC'] = self.created_time_utc
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.is_multi_model is not None:
            result['IsMultiModel'] = self.is_multi_model
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.master_node_count is not None:
            result['MasterNodeCount'] = self.master_node_count
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.core_disk_type is not None:
            result['CoreDiskType'] = self.core_disk_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.core_disk_size is not None:
            result['CoreDiskSize'] = self.core_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleStackVersion') is not None:
            self.module_stack_version = m.get('ModuleStackVersion')
        if m.get('IsHa') is not None:
            self.is_ha = m.get('IsHa')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('MasterInstanceType') is not None:
            self.master_instance_type = m.get('MasterInstanceType')
        if m.get('IsDeletionProtection') is not None:
            self.is_deletion_protection = m.get('IsDeletionProtection')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('IsLatestVersion') is not None:
            self.is_latest_version = m.get('IsLatestVersion')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('CoreInstanceType') is not None:
            self.core_instance_type = m.get('CoreInstanceType')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('MasterDiskType') is not None:
            self.master_disk_type = m.get('MasterDiskType')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('Tags') is not None:
            temp_model = DescribeInstanceResponseBodyTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ColdStorageSize') is not None:
            self.cold_storage_size = m.get('ColdStorageSize')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
        if m.get('CoreDiskCount') is not None:
            self.core_disk_count = m.get('CoreDiskCount')
        if m.get('ExpireTimeUTC') is not None:
            self.expire_time_utc = m.get('ExpireTimeUTC')
        if m.get('MasterDiskSize') is not None:
            self.master_disk_size = m.get('MasterDiskSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CoreNodeCount') is not None:
            self.core_node_count = m.get('CoreNodeCount')
        if m.get('ColdStorageStatus') is not None:
            self.cold_storage_status = m.get('ColdStorageStatus')
        if m.get('CreatedTimeUTC') is not None:
            self.created_time_utc = m.get('CreatedTimeUTC')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('IsMultiModel') is not None:
            self.is_multi_model = m.get('IsMultiModel')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('MasterNodeCount') is not None:
            self.master_node_count = m.get('MasterNodeCount')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('CoreDiskType') is not None:
            self.core_disk_type = m.get('CoreDiskType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('CoreDiskSize') is not None:
            self.core_disk_size = m.get('CoreDiskSize')
        return self


class DescribeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceResponseBody = None,
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
            temp_model = DescribeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeInstancesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        page_number: int = None,
        page_size: int = None,
        db_type: str = None,
        cluster_name: str = None,
        resource_group_id: str = None,
        tag: List[DescribeInstancesRequestTag] = None,
    ):
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size
        self.db_type = db_type
        self.cluster_name = cluster_name
        self.resource_group_id = resource_group_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.db_type is not None:
            result['DbType'] = self.db_type
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBodyInstancesInstanceTagsTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeInstancesResponseBodyInstancesInstanceTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeInstancesResponseBodyInstancesInstanceTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeInstancesResponseBodyInstancesInstanceTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBodyInstancesInstance(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        status: str = None,
        module_id: int = None,
        vswitch_id: str = None,
        backup_status: str = None,
        pay_type: str = None,
        core_disk_type: str = None,
        tags: DescribeInstancesResponseBodyInstancesInstanceTags = None,
        master_node_count: int = None,
        network_type: str = None,
        created_time_utc: str = None,
        parent_id: str = None,
        expire_time_utc: str = None,
        instance_name: str = None,
        master_instance_type: str = None,
        core_instance_type: str = None,
        created_time: str = None,
        core_disk_size: int = None,
        cluster_id: str = None,
        expire_time: str = None,
        is_ha: bool = None,
        instance_id: str = None,
        cold_storage_status: str = None,
        is_deletion_protection: bool = None,
        region_id: str = None,
        master_disk_size: int = None,
        master_disk_type: str = None,
        auto_renewal: bool = None,
        cluster_type: str = None,
        resource_group_id: str = None,
        cluster_name: str = None,
        zone_id: str = None,
        duration: int = None,
        module_stack_version: str = None,
        engine: str = None,
        major_version: str = None,
        core_disk_count: str = None,
        core_node_count: int = None,
    ):
        self.vpc_id = vpc_id
        self.status = status
        self.module_id = module_id
        self.vswitch_id = vswitch_id
        self.backup_status = backup_status
        self.pay_type = pay_type
        self.core_disk_type = core_disk_type
        self.tags = tags
        self.master_node_count = master_node_count
        self.network_type = network_type
        self.created_time_utc = created_time_utc
        self.parent_id = parent_id
        self.expire_time_utc = expire_time_utc
        self.instance_name = instance_name
        self.master_instance_type = master_instance_type
        self.core_instance_type = core_instance_type
        self.created_time = created_time
        self.core_disk_size = core_disk_size
        self.cluster_id = cluster_id
        self.expire_time = expire_time
        self.is_ha = is_ha
        self.instance_id = instance_id
        self.cold_storage_status = cold_storage_status
        self.is_deletion_protection = is_deletion_protection
        self.region_id = region_id
        self.master_disk_size = master_disk_size
        self.master_disk_type = master_disk_type
        self.auto_renewal = auto_renewal
        self.cluster_type = cluster_type
        self.resource_group_id = resource_group_id
        self.cluster_name = cluster_name
        self.zone_id = zone_id
        self.duration = duration
        self.module_stack_version = module_stack_version
        self.engine = engine
        self.major_version = major_version
        self.core_disk_count = core_disk_count
        self.core_node_count = core_node_count

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.status is not None:
            result['Status'] = self.status
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.backup_status is not None:
            result['BackupStatus'] = self.backup_status
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.core_disk_type is not None:
            result['CoreDiskType'] = self.core_disk_type
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.master_node_count is not None:
            result['MasterNodeCount'] = self.master_node_count
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.created_time_utc is not None:
            result['CreatedTimeUTC'] = self.created_time_utc
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.expire_time_utc is not None:
            result['ExpireTimeUTC'] = self.expire_time_utc
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.master_instance_type is not None:
            result['MasterInstanceType'] = self.master_instance_type
        if self.core_instance_type is not None:
            result['CoreInstanceType'] = self.core_instance_type
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.core_disk_size is not None:
            result['CoreDiskSize'] = self.core_disk_size
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.is_ha is not None:
            result['IsHa'] = self.is_ha
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.cold_storage_status is not None:
            result['ColdStorageStatus'] = self.cold_storage_status
        if self.is_deletion_protection is not None:
            result['IsDeletionProtection'] = self.is_deletion_protection
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.master_disk_size is not None:
            result['MasterDiskSize'] = self.master_disk_size
        if self.master_disk_type is not None:
            result['MasterDiskType'] = self.master_disk_type
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.module_stack_version is not None:
            result['ModuleStackVersion'] = self.module_stack_version
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
        if self.core_disk_count is not None:
            result['CoreDiskCount'] = self.core_disk_count
        if self.core_node_count is not None:
            result['CoreNodeCount'] = self.core_node_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('BackupStatus') is not None:
            self.backup_status = m.get('BackupStatus')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('CoreDiskType') is not None:
            self.core_disk_type = m.get('CoreDiskType')
        if m.get('Tags') is not None:
            temp_model = DescribeInstancesResponseBodyInstancesInstanceTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('MasterNodeCount') is not None:
            self.master_node_count = m.get('MasterNodeCount')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('CreatedTimeUTC') is not None:
            self.created_time_utc = m.get('CreatedTimeUTC')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('ExpireTimeUTC') is not None:
            self.expire_time_utc = m.get('ExpireTimeUTC')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('MasterInstanceType') is not None:
            self.master_instance_type = m.get('MasterInstanceType')
        if m.get('CoreInstanceType') is not None:
            self.core_instance_type = m.get('CoreInstanceType')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('CoreDiskSize') is not None:
            self.core_disk_size = m.get('CoreDiskSize')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('IsHa') is not None:
            self.is_ha = m.get('IsHa')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ColdStorageStatus') is not None:
            self.cold_storage_status = m.get('ColdStorageStatus')
        if m.get('IsDeletionProtection') is not None:
            self.is_deletion_protection = m.get('IsDeletionProtection')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('MasterDiskSize') is not None:
            self.master_disk_size = m.get('MasterDiskSize')
        if m.get('MasterDiskType') is not None:
            self.master_disk_type = m.get('MasterDiskType')
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ModuleStackVersion') is not None:
            self.module_stack_version = m.get('ModuleStackVersion')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
        if m.get('CoreDiskCount') is not None:
            self.core_disk_count = m.get('CoreDiskCount')
        if m.get('CoreNodeCount') is not None:
            self.core_node_count = m.get('CoreNodeCount')
        return self


class DescribeInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        instance: List[DescribeInstancesResponseBodyInstancesInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = DescribeInstancesResponseBodyInstancesInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: DescribeInstancesResponseBodyInstances = None,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
    ):
        self.instances = instances
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = dict()
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instances') is not None:
            temp_model = DescribeInstancesResponseBodyInstances()
            self.instances = temp_model.from_map(m['Instances'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstancesResponseBody = None,
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
            temp_model = DescribeInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceTypeRequest(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
    ):
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeInstanceTypeResponseBodyInstanceTypeSpecListInstanceTypeSpec(TeaModel):
    def __init__(
        self,
        cpu_size: int = None,
        mem_size: int = None,
        instance_type: str = None,
    ):
        self.cpu_size = cpu_size
        self.mem_size = mem_size
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cpu_size is not None:
            result['CpuSize'] = self.cpu_size
        if self.mem_size is not None:
            result['MemSize'] = self.mem_size
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuSize') is not None:
            self.cpu_size = m.get('CpuSize')
        if m.get('MemSize') is not None:
            self.mem_size = m.get('MemSize')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeInstanceTypeResponseBodyInstanceTypeSpecList(TeaModel):
    def __init__(
        self,
        instance_type_spec: List[DescribeInstanceTypeResponseBodyInstanceTypeSpecListInstanceTypeSpec] = None,
    ):
        self.instance_type_spec = instance_type_spec

    def validate(self):
        if self.instance_type_spec:
            for k in self.instance_type_spec:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['InstanceTypeSpec'] = []
        if self.instance_type_spec is not None:
            for k in self.instance_type_spec:
                result['InstanceTypeSpec'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_type_spec = []
        if m.get('InstanceTypeSpec') is not None:
            for k in m.get('InstanceTypeSpec'):
                temp_model = DescribeInstanceTypeResponseBodyInstanceTypeSpecListInstanceTypeSpec()
                self.instance_type_spec.append(temp_model.from_map(k))
        return self


class DescribeInstanceTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_type_spec_list: DescribeInstanceTypeResponseBodyInstanceTypeSpecList = None,
    ):
        self.request_id = request_id
        self.instance_type_spec_list = instance_type_spec_list

    def validate(self):
        if self.instance_type_spec_list:
            self.instance_type_spec_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_type_spec_list is not None:
            result['InstanceTypeSpecList'] = self.instance_type_spec_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceTypeSpecList') is not None:
            temp_model = DescribeInstanceTypeResponseBodyInstanceTypeSpecList()
            self.instance_type_spec_list = temp_model.from_map(m['InstanceTypeSpecList'])
        return self


class DescribeInstanceTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceTypeResponseBody = None,
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
            temp_model = DescribeInstanceTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIpWhitelistRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeIpWhitelistResponseBodyGroupsGroupIpList(TeaModel):
    def __init__(
        self,
        ip: List[str] = None,
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


class DescribeIpWhitelistResponseBodyGroupsGroup(TeaModel):
    def __init__(
        self,
        ip_version: int = None,
        group_name: str = None,
        ip_list: DescribeIpWhitelistResponseBodyGroupsGroupIpList = None,
    ):
        self.ip_version = ip_version
        self.group_name = group_name
        self.ip_list = ip_list

    def validate(self):
        if self.ip_list:
            self.ip_list.validate()

    def to_map(self):
        result = dict()
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.ip_list is not None:
            result['IpList'] = self.ip_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('IpList') is not None:
            temp_model = DescribeIpWhitelistResponseBodyGroupsGroupIpList()
            self.ip_list = temp_model.from_map(m['IpList'])
        return self


class DescribeIpWhitelistResponseBodyGroups(TeaModel):
    def __init__(
        self,
        group: List[DescribeIpWhitelistResponseBodyGroupsGroup] = None,
    ):
        self.group = group

    def validate(self):
        if self.group:
            for k in self.group:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Group'] = []
        if self.group is not None:
            for k in self.group:
                result['Group'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.group = []
        if m.get('Group') is not None:
            for k in m.get('Group'):
                temp_model = DescribeIpWhitelistResponseBodyGroupsGroup()
                self.group.append(temp_model.from_map(k))
        return self


class DescribeIpWhitelistResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        groups: DescribeIpWhitelistResponseBodyGroups = None,
    ):
        self.request_id = request_id
        self.groups = groups

    def validate(self):
        if self.groups:
            self.groups.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.groups is not None:
            result['Groups'] = self.groups.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Groups') is not None:
            temp_model = DescribeIpWhitelistResponseBodyGroups()
            self.groups = temp_model.from_map(m['Groups'])
        return self


class DescribeIpWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeIpWhitelistResponseBody = None,
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
            temp_model = DescribeIpWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMultiZoneAvailableRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombinesAvailableCombineZones(TeaModel):
    def __init__(
        self,
        zone: List[str] = None,
    ):
        self.zone = zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.zone is not None:
            result['Zone'] = self.zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Zone') is not None:
            self.zone = m.get('Zone')
        return self


class DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombinesAvailableCombine(TeaModel):
    def __init__(
        self,
        zones: DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombinesAvailableCombineZones = None,
        id: str = None,
    ):
        self.zones = zones
        self.id = id

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        result = dict()
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Zones') is not None:
            temp_model = DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombinesAvailableCombineZones()
            self.zones = temp_model.from_map(m['Zones'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombines(TeaModel):
    def __init__(
        self,
        available_combine: List[DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombinesAvailableCombine] = None,
    ):
        self.available_combine = available_combine

    def validate(self):
        if self.available_combine:
            for k in self.available_combine:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AvailableCombine'] = []
        if self.available_combine is not None:
            for k in self.available_combine:
                result['AvailableCombine'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_combine = []
        if m.get('AvailableCombine') is not None:
            for k in m.get('AvailableCombine'):
                temp_model = DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombinesAvailableCombine()
                self.available_combine.append(temp_model.from_map(k))
        return self


class DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        available_combines: DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombines = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_endpoint = region_endpoint
        self.available_combines = available_combines
        self.region_id = region_id

    def validate(self):
        if self.available_combines:
            self.available_combines.validate()

    def to_map(self):
        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.available_combines is not None:
            result['AvailableCombines'] = self.available_combines.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('AvailableCombines') is not None:
            temp_model = DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombines()
            self.available_combines = temp_model.from_map(m['AvailableCombines'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeMultiZoneAvailableRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        region: List[DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeMultiZoneAvailableRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        regions: DescribeMultiZoneAvailableRegionsResponseBodyRegions = None,
    ):
        self.request_id = request_id
        self.regions = regions

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Regions') is not None:
            temp_model = DescribeMultiZoneAvailableRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        return self


class DescribeMultiZoneAvailableRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMultiZoneAvailableRegionsResponseBody = None,
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
            temp_model = DescribeMultiZoneAvailableRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMultiZoneAvailableResourceRequest(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        region_id: str = None,
        zone_combination: str = None,
    ):
        self.charge_type = charge_type
        self.region_id = region_id
        self.zone_combination = zone_combination

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_combination is not None:
            result['ZoneCombination'] = self.zone_combination
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneCombination') is not None:
            self.zone_combination = m.get('ZoneCombination')
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceInstanceTypeDetail(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        mem: int = None,
    ):
        self.cpu = cpu
        self.mem = mem

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.mem is not None:
            result['Mem'] = self.mem
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Mem') is not None:
            self.mem = m.get('Mem')
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceDBInstanceStorageRange(TeaModel):
    def __init__(
        self,
        max_size: int = None,
        step_size: int = None,
        min_size: int = None,
    ):
        self.max_size = max_size
        self.step_size = step_size
        self.min_size = min_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.max_size is not None:
            result['MaxSize'] = self.max_size
        if self.step_size is not None:
            result['StepSize'] = self.step_size
        if self.min_size is not None:
            result['MinSize'] = self.min_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxSize') is not None:
            self.max_size = m.get('MaxSize')
        if m.get('StepSize') is not None:
            self.step_size = m.get('StepSize')
        if m.get('MinSize') is not None:
            self.min_size = m.get('MinSize')
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResource(TeaModel):
    def __init__(
        self,
        instance_type_detail: DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceInstanceTypeDetail = None,
        dbinstance_storage_range: DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceDBInstanceStorageRange = None,
        max_core_count: int = None,
        instance_type: str = None,
    ):
        self.instance_type_detail = instance_type_detail
        self.dbinstance_storage_range = dbinstance_storage_range
        self.max_core_count = max_core_count
        self.instance_type = instance_type

    def validate(self):
        if self.instance_type_detail:
            self.instance_type_detail.validate()
        if self.dbinstance_storage_range:
            self.dbinstance_storage_range.validate()

    def to_map(self):
        result = dict()
        if self.instance_type_detail is not None:
            result['InstanceTypeDetail'] = self.instance_type_detail.to_map()
        if self.dbinstance_storage_range is not None:
            result['DBInstanceStorageRange'] = self.dbinstance_storage_range.to_map()
        if self.max_core_count is not None:
            result['MaxCoreCount'] = self.max_core_count
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceTypeDetail') is not None:
            temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceInstanceTypeDetail()
            self.instance_type_detail = temp_model.from_map(m['InstanceTypeDetail'])
        if m.get('DBInstanceStorageRange') is not None:
            temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceDBInstanceStorageRange()
            self.dbinstance_storage_range = temp_model.from_map(m['DBInstanceStorageRange'])
        if m.get('MaxCoreCount') is not None:
            self.max_core_count = m.get('MaxCoreCount')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResources(TeaModel):
    def __init__(
        self,
        core_resource: List[DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResource] = None,
    ):
        self.core_resource = core_resource

    def validate(self):
        if self.core_resource:
            for k in self.core_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['CoreResource'] = []
        if self.core_resource is not None:
            for k in self.core_resource:
                result['CoreResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.core_resource = []
        if m.get('CoreResource') is not None:
            for k in m.get('CoreResource'):
                temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResource()
                self.core_resource.append(temp_model.from_map(k))
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageType(TeaModel):
    def __init__(
        self,
        core_resources: DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResources = None,
        storage_type: str = None,
    ):
        self.core_resources = core_resources
        self.storage_type = storage_type

    def validate(self):
        if self.core_resources:
            self.core_resources.validate()

    def to_map(self):
        result = dict()
        if self.core_resources is not None:
            result['CoreResources'] = self.core_resources.to_map()
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoreResources') is not None:
            temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResources()
            self.core_resources = temp_model.from_map(m['CoreResources'])
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypes(TeaModel):
    def __init__(
        self,
        supported_storage_type: List[DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageType] = None,
    ):
        self.supported_storage_type = supported_storage_type

    def validate(self):
        if self.supported_storage_type:
            for k in self.supported_storage_type:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SupportedStorageType'] = []
        if self.supported_storage_type is not None:
            for k in self.supported_storage_type:
                result['SupportedStorageType'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_storage_type = []
        if m.get('SupportedStorageType') is not None:
            for k in m.get('SupportedStorageType'):
                temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageType()
                self.supported_storage_type.append(temp_model.from_map(k))
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategories(TeaModel):
    def __init__(
        self,
        supported_storage_types: DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypes = None,
        category: str = None,
    ):
        self.supported_storage_types = supported_storage_types
        self.category = category

    def validate(self):
        if self.supported_storage_types:
            self.supported_storage_types.validate()

    def to_map(self):
        result = dict()
        if self.supported_storage_types is not None:
            result['SupportedStorageTypes'] = self.supported_storage_types.to_map()
        if self.category is not None:
            result['Category'] = self.category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedStorageTypes') is not None:
            temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypes()
            self.supported_storage_types = temp_model.from_map(m['SupportedStorageTypes'])
        if m.get('Category') is not None:
            self.category = m.get('Category')
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategories(TeaModel):
    def __init__(
        self,
        supported_categories: List[DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategories] = None,
    ):
        self.supported_categories = supported_categories

    def validate(self):
        if self.supported_categories:
            for k in self.supported_categories:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SupportedCategories'] = []
        if self.supported_categories is not None:
            for k in self.supported_categories:
                result['SupportedCategories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_categories = []
        if m.get('SupportedCategories') is not None:
            for k in m.get('SupportedCategories'):
                temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategories()
                self.supported_categories.append(temp_model.from_map(k))
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersion(TeaModel):
    def __init__(
        self,
        version: str = None,
        supported_categories: DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategories = None,
    ):
        self.version = version
        self.supported_categories = supported_categories

    def validate(self):
        if self.supported_categories:
            self.supported_categories.validate()

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.supported_categories is not None:
            result['SupportedCategories'] = self.supported_categories.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('SupportedCategories') is not None:
            temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategories()
            self.supported_categories = temp_model.from_map(m['SupportedCategories'])
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersions(TeaModel):
    def __init__(
        self,
        supported_engine_version: List[DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersion] = None,
    ):
        self.supported_engine_version = supported_engine_version

    def validate(self):
        if self.supported_engine_version:
            for k in self.supported_engine_version:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SupportedEngineVersion'] = []
        if self.supported_engine_version is not None:
            for k in self.supported_engine_version:
                result['SupportedEngineVersion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_engine_version = []
        if m.get('SupportedEngineVersion') is not None:
            for k in m.get('SupportedEngineVersion'):
                temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersion()
                self.supported_engine_version.append(temp_model.from_map(k))
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngine(TeaModel):
    def __init__(
        self,
        supported_engine_versions: DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersions = None,
        engine: str = None,
    ):
        self.supported_engine_versions = supported_engine_versions
        self.engine = engine

    def validate(self):
        if self.supported_engine_versions:
            self.supported_engine_versions.validate()

    def to_map(self):
        result = dict()
        if self.supported_engine_versions is not None:
            result['SupportedEngineVersions'] = self.supported_engine_versions.to_map()
        if self.engine is not None:
            result['Engine'] = self.engine
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedEngineVersions') is not None:
            temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersions()
            self.supported_engine_versions = temp_model.from_map(m['SupportedEngineVersions'])
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEngines(TeaModel):
    def __init__(
        self,
        supported_engine: List[DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngine] = None,
    ):
        self.supported_engine = supported_engine

    def validate(self):
        if self.supported_engine:
            for k in self.supported_engine:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SupportedEngine'] = []
        if self.supported_engine is not None:
            for k in self.supported_engine:
                result['SupportedEngine'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_engine = []
        if m.get('SupportedEngine') is not None:
            for k in m.get('SupportedEngine'):
                temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngine()
                self.supported_engine.append(temp_model.from_map(k))
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResourceInstanceTypeDetail(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        mem: int = None,
    ):
        self.cpu = cpu
        self.mem = mem

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.mem is not None:
            result['Mem'] = self.mem
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Mem') is not None:
            self.mem = m.get('Mem')
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResource(TeaModel):
    def __init__(
        self,
        instance_type_detail: DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResourceInstanceTypeDetail = None,
        instance_type: str = None,
    ):
        self.instance_type_detail = instance_type_detail
        self.instance_type = instance_type

    def validate(self):
        if self.instance_type_detail:
            self.instance_type_detail.validate()

    def to_map(self):
        result = dict()
        if self.instance_type_detail is not None:
            result['InstanceTypeDetail'] = self.instance_type_detail.to_map()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceTypeDetail') is not None:
            temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResourceInstanceTypeDetail()
            self.instance_type_detail = temp_model.from_map(m['InstanceTypeDetail'])
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResources(TeaModel):
    def __init__(
        self,
        master_resource: List[DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResource] = None,
    ):
        self.master_resource = master_resource

    def validate(self):
        if self.master_resource:
            for k in self.master_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['MasterResource'] = []
        if self.master_resource is not None:
            for k in self.master_resource:
                result['MasterResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.master_resource = []
        if m.get('MasterResource') is not None:
            for k in m.get('MasterResource'):
                temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResource()
                self.master_resource.append(temp_model.from_map(k))
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZone(TeaModel):
    def __init__(
        self,
        supported_engines: DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEngines = None,
        zone_combination: str = None,
        master_resources: DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResources = None,
        region_id: str = None,
    ):
        self.supported_engines = supported_engines
        self.zone_combination = zone_combination
        self.master_resources = master_resources
        self.region_id = region_id

    def validate(self):
        if self.supported_engines:
            self.supported_engines.validate()
        if self.master_resources:
            self.master_resources.validate()

    def to_map(self):
        result = dict()
        if self.supported_engines is not None:
            result['SupportedEngines'] = self.supported_engines.to_map()
        if self.zone_combination is not None:
            result['ZoneCombination'] = self.zone_combination
        if self.master_resources is not None:
            result['MasterResources'] = self.master_resources.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedEngines') is not None:
            temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEngines()
            self.supported_engines = temp_model.from_map(m['SupportedEngines'])
        if m.get('ZoneCombination') is not None:
            self.zone_combination = m.get('ZoneCombination')
        if m.get('MasterResources') is not None:
            temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResources()
            self.master_resources = temp_model.from_map(m['MasterResources'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeMultiZoneAvailableResourceResponseBodyAvailableZones(TeaModel):
    def __init__(
        self,
        available_zone: List[DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZone] = None,
    ):
        self.available_zone = available_zone

    def validate(self):
        if self.available_zone:
            for k in self.available_zone:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AvailableZone'] = []
        if self.available_zone is not None:
            for k in self.available_zone:
                result['AvailableZone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_zone = []
        if m.get('AvailableZone') is not None:
            for k in m.get('AvailableZone'):
                temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZonesAvailableZone()
                self.available_zone.append(temp_model.from_map(k))
        return self


class DescribeMultiZoneAvailableResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        available_zones: DescribeMultiZoneAvailableResourceResponseBodyAvailableZones = None,
    ):
        self.request_id = request_id
        self.available_zones = available_zones

    def validate(self):
        if self.available_zones:
            self.available_zones.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.available_zones is not None:
            result['AvailableZones'] = self.available_zones.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AvailableZones') is not None:
            temp_model = DescribeMultiZoneAvailableResourceResponseBodyAvailableZones()
            self.available_zones = temp_model.from_map(m['AvailableZones'])
        return self


class DescribeMultiZoneAvailableResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMultiZoneAvailableResourceResponseBody = None,
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
            temp_model = DescribeMultiZoneAvailableResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMultiZoneClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeMultiZoneClusterResponseBodyTagsTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeMultiZoneClusterResponseBodyTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeMultiZoneClusterResponseBodyTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeMultiZoneClusterResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeMultiZoneClusterResponseBodyMultiZoneInstanceModelsMultiZoneInstanceModel(TeaModel):
    def __init__(
        self,
        status: str = None,
        is_latest_version: bool = None,
        ins_name: str = None,
        role: str = None,
        minor_version: str = None,
    ):
        self.status = status
        self.is_latest_version = is_latest_version
        self.ins_name = ins_name
        self.role = role
        self.minor_version = minor_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.is_latest_version is not None:
            result['IsLatestVersion'] = self.is_latest_version
        if self.ins_name is not None:
            result['InsName'] = self.ins_name
        if self.role is not None:
            result['Role'] = self.role
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('IsLatestVersion') is not None:
            self.is_latest_version = m.get('IsLatestVersion')
        if m.get('InsName') is not None:
            self.ins_name = m.get('InsName')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        return self


class DescribeMultiZoneClusterResponseBodyMultiZoneInstanceModels(TeaModel):
    def __init__(
        self,
        multi_zone_instance_model: List[DescribeMultiZoneClusterResponseBodyMultiZoneInstanceModelsMultiZoneInstanceModel] = None,
    ):
        self.multi_zone_instance_model = multi_zone_instance_model

    def validate(self):
        if self.multi_zone_instance_model:
            for k in self.multi_zone_instance_model:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['MultiZoneInstanceModel'] = []
        if self.multi_zone_instance_model is not None:
            for k in self.multi_zone_instance_model:
                result['MultiZoneInstanceModel'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.multi_zone_instance_model = []
        if m.get('MultiZoneInstanceModel') is not None:
            for k in m.get('MultiZoneInstanceModel'):
                temp_model = DescribeMultiZoneClusterResponseBodyMultiZoneInstanceModelsMultiZoneInstanceModel()
                self.multi_zone_instance_model.append(temp_model.from_map(k))
        return self


class DescribeMultiZoneClusterResponseBody(TeaModel):
    def __init__(
        self,
        standby_zone_id: str = None,
        module_stack_version: str = None,
        created_time: str = None,
        resource_group_id: str = None,
        primary_vswitch_ids: str = None,
        master_instance_type: str = None,
        log_disk_count: str = None,
        is_deletion_protection: bool = None,
        log_disk_size: int = None,
        module_id: int = None,
        arbiter_vswitch_ids: str = None,
        maintain_end_time: str = None,
        standby_vswitch_ids: str = None,
        network_type: str = None,
        core_instance_type: str = None,
        cluster_name: str = None,
        master_disk_type: str = None,
        maintain_start_time: str = None,
        engine: str = None,
        tags: DescribeMultiZoneClusterResponseBodyTags = None,
        arbiter_zone_id: str = None,
        status: str = None,
        parent_id: str = None,
        major_version: str = None,
        core_disk_count: str = None,
        multi_zone_instance_models: DescribeMultiZoneClusterResponseBodyMultiZoneInstanceModels = None,
        expire_time_utc: str = None,
        primary_zone_id: str = None,
        master_disk_size: int = None,
        request_id: str = None,
        multi_zone_combination: str = None,
        cluster_id: str = None,
        instance_id: str = None,
        core_node_count: int = None,
        created_time_utc: str = None,
        log_instance_type: str = None,
        duration: int = None,
        pay_type: str = None,
        master_node_count: int = None,
        instance_name: str = None,
        vpc_id: str = None,
        auto_renewal: bool = None,
        core_disk_type: str = None,
        log_node_count: int = None,
        log_disk_type: str = None,
        region_id: str = None,
        expire_time: str = None,
        core_disk_size: int = None,
    ):
        self.standby_zone_id = standby_zone_id
        self.module_stack_version = module_stack_version
        self.created_time = created_time
        self.resource_group_id = resource_group_id
        self.primary_vswitch_ids = primary_vswitch_ids
        self.master_instance_type = master_instance_type
        self.log_disk_count = log_disk_count
        self.is_deletion_protection = is_deletion_protection
        self.log_disk_size = log_disk_size
        self.module_id = module_id
        self.arbiter_vswitch_ids = arbiter_vswitch_ids
        self.maintain_end_time = maintain_end_time
        self.standby_vswitch_ids = standby_vswitch_ids
        self.network_type = network_type
        self.core_instance_type = core_instance_type
        self.cluster_name = cluster_name
        self.master_disk_type = master_disk_type
        self.maintain_start_time = maintain_start_time
        self.engine = engine
        self.tags = tags
        self.arbiter_zone_id = arbiter_zone_id
        self.status = status
        self.parent_id = parent_id
        self.major_version = major_version
        self.core_disk_count = core_disk_count
        self.multi_zone_instance_models = multi_zone_instance_models
        self.expire_time_utc = expire_time_utc
        self.primary_zone_id = primary_zone_id
        self.master_disk_size = master_disk_size
        self.request_id = request_id
        self.multi_zone_combination = multi_zone_combination
        self.cluster_id = cluster_id
        self.instance_id = instance_id
        self.core_node_count = core_node_count
        self.created_time_utc = created_time_utc
        self.log_instance_type = log_instance_type
        self.duration = duration
        self.pay_type = pay_type
        self.master_node_count = master_node_count
        self.instance_name = instance_name
        self.vpc_id = vpc_id
        self.auto_renewal = auto_renewal
        self.core_disk_type = core_disk_type
        self.log_node_count = log_node_count
        self.log_disk_type = log_disk_type
        self.region_id = region_id
        self.expire_time = expire_time
        self.core_disk_size = core_disk_size

    def validate(self):
        if self.tags:
            self.tags.validate()
        if self.multi_zone_instance_models:
            self.multi_zone_instance_models.validate()

    def to_map(self):
        result = dict()
        if self.standby_zone_id is not None:
            result['StandbyZoneId'] = self.standby_zone_id
        if self.module_stack_version is not None:
            result['ModuleStackVersion'] = self.module_stack_version
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.primary_vswitch_ids is not None:
            result['PrimaryVSwitchIds'] = self.primary_vswitch_ids
        if self.master_instance_type is not None:
            result['MasterInstanceType'] = self.master_instance_type
        if self.log_disk_count is not None:
            result['LogDiskCount'] = self.log_disk_count
        if self.is_deletion_protection is not None:
            result['IsDeletionProtection'] = self.is_deletion_protection
        if self.log_disk_size is not None:
            result['LogDiskSize'] = self.log_disk_size
        if self.module_id is not None:
            result['ModuleId'] = self.module_id
        if self.arbiter_vswitch_ids is not None:
            result['ArbiterVSwitchIds'] = self.arbiter_vswitch_ids
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.standby_vswitch_ids is not None:
            result['StandbyVSwitchIds'] = self.standby_vswitch_ids
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.core_instance_type is not None:
            result['CoreInstanceType'] = self.core_instance_type
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.master_disk_type is not None:
            result['MasterDiskType'] = self.master_disk_type
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.arbiter_zone_id is not None:
            result['ArbiterZoneId'] = self.arbiter_zone_id
        if self.status is not None:
            result['Status'] = self.status
        if self.parent_id is not None:
            result['ParentId'] = self.parent_id
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
        if self.core_disk_count is not None:
            result['CoreDiskCount'] = self.core_disk_count
        if self.multi_zone_instance_models is not None:
            result['MultiZoneInstanceModels'] = self.multi_zone_instance_models.to_map()
        if self.expire_time_utc is not None:
            result['ExpireTimeUTC'] = self.expire_time_utc
        if self.primary_zone_id is not None:
            result['PrimaryZoneId'] = self.primary_zone_id
        if self.master_disk_size is not None:
            result['MasterDiskSize'] = self.master_disk_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.multi_zone_combination is not None:
            result['MultiZoneCombination'] = self.multi_zone_combination
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.core_node_count is not None:
            result['CoreNodeCount'] = self.core_node_count
        if self.created_time_utc is not None:
            result['CreatedTimeUTC'] = self.created_time_utc
        if self.log_instance_type is not None:
            result['LogInstanceType'] = self.log_instance_type
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.master_node_count is not None:
            result['MasterNodeCount'] = self.master_node_count
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.core_disk_type is not None:
            result['CoreDiskType'] = self.core_disk_type
        if self.log_node_count is not None:
            result['LogNodeCount'] = self.log_node_count
        if self.log_disk_type is not None:
            result['LogDiskType'] = self.log_disk_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.core_disk_size is not None:
            result['CoreDiskSize'] = self.core_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StandbyZoneId') is not None:
            self.standby_zone_id = m.get('StandbyZoneId')
        if m.get('ModuleStackVersion') is not None:
            self.module_stack_version = m.get('ModuleStackVersion')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('PrimaryVSwitchIds') is not None:
            self.primary_vswitch_ids = m.get('PrimaryVSwitchIds')
        if m.get('MasterInstanceType') is not None:
            self.master_instance_type = m.get('MasterInstanceType')
        if m.get('LogDiskCount') is not None:
            self.log_disk_count = m.get('LogDiskCount')
        if m.get('IsDeletionProtection') is not None:
            self.is_deletion_protection = m.get('IsDeletionProtection')
        if m.get('LogDiskSize') is not None:
            self.log_disk_size = m.get('LogDiskSize')
        if m.get('ModuleId') is not None:
            self.module_id = m.get('ModuleId')
        if m.get('ArbiterVSwitchIds') is not None:
            self.arbiter_vswitch_ids = m.get('ArbiterVSwitchIds')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('StandbyVSwitchIds') is not None:
            self.standby_vswitch_ids = m.get('StandbyVSwitchIds')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('CoreInstanceType') is not None:
            self.core_instance_type = m.get('CoreInstanceType')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('MasterDiskType') is not None:
            self.master_disk_type = m.get('MasterDiskType')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('Tags') is not None:
            temp_model = DescribeMultiZoneClusterResponseBodyTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('ArbiterZoneId') is not None:
            self.arbiter_zone_id = m.get('ArbiterZoneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
        if m.get('CoreDiskCount') is not None:
            self.core_disk_count = m.get('CoreDiskCount')
        if m.get('MultiZoneInstanceModels') is not None:
            temp_model = DescribeMultiZoneClusterResponseBodyMultiZoneInstanceModels()
            self.multi_zone_instance_models = temp_model.from_map(m['MultiZoneInstanceModels'])
        if m.get('ExpireTimeUTC') is not None:
            self.expire_time_utc = m.get('ExpireTimeUTC')
        if m.get('PrimaryZoneId') is not None:
            self.primary_zone_id = m.get('PrimaryZoneId')
        if m.get('MasterDiskSize') is not None:
            self.master_disk_size = m.get('MasterDiskSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MultiZoneCombination') is not None:
            self.multi_zone_combination = m.get('MultiZoneCombination')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CoreNodeCount') is not None:
            self.core_node_count = m.get('CoreNodeCount')
        if m.get('CreatedTimeUTC') is not None:
            self.created_time_utc = m.get('CreatedTimeUTC')
        if m.get('LogInstanceType') is not None:
            self.log_instance_type = m.get('LogInstanceType')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('MasterNodeCount') is not None:
            self.master_node_count = m.get('MasterNodeCount')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('CoreDiskType') is not None:
            self.core_disk_type = m.get('CoreDiskType')
        if m.get('LogNodeCount') is not None:
            self.log_node_count = m.get('LogNodeCount')
        if m.get('LogDiskType') is not None:
            self.log_disk_type = m.get('LogDiskType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('CoreDiskSize') is not None:
            self.core_disk_size = m.get('CoreDiskSize')
        return self


class DescribeMultiZoneClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeMultiZoneClusterResponseBody = None,
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
            temp_model = DescribeMultiZoneClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRecoverableTimeRangeRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeRecoverableTimeRangeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        time_end: str = None,
        time_begin: str = None,
    ):
        self.request_id = request_id
        self.time_end = time_end
        self.time_begin = time_begin

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.time_end is not None:
            result['TimeEnd'] = self.time_end
        if self.time_begin is not None:
            result['TimeBegin'] = self.time_begin
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TimeEnd') is not None:
            self.time_end = m.get('TimeEnd')
        if m.get('TimeBegin') is not None:
            self.time_begin = m.get('TimeBegin')
        return self


class DescribeRecoverableTimeRangeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRecoverableTimeRangeResponseBody = None,
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
            temp_model = DescribeRecoverableTimeRangeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeRegionsResponseBodyRegionsRegionZonesZone(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeRegionsResponseBodyRegionsRegionZones(TeaModel):
    def __init__(
        self,
        zone: List[DescribeRegionsResponseBodyRegionsRegionZonesZone] = None,
    ):
        self.zone = zone

    def validate(self):
        if self.zone:
            for k in self.zone:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Zone'] = []
        if self.zone is not None:
            for k in self.zone:
                result['Zone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone = []
        if m.get('Zone') is not None:
            for k in m.get('Zone'):
                temp_model = DescribeRegionsResponseBodyRegionsRegionZonesZone()
                self.zone.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(
        self,
        zones: DescribeRegionsResponseBodyRegionsRegionZones = None,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        self.zones = zones
        self.local_name = local_name
        self.region_endpoint = region_endpoint
        self.region_id = region_id

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        result = dict()
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Zones') is not None:
            temp_model = DescribeRegionsResponseBodyRegionsRegionZones()
            self.zones = temp_model.from_map(m['Zones'])
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
        request_id: str = None,
        regions: DescribeRegionsResponseBodyRegions = None,
    ):
        self.request_id = request_id
        self.regions = regions

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRegionsResponseBody = None,
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRestoreFullDetailsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        restore_record_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.cluster_id = cluster_id
        self.restore_record_id = restore_record_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.restore_record_id is not None:
            result['RestoreRecordId'] = self.restore_record_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RestoreRecordId') is not None:
            self.restore_record_id = m.get('RestoreRecordId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeRestoreFullDetailsResponseBodyRestoreFullRestoreFullDetailsRestoreFullDetail(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        process: str = None,
        data_size: str = None,
        speed: str = None,
        state: str = None,
        message: str = None,
        table: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.process = process
        self.data_size = data_size
        self.speed = speed
        self.state = state
        self.message = message
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.process is not None:
            result['Process'] = self.process
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.state is not None:
            result['State'] = self.state
        if self.message is not None:
            result['Message'] = self.message
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class DescribeRestoreFullDetailsResponseBodyRestoreFullRestoreFullDetails(TeaModel):
    def __init__(
        self,
        restore_full_detail: List[DescribeRestoreFullDetailsResponseBodyRestoreFullRestoreFullDetailsRestoreFullDetail] = None,
    ):
        self.restore_full_detail = restore_full_detail

    def validate(self):
        if self.restore_full_detail:
            for k in self.restore_full_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['RestoreFullDetail'] = []
        if self.restore_full_detail is not None:
            for k in self.restore_full_detail:
                result['RestoreFullDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.restore_full_detail = []
        if m.get('RestoreFullDetail') is not None:
            for k in m.get('RestoreFullDetail'):
                temp_model = DescribeRestoreFullDetailsResponseBodyRestoreFullRestoreFullDetailsRestoreFullDetail()
                self.restore_full_detail.append(temp_model.from_map(k))
        return self


class DescribeRestoreFullDetailsResponseBodyRestoreFull(TeaModel):
    def __init__(
        self,
        succeed: int = None,
        data_size: str = None,
        speed: str = None,
        restore_full_details: DescribeRestoreFullDetailsResponseBodyRestoreFullRestoreFullDetails = None,
        page_size: int = None,
        fail: int = None,
        page_number: int = None,
        total: int = None,
    ):
        self.succeed = succeed
        self.data_size = data_size
        self.speed = speed
        self.restore_full_details = restore_full_details
        self.page_size = page_size
        self.fail = fail
        self.page_number = page_number
        self.total = total

    def validate(self):
        if self.restore_full_details:
            self.restore_full_details.validate()

    def to_map(self):
        result = dict()
        if self.succeed is not None:
            result['Succeed'] = self.succeed
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.restore_full_details is not None:
            result['RestoreFullDetails'] = self.restore_full_details.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.fail is not None:
            result['Fail'] = self.fail
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Succeed') is not None:
            self.succeed = m.get('Succeed')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('RestoreFullDetails') is not None:
            temp_model = DescribeRestoreFullDetailsResponseBodyRestoreFullRestoreFullDetails()
            self.restore_full_details = temp_model.from_map(m['RestoreFullDetails'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Fail') is not None:
            self.fail = m.get('Fail')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeRestoreFullDetailsResponseBody(TeaModel):
    def __init__(
        self,
        restore_full: DescribeRestoreFullDetailsResponseBodyRestoreFull = None,
        request_id: str = None,
    ):
        self.restore_full = restore_full
        self.request_id = request_id

    def validate(self):
        if self.restore_full:
            self.restore_full.validate()

    def to_map(self):
        result = dict()
        if self.restore_full is not None:
            result['RestoreFull'] = self.restore_full.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RestoreFull') is not None:
            temp_model = DescribeRestoreFullDetailsResponseBodyRestoreFull()
            self.restore_full = temp_model.from_map(m['RestoreFull'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRestoreFullDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRestoreFullDetailsResponseBody = None,
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
            temp_model = DescribeRestoreFullDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRestoreIncrDetailRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        restore_record_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.restore_record_id = restore_record_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.restore_record_id is not None:
            result['RestoreRecordId'] = self.restore_record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RestoreRecordId') is not None:
            self.restore_record_id = m.get('RestoreRecordId')
        return self


class DescribeRestoreIncrDetailResponseBodyRestoreIncrDetail(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        process: str = None,
        restore_start_ts: str = None,
        state: str = None,
        restored_ts: str = None,
        restore_delay: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.process = process
        self.restore_start_ts = restore_start_ts
        self.state = state
        self.restored_ts = restored_ts
        self.restore_delay = restore_delay

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.process is not None:
            result['Process'] = self.process
        if self.restore_start_ts is not None:
            result['RestoreStartTs'] = self.restore_start_ts
        if self.state is not None:
            result['State'] = self.state
        if self.restored_ts is not None:
            result['RestoredTs'] = self.restored_ts
        if self.restore_delay is not None:
            result['RestoreDelay'] = self.restore_delay
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('RestoreStartTs') is not None:
            self.restore_start_ts = m.get('RestoreStartTs')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('RestoredTs') is not None:
            self.restored_ts = m.get('RestoredTs')
        if m.get('RestoreDelay') is not None:
            self.restore_delay = m.get('RestoreDelay')
        return self


class DescribeRestoreIncrDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        restore_incr_detail: DescribeRestoreIncrDetailResponseBodyRestoreIncrDetail = None,
    ):
        self.request_id = request_id
        self.restore_incr_detail = restore_incr_detail

    def validate(self):
        if self.restore_incr_detail:
            self.restore_incr_detail.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.restore_incr_detail is not None:
            result['RestoreIncrDetail'] = self.restore_incr_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RestoreIncrDetail') is not None:
            temp_model = DescribeRestoreIncrDetailResponseBodyRestoreIncrDetail()
            self.restore_incr_detail = temp_model.from_map(m['RestoreIncrDetail'])
        return self


class DescribeRestoreIncrDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRestoreIncrDetailResponseBody = None,
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
            temp_model = DescribeRestoreIncrDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRestoreSchemaDetailsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        restore_record_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.cluster_id = cluster_id
        self.restore_record_id = restore_record_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.restore_record_id is not None:
            result['RestoreRecordId'] = self.restore_record_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RestoreRecordId') is not None:
            self.restore_record_id = m.get('RestoreRecordId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeRestoreSchemaDetailsResponseBodyRestoreSchemaRestoreSchemaDetailsRestoreSchemaDetail(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        state: str = None,
        message: str = None,
        table: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.state = state
        self.message = message
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.message is not None:
            result['Message'] = self.message
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class DescribeRestoreSchemaDetailsResponseBodyRestoreSchemaRestoreSchemaDetails(TeaModel):
    def __init__(
        self,
        restore_schema_detail: List[DescribeRestoreSchemaDetailsResponseBodyRestoreSchemaRestoreSchemaDetailsRestoreSchemaDetail] = None,
    ):
        self.restore_schema_detail = restore_schema_detail

    def validate(self):
        if self.restore_schema_detail:
            for k in self.restore_schema_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['RestoreSchemaDetail'] = []
        if self.restore_schema_detail is not None:
            for k in self.restore_schema_detail:
                result['RestoreSchemaDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.restore_schema_detail = []
        if m.get('RestoreSchemaDetail') is not None:
            for k in m.get('RestoreSchemaDetail'):
                temp_model = DescribeRestoreSchemaDetailsResponseBodyRestoreSchemaRestoreSchemaDetailsRestoreSchemaDetail()
                self.restore_schema_detail.append(temp_model.from_map(k))
        return self


class DescribeRestoreSchemaDetailsResponseBodyRestoreSchema(TeaModel):
    def __init__(
        self,
        succeed: int = None,
        restore_schema_details: DescribeRestoreSchemaDetailsResponseBodyRestoreSchemaRestoreSchemaDetails = None,
        page_size: int = None,
        page_number: int = None,
        fail: int = None,
        total: int = None,
    ):
        self.succeed = succeed
        self.restore_schema_details = restore_schema_details
        self.page_size = page_size
        self.page_number = page_number
        self.fail = fail
        self.total = total

    def validate(self):
        if self.restore_schema_details:
            self.restore_schema_details.validate()

    def to_map(self):
        result = dict()
        if self.succeed is not None:
            result['Succeed'] = self.succeed
        if self.restore_schema_details is not None:
            result['RestoreSchemaDetails'] = self.restore_schema_details.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.fail is not None:
            result['Fail'] = self.fail
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Succeed') is not None:
            self.succeed = m.get('Succeed')
        if m.get('RestoreSchemaDetails') is not None:
            temp_model = DescribeRestoreSchemaDetailsResponseBodyRestoreSchemaRestoreSchemaDetails()
            self.restore_schema_details = temp_model.from_map(m['RestoreSchemaDetails'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Fail') is not None:
            self.fail = m.get('Fail')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeRestoreSchemaDetailsResponseBody(TeaModel):
    def __init__(
        self,
        restore_schema: DescribeRestoreSchemaDetailsResponseBodyRestoreSchema = None,
        request_id: str = None,
    ):
        self.restore_schema = restore_schema
        self.request_id = request_id

    def validate(self):
        if self.restore_schema:
            self.restore_schema.validate()

    def to_map(self):
        result = dict()
        if self.restore_schema is not None:
            result['RestoreSchema'] = self.restore_schema.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RestoreSchema') is not None:
            temp_model = DescribeRestoreSchemaDetailsResponseBodyRestoreSchema()
            self.restore_schema = temp_model.from_map(m['RestoreSchema'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRestoreSchemaDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRestoreSchemaDetailsResponseBody = None,
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
            temp_model = DescribeRestoreSchemaDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRestoreSummaryRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.cluster_id = cluster_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeRestoreSummaryResponseBodyRescordsRescord(TeaModel):
    def __init__(
        self,
        status: str = None,
        finish_time: str = None,
        schema_process: str = None,
        bulk_load_process: str = None,
        record_id: str = None,
        create_time: str = None,
        log_process: str = None,
        hfile_restore_process: str = None,
    ):
        self.status = status
        self.finish_time = finish_time
        self.schema_process = schema_process
        self.bulk_load_process = bulk_load_process
        self.record_id = record_id
        self.create_time = create_time
        self.log_process = log_process
        self.hfile_restore_process = hfile_restore_process

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.schema_process is not None:
            result['SchemaProcess'] = self.schema_process
        if self.bulk_load_process is not None:
            result['BulkLoadProcess'] = self.bulk_load_process
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.log_process is not None:
            result['LogProcess'] = self.log_process
        if self.hfile_restore_process is not None:
            result['HfileRestoreProcess'] = self.hfile_restore_process
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('SchemaProcess') is not None:
            self.schema_process = m.get('SchemaProcess')
        if m.get('BulkLoadProcess') is not None:
            self.bulk_load_process = m.get('BulkLoadProcess')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LogProcess') is not None:
            self.log_process = m.get('LogProcess')
        if m.get('HfileRestoreProcess') is not None:
            self.hfile_restore_process = m.get('HfileRestoreProcess')
        return self


class DescribeRestoreSummaryResponseBodyRescords(TeaModel):
    def __init__(
        self,
        rescord: List[DescribeRestoreSummaryResponseBodyRescordsRescord] = None,
    ):
        self.rescord = rescord

    def validate(self):
        if self.rescord:
            for k in self.rescord:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Rescord'] = []
        if self.rescord is not None:
            for k in self.rescord:
                result['Rescord'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rescord = []
        if m.get('Rescord') is not None:
            for k in m.get('Rescord'):
                temp_model = DescribeRestoreSummaryResponseBodyRescordsRescord()
                self.rescord.append(temp_model.from_map(k))
        return self


class DescribeRestoreSummaryResponseBody(TeaModel):
    def __init__(
        self,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        total: int = None,
        has_more_restore_record: int = None,
        rescords: DescribeRestoreSummaryResponseBodyRescords = None,
    ):
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.total = total
        self.has_more_restore_record = has_more_restore_record
        self.rescords = rescords

    def validate(self):
        if self.rescords:
            self.rescords.validate()

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total is not None:
            result['Total'] = self.total
        if self.has_more_restore_record is not None:
            result['HasMoreRestoreRecord'] = self.has_more_restore_record
        if self.rescords is not None:
            result['Rescords'] = self.rescords.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('HasMoreRestoreRecord') is not None:
            self.has_more_restore_record = m.get('HasMoreRestoreRecord')
        if m.get('Rescords') is not None:
            temp_model = DescribeRestoreSummaryResponseBodyRescords()
            self.rescords = temp_model.from_map(m['Rescords'])
        return self


class DescribeRestoreSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRestoreSummaryResponseBody = None,
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
            temp_model = DescribeRestoreSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRestoreTablesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        restore_record_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.restore_record_id = restore_record_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.restore_record_id is not None:
            result['RestoreRecordId'] = self.restore_record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RestoreRecordId') is not None:
            self.restore_record_id = m.get('RestoreRecordId')
        return self


class DescribeRestoreTablesResponseBodyRestoreSchemaRestoreSchemaDetailsRestoreSchemaDetail(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        state: str = None,
        message: str = None,
        table: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.state = state
        self.message = message
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.message is not None:
            result['Message'] = self.message
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class DescribeRestoreTablesResponseBodyRestoreSchemaRestoreSchemaDetails(TeaModel):
    def __init__(
        self,
        restore_schema_detail: List[DescribeRestoreTablesResponseBodyRestoreSchemaRestoreSchemaDetailsRestoreSchemaDetail] = None,
    ):
        self.restore_schema_detail = restore_schema_detail

    def validate(self):
        if self.restore_schema_detail:
            for k in self.restore_schema_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['RestoreSchemaDetail'] = []
        if self.restore_schema_detail is not None:
            for k in self.restore_schema_detail:
                result['RestoreSchemaDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.restore_schema_detail = []
        if m.get('RestoreSchemaDetail') is not None:
            for k in m.get('RestoreSchemaDetail'):
                temp_model = DescribeRestoreTablesResponseBodyRestoreSchemaRestoreSchemaDetailsRestoreSchemaDetail()
                self.restore_schema_detail.append(temp_model.from_map(k))
        return self


class DescribeRestoreTablesResponseBodyRestoreSchema(TeaModel):
    def __init__(
        self,
        succeed: int = None,
        restore_schema_details: DescribeRestoreTablesResponseBodyRestoreSchemaRestoreSchemaDetails = None,
        page_size: int = None,
        page_number: int = None,
        fail: int = None,
        total: int = None,
    ):
        self.succeed = succeed
        self.restore_schema_details = restore_schema_details
        self.page_size = page_size
        self.page_number = page_number
        self.fail = fail
        self.total = total

    def validate(self):
        if self.restore_schema_details:
            self.restore_schema_details.validate()

    def to_map(self):
        result = dict()
        if self.succeed is not None:
            result['Succeed'] = self.succeed
        if self.restore_schema_details is not None:
            result['RestoreSchemaDetails'] = self.restore_schema_details.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.fail is not None:
            result['Fail'] = self.fail
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Succeed') is not None:
            self.succeed = m.get('Succeed')
        if m.get('RestoreSchemaDetails') is not None:
            temp_model = DescribeRestoreTablesResponseBodyRestoreSchemaRestoreSchemaDetails()
            self.restore_schema_details = temp_model.from_map(m['RestoreSchemaDetails'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Fail') is not None:
            self.fail = m.get('Fail')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeRestoreTablesResponseBodyRestoreFullRestoreFullDetailsRestoreFullDetail(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        process: str = None,
        data_size: str = None,
        speed: str = None,
        state: str = None,
        message: str = None,
        table: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.process = process
        self.data_size = data_size
        self.speed = speed
        self.state = state
        self.message = message
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.process is not None:
            result['Process'] = self.process
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.state is not None:
            result['State'] = self.state
        if self.message is not None:
            result['Message'] = self.message
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class DescribeRestoreTablesResponseBodyRestoreFullRestoreFullDetails(TeaModel):
    def __init__(
        self,
        restore_full_detail: List[DescribeRestoreTablesResponseBodyRestoreFullRestoreFullDetailsRestoreFullDetail] = None,
    ):
        self.restore_full_detail = restore_full_detail

    def validate(self):
        if self.restore_full_detail:
            for k in self.restore_full_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['RestoreFullDetail'] = []
        if self.restore_full_detail is not None:
            for k in self.restore_full_detail:
                result['RestoreFullDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.restore_full_detail = []
        if m.get('RestoreFullDetail') is not None:
            for k in m.get('RestoreFullDetail'):
                temp_model = DescribeRestoreTablesResponseBodyRestoreFullRestoreFullDetailsRestoreFullDetail()
                self.restore_full_detail.append(temp_model.from_map(k))
        return self


class DescribeRestoreTablesResponseBodyRestoreFull(TeaModel):
    def __init__(
        self,
        succeed: int = None,
        data_size: str = None,
        speed: str = None,
        restore_full_details: DescribeRestoreTablesResponseBodyRestoreFullRestoreFullDetails = None,
        page_size: int = None,
        fail: int = None,
        page_number: int = None,
        total: int = None,
    ):
        self.succeed = succeed
        self.data_size = data_size
        self.speed = speed
        self.restore_full_details = restore_full_details
        self.page_size = page_size
        self.fail = fail
        self.page_number = page_number
        self.total = total

    def validate(self):
        if self.restore_full_details:
            self.restore_full_details.validate()

    def to_map(self):
        result = dict()
        if self.succeed is not None:
            result['Succeed'] = self.succeed
        if self.data_size is not None:
            result['DataSize'] = self.data_size
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.restore_full_details is not None:
            result['RestoreFullDetails'] = self.restore_full_details.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.fail is not None:
            result['Fail'] = self.fail
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Succeed') is not None:
            self.succeed = m.get('Succeed')
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('RestoreFullDetails') is not None:
            temp_model = DescribeRestoreTablesResponseBodyRestoreFullRestoreFullDetails()
            self.restore_full_details = temp_model.from_map(m['RestoreFullDetails'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Fail') is not None:
            self.fail = m.get('Fail')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class DescribeRestoreTablesResponseBodyTables(TeaModel):
    def __init__(
        self,
        table: List[str] = None,
    ):
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.table is not None:
            result['Table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Table') is not None:
            self.table = m.get('Table')
        return self


class DescribeRestoreTablesResponseBodyRestoreSummary(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        state: str = None,
        record_id: str = None,
        restore_to_date: str = None,
        target_cluster: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.state = state
        self.record_id = record_id
        self.restore_to_date = restore_to_date
        self.target_cluster = target_cluster

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.restore_to_date is not None:
            result['RestoreToDate'] = self.restore_to_date
        if self.target_cluster is not None:
            result['TargetCluster'] = self.target_cluster
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('RestoreToDate') is not None:
            self.restore_to_date = m.get('RestoreToDate')
        if m.get('TargetCluster') is not None:
            self.target_cluster = m.get('TargetCluster')
        return self


class DescribeRestoreTablesResponseBodyRestoreIncrDetail(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        process: str = None,
        restore_start_ts: str = None,
        state: str = None,
        restored_ts: str = None,
        restore_delay: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.process = process
        self.restore_start_ts = restore_start_ts
        self.state = state
        self.restored_ts = restored_ts
        self.restore_delay = restore_delay

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.process is not None:
            result['Process'] = self.process
        if self.restore_start_ts is not None:
            result['RestoreStartTs'] = self.restore_start_ts
        if self.state is not None:
            result['State'] = self.state
        if self.restored_ts is not None:
            result['RestoredTs'] = self.restored_ts
        if self.restore_delay is not None:
            result['RestoreDelay'] = self.restore_delay
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('RestoreStartTs') is not None:
            self.restore_start_ts = m.get('RestoreStartTs')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('RestoredTs') is not None:
            self.restored_ts = m.get('RestoredTs')
        if m.get('RestoreDelay') is not None:
            self.restore_delay = m.get('RestoreDelay')
        return self


class DescribeRestoreTablesResponseBody(TeaModel):
    def __init__(
        self,
        restore_schema: DescribeRestoreTablesResponseBodyRestoreSchema = None,
        restore_full: DescribeRestoreTablesResponseBodyRestoreFull = None,
        request_id: str = None,
        tables: DescribeRestoreTablesResponseBodyTables = None,
        restore_summary: DescribeRestoreTablesResponseBodyRestoreSummary = None,
        restore_incr_detail: DescribeRestoreTablesResponseBodyRestoreIncrDetail = None,
    ):
        self.restore_schema = restore_schema
        self.restore_full = restore_full
        self.request_id = request_id
        self.tables = tables
        self.restore_summary = restore_summary
        self.restore_incr_detail = restore_incr_detail

    def validate(self):
        if self.restore_schema:
            self.restore_schema.validate()
        if self.restore_full:
            self.restore_full.validate()
        if self.tables:
            self.tables.validate()
        if self.restore_summary:
            self.restore_summary.validate()
        if self.restore_incr_detail:
            self.restore_incr_detail.validate()

    def to_map(self):
        result = dict()
        if self.restore_schema is not None:
            result['RestoreSchema'] = self.restore_schema.to_map()
        if self.restore_full is not None:
            result['RestoreFull'] = self.restore_full.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tables is not None:
            result['Tables'] = self.tables.to_map()
        if self.restore_summary is not None:
            result['RestoreSummary'] = self.restore_summary.to_map()
        if self.restore_incr_detail is not None:
            result['RestoreIncrDetail'] = self.restore_incr_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RestoreSchema') is not None:
            temp_model = DescribeRestoreTablesResponseBodyRestoreSchema()
            self.restore_schema = temp_model.from_map(m['RestoreSchema'])
        if m.get('RestoreFull') is not None:
            temp_model = DescribeRestoreTablesResponseBodyRestoreFull()
            self.restore_full = temp_model.from_map(m['RestoreFull'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tables') is not None:
            temp_model = DescribeRestoreTablesResponseBodyTables()
            self.tables = temp_model.from_map(m['Tables'])
        if m.get('RestoreSummary') is not None:
            temp_model = DescribeRestoreTablesResponseBodyRestoreSummary()
            self.restore_summary = temp_model.from_map(m['RestoreSummary'])
        if m.get('RestoreIncrDetail') is not None:
            temp_model = DescribeRestoreTablesResponseBodyRestoreIncrDetail()
            self.restore_incr_detail = temp_model.from_map(m['RestoreIncrDetail'])
        return self


class DescribeRestoreTablesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeRestoreTablesResponseBody = None,
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
            temp_model = DescribeRestoreTablesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSecurityGroupsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeSecurityGroupsResponseBodySecurityGroupIds(TeaModel):
    def __init__(
        self,
        security_group_id: List[str] = None,
    ):
        self.security_group_id = security_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class DescribeSecurityGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        security_group_ids: DescribeSecurityGroupsResponseBodySecurityGroupIds = None,
    ):
        self.request_id = request_id
        self.security_group_ids = security_group_ids

    def validate(self):
        if self.security_group_ids:
            self.security_group_ids.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityGroupIds') is not None:
            temp_model = DescribeSecurityGroupsResponseBodySecurityGroupIds()
            self.security_group_ids = temp_model.from_map(m['SecurityGroupIds'])
        return self


class DescribeSecurityGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSecurityGroupsResponseBody = None,
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
            temp_model = DescribeSecurityGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSubDomainRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        zone_id: str = None,
    ):
        self.region_id = region_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeSubDomainResponseBody(TeaModel):
    def __init__(
        self,
        sub_domain: str = None,
        request_id: str = None,
    ):
        self.sub_domain = sub_domain
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeSubDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSubDomainResponseBody = None,
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
            temp_model = DescribeSubDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableHBaseueBackupRequest(TeaModel):
    def __init__(
        self,
        hbaseue_cluster_id: str = None,
        node_count: int = None,
        cold_storage_size: int = None,
        client_token: str = None,
    ):
        self.hbaseue_cluster_id = hbaseue_cluster_id
        self.node_count = node_count
        self.cold_storage_size = cold_storage_size
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.hbaseue_cluster_id is not None:
            result['HbaseueClusterId'] = self.hbaseue_cluster_id
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.cold_storage_size is not None:
            result['ColdStorageSize'] = self.cold_storage_size
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HbaseueClusterId') is not None:
            self.hbaseue_cluster_id = m.get('HbaseueClusterId')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('ColdStorageSize') is not None:
            self.cold_storage_size = m.get('ColdStorageSize')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class EnableHBaseueBackupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cluster_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.cluster_id = cluster_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class EnableHBaseueBackupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableHBaseueBackupResponseBody = None,
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
            temp_model = EnableHBaseueBackupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableHBaseueModuleRequest(TeaModel):
    def __init__(
        self,
        module_cluster_name: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        master_instance_type: str = None,
        core_instance_type: str = None,
        disk_type: str = None,
        disk_size: int = None,
        node_count: int = None,
        pay_type: str = None,
        period_unit: str = None,
        period: int = None,
        auto_renew_period: int = None,
        client_token: str = None,
        hbaseue_cluster_id: str = None,
        bds_id: str = None,
        module_type_name: str = None,
        region_id: str = None,
        zone_id: str = None,
    ):
        self.module_cluster_name = module_cluster_name
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id
        self.master_instance_type = master_instance_type
        self.core_instance_type = core_instance_type
        self.disk_type = disk_type
        self.disk_size = disk_size
        self.node_count = node_count
        self.pay_type = pay_type
        self.period_unit = period_unit
        self.period = period
        self.auto_renew_period = auto_renew_period
        self.client_token = client_token
        self.hbaseue_cluster_id = hbaseue_cluster_id
        self.bds_id = bds_id
        self.module_type_name = module_type_name
        self.region_id = region_id
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.module_cluster_name is not None:
            result['ModuleClusterName'] = self.module_cluster_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.master_instance_type is not None:
            result['MasterInstanceType'] = self.master_instance_type
        if self.core_instance_type is not None:
            result['CoreInstanceType'] = self.core_instance_type
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.period is not None:
            result['Period'] = self.period
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.hbaseue_cluster_id is not None:
            result['HbaseueClusterId'] = self.hbaseue_cluster_id
        if self.bds_id is not None:
            result['BdsId'] = self.bds_id
        if self.module_type_name is not None:
            result['ModuleTypeName'] = self.module_type_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModuleClusterName') is not None:
            self.module_cluster_name = m.get('ModuleClusterName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('MasterInstanceType') is not None:
            self.master_instance_type = m.get('MasterInstanceType')
        if m.get('CoreInstanceType') is not None:
            self.core_instance_type = m.get('CoreInstanceType')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('HbaseueClusterId') is not None:
            self.hbaseue_cluster_id = m.get('HbaseueClusterId')
        if m.get('BdsId') is not None:
            self.bds_id = m.get('BdsId')
        if m.get('ModuleTypeName') is not None:
            self.module_type_name = m.get('ModuleTypeName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class EnableHBaseueModuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cluster_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.cluster_id = cluster_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class EnableHBaseueModuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableHBaseueModuleResponseBody = None,
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
            temp_model = EnableHBaseueModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EvaluateMultiZoneResourceRequest(TeaModel):
    def __init__(
        self,
        engine: str = None,
        engine_version: str = None,
        arch_version: str = None,
        cluster_name: str = None,
        region_id: str = None,
        vpc_id: str = None,
        multi_zone_combination: str = None,
        primary_zone_id: str = None,
        primary_vswitch_id: str = None,
        standby_zone_id: str = None,
        standby_vswitch_id: str = None,
        arbiter_zone_id: str = None,
        arbiter_vswitch_id: str = None,
        master_instance_type: str = None,
        core_instance_type: str = None,
        core_disk_type: str = None,
        core_disk_size: int = None,
        core_node_count: int = None,
        log_instance_type: str = None,
        log_disk_type: str = None,
        log_disk_size: int = None,
        log_node_count: int = None,
        security_iplist: str = None,
        pay_type: str = None,
        period_unit: str = None,
        period: int = None,
        auto_renew_period: int = None,
        client_token: str = None,
    ):
        self.engine = engine
        self.engine_version = engine_version
        self.arch_version = arch_version
        self.cluster_name = cluster_name
        self.region_id = region_id
        self.vpc_id = vpc_id
        self.multi_zone_combination = multi_zone_combination
        self.primary_zone_id = primary_zone_id
        self.primary_vswitch_id = primary_vswitch_id
        self.standby_zone_id = standby_zone_id
        self.standby_vswitch_id = standby_vswitch_id
        self.arbiter_zone_id = arbiter_zone_id
        self.arbiter_vswitch_id = arbiter_vswitch_id
        self.master_instance_type = master_instance_type
        self.core_instance_type = core_instance_type
        self.core_disk_type = core_disk_type
        self.core_disk_size = core_disk_size
        self.core_node_count = core_node_count
        self.log_instance_type = log_instance_type
        self.log_disk_type = log_disk_type
        self.log_disk_size = log_disk_size
        self.log_node_count = log_node_count
        self.security_iplist = security_iplist
        self.pay_type = pay_type
        self.period_unit = period_unit
        self.period = period
        self.auto_renew_period = auto_renew_period
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.engine is not None:
            result['Engine'] = self.engine
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version
        if self.arch_version is not None:
            result['ArchVersion'] = self.arch_version
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.multi_zone_combination is not None:
            result['MultiZoneCombination'] = self.multi_zone_combination
        if self.primary_zone_id is not None:
            result['PrimaryZoneId'] = self.primary_zone_id
        if self.primary_vswitch_id is not None:
            result['PrimaryVSwitchId'] = self.primary_vswitch_id
        if self.standby_zone_id is not None:
            result['StandbyZoneId'] = self.standby_zone_id
        if self.standby_vswitch_id is not None:
            result['StandbyVSwitchId'] = self.standby_vswitch_id
        if self.arbiter_zone_id is not None:
            result['ArbiterZoneId'] = self.arbiter_zone_id
        if self.arbiter_vswitch_id is not None:
            result['ArbiterVSwitchId'] = self.arbiter_vswitch_id
        if self.master_instance_type is not None:
            result['MasterInstanceType'] = self.master_instance_type
        if self.core_instance_type is not None:
            result['CoreInstanceType'] = self.core_instance_type
        if self.core_disk_type is not None:
            result['CoreDiskType'] = self.core_disk_type
        if self.core_disk_size is not None:
            result['CoreDiskSize'] = self.core_disk_size
        if self.core_node_count is not None:
            result['CoreNodeCount'] = self.core_node_count
        if self.log_instance_type is not None:
            result['LogInstanceType'] = self.log_instance_type
        if self.log_disk_type is not None:
            result['LogDiskType'] = self.log_disk_type
        if self.log_disk_size is not None:
            result['LogDiskSize'] = self.log_disk_size
        if self.log_node_count is not None:
            result['LogNodeCount'] = self.log_node_count
        if self.security_iplist is not None:
            result['SecurityIPList'] = self.security_iplist
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.period is not None:
            result['Period'] = self.period
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')
        if m.get('ArchVersion') is not None:
            self.arch_version = m.get('ArchVersion')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('MultiZoneCombination') is not None:
            self.multi_zone_combination = m.get('MultiZoneCombination')
        if m.get('PrimaryZoneId') is not None:
            self.primary_zone_id = m.get('PrimaryZoneId')
        if m.get('PrimaryVSwitchId') is not None:
            self.primary_vswitch_id = m.get('PrimaryVSwitchId')
        if m.get('StandbyZoneId') is not None:
            self.standby_zone_id = m.get('StandbyZoneId')
        if m.get('StandbyVSwitchId') is not None:
            self.standby_vswitch_id = m.get('StandbyVSwitchId')
        if m.get('ArbiterZoneId') is not None:
            self.arbiter_zone_id = m.get('ArbiterZoneId')
        if m.get('ArbiterVSwitchId') is not None:
            self.arbiter_vswitch_id = m.get('ArbiterVSwitchId')
        if m.get('MasterInstanceType') is not None:
            self.master_instance_type = m.get('MasterInstanceType')
        if m.get('CoreInstanceType') is not None:
            self.core_instance_type = m.get('CoreInstanceType')
        if m.get('CoreDiskType') is not None:
            self.core_disk_type = m.get('CoreDiskType')
        if m.get('CoreDiskSize') is not None:
            self.core_disk_size = m.get('CoreDiskSize')
        if m.get('CoreNodeCount') is not None:
            self.core_node_count = m.get('CoreNodeCount')
        if m.get('LogInstanceType') is not None:
            self.log_instance_type = m.get('LogInstanceType')
        if m.get('LogDiskType') is not None:
            self.log_disk_type = m.get('LogDiskType')
        if m.get('LogDiskSize') is not None:
            self.log_disk_size = m.get('LogDiskSize')
        if m.get('LogNodeCount') is not None:
            self.log_node_count = m.get('LogNodeCount')
        if m.get('SecurityIPList') is not None:
            self.security_iplist = m.get('SecurityIPList')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class EvaluateMultiZoneResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EvaluateMultiZoneResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EvaluateMultiZoneResourceResponseBody = None,
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
            temp_model = EvaluateMultiZoneResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMultimodeCmsUrlRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetMultimodeCmsUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cluster_id: str = None,
        multimod_cms_url: str = None,
    ):
        self.request_id = request_id
        self.cluster_id = cluster_id
        self.multimod_cms_url = multimod_cms_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.multimod_cms_url is not None:
            result['MultimodCmsUrl'] = self.multimod_cms_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('MultimodCmsUrl') is not None:
            self.multimod_cms_url = m.get('MultimodCmsUrl')
        return self


class GetMultimodeCmsUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMultimodeCmsUrlResponseBody = None,
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
            temp_model = GetMultimodeCmsUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHBaseInstancesRequest(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
    ):
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListHBaseInstancesResponseBodyInstancesInstance(TeaModel):
    def __init__(
        self,
        is_default: bool = None,
        instance_name: str = None,
        instance_id: str = None,
    ):
        self.is_default = is_default
        self.instance_name = instance_name
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListHBaseInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        instance: List[ListHBaseInstancesResponseBodyInstancesInstance] = None,
    ):
        self.instance = instance

    def validate(self):
        if self.instance:
            for k in self.instance:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Instance'] = []
        if self.instance is not None:
            for k in self.instance:
                result['Instance'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance = []
        if m.get('Instance') is not None:
            for k in m.get('Instance'):
                temp_model = ListHBaseInstancesResponseBodyInstancesInstance()
                self.instance.append(temp_model.from_map(k))
        return self


class ListHBaseInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: ListHBaseInstancesResponseBodyInstances = None,
        request_id: str = None,
    ):
        self.instances = instances
        self.request_id = request_id

    def validate(self):
        if self.instances:
            self.instances.validate()

    def to_map(self):
        result = dict()
        if self.instances is not None:
            result['Instances'] = self.instances.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instances') is not None:
            temp_model = ListHBaseInstancesResponseBodyInstances()
            self.instances = temp_model.from_map(m['Instances'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListHBaseInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListHBaseInstancesResponseBody = None,
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
            temp_model = ListHBaseInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceServiceConfigHistoriesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.cluster_id = cluster_id
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListInstanceServiceConfigHistoriesResponseBodyConfigureHistoryListConfig(TeaModel):
    def __init__(
        self,
        effective: str = None,
        old_value: str = None,
        create_time: str = None,
        configure_name: str = None,
        new_value: str = None,
    ):
        self.effective = effective
        self.old_value = old_value
        self.create_time = create_time
        self.configure_name = configure_name
        self.new_value = new_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.effective is not None:
            result['Effective'] = self.effective
        if self.old_value is not None:
            result['OldValue'] = self.old_value
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.configure_name is not None:
            result['ConfigureName'] = self.configure_name
        if self.new_value is not None:
            result['NewValue'] = self.new_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Effective') is not None:
            self.effective = m.get('Effective')
        if m.get('OldValue') is not None:
            self.old_value = m.get('OldValue')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ConfigureName') is not None:
            self.configure_name = m.get('ConfigureName')
        if m.get('NewValue') is not None:
            self.new_value = m.get('NewValue')
        return self


class ListInstanceServiceConfigHistoriesResponseBodyConfigureHistoryList(TeaModel):
    def __init__(
        self,
        config: List[ListInstanceServiceConfigHistoriesResponseBodyConfigureHistoryListConfig] = None,
    ):
        self.config = config

    def validate(self):
        if self.config:
            for k in self.config:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Config'] = []
        if self.config is not None:
            for k in self.config:
                result['Config'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config = []
        if m.get('Config') is not None:
            for k in m.get('Config'):
                temp_model = ListInstanceServiceConfigHistoriesResponseBodyConfigureHistoryListConfig()
                self.config.append(temp_model.from_map(k))
        return self


class ListInstanceServiceConfigHistoriesResponseBody(TeaModel):
    def __init__(
        self,
        total_record_count: int = None,
        page_record_count: int = None,
        request_id: str = None,
        page_number: int = None,
        configure_history_list: ListInstanceServiceConfigHistoriesResponseBodyConfigureHistoryList = None,
    ):
        self.total_record_count = total_record_count
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.page_number = page_number
        self.configure_history_list = configure_history_list

    def validate(self):
        if self.configure_history_list:
            self.configure_history_list.validate()

    def to_map(self):
        result = dict()
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.configure_history_list is not None:
            result['ConfigureHistoryList'] = self.configure_history_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ConfigureHistoryList') is not None:
            temp_model = ListInstanceServiceConfigHistoriesResponseBodyConfigureHistoryList()
            self.configure_history_list = temp_model.from_map(m['ConfigureHistoryList'])
        return self


class ListInstanceServiceConfigHistoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstanceServiceConfigHistoriesResponseBody = None,
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
            temp_model = ListInstanceServiceConfigHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceServiceConfigurationsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.cluster_id = cluster_id
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListInstanceServiceConfigurationsResponseBodyConfigureListConfig(TeaModel):
    def __init__(
        self,
        description: str = None,
        running_value: str = None,
        configure_unit: str = None,
        configure_name: str = None,
        value_range: str = None,
        default_value: str = None,
        need_restart: str = None,
    ):
        self.description = description
        self.running_value = running_value
        self.configure_unit = configure_unit
        self.configure_name = configure_name
        self.value_range = value_range
        self.default_value = default_value
        self.need_restart = need_restart

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.running_value is not None:
            result['RunningValue'] = self.running_value
        if self.configure_unit is not None:
            result['ConfigureUnit'] = self.configure_unit
        if self.configure_name is not None:
            result['ConfigureName'] = self.configure_name
        if self.value_range is not None:
            result['ValueRange'] = self.value_range
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.need_restart is not None:
            result['NeedRestart'] = self.need_restart
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RunningValue') is not None:
            self.running_value = m.get('RunningValue')
        if m.get('ConfigureUnit') is not None:
            self.configure_unit = m.get('ConfigureUnit')
        if m.get('ConfigureName') is not None:
            self.configure_name = m.get('ConfigureName')
        if m.get('ValueRange') is not None:
            self.value_range = m.get('ValueRange')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('NeedRestart') is not None:
            self.need_restart = m.get('NeedRestart')
        return self


class ListInstanceServiceConfigurationsResponseBodyConfigureList(TeaModel):
    def __init__(
        self,
        config: List[ListInstanceServiceConfigurationsResponseBodyConfigureListConfig] = None,
    ):
        self.config = config

    def validate(self):
        if self.config:
            for k in self.config:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Config'] = []
        if self.config is not None:
            for k in self.config:
                result['Config'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config = []
        if m.get('Config') is not None:
            for k in m.get('Config'):
                temp_model = ListInstanceServiceConfigurationsResponseBodyConfigureListConfig()
                self.config.append(temp_model.from_map(k))
        return self


class ListInstanceServiceConfigurationsResponseBody(TeaModel):
    def __init__(
        self,
        total_record_count: int = None,
        page_record_count: int = None,
        request_id: str = None,
        page_number: int = None,
        configure_list: ListInstanceServiceConfigurationsResponseBodyConfigureList = None,
    ):
        self.total_record_count = total_record_count
        self.page_record_count = page_record_count
        self.request_id = request_id
        self.page_number = page_number
        self.configure_list = configure_list

    def validate(self):
        if self.configure_list:
            self.configure_list.validate()

    def to_map(self):
        result = dict()
        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count
        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.configure_list is not None:
            result['ConfigureList'] = self.configure_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')
        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('ConfigureList') is not None:
            temp_model = ListInstanceServiceConfigurationsResponseBodyConfigureList()
            self.configure_list = temp_model.from_map(m['ConfigureList'])
        return self


class ListInstanceServiceConfigurationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstanceServiceConfigurationsResponseBody = None,
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
            temp_model = ListInstanceServiceConfigurationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        next_token: str = None,
        resource_id: List[str] = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.region_id = region_id
        self.next_token = next_token
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        tag_value: str = None,
        resource_id: str = None,
        tag_key: str = None,
    ):
        self.resource_type = resource_type
        self.tag_value = tag_value
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagResourcesResponseBody = None,
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagsRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListTagsResponseBodyTagsTag(TeaModel):
    def __init__(
        self,
        tag_value: str = None,
        tag_key: str = None,
    ):
        self.tag_value = tag_value
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagsResponseBodyTags(TeaModel):
    def __init__(
        self,
        tag: List[ListTagsResponseBodyTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagsResponseBodyTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        tags: ListTagsResponseBodyTags = None,
    ):
        self.request_id = request_id
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tags') is not None:
            temp_model = ListTagsResponseBodyTags()
            self.tags = temp_model.from_map(m['Tags'])
        return self


class ListTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagsResponseBody = None,
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
            temp_model = ListTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupPlanConfigRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        tables: str = None,
        full_backup_cycle: str = None,
        min_hfile_backup_count: str = None,
        next_full_backup_date: str = None,
    ):
        self.cluster_id = cluster_id
        self.tables = tables
        self.full_backup_cycle = full_backup_cycle
        self.min_hfile_backup_count = min_hfile_backup_count
        self.next_full_backup_date = next_full_backup_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.tables is not None:
            result['Tables'] = self.tables
        if self.full_backup_cycle is not None:
            result['FullBackupCycle'] = self.full_backup_cycle
        if self.min_hfile_backup_count is not None:
            result['MinHFileBackupCount'] = self.min_hfile_backup_count
        if self.next_full_backup_date is not None:
            result['NextFullBackupDate'] = self.next_full_backup_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Tables') is not None:
            self.tables = m.get('Tables')
        if m.get('FullBackupCycle') is not None:
            self.full_backup_cycle = m.get('FullBackupCycle')
        if m.get('MinHFileBackupCount') is not None:
            self.min_hfile_backup_count = m.get('MinHFileBackupCount')
        if m.get('NextFullBackupDate') is not None:
            self.next_full_backup_date = m.get('NextFullBackupDate')
        return self


class ModifyBackupPlanConfigResponseBody(TeaModel):
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


class ModifyBackupPlanConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyBackupPlanConfigResponseBody = None,
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
            temp_model = ModifyBackupPlanConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupPolicyRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        preferred_backup_time: str = None,
        preferred_backup_period: str = None,
        preferred_backup_start_time_utc: str = None,
        preferred_backup_end_time_utc: str = None,
    ):
        self.cluster_id = cluster_id
        self.preferred_backup_time = preferred_backup_time
        self.preferred_backup_period = preferred_backup_period
        self.preferred_backup_start_time_utc = preferred_backup_start_time_utc
        self.preferred_backup_end_time_utc = preferred_backup_end_time_utc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.preferred_backup_time is not None:
            result['PreferredBackupTime'] = self.preferred_backup_time
        if self.preferred_backup_period is not None:
            result['PreferredBackupPeriod'] = self.preferred_backup_period
        if self.preferred_backup_start_time_utc is not None:
            result['PreferredBackupStartTimeUTC'] = self.preferred_backup_start_time_utc
        if self.preferred_backup_end_time_utc is not None:
            result['PreferredBackupEndTimeUTC'] = self.preferred_backup_end_time_utc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PreferredBackupTime') is not None:
            self.preferred_backup_time = m.get('PreferredBackupTime')
        if m.get('PreferredBackupPeriod') is not None:
            self.preferred_backup_period = m.get('PreferredBackupPeriod')
        if m.get('PreferredBackupStartTimeUTC') is not None:
            self.preferred_backup_start_time_utc = m.get('PreferredBackupStartTimeUTC')
        if m.get('PreferredBackupEndTimeUTC') is not None:
            self.preferred_backup_end_time_utc = m.get('PreferredBackupEndTimeUTC')
        return self


class ModifyBackupPolicyResponseBody(TeaModel):
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


class ModifyBackupPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyBackupPolicyResponseBody = None,
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
            temp_model = ModifyBackupPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyClusterDeletionProtectionRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        protection: bool = None,
    ):
        self.cluster_id = cluster_id
        self.protection = protection

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.protection is not None:
            result['Protection'] = self.protection
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Protection') is not None:
            self.protection = m.get('Protection')
        return self


class ModifyClusterDeletionProtectionResponseBody(TeaModel):
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


class ModifyClusterDeletionProtectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyClusterDeletionProtectionResponseBody = None,
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
            temp_model = ModifyClusterDeletionProtectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDiskWarningLineRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        warning_line: int = None,
    ):
        self.cluster_id = cluster_id
        self.warning_line = warning_line

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.warning_line is not None:
            result['WarningLine'] = self.warning_line
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('WarningLine') is not None:
            self.warning_line = m.get('WarningLine')
        return self


class ModifyDiskWarningLineResponseBody(TeaModel):
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


class ModifyDiskWarningLineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDiskWarningLineResponseBody = None,
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
            temp_model = ModifyDiskWarningLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceMaintainTimeRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        maintain_start_time: str = None,
        maintain_end_time: str = None,
    ):
        self.cluster_id = cluster_id
        self.maintain_start_time = maintain_start_time
        self.maintain_end_time = maintain_end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        return self


class ModifyInstanceMaintainTimeResponseBody(TeaModel):
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


class ModifyInstanceMaintainTimeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceMaintainTimeResponseBody = None,
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
            temp_model = ModifyInstanceMaintainTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceNameRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        region_id: str = None,
        zone_id: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
    ):
        self.client_token = client_token
        self.region_id = region_id
        self.zone_id = zone_id
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        return self


class ModifyInstanceNameResponseBody(TeaModel):
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


class ModifyInstanceNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceNameResponseBody = None,
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
            temp_model = ModifyInstanceNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceServiceConfigRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        restart: bool = None,
        configure_name: str = None,
        configure_value: str = None,
        parameters: str = None,
    ):
        self.cluster_id = cluster_id
        self.restart = restart
        self.configure_name = configure_name
        self.configure_value = configure_value
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.restart is not None:
            result['Restart'] = self.restart
        if self.configure_name is not None:
            result['ConfigureName'] = self.configure_name
        if self.configure_value is not None:
            result['ConfigureValue'] = self.configure_value
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Restart') is not None:
            self.restart = m.get('Restart')
        if m.get('ConfigureName') is not None:
            self.configure_name = m.get('ConfigureName')
        if m.get('ConfigureValue') is not None:
            self.configure_value = m.get('ConfigureValue')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class ModifyInstanceServiceConfigResponseBody(TeaModel):
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


class ModifyInstanceServiceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceServiceConfigResponseBody = None,
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
            temp_model = ModifyInstanceServiceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceTypeRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        master_instance_type: str = None,
        core_instance_type: str = None,
    ):
        self.cluster_id = cluster_id
        self.master_instance_type = master_instance_type
        self.core_instance_type = core_instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.master_instance_type is not None:
            result['MasterInstanceType'] = self.master_instance_type
        if self.core_instance_type is not None:
            result['CoreInstanceType'] = self.core_instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('MasterInstanceType') is not None:
            self.master_instance_type = m.get('MasterInstanceType')
        if m.get('CoreInstanceType') is not None:
            self.core_instance_type = m.get('CoreInstanceType')
        return self


class ModifyInstanceTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ModifyInstanceTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceTypeResponseBody = None,
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
            temp_model = ModifyInstanceTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyIpWhitelistRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        ip_list: str = None,
        group_name: str = None,
        ip_version: str = None,
    ):
        self.cluster_id = cluster_id
        self.ip_list = ip_list
        self.group_name = group_name
        self.ip_version = ip_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        return self


class ModifyIpWhitelistResponseBody(TeaModel):
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


class ModifyIpWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyIpWhitelistResponseBody = None,
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
            temp_model = ModifyIpWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyMultiZoneClusterNodeTypeRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        master_instance_type: str = None,
        core_instance_type: str = None,
        log_instance_type: str = None,
    ):
        self.cluster_id = cluster_id
        self.master_instance_type = master_instance_type
        self.core_instance_type = core_instance_type
        self.log_instance_type = log_instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.master_instance_type is not None:
            result['MasterInstanceType'] = self.master_instance_type
        if self.core_instance_type is not None:
            result['CoreInstanceType'] = self.core_instance_type
        if self.log_instance_type is not None:
            result['LogInstanceType'] = self.log_instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('MasterInstanceType') is not None:
            self.master_instance_type = m.get('MasterInstanceType')
        if m.get('CoreInstanceType') is not None:
            self.core_instance_type = m.get('CoreInstanceType')
        if m.get('LogInstanceType') is not None:
            self.log_instance_type = m.get('LogInstanceType')
        return self


class ModifyMultiZoneClusterNodeTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ModifyMultiZoneClusterNodeTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyMultiZoneClusterNodeTypeResponseBody = None,
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
            temp_model = ModifyMultiZoneClusterNodeTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifySecurityGroupsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        security_group_ids: str = None,
    ):
        self.cluster_id = cluster_id
        self.security_group_ids = security_group_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        return self


class ModifySecurityGroupsResponseBody(TeaModel):
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


class ModifySecurityGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifySecurityGroupsResponseBody = None,
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
            temp_model = ModifySecurityGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUIAccountPasswordRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        account_name: str = None,
        account_password: str = None,
    ):
        self.cluster_id = cluster_id
        self.account_name = account_name
        self.account_password = account_password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_password is not None:
            result['AccountPassword'] = self.account_password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountPassword') is not None:
            self.account_password = m.get('AccountPassword')
        return self


class ModifyUIAccountPasswordResponseBody(TeaModel):
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


class ModifyUIAccountPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyUIAccountPasswordResponseBody = None,
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
            temp_model = ModifyUIAccountPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        new_resource_group_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.new_resource_group_id = new_resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        return self


class MoveResourceGroupResponseBody(TeaModel):
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


class MoveResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MoveResourceGroupResponseBody = None,
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
            temp_model = MoveResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenBackupRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class OpenBackupResponseBody(TeaModel):
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


class OpenBackupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpenBackupResponseBody = None,
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
            temp_model = OpenBackupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PurgeInstanceRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class PurgeInstanceResponseBody(TeaModel):
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


class PurgeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PurgeInstanceResponseBody = None,
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
            temp_model = PurgeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryHBaseHaDBRequest(TeaModel):
    def __init__(
        self,
        bds_id: str = None,
    ):
        self.bds_id = bds_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.bds_id is not None:
            result['BdsId'] = self.bds_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BdsId') is not None:
            self.bds_id = m.get('BdsId')
        return self


class QueryHBaseHaDBResponseBodyClusterListClusterHaSlbConnListHaSlbConn(TeaModel):
    def __init__(
        self,
        slb_conn_addr: str = None,
        hbase_type: str = None,
        slb_type: str = None,
    ):
        self.slb_conn_addr = slb_conn_addr
        self.hbase_type = hbase_type
        self.slb_type = slb_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.slb_conn_addr is not None:
            result['SlbConnAddr'] = self.slb_conn_addr
        if self.hbase_type is not None:
            result['HbaseType'] = self.hbase_type
        if self.slb_type is not None:
            result['SlbType'] = self.slb_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlbConnAddr') is not None:
            self.slb_conn_addr = m.get('SlbConnAddr')
        if m.get('HbaseType') is not None:
            self.hbase_type = m.get('HbaseType')
        if m.get('SlbType') is not None:
            self.slb_type = m.get('SlbType')
        return self


class QueryHBaseHaDBResponseBodyClusterListClusterHaSlbConnList(TeaModel):
    def __init__(
        self,
        ha_slb_conn: List[QueryHBaseHaDBResponseBodyClusterListClusterHaSlbConnListHaSlbConn] = None,
    ):
        self.ha_slb_conn = ha_slb_conn

    def validate(self):
        if self.ha_slb_conn:
            for k in self.ha_slb_conn:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['HaSlbConn'] = []
        if self.ha_slb_conn is not None:
            for k in self.ha_slb_conn:
                result['HaSlbConn'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ha_slb_conn = []
        if m.get('HaSlbConn') is not None:
            for k in m.get('HaSlbConn'):
                temp_model = QueryHBaseHaDBResponseBodyClusterListClusterHaSlbConnListHaSlbConn()
                self.ha_slb_conn.append(temp_model.from_map(k))
        return self


class QueryHBaseHaDBResponseBodyClusterListCluster(TeaModel):
    def __init__(
        self,
        ha_name: str = None,
        bds_name: str = None,
        ha_slb_conn_list: QueryHBaseHaDBResponseBodyClusterListClusterHaSlbConnList = None,
        active_name: str = None,
        standby_name: str = None,
    ):
        self.ha_name = ha_name
        self.bds_name = bds_name
        self.ha_slb_conn_list = ha_slb_conn_list
        self.active_name = active_name
        self.standby_name = standby_name

    def validate(self):
        if self.ha_slb_conn_list:
            self.ha_slb_conn_list.validate()

    def to_map(self):
        result = dict()
        if self.ha_name is not None:
            result['HaName'] = self.ha_name
        if self.bds_name is not None:
            result['BdsName'] = self.bds_name
        if self.ha_slb_conn_list is not None:
            result['HaSlbConnList'] = self.ha_slb_conn_list.to_map()
        if self.active_name is not None:
            result['ActiveName'] = self.active_name
        if self.standby_name is not None:
            result['StandbyName'] = self.standby_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HaName') is not None:
            self.ha_name = m.get('HaName')
        if m.get('BdsName') is not None:
            self.bds_name = m.get('BdsName')
        if m.get('HaSlbConnList') is not None:
            temp_model = QueryHBaseHaDBResponseBodyClusterListClusterHaSlbConnList()
            self.ha_slb_conn_list = temp_model.from_map(m['HaSlbConnList'])
        if m.get('ActiveName') is not None:
            self.active_name = m.get('ActiveName')
        if m.get('StandbyName') is not None:
            self.standby_name = m.get('StandbyName')
        return self


class QueryHBaseHaDBResponseBodyClusterList(TeaModel):
    def __init__(
        self,
        cluster: List[QueryHBaseHaDBResponseBodyClusterListCluster] = None,
    ):
        self.cluster = cluster

    def validate(self):
        if self.cluster:
            for k in self.cluster:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Cluster'] = []
        if self.cluster is not None:
            for k in self.cluster:
                result['Cluster'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster = []
        if m.get('Cluster') is not None:
            for k in m.get('Cluster'):
                temp_model = QueryHBaseHaDBResponseBodyClusterListCluster()
                self.cluster.append(temp_model.from_map(k))
        return self


class QueryHBaseHaDBResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        cluster_list: QueryHBaseHaDBResponseBodyClusterList = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
    ):
        self.total_count = total_count
        self.cluster_list = cluster_list
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number

    def validate(self):
        if self.cluster_list:
            self.cluster_list.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.cluster_list is not None:
            result['ClusterList'] = self.cluster_list.to_map()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('ClusterList') is not None:
            temp_model = QueryHBaseHaDBResponseBodyClusterList()
            self.cluster_list = temp_model.from_map(m['ClusterList'])
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class QueryHBaseHaDBResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryHBaseHaDBResponseBody = None,
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
            temp_model = QueryHBaseHaDBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryXpackRelateDBRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        relate_db_type: str = None,
        has_single_node: bool = None,
    ):
        self.cluster_id = cluster_id
        self.relate_db_type = relate_db_type
        self.has_single_node = has_single_node

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.relate_db_type is not None:
            result['RelateDbType'] = self.relate_db_type
        if self.has_single_node is not None:
            result['HasSingleNode'] = self.has_single_node
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RelateDbType') is not None:
            self.relate_db_type = m.get('RelateDbType')
        if m.get('HasSingleNode') is not None:
            self.has_single_node = m.get('HasSingleNode')
        return self


class QueryXpackRelateDBResponseBodyClusterListCluster(TeaModel):
    def __init__(
        self,
        status: str = None,
        dbversion: str = None,
        is_related: bool = None,
        cluster_name: str = None,
        dbtype: str = None,
        lock_mode: str = None,
        cluster_id: str = None,
    ):
        self.status = status
        self.dbversion = dbversion
        self.is_related = is_related
        self.cluster_name = cluster_name
        self.dbtype = dbtype
        self.lock_mode = lock_mode
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.dbversion is not None:
            result['DBVersion'] = self.dbversion
        if self.is_related is not None:
            result['IsRelated'] = self.is_related
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.dbtype is not None:
            result['DBType'] = self.dbtype
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DBVersion') is not None:
            self.dbversion = m.get('DBVersion')
        if m.get('IsRelated') is not None:
            self.is_related = m.get('IsRelated')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class QueryXpackRelateDBResponseBodyClusterList(TeaModel):
    def __init__(
        self,
        cluster: List[QueryXpackRelateDBResponseBodyClusterListCluster] = None,
    ):
        self.cluster = cluster

    def validate(self):
        if self.cluster:
            for k in self.cluster:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Cluster'] = []
        if self.cluster is not None:
            for k in self.cluster:
                result['Cluster'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster = []
        if m.get('Cluster') is not None:
            for k in m.get('Cluster'):
                temp_model = QueryXpackRelateDBResponseBodyClusterListCluster()
                self.cluster.append(temp_model.from_map(k))
        return self


class QueryXpackRelateDBResponseBody(TeaModel):
    def __init__(
        self,
        cluster_list: QueryXpackRelateDBResponseBodyClusterList = None,
        request_id: str = None,
    ):
        self.cluster_list = cluster_list
        self.request_id = request_id

    def validate(self):
        if self.cluster_list:
            self.cluster_list.validate()

    def to_map(self):
        result = dict()
        if self.cluster_list is not None:
            result['ClusterList'] = self.cluster_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterList') is not None:
            temp_model = QueryXpackRelateDBResponseBodyClusterList()
            self.cluster_list = temp_model.from_map(m['ClusterList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryXpackRelateDBResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryXpackRelateDBResponseBody = None,
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
            temp_model = QueryXpackRelateDBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RelateDbForHBaseHaRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        ha_tables: str = None,
        ha_active_hdfs_uri: str = None,
        ha_active_hbase_fs_dir: str = None,
        ha_active_cluster_key: str = None,
        ha_active_version: str = None,
        ha_active_user: str = None,
        ha_active_password: str = None,
        ha_standby_hdfs_uri: str = None,
        ha_standby_hbase_fs_dir: str = None,
        ha_standby_cluster_key: str = None,
        ha_standby_version: str = None,
        ha_standby_user: str = None,
        ha_standby_password: str = None,
        ha_active: str = None,
        ha_standby: str = None,
        ha_active_dbtype: str = None,
        ha_standby_dbtype: str = None,
        is_active_standard: bool = None,
        is_standby_standard: bool = None,
        ha_migrate_type: str = None,
    ):
        self.cluster_id = cluster_id
        self.ha_tables = ha_tables
        self.ha_active_hdfs_uri = ha_active_hdfs_uri
        self.ha_active_hbase_fs_dir = ha_active_hbase_fs_dir
        self.ha_active_cluster_key = ha_active_cluster_key
        self.ha_active_version = ha_active_version
        self.ha_active_user = ha_active_user
        self.ha_active_password = ha_active_password
        self.ha_standby_hdfs_uri = ha_standby_hdfs_uri
        self.ha_standby_hbase_fs_dir = ha_standby_hbase_fs_dir
        self.ha_standby_cluster_key = ha_standby_cluster_key
        self.ha_standby_version = ha_standby_version
        self.ha_standby_user = ha_standby_user
        self.ha_standby_password = ha_standby_password
        self.ha_active = ha_active
        self.ha_standby = ha_standby
        self.ha_active_dbtype = ha_active_dbtype
        self.ha_standby_dbtype = ha_standby_dbtype
        self.is_active_standard = is_active_standard
        self.is_standby_standard = is_standby_standard
        self.ha_migrate_type = ha_migrate_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.ha_tables is not None:
            result['HaTables'] = self.ha_tables
        if self.ha_active_hdfs_uri is not None:
            result['HaActiveHdfsUri'] = self.ha_active_hdfs_uri
        if self.ha_active_hbase_fs_dir is not None:
            result['HaActiveHbaseFsDir'] = self.ha_active_hbase_fs_dir
        if self.ha_active_cluster_key is not None:
            result['HaActiveClusterKey'] = self.ha_active_cluster_key
        if self.ha_active_version is not None:
            result['HaActiveVersion'] = self.ha_active_version
        if self.ha_active_user is not None:
            result['HaActiveUser'] = self.ha_active_user
        if self.ha_active_password is not None:
            result['HaActivePassword'] = self.ha_active_password
        if self.ha_standby_hdfs_uri is not None:
            result['HaStandbyHdfsUri'] = self.ha_standby_hdfs_uri
        if self.ha_standby_hbase_fs_dir is not None:
            result['HaStandbyHbaseFsDir'] = self.ha_standby_hbase_fs_dir
        if self.ha_standby_cluster_key is not None:
            result['HaStandbyClusterKey'] = self.ha_standby_cluster_key
        if self.ha_standby_version is not None:
            result['HaStandbyVersion'] = self.ha_standby_version
        if self.ha_standby_user is not None:
            result['HaStandbyUser'] = self.ha_standby_user
        if self.ha_standby_password is not None:
            result['HaStandbyPassword'] = self.ha_standby_password
        if self.ha_active is not None:
            result['HaActive'] = self.ha_active
        if self.ha_standby is not None:
            result['HaStandby'] = self.ha_standby
        if self.ha_active_dbtype is not None:
            result['HaActiveDBType'] = self.ha_active_dbtype
        if self.ha_standby_dbtype is not None:
            result['HaStandbyDBType'] = self.ha_standby_dbtype
        if self.is_active_standard is not None:
            result['IsActiveStandard'] = self.is_active_standard
        if self.is_standby_standard is not None:
            result['IsStandbyStandard'] = self.is_standby_standard
        if self.ha_migrate_type is not None:
            result['HaMigrateType'] = self.ha_migrate_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('HaTables') is not None:
            self.ha_tables = m.get('HaTables')
        if m.get('HaActiveHdfsUri') is not None:
            self.ha_active_hdfs_uri = m.get('HaActiveHdfsUri')
        if m.get('HaActiveHbaseFsDir') is not None:
            self.ha_active_hbase_fs_dir = m.get('HaActiveHbaseFsDir')
        if m.get('HaActiveClusterKey') is not None:
            self.ha_active_cluster_key = m.get('HaActiveClusterKey')
        if m.get('HaActiveVersion') is not None:
            self.ha_active_version = m.get('HaActiveVersion')
        if m.get('HaActiveUser') is not None:
            self.ha_active_user = m.get('HaActiveUser')
        if m.get('HaActivePassword') is not None:
            self.ha_active_password = m.get('HaActivePassword')
        if m.get('HaStandbyHdfsUri') is not None:
            self.ha_standby_hdfs_uri = m.get('HaStandbyHdfsUri')
        if m.get('HaStandbyHbaseFsDir') is not None:
            self.ha_standby_hbase_fs_dir = m.get('HaStandbyHbaseFsDir')
        if m.get('HaStandbyClusterKey') is not None:
            self.ha_standby_cluster_key = m.get('HaStandbyClusterKey')
        if m.get('HaStandbyVersion') is not None:
            self.ha_standby_version = m.get('HaStandbyVersion')
        if m.get('HaStandbyUser') is not None:
            self.ha_standby_user = m.get('HaStandbyUser')
        if m.get('HaStandbyPassword') is not None:
            self.ha_standby_password = m.get('HaStandbyPassword')
        if m.get('HaActive') is not None:
            self.ha_active = m.get('HaActive')
        if m.get('HaStandby') is not None:
            self.ha_standby = m.get('HaStandby')
        if m.get('HaActiveDBType') is not None:
            self.ha_active_dbtype = m.get('HaActiveDBType')
        if m.get('HaStandbyDBType') is not None:
            self.ha_standby_dbtype = m.get('HaStandbyDBType')
        if m.get('IsActiveStandard') is not None:
            self.is_active_standard = m.get('IsActiveStandard')
        if m.get('IsStandbyStandard') is not None:
            self.is_standby_standard = m.get('IsStandbyStandard')
        if m.get('HaMigrateType') is not None:
            self.ha_migrate_type = m.get('HaMigrateType')
        return self


class RelateDbForHBaseHaResponseBody(TeaModel):
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


class RelateDbForHBaseHaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RelateDbForHBaseHaResponseBody = None,
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
            temp_model = RelateDbForHBaseHaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleasePublicNetworkAddressRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class ReleasePublicNetworkAddressResponseBody(TeaModel):
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


class ReleasePublicNetworkAddressResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReleasePublicNetworkAddressResponseBody = None,
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
            temp_model = ReleasePublicNetworkAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewInstanceRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        pricing_cycle: str = None,
        duration: int = None,
    ):
        self.cluster_id = cluster_id
        self.pricing_cycle = pricing_cycle
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class RenewInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: int = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class RenewInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenewInstanceResponseBody = None,
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
            temp_model = RenewInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResizeColdStorageSizeRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cold_storage_size: int = None,
    ):
        self.cluster_id = cluster_id
        self.cold_storage_size = cold_storage_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cold_storage_size is not None:
            result['ColdStorageSize'] = self.cold_storage_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ColdStorageSize') is not None:
            self.cold_storage_size = m.get('ColdStorageSize')
        return self


class ResizeColdStorageSizeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ResizeColdStorageSizeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResizeColdStorageSizeResponseBody = None,
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
            temp_model = ResizeColdStorageSizeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResizeDiskSizeRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        node_disk_size: int = None,
    ):
        self.cluster_id = cluster_id
        self.node_disk_size = node_disk_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.node_disk_size is not None:
            result['NodeDiskSize'] = self.node_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('NodeDiskSize') is not None:
            self.node_disk_size = m.get('NodeDiskSize')
        return self


class ResizeDiskSizeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ResizeDiskSizeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResizeDiskSizeResponseBody = None,
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
            temp_model = ResizeDiskSizeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResizeMultiZoneClusterDiskSizeRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        core_disk_size: int = None,
        log_disk_size: int = None,
    ):
        self.cluster_id = cluster_id
        self.core_disk_size = core_disk_size
        self.log_disk_size = log_disk_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.core_disk_size is not None:
            result['CoreDiskSize'] = self.core_disk_size
        if self.log_disk_size is not None:
            result['LogDiskSize'] = self.log_disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CoreDiskSize') is not None:
            self.core_disk_size = m.get('CoreDiskSize')
        if m.get('LogDiskSize') is not None:
            self.log_disk_size = m.get('LogDiskSize')
        return self


class ResizeMultiZoneClusterDiskSizeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ResizeMultiZoneClusterDiskSizeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResizeMultiZoneClusterDiskSizeResponseBody = None,
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
            temp_model = ResizeMultiZoneClusterDiskSizeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResizeMultiZoneClusterNodeCountRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        primary_vswitch_id: str = None,
        standby_vswitch_id: str = None,
        arbiter_vswitch_id: str = None,
        core_node_count: int = None,
        primary_core_node_count: int = None,
        standby_core_node_count: int = None,
        log_node_count: int = None,
    ):
        self.cluster_id = cluster_id
        self.primary_vswitch_id = primary_vswitch_id
        self.standby_vswitch_id = standby_vswitch_id
        self.arbiter_vswitch_id = arbiter_vswitch_id
        self.core_node_count = core_node_count
        self.primary_core_node_count = primary_core_node_count
        self.standby_core_node_count = standby_core_node_count
        self.log_node_count = log_node_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.primary_vswitch_id is not None:
            result['PrimaryVSwitchId'] = self.primary_vswitch_id
        if self.standby_vswitch_id is not None:
            result['StandbyVSwitchId'] = self.standby_vswitch_id
        if self.arbiter_vswitch_id is not None:
            result['ArbiterVSwitchId'] = self.arbiter_vswitch_id
        if self.core_node_count is not None:
            result['CoreNodeCount'] = self.core_node_count
        if self.primary_core_node_count is not None:
            result['PrimaryCoreNodeCount'] = self.primary_core_node_count
        if self.standby_core_node_count is not None:
            result['StandbyCoreNodeCount'] = self.standby_core_node_count
        if self.log_node_count is not None:
            result['LogNodeCount'] = self.log_node_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PrimaryVSwitchId') is not None:
            self.primary_vswitch_id = m.get('PrimaryVSwitchId')
        if m.get('StandbyVSwitchId') is not None:
            self.standby_vswitch_id = m.get('StandbyVSwitchId')
        if m.get('ArbiterVSwitchId') is not None:
            self.arbiter_vswitch_id = m.get('ArbiterVSwitchId')
        if m.get('CoreNodeCount') is not None:
            self.core_node_count = m.get('CoreNodeCount')
        if m.get('PrimaryCoreNodeCount') is not None:
            self.primary_core_node_count = m.get('PrimaryCoreNodeCount')
        if m.get('StandbyCoreNodeCount') is not None:
            self.standby_core_node_count = m.get('StandbyCoreNodeCount')
        if m.get('LogNodeCount') is not None:
            self.log_node_count = m.get('LogNodeCount')
        return self


class ResizeMultiZoneClusterNodeCountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ResizeMultiZoneClusterNodeCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResizeMultiZoneClusterNodeCountResponseBody = None,
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
            temp_model = ResizeMultiZoneClusterNodeCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResizeNodeCountRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        node_count: int = None,
        zone_id: str = None,
        v_switch_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.node_count = node_count
        self.zone_id = zone_id
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class ResizeNodeCountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ResizeNodeCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResizeNodeCountResponseBody = None,
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
            temp_model = ResizeNodeCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartInstanceRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        components: str = None,
    ):
        self.cluster_id = cluster_id
        self.components = components

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.components is not None:
            result['Components'] = self.components
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Components') is not None:
            self.components = m.get('Components')
        return self


class RestartInstanceResponseBody(TeaModel):
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


class RestartInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RestartInstanceResponseBody = None,
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
            temp_model = RestartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SwitchHbaseHaSlbRequest(TeaModel):
    def __init__(
        self,
        bds_id: str = None,
        ha_id: str = None,
        ha_types: str = None,
        hbase_type: str = None,
    ):
        self.bds_id = bds_id
        self.ha_id = ha_id
        self.ha_types = ha_types
        self.hbase_type = hbase_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.bds_id is not None:
            result['BdsId'] = self.bds_id
        if self.ha_id is not None:
            result['HaId'] = self.ha_id
        if self.ha_types is not None:
            result['HaTypes'] = self.ha_types
        if self.hbase_type is not None:
            result['HbaseType'] = self.hbase_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BdsId') is not None:
            self.bds_id = m.get('BdsId')
        if m.get('HaId') is not None:
            self.ha_id = m.get('HaId')
        if m.get('HaTypes') is not None:
            self.ha_types = m.get('HaTypes')
        if m.get('HbaseType') is not None:
            self.hbase_type = m.get('HbaseType')
        return self


class SwitchHbaseHaSlbResponseBody(TeaModel):
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


class SwitchHbaseHaSlbResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SwitchHbaseHaSlbResponseBody = None,
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
            temp_model = SwitchHbaseHaSlbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_id: List[str] = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.region_id = region_id
        self.resource_id = resource_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
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


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TagResourcesResponseBody = None,
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnTagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        all: bool = None,
        resource_id: List[str] = None,
        tag_key: List[str] = None,
    ):
        self.region_id = region_id
        self.all = all
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UnTagResourcesResponseBody(TeaModel):
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


class UnTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnTagResourcesResponseBody = None,
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
            temp_model = UnTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeMinorVersionRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        components: str = None,
    ):
        self.cluster_id = cluster_id
        self.components = components

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.components is not None:
            result['Components'] = self.components
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Components') is not None:
            self.components = m.get('Components')
        return self


class UpgradeMinorVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        upgrading_components: str = None,
    ):
        self.request_id = request_id
        self.upgrading_components = upgrading_components

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.upgrading_components is not None:
            result['UpgradingComponents'] = self.upgrading_components
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UpgradingComponents') is not None:
            self.upgrading_components = m.get('UpgradingComponents')
        return self


class UpgradeMinorVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpgradeMinorVersionResponseBody = None,
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
            temp_model = UpgradeMinorVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeMultiZoneClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        run_mode: str = None,
        upgrade_ins_name: str = None,
        components: str = None,
        versions: str = None,
        restart_components: str = None,
    ):
        self.cluster_id = cluster_id
        self.run_mode = run_mode
        self.upgrade_ins_name = upgrade_ins_name
        self.components = components
        self.versions = versions
        self.restart_components = restart_components

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.run_mode is not None:
            result['RunMode'] = self.run_mode
        if self.upgrade_ins_name is not None:
            result['UpgradeInsName'] = self.upgrade_ins_name
        if self.components is not None:
            result['Components'] = self.components
        if self.versions is not None:
            result['Versions'] = self.versions
        if self.restart_components is not None:
            result['RestartComponents'] = self.restart_components
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')
        if m.get('UpgradeInsName') is not None:
            self.upgrade_ins_name = m.get('UpgradeInsName')
        if m.get('Components') is not None:
            self.components = m.get('Components')
        if m.get('Versions') is not None:
            self.versions = m.get('Versions')
        if m.get('RestartComponents') is not None:
            self.restart_components = m.get('RestartComponents')
        return self


class UpgradeMultiZoneClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        upgrading_components: str = None,
    ):
        self.request_id = request_id
        self.upgrading_components = upgrading_components

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.upgrading_components is not None:
            result['UpgradingComponents'] = self.upgrading_components
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UpgradingComponents') is not None:
            self.upgrading_components = m.get('UpgradingComponents')
        return self


class UpgradeMultiZoneClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpgradeMultiZoneClusterResponseBody = None,
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
            temp_model = UpgradeMultiZoneClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class XpackRelateDBRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        db_cluster_ids: str = None,
        relate_db_type: str = None,
    ):
        self.cluster_id = cluster_id
        self.db_cluster_ids = db_cluster_ids
        self.relate_db_type = relate_db_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.db_cluster_ids is not None:
            result['DbClusterIds'] = self.db_cluster_ids
        if self.relate_db_type is not None:
            result['RelateDbType'] = self.relate_db_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DbClusterIds') is not None:
            self.db_cluster_ids = m.get('DbClusterIds')
        if m.get('RelateDbType') is not None:
            self.relate_db_type = m.get('RelateDbType')
        return self


class XpackRelateDBResponseBody(TeaModel):
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


class XpackRelateDBResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: XpackRelateDBResponseBody = None,
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
            temp_model = XpackRelateDBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


