# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListTimingSyntheticTasksResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListTimingSyntheticTasksResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The returned struct.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListTimingSyntheticTasksResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListTimingSyntheticTasksResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListTimingSyntheticTasksResponseBodyDataItems] = None,
        page: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # The queried tasks.
        self.items = items
        # The page number.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of tasks.
        self.total = total

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListTimingSyntheticTasksResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListTimingSyntheticTasksResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        common_setting: main_models.ListTimingSyntheticTasksResponseBodyDataItemsCommonSetting = None,
        frequency: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        monitor_category: int = None,
        monitor_num: str = None,
        name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[main_models.ListTimingSyntheticTasksResponseBodyDataItemsTags] = None,
        task_id: str = None,
        task_type: int = None,
        url: str = None,
    ):
        # The general settings.
        self.common_setting = common_setting
        # The detection frequency. Valid values: 1m, 5m, 10m, 15m, 20m, 30m, 1h, 2h, 3h, 4h, 6h, 8h, 12h, and 24h.
        self.frequency = frequency
        # The time when the task was created.
        self.gmt_create = gmt_create
        # The time when the task was modified.
        self.gmt_modified = gmt_modified
        # The detection point type. 1: PC. 2: mobile device.
        self.monitor_category = monitor_category
        # The number of detection points.
        self.monitor_num = monitor_num
        # The task name.
        self.name = name
        # The region ID.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The task status. CREATING: The task is being created. RUNNING: The task is running. PARTIAL_RUNNING: The task is partially running. STOP: The task is stopped. LIMIT_STOP: The task is stopped due to quota limit. EXCEPTION: The task is abnormal. DELETE: The task is deleted. DELETE_EXCEPTION: An exception occurs while deleting the task.
        self.status = status
        # The tags.
        self.tags = tags
        # The ID of the synthetic monitoring task.
        self.task_id = task_id
        # The type of the task. Valid values:
        # 
        # 1: ICMP. 2: TCP. 3: DNS. 4: HTTP. 5: website speed. 6: file download.
        self.task_type = task_type
        # The URL for synthetic monitoring.
        self.url = url

    def validate(self):
        if self.common_setting:
            self.common_setting.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.common_setting is not None:
            result['CommonSetting'] = self.common_setting.to_map()

        if self.frequency is not None:
            result['Frequency'] = self.frequency

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.monitor_category is not None:
            result['MonitorCategory'] = self.monitor_category

        if self.monitor_num is not None:
            result['MonitorNum'] = self.monitor_num

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommonSetting') is not None:
            temp_model = main_models.ListTimingSyntheticTasksResponseBodyDataItemsCommonSetting()
            self.common_setting = temp_model.from_map(m.get('CommonSetting'))

        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('MonitorCategory') is not None:
            self.monitor_category = m.get('MonitorCategory')

        if m.get('MonitorNum') is not None:
            self.monitor_num = m.get('MonitorNum')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListTimingSyntheticTasksResponseBodyDataItemsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class ListTimingSyntheticTasksResponseBodyDataItemsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class ListTimingSyntheticTasksResponseBodyDataItemsCommonSetting(DaraModel):
    def __init__(
        self,
        custom_host: main_models.ListTimingSyntheticTasksResponseBodyDataItemsCommonSettingCustomHost = None,
        custom_prometheus_setting: main_models.ListTimingSyntheticTasksResponseBodyDataItemsCommonSettingCustomPrometheusSetting = None,
        custom_vpcsetting: main_models.ListTimingSyntheticTasksResponseBodyDataItemsCommonSettingCustomVPCSetting = None,
        ip_type: int = None,
        is_open_trace: bool = None,
        monitor_samples: int = None,
        trace_client_type: int = None,
        xtrace_region: str = None,
    ):
        # The custom host settings.
        self.custom_host = custom_host
        # A reserved field.
        self.custom_prometheus_setting = custom_prometheus_setting
        # The information about the virtual private cloud (VPC). If the destination URL is an Alibaba Cloud internal endpoint, you need to configure a VPC.
        self.custom_vpcsetting = custom_vpcsetting
        # The IP version. Valid values:
        # 
        # *   0: A version is automatically selected.
        # *   1: IPv4.
        # *   2: IPv6.
        self.ip_type = ip_type
        # Indicates whether tracing is enabled.
        self.is_open_trace = is_open_trace
        # Indicates whether monitoring samples are evenly distributed. Valid values:
        # 
        # *   0: No
        # *   1: Yes
        self.monitor_samples = monitor_samples
        # The type of the client for tracing. Valid values:
        # 
        # *   0: ARMS agent
        # *   1: OpenTelemetry
        # *   2: Jaeger
        self.trace_client_type = trace_client_type
        # The region to which trace data is reported.
        self.xtrace_region = xtrace_region

    def validate(self):
        if self.custom_host:
            self.custom_host.validate()
        if self.custom_prometheus_setting:
            self.custom_prometheus_setting.validate()
        if self.custom_vpcsetting:
            self.custom_vpcsetting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_host is not None:
            result['CustomHost'] = self.custom_host.to_map()

        if self.custom_prometheus_setting is not None:
            result['CustomPrometheusSetting'] = self.custom_prometheus_setting.to_map()

        if self.custom_vpcsetting is not None:
            result['CustomVPCSetting'] = self.custom_vpcsetting.to_map()

        if self.ip_type is not None:
            result['IpType'] = self.ip_type

        if self.is_open_trace is not None:
            result['IsOpenTrace'] = self.is_open_trace

        if self.monitor_samples is not None:
            result['MonitorSamples'] = self.monitor_samples

        if self.trace_client_type is not None:
            result['TraceClientType'] = self.trace_client_type

        if self.xtrace_region is not None:
            result['XtraceRegion'] = self.xtrace_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomHost') is not None:
            temp_model = main_models.ListTimingSyntheticTasksResponseBodyDataItemsCommonSettingCustomHost()
            self.custom_host = temp_model.from_map(m.get('CustomHost'))

        if m.get('CustomPrometheusSetting') is not None:
            temp_model = main_models.ListTimingSyntheticTasksResponseBodyDataItemsCommonSettingCustomPrometheusSetting()
            self.custom_prometheus_setting = temp_model.from_map(m.get('CustomPrometheusSetting'))

        if m.get('CustomVPCSetting') is not None:
            temp_model = main_models.ListTimingSyntheticTasksResponseBodyDataItemsCommonSettingCustomVPCSetting()
            self.custom_vpcsetting = temp_model.from_map(m.get('CustomVPCSetting'))

        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')

        if m.get('IsOpenTrace') is not None:
            self.is_open_trace = m.get('IsOpenTrace')

        if m.get('MonitorSamples') is not None:
            self.monitor_samples = m.get('MonitorSamples')

        if m.get('TraceClientType') is not None:
            self.trace_client_type = m.get('TraceClientType')

        if m.get('XtraceRegion') is not None:
            self.xtrace_region = m.get('XtraceRegion')

        return self

