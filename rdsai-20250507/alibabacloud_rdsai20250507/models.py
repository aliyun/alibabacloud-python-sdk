# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateAppInstanceRequestDBInstanceConfig(TeaModel):
    def __init__(
        self,
        dbinstance_class: str = None,
        dbinstance_storage: int = None,
        pay_type: str = None,
    ):
        self.dbinstance_class = dbinstance_class
        self.dbinstance_storage = dbinstance_storage
        self.pay_type = pay_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbinstance_class is not None:
            result['DBInstanceClass'] = self.dbinstance_class
        if self.dbinstance_storage is not None:
            result['DBInstanceStorage'] = self.dbinstance_storage
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceClass') is not None:
            self.dbinstance_class = m.get('DBInstanceClass')
        if m.get('DBInstanceStorage') is not None:
            self.dbinstance_storage = m.get('DBInstanceStorage')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        return self


class CreateAppInstanceRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_type: str = None,
        client_token: str = None,
        dbinstance_config: CreateAppInstanceRequestDBInstanceConfig = None,
        dbinstance_name: str = None,
        dashboard_password: str = None,
        dashboard_username: str = None,
        database_password: str = None,
        instance_class: str = None,
        public_network_access_enabled: bool = None,
        ragenabled: bool = None,
        region_id: str = None,
        v_switch_id: str = None,
    ):
        self.app_name = app_name
        self.app_type = app_type
        self.client_token = client_token
        self.dbinstance_config = dbinstance_config
        self.dbinstance_name = dbinstance_name
        self.dashboard_password = dashboard_password
        self.dashboard_username = dashboard_username
        self.database_password = database_password
        self.instance_class = instance_class
        self.public_network_access_enabled = public_network_access_enabled
        self.ragenabled = ragenabled
        self.region_id = region_id
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.dbinstance_config:
            self.dbinstance_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_config is not None:
            result['DBInstanceConfig'] = self.dbinstance_config.to_map()
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dashboard_password is not None:
            result['DashboardPassword'] = self.dashboard_password
        if self.dashboard_username is not None:
            result['DashboardUsername'] = self.dashboard_username
        if self.database_password is not None:
            result['DatabasePassword'] = self.database_password
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.public_network_access_enabled is not None:
            result['PublicNetworkAccessEnabled'] = self.public_network_access_enabled
        if self.ragenabled is not None:
            result['RAGEnabled'] = self.ragenabled
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceConfig') is not None:
            temp_model = CreateAppInstanceRequestDBInstanceConfig()
            self.dbinstance_config = temp_model.from_map(m['DBInstanceConfig'])
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DashboardPassword') is not None:
            self.dashboard_password = m.get('DashboardPassword')
        if m.get('DashboardUsername') is not None:
            self.dashboard_username = m.get('DashboardUsername')
        if m.get('DatabasePassword') is not None:
            self.database_password = m.get('DatabasePassword')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('PublicNetworkAccessEnabled') is not None:
            self.public_network_access_enabled = m.get('PublicNetworkAccessEnabled')
        if m.get('RAGEnabled') is not None:
            self.ragenabled = m.get('RAGEnabled')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateAppInstanceShrinkRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_type: str = None,
        client_token: str = None,
        dbinstance_config_shrink: str = None,
        dbinstance_name: str = None,
        dashboard_password: str = None,
        dashboard_username: str = None,
        database_password: str = None,
        instance_class: str = None,
        public_network_access_enabled: bool = None,
        ragenabled: bool = None,
        region_id: str = None,
        v_switch_id: str = None,
    ):
        self.app_name = app_name
        self.app_type = app_type
        self.client_token = client_token
        self.dbinstance_config_shrink = dbinstance_config_shrink
        self.dbinstance_name = dbinstance_name
        self.dashboard_password = dashboard_password
        self.dashboard_username = dashboard_username
        self.database_password = database_password
        self.instance_class = instance_class
        self.public_network_access_enabled = public_network_access_enabled
        self.ragenabled = ragenabled
        self.region_id = region_id
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbinstance_config_shrink is not None:
            result['DBInstanceConfig'] = self.dbinstance_config_shrink
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.dashboard_password is not None:
            result['DashboardPassword'] = self.dashboard_password
        if self.dashboard_username is not None:
            result['DashboardUsername'] = self.dashboard_username
        if self.database_password is not None:
            result['DatabasePassword'] = self.database_password
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.public_network_access_enabled is not None:
            result['PublicNetworkAccessEnabled'] = self.public_network_access_enabled
        if self.ragenabled is not None:
            result['RAGEnabled'] = self.ragenabled
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DBInstanceConfig') is not None:
            self.dbinstance_config_shrink = m.get('DBInstanceConfig')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('DashboardPassword') is not None:
            self.dashboard_password = m.get('DashboardPassword')
        if m.get('DashboardUsername') is not None:
            self.dashboard_username = m.get('DashboardUsername')
        if m.get('DatabasePassword') is not None:
            self.database_password = m.get('DatabasePassword')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('PublicNetworkAccessEnabled') is not None:
            self.public_network_access_enabled = m.get('PublicNetworkAccessEnabled')
        if m.get('RAGEnabled') is not None:
            self.ragenabled = m.get('RAGEnabled')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class CreateAppInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        request_id: str = None,
    ):
        self.instance_name = instance_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAppInstanceResponseBody = None,
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
            temp_model = CreateAppInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppInstanceRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteAppInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        request_id: str = None,
    ):
        self.instance_name = instance_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAppInstanceResponseBody = None,
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
            temp_model = DeleteAppInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppInstanceAttributeRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAppInstanceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_type: str = None,
        dbinstance_name: str = None,
        instance_class: str = None,
        instance_minor_version: str = None,
        instance_name: str = None,
        public_connection_string: str = None,
        region_id: str = None,
        request_id: str = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_connection_string: str = None,
        zone_id: str = None,
    ):
        self.app_name = app_name
        self.app_type = app_type
        self.dbinstance_name = dbinstance_name
        self.instance_class = instance_class
        self.instance_minor_version = instance_minor_version
        self.instance_name = instance_name
        self.public_connection_string = public_connection_string
        self.region_id = region_id
        self.request_id = request_id
        self.status = status
        self.v_switch_id = v_switch_id
        self.vpc_connection_string = vpc_connection_string
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_minor_version is not None:
            result['InstanceMinorVersion'] = self.instance_minor_version
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.public_connection_string is not None:
            result['PublicConnectionString'] = self.public_connection_string
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_connection_string is not None:
            result['VpcConnectionString'] = self.vpc_connection_string
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceMinorVersion') is not None:
            self.instance_minor_version = m.get('InstanceMinorVersion')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PublicConnectionString') is not None:
            self.public_connection_string = m.get('PublicConnectionString')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcConnectionString') is not None:
            self.vpc_connection_string = m.get('VpcConnectionString')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeAppInstanceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAppInstanceAttributeResponseBody = None,
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
            temp_model = DescribeAppInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppInstancesRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        dbinstance_name: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
    ):
        self.app_type = app_type
        self.dbinstance_name = dbinstance_name
        self.page_number = page_number
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeAppInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_type: str = None,
        dbinstance_name: str = None,
        instance_class: str = None,
        instance_minor_version: str = None,
        instance_name: str = None,
        public_connection_string: str = None,
        region_id: str = None,
        status: str = None,
        v_switch_id: str = None,
        vpc_connection_string: str = None,
    ):
        self.app_name = app_name
        self.app_type = app_type
        self.dbinstance_name = dbinstance_name
        self.instance_class = instance_class
        self.instance_minor_version = instance_minor_version
        self.instance_name = instance_name
        self.public_connection_string = public_connection_string
        self.region_id = region_id
        self.status = status
        self.v_switch_id = v_switch_id
        self.vpc_connection_string = vpc_connection_string

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class
        if self.instance_minor_version is not None:
            result['InstanceMinorVersion'] = self.instance_minor_version
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.public_connection_string is not None:
            result['PublicConnectionString'] = self.public_connection_string
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_connection_string is not None:
            result['VpcConnectionString'] = self.vpc_connection_string
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')
        if m.get('InstanceMinorVersion') is not None:
            self.instance_minor_version = m.get('InstanceMinorVersion')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('PublicConnectionString') is not None:
            self.public_connection_string = m.get('PublicConnectionString')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcConnectionString') is not None:
            self.vpc_connection_string = m.get('VpcConnectionString')
        return self


class DescribeAppInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[DescribeAppInstancesResponseBodyInstances] = None,
        max_results: int = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.instances = instances
        self.max_results = max_results
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeAppInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeAppInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAppInstancesResponseBody = None,
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
            temp_model = DescribeAppInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceAuthInfoRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInstanceAuthInfoResponseBodyApiKeys(TeaModel):
    def __init__(
        self,
        anon_key: str = None,
        service_key: str = None,
    ):
        # Supabase ANON_KEY
        self.anon_key = anon_key
        # Supabase SERVICE_ROLE_KEY
        self.service_key = service_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anon_key is not None:
            result['AnonKey'] = self.anon_key
        if self.service_key is not None:
            result['ServiceKey'] = self.service_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnonKey') is not None:
            self.anon_key = m.get('AnonKey')
        if m.get('ServiceKey') is not None:
            self.service_key = m.get('ServiceKey')
        return self


class DescribeInstanceAuthInfoResponseBody(TeaModel):
    def __init__(
        self,
        api_keys: DescribeInstanceAuthInfoResponseBodyApiKeys = None,
        jwt_secret: str = None,
        request_id: str = None,
    ):
        # API Keys
        self.api_keys = api_keys
        self.jwt_secret = jwt_secret
        self.request_id = request_id

    def validate(self):
        if self.api_keys:
            self.api_keys.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_keys is not None:
            result['ApiKeys'] = self.api_keys.to_map()
        if self.jwt_secret is not None:
            result['JwtSecret'] = self.jwt_secret
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKeys') is not None:
            temp_model = DescribeInstanceAuthInfoResponseBodyApiKeys()
            self.api_keys = temp_model.from_map(m['ApiKeys'])
        if m.get('JwtSecret') is not None:
            self.jwt_secret = m.get('JwtSecret')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceAuthInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceAuthInfoResponseBody = None,
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
            temp_model = DescribeInstanceAuthInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceEndpointsRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInstanceEndpointsResponseBodyInstanceEndpoints(TeaModel):
    def __init__(
        self,
        connection_string: str = None,
        ip: str = None,
        ip_type: str = None,
        port: str = None,
    ):
        self.connection_string = connection_string
        self.ip = ip
        self.ip_type = ip_type
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string
        if self.ip is not None:
            result['IP'] = self.ip
        if self.ip_type is not None:
            result['IpType'] = self.ip_type
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class DescribeInstanceEndpointsResponseBody(TeaModel):
    def __init__(
        self,
        instance_endpoints: List[DescribeInstanceEndpointsResponseBodyInstanceEndpoints] = None,
        instance_name: str = None,
        request_id: str = None,
    ):
        self.instance_endpoints = instance_endpoints
        self.instance_name = instance_name
        self.request_id = request_id

    def validate(self):
        if self.instance_endpoints:
            for k in self.instance_endpoints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceEndpoints'] = []
        if self.instance_endpoints is not None:
            for k in self.instance_endpoints:
                result['InstanceEndpoints'].append(k.to_map() if k else None)
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_endpoints = []
        if m.get('InstanceEndpoints') is not None:
            for k in m.get('InstanceEndpoints'):
                temp_model = DescribeInstanceEndpointsResponseBodyInstanceEndpoints()
                self.instance_endpoints.append(temp_model.from_map(k))
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceEndpointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceEndpointsResponseBody = None,
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
            temp_model = DescribeInstanceEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceIpWhitelistRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        region_id: str = None,
    ):
        self.instance_name = instance_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInstanceIpWhitelistResponseBodyIpWhiteListGroups(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        ip_whitelist: str = None,
    ):
        self.group_name = group_name
        self.ip_whitelist = ip_whitelist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.ip_whitelist is not None:
            result['IpWhitelist'] = self.ip_whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('IpWhitelist') is not None:
            self.ip_whitelist = m.get('IpWhitelist')
        return self


