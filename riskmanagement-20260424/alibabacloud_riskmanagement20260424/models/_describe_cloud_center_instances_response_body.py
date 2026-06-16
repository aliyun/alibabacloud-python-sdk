# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudCenterInstancesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeCloudCenterInstancesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
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
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

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
            temp_model = main_models.DescribeCloudCenterInstancesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeCloudCenterInstancesResponseBodyData(DaraModel):
    def __init__(
        self,
        body: main_models.DescribeCloudCenterInstancesResponseBodyDataBody = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['Body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            temp_model = main_models.DescribeCloudCenterInstancesResponseBodyDataBody()
            self.body = temp_model.from_map(m.get('Body'))

        return self

class DescribeCloudCenterInstancesResponseBodyDataBody(DaraModel):
    def __init__(
        self,
        instances: List[main_models.DescribeCloudCenterInstancesResponseBodyDataBodyInstances] = None,
        page_info: main_models.DescribeCloudCenterInstancesResponseBodyDataBodyPageInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.instances = instances
        self.page_info = page_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.DescribeCloudCenterInstancesResponseBodyDataBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeCloudCenterInstancesResponseBodyDataBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeCloudCenterInstancesResponseBodyDataBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        next_token: str = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.count = count
        self.current_page = current_page
        self.next_token = next_token
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCloudCenterInstancesResponseBodyDataBodyInstances(DaraModel):
    def __init__(
        self,
        alarm_status: str = None,
        app_id: str = None,
        app_name: str = None,
        asset_type: str = None,
        asset_type_name: str = None,
        auth_modify_time: int = None,
        auth_version: int = None,
        auth_version_name: str = None,
        bind: bool = None,
        bind_file_protect_type: str = None,
        client_status: str = None,
        client_sub_status: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cores: int = None,
        cpu_info: str = None,
        created_time: int = None,
        exposed_status: int = None,
        flag: int = None,
        flag_name: str = None,
        group_id: int = None,
        group_trace: str = None,
        has_container: str = None,
        hc_status: str = None,
        health_check_count: int = None,
        importance: int = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        ip: str = None,
        ip_list_string: str = None,
        kernel: str = None,
        last_login_timestamp: int = None,
        mac_list_string: str = None,
        mem: str = None,
        namespace: str = None,
        os: str = None,
        os_name: str = None,
        pod_count: int = None,
        post_paid_flag: int = None,
        region: str = None,
        region_id: str = None,
        region_name: str = None,
        risk_count: str = None,
        risk_status: str = None,
        safe_event_count: str = None,
        service_id: str = None,
        status: str = None,
        tag: str = None,
        tag_id: str = None,
        tag_resources: str = None,
        uuid: str = None,
        vendor: int = None,
        vendor_name: str = None,
        vendor_uid: str = None,
        vendor_user_name: str = None,
        vpc_instance_id: str = None,
        vul_count: int = None,
        vul_status: str = None,
    ):
        self.alarm_status = alarm_status
        self.app_id = app_id
        self.app_name = app_name
        self.asset_type = asset_type
        self.asset_type_name = asset_type_name
        self.auth_modify_time = auth_modify_time
        self.auth_version = auth_version
        self.auth_version_name = auth_version_name
        self.bind = bind
        self.bind_file_protect_type = bind_file_protect_type
        self.client_status = client_status
        self.client_sub_status = client_sub_status
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.cores = cores
        self.cpu_info = cpu_info
        self.created_time = created_time
        self.exposed_status = exposed_status
        self.flag = flag
        self.flag_name = flag_name
        self.group_id = group_id
        self.group_trace = group_trace
        self.has_container = has_container
        self.hc_status = hc_status
        self.health_check_count = health_check_count
        self.importance = importance
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.internet_ip = internet_ip
        self.intranet_ip = intranet_ip
        self.ip = ip
        self.ip_list_string = ip_list_string
        self.kernel = kernel
        self.last_login_timestamp = last_login_timestamp
        self.mac_list_string = mac_list_string
        self.mem = mem
        self.namespace = namespace
        self.os = os
        self.os_name = os_name
        self.pod_count = pod_count
        self.post_paid_flag = post_paid_flag
        self.region = region
        self.region_id = region_id
        self.region_name = region_name
        self.risk_count = risk_count
        self.risk_status = risk_status
        self.safe_event_count = safe_event_count
        self.service_id = service_id
        self.status = status
        self.tag = tag
        self.tag_id = tag_id
        self.tag_resources = tag_resources
        self.uuid = uuid
        self.vendor = vendor
        self.vendor_name = vendor_name
        self.vendor_uid = vendor_uid
        self.vendor_user_name = vendor_user_name
        self.vpc_instance_id = vpc_instance_id
        self.vul_count = vul_count
        self.vul_status = vul_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_status is not None:
            result['AlarmStatus'] = self.alarm_status

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.asset_type_name is not None:
            result['AssetTypeName'] = self.asset_type_name

        if self.auth_modify_time is not None:
            result['AuthModifyTime'] = self.auth_modify_time

        if self.auth_version is not None:
            result['AuthVersion'] = self.auth_version

        if self.auth_version_name is not None:
            result['AuthVersionName'] = self.auth_version_name

        if self.bind is not None:
            result['Bind'] = self.bind

        if self.bind_file_protect_type is not None:
            result['BindFileProtectType'] = self.bind_file_protect_type

        if self.client_status is not None:
            result['ClientStatus'] = self.client_status

        if self.client_sub_status is not None:
            result['ClientSubStatus'] = self.client_sub_status

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cores is not None:
            result['Cores'] = self.cores

        if self.cpu_info is not None:
            result['CpuInfo'] = self.cpu_info

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.exposed_status is not None:
            result['ExposedStatus'] = self.exposed_status

        if self.flag is not None:
            result['Flag'] = self.flag

        if self.flag_name is not None:
            result['FlagName'] = self.flag_name

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_trace is not None:
            result['GroupTrace'] = self.group_trace

        if self.has_container is not None:
            result['HasContainer'] = self.has_container

        if self.hc_status is not None:
            result['HcStatus'] = self.hc_status

        if self.health_check_count is not None:
            result['HealthCheckCount'] = self.health_check_count

        if self.importance is not None:
            result['Importance'] = self.importance

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.ip_list_string is not None:
            result['IpListString'] = self.ip_list_string

        if self.kernel is not None:
            result['Kernel'] = self.kernel

        if self.last_login_timestamp is not None:
            result['LastLoginTimestamp'] = self.last_login_timestamp

        if self.mac_list_string is not None:
            result['MacListString'] = self.mac_list_string

        if self.mem is not None:
            result['Mem'] = self.mem

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.os is not None:
            result['Os'] = self.os

        if self.os_name is not None:
            result['OsName'] = self.os_name

        if self.pod_count is not None:
            result['PodCount'] = self.pod_count

        if self.post_paid_flag is not None:
            result['PostPaidFlag'] = self.post_paid_flag

        if self.region is not None:
            result['Region'] = self.region

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        if self.risk_count is not None:
            result['RiskCount'] = self.risk_count

        if self.risk_status is not None:
            result['RiskStatus'] = self.risk_status

        if self.safe_event_count is not None:
            result['SafeEventCount'] = self.safe_event_count

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.status is not None:
            result['Status'] = self.status

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        if self.vendor_name is not None:
            result['VendorName'] = self.vendor_name

        if self.vendor_uid is not None:
            result['VendorUid'] = self.vendor_uid

        if self.vendor_user_name is not None:
            result['VendorUserName'] = self.vendor_user_name

        if self.vpc_instance_id is not None:
            result['VpcInstanceId'] = self.vpc_instance_id

        if self.vul_count is not None:
            result['VulCount'] = self.vul_count

        if self.vul_status is not None:
            result['VulStatus'] = self.vul_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmStatus') is not None:
            self.alarm_status = m.get('AlarmStatus')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('AssetTypeName') is not None:
            self.asset_type_name = m.get('AssetTypeName')

        if m.get('AuthModifyTime') is not None:
            self.auth_modify_time = m.get('AuthModifyTime')

        if m.get('AuthVersion') is not None:
            self.auth_version = m.get('AuthVersion')

        if m.get('AuthVersionName') is not None:
            self.auth_version_name = m.get('AuthVersionName')

        if m.get('Bind') is not None:
            self.bind = m.get('Bind')

        if m.get('BindFileProtectType') is not None:
            self.bind_file_protect_type = m.get('BindFileProtectType')

        if m.get('ClientStatus') is not None:
            self.client_status = m.get('ClientStatus')

        if m.get('ClientSubStatus') is not None:
            self.client_sub_status = m.get('ClientSubStatus')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('Cores') is not None:
            self.cores = m.get('Cores')

        if m.get('CpuInfo') is not None:
            self.cpu_info = m.get('CpuInfo')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('ExposedStatus') is not None:
            self.exposed_status = m.get('ExposedStatus')

        if m.get('Flag') is not None:
            self.flag = m.get('Flag')

        if m.get('FlagName') is not None:
            self.flag_name = m.get('FlagName')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupTrace') is not None:
            self.group_trace = m.get('GroupTrace')

        if m.get('HasContainer') is not None:
            self.has_container = m.get('HasContainer')

        if m.get('HcStatus') is not None:
            self.hc_status = m.get('HcStatus')

        if m.get('HealthCheckCount') is not None:
            self.health_check_count = m.get('HealthCheckCount')

        if m.get('Importance') is not None:
            self.importance = m.get('Importance')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('IpListString') is not None:
            self.ip_list_string = m.get('IpListString')

        if m.get('Kernel') is not None:
            self.kernel = m.get('Kernel')

        if m.get('LastLoginTimestamp') is not None:
            self.last_login_timestamp = m.get('LastLoginTimestamp')

        if m.get('MacListString') is not None:
            self.mac_list_string = m.get('MacListString')

        if m.get('Mem') is not None:
            self.mem = m.get('Mem')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('OsName') is not None:
            self.os_name = m.get('OsName')

        if m.get('PodCount') is not None:
            self.pod_count = m.get('PodCount')

        if m.get('PostPaidFlag') is not None:
            self.post_paid_flag = m.get('PostPaidFlag')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        if m.get('RiskCount') is not None:
            self.risk_count = m.get('RiskCount')

        if m.get('RiskStatus') is not None:
            self.risk_status = m.get('RiskStatus')

        if m.get('SafeEventCount') is not None:
            self.safe_event_count = m.get('SafeEventCount')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        if m.get('TagResources') is not None:
            self.tag_resources = m.get('TagResources')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        if m.get('VendorName') is not None:
            self.vendor_name = m.get('VendorName')

        if m.get('VendorUid') is not None:
            self.vendor_uid = m.get('VendorUid')

        if m.get('VendorUserName') is not None:
            self.vendor_user_name = m.get('VendorUserName')

        if m.get('VpcInstanceId') is not None:
            self.vpc_instance_id = m.get('VpcInstanceId')

        if m.get('VulCount') is not None:
            self.vul_count = m.get('VulCount')

        if m.get('VulStatus') is not None:
            self.vul_status = m.get('VulStatus')

        return self