class ListTimingSyntheticTasksResponseBodyDataItemsCommonSettingCustomVPCSetting(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        secure_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The ID of the security group to which the client belongs. The security group specifies the inbound and outbound rules of the client for the VPC. You need to allow the security group to which the client belongs to access the security group to which the VPC belongs. Otherwise, the client cannot access resources in the VPC.
        self.secure_group_id = secure_group_id
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.secure_group_id is not None:
            result['SecureGroupId'] = self.secure_group_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SecureGroupId') is not None:
            self.secure_group_id = m.get('SecureGroupId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class ListTimingSyntheticTasksResponseBodyDataItemsCommonSettingCustomPrometheusSetting(DaraModel):
    def __init__(
        self,
        prometheus_cluster_id: str = None,
        prometheus_cluster_region: str = None,
        prometheus_labels: Dict[str, str] = None,
    ):
        # A reserved field.
        self.prometheus_cluster_id = prometheus_cluster_id
        # A reserved field.
        self.prometheus_cluster_region = prometheus_cluster_region
        # A reserved field.
        self.prometheus_labels = prometheus_labels

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prometheus_cluster_id is not None:
            result['PrometheusClusterId'] = self.prometheus_cluster_id

        if self.prometheus_cluster_region is not None:
            result['PrometheusClusterRegion'] = self.prometheus_cluster_region

        if self.prometheus_labels is not None:
            result['PrometheusLabels'] = self.prometheus_labels

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrometheusClusterId') is not None:
            self.prometheus_cluster_id = m.get('PrometheusClusterId')

        if m.get('PrometheusClusterRegion') is not None:
            self.prometheus_cluster_region = m.get('PrometheusClusterRegion')

        if m.get('PrometheusLabels') is not None:
            self.prometheus_labels = m.get('PrometheusLabels')

        return self

class ListTimingSyntheticTasksResponseBodyDataItemsCommonSettingCustomHost(DaraModel):
    def __init__(
        self,
        hosts: List[main_models.ListTimingSyntheticTasksResponseBodyDataItemsCommonSettingCustomHostHosts] = None,
        select_type: int = None,
    ):
        # The custom host settings.
        self.hosts = hosts
        # The selection mode. Valid values:
        # 
        # *   0: random
        # *   1: polling
        self.select_type = select_type

    def validate(self):
        if self.hosts:
            for v1 in self.hosts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Hosts'] = []
        if self.hosts is not None:
            for k1 in self.hosts:
                result['Hosts'].append(k1.to_map() if k1 else None)

        if self.select_type is not None:
            result['SelectType'] = self.select_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hosts = []
        if m.get('Hosts') is not None:
            for k1 in m.get('Hosts'):
                temp_model = main_models.ListTimingSyntheticTasksResponseBodyDataItemsCommonSettingCustomHostHosts()
                self.hosts.append(temp_model.from_map(k1))

        if m.get('SelectType') is not None:
            self.select_type = m.get('SelectType')

        return self

class ListTimingSyntheticTasksResponseBodyDataItemsCommonSettingCustomHostHosts(DaraModel):
    def __init__(
        self,
        domain: str = None,
        ip_type: int = None,
        ips: List[str] = None,
    ):
        # The destination domain name.
        self.domain = domain
        # The IP version. Valid values:
        # 
        # *   0: A version is automatically selected.
        # *   1: IPv4.
        # *   2: IPv6.
        self.ip_type = ip_type
        # The IP address.
        self.ips = ips

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.ip_type is not None:
            result['IpType'] = self.ip_type

        if self.ips is not None:
            result['Ips'] = self.ips

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')

        if m.get('Ips') is not None:
            self.ips = m.get('Ips')

        return self

