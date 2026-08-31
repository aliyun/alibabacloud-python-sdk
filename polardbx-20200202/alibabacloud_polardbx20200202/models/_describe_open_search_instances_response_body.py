# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeOpenSearchInstancesResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.DescribeOpenSearchInstancesResponseBodyAccessDeniedDetail = None,
        data: main_models.DescribeOpenSearchInstancesResponseBodyData = None,
        request_id: str = None,
    ):
        # The details of the access denial.
        self.access_denied_detail = access_denied_detail
        # The operation result.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.DescribeOpenSearchInstancesResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Data') is not None:
            temp_model = main_models.DescribeOpenSearchInstancesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeOpenSearchInstancesResponseBodyData(DaraModel):
    def __init__(
        self,
        instances: List[main_models.DescribeOpenSearchInstancesResponseBodyDataInstances] = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        total_number: int = None,
    ):
        # The cluster ID.
        self.instances = instances
        # The maximum number of entries per page for a paging query. Maximum value: 100. Default value: If you do not specify a value or the value is less than 10, the default value is 10. If the value is greater than 100, the default value is 100.
        self.max_results = max_results
        # The token for the next query.
        self.next_token = next_token
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The total number of entries.
        self.total_number = total_number

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_number is not None:
            result['TotalNumber'] = self.total_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.DescribeOpenSearchInstancesResponseBodyDataInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalNumber') is not None:
            self.total_number = m.get('TotalNumber')

        return self

class DescribeOpenSearchInstancesResponseBodyDataInstances(DaraModel):
    def __init__(
        self,
        availability_zone: str = None,
        charge_type: str = None,
        cpu: int = None,
        create_time: str = None,
        data_node_count: int = None,
        description: str = None,
        engine_version: str = None,
        instance_id: str = None,
        memory_gb: int = None,
        net_type: str = None,
        region_id: str = None,
        spec_display: str = None,
        status: str = None,
        storage_size_gb: int = None,
    ):
        # The zone.
        self.availability_zone = availability_zone
        # The billing method. Valid values:
        # * **PrePaid**: subscription.
        # * **PostPaid**: pay-as-you-go.
        self.charge_type = charge_type
        # The number of CPUs.
        self.cpu = cpu
        # The creation time.
        self.create_time = create_time
        # The number of data nodes.
        self.data_node_count = data_node_count
        # The instance description.
        self.description = description
        # The DPI engine version. Default value: 2.0.
        self.engine_version = engine_version
        # The instance ID.
        self.instance_id = instance_id
        # The memory size. Unit: GB.
        self.memory_gb = memory_gb
        # The network type of the connection string. Valid values:
        # * **Public**: public endpoint.
        # * **Private**: private endpoint.
        # * **Inner**: private endpoint (classic network).
        self.net_type = net_type
        # The region ID.
        self.region_id = region_id
        # The display name of the instance specifications.
        self.spec_display = spec_display
        # The instance status.
        self.status = status
        # The storage size of a single data node. Unit: GB.
        self.storage_size_gb = storage_size_gb

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.availability_zone is not None:
            result['AvailabilityZone'] = self.availability_zone

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_node_count is not None:
            result['DataNodeCount'] = self.data_node_count

        if self.description is not None:
            result['Description'] = self.description

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.memory_gb is not None:
            result['MemoryGB'] = self.memory_gb

        if self.net_type is not None:
            result['NetType'] = self.net_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.spec_display is not None:
            result['SpecDisplay'] = self.spec_display

        if self.status is not None:
            result['Status'] = self.status

        if self.storage_size_gb is not None:
            result['StorageSizeGB'] = self.storage_size_gb

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailabilityZone') is not None:
            self.availability_zone = m.get('AvailabilityZone')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataNodeCount') is not None:
            self.data_node_count = m.get('DataNodeCount')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MemoryGB') is not None:
            self.memory_gb = m.get('MemoryGB')

        if m.get('NetType') is not None:
            self.net_type = m.get('NetType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SpecDisplay') is not None:
            self.spec_display = m.get('SpecDisplay')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StorageSizeGB') is not None:
            self.storage_size_gb = m.get('StorageSizeGB')

        return self

class DescribeOpenSearchInstancesResponseBodyAccessDeniedDetail(DaraModel):
    def __init__(
        self,
        auth_action: str = None,
        auth_principal_display_name: str = None,
        auth_principal_owner_id: str = None,
        auth_principal_type: str = None,
        encoded_diagnostic_message: str = None,
        no_permission_type: str = None,
        policy_type: str = None,
    ):
        # The authentication action.
        self.auth_action = auth_action
        # The display name of the authentication principal.
        self.auth_principal_display_name = auth_principal_display_name
        # The owner ID of the authentication principal.
        self.auth_principal_owner_id = auth_principal_owner_id
        # The type of the authentication principal.
        self.auth_principal_type = auth_principal_type
        # The encoded diagnostic message.
        self.encoded_diagnostic_message = encoded_diagnostic_message
        # The type of the permission denial.
        self.no_permission_type = no_permission_type
        # The policy type.
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_action is not None:
            result['AuthAction'] = self.auth_action

        if self.auth_principal_display_name is not None:
            result['AuthPrincipalDisplayName'] = self.auth_principal_display_name

        if self.auth_principal_owner_id is not None:
            result['AuthPrincipalOwnerId'] = self.auth_principal_owner_id

        if self.auth_principal_type is not None:
            result['AuthPrincipalType'] = self.auth_principal_type

        if self.encoded_diagnostic_message is not None:
            result['EncodedDiagnosticMessage'] = self.encoded_diagnostic_message

        if self.no_permission_type is not None:
            result['NoPermissionType'] = self.no_permission_type

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthAction') is not None:
            self.auth_action = m.get('AuthAction')

        if m.get('AuthPrincipalDisplayName') is not None:
            self.auth_principal_display_name = m.get('AuthPrincipalDisplayName')

        if m.get('AuthPrincipalOwnerId') is not None:
            self.auth_principal_owner_id = m.get('AuthPrincipalOwnerId')

        if m.get('AuthPrincipalType') is not None:
            self.auth_principal_type = m.get('AuthPrincipalType')

        if m.get('EncodedDiagnosticMessage') is not None:
            self.encoded_diagnostic_message = m.get('EncodedDiagnosticMessage')

        if m.get('NoPermissionType') is not None:
            self.no_permission_type = m.get('NoPermissionType')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

