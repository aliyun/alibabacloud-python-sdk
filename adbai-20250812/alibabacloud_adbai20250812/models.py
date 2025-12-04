# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class CreateEmbodiedAIPlatformRequestRayConfigWorkerGroups(TeaModel):
    def __init__(
        self,
        allocate_unit: str = None,
        group_name: str = None,
        max_worker_quantity: int = None,
        min_worker_quantity: int = None,
        worker_disk_capacity: str = None,
        worker_spec_name: str = None,
        worker_spec_type: str = None,
    ):
        self.allocate_unit = allocate_unit
        self.group_name = group_name
        self.max_worker_quantity = max_worker_quantity
        self.min_worker_quantity = min_worker_quantity
        self.worker_disk_capacity = worker_disk_capacity
        self.worker_spec_name = worker_spec_name
        self.worker_spec_type = worker_spec_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocate_unit is not None:
            result['AllocateUnit'] = self.allocate_unit
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.max_worker_quantity is not None:
            result['MaxWorkerQuantity'] = self.max_worker_quantity
        if self.min_worker_quantity is not None:
            result['MinWorkerQuantity'] = self.min_worker_quantity
        if self.worker_disk_capacity is not None:
            result['WorkerDiskCapacity'] = self.worker_disk_capacity
        if self.worker_spec_name is not None:
            result['WorkerSpecName'] = self.worker_spec_name
        if self.worker_spec_type is not None:
            result['WorkerSpecType'] = self.worker_spec_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocateUnit') is not None:
            self.allocate_unit = m.get('AllocateUnit')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('MaxWorkerQuantity') is not None:
            self.max_worker_quantity = m.get('MaxWorkerQuantity')
        if m.get('MinWorkerQuantity') is not None:
            self.min_worker_quantity = m.get('MinWorkerQuantity')
        if m.get('WorkerDiskCapacity') is not None:
            self.worker_disk_capacity = m.get('WorkerDiskCapacity')
        if m.get('WorkerSpecName') is not None:
            self.worker_spec_name = m.get('WorkerSpecName')
        if m.get('WorkerSpecType') is not None:
            self.worker_spec_type = m.get('WorkerSpecType')
        return self


