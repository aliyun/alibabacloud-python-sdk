# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class GetGatewayResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetGatewayResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned. A value of 200 indicates that the request is successful.
        self.code = code
        # The information about the gateway.
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
            temp_model = main_models.GetGatewayResponseBodyData()
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

class GetGatewayResponseBodyData(DaraModel):
    def __init__(
        self,
        charge_type: str = None,
        elastic: bool = None,
        elastic_policy: main_models.GetGatewayResponseBodyDataElasticPolicy = None,
        elastic_replica: int = None,
        elastic_type: str = None,
        end_date: str = None,
        gateway_unique_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        instance_id: str = None,
        log_config_details: main_models.GetGatewayResponseBodyDataLogConfigDetails = None,
        mse_tag: str = None,
        name: str = None,
        primary_user: str = None,
        region: str = None,
        replica: int = None,
        resource_group_id: str = None,
        security_group: str = None,
        spec: str = None,
        status: int = None,
        status_desc: str = None,
        total_replica: int = None,
        vpc: str = None,
        vswitch: str = None,
        vswitch_2: str = None,
        xtrace_details: main_models.GetGatewayResponseBodyDataXtraceDetails = None,
    ):
        # The billing method, such as subscription or pay-as-you-go.
        self.charge_type = charge_type
        # Indicates whether auto scale-out is enabled.
        self.elastic = elastic
        # The auto scale-out policy.
        self.elastic_policy = elastic_policy
        # The number of replicas that are automatically scaled out.
        self.elastic_replica = elastic_replica
        # The type of auto scale-out. Valid value:
        # 
        # *   CronHPA: scale-out by time
        self.elastic_type = elastic_type
        # The time when the gateway expires.
        self.end_date = end_date
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The time when the gateway was created. The time is displayed in GMT. The time is the local time of the region in which the gateway resides.
        self.gmt_create = gmt_create
        # The time when the gateway was last modified.
        self.gmt_modified = gmt_modified
        # The ID of the gateway.
        self.id = id
        # The ID of the instance.
        self.instance_id = instance_id
        # The log configuration.
        self.log_config_details = log_config_details
        # The tag of the resource.
        self.mse_tag = mse_tag
        # The name of the gateway.
        self.name = name
        # The Alibaba Cloud account ID of the user who created the gateway.
        self.primary_user = primary_user
        # The region ID.
        self.region = region
        # The number of gateway replicas.
        self.replica = replica
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the security group.
        self.security_group = security_group
        # The specifications of the gateway.
        self.spec = spec
        # The status of the gateway. Valid values:
        # 
        # *   0: The gateway is being created.
        # *   1: The gateway fails to be created.
        # *   2: The gateway is running.
        # *   3: The gateway is changing.
        # *   4: The gateway is scaling in.
        # *   6: The gateway is scaling out.
        # *   8: The gateway is being deleted.
        # *   10: The gateway is restarting.
        # *   11: The gateway is being rebuilt.
        # *   12: The gateway is updating.
        # *   13: The gateway fails to be updated.
        self.status = status
        # The description of the status.
        self.status_desc = status_desc
        # The total number of replicas, including the number of replicas that are automatically scaled out.
        self.total_replica = total_replica
        # The ID of the VPC.
        self.vpc = vpc
        # The ID of the vSwitch.
        self.vswitch = vswitch
        # The ID of the secondary vSwitch.
        self.vswitch_2 = vswitch_2
        # The details of Tracing Analysis.
        self.xtrace_details = xtrace_details

    def validate(self):
        if self.elastic_policy:
            self.elastic_policy.validate()
        if self.log_config_details:
            self.log_config_details.validate()
        if self.xtrace_details:
            self.xtrace_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.elastic is not None:
            result['Elastic'] = self.elastic

        if self.elastic_policy is not None:
            result['ElasticPolicy'] = self.elastic_policy.to_map()

        if self.elastic_replica is not None:
            result['ElasticReplica'] = self.elastic_replica

        if self.elastic_type is not None:
            result['ElasticType'] = self.elastic_type

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.log_config_details is not None:
            result['LogConfigDetails'] = self.log_config_details.to_map()

        if self.mse_tag is not None:
            result['MseTag'] = self.mse_tag

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

        if self.security_group is not None:
            result['SecurityGroup'] = self.security_group

        if self.spec is not None:
            result['Spec'] = self.spec

        if self.status is not None:
            result['Status'] = self.status

        if self.status_desc is not None:
            result['StatusDesc'] = self.status_desc

        if self.total_replica is not None:
            result['TotalReplica'] = self.total_replica

        if self.vpc is not None:
            result['Vpc'] = self.vpc

        if self.vswitch is not None:
            result['Vswitch'] = self.vswitch

        if self.vswitch_2 is not None:
            result['Vswitch2'] = self.vswitch_2

        if self.xtrace_details is not None:
            result['XtraceDetails'] = self.xtrace_details.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Elastic') is not None:
            self.elastic = m.get('Elastic')

        if m.get('ElasticPolicy') is not None:
            temp_model = main_models.GetGatewayResponseBodyDataElasticPolicy()
            self.elastic_policy = temp_model.from_map(m.get('ElasticPolicy'))

        if m.get('ElasticReplica') is not None:
            self.elastic_replica = m.get('ElasticReplica')

        if m.get('ElasticType') is not None:
            self.elastic_type = m.get('ElasticType')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LogConfigDetails') is not None:
            temp_model = main_models.GetGatewayResponseBodyDataLogConfigDetails()
            self.log_config_details = temp_model.from_map(m.get('LogConfigDetails'))

        if m.get('MseTag') is not None:
            self.mse_tag = m.get('MseTag')

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

        if m.get('SecurityGroup') is not None:
            self.security_group = m.get('SecurityGroup')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusDesc') is not None:
            self.status_desc = m.get('StatusDesc')

        if m.get('TotalReplica') is not None:
            self.total_replica = m.get('TotalReplica')

        if m.get('Vpc') is not None:
            self.vpc = m.get('Vpc')

        if m.get('Vswitch') is not None:
            self.vswitch = m.get('Vswitch')

        if m.get('Vswitch2') is not None:
            self.vswitch_2 = m.get('Vswitch2')

        if m.get('XtraceDetails') is not None:
            temp_model = main_models.GetGatewayResponseBodyDataXtraceDetails()
            self.xtrace_details = temp_model.from_map(m.get('XtraceDetails'))

        return self

