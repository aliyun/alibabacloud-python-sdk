# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class ListServiceInstanceLogsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        service_instances_logs: List[main_models.ListServiceInstanceLogsResponseBodyServiceInstancesLogs] = None,
    ):
        # The number of entries returned on each page.
        self.max_results = max_results
        # The token to retrieve the next page of results. If this parameter is empty, all results have been returned.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The logs of the service instance.
        self.service_instances_logs = service_instances_logs

    def validate(self):
        if self.service_instances_logs:
            for v1 in self.service_instances_logs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ServiceInstancesLogs'] = []
        if self.service_instances_logs is not None:
            for k1 in self.service_instances_logs:
                result['ServiceInstancesLogs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.service_instances_logs = []
        if m.get('ServiceInstancesLogs') is not None:
            for k1 in m.get('ServiceInstancesLogs'):
                temp_model = main_models.ListServiceInstanceLogsResponseBodyServiceInstancesLogs()
                self.service_instances_logs.append(temp_model.from_map(k1))

        return self

class ListServiceInstanceLogsResponseBodyServiceInstancesLogs(DaraModel):
    def __init__(
        self,
        compliance_pack_type: str = None,
        compliance_rule_name: str = None,
        content: str = None,
        log_type: str = None,
        resource_id: str = None,
        resource_type: str = None,
        source: str = None,
        status: str = None,
        timestamp: str = None,
    ):
        # The threat type from the compliance package. This parameter is returned only when Source is set to compliancePack. For example, VpcDataRisk indicates a data security check within a VPC.
        self.compliance_pack_type = compliance_pack_type
        # The name of the threat rule from the compliance package. This parameter is returned only when Source is set to compliancePack. For example, vpc-ecs-move-out-vpc indicates that an ECS instance was moved out of a VPC.
        self.compliance_rule_name = compliance_rule_name
        # The content of the log entry.
        self.content = content
        # The log type. Valid values:
        # 
        # - serviceInstance: Logs at the service instance level.
        # 
        # - resource: Logs at the ROS resource level.
        self.log_type = log_type
        # The ID of the associated resource.
        self.resource_id = resource_id
        # The resource type.
        self.resource_type = resource_type
        # The source of the log. Valid values:
        # 
        # - ros: Logs from ROS.
        # 
        # - computeNest: Logs from Compute Nest.
        # 
        # - application: Logs from the application in the instance.
        # 
        # - compliancePack: Logs from the compliance package of the instance.
        # 
        # - actionTrail: Logs from ActionTrail.
        self.source = source
        # The status of the event that the log records. Valid values:
        # 
        # - Creating: The instance is being created.
        # 
        # - Created: The instance is created.
        # 
        # - Deploying: The instance is being deployed.
        # 
        # - Deployed: The instance is deployed.
        # 
        # - DeployedFailed: The instance failed to be deployed.
        # 
        # - Expired: The instance has expired.
        # 
        # - ExtendSuccess: The instance is successfully renewed.
        # 
        # - Upgrading: The instance is being upgraded.
        # 
        # - UpgradeSuccess: The instance is successfully upgraded.
        self.status = status
        # The timestamp of the log entry.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_pack_type is not None:
            result['CompliancePackType'] = self.compliance_pack_type

        if self.compliance_rule_name is not None:
            result['ComplianceRuleName'] = self.compliance_rule_name

        if self.content is not None:
            result['Content'] = self.content

        if self.log_type is not None:
            result['LogType'] = self.log_type

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackType') is not None:
            self.compliance_pack_type = m.get('CompliancePackType')

        if m.get('ComplianceRuleName') is not None:
            self.compliance_rule_name = m.get('ComplianceRuleName')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

