# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListClustersResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListClustersResponseBodyData] = None,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The details of the data.
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The HTTP status code returned.
        self.http_code = http_code
        # The message returned.
        self.message = message
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success
        # The total number of returned instances.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

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
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListClustersResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

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

class ListClustersResponseBodyData(DaraModel):
    def __init__(
        self,
        app_version: str = None,
        can_update: bool = None,
        charge_type: str = None,
        cluster_alias_name: str = None,
        cluster_name: str = None,
        cluster_type: str = None,
        create_time: str = None,
        end_date: str = None,
        init_status: str = None,
        instance_count: int = None,
        instance_id: str = None,
        internet_address: str = None,
        internet_domain: str = None,
        intranet_address: str = None,
        intranet_domain: str = None,
        maintenance_period: main_models.ListClustersResponseBodyDataMaintenancePeriod = None,
        mse_version: str = None,
        resource_group_id: str = None,
        tags: Dict[str, Any] = None,
        version_code: str = None,
        version_lifecycle: str = None,
        vpc_id: str = None,
    ):
        # The application version.
        self.app_version = app_version
        # Indicates whether the instance can be upgraded.
        self.can_update = can_update
        # The billing method, such as subscription or pay-as-you-go.
        self.charge_type = charge_type
        # The alias of the cluster.
        self.cluster_alias_name = cluster_alias_name
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The type of the cluster. Valid values: ZooKeeper, Nacos-Ans, and Eureka.
        self.cluster_type = cluster_type
        # The time when the cluster was created.
        self.create_time = create_time
        # The time when the cluster expires.
        self.end_date = end_date
        # The initialization status of the instance.
        self.init_status = init_status
        # The number of clusters.
        self.instance_count = instance_count
        # The instance ID.
        self.instance_id = instance_id
        # The public IP address.
        self.internet_address = internet_address
        # The public endpoint.
        self.internet_domain = internet_domain
        # The internal IP address.
        self.intranet_address = intranet_address
        # The internal endpoint.
        self.intranet_domain = intranet_domain
        self.maintenance_period = maintenance_period
        # The edition of the cluster.
        self.mse_version = mse_version
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The tags that are attached to the instance.
        self.tags = tags
        # The version information.
        self.version_code = version_code
        self.version_lifecycle = version_lifecycle
        self.vpc_id = vpc_id

    def validate(self):
        if self.maintenance_period:
            self.maintenance_period.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_version is not None:
            result['AppVersion'] = self.app_version

        if self.can_update is not None:
            result['CanUpdate'] = self.can_update

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cluster_alias_name is not None:
            result['ClusterAliasName'] = self.cluster_alias_name

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.init_status is not None:
            result['InitStatus'] = self.init_status

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.internet_address is not None:
            result['InternetAddress'] = self.internet_address

        if self.internet_domain is not None:
            result['InternetDomain'] = self.internet_domain

        if self.intranet_address is not None:
            result['IntranetAddress'] = self.intranet_address

        if self.intranet_domain is not None:
            result['IntranetDomain'] = self.intranet_domain

        if self.maintenance_period is not None:
            result['MaintenancePeriod'] = self.maintenance_period.to_map()

        if self.mse_version is not None:
            result['MseVersion'] = self.mse_version

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.version_code is not None:
            result['VersionCode'] = self.version_code

        if self.version_lifecycle is not None:
            result['VersionLifecycle'] = self.version_lifecycle

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')

        if m.get('CanUpdate') is not None:
            self.can_update = m.get('CanUpdate')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('ClusterAliasName') is not None:
            self.cluster_alias_name = m.get('ClusterAliasName')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('InitStatus') is not None:
            self.init_status = m.get('InitStatus')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InternetAddress') is not None:
            self.internet_address = m.get('InternetAddress')

        if m.get('InternetDomain') is not None:
            self.internet_domain = m.get('InternetDomain')

        if m.get('IntranetAddress') is not None:
            self.intranet_address = m.get('IntranetAddress')

        if m.get('IntranetDomain') is not None:
            self.intranet_domain = m.get('IntranetDomain')

        if m.get('MaintenancePeriod') is not None:
            temp_model = main_models.ListClustersResponseBodyDataMaintenancePeriod()
            self.maintenance_period = temp_model.from_map(m.get('MaintenancePeriod'))

        if m.get('MseVersion') is not None:
            self.mse_version = m.get('MseVersion')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('VersionCode') is not None:
            self.version_code = m.get('VersionCode')

        if m.get('VersionLifecycle') is not None:
            self.version_lifecycle = m.get('VersionLifecycle')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class ListClustersResponseBodyDataMaintenancePeriod(DaraModel):
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