class CreateEmbodiedAIPlatformRequestRayConfig(TeaModel):
    def __init__(
        self,
        category: str = None,
        head_spec: str = None,
        worker_groups: List[CreateEmbodiedAIPlatformRequestRayConfigWorkerGroups] = None,
    ):
        self.category = category
        self.head_spec = head_spec
        self.worker_groups = worker_groups

    def validate(self):
        if self.worker_groups:
            for k in self.worker_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.head_spec is not None:
            result['HeadSpec'] = self.head_spec
        result['WorkerGroups'] = []
        if self.worker_groups is not None:
            for k in self.worker_groups:
                result['WorkerGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('HeadSpec') is not None:
            self.head_spec = m.get('HeadSpec')
        self.worker_groups = []
        if m.get('WorkerGroups') is not None:
            for k in m.get('WorkerGroups'):
                temp_model = CreateEmbodiedAIPlatformRequestRayConfigWorkerGroups()
                self.worker_groups.append(temp_model.from_map(k))
        return self


class CreateEmbodiedAIPlatformRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        platform_name: str = None,
        ray_config: CreateEmbodiedAIPlatformRequestRayConfig = None,
        region_id: str = None,
        webserver_spec_name: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.platform_name = platform_name
        self.ray_config = ray_config
        # This parameter is required.
        self.region_id = region_id
        self.webserver_spec_name = webserver_spec_name

    def validate(self):
        if self.ray_config:
            self.ray_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.platform_name is not None:
            result['PlatformName'] = self.platform_name
        if self.ray_config is not None:
            result['RayConfig'] = self.ray_config.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.webserver_spec_name is not None:
            result['WebserverSpecName'] = self.webserver_spec_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('PlatformName') is not None:
            self.platform_name = m.get('PlatformName')
        if m.get('RayConfig') is not None:
            temp_model = CreateEmbodiedAIPlatformRequestRayConfig()
            self.ray_config = temp_model.from_map(m['RayConfig'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WebserverSpecName') is not None:
            self.webserver_spec_name = m.get('WebserverSpecName')
        return self


class CreateEmbodiedAIPlatformShrinkRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        platform_name: str = None,
        ray_config_shrink: str = None,
        region_id: str = None,
        webserver_spec_name: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.platform_name = platform_name
        self.ray_config_shrink = ray_config_shrink
        # This parameter is required.
        self.region_id = region_id
        self.webserver_spec_name = webserver_spec_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.platform_name is not None:
            result['PlatformName'] = self.platform_name
        if self.ray_config_shrink is not None:
            result['RayConfig'] = self.ray_config_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.webserver_spec_name is not None:
            result['WebserverSpecName'] = self.webserver_spec_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('PlatformName') is not None:
            self.platform_name = m.get('PlatformName')
        if m.get('RayConfig') is not None:
            self.ray_config_shrink = m.get('RayConfig')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WebserverSpecName') is not None:
            self.webserver_spec_name = m.get('WebserverSpecName')
        return self


class CreateEmbodiedAIPlatformResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateEmbodiedAIPlatformResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateEmbodiedAIPlatformResponseBody = None,
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
            temp_model = CreateEmbodiedAIPlatformResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEmbodiedAIPlatformsRequest(TeaModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        end_time: str = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        platform_name: str = None,
        region_id: str = None,
        start_time: str = None,
        state: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.end_time = end_time
        self.max_results = max_results
        self.next_token = next_token
        self.page_number = page_number
        self.page_size = page_size
        self.platform_name = platform_name
        # This parameter is required.
        self.region_id = region_id
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.start_time = start_time
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.platform_name is not None:
            result['PlatformName'] = self.platform_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlatformName') is not None:
            self.platform_name = m.get('PlatformName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeEmbodiedAIPlatformsResponseBodyPlatformsEapConfig(TeaModel):
    def __init__(
        self,
        webserver_address: str = None,
        webserver_spec_name: str = None,
    ):
        self.webserver_address = webserver_address
        self.webserver_spec_name = webserver_spec_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.webserver_address is not None:
            result['WebserverAddress'] = self.webserver_address
        if self.webserver_spec_name is not None:
            result['WebserverSpecName'] = self.webserver_spec_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WebserverAddress') is not None:
            self.webserver_address = m.get('WebserverAddress')
        if m.get('WebserverSpecName') is not None:
            self.webserver_spec_name = m.get('WebserverSpecName')
        return self


class DescribeEmbodiedAIPlatformsResponseBodyPlatformsRayConfigWorkerGroups(TeaModel):
    def __init__(
        self,
        allocate_unit: str = None,
        group_name: str = None,
        max_worker_quantity: int = None,
        min_worker_quantity: int = None,
        worker_disk_capacity: str = None,
        worker_spec_name: str = None,
        worker_spec_type: str = None,
    ):
        self.allocate_unit = allocate_unit
        self.group_name = group_name
        self.max_worker_quantity = max_worker_quantity
        self.min_worker_quantity = min_worker_quantity
        self.worker_disk_capacity = worker_disk_capacity
        self.worker_spec_name = worker_spec_name
        self.worker_spec_type = worker_spec_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocate_unit is not None:
            result['AllocateUnit'] = self.allocate_unit
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.max_worker_quantity is not None:
            result['MaxWorkerQuantity'] = self.max_worker_quantity
        if self.min_worker_quantity is not None:
            result['MinWorkerQuantity'] = self.min_worker_quantity
        if self.worker_disk_capacity is not None:
            result['WorkerDiskCapacity'] = self.worker_disk_capacity
        if self.worker_spec_name is not None:
            result['WorkerSpecName'] = self.worker_spec_name
        if self.worker_spec_type is not None:
            result['WorkerSpecType'] = self.worker_spec_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocateUnit') is not None:
            self.allocate_unit = m.get('AllocateUnit')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('MaxWorkerQuantity') is not None:
            self.max_worker_quantity = m.get('MaxWorkerQuantity')
        if m.get('MinWorkerQuantity') is not None:
            self.min_worker_quantity = m.get('MinWorkerQuantity')
        if m.get('WorkerDiskCapacity') is not None:
            self.worker_disk_capacity = m.get('WorkerDiskCapacity')
        if m.get('WorkerSpecName') is not None:
            self.worker_spec_name = m.get('WorkerSpecName')
        if m.get('WorkerSpecType') is not None:
            self.worker_spec_type = m.get('WorkerSpecType')
        return self


class DescribeEmbodiedAIPlatformsResponseBodyPlatformsRayConfig(TeaModel):
    def __init__(
        self,
        category: str = None,
        head_disk_capacity: str = None,
        head_spec: str = None,
        head_spec_type: str = None,
        ray_cluster_address: str = None,
        ray_dashboard_address: str = None,
        ray_grafana_address: str = None,
        worker_groups: List[DescribeEmbodiedAIPlatformsResponseBodyPlatformsRayConfigWorkerGroups] = None,
    ):
        self.category = category
        self.head_disk_capacity = head_disk_capacity
        self.head_spec = head_spec
        self.head_spec_type = head_spec_type
        self.ray_cluster_address = ray_cluster_address
        self.ray_dashboard_address = ray_dashboard_address
        self.ray_grafana_address = ray_grafana_address
        self.worker_groups = worker_groups

    def validate(self):
        if self.worker_groups:
            for k in self.worker_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.head_disk_capacity is not None:
            result['HeadDiskCapacity'] = self.head_disk_capacity
        if self.head_spec is not None:
            result['HeadSpec'] = self.head_spec
        if self.head_spec_type is not None:
            result['HeadSpecType'] = self.head_spec_type
        if self.ray_cluster_address is not None:
            result['RayClusterAddress'] = self.ray_cluster_address
        if self.ray_dashboard_address is not None:
            result['RayDashboardAddress'] = self.ray_dashboard_address
        if self.ray_grafana_address is not None:
            result['RayGrafanaAddress'] = self.ray_grafana_address
        result['WorkerGroups'] = []
        if self.worker_groups is not None:
            for k in self.worker_groups:
                result['WorkerGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('HeadDiskCapacity') is not None:
            self.head_disk_capacity = m.get('HeadDiskCapacity')
        if m.get('HeadSpec') is not None:
            self.head_spec = m.get('HeadSpec')
        if m.get('HeadSpecType') is not None:
            self.head_spec_type = m.get('HeadSpecType')
        if m.get('RayClusterAddress') is not None:
            self.ray_cluster_address = m.get('RayClusterAddress')
        if m.get('RayDashboardAddress') is not None:
            self.ray_dashboard_address = m.get('RayDashboardAddress')
        if m.get('RayGrafanaAddress') is not None:
            self.ray_grafana_address = m.get('RayGrafanaAddress')
        self.worker_groups = []
        if m.get('WorkerGroups') is not None:
            for k in m.get('WorkerGroups'):
                temp_model = DescribeEmbodiedAIPlatformsResponseBodyPlatformsRayConfigWorkerGroups()
                self.worker_groups.append(temp_model.from_map(k))
        return self


class DescribeEmbodiedAIPlatformsResponseBodyPlatforms(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        eap_config: DescribeEmbodiedAIPlatformsResponseBodyPlatformsEapConfig = None,
        oss_bucket_name: str = None,
        platform_name: str = None,
        ray_config: DescribeEmbodiedAIPlatformsResponseBodyPlatformsRayConfig = None,
        state: str = None,
    ):
        self.create_time = create_time
        self.eap_config = eap_config
        self.oss_bucket_name = oss_bucket_name
        self.platform_name = platform_name
        self.ray_config = ray_config
        self.state = state

    def validate(self):
        if self.eap_config:
            self.eap_config.validate()
        if self.ray_config:
            self.ray_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.eap_config is not None:
            result['EapConfig'] = self.eap_config.to_map()
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.platform_name is not None:
            result['PlatformName'] = self.platform_name
        if self.ray_config is not None:
            result['RayConfig'] = self.ray_config.to_map()
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EapConfig') is not None:
            temp_model = DescribeEmbodiedAIPlatformsResponseBodyPlatformsEapConfig()
            self.eap_config = temp_model.from_map(m['EapConfig'])
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('PlatformName') is not None:
            self.platform_name = m.get('PlatformName')
        if m.get('RayConfig') is not None:
            temp_model = DescribeEmbodiedAIPlatformsResponseBodyPlatformsRayConfig()
            self.ray_config = temp_model.from_map(m['RayConfig'])
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeEmbodiedAIPlatformsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        platforms: List[DescribeEmbodiedAIPlatformsResponseBodyPlatforms] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.page_number = page_number
        self.page_size = page_size
        self.platforms = platforms
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.platforms:
            for k in self.platforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Platforms'] = []
        if self.platforms is not None:
            for k in self.platforms:
                result['Platforms'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.platforms = []
        if m.get('Platforms') is not None:
            for k in m.get('Platforms'):
                temp_model = DescribeEmbodiedAIPlatformsResponseBodyPlatforms()
                self.platforms.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeEmbodiedAIPlatformsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEmbodiedAIPlatformsResponseBody = None,
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
            temp_model = DescribeEmbodiedAIPlatformsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