class GetGatewayResponseBodyDataXtraceDetails(DaraModel):
    def __init__(
        self,
        sample: int = None,
        trace_on: bool = None,
    ):
        # The sampling rate of Tracing Analysis.
        self.sample = sample
        # Indicates whether sampling by using Tracing Analysis is enabled.
        self.trace_on = trace_on

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sample is not None:
            result['Sample'] = self.sample

        if self.trace_on is not None:
            result['TraceOn'] = self.trace_on

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Sample') is not None:
            self.sample = m.get('Sample')

        if m.get('TraceOn') is not None:
            self.trace_on = m.get('TraceOn')

        return self

class GetGatewayResponseBodyDataLogConfigDetails(DaraModel):
    def __init__(
        self,
        log_enabled: bool = None,
        log_store_name: str = None,
        project_name: str = None,
    ):
        # Indicates whether Log Service is activated.
        self.log_enabled = log_enabled
        # The name of the Logstore.
        self.log_store_name = log_store_name
        # The name of the project.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_enabled is not None:
            result['LogEnabled'] = self.log_enabled

        if self.log_store_name is not None:
            result['LogStoreName'] = self.log_store_name

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogEnabled') is not None:
            self.log_enabled = m.get('LogEnabled')

        if m.get('LogStoreName') is not None:
            self.log_store_name = m.get('LogStoreName')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

class GetGatewayResponseBodyDataElasticPolicy(DaraModel):
    def __init__(
        self,
        elastic_type: str = None,
        max_replica: int = None,
        time_policy_list: List[main_models.GetGatewayResponseBodyDataElasticPolicyTimePolicyList] = None,
    ):
        # The type of auto scale-out. Valid value:
        # 
        # *   CronHPA: scale-out by time
        self.elastic_type = elastic_type
        # The maximum number of instances that are automatically scaled out. This parameter is used for horizontal scale-out.
        self.max_replica = max_replica
        # The policy of scale-out by time.
        self.time_policy_list = time_policy_list

    def validate(self):
        if self.time_policy_list:
            for v1 in self.time_policy_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.elastic_type is not None:
            result['ElasticType'] = self.elastic_type

        if self.max_replica is not None:
            result['MaxReplica'] = self.max_replica

        result['TimePolicyList'] = []
        if self.time_policy_list is not None:
            for k1 in self.time_policy_list:
                result['TimePolicyList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ElasticType') is not None:
            self.elastic_type = m.get('ElasticType')

        if m.get('MaxReplica') is not None:
            self.max_replica = m.get('MaxReplica')

        self.time_policy_list = []
        if m.get('TimePolicyList') is not None:
            for k1 in m.get('TimePolicyList'):
                temp_model = main_models.GetGatewayResponseBodyDataElasticPolicyTimePolicyList()
                self.time_policy_list.append(temp_model.from_map(k1))

        return self

class GetGatewayResponseBodyDataElasticPolicyTimePolicyList(DaraModel):
    def __init__(
        self,
        desired_replica: int = None,
        end_time: str = None,
        start_time: str = None,
    ):
        # The number of expected replicas.
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

