# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AllocatePublicContactPointsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        data_center_id: str = None,
        client_token: str = None,
    ):
        self.cluster_id = cluster_id
        self.data_center_id = data_center_id
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class AllocatePublicContactPointsResponseBody(TeaModel):
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


class AllocatePublicContactPointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AllocatePublicContactPointsResponseBody = None,
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
            temp_model = AllocatePublicContactPointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBackupPlanRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        data_center_id: str = None,
        backup_time: str = None,
        backup_period: str = None,
        retention_period: int = None,
        active: bool = None,
        client_token: str = None,
    ):
        self.cluster_id = cluster_id
        self.data_center_id = data_center_id
        self.backup_time = backup_time
        self.backup_period = backup_period
        self.retention_period = retention_period
        self.active = active
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.backup_time is not None:
            result['BackupTime'] = self.backup_time
        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period
        if self.retention_period is not None:
            result['RetentionPeriod'] = self.retention_period
        if self.active is not None:
            result['Active'] = self.active
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('BackupTime') is not None:
            self.backup_time = m.get('BackupTime')
        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')
        if m.get('RetentionPeriod') is not None:
            self.retention_period = m.get('RetentionPeriod')
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
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
        pay_type: str = None,
        period_unit: str = None,
        period: int = None,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        client_token: str = None,
        region_id: str = None,
        zone_id: str = None,
        cluster_name: str = None,
        data_center_name: str = None,
        major_version: str = None,
        instance_type: str = None,
        node_count: int = None,
        disk_type: str = None,
        disk_size: int = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        password: str = None,
        resource_group_id: str = None,
    ):
        self.pay_type = pay_type
        self.period_unit = period_unit
        self.period = period
        self.auto_renew = auto_renew
        self.auto_renew_period = auto_renew_period
        self.client_token = client_token
        self.region_id = region_id
        self.zone_id = zone_id
        self.cluster_name = cluster_name
        self.data_center_name = data_center_name
        self.major_version = major_version
        self.instance_type = instance_type
        self.node_count = node_count
        self.disk_type = disk_type
        self.disk_size = disk_size
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id
        self.password = password
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.period is not None:
            result['Period'] = self.period
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.data_center_name is not None:
            result['DataCenterName'] = self.data_center_name
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.password is not None:
            result['Password'] = self.password
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('DataCenterName') is not None:
            self.data_center_name = m.get('DataCenterName')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cluster_id: str = None,
    ):
        self.request_id = request_id
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
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


class CreateDataCenterRequest(TeaModel):
    def __init__(
        self,
        pay_type: str = None,
        period_unit: str = None,
        period: int = None,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        client_token: str = None,
        region_id: str = None,
        zone_id: str = None,
        cluster_id: str = None,
        data_center_name: str = None,
        instance_type: str = None,
        node_count: int = None,
        disk_type: str = None,
        disk_size: int = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        self.pay_type = pay_type
        self.period_unit = period_unit
        self.period = period
        self.auto_renew = auto_renew
        self.auto_renew_period = auto_renew_period
        self.client_token = client_token
        self.region_id = region_id
        self.zone_id = zone_id
        self.cluster_id = cluster_id
        self.data_center_name = data_center_name
        self.instance_type = instance_type
        self.node_count = node_count
        self.disk_type = disk_type
        self.disk_size = disk_size
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.period is not None:
            result['Period'] = self.period
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_name is not None:
            result['DataCenterName'] = self.data_center_name
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterName') is not None:
            self.data_center_name = m.get('DataCenterName')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class CreateDataCenterResponseBody(TeaModel):
    def __init__(
        self,
        data_center_id: str = None,
        request_id: str = None,
    ):
        self.data_center_id = data_center_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDataCenterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDataCenterResponseBody = None,
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
            temp_model = CreateDataCenterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteBackupPlanRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        data_center_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.data_center_id = data_center_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        return self


class DeleteBackupPlanResponseBody(TeaModel):
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


class DeleteBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteBackupPlanResponseBody = None,
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
            temp_model = DeleteBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClusterRequest(TeaModel):
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


class DeleteClusterResponseBody(TeaModel):
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


class DeleteClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteClusterResponseBody = None,
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
            temp_model = DeleteClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDataCenterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        data_center_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.data_center_id = data_center_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        return self


class DeleteDataCenterResponseBody(TeaModel):
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


class DeleteDataCenterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDataCenterResponseBody = None,
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
            temp_model = DeleteDataCenterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNodeToolExecutionHistoryRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        job_id: str = None,
        data_center_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.job_id = job_id
        self.data_center_id = data_center_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        return self


class DeleteNodeToolExecutionHistoryResponseBody(TeaModel):
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


class DeleteNodeToolExecutionHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteNodeToolExecutionHistoryResponseBody = None,
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
            temp_model = DeleteNodeToolExecutionHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAccountsRequest(TeaModel):
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


class DescribeAccountsResponseBodyAccountsAccount(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeAccountsResponseBodyAccounts(TeaModel):
    def __init__(
        self,
        account: List[DescribeAccountsResponseBodyAccountsAccount] = None,
    ):
        self.account = account

    def validate(self):
        if self.account:
            for k in self.account:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Account'] = []
        if self.account is not None:
            for k in self.account:
                result['Account'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account = []
        if m.get('Account') is not None:
            for k in m.get('Account'):
                temp_model = DescribeAccountsResponseBodyAccountsAccount()
                self.account.append(temp_model.from_map(k))
        return self


class DescribeAccountsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        accounts: DescribeAccountsResponseBodyAccounts = None,
    ):
        self.request_id = request_id
        self.accounts = accounts

    def validate(self):
        if self.accounts:
            self.accounts.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Accounts') is not None:
            temp_model = DescribeAccountsResponseBodyAccounts()
            self.accounts = temp_model.from_map(m['Accounts'])
        return self


class DescribeAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeAccountsResponseBody = None,
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
            temp_model = DescribeAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        data_center_id: str = None,
        backup_id: str = None,
        backup_type: str = None,
    ):
        self.cluster_id = cluster_id
        self.data_center_id = data_center_id
        self.backup_id = backup_id
        self.backup_type = backup_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        return self


class DescribeBackupResponseBodyBackup(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        status: str = None,
        start_time: str = None,
        size: int = None,
        backup_type: str = None,
        backup_id: str = None,
        details: str = None,
        data_center_id: str = None,
        cluster_id: str = None,
    ):
        self.end_time = end_time
        self.status = status
        self.start_time = start_time
        self.size = size
        self.backup_type = backup_type
        self.backup_id = backup_id
        self.details = details
        self.data_center_id = data_center_id
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.status is not None:
            result['Status'] = self.status
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.size is not None:
            result['Size'] = self.size
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.details is not None:
            result['Details'] = self.details
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('Details') is not None:
            self.details = m.get('Details')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeBackupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        backup: DescribeBackupResponseBodyBackup = None,
    ):
        self.request_id = request_id
        self.backup = backup

    def validate(self):
        if self.backup:
            self.backup.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.backup is not None:
            result['Backup'] = self.backup.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Backup') is not None:
            temp_model = DescribeBackupResponseBodyBackup()
            self.backup = temp_model.from_map(m['Backup'])
        return self


class DescribeBackupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBackupResponseBody = None,
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
            temp_model = DescribeBackupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPlanRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        data_center_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.data_center_id = data_center_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        return self


class DescribeBackupPlanResponseBodyBackupPlan(TeaModel):
    def __init__(
        self,
        active: bool = None,
        backup_period: str = None,
        retention_period: int = None,
        created_time: str = None,
        backup_time: str = None,
        cluster_id: str = None,
        data_center_id: str = None,
    ):
        self.active = active
        self.backup_period = backup_period
        self.retention_period = retention_period
        self.created_time = created_time
        self.backup_time = backup_time
        self.cluster_id = cluster_id
        self.data_center_id = data_center_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period
        if self.retention_period is not None:
            result['RetentionPeriod'] = self.retention_period
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.backup_time is not None:
            result['BackupTime'] = self.backup_time
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')
        if m.get('RetentionPeriod') is not None:
            self.retention_period = m.get('RetentionPeriod')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('BackupTime') is not None:
            self.backup_time = m.get('BackupTime')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        return self


class DescribeBackupPlanResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        backup_plan: DescribeBackupPlanResponseBodyBackupPlan = None,
    ):
        self.request_id = request_id
        self.backup_plan = backup_plan

    def validate(self):
        if self.backup_plan:
            self.backup_plan.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.backup_plan is not None:
            result['BackupPlan'] = self.backup_plan.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BackupPlan') is not None:
            temp_model = DescribeBackupPlanResponseBodyBackupPlan()
            self.backup_plan = temp_model.from_map(m['BackupPlan'])
        return self


class DescribeBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBackupPlanResponseBody = None,
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
            temp_model = DescribeBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupPlansRequest(TeaModel):
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


class DescribeBackupPlansResponseBodyBackupPlansBackupPlan(TeaModel):
    def __init__(
        self,
        active: bool = None,
        backup_period: str = None,
        retention_period: int = None,
        created_time: str = None,
        backup_time: str = None,
        cluster_id: str = None,
        data_center_id: str = None,
    ):
        self.active = active
        self.backup_period = backup_period
        self.retention_period = retention_period
        self.created_time = created_time
        self.backup_time = backup_time
        self.cluster_id = cluster_id
        self.data_center_id = data_center_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period
        if self.retention_period is not None:
            result['RetentionPeriod'] = self.retention_period
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.backup_time is not None:
            result['BackupTime'] = self.backup_time
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')
        if m.get('RetentionPeriod') is not None:
            self.retention_period = m.get('RetentionPeriod')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('BackupTime') is not None:
            self.backup_time = m.get('BackupTime')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        return self


class DescribeBackupPlansResponseBodyBackupPlans(TeaModel):
    def __init__(
        self,
        backup_plan: List[DescribeBackupPlansResponseBodyBackupPlansBackupPlan] = None,
    ):
        self.backup_plan = backup_plan

    def validate(self):
        if self.backup_plan:
            for k in self.backup_plan:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['BackupPlan'] = []
        if self.backup_plan is not None:
            for k in self.backup_plan:
                result['BackupPlan'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup_plan = []
        if m.get('BackupPlan') is not None:
            for k in m.get('BackupPlan'):
                temp_model = DescribeBackupPlansResponseBodyBackupPlansBackupPlan()
                self.backup_plan.append(temp_model.from_map(k))
        return self


class DescribeBackupPlansResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        backup_plans: DescribeBackupPlansResponseBodyBackupPlans = None,
    ):
        self.request_id = request_id
        self.backup_plans = backup_plans

    def validate(self):
        if self.backup_plans:
            self.backup_plans.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.backup_plans is not None:
            result['BackupPlans'] = self.backup_plans.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BackupPlans') is not None:
            temp_model = DescribeBackupPlansResponseBodyBackupPlans()
            self.backup_plans = temp_model.from_map(m['BackupPlans'])
        return self


class DescribeBackupPlansResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeBackupPlansResponseBody = None,
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
            temp_model = DescribeBackupPlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeBackupsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        data_center_id: str = None,
        backup_type: str = None,
    ):
        self.cluster_id = cluster_id
        self.data_center_id = data_center_id
        self.backup_type = backup_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        return self


class DescribeBackupsResponseBodyBackupsBackup(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        status: str = None,
        start_time: str = None,
        size: int = None,
        backup_type: str = None,
        backup_id: str = None,
        cluster_id: str = None,
        data_center_id: str = None,
    ):
        self.end_time = end_time
        self.status = status
        self.start_time = start_time
        self.size = size
        self.backup_type = backup_type
        self.backup_id = backup_id
        self.cluster_id = cluster_id
        self.data_center_id = data_center_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.status is not None:
            result['Status'] = self.status
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.size is not None:
            result['Size'] = self.size
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
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
        request_id: str = None,
        backups: DescribeBackupsResponseBodyBackups = None,
    ):
        self.request_id = request_id
        self.backups = backups

    def validate(self):
        if self.backups:
            self.backups.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.backups is not None:
            result['Backups'] = self.backups.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class DescribeClusterRequest(TeaModel):
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