class DescribeInstanceIpWhitelistResponseBody(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        ip_white_list_groups: List[DescribeInstanceIpWhitelistResponseBodyIpWhiteListGroups] = None,
        request_id: str = None,
    ):
        self.instance_name = instance_name
        self.ip_white_list_groups = ip_white_list_groups
        self.request_id = request_id

    def validate(self):
        if self.ip_white_list_groups:
            for k in self.ip_white_list_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        result['IpWhiteListGroups'] = []
        if self.ip_white_list_groups is not None:
            for k in self.ip_white_list_groups:
                result['IpWhiteListGroups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        self.ip_white_list_groups = []
        if m.get('IpWhiteListGroups') is not None:
            for k in m.get('IpWhiteListGroups'):
                temp_model = DescribeInstanceIpWhitelistResponseBodyIpWhiteListGroups()
                self.ip_white_list_groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceIpWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInstanceIpWhitelistResponseBody = None,
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
            temp_model = DescribeInstanceIpWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceIpWhitelistRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        group_name: str = None,
        instance_name: str = None,
        ip_whitelist: str = None,
        modify_mode: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.group_name = group_name
        self.instance_name = instance_name
        self.ip_whitelist = ip_whitelist
        self.modify_mode = modify_mode
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.ip_whitelist is not None:
            result['IpWhitelist'] = self.ip_whitelist
        if self.modify_mode is not None:
            result['ModifyMode'] = self.modify_mode
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('IpWhitelist') is not None:
            self.ip_whitelist = m.get('IpWhitelist')
        if m.get('ModifyMode') is not None:
            self.modify_mode = m.get('ModifyMode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyInstanceIpWhitelistResponseBody(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        request_id: str = None,
    ):
        self.instance_name = instance_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyInstanceIpWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyInstanceIpWhitelistResponseBody = None,
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
            temp_model = ModifyInstanceIpWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


