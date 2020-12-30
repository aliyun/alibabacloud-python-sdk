# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateClusterRequest(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        cluster_type: str = None,
        v_switch_id: str = None,
    ):
        self.vpc_id = vpc_id
        self.cluster_type = cluster_type
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
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


class CreateImageRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
    ):
        self.instance_id = instance_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateImageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        image_id: str = None,
    ):
        self.request_id = request_id
        self.image_id = image_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class CreateImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateImageResponseBody = None,
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
            temp_model = CreateImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequestAppList(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_path: str = None,
        app_args: str = None,
    ):
        self.app_name = app_name
        self.app_path = app_path
        self.app_args = app_args

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_path is not None:
            result['AppPath'] = self.app_path
        if self.app_args is not None:
            result['AppArgs'] = self.app_args
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppPath') is not None:
            self.app_path = m.get('AppPath')
        if m.get('AppArgs') is not None:
            self.app_args = m.get('AppArgs')
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        v_switch_id: str = None,
        name: str = None,
        image_id: str = None,
        system_disk_size: int = None,
        system_disk_category: str = None,
        allocate_public_address: str = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_in: int = None,
        internet_max_bandwidth_out: int = None,
        instance_type: str = None,
        instance_charge_type: str = None,
        auto_renew: str = None,
        period: int = None,
        period_unit: str = None,
        work_mode: str = None,
        app_list: List[CreateInstanceRequestAppList] = None,
    ):
        self.cluster_id = cluster_id
        self.v_switch_id = v_switch_id
        self.name = name
        self.image_id = image_id
        self.system_disk_size = system_disk_size
        self.system_disk_category = system_disk_category
        self.allocate_public_address = allocate_public_address
        self.internet_charge_type = internet_charge_type
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        self.instance_type = instance_type
        self.instance_charge_type = instance_charge_type
        self.auto_renew = auto_renew
        self.period = period
        self.period_unit = period_unit
        self.work_mode = work_mode
        self.app_list = app_list

    def validate(self):
        if self.app_list:
            for k in self.app_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.name is not None:
            result['Name'] = self.name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size
        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category
        if self.allocate_public_address is not None:
            result['AllocatePublicAddress'] = self.allocate_public_address
        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type
        if self.internet_max_bandwidth_in is not None:
            result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in
        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.work_mode is not None:
            result['WorkMode'] = self.work_mode
        result['AppList'] = []
        if self.app_list is not None:
            for k in self.app_list:
                result['AppList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')
        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')
        if m.get('AllocatePublicAddress') is not None:
            self.allocate_public_address = m.get('AllocatePublicAddress')
        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')
        if m.get('InternetMaxBandwidthIn') is not None:
            self.internet_max_bandwidth_in = m.get('InternetMaxBandwidthIn')
        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('WorkMode') is not None:
            self.work_mode = m.get('WorkMode')
        self.app_list = []
        if m.get('AppList') is not None:
            for k in m.get('AppList'):
                temp_model = CreateInstanceRequestAppList()
                self.app_list.append(temp_model.from_map(k))
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        instance_id: str = None,
    ):
        self.request_id = request_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateInstanceResponseBody = None,
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
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceLinkedRoleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        already_exists: bool = None,
    ):
        self.request_id = request_id
        self.already_exists = already_exists

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.already_exists is not None:
            result['AlreadyExists'] = self.already_exists
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AlreadyExists') is not None:
            self.already_exists = m.get('AlreadyExists')
        return self


class CreateServiceLinkedRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateServiceLinkedRoleResponseBody = None,
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
            temp_model = CreateServiceLinkedRoleResponseBody()
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


class DeleteImageRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
    ):
        self.image_id = image_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class DeleteImageResponseBody(TeaModel):
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


class DeleteImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteImageResponseBody = None,
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
            temp_model = DeleteImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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


class DescribeAvailableResourceResponseBodyAvailableResources(TeaModel):
    def __init__(
        self,
        cluster_type: str = None,
        zone: str = None,
    ):
        self.cluster_type = cluster_type
        self.zone = zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.zone is not None:
            result['Zone'] = self.zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Zone') is not None:
            self.zone = m.get('Zone')
        return self


class DescribeAvailableResourceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        available_resources: List[DescribeAvailableResourceResponseBodyAvailableResources] = None,
    ):
        self.request_id = request_id
        self.available_resources = available_resources

    def validate(self):
        if self.available_resources:
            for k in self.available_resources:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['AvailableResources'] = []
        if self.available_resources is not None:
            for k in self.available_resources:
                result['AvailableResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.available_resources = []
        if m.get('AvailableResources') is not None:
            for k in m.get('AvailableResources'):
                temp_model = DescribeAvailableResourceResponseBodyAvailableResources()
                self.available_resources.append(temp_model.from_map(k))
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


class DescribeClusterADDomainRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        task_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeClusterADDomainResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        request_id: str = None,
        domain_name: str = None,
        task_finished: bool = None,
        is_supported: bool = None,
        domain_dns_ip: str = None,
    ):
        self.task_id = task_id
        self.request_id = request_id
        self.domain_name = domain_name
        self.task_finished = task_finished
        self.is_supported = is_supported
        self.domain_dns_ip = domain_dns_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.task_finished is not None:
            result['TaskFinished'] = self.task_finished
        if self.is_supported is not None:
            result['IsSupported'] = self.is_supported
        if self.domain_dns_ip is not None:
            result['DomainDnsIp'] = self.domain_dns_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('TaskFinished') is not None:
            self.task_finished = m.get('TaskFinished')
        if m.get('IsSupported') is not None:
            self.is_supported = m.get('IsSupported')
        if m.get('DomainDnsIp') is not None:
            self.domain_dns_ip = m.get('DomainDnsIp')
        return self


class DescribeClusterADDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeClusterADDomainResponseBody = None,
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
            temp_model = DescribeClusterADDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterConnectionsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        start_time: str = None,
        end_time: str = None,
        task_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.start_time = start_time
        self.end_time = end_time
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeClusterConnectionsResponseBodyConnections(TeaModel):
    def __init__(
        self,
        logoff_status: str = None,
        instance_name: str = None,
        logon_time: str = None,
        host_name: str = None,
        logoff_time: str = None,
        instance_id: str = None,
        client_name: str = None,
    ):
        self.logoff_status = logoff_status
        self.instance_name = instance_name
        self.logon_time = logon_time
        self.host_name = host_name
        self.logoff_time = logoff_time
        self.instance_id = instance_id
        self.client_name = client_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.logoff_status is not None:
            result['LogoffStatus'] = self.logoff_status
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.logon_time is not None:
            result['LogonTime'] = self.logon_time
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.logoff_time is not None:
            result['LogoffTime'] = self.logoff_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.client_name is not None:
            result['ClientName'] = self.client_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogoffStatus') is not None:
            self.logoff_status = m.get('LogoffStatus')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('LogonTime') is not None:
            self.logon_time = m.get('LogonTime')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('LogoffTime') is not None:
            self.logoff_time = m.get('LogoffTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ClientName') is not None:
            self.client_name = m.get('ClientName')
        return self


class DescribeClusterConnectionsResponseBody(TeaModel):
    def __init__(
        self,
        connections: List[DescribeClusterConnectionsResponseBodyConnections] = None,
        total_count: int = None,
        task_id: str = None,
        request_id: str = None,
        task_finished: bool = None,
    ):
        self.connections = connections
        self.total_count = total_count
        self.task_id = task_id
        self.request_id = request_id
        self.task_finished = task_finished

    def validate(self):
        if self.connections:
            for k in self.connections:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Connections'] = []
        if self.connections is not None:
            for k in self.connections:
                result['Connections'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_finished is not None:
            result['TaskFinished'] = self.task_finished
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connections = []
        if m.get('Connections') is not None:
            for k in m.get('Connections'):
                temp_model = DescribeClusterConnectionsResponseBodyConnections()
                self.connections.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskFinished') is not None:
            self.task_finished = m.get('TaskFinished')
        return self


class DescribeClusterConnectionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeClusterConnectionsResponseBody = None,
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
            temp_model = DescribeClusterConnectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterPolicyRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        async_mode: bool = None,
        cluster_id: str = None,
    ):
        self.task_id = task_id
        self.async_mode = async_mode
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.async_mode is not None:
            result['AsyncMode'] = self.async_mode
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('AsyncMode') is not None:
            self.async_mode = m.get('AsyncMode')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeClusterPolicyResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        udp_port: str = None,
        request_id: str = None,
        local_drive: str = None,
        usb_redirect: str = None,
        task_finished: bool = None,
        clipboard: str = None,
        domain_list: str = None,
        watermark: str = None,
    ):
        self.task_id = task_id
        self.udp_port = udp_port
        self.request_id = request_id
        self.local_drive = local_drive
        self.usb_redirect = usb_redirect
        self.task_finished = task_finished
        self.clipboard = clipboard
        self.domain_list = domain_list
        self.watermark = watermark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.udp_port is not None:
            result['UdpPort'] = self.udp_port
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        if self.usb_redirect is not None:
            result['UsbRedirect'] = self.usb_redirect
        if self.task_finished is not None:
            result['TaskFinished'] = self.task_finished
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        if self.watermark is not None:
            result['Watermark'] = self.watermark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('UdpPort') is not None:
            self.udp_port = m.get('UdpPort')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        if m.get('UsbRedirect') is not None:
            self.usb_redirect = m.get('UsbRedirect')
        if m.get('TaskFinished') is not None:
            self.task_finished = m.get('TaskFinished')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')
        return self


class DescribeClusterPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeClusterPolicyResponseBody = None,
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
            temp_model = DescribeClusterPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClustersRequest(TeaModel):
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


class DescribeClustersResponseBodyClusters(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
        status: str = None,
        nat_id: str = None,
        instance_count: int = None,
        create_time: str = None,
        nat_eip: str = None,
        security_group: str = None,
        name: str = None,
        domain_name: str = None,
        cluster_id: str = None,
    ):
        self.vpc_id = vpc_id
        self.status = status
        self.nat_id = nat_id
        self.instance_count = instance_count
        self.create_time = create_time
        self.nat_eip = nat_eip
        self.security_group = security_group
        self.name = name
        self.domain_name = domain_name
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.status is not None:
            result['Status'] = self.status
        if self.nat_id is not None:
            result['NatId'] = self.nat_id
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.nat_eip is not None:
            result['NatEip'] = self.nat_eip
        if self.security_group is not None:
            result['SecurityGroup'] = self.security_group
        if self.name is not None:
            result['Name'] = self.name
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('NatId') is not None:
            self.nat_id = m.get('NatId')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('NatEip') is not None:
            self.nat_eip = m.get('NatEip')
        if m.get('SecurityGroup') is not None:
            self.security_group = m.get('SecurityGroup')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeClustersResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        clusters: List[DescribeClustersResponseBodyClusters] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.clusters = clusters

    def validate(self):
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

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
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
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
        self.clusters = []
        if m.get('Clusters') is not None:
            for k in m.get('Clusters'):
                temp_model = DescribeClustersResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k))
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


class DescribeImagesRequest(TeaModel):
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


class DescribeImagesResponseBodyImages(TeaModel):
    def __init__(
        self,
        status: str = None,
        image_type: str = None,
        progress: str = None,
        size: int = None,
        create_time: str = None,
        name: str = None,
        image_id: str = None,
        product_code: str = None,
    ):
        self.status = status
        self.image_type = image_type
        self.progress = progress
        self.size = size
        self.create_time = create_time
        self.name = name
        self.image_id = image_id
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.size is not None:
            result['Size'] = self.size
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.name is not None:
            result['Name'] = self.name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class DescribeImagesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        images: List[DescribeImagesResponseBodyImages] = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.images = images

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

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
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
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
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = DescribeImagesResponseBodyImages()
                self.images.append(temp_model.from_map(k))
        return self


class DescribeImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeImagesResponseBody = None,
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
            temp_model = DescribeImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancePolicyRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        task_id: str = None,
        async_mode: bool = None,
    ):
        self.instance_id = instance_id
        self.task_id = task_id
        self.async_mode = async_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.async_mode is not None:
            result['AsyncMode'] = self.async_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('AsyncMode') is not None:
            self.async_mode = m.get('AsyncMode')
        return self


class DescribeInstancePolicyResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        request_id: str = None,
        task_finished: bool = None,
        visual_lossless: str = None,
        optimize_for_3d: str = None,
    ):
        self.task_id = task_id
        self.request_id = request_id
        self.task_finished = task_finished
        self.visual_lossless = visual_lossless
        self.optimize_for_3d = optimize_for_3d

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_finished is not None:
            result['TaskFinished'] = self.task_finished
        if self.visual_lossless is not None:
            result['VisualLossless'] = self.visual_lossless
        if self.optimize_for_3d is not None:
            result['OptimizeFor3d'] = self.optimize_for_3d
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskFinished') is not None:
            self.task_finished = m.get('TaskFinished')
        if m.get('VisualLossless') is not None:
            self.visual_lossless = m.get('VisualLossless')
        if m.get('OptimizeFor3d') is not None:
            self.optimize_for_3d = m.get('OptimizeFor3d')
        return self


class DescribeInstancePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstancePolicyResponseBody = None,
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
            temp_model = DescribeInstancePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        cluster_id: str = None,
        instance_id: str = None,
        user_uid: int = None,
        user_name: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.cluster_id = cluster_id
        self.instance_id = instance_id
        self.user_uid = user_uid
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_uid is not None:
            result['UserUid'] = self.user_uid
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserUid') is not None:
            self.user_uid = m.get('UserUid')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DescribeInstancesResponseBodyInstancesAppList(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_path: str = None,
        app_args: str = None,
    ):
        self.app_name = app_name
        self.app_path = app_path
        self.app_args = app_args

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_path is not None:
            result['AppPath'] = self.app_path
        if self.app_args is not None:
            result['AppArgs'] = self.app_args
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppPath') is not None:
            self.app_path = m.get('AppPath')
        if m.get('AppArgs') is not None:
            self.app_args = m.get('AppArgs')
        return self


class DescribeInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        status: str = None,
        work_mode: str = None,
        expire_time: str = None,
        create_time: str = None,
        stopped_mode: str = None,
        user_uid: int = None,
        instance_id: str = None,
        instance_type: str = None,
        domain_name: str = None,
        instance_charge_type: str = None,
        app_list: List[DescribeInstancesResponseBodyInstancesAppList] = None,
        max_bandwidth_in: int = None,
        is_bound_user: bool = None,
        max_bandwidth_out: int = None,
        name: str = None,
        user_name: str = None,
        image_id: str = None,
        cluster_id: str = None,
    ):
        self.status = status
        self.work_mode = work_mode
        self.expire_time = expire_time
        self.create_time = create_time
        self.stopped_mode = stopped_mode
        self.user_uid = user_uid
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.domain_name = domain_name
        self.instance_charge_type = instance_charge_type
        self.app_list = app_list
        self.max_bandwidth_in = max_bandwidth_in
        self.is_bound_user = is_bound_user
        self.max_bandwidth_out = max_bandwidth_out
        self.name = name
        self.user_name = user_name
        self.image_id = image_id
        self.cluster_id = cluster_id

    def validate(self):
        if self.app_list:
            for k in self.app_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.work_mode is not None:
            result['WorkMode'] = self.work_mode
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.stopped_mode is not None:
            result['StoppedMode'] = self.stopped_mode
        if self.user_uid is not None:
            result['UserUid'] = self.user_uid
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.instance_charge_type is not None:
            result['InstanceChargeType'] = self.instance_charge_type
        result['AppList'] = []
        if self.app_list is not None:
            for k in self.app_list:
                result['AppList'].append(k.to_map() if k else None)
        if self.max_bandwidth_in is not None:
            result['MaxBandwidthIn'] = self.max_bandwidth_in
        if self.is_bound_user is not None:
            result['IsBoundUser'] = self.is_bound_user
        if self.max_bandwidth_out is not None:
            result['MaxBandwidthOut'] = self.max_bandwidth_out
        if self.name is not None:
            result['Name'] = self.name
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WorkMode') is not None:
            self.work_mode = m.get('WorkMode')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('StoppedMode') is not None:
            self.stopped_mode = m.get('StoppedMode')
        if m.get('UserUid') is not None:
            self.user_uid = m.get('UserUid')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('InstanceChargeType') is not None:
            self.instance_charge_type = m.get('InstanceChargeType')
        self.app_list = []
        if m.get('AppList') is not None:
            for k in m.get('AppList'):
                temp_model = DescribeInstancesResponseBodyInstancesAppList()
                self.app_list.append(temp_model.from_map(k))
        if m.get('MaxBandwidthIn') is not None:
            self.max_bandwidth_in = m.get('MaxBandwidthIn')
        if m.get('IsBoundUser') is not None:
            self.is_bound_user = m.get('IsBoundUser')
        if m.get('MaxBandwidthOut') is not None:
            self.max_bandwidth_out = m.get('MaxBandwidthOut')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[DescribeInstancesResponseBodyInstances] = None,
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
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
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
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
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


class GetConnectTicketRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        app_name: str = None,
        user_name: str = None,
        password: str = None,
        task_id: str = None,
        async_mode: bool = None,
    ):
        self.instance_id = instance_id
        self.app_name = app_name
        self.user_name = user_name
        self.password = password
        self.task_id = task_id
        self.async_mode = async_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.password is not None:
            result['Password'] = self.password
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.async_mode is not None:
            result['AsyncMode'] = self.async_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('AsyncMode') is not None:
            self.async_mode = m.get('AsyncMode')
        return self


class GetConnectTicketResponseBody(TeaModel):
    def __init__(
        self,
        ticket: str = None,
        task_id: str = None,
        request_id: str = None,
        task_finished: bool = None,
    ):
        self.ticket = ticket
        self.task_id = task_id
        self.request_id = request_id
        self.task_finished = task_finished

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.ticket is not None:
            result['Ticket'] = self.ticket
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_finished is not None:
            result['TaskFinished'] = self.task_finished
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskFinished') is not None:
            self.task_finished = m.get('TaskFinished')
        return self


class GetConnectTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetConnectTicketResponseBody = None,
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
            temp_model = GetConnectTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IsUserAdminResponseBody(TeaModel):
    def __init__(
        self,
        is_admin: bool = None,
        request_id: str = None,
        is_allow: bool = None,
    ):
        self.is_admin = is_admin
        self.request_id = request_id
        self.is_allow = is_allow

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_admin is not None:
            result['IsAdmin'] = self.is_admin
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_allow is not None:
            result['IsAllow'] = self.is_allow
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsAdmin') is not None:
            self.is_admin = m.get('IsAdmin')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IsAllow') is not None:
            self.is_allow = m.get('IsAllow')
        return self


class IsUserAdminResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: IsUserAdminResponseBody = None,
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
            temp_model = IsUserAdminResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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


class SetClusterADDomainRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        domain_dns_ip: str = None,
        domain_name: str = None,
        domain_password: str = None,
        domain_admin: str = None,
        domain_delete: bool = None,
    ):
        self.cluster_id = cluster_id
        self.domain_dns_ip = domain_dns_ip
        self.domain_name = domain_name
        self.domain_password = domain_password
        self.domain_admin = domain_admin
        self.domain_delete = domain_delete

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.domain_dns_ip is not None:
            result['DomainDnsIp'] = self.domain_dns_ip
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.domain_password is not None:
            result['DomainPassword'] = self.domain_password
        if self.domain_admin is not None:
            result['DomainAdmin'] = self.domain_admin
        if self.domain_delete is not None:
            result['DomainDelete'] = self.domain_delete
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DomainDnsIp') is not None:
            self.domain_dns_ip = m.get('DomainDnsIp')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('DomainPassword') is not None:
            self.domain_password = m.get('DomainPassword')
        if m.get('DomainAdmin') is not None:
            self.domain_admin = m.get('DomainAdmin')
        if m.get('DomainDelete') is not None:
            self.domain_delete = m.get('DomainDelete')
        return self


class SetClusterADDomainResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        request_id: str = None,
    ):
        self.task_id = task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetClusterADDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetClusterADDomainResponseBody = None,
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
            temp_model = SetClusterADDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetClusterDnatRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        nat_id: str = None,
        nat_eip: str = None,
    ):
        self.cluster_id = cluster_id
        self.nat_id = nat_id
        self.nat_eip = nat_eip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.nat_id is not None:
            result['NatId'] = self.nat_id
        if self.nat_eip is not None:
            result['NatEip'] = self.nat_eip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('NatId') is not None:
            self.nat_id = m.get('NatId')
        if m.get('NatEip') is not None:
            self.nat_eip = m.get('NatEip')
        return self


class SetClusterDnatResponseBody(TeaModel):
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


class SetClusterDnatResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetClusterDnatResponseBody = None,
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
            temp_model = SetClusterDnatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetClusterNameRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        name: str = None,
    ):
        self.cluster_id = cluster_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class SetClusterNameResponseBody(TeaModel):
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


class SetClusterNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetClusterNameResponseBody = None,
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
            temp_model = SetClusterNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetClusterPolicyRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        usb_redirect: str = None,
        watermark: str = None,
        local_drive: str = None,
        clipboard: str = None,
        udp_port: str = None,
        domain_list: str = None,
        async_mode: bool = None,
    ):
        self.cluster_id = cluster_id
        self.usb_redirect = usb_redirect
        self.watermark = watermark
        self.local_drive = local_drive
        self.clipboard = clipboard
        self.udp_port = udp_port
        self.domain_list = domain_list
        self.async_mode = async_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.usb_redirect is not None:
            result['UsbRedirect'] = self.usb_redirect
        if self.watermark is not None:
            result['Watermark'] = self.watermark
        if self.local_drive is not None:
            result['LocalDrive'] = self.local_drive
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.udp_port is not None:
            result['UdpPort'] = self.udp_port
        if self.domain_list is not None:
            result['DomainList'] = self.domain_list
        if self.async_mode is not None:
            result['AsyncMode'] = self.async_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('UsbRedirect') is not None:
            self.usb_redirect = m.get('UsbRedirect')
        if m.get('Watermark') is not None:
            self.watermark = m.get('Watermark')
        if m.get('LocalDrive') is not None:
            self.local_drive = m.get('LocalDrive')
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('UdpPort') is not None:
            self.udp_port = m.get('UdpPort')
        if m.get('DomainList') is not None:
            self.domain_list = m.get('DomainList')
        if m.get('AsyncMode') is not None:
            self.async_mode = m.get('AsyncMode')
        return self


class SetClusterPolicyResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        request_id: str = None,
    ):
        self.task_id = task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetClusterPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetClusterPolicyResponseBody = None,
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
            temp_model = SetClusterPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetImageNameRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        name: str = None,
    ):
        self.image_id = image_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class SetImageNameResponseBody(TeaModel):
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


class SetImageNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetImageNameResponseBody = None,
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
            temp_model = SetImageNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetInstanceNameRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
    ):
        self.instance_id = instance_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class SetInstanceNameResponseBody(TeaModel):
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


class SetInstanceNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetInstanceNameResponseBody = None,
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
            temp_model = SetInstanceNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetInstancePolicyRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        visual_lossless: str = None,
        optimize_for_3d: str = None,
        async_mode: bool = None,
    ):
        self.instance_id = instance_id
        self.visual_lossless = visual_lossless
        self.optimize_for_3d = optimize_for_3d
        self.async_mode = async_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.visual_lossless is not None:
            result['VisualLossless'] = self.visual_lossless
        if self.optimize_for_3d is not None:
            result['OptimizeFor3d'] = self.optimize_for_3d
        if self.async_mode is not None:
            result['AsyncMode'] = self.async_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VisualLossless') is not None:
            self.visual_lossless = m.get('VisualLossless')
        if m.get('OptimizeFor3d') is not None:
            self.optimize_for_3d = m.get('OptimizeFor3d')
        if m.get('AsyncMode') is not None:
            self.async_mode = m.get('AsyncMode')
        return self


class SetInstancePolicyResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        request_id: str = None,
    ):
        self.task_id = task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetInstancePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetInstancePolicyResponseBody = None,
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
            temp_model = SetInstancePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetInstanceUserRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        user_uid: int = None,
        user_name: str = None,
    ):
        self.instance_id = instance_id
        self.user_uid = user_uid
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.user_uid is not None:
            result['UserUid'] = self.user_uid
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UserUid') is not None:
            self.user_uid = m.get('UserUid')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class SetInstanceUserResponseBody(TeaModel):
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


class SetInstanceUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetInstanceUserResponseBody = None,
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
            temp_model = SetInstanceUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class StartInstanceResponseBody(TeaModel):
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


class StartInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartInstanceResponseBody = None,
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
            temp_model = StartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class StopInstanceResponseBody(TeaModel):
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


class StopInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopInstanceResponseBody = None,
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
            temp_model = StopInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