class DescribeClusterResponseBodyClusterTagsTag(TeaModel):
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


class DescribeClusterResponseBodyClusterTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeClusterResponseBodyClusterTagsTag] = None,
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
                temp_model = DescribeClusterResponseBodyClusterTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeClusterResponseBodyCluster(TeaModel):
    def __init__(
        self,
        status: str = None,
        expire_time: str = None,
        maintain_start_time: str = None,
        pay_type: str = None,
        maintain_end_time: str = None,
        tags: DescribeClusterResponseBodyClusterTags = None,
        lock_mode: str = None,
        minor_version: str = None,
        auto_renew_period: int = None,
        is_latest_version: bool = None,
        data_center_count: int = None,
        auto_renewal: bool = None,
        resource_group_id: str = None,
        cluster_name: str = None,
        major_version: str = None,
        created_time: str = None,
        cluster_id: str = None,
    ):
        self.status = status
        self.expire_time = expire_time
        self.maintain_start_time = maintain_start_time
        self.pay_type = pay_type
        self.maintain_end_time = maintain_end_time
        self.tags = tags
        self.lock_mode = lock_mode
        self.minor_version = minor_version
        self.auto_renew_period = auto_renew_period
        self.is_latest_version = is_latest_version
        self.data_center_count = data_center_count
        self.auto_renewal = auto_renewal
        self.resource_group_id = resource_group_id
        self.cluster_name = cluster_name
        self.major_version = major_version
        self.created_time = created_time
        self.cluster_id = cluster_id

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.maintain_start_time is not None:
            result['MaintainStartTime'] = self.maintain_start_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.maintain_end_time is not None:
            result['MaintainEndTime'] = self.maintain_end_time
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.is_latest_version is not None:
            result['IsLatestVersion'] = self.is_latest_version
        if self.data_center_count is not None:
            result['DataCenterCount'] = self.data_center_count
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('MaintainStartTime') is not None:
            self.maintain_start_time = m.get('MaintainStartTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('MaintainEndTime') is not None:
            self.maintain_end_time = m.get('MaintainEndTime')
        if m.get('Tags') is not None:
            temp_model = DescribeClusterResponseBodyClusterTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('IsLatestVersion') is not None:
            self.is_latest_version = m.get('IsLatestVersion')
        if m.get('DataCenterCount') is not None:
            self.data_center_count = m.get('DataCenterCount')
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        cluster: DescribeClusterResponseBodyCluster = None,
    ):
        self.request_id = request_id
        self.cluster = cluster

    def validate(self):
        if self.cluster:
            self.cluster.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.cluster is not None:
            result['Cluster'] = self.cluster.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Cluster') is not None:
            temp_model = DescribeClusterResponseBodyCluster()
            self.cluster = temp_model.from_map(m['Cluster'])
        return self


class DescribeClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeClusterResponseBody = None,
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
            temp_model = DescribeClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterDashboardRequest(TeaModel):
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


class DescribeClusterDashboardResponseBodyDashboardDataCentersDataCenterNodesNode(TeaModel):
    def __init__(
        self,
        status: str = None,
        address: str = None,
        load: str = None,
    ):
        self.status = status
        self.address = address
        self.load = load

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.address is not None:
            result['Address'] = self.address
        if self.load is not None:
            result['Load'] = self.load
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Load') is not None:
            self.load = m.get('Load')
        return self


class DescribeClusterDashboardResponseBodyDashboardDataCentersDataCenterNodes(TeaModel):
    def __init__(
        self,
        node: List[DescribeClusterDashboardResponseBodyDashboardDataCentersDataCenterNodesNode] = None,
    ):
        self.node = node

    def validate(self):
        if self.node:
            for k in self.node:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Node'] = []
        if self.node is not None:
            for k in self.node:
                result['Node'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.node = []
        if m.get('Node') is not None:
            for k in m.get('Node'):
                temp_model = DescribeClusterDashboardResponseBodyDashboardDataCentersDataCenterNodesNode()
                self.node.append(temp_model.from_map(k))
        return self


class DescribeClusterDashboardResponseBodyDashboardDataCentersDataCenter(TeaModel):
    def __init__(
        self,
        nodes: DescribeClusterDashboardResponseBodyDashboardDataCentersDataCenterNodes = None,
        data_center_id: str = None,
    ):
        self.nodes = nodes
        self.data_center_id = data_center_id

    def validate(self):
        if self.nodes:
            self.nodes.validate()

    def to_map(self):
        result = dict()
        if self.nodes is not None:
            result['Nodes'] = self.nodes.to_map()
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Nodes') is not None:
            temp_model = DescribeClusterDashboardResponseBodyDashboardDataCentersDataCenterNodes()
            self.nodes = temp_model.from_map(m['Nodes'])
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        return self


class DescribeClusterDashboardResponseBodyDashboardDataCenters(TeaModel):
    def __init__(
        self,
        data_center: List[DescribeClusterDashboardResponseBodyDashboardDataCentersDataCenter] = None,
    ):
        self.data_center = data_center

    def validate(self):
        if self.data_center:
            for k in self.data_center:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DataCenter'] = []
        if self.data_center is not None:
            for k in self.data_center:
                result['DataCenter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_center = []
        if m.get('DataCenter') is not None:
            for k in m.get('DataCenter'):
                temp_model = DescribeClusterDashboardResponseBodyDashboardDataCentersDataCenter()
                self.data_center.append(temp_model.from_map(k))
        return self


class DescribeClusterDashboardResponseBodyDashboard(TeaModel):
    def __init__(
        self,
        data_centers: DescribeClusterDashboardResponseBodyDashboardDataCenters = None,
        cluster_id: str = None,
    ):
        self.data_centers = data_centers
        self.cluster_id = cluster_id

    def validate(self):
        if self.data_centers:
            self.data_centers.validate()

    def to_map(self):
        result = dict()
        if self.data_centers is not None:
            result['DataCenters'] = self.data_centers.to_map()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCenters') is not None:
            temp_model = DescribeClusterDashboardResponseBodyDashboardDataCenters()
            self.data_centers = temp_model.from_map(m['DataCenters'])
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeClusterDashboardResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        dashboard: DescribeClusterDashboardResponseBodyDashboard = None,
    ):
        self.request_id = request_id
        self.dashboard = dashboard

    def validate(self):
        if self.dashboard:
            self.dashboard.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.dashboard is not None:
            result['Dashboard'] = self.dashboard.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Dashboard') is not None:
            temp_model = DescribeClusterDashboardResponseBodyDashboard()
            self.dashboard = temp_model.from_map(m['Dashboard'])
        return self


class DescribeClusterDashboardResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeClusterDashboardResponseBody = None,
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
            temp_model = DescribeClusterDashboardResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClustersRequestTag(TeaModel):
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


class DescribeClustersRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        page_number: int = None,
        page_size: int = None,
        cluster_name: str = None,
        resource_group_id: str = None,
        tag: List[DescribeClustersRequestTag] = None,
    ):
        self.region_id = region_id
        self.page_number = page_number
        self.page_size = page_size
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
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeClustersRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeClustersResponseBodyClustersClusterTagsTag(TeaModel):
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


class DescribeClustersResponseBodyClustersClusterTags(TeaModel):
    def __init__(
        self,
        tag: List[DescribeClustersResponseBodyClustersClusterTagsTag] = None,
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
                temp_model = DescribeClustersResponseBodyClustersClusterTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeClustersResponseBodyClustersCluster(TeaModel):
    def __init__(
        self,
        status: str = None,
        expire_time: str = None,
        pay_type: str = None,
        tags: DescribeClustersResponseBodyClustersClusterTags = None,
        lock_mode: str = None,
        auto_renew_period: int = None,
        minor_version: str = None,
        data_center_count: int = None,
        auto_renewal: bool = None,
        resource_group_id: str = None,
        cluster_name: str = None,
        major_version: str = None,
        created_time: str = None,
        cluster_id: str = None,
    ):
        self.status = status
        self.expire_time = expire_time
        self.pay_type = pay_type
        self.tags = tags
        self.lock_mode = lock_mode
        self.auto_renew_period = auto_renew_period
        self.minor_version = minor_version
        self.data_center_count = data_center_count
        self.auto_renewal = auto_renewal
        self.resource_group_id = resource_group_id
        self.cluster_name = cluster_name
        self.major_version = major_version
        self.created_time = created_time
        self.cluster_id = cluster_id

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.data_center_count is not None:
            result['DataCenterCount'] = self.data_center_count
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('Tags') is not None:
            temp_model = DescribeClustersResponseBodyClustersClusterTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('DataCenterCount') is not None:
            self.data_center_count = m.get('DataCenterCount')
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeClustersResponseBodyClusters(TeaModel):
    def __init__(
        self,
        cluster: List[DescribeClustersResponseBodyClustersCluster] = None,
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
                temp_model = DescribeClustersResponseBodyClustersCluster()
                self.cluster.append(temp_model.from_map(k))
        return self


class DescribeClustersResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        clusters: DescribeClustersResponseBodyClusters = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.clusters = clusters

    def validate(self):
        if self.clusters:
            self.clusters.validate()

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
        if self.clusters is not None:
            result['Clusters'] = self.clusters.to_map()
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
        if m.get('Clusters') is not None:
            temp_model = DescribeClustersResponseBodyClusters()
            self.clusters = temp_model.from_map(m['Clusters'])
        return self


class DescribeClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeClustersResponseBody = None,
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
            temp_model = DescribeClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterStatusRequest(TeaModel):
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


class DescribeClusterStatusResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        created_time: str = None,
        request_id: str = None,
    ):
        self.status = status
        self.created_time = created_time
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeClusterStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeClusterStatusResponseBody = None,
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
            temp_model = DescribeClusterStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeContactPointsRequest(TeaModel):
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


class DescribeContactPointsResponseBodyContactPointsContactPointPublicAddresses(TeaModel):
    def __init__(
        self,
        public_address: List[str] = None,
    ):
        self.public_address = public_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.public_address is not None:
            result['PublicAddress'] = self.public_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PublicAddress') is not None:
            self.public_address = m.get('PublicAddress')
        return self


class DescribeContactPointsResponseBodyContactPointsContactPointPrivateAddresses(TeaModel):
    def __init__(
        self,
        private_address: List[str] = None,
    ):
        self.private_address = private_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.private_address is not None:
            result['PrivateAddress'] = self.private_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivateAddress') is not None:
            self.private_address = m.get('PrivateAddress')
        return self


class DescribeContactPointsResponseBodyContactPointsContactPoint(TeaModel):
    def __init__(
        self,
        public_addresses: DescribeContactPointsResponseBodyContactPointsContactPointPublicAddresses = None,
        port: int = None,
        private_addresses: DescribeContactPointsResponseBodyContactPointsContactPointPrivateAddresses = None,
        data_center_id: str = None,
    ):
        self.public_addresses = public_addresses
        self.port = port
        self.private_addresses = private_addresses
        self.data_center_id = data_center_id

    def validate(self):
        if self.public_addresses:
            self.public_addresses.validate()
        if self.private_addresses:
            self.private_addresses.validate()

    def to_map(self):
        result = dict()
        if self.public_addresses is not None:
            result['PublicAddresses'] = self.public_addresses.to_map()
        if self.port is not None:
            result['Port'] = self.port
        if self.private_addresses is not None:
            result['PrivateAddresses'] = self.private_addresses.to_map()
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PublicAddresses') is not None:
            temp_model = DescribeContactPointsResponseBodyContactPointsContactPointPublicAddresses()
            self.public_addresses = temp_model.from_map(m['PublicAddresses'])
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('PrivateAddresses') is not None:
            temp_model = DescribeContactPointsResponseBodyContactPointsContactPointPrivateAddresses()
            self.private_addresses = temp_model.from_map(m['PrivateAddresses'])
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        return self


class DescribeContactPointsResponseBodyContactPoints(TeaModel):
    def __init__(
        self,
        contact_point: List[DescribeContactPointsResponseBodyContactPointsContactPoint] = None,
    ):
        self.contact_point = contact_point

    def validate(self):
        if self.contact_point:
            for k in self.contact_point:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ContactPoint'] = []
        if self.contact_point is not None:
            for k in self.contact_point:
                result['ContactPoint'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact_point = []
        if m.get('ContactPoint') is not None:
            for k in m.get('ContactPoint'):
                temp_model = DescribeContactPointsResponseBodyContactPointsContactPoint()
                self.contact_point.append(temp_model.from_map(k))
        return self


class DescribeContactPointsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        contact_points: DescribeContactPointsResponseBodyContactPoints = None,
    ):
        self.request_id = request_id
        self.contact_points = contact_points

    def validate(self):
        if self.contact_points:
            self.contact_points.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.contact_points is not None:
            result['ContactPoints'] = self.contact_points.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ContactPoints') is not None:
            temp_model = DescribeContactPointsResponseBodyContactPoints()
            self.contact_points = temp_model.from_map(m['ContactPoints'])
        return self


class DescribeContactPointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeContactPointsResponseBody = None,
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
            temp_model = DescribeContactPointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataCenterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        data_center_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.data_center_id = data_center_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        return self


class DescribeDataCenterResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        auto_renew_period: int = None,
        data_center_id: str = None,
        commodity_instance: str = None,
        created_time: str = None,
        request_id: str = None,
        node_count: int = None,
        zone_id: str = None,
        cluster_id: str = None,
        pay_type: str = None,
        lock_mode: str = None,
        vswitch_id: str = None,
        data_center_name: str = None,
        disk_type: str = None,
        vpc_id: str = None,
        auto_renewal: bool = None,
        disk_size: int = None,
        region_id: str = None,
        expire_time: str = None,
        instance_type: str = None,
    ):
        self.status = status
        self.auto_renew_period = auto_renew_period
        self.data_center_id = data_center_id
        self.commodity_instance = commodity_instance
        self.created_time = created_time
        self.request_id = request_id
        self.node_count = node_count
        self.zone_id = zone_id
        self.cluster_id = cluster_id
        self.pay_type = pay_type
        self.lock_mode = lock_mode
        self.vswitch_id = vswitch_id
        self.data_center_name = data_center_name
        self.disk_type = disk_type
        self.vpc_id = vpc_id
        self.auto_renewal = auto_renewal
        self.disk_size = disk_size
        self.region_id = region_id
        self.expire_time = expire_time
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.commodity_instance is not None:
            result['CommodityInstance'] = self.commodity_instance
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.data_center_name is not None:
            result['DataCenterName'] = self.data_center_name
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('CommodityInstance') is not None:
            self.commodity_instance = m.get('CommodityInstance')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('DataCenterName') is not None:
            self.data_center_name = m.get('DataCenterName')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class DescribeDataCenterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDataCenterResponseBody = None,
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
            temp_model = DescribeDataCenterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDataCentersRequest(TeaModel):
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


class DescribeDataCentersResponseBodyDataCentersDataCenter(TeaModel):
    def __init__(
        self,
        status: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        expire_time: str = None,
        disk_size: int = None,
        pay_type: str = None,
        disk_type: str = None,
        instance_type: str = None,
        lock_mode: str = None,
        auto_renew_period: int = None,
        region_id: str = None,
        auto_renewal: bool = None,
        commodity_instance: str = None,
        node_count: int = None,
        data_center_name: str = None,
        zone_id: str = None,
        created_time: str = None,
        cluster_id: str = None,
        data_center_id: str = None,
    ):
        self.status = status
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id
        self.expire_time = expire_time
        self.disk_size = disk_size
        self.pay_type = pay_type
        self.disk_type = disk_type
        self.instance_type = instance_type
        self.lock_mode = lock_mode
        self.auto_renew_period = auto_renew_period
        self.region_id = region_id
        self.auto_renewal = auto_renewal
        self.commodity_instance = commodity_instance
        self.node_count = node_count
        self.data_center_name = data_center_name
        self.zone_id = zone_id
        self.created_time = created_time
        self.cluster_id = cluster_id
        self.data_center_id = data_center_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.lock_mode is not None:
            result['LockMode'] = self.lock_mode
        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.auto_renewal is not None:
            result['AutoRenewal'] = self.auto_renewal
        if self.commodity_instance is not None:
            result['CommodityInstance'] = self.commodity_instance
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.data_center_name is not None:
            result['DataCenterName'] = self.data_center_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('LockMode') is not None:
            self.lock_mode = m.get('LockMode')
        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('AutoRenewal') is not None:
            self.auto_renewal = m.get('AutoRenewal')
        if m.get('CommodityInstance') is not None:
            self.commodity_instance = m.get('CommodityInstance')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('DataCenterName') is not None:
            self.data_center_name = m.get('DataCenterName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        return self


class DescribeDataCentersResponseBodyDataCenters(TeaModel):
    def __init__(
        self,
        data_center: List[DescribeDataCentersResponseBodyDataCentersDataCenter] = None,
    ):
        self.data_center = data_center

    def validate(self):
        if self.data_center:
            for k in self.data_center:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DataCenter'] = []
        if self.data_center is not None:
            for k in self.data_center:
                result['DataCenter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_center = []
        if m.get('DataCenter') is not None:
            for k in m.get('DataCenter'):
                temp_model = DescribeDataCentersResponseBodyDataCentersDataCenter()
                self.data_center.append(temp_model.from_map(k))
        return self


class DescribeDataCentersResponseBody(TeaModel):
    def __init__(
        self,
        data_centers: DescribeDataCentersResponseBodyDataCenters = None,
        request_id: str = None,
    ):
        self.data_centers = data_centers
        self.request_id = request_id

    def validate(self):
        if self.data_centers:
            self.data_centers.validate()

    def to_map(self):
        result = dict()
        if self.data_centers is not None:
            result['DataCenters'] = self.data_centers.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCenters') is not None:
            temp_model = DescribeDataCentersResponseBodyDataCenters()
            self.data_centers = temp_model.from_map(m['DataCenters'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDataCentersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDataCentersResponseBody = None,
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
            temp_model = DescribeDataCentersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDeletedClustersRequest(TeaModel):
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


class DescribeDeletedClustersResponseBodyClustersCluster(TeaModel):
    def __init__(
        self,
        status: str = None,
        data_center_count: int = None,
        expire_time: str = None,
        pay_type: str = None,
        cluster_name: str = None,
        major_version: str = None,
        created_time: str = None,
        minor_version: str = None,
        cluster_id: str = None,
    ):
        self.status = status
        self.data_center_count = data_center_count
        self.expire_time = expire_time
        self.pay_type = pay_type
        self.cluster_name = cluster_name
        self.major_version = major_version
        self.created_time = created_time
        self.minor_version = minor_version
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.data_center_count is not None:
            result['DataCenterCount'] = self.data_center_count
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.major_version is not None:
            result['MajorVersion'] = self.major_version
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.minor_version is not None:
            result['MinorVersion'] = self.minor_version
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('DataCenterCount') is not None:
            self.data_center_count = m.get('DataCenterCount')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('MajorVersion') is not None:
            self.major_version = m.get('MajorVersion')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('MinorVersion') is not None:
            self.minor_version = m.get('MinorVersion')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeDeletedClustersResponseBodyClusters(TeaModel):
    def __init__(
        self,
        cluster: List[DescribeDeletedClustersResponseBodyClustersCluster] = None,
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
                temp_model = DescribeDeletedClustersResponseBodyClustersCluster()
                self.cluster.append(temp_model.from_map(k))
        return self


class DescribeDeletedClustersResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        clusters: DescribeDeletedClustersResponseBodyClusters = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.clusters = clusters

    def validate(self):
        if self.clusters:
            self.clusters.validate()

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
        if self.clusters is not None:
            result['Clusters'] = self.clusters.to_map()
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
        if m.get('Clusters') is not None:
            temp_model = DescribeDeletedClustersResponseBodyClusters()
            self.clusters = temp_model.from_map(m['Clusters'])
        return self


class DescribeDeletedClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeDeletedClustersResponseBody = None,
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
            temp_model = DescribeDeletedClustersResponseBody()
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


class DescribeIpWhitelistResponseBodyIpList(TeaModel):
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
            result['IP'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        return self


class DescribeIpWhitelistResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        ip_list: DescribeIpWhitelistResponseBodyIpList = None,
    ):
        self.request_id = request_id
        self.ip_list = ip_list

    def validate(self):
        if self.ip_list:
            self.ip_list.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ip_list is not None:
            result['IpList'] = self.ip_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IpList') is not None:
            temp_model = DescribeIpWhitelistResponseBodyIpList()
            self.ip_list = temp_model.from_map(m['IpList'])
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


class DescribeIpWhitelistGroupsRequest(TeaModel):
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


class DescribeIpWhitelistGroupsResponseBodyGroupsGroupIpList(TeaModel):
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
            result['IP'] = self.ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        return self


class DescribeIpWhitelistGroupsResponseBodyGroupsGroup(TeaModel):
    def __init__(
        self,
        ip_version: int = None,
        group_name: str = None,
        ip_list: DescribeIpWhitelistGroupsResponseBodyGroupsGroupIpList = None,
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
            temp_model = DescribeIpWhitelistGroupsResponseBodyGroupsGroupIpList()
            self.ip_list = temp_model.from_map(m['IpList'])
        return self


class DescribeIpWhitelistGroupsResponseBodyGroups(TeaModel):
    def __init__(
        self,
        group: List[DescribeIpWhitelistGroupsResponseBodyGroupsGroup] = None,
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
                temp_model = DescribeIpWhitelistGroupsResponseBodyGroupsGroup()
                self.group.append(temp_model.from_map(k))
        return self


class DescribeIpWhitelistGroupsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        groups: DescribeIpWhitelistGroupsResponseBodyGroups = None,
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
            temp_model = DescribeIpWhitelistGroupsResponseBodyGroups()
            self.groups = temp_model.from_map(m['Groups'])
        return self


class DescribeIpWhitelistGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeIpWhitelistGroupsResponseBody = None,
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
            temp_model = DescribeIpWhitelistGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNodeToolExecutionHistoriesRequest(TeaModel):
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


class DescribeNodeToolExecutionHistoriesResponseBodyHistoriesHistory(TeaModel):
    def __init__(
        self,
        nodes: str = None,
        error_message: str = None,
        is_ended: bool = None,
        create_time: int = None,
        job_id: str = None,
        command: str = None,
        data_center_id: str = None,
        arguments: str = None,
        region_id: str = None,
        modify_time: int = None,
    ):
        self.nodes = nodes
        self.error_message = error_message
        self.is_ended = is_ended
        self.create_time = create_time
        self.job_id = job_id
        self.command = command
        self.data_center_id = data_center_id
        self.arguments = arguments
        self.region_id = region_id
        self.modify_time = modify_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.nodes is not None:
            result['Nodes'] = self.nodes
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_ended is not None:
            result['IsEnded'] = self.is_ended
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.command is not None:
            result['Command'] = self.command
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.arguments is not None:
            result['Arguments'] = self.arguments
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsEnded') is not None:
            self.is_ended = m.get('IsEnded')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('Arguments') is not None:
            self.arguments = m.get('Arguments')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        return self


class DescribeNodeToolExecutionHistoriesResponseBodyHistories(TeaModel):
    def __init__(
        self,
        history: List[DescribeNodeToolExecutionHistoriesResponseBodyHistoriesHistory] = None,
    ):
        self.history = history

    def validate(self):
        if self.history:
            for k in self.history:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['History'] = []
        if self.history is not None:
            for k in self.history:
                result['History'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.history = []
        if m.get('History') is not None:
            for k in m.get('History'):
                temp_model = DescribeNodeToolExecutionHistoriesResponseBodyHistoriesHistory()
                self.history.append(temp_model.from_map(k))
        return self


class DescribeNodeToolExecutionHistoriesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        histories: DescribeNodeToolExecutionHistoriesResponseBodyHistories = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
        self.histories = histories

    def validate(self):
        if self.histories:
            self.histories.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.histories is not None:
            result['Histories'] = self.histories.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Histories') is not None:
            temp_model = DescribeNodeToolExecutionHistoriesResponseBodyHistories()
            self.histories = temp_model.from_map(m['Histories'])
        return self


class DescribeNodeToolExecutionHistoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeNodeToolExecutionHistoriesResponseBody = None,
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
            temp_model = DescribeNodeToolExecutionHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNodeToolExecutionHistoryRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        dc_id: str = None,
        job_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.dc_id = dc_id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.dc_id is not None:
            result['DcId'] = self.dc_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DcId') is not None:
            self.dc_id = m.get('DcId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DescribeNodeToolExecutionHistoryResponseBody(TeaModel):
    def __init__(
        self,
        modify_time: int = None,
        data_center_id: str = None,
        request_id: str = None,
        is_ended: bool = None,
        command: str = None,
        create_time: int = None,
        arguments: str = None,
        region_id: str = None,
        error_message: str = None,
        nodes: str = None,
        job_id: str = None,
        result: str = None,
    ):
        self.modify_time = modify_time
        self.data_center_id = data_center_id
        self.request_id = request_id
        self.is_ended = is_ended
        self.command = command
        self.create_time = create_time
        self.arguments = arguments
        self.region_id = region_id
        self.error_message = error_message
        self.nodes = nodes
        self.job_id = job_id
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_ended is not None:
            result['IsEnded'] = self.is_ended
        if self.command is not None:
            result['Command'] = self.command
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.arguments is not None:
            result['Arguments'] = self.arguments
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.nodes is not None:
            result['Nodes'] = self.nodes
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IsEnded') is not None:
            self.is_ended = m.get('IsEnded')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Arguments') is not None:
            self.arguments = m.get('Arguments')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class DescribeNodeToolExecutionHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeNodeToolExecutionHistoryResponseBody = None,
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
            temp_model = DescribeNodeToolExecutionHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParameterModificationHistoriesRequest(TeaModel):
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


class DescribeParameterModificationHistoriesResponseBodyHistoriesHistory(TeaModel):
    def __init__(
        self,
        time: int = None,
        old_value: str = None,
        name: str = None,
        new_value: str = None,
    ):
        self.time = time
        self.old_value = old_value
        self.name = name
        self.new_value = new_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.old_value is not None:
            result['OldValue'] = self.old_value
        if self.name is not None:
            result['Name'] = self.name
        if self.new_value is not None:
            result['NewValue'] = self.new_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('OldValue') is not None:
            self.old_value = m.get('OldValue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NewValue') is not None:
            self.new_value = m.get('NewValue')
        return self


class DescribeParameterModificationHistoriesResponseBodyHistories(TeaModel):
    def __init__(
        self,
        history: List[DescribeParameterModificationHistoriesResponseBodyHistoriesHistory] = None,
    ):
        self.history = history

    def validate(self):
        if self.history:
            for k in self.history:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['History'] = []
        if self.history is not None:
            for k in self.history:
                result['History'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.history = []
        if m.get('History') is not None:
            for k in m.get('History'):
                temp_model = DescribeParameterModificationHistoriesResponseBodyHistoriesHistory()
                self.history.append(temp_model.from_map(k))
        return self


class DescribeParameterModificationHistoriesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        histories: DescribeParameterModificationHistoriesResponseBodyHistories = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
        self.histories = histories

    def validate(self):
        if self.histories:
            self.histories.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.histories is not None:
            result['Histories'] = self.histories.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Histories') is not None:
            temp_model = DescribeParameterModificationHistoriesResponseBodyHistories()
            self.histories = temp_model.from_map(m['Histories'])
        return self


class DescribeParameterModificationHistoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeParameterModificationHistoriesResponseBody = None,
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
            temp_model = DescribeParameterModificationHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeParametersRequest(TeaModel):
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


class DescribeParametersResponseBodyParametersParameter(TeaModel):
    def __init__(
        self,
        value: str = None,
        data_type: str = None,
        description: str = None,
        name: str = None,
        default_value: str = None,
        allowed_values: str = None,
    ):
        self.value = value
        self.data_type = data_type
        self.description = description
        self.name = name
        self.default_value = default_value
        self.allowed_values = allowed_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value
        if self.allowed_values is not None:
            result['AllowedValues'] = self.allowed_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')
        if m.get('AllowedValues') is not None:
            self.allowed_values = m.get('AllowedValues')
        return self


class DescribeParametersResponseBodyParameters(TeaModel):
    def __init__(
        self,
        parameter: List[DescribeParametersResponseBodyParametersParameter] = None,
    ):
        self.parameter = parameter

    def validate(self):
        if self.parameter:
            for k in self.parameter:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Parameter'] = []
        if self.parameter is not None:
            for k in self.parameter:
                result['Parameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parameter = []
        if m.get('Parameter') is not None:
            for k in m.get('Parameter'):
                temp_model = DescribeParametersResponseBodyParametersParameter()
                self.parameter.append(temp_model.from_map(k))
        return self


class DescribeParametersResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        parameters: DescribeParametersResponseBodyParameters = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.total_count = total_count
        self.parameters = parameters
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.parameters is not None:
            result['Parameters'] = self.parameters.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('Parameters') is not None:
            temp_model = DescribeParametersResponseBodyParameters()
            self.parameters = temp_model.from_map(m['Parameters'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class DescribeParametersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeParametersResponseBody = None,
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
            temp_model = DescribeParametersResponseBody()
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


class ExecuteNodeToolRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        command: str = None,
        arguments: str = None,
        data_center_id: str = None,
        execute_nodes: str = None,
    ):
        self.cluster_id = cluster_id
        self.command = command
        self.arguments = arguments
        self.data_center_id = data_center_id
        self.execute_nodes = execute_nodes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.command is not None:
            result['Command'] = self.command
        if self.arguments is not None:
            result['Arguments'] = self.arguments
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.execute_nodes is not None:
            result['ExecuteNodes'] = self.execute_nodes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Arguments') is not None:
            self.arguments = m.get('Arguments')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('ExecuteNodes') is not None:
            self.execute_nodes = m.get('ExecuteNodes')
        return self


class ExecuteNodeToolResponseBody(TeaModel):
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


class ExecuteNodeToolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExecuteNodeToolResponseBody = None,
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
            temp_model = ExecuteNodeToolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCmsUrlRequest(TeaModel):
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


class GetCmsUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        url: str = None,
    ):
        self.request_id = request_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetCmsUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetCmsUrlResponseBody = None,
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
            temp_model = GetCmsUrlResponseBody()
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


class ModifyAccountPasswordRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        account: str = None,
        password: str = None,
    ):
        self.cluster_id = cluster_id
        self.account = account
        self.password = password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.account is not None:
            result['Account'] = self.account
        if self.password is not None:
            result['Password'] = self.password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        return self


class ModifyAccountPasswordResponseBody(TeaModel):
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


class ModifyAccountPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyAccountPasswordResponseBody = None,
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
            temp_model = ModifyAccountPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBackupPlanRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        data_center_id: str = None,
        backup_time: str = None,
        backup_period: str = None,
        retention_period: int = None,
        active: bool = None,
    ):
        self.cluster_id = cluster_id
        self.data_center_id = data_center_id
        self.backup_time = backup_time
        self.backup_period = backup_period
        self.retention_period = retention_period
        self.active = active

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.backup_time is not None:
            result['BackupTime'] = self.backup_time
        if self.backup_period is not None:
            result['BackupPeriod'] = self.backup_period
        if self.retention_period is not None:
            result['RetentionPeriod'] = self.retention_period
        if self.active is not None:
            result['Active'] = self.active
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('BackupTime') is not None:
            self.backup_time = m.get('BackupTime')
        if m.get('BackupPeriod') is not None:
            self.backup_period = m.get('BackupPeriod')
        if m.get('RetentionPeriod') is not None:
            self.retention_period = m.get('RetentionPeriod')
        if m.get('Active') is not None:
            self.active = m.get('Active')
        return self


class ModifyBackupPlanResponseBody(TeaModel):
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


class ModifyBackupPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyBackupPlanResponseBody = None,
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
            temp_model = ModifyBackupPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        return self


class ModifyClusterResponseBody(TeaModel):
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


class ModifyClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyClusterResponseBody = None,
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
            temp_model = ModifyClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDataCenterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        data_center_id: str = None,
        data_center_name: str = None,
    ):
        self.cluster_id = cluster_id
        self.data_center_id = data_center_id
        self.data_center_name = data_center_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.data_center_name is not None:
            result['DataCenterName'] = self.data_center_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('DataCenterName') is not None:
            self.data_center_name = m.get('DataCenterName')
        return self


class ModifyDataCenterResponseBody(TeaModel):
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


class ModifyDataCenterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDataCenterResponseBody = None,
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
            temp_model = ModifyDataCenterResponseBody()
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


class ModifyInstanceTypeRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        data_center_id: str = None,
        instance_type: str = None,
    ):
        self.cluster_id = cluster_id
        self.data_center_id = data_center_id
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class ModifyInstanceTypeResponseBody(TeaModel):
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
    ):
        self.cluster_id = cluster_id
        self.ip_list = ip_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.ip_list is not None:
            result['IpList'] = self.ip_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('IpList') is not None:
            self.ip_list = m.get('IpList')
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


class ModifyIpWhitelistGroupRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        ip_list: str = None,
        group_name: str = None,
        ip_version: int = None,
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


class ModifyIpWhitelistGroupResponseBody(TeaModel):
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


class ModifyIpWhitelistGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyIpWhitelistGroupResponseBody = None,
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
            temp_model = ModifyIpWhitelistGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyParameterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        name: str = None,
        value: str = None,
    ):
        self.cluster_id = cluster_id
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ModifyParameterResponseBody(TeaModel):
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


class ModifyParameterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyParameterResponseBody = None,
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
            temp_model = ModifyParameterResponseBody()
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


class PurgeClusterRequest(TeaModel):
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


class PurgeClusterResponseBody(TeaModel):
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


class PurgeClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PurgeClusterResponseBody = None,
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
            temp_model = PurgeClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebootClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        data_center_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.data_center_id = data_center_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        return self


class RebootClusterResponseBody(TeaModel):
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


class RebootClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RebootClusterResponseBody = None,
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
            temp_model = RebootClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleasePublicContactPointsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        data_center_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.data_center_id = data_center_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        return self


class ReleasePublicContactPointsResponseBody(TeaModel):
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


class ReleasePublicContactPointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReleasePublicContactPointsResponseBody = None,
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
            temp_model = ReleasePublicContactPointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResizeDiskSizeRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        data_center_id: str = None,
        disk_size: int = None,
    ):
        self.cluster_id = cluster_id
        self.data_center_id = data_center_id
        self.disk_size = disk_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        return self


class ResizeDiskSizeResponseBody(TeaModel):
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


class ResizeNodeCountRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        data_center_id: str = None,
        node_count: int = None,
    ):
        self.cluster_id = cluster_id
        self.data_center_id = data_center_id
        self.node_count = node_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.data_center_id is not None:
            result['DataCenterId'] = self.data_center_id
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DataCenterId') is not None:
            self.data_center_id = m.get('DataCenterId')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        return self


class ResizeNodeCountResponseBody(TeaModel):
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


class UpgradeClusterVersionRequest(TeaModel):
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


class UpgradeClusterVersionResponseBody(TeaModel):
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


class UpgradeClusterVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpgradeClusterVersionResponseBody = None,
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
            temp_model = UpgradeClusterVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


